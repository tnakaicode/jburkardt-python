#! /usr/bin/env python3
#
def polynomial_conversion_test ( ):

#*****************************************************************************80
#
## polynomial_conversion_test() tests polynomial_conversion().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'polynomial_conversion_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polynomial_conversion().' )

  bernstein_to_legendre01_test ( )
  bernstein_to_legendre01_matrix_test ( )
  legendre01_to_bernstein_test ( )
  legendre01_to_bernstein_matrix_test ( )
  bernstein_legendre01_bernstein_test ( )

  bernstein_to_monomial_test ( )
  bernstein_to_monomial_matrix_test ( )
  monomial_to_bernstein_test ( )
  monomial_to_bernstein_matrix_test ( )
  bernstein_monomial_bernstein_test ( )

  chebyshev_to_monomial_test ( )
  monomial_to_chebyshev_test ( )
  chebyshev_monomial_chebyshev_test ( )

  gegenbauer_to_monomial_test ( )
  gegenbauer_to_monomial_matrix_test ( )
  monomial_to_gegenbauer_test ( )
  monomial_to_gegenbauer_matrix_test ( )
  gegenbauer_monomial_gegenbauer_test ( )

  hermite_to_monomial_test ( )
  hermite_to_monomial_matrix_test ( )
  monomial_to_hermite_test ( )
  monomial_to_hermite_matrix_test ( )
  hermite_monomial_hermite_test ( )

  laguerre_to_monomial_test ( )
  laguerre_to_monomial_matrix_test ( )
  monomial_to_laguerre_test ( )
  monomial_to_laguerre_matrix_test ( )
  laguerre_monomial_laguerre_test ( )

  legendre_to_monomial_test ( )
  legendre_to_monomial_matrix_test ( )
  monomial_to_legendre_test ( )
  monomial_to_legendre_matrix_test ( )
  legendre_monomial_legendre_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polynomial_conversion_test():' )
  print ( '  Normal end of execution.' )

  return

def bernstein_legendre01_bernstein_test ( ):

#*****************************************************************************80
#
## bernstein_legendre01_bernstein_test() tests accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'bernstein_legendre01_bernstein_test ( ):' )
  print ( '  Convert a polynomial from Bernstein form' )
  print ( '  to Legendre01 form and back.' )

  rng = default_rng ( )

  n = 10

  bcoef = rng.random ( n + 1 )
  lcoef = bernstein_to_legendre01 ( n, bcoef )
  bcoef2 = legendre01_to_bernstein ( n, lcoef )

  e = np.linalg.norm ( bcoef - bcoef2 )
  print ( '' )
  print ( '  L2 difference = ', e )

  return

def bernstein_monomial_bernstein_test ( ):

#*****************************************************************************80
#
## bernstein_monomial_bernstein_test() tests accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'bernstein_monomial_bernstein_test ( ):' )
  print ( '  Convert a polynomial from Bernstein form' )
  print ( '  to monomial form and back.' )

  rng = default_rng ( )

  n = 10

  bcoef = rng.random ( n + 1 )
  mcoef = bernstein_to_monomial ( n, bcoef )
  bcoef2 = monomial_to_bernstein ( n, mcoef )

  e = np.linalg.norm ( bcoef - bcoef2 )
  print ( '' )
  print ( '  L2 difference = ', e )

  return

def bernstein_to_legendre01 ( n, bcoef ):

#*****************************************************************************80
#
## bernstein_to_legendre01() converts from Bernstein to Legendre01 form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real bcoef(1:n+1): the Bernstein coefficients of the polynomial.
# 
#  Output:
#
#    real lcoef(1:n+1): the Legendre01 coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = bernstein_to_legendre01_matrix ( n )
#
#  Apply the transformation.
#
  lcoef = np.matmul ( A, bcoef )

  return lcoef

def bernstein_to_legendre01_test ( ):

#*****************************************************************************80
#
## bernstein_to_legendre01_test() tests bernstein_to_legendre01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'bernstein_to_legendre01_test ( ):' )
  print ( '  bernstein_to_legendre01() converts a' )
  print ( '  polynomial from Bernstein form' )
  print ( '  to Legendre01 form.' )

  nmax = 6

  print ( '' )
  print ( '           ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'P01%d    ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    bcoef = np.zeros ( n + 1 )
    bcoef[n] = 1.0
    lcoef = bernstein_to_monomial ( n, bcoef )
    print ( 'B%d(x) = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.3f' % ( lcoef[k] ), end = '' )
    print ( '' )

  return

def bernstein_to_legendre01_matrix ( n ):

#*****************************************************************************80
#
## bernstein_to_legendre01_matrix() returns the Bernstein-to-Legendre01 matrix.
#
#  Discussion:
#
#    The Legendre polynomials are often defined on [-1,+1], while the
#    Bernstein polynomials are defined on [0,1].  For this function,
#    the Legendre polynomials have been shifted to share the [0,1]
#    interval of definition.
#
#  Example:
#
#    bernstein_to_legendre01_matrix ( 5 ):
#
#    0.1667    0.1667    0.1667    0.1667    0.1667    0.1667
#   -0.3571   -0.2143   -0.0714    0.0714    0.2143    0.3571
#    0.2976   -0.0595   -0.2381   -0.2381   -0.0595    0.2976
#   -0.1389    0.1944    0.1111   -0.1111   -0.1944    0.1389
#    0.0357   -0.1071    0.0714    0.0714   -0.1071    0.0357
#   -0.0040    0.0198   -0.0397    0.0397   -0.0198    0.0040
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the maximum degree of the polynomials.
#
#  Output:
#
#    real A(N+1,N+1), the matrix.
#
  from scipy.special import comb
  import numpy as np

  a = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      for k in range ( 0, i + 1 ):
        a[i,j] = a[i,j] \
          + ( -1.0 ) ** ( i + k ) \
          * ( comb ( i, k ) ) ** 2 / comb ( n + i, j + k )
      a[i,j] = a[i,j] * comb ( n, j ) \
        * ( 2 * i + 1 ) / ( n + i + 1 )

  return a

def bernstein_to_legendre01_matrix_test ( ):

#*****************************************************************************80
#
## bernstein_to_legendre01_matrix_test() tests bernstein_to_legendre01_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'bernstein_to_legendre01_matrix_test ( ):' )
  print ( '  bernstein_to_legendre01_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from Bernstein form' )
  print ( '  to Legendre01 form.' )

  n = 4
  A = bernstein_to_legendre01_matrix ( n )
  print ( '' )
  print ( A )

  return

def bernstein_to_monomial ( n, bcoef ):

#*****************************************************************************80
#
## bernstein_to_monomial() converts from Bernstein to monomial form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real bcoef(1:n+1): the Bernstein coefficients of the polynomial.
# 
#  Output:
#
#    real mcoef(1:n+1): the monomial coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = bernstein_to_monomial_matrix ( n )
#
#  Apply the transformation.
#
  mcoef = np.matmul ( A, bcoef )

  return mcoef

def bernstein_to_monomial_test ( ):

#*****************************************************************************80
#
## bernstein_to_monomial_test() tests bernstein_to_monomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'bernstein_to_monomial_test ( ):' )
  print ( '  bernstein_to_monomial() converts a' )
  print ( '  polynomial from Bernstein form' )
  print ( '  to monomial form.' )

  nmax = 6

  print ( '' )
  print ( '           ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'X**%d    ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    bcoef = np.zeros ( n + 1 )
    bcoef[n] = 1.0
    mcoef = bernstein_to_monomial ( n, bcoef )
    print ( 'B%d(x) = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.3f' % ( mcoef[k] ), end = '' )
    print ( '' )

  return

def bernstein_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## bernstein_to_monomial_matrix() returns the Bernstein-to-Monomial matrix.
#
#  Discussion:
#
#    The Bernstein-to-Monomial matrix of degree N is an N+1xN+1 matrix A which can 
#    be used to transform the N+1 coefficients of a polynomial of degree N
#    from a vector B of Bernstein basis polynomial coefficients ((1-x)^n,...,x^n).
#    to a vector P of coefficients of the power basis (1,x,x^2,...,x^n).
#
#    If we are using N=4-th degree polynomials, the matrix has the form:
#
#      1  -4   6  -4  1
#      0   4 -12  12 -4
#      0   0   6 -12  6
#      0   0   0   4 -4
#      0   0   0   0  1
#
#   and a polynomial with the Bernstein basis representation
#     p(x) = 3/4 * b(4,1) + 1/2 b(4,2)
#   whose Bernstein coefficient vector is
#     B = ( 0, 3/4, 1/2, 0, 0 )
#   will have the Bernstein basis coefficients 
#     P = A * B = ( 0, 3, -6, 3, 0 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the degree of the polynomials.
#
#  Output:
#
#    real A(N+1,N+1), the matrix.
#
  from scipy.special import comb
  import numpy as np

  A = np.zeros ( [ n + 1, n + 1 ] )

  for j in range ( 0, n + 1 ):
    for i in range ( 0, j + 1 ):
      A[i,j] = ( -1 ) ** (j - i ) * comb ( n - i, j - i ) * comb ( n, i )

  return A

def bernstein_to_monomial_matrix_test ( ):

#*****************************************************************************80
#
## bernstein_to_monomial_matrix_test() tests bernstein_to_monomial_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'bernstein_to_monomial_matrix_test ( ):' )
  print ( '  bernstein_to_monomial_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from Bernstein form' )
  print ( '  to monomial form.' )

  n = 4
  A = bernstein_to_monomial_matrix ( n )
  print ( '' )
  print ( A )

  return

def chebyshev_monomial_chebyshev_test ( ):

#*****************************************************************************80
#
## chebyshev_monomial_chebyshev_test() tests accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'chebyshev_monomial_chebyshev_test ( ):' )
  print ( '  Convert a polynomial from Chebyshev form' )
  print ( '  to monomial form and back.' )

  rng = default_rng ( )

  n = 10

  ccoef = rng.random ( n + 1 )
  mcoef = chebyshev_to_monomial ( n, ccoef )
  ccoef2 = monomial_to_chebyshev ( n, mcoef )

  e = np.linalg.norm ( ccoef - ccoef2 )
  print ( '' )
  print ( '  L2 difference = ', e )

  return

def chebyshev_to_monomial ( n, ccoef ):

#*****************************************************************************80
#
## chebyshev_to_monomial() converts from Chebyshev to monomial form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2024
#
#  Author:
#
#    Original Fortran77 version by Fred Krogh.
#    This version by John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real ccoef(0:n): the Chebyshev coefficients of the polynomial.
# 
#  Output:
#
#    real mcoef(0:n): the monomial coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []

  tp = 1.0

  mcoef = np.zeros ( n + 1 )

  mcoef = ccoef.copy ( )

  for j in range ( 0, n - 1 ):
    for i in range ( n - 2, j - 1, -1 ):
      mcoef[i] = mcoef[i] - mcoef[i+2]
    mcoef[j+1] = 0.5 * mcoef[j+1]
    mcoef[j] = tp * mcoef[j]
    tp = 2.0 * tp

  mcoef[n] = tp * mcoef[n]
  if ( 0 < n ):
    mcoef[n-1] = tp * mcoef[n-1]

  return mcoef

def chebyshev_to_monomial_test ( ):

#*****************************************************************************80
#
## chebyshev_to_monomial_test() tests chebyshev_to_monomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'chebyshev_to_monomial_test ( ):' )
  print ( '  chebyshev_to_monomial() converts a' )
  print ( '  polynomial from Chebyshev form' )
  print ( '  to monomial form.' )

  nmax = 6

  print ( '' )
  print ( '           ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'X**%d    ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    ccoef = np.zeros ( n + 1 )
    ccoef[n] = 1.0
    mcoef = chebyshev_to_monomial ( n, ccoef )
    print ( 'T%d(x) = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.3f' % ( mcoef[k] ), end = '' )
    print ( '' )

  return

def chebyshev_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## chebyshev_to_monomial_matrix() converts Chebyshev T to monomial.
#
#  Example:
#
#    N = 11
#
#    1  .  -1    .    1    .   -1    .     1    .    -1
#    .  1   .   -3    .    5    .   -7     .    9     .
#    .  .   2    .   -8    .   18    .   -32    .    50
#    .  .   .    4    .  -20    .   56     . -120     .
#    .  .   .    .    8    .  -48    .   160    .  -400
#    .  .   .    .    .   16    . -112     .  432     .
#    .  .   .    .    .    .   32    .  -256    .  1120
#    .  .   .    .    .    .    .   64     . -576     .
#    .  .   .    .    .    .    .    .   128    . -1280
#    .  .   .    .    .    .    .    .     .  256     .
#    .  .   .    .    .    .    .    .     .    .   512
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is reducible.
#
#    A is lower triangular.
#
#    Each row of A sums to 1.
#
#    det ( A ) = 2^( (N-1) * (N-2) / 2 )
#
#    A is not normal: A' * A /= A * A'.
#
#    For I = 1:
#      LAMBDA(1) = 1
#    For 1 < I
#      LAMBDA(I) = 2^(I-2)
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of A.
#
#  Output:
#
#    real A(N,N): the matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  A[0,0] = 1.0

  if ( n == 1 ):
    return A

  A[1,1] = 1.0

  for j in range ( 2, n ):
    for i in range ( 0, n ):
      A[i,j] = - A[i,j-2]
    for i in range ( 1, n ):
      A[i,j] = A[i,j] + 2.0 * A[i-1,j-1]

  return A

def gegenbauer_monomial_gegenbauer_test ( ):

#*****************************************************************************80
#
## gegenbauer_monomial_hermite_test() tests accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'gegenbauer_monomial_gegenbauer_test ( ):' )
  print ( '  Convert a polynomial from Gegenbauer form' )
  print ( '  to monomial form and back.' )

  rng = default_rng ( )

  n = 10
  alpha = 0.5
  print ( '' )
  print ( '  Gegenbauer parameter alpha = ', alpha )

  gcoef = rng.random ( n + 1 )
  mcoef = gegenbauer_to_monomial ( n, alpha, gcoef )
  gcoef2 = monomial_to_gegenbauer ( n, alpha, mcoef )

  e = np.linalg.norm ( gcoef - gcoef2 )
  print ( '' )
  print ( '  L2 difference = ', e )

  return

def gegenbauer_to_monomial ( n, alpha, gcoef ):

#*****************************************************************************80
#
## gegenbauer_to_monomial() converts from Gegenbauer to monomial form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real alpha: the Gegenbauer parameter.
#
#    real gcoef(1:n+1): the Gegenbauer coefficients of the polynomial.
# 
#  Output:
#
#    real mcoef(1:n+1): the monomial coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = gegenbauer_to_monomial_matrix ( n + 1, alpha )
#
#  Apply the transformation.
#
  mcoef = np.matmul ( A, gcoef )

  return mcoef

def gegenbauer_to_monomial_test ( ):

#*****************************************************************************80
#
## gegenbauer_to_monomial_test() tests gegenbauer_to_monomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'gegenbauer_to_monomial_test ( ):' )
  print ( '  gegenbauer_to_monomial() converts a' )
  print ( '  polynomial from Gegenbauer form' )
  print ( '  to monomial form.' )

  nmax = 6
  alpha = 0.5

  print ( '' )
  print ( '  Gegenbauer parameter alpha = ', alpha )

  print ( '' )
  print ( '           ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'X**%d    ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    gcoef = np.zeros ( n + 1 )
    gcoef[n] = 1.0
    mcoef = gegenbauer_to_monomial ( n, alpha, gcoef )
    print ( 'C%d(x) = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.3f' % ( mcoef[k] ), end = '' )
    print ( '' )

  return

def gegenbauer_to_monomial_matrix_test ( ):

#*****************************************************************************80
#
## gegenbauer_to_monomial_matrix_test() tests gegenbauer_to_monomial_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'gegenbauer_to_monomial_matrix_test ( ):' )
  print ( '  gegenbauer_to_monomial_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from Gegenbauer form' )
  print ( '  to monomial form.' )

  n = 5
  alpha = 0.5
  A = gegenbauer_to_monomial_matrix ( n, alpha )
  print ( '' )
  print ( '  alpha = ', alpha )
  print ( A )

  return

def gegenbauer_to_monomial_matrix ( n, alpha ):

#*****************************************************************************80
#
## gegenbauer_to_monomial_matrix(): Gegenbauer to monomial conversion matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of A.
#
#    real alpha: the parameter.
#
#  Output:
#
#    real A(N,N): the matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  if ( n <= 0 ):
    return A

  A[0,0] = 1.0

  if ( n == 1 ):
    return A

  A[1,1] = 2.0 * alpha
#
#  Perform convex sum.
#  Translating "(n+1) C(n+1) = 2 (n+alpha) x C(n) - ( n + 2 alpha - 1 ) C(n-1)"
#  drove me nuts, between indexing at 1 rather than 0, and dealing with
#  the interpretation of "n+1", because I now face the rare "off by 2" error!
#
  for j in range ( 2, n ):
    nn = j - 1
    c1 = ( 2 * nn + 2 * alpha     ) / ( nn + 1 )
    c2 = (   - nn - 2 * alpha + 1 ) / ( nn + 1 )
    A[1:j+1,j] =              c1 * A[0:j,j-1]
    A[0:j-1,j] = A[0:j-1,j] + c2 * A[0:j-1,j-2]

  return A

def hermite_monomial_hermite_test ( ):

#*****************************************************************************80
#
## hermite_monomial_hermite_test() tests accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'hermite_monomial_hermite_test ( ):' )
  print ( '  Convert a polynomial from Hermite form' )
  print ( '  to monomial form and back.' )

  rng = default_rng ( )

  n = 10

  hcoef = rng.random ( n + 1 )
  mcoef = hermite_to_monomial ( n, hcoef )
  hcoef2 = monomial_to_hermite ( n, mcoef )

  e = np.linalg.norm ( hcoef - hcoef2 )
  print ( '' )
  print ( '  L2 difference = ', e )

  return

def hermite_to_monomial ( n, hcoef ):

#*****************************************************************************80
#
## hermite_to_monomial() converts from Hermite to monomial form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real hcoef(1:n+1): the Hermite coefficients of the polynomial.
# 
#  Output:
#
#    real mcoef(1:n+1): the monomial coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = hermite_to_monomial_matrix ( n + 1 )
#
#  Apply the transformation.
#
  mcoef = np.matmul ( A, hcoef )

  return mcoef

def hermite_to_monomial_test ( ):

#*****************************************************************************80
#
## hermite_to_monomial_test() tests hermite_to_monomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_to_monomial_test ( ):' )
  print ( '  hermite_to_monomial() converts a' )
  print ( '  polynomial from Hermite form' )
  print ( '  to monomial form.' )

  nmax = 6

  print ( '' )
  print ( '           ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'X**%d    ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    hcoef = np.zeros ( n + 1 )
    hcoef[n] = 1.0
    mcoef = hermite_to_monomial ( n, hcoef )
    print ( 'H%d(x) = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.3f' % ( mcoef[k] ), end = '' )
    print ( '' )

  return

def hermite_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## hermite_to_monomial_matrix() converts from Hermite to monomial form.
#
#  Example:
#
#      1   .   -2      .      12     .   -120     .   1680      .  -30240
#      .   2    .    -12       .   120      . -1680      .  30240       .
#      .   .    4      .     -48     .    720     . -13440      .  302400
#      .   .    .      8       .  -160      .  3360      . -80640       .
#      .   .    .      .      16     .   -480     .  13440      . -403200
#      .   .    .      .       .    32      . -1344      .  48384       .
#      .   .    .      .       .     .     64     .  -3584      .  161280
#      .   .    .      .       .     .      .   128      .  -9216       .
#      .   .    .      .       .     .      .     .    256      .  -23040
#      .   .    .      .       .     .      .     .      .    512       .
#      .   .    .      .       .     .      .     .      .      .    1024
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np
  
  A = np.zeros ( ( n, n ) )

  A[0,0] = 1.0

  if ( 1 < n ):

    A[1,1] = 2.0

    for j in range ( 2, n ):
      for i in range ( 0, n ):
        if ( i == 0 ):
          A[i,j] =                  - 2.0 * ( j - 1 ) * A[i,j-2]
        else:
          A[i,j] = 2.0 * A[i-1,j-1] - 2.0 * ( j - 1 ) * A[i,j-2]

  return A

def hermite_to_monomial_matrix_test ( ):

#*****************************************************************************80
#
## hermite_to_monomial_matrix_test() tests hermite_to_monomial_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_to_monomial_matrix_test ( ):' )
  print ( '  hermite_to_monomial_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from Hermite form' )
  print ( '  to monomial form.' )

  n = 5
  A = hermite_to_monomial_matrix ( n )
  print ( '' )
  print ( A )

  return

def laguerre_monomial_laguerre_test ( ):

#*****************************************************************************80
#
## laguerre_monomial_laguerre_test() tests accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'laguerre_monomial_laguerre_test ( ):' )
  print ( '  Convert a polynomial from Laguerre form' )
  print ( '  to monomial form and back.' )

  rng = default_rng ( )

  n = 10

  lcoef = rng.random ( n + 1 )
  mcoef = laguerre_to_monomial ( n, lcoef )
  lcoef2 = monomial_to_laguerre ( n, mcoef )

  e = np.linalg.norm ( lcoef - lcoef2 )
  print ( '' )
  print ( '  L2 difference = ', e )

  return

def laguerre_to_monomial ( n, lcoef ):

#*****************************************************************************80
#
## laguerre_to_monomial() converts from Laguerre to monomial form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real lcoef(1:n+1): the Laguerre coefficients of the polynomial.
# 
#  Output:
#
#    real mcoef(1:n+1): the monomial coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = laguerre_to_monomial_matrix ( n + 1 )
#
#  Apply the transformation.
#
  mcoef = np.matmul ( A, lcoef )

  return mcoef

def laguerre_to_monomial_test ( ):

#*****************************************************************************80
#
## laguerre_to_monomial_test() tests laguerre_to_monomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'laguerre_to_monomial_test ( ):' )
  print ( '  laguerre_to_monomial() converts a' )
  print ( '  polynomial from Laguerre form' )
  print ( '  to monomial form.' )

  nmax = 6

  print ( '' )
  print ( '           ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'X**%d    ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    lcoef = np.zeros ( n + 1 )
    lcoef[n] = 1.0
    mcoef = laguerre_to_monomial ( n, lcoef )
    print ( 'L%d(x) = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.3f' % ( mcoef[k] ), end = '' )
    print ( '' )

  return

def laguerre_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## laguerre_to_monomial_matrix() converts Laguerre to monomial form.
#
#  Example:
#
#    N = 8 (each column must be divided by the factor below it.)
#
#      1      1      2      6     24    120    720   5040
#      .     -1     -4    -18    -96   -600  -4320 -35280
#      .      .      1      9     72    600   5400  52920
#      .      .      .      1    -16   -200  -2400 -29400
#      .      .      .      .      1     25    450   7350
#      .      .      .      .      .     -1    -36   -882
#      .      .      .      .      .      .      1     49
#      .      .      .      .      .      .      .     -1
#
#     /1     /1     /2     /6    /24   /120   /720  /5040
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N): the matrix.
#
  import numpy as np

  A = np.zeros ( ( n, n ) )

  A[0,0] = 1.0

  if ( 1 < n ):

    A[0,1] = 1.0
    A[1,1] = -1.0

    if ( 2 < n ):

      for j in range ( 3, n + 1 ):
        for i in range ( 0, n ):
          if ( i == 0 ):
            A[i,j-1] = ( float ( 2 * j - 3 ) * A[i,j-2] \
                      +  float (   - j + 2 ) * A[i,j-3] ) \
                      /  float (     j - 1 )
          else:
            A[i,j-1] = ( float ( 2 * j - 3 ) * A[i,j-2] \
                      -  float (         1 ) * A[i-1,j-2] \
                      +  float (   - j + 2 ) * A[i,j-3] ) \
                      /  float (     j - 1 )

  return A

def laguerre_to_monomial_matrix_test ( ):

#*****************************************************************************80
#
## laguerre_to_monomial_matrix_test() tests laguerre_to_monomial_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'laguerre_to_monomial_matrix_test ( ):' )
  print ( '  laguerre_to_monomial_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from Laguerre form' )
  print ( '  to monomial form.' )

  n = 5
  A = laguerre_to_monomial_matrix ( n )
  print ( '' )
  print ( A )

  return

def legendre_monomial_legendre_test ( ):

#*****************************************************************************80
#
## legendre_monomial_legendre_test() tests accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'legendre_monomial_legendre_test ( ):' )
  print ( '  Convert a polynomial from Legendre form' )
  print ( '  to monomial form and back.' )

  rng = default_rng ( )

  n = 10

  lcoef = rng.random ( n + 1 )
  mcoef = legendre_to_monomial ( n, lcoef )
  lcoef2 = monomial_to_legendre ( n, mcoef )

  e = np.linalg.norm ( lcoef - lcoef2 )
  print ( '' )
  print ( '  L2 difference = ', e )

  return

def legendre_to_monomial ( n, lcoef ):

#*****************************************************************************80
#
## legendre_to_monomial() converts from Legendre to monomial form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real lcoef(1:n+1): the Legendre coefficients of the polynomial.
# 
#  Output:
#
#    real mcoef(1:n+1): the monomial coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = legendre_to_monomial_matrix ( n + 1 )
#
#  Apply the transformation.
#
  mcoef = np.matmul ( A, lcoef )

  return mcoef

def legendre_to_monomial_test ( ):

#*****************************************************************************80
#
## legendre_to_monomial_test() tests legendre_to_monomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'legendre_to_monomial_test ( ):' )
  print ( '  legendre_to_monomial() converts a' )
  print ( '  polynomial from Legendre form' )
  print ( '  to monomial form.' )

  nmax = 6

  print ( '' )
  print ( '           ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'X**%d    ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    lcoef = np.zeros ( n + 1 )
    lcoef[n] = 1.0
    mcoef = legendre_to_monomial ( n, lcoef )
    print ( 'P%d(x) = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.3f' % ( mcoef[k] ), end = '' )
    print ( '' )

  return

def legendre_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## legendre_to_monomial_matrix() converts from Legendre to monomial form.
#
#  Discussion:
#
#    If PL(x) is a linear combination of Legendre polynomials
#    with coefficients CL, then PM(x) is a linear combination of
#    monomials with coefficients CM = A * CL.
#    
#    The coefficients are ordered so the constant term is first.
#
#  Example:
#
#    N = 11 (each column must be divided by factor at bottom)
#
#     1    .    -1     .      3     .     -5      .      35     .   -63
#     .    1     .    -3      .    15      .    -25       .   315     .
#     .    .     3     .    -30     .    105      .   -1260     .  3465
#     .    .     .     5      .   -70      .    315       . -4620     .
#     .    .     .     .     35     .   -315      .    6930     .-30030
#     .    .     .     .      .    63      .   -693       . 18018     .
#     .    .     .     .      .     .    231      .  -12012     . 90090
#     .    .     .     .      .     .      .    429       .-25740     .
#     .    .     .     .      .     .      .      .    6435     -109395
#     .    .     .     .      .     .      .      .       . 12155     .
#     .    .     .     .      .     .      .      .       .     . 46189
#
#    /1   /1    /2    /2     /8    /8    /16    /16    /128  /128  /256
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( ( n, n ) )

  if ( n <= 0 ):
    return A

  A[0,0] = 1.0

  if ( n == 1 ):
    return A

  A[1,1] = 1.0

  if ( n == 2 ):
    return A

  for j in range ( 3, n + 1 ):
    for i in range ( 1, n + 1 ):
      if ( i == 1 ):
        A[i-1,j-1] = - ( j - 2 ) * A[i-1,j-3] \
                     / ( j - 1 )
      else:
        A[i-1,j-1] = ( ( 2 * j - 3 ) * A[i-2,j-2] \
                     + (   - j + 2 ) * A[i-1,j-3] ) \
                     / (     j - 1 )

  return A

def legendre_to_monomial_matrix_test ( ):

#*****************************************************************************80
#
## legendre_to_monomial_matrix_test() tests legendre_to_monomial_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'legendre_to_monomial_matrix_test ( ):' )
  print ( '  legendre_to_monomial_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from Legendre form' )
  print ( '  to monomial form.' )

  n = 5
  A = legendre_to_monomial_matrix ( n )
  print ( '' )
  print ( A )

  return

def legendre01_to_bernstein ( n, lcoef ):

#*****************************************************************************80
#
## legendre01_to_bernstein() converts from Legendre01 to Bernstein form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real lcoef(1:n+1): the Legendre01 coefficients of the polynomial.
# 
#  Output:
#
#    real bcoef(1:n+1): the Bernstein coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = legendre01_to_bernstein_matrix ( n )
#
#  Apply the transformation.
#
  bcoef = np.matmul ( A, lcoef )

  return bcoef

def legendre01_to_bernstein_test ( ):

#*****************************************************************************80
#
## legendre01_to_bernstein_test() tests legendre01_to_bernstein().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'legendre01_to_bernstein_test ( ):' )
  print ( '  legendre01_to_bernstein() converts a' )
  print ( '  polynomial from Legendre01 form' )
  print ( '  to Bernstein form.' )

  nmax = 6

  print ( '' )
  print ( '           ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'B%d(X)    ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    lcoef = np.zeros ( n + 1 )
    lcoef[n] = 1.0
    bcoef = legendre01_to_bernstein ( n, lcoef )
    print ( 'P01%d(x) = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.3f' % ( bcoef[k] ), end = '' )
    print ( '' )

  return

def legendre01_to_bernstein_matrix ( n ):

#*****************************************************************************80
#
## legendre01_to_bernstein_matrix() returns the Legendre01-to-Bernstein matrix.
#
#  Discussion:
#
#    The Legendre polynomials are often defined on [-1,+1], while the
#    Bernstein polynomials are defined on [0,1].  For this function,
#    the Legendre polynomials have been shifted to share the [0,1]
#    interval of definition.
#
#  Example:
#
#    legendre01_to_bernstein_matrix(5):
#
#    1.0000   -1.0000    1.0000   -1.0000    1.0000   -1.0000
#    1.0000   -0.6000   -0.2000    1.4000   -3.0000    5.0000
#    1.0000   -0.2000   -0.8000    0.8000    2.0000  -10.0000
#    1.0000    0.2000   -0.8000   -0.8000    2.0000   10.0000
#    1.0000    0.6000   -0.2000   -1.4000   -3.0000   -5.0000
#    1.0000    1.0000    1.0000    1.0000    1.0000    1.0000
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the maximum degree of the polynomials.
#
#  Output:
#
#    real A(N+1,N+1), the matrix.
#
  from scipy.special import comb
  import numpy as np

  a = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      for k in range ( max ( 0, i + j - n ), min ( i, j ) + 1 ):
        a[i,j] = a[i,j] \
          + ( -1.0 ) ** ( j + k ) \
          * ( comb ( j, k ) ) ** 2 * comb ( n - j, i - k )
      a[i,j] = a[i,j] / comb ( n, i )

  return a

def legendre01_to_bernstein_matrix_test ( ):

#*****************************************************************************80
#
## legendre01_to_bernstein_matrix_test() tests legendre01_to_bernstein_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'legendre01_to_bernstein_matrix_test ( ):' )
  print ( '  legendre01_to_bernstein_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from Legendre01 form' )
  print ( '  to Bernstein form.' )

  n = 5
  A = legendre01_to_bernstein_matrix ( n )
  print ( '' )
  print ( A )

  return

def monomial_to_bernstein ( n, mcoef ):

#*****************************************************************************80
#
## monomial_to_bernstein() converts from monomial to Bernstein form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real mcoef(1:n+1): the monomial coefficients of the polynomial.
# 
#  Output:
#
#    real bcoef(1:n+1): the Bernstein coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = monomial_to_bernstein_matrix ( n )
#
#  Apply the transformation.
#
  bcoef = np.matmul ( A, mcoef )

  return bcoef

def monomial_to_bernstein_test ( ):

#*****************************************************************************80
#
## monomial_to_bernstein_test() tests monomial_to_bernstein().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_bernstein_test ( ):' )
  print ( '  monomial_to_bernstein() converts a' )
  print ( '  polynomial from monomial form to ' )
  print ( '  Bernstein form.' )

  nmax = 6

  print ( '' )
  print ( '        ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'B%d(x)   ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    mcoef = np.zeros ( n + 1 )
    mcoef[n] = 1.0
    bcoef = monomial_to_bernstein ( n, mcoef )
    print ( 'X**%d = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.5f' % ( bcoef[k] ), end = '' )
    print ( '' )

  return

def monomial_to_bernstein_matrix ( n ):

#*****************************************************************************80
#
## monomial_to_bernstein_matrix() returns the Monomial-to-Bernstein matrix.
#
#  Discussion:
#
#    The Monomial-to-Bernstein matrix of degree N is an N+1xN+1 matrix A which can 
#    be used to transform the N+1 coefficients of a polynomial of degree N
#    from a vector P of coefficients of the power basis (1,x,x^2,...,x^n)
#    to a vector B of Bernstein basis polynomial coefficients ((1-x)^n,...,x^n).
#
#    If we are using N=4-th degree polynomials, the matrix has the form:
#
#          1   1    1    1   1
#          0  1/4  1/2  3/4  1
#      A = 0   0   1/6  1/2  1
#          0   0    0   1/4  1
#          0   0    0    0   1
#
#   and a polynomial 
#     p(x) = 3x - 6x^2 + 3x^3
#   whose power coefficient vector is
#     P = ( 0, 3, -6, 3, 0 )
#   will have the Bernstein basis coefficients 
#     B = A * P = ( 0, 3/4, 1/2, 0, 0 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the degree of the polynomials.
#
#  Output:
#
#    real A[0:N,0:N], the Monomial-to-Bernstein matrix.
#
  from scipy.special import comb
  import numpy as np

  A = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, i + 1 ):
      A[n-i,n-j] = comb ( i, j ) / comb ( n, j )

  return A

def monomial_to_bernstein_matrix_test ( ):

#*****************************************************************************80
#
## monomial_to_bernstein_matrix_test() tests monomial_to_bernstein_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_bernstein_matrix_test ( ):' )
  print ( '  monomial_to_bernstein_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from monomial form' )
  print ( '  to Bernstein form.' )

  n = 4
  A = monomial_to_bernstein_matrix ( n )
  print ( '' )
  print ( A )

  return

def monomial_to_chebyshev ( n, mcoef ):

#*****************************************************************************80
#
## monomial_to_chebyshev() converts from monomial to Chebyshev form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2024
#
#  Author:
#
#    Original Fortran77 version by Fred Krogh.
#    This version by John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real mcoef(0:n): the monomial coefficients of the polynomial.
# 
#  Output:
#
#    real ccoef(0:n): the Chebyshev coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []

  ccoef = np.zeros ( n + 1 )

  ccoef = mcoef.copy ( )

  tp = 0.5 ** ( n - 1 )
  ccoef[n] = tp * ccoef[n]

  if ( n == 0 ):
    return ccoef

  ccoef[n-1] = tp * ccoef[n-1]
  for j in range ( n - 2, -1, -1 ):
    tp = 2.0 * tp
    ccoef[j] = tp * ccoef[j]
    ccoef[j+1] = 2.0 * ccoef[j+1]
    for i in range ( j, n - 1 ):
      ccoef[i] = ccoef[i] + ccoef[i+2]

  return ccoef

def monomial_to_chebyshev_test ( ):

#*****************************************************************************80
#
## monomial_to_chebyshev_test() tests monomial_to_chebyshev().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_chebyshev_test ( ):' )
  print ( '  monomial_to_chebyshev() converts a' )
  print ( '  polynomial from monomial form to ' )
  print ( '  Chebyshev form.' )

  nmax = 6

  print ( '' )
  print ( '        ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'T%d(x)   ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    mcoef = np.zeros ( n + 1 )
    mcoef[n] = 1.0
    ccoef = monomial_to_chebyshev ( n, mcoef )
    print ( 'X**%d = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.5f' % ( ccoef[k] ), end = '' )
    print ( '' )

  return

def monomial_to_chebyshev_matrix ( n ):

#*****************************************************************************80
#
## monomial_to_chebyshev_matrix() converts a monomial to a Chebyshev T polynomial.
#
#  Example:
#
#    N = 11
#    Each column must be divided by the divisor below it.
#
#      1   .   1   .   3   .  10   .   35    .  126
#      .   1   .   3   .  10   .  35    .  126    .
#      .   .   1   .   4   .  15   .   56    .  210
#      .   .   .   1   .   5   .  21    .   84    .
#      .   .   .   .   1   .   6   .   28    .  120
#      .   .   .   .   .   1   .   7    .   36    .
#      .   .   .   .   .   .   1   .    8    .   45
#      .   .   .   .   .   .   .   1    .    9    .
#      .   .   .   .   .   .   .   .    1    .   10
#      .   .   .   .   .   .   .   .    .    1    .
#      .   .   .   .   .   .   .   .    .    .    1  
#     /1  /1  /2  /4  /8 /16 /32 /64 /128 /256 /512 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of A.
#
#  Output:
#
#    real A(N,N): the matrix.
#
  import numpy as np

  A = np.zeros ( ( n, n ) )

  A[0,0] = 1.0

  if ( 1 < n ):

    A[1,1] = 1.0

    if ( 2 < n ):

      for j in range ( 2, n ):
        for i in range ( 0, n ):
          if ( i == 0 ):
            A[i,j] =                      A[i+1,j-1]   / 2.0
          elif ( i == 1 ):
            A[i,j] = ( 2.0 * A[i-1,j-1] + A[i+1,j-1] ) / 2.0
          elif ( i < n - 1 ):
            A[i,j] = (       A[i-1,j-1] + A[i+1,j-1] ) / 2.0
          else:
            A[i,j] =         A[i-1,j-1]                / 2.0

  return A

def monomial_to_gegenbauer ( n, alpha, mcoef ):

#*****************************************************************************80
#
## monomial_to_gegenbauer() converts from monomial to Gegenbauer form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real alpha: the Gegenbauer parameter.
#
#    real mcoef(1:n+1): the monomial coefficients of the polynomial.
# 
#  Output:
#
#    real gcoef(1:n+1): the Gegenbauer coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = monomial_to_gegenbauer_matrix ( n + 1, alpha )
#
#  Apply the transformation.
#
  gcoef = np.matmul ( A, mcoef )

  return gcoef

def monomial_to_gegenbauer_test ( ):

#*****************************************************************************80
#
## monomial_to_gegenbauer_test() tests monomial_to_gegenbauer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_gegenbauer_test ( ):' )
  print ( '  monomial_to_gegenbauer() converts a' )
  print ( '  polynomial from monomial form to ' )
  print ( '  Gegenbauer form.' )

  nmax = 6
  alpha = 0.5
  print ( '' )
  print ( '  Gegenbauer parameter alpha = ', alpha )

  print ( '' )
  print ( '        ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'C%d(x)   ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    mcoef = np.zeros ( n + 1 )
    mcoef[n] = 1.0
    gcoef = monomial_to_gegenbauer ( n, alpha, mcoef )
    print ( 'X**%d = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.5f' % ( gcoef[k] ), end = '' )
    print ( '' )

  return

def monomial_to_gegenbauer_matrix ( n, alpha ):

#*****************************************************************************80
#
## monomial_to_gegenbauer_matrix(): Monomial to Gegenbauer conversion matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dae San Kim, Taekyun Kim, Soog-Hoon Rim,
#    Some identities involving Gegenbauer polynomials.
#    Advances in Difference Equations,
#    Volume 2012, Number 19, 19 December 2012.
#
#  Input:
#
#    integer N: the order of A.
#
#    real alpha: the parameter.
#
#  Output:
#
#    real A(N,N): the matrix.
#
  from math import factorial
  from math import gamma
  import numpy as np

  A = np.zeros ( [ n, n ] )

  if ( n <= 0 ):
    return A

  for j in range ( 0, n ):
    ilo = ( j % 2 )
    for i in range ( ilo, j + 1, 2 ):
      top = ( i + alpha ) * factorial ( j ) * gamma ( alpha )
      bot = 2**j * factorial ( ( j - i ) // 2 ) \
        * gamma ( ( j + i ) / 2 + alpha + 1.0 )
      A[i,j] = top / bot

  return A

def monomial_to_gegenbauer_matrix_test ( ):

#*****************************************************************************80
#
## monomial_to_gegenbauer_matrix_test() tests monomial_to_gegenbauer_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_gegenbauer_matrix_test ( ):' )
  print ( '  monomial_to_gegenbauer_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from monomial form' )
  print ( '  to Gegenbauer form.' )

  n = 4
  alpha = 0.5
  print ( '' )
  print ( '  Gegenbauer parameter alpha = ', alpha )

  A = monomial_to_gegenbauer_matrix ( n, alpha )
  print ( '' )
  print ( A )

  return

def monomial_to_hermite ( n, mcoef ):

#*****************************************************************************80
#
## monomial_to_hermite() converts from monomial to Hermite form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real mcoef(1:n+1): the monomial coefficients of the polynomial.
# 
#  Output:
#
#    real hcoef(1:n+1): the Hermite coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = monomial_to_hermite_matrix ( n + 1 )
#
#  Apply the transformation.
#
  hcoef = np.matmul ( A, mcoef )

  return hcoef

def monomial_to_hermite_test ( ):

#*****************************************************************************80
#
## monomial_to_hermite_test() tests monomial_to_hermite().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_hermite_test ( ):' )
  print ( '  monomial_to_hermite() converts a' )
  print ( '  polynomial from monomial form to ' )
  print ( '  Hermite form.' )

  nmax = 6

  print ( '' )
  print ( '        ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'H%d(x)   ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    mcoef = np.zeros ( n + 1 )
    mcoef[n] = 1.0
    hcoef = monomial_to_hermite ( n, mcoef )
    print ( 'X**%d = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.5f' % ( hcoef[k] ), end = '' )
    print ( '' )

  return

def monomial_to_hermite_matrix ( n ):

#*****************************************************************************80
#
## monomial_to_hermite_matrix() converts from monomial to Hermite form.
#
#  Example:
#
#    N = 11 (each column must be divided by the factor below it)
#
#    1     .     2     .    12     .   120     .  1680     . 30240
#    .     1     .     6     .    60     .   840     . 15120     .
#    .     .     1     .    12     .   180     .  3360     . 75600
#    .     .     .     1     .    20     .   420     . 10080     .
#    .     .     .     .     1     .    30     .   840     . 25200
#    .     .     .     .     .     1     .    42     .  1512     .
#    .     .     .     .     .     .     1     .    56     .  2520
#    .     .     .     .     .     .     .     1     .    72     .
#    .     .     .     .     .     .     .     .     1     .    90
#    .     .     .     .     .     .     .     .     .     1     .
#    .     .     .     .     .     .     .     .     .     .     1
#
#   /1    /2    /4    /8   /16   /32   /64  /128  /256  /512 /1024
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( ( n, n ) )

  A[0,0] = 1.0

  if ( 1 < n ):

    A[1,1] = 0.5

    if ( 2 < n ):

      for j in range ( 2, n ):
        for i in range ( 0, n ):
          if ( i == 0 ):
            A[i,j] = ( float ( j - 1 ) * A[i,j-2]              ) / 2.0
          else:
            A[i,j] = ( float ( j - 1 ) * A[i,j-2] + A[i-1,j-1] ) / 2.0

  return A

def monomial_to_hermite_matrix_test ( ):

#*****************************************************************************80
#
## monomial_to_hermite_matrix_test() tests monomial_to_hermite_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_hermite_matrix_test ( ):' )
  print ( '  monomial_to_hermite_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from monomial form' )
  print ( '  to Hermite form.' )

  n = 4
  A = monomial_to_hermite_matrix ( n )
  print ( '' )
  print ( A )

  return

def monomial_to_laguerre ( n, mcoef ):

#*****************************************************************************80
#
## monomial_to_laguerre() converts from monomial to Laguerre form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real mcoef(1:n+1): the monomial coefficients of the polynomial.
# 
#  Output:
#
#    real lcoef(1:n+1): the Laguerre coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = monomial_to_laguerre_matrix ( n + 1 )
#
#  Apply the transformation.
#
  lcoef = np.matmul ( A, mcoef )

  return lcoef

def monomial_to_laguerre_test ( ):

#*****************************************************************************80
#
## monomial_to_laguerre_test() tests monomial_to_laguerre().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_laguerre_test ( ):' )
  print ( '  monomial_to_laguerre() converts a' )
  print ( '  polynomial from monomial form to ' )
  print ( '  Laguerre form.' )

  nmax = 6

  print ( '' )
  print ( '        ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'L%d(x)   ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    mcoef = np.zeros ( n + 1 )
    mcoef[n] = 1.0
    lcoef = monomial_to_laguerre ( n, mcoef )
    print ( 'X**%d = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.1f' % ( lcoef[k] ), end = '' )
    print ( '' )

  return

def monomial_to_laguerre_matrix ( n ):

#*****************************************************************************80
#
## monomial_to_laguerre_matrix() converts from monomial to Laguerre form.
#
#  Example:
#
#    N = 9
#
#        1       1       2       6      24     120     720    5040    40320
#        .      -1      -4     -18     -96    -600   -4320  -35280  -322560
#        .       .       2      18     144    1200   10800  105840  1128960
#        .       .       .      -6     -96   -1200  -14400 -176400 -2257920
#        .       .       .       .      24     600   10800  176400  2822400
#        .       .       .       .       .    -120   -4320 -105840 -2257920
#        .       .       .       .       .       .     720   35280  1128960
#        .       .       .       .       .       .       .   -5040  -322560
#        .       .       .       .       .       .       .       .    40320
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of A.
#
#  Output:
#
#    real A(N,N): the matrix.
#
  import numpy as np

  A = np.zeros ( ( n, n ) )

  A[0,0] = 1.0

  if ( 1 < n ):

    A[0,1] = 1.0
    A[1,1] = -1.0

    if ( 2 < n ):
      
      for j in range ( 2, n ):
        for i in range ( 0, n ):

          if ( i == 0 ):
            A[i,j] = float ( j ) * ( A[i,j-1]              )
          else:
            A[i,j] = float ( j ) * ( A[i,j-1] - A[i-1,j-1] )

  return A

def monomial_to_laguerre_matrix_test ( ):

#*****************************************************************************80
#
## monomial_to_laguerre_matrix_test() tests monomial_to_laguerre_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_laguerre_matrix_test ( ):' )
  print ( '  monomial_to_laguerre_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from monomial form' )
  print ( '  to Laguerre form.' )

  n = 4
  A = monomial_to_laguerre_matrix ( n )
  print ( '' )
  print ( A )

  return

def monomial_to_legendre ( n, mcoef ):

#*****************************************************************************80
#
## monomial_to_legendre() converts from monomial to Legendre form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2024
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer n: the order of the polynomial.
#
#    real mcoef(1:n+1): the monomial coefficients of the polynomial.
# 
#  Output:
#
#    real lcoef(1:n+1): the Legendre coefficients of the polynomial.
#
  import numpy as np

  if ( n < 0 ):
    return []
#
#  Get the matrix.
#
  A = monomial_to_legendre_matrix ( n + 1 )
#
#  Apply the transformation.
#
  lcoef = np.matmul ( A, mcoef )

  return lcoef

def monomial_to_legendre_test ( ):

#*****************************************************************************80
#
## monomial_to_legendre_test() tests monomial_to_legendre().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_legendre_test ( ):' )
  print ( '  monomial_to_legendre() converts a' )
  print ( '  polynomial from monomial form to ' )
  print ( '  Legendre form.' )

  nmax = 6

  print ( '' )
  print ( '        ', end = '' )
  for k in range ( 0, nmax + 1 ):
    print ( 'P%d(x)   ' % ( k ), end = '' )
  print ( '' )
  print ( '' )
  for n in range ( 0, nmax + 1 ):
    mcoef = np.zeros ( n + 1 )
    mcoef[n] = 1.0
    lcoef = monomial_to_legendre ( n, mcoef )
    print ( 'X**%d = ' % ( n ), end = '' )
    for k in range ( 0, n + 1 ):
      print ( '%8.5f' % ( lcoef[k] ), end = '' )
    print ( '' )

  return

def monomial_to_legendre_matrix ( n ):

#*****************************************************************************80
#
## monomial_to_legendre_matrix(): convert monomial to Legendre basis.
#
#  Discussion:
#
#    If PM(x) is a linear combination of monomials
#    with coefficients CM, then PL(x) is a linear combination of
#    Legendre polynomials with coefficients CL = A * CM.
#    
#    The coefficients are ordered such that
#    the constant term is first.
#
#  Example:
#
#    N = 11 (each column must be divided by the underlying factor).
#
#       1     .      1     .      7     .    33    .   715    . 4199
#       .     1      .     3      .    27     .  143     . 3315    .
#       .     .      2     .     20     .   110    .  2600    .16150
#       .     .      .     2      .    28     .  182     . 4760    .
#       .     .      .     .      8     .    72    .  2160    .15504
#       .     .      .     .      .     8     .   88     . 2992    .
#       .     .      .     .      .     .    16    .   832    . 7904
#       .     .      .     .      .     .     .   16     .  960    .
#       .     .      .     .      .     .     .    .   128    . 2176
#       .     .      .     .      .     .     .    .     .  128    .
#       .     .      .     .      .     .     .    .     .    .  256
#
#      /1    /1     /3    /5    /35   /63  /231 /429 /6435/12155/46189  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt 
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( ( n, n ) )

  A[0,0] = 1.0

  if ( 1 < n ):

    A[1,1] = 1.0

    if ( 2 < n ):

      for j in range ( 2, n ):
        for i in range ( 0, n ):

          if ( i == 0 ):

            A[i,j] = (     i + 1 ) * A[i+1,j-1] / float ( 2 * i + 3 )

          elif ( i < n - 1 ):

            A[i,j] = (     i     ) * A[i-1,j-1] / float ( 2 * i - 1 ) \
                   + (     i + 1 ) * A[i+1,j-1] / float ( 2 * i + 3 )

          else:

            A[i,j] = (     i     ) * A[i-1,j-1] / float ( 2 * i - 1 )

  return A

def monomial_to_legendre_matrix_test ( ):

#*****************************************************************************80
#
## monomial_to_legendre_matrix_test() tests monomial_to_legendre_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'monomial_to_legendre_matrix_test ( ):' )
  print ( '  monomial_to_legendre_matrix() returns the matrix which' )
  print ( '  maps polynomial coefficients from monomial form' )
  print ( '  to Legendre form.' )

  n = 4
  A = monomial_to_legendre_matrix ( n )
  print ( '' )
  print ( A )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  polynomial_conversion_test ( )
  timestamp ( )

