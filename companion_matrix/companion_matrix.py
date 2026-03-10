#! /usr/bin/env python3
#
def companion_matrix_test ( ):

#*****************************************************************************80
#
## companion_matrix_test() tests companion_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'companion_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  companion_matrix() computes the companion matrix' )
  print ( '  of a polynomial, in various bases.' )

  companion_chebyshev_test ( )
  companion_gegenbauer_test ( )
  companion_hermite_test ( )
  companion_laguerre_test ( )
  companion_legendre_test ( )
  companion_monomial_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'companion_matrix_test():' )
  print ( '  Normal end of execution.' )

  return

def companion_chebyshev ( p ):

#*****************************************************************************80
#
## companion_chebyshev() returns the Chebyshev basis companion matrix for a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Boyd,
#    Solving Transcendental Equations,
#    The Chebyshev Polynomial Proxy and other Numerical Rootfinders,
#    Perturbation Series, and Oracles,
#    SIAM, 2014,
#    ISBN: 978-1-611973-51-8,
#    LC: QA:353.T7B69
#
#  Input:
#
#    real p(n+1): the polynomial coefficients, in order of increasing degree.
#
#  Output:
#
#    real A(n,n): the companion matrix.
#
  import numpy as np

  np1 = len ( p )
  n = np1 - 1

  A = np.zeros ( [ n, n ] )

  A[0,1] = 1.0

  for i in range ( 1, n - 1 ):
    A[i,i-1] = 0.5
    A[i,i+1] = 0.5

  for j in range ( 0, n ):
    A[n-1,j] = - 0.5 * p[j] / p[n]

  A[n-1,n-2] = A[n-1,n-2] + 0.5

  return A

def companion_chebyshev_test ( ):

#*****************************************************************************80
#
## companion_chebyshev_test() tests companion_chebyshev().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.polynomial.polynomial import polyroots
  from scipy.linalg import eigvals
  import numpy as np

  print ( '' )
  print ( 'companion_chebyshev_test():' )
  print ( '  companion_chebyshev() computes the companion matrix' )
  print ( '  of a polynomial p(x) in the Chebyshev basis.' )

  p = np.array ( [ 6.0, 5.0, 4.0, 3.0, 2.0, 1.0 ] )

  polynomial_chebyshev_print ( p, '  p(x)' )
#
#  Compute monomial form so we can get roots directly.
#
  n = len ( p )
  A = chebyshev_to_monomial_matrix ( n )
  q = np.matmul ( A, p )
  polynomial_monomial_print ( q, '  Monomial q(x)' )
  r1 = polyroots ( q )
  print ( '' )
  print ( '  Roots of q(x):' )
  print ( r1 )

  A = companion_chebyshev ( p )

  print ( '' )
  print ( '  Chebyshev companion matrix A(p):' )

  print ( A )

  r = eigvals ( A )
  print ( '' )
  print ( '  Eigenvalues of A(p):' )
  print ( r )

  return

def companion_gegenbauer ( p, alpha ):

#*****************************************************************************80
#
## companion_gegenbauer() returns the Gegenbauer companion matrix for a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Boyd,
#    Solving Transcendental Equations,
#    The Chebyshev Polynomial Proxy and other Numerical Rootfinders,
#    Perturbation Series, and Oracles,
#    SIAM, 2014,
#    ISBN: 978-1-611973-51-8,
#    LC: QA:353.T7B69
#
#  Input:
#
#    real p(n+1): the polynomial coefficients, in order of increasing degree.
#
#    real alpha: the Gegenbauer parameter.
#
#  Output:
#
#    real A(n,n): the companion matrix.
#
  import numpy as np

  np1 = len ( p )
  n = np1 - 1

  A = np.zeros ( [ n, n ] )

  A[0,1] = 0.5 / alpha

  for i in range ( 1, n - 1 ):
    A[i,i-1] = 0.5 * ( i + 2 * alpha - 1 ) / ( i + alpha )
    A[i,i+1] = 0.5 * ( i             + 1 ) / ( i + alpha )

  for j in range ( 0, n ):
    A[n-1,j] = - 0.5 * p[j] * n / ( n - 1 + alpha ) / p[n]

  A[n-1,n-2] = A[n-1,n-2] + 0.5 * ( n - 2 + 2 * alpha ) / ( n - 1 + alpha )

  return A

def companion_gegenbauer_test ( ):

#*****************************************************************************80
#
## companion_gegenbauer_test() tests companion_gegenbauer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.polynomial.polynomial import polyroots
  from scipy.linalg import eigvals
  import numpy as np

  print ( '' )
  print ( 'companion_gegenbauer_test():' )
  print ( '  companion_gegenbauer() computes the companion matrix' )
  print ( '  of a polynomial p(x) in the Gegenbauer basis.' )

  for alpha in [ 0.5, 1.0 ]:

    print ( '' )
    print ( '  alpha = ', alpha )

    p = np.array ( [ 6.0, 5.0, 4.0, 3.0, 2.0, 1.0 ] )

    polynomial_gegenbauer_print ( p, '  p(x)' )
#
#  Compute monomial form so we can get roots directly.
#
    n = len ( p )
    A = gegenbauer_to_monomial_matrix ( n, alpha )
    q = np.matmul ( A, p )
    polynomial_monomial_print ( q, '  Monomial q(x)' )
    r1 = polyroots ( q )
    print ( '' )
    print ( '  Roots of q(x):' )
    print ( r1 )

    A = companion_gegenbauer ( p, alpha )

    print ( '' )
    print ( '  Gegenbauer companion matrix A(p):' )

    print ( A )

    r = eigvals ( A )
    print ( '' )
    print ( '  Eigenvalues of A(p):' )
    print ( r )

  return

def companion_hermite ( p ):

#*****************************************************************************80
#
## companion_hermite() returns the Hermite basis companion matrix for a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Boyd,
#    Solving Transcendental Equations,
#    The Chebyshev Polynomial Proxy and other Numerical Rootfinders,
#    Perturbation Series, and Oracles,
#    SIAM, 2014,
#    ISBN: 978-1-611973-51-8,
#    LC: QA:353.T7B69
#
#  Input:
#
#    real p(n+1): the polynomial coefficients, in order of increasing degree.
#
#  Output:
#
#    real A(n,n): the companion matrix.
#
  import numpy as np

  np1 = len ( p )
  n = np1 - 1

  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n - 1 ):
    A[i,i+1] = 0.5

  for i in range ( 1, n ):
    A[i,i-1] = i

  for j in range ( 0, n ):
    A[n-1,j] = A[n-1,j] - p[j] / 2.0 * p[n]

  return A

def companion_hermite_test ( ):

#*****************************************************************************80
#
## companion_hermite_test() tests companion_hermite().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.polynomial.polynomial import polyroots
  from scipy.linalg import eigvals
  import numpy as np

  print ( '' )
  print ( 'companion_hermite_test():' )
  print ( '  companion_hermite() computes the companion matrix' )
  print ( '  of a polynomial p(x) in the Hermite basis.' )

  p = np.array ( [ 6.0, 5.0, 4.0, 3.0, 2.0, 1.0 ] )

  polynomial_hermite_print ( p, '  Hermite p(x)' )
#
#  Compute monomial form so we can get roots directly.
#
  n = len ( p )
  A = h_to_monomial_matrix ( n )
  q = np.matmul ( A, p )
  polynomial_monomial_print ( q, '  Monomial q(x)' )
  r1 = polyroots ( q )
  print ( '' )
  print ( '  Roots of q(x):' )
  print ( r1 )
 
  A = companion_hermite ( p )

  print ( '' )
  print ( '  Hermite companion matrix A(p):' )

  print ( A )

  r = eigvals ( A )
  print ( '' )
  print ( '  Eigenvalues of A(p):' )
  print ( r )

  return

def companion_laguerre ( p ):

#*****************************************************************************80
#
## companion_laguerre() returns the Laguerre basis companion matrix for a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Boyd,
#    Solving Transcendental Equations,
#    The Chebyshev Polynomial Proxy and other Numerical Rootfinders,
#    Perturbation Series, and Oracles,
#    SIAM, 2014,
#    ISBN: 978-1-611973-51-8,
#    LC: QA:353.T7B69
#
#  Input:
#
#    real p(n+1): the polynomial coefficients, in order of increasing degree.
#
#  Output:
#
#    real A(n,n): the companion matrix.
#
  import numpy as np

  np1 = len ( p )
  n = np1 - 1

  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    A[i,i] = 2 * i + 1

  for i in range ( 1, n ):
    A[i,i-1] = - i

  for i in range ( 0, n -1 ):
    A[i,i+1] = - i - 1

  for j in range ( 0, n ):
    A[n-1,j] = A[n-1,j] + n * p[j] / p[n]
 
  return A

def companion_laguerre_test ( ):

#*****************************************************************************80
#
## companion_laguerre_test() tests companion_laguerre().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.polynomial.polynomial import polyroots
  from scipy.linalg import eigvals
  import numpy as np

  print ( '' )
  print ( 'companion_laguerre_test():' )
  print ( '  companion_laguerre() computes the companion matrix' )
  print ( '  of a polynomial p(x) in the Laguerre basis.' )

  p = np.array ( [ 6.0, 5.0, 4.0, 3.0, 2.0, 1.0 ] )

  polynomial_laguerre_print ( p, '  Laguerre p(x)' )
#
#  Compute monomial form so we can get roots directly.
#
  n = len ( p )
  A = laguerre_to_monomial_matrix ( n )
  q = np.matmul ( A, p )
  polynomial_monomial_print ( q, '  Monomial q(x)' )
  r1 = polyroots ( q )
  print ( '' )
  print ( '  Roots of q(x):' )
  print ( r1 )
 
  A = companion_laguerre ( p )

  print ( '' )
  print ( '  Laguerre companion matrix A(p):' )

  print ( A )

  r = eigvals ( A )
  print ( '' )
  print ( '  Eigenvalues of A(p):' )
  print ( r )

  return

def companion_legendre ( p ):

#*****************************************************************************80
#
## companion_legendre() returns the Legendre basis companion matrix for a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Boyd,
#    Solving Transcendental Equations,
#    The Chebyshev Polynomial Proxy and other Numerical Rootfinders,
#    Perturbation Series, and Oracles,
#    SIAM, 2014,
#    ISBN: 978-1-611973-51-8,
#    LC: QA:353.T7B69
#
#  Input:
#
#    real p(n+1): the polynomial coefficients, in order of increasing degree.
#
#  Output:
#
#    real A(n,n): the companion matrix.
#
  import numpy as np

  np1 = len ( p )
  n = np1 - 1

  A = np.zeros ( [ n, n ] )

  A[0,1] = 1.0

  for i in range ( 1, n - 1 ):
    A[i,i-1] =   i       / ( 2 * i + 1 )
    A[i,i+1] = ( i + 1 ) / ( 2 * i + 1 )

  for j in range ( 0, n ):
    A[n-1,j] = - p[j] / p[n] * ( n ) / ( 2 * n - 1 )

  A[n-1,n-2] = A[n-1,n-2] + ( n - 1 ) / ( 2 * n - 1 )

  return A

def companion_legendre_test ( ):

#*****************************************************************************80
#
## companion_legendre_test() tests companion_legendre().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.polynomial.polynomial import polyroots
  from scipy.linalg import eigvals
  import numpy as np

  print ( '' )
  print ( 'companion_legendre_test():' )
  print ( '  companion_legendre() computes the companion matrix' )
  print ( '  of a polynomial p(x) in the Legendre basis.' )

  p = np.array ( [ 6.0, 5.0, 4.0, 3.0, 2.0, 1.0 ] )

  polynomial_legendre_print ( p, '  Legendre p(x)' )
#
#  Compute monomial form so we can get roots directly.
#
  n = len ( p )
  A = legendre_to_monomial_matrix ( n )
  q = np.matmul ( A, p )
  polynomial_monomial_print ( q, '  Monomial q(x)' )
  r1 = polyroots ( q )
  print ( '' )
  print ( '  Roots of q(x):' )
  print ( r1 )
 
  A = companion_legendre ( p )

  print ( '' )
  print ( '  Legendre companion matrix A(p):' )

  print ( A )

  r = eigvals ( A )
  print ( '' )
  print ( '  Eigenvalues of A(p):' )
  print ( r )

  return

def companion_monomial ( p ):

#*****************************************************************************80
#
## companion_monomial() returns the monomial basis companion matrix for a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Boyd,
#    Solving Transcendental Equations,
#    The Chebyshev Polynomial Proxy and other Numerical Rootfinders,
#    Perturbation Series, and Oracles,
#    SIAM, 2014,
#    ISBN: 978-1-611973-51-8,
#    LC: QA:353.T7B69
#
#  Input:
#
#    real p(n+1): the polynomial coefficients, in order of increasing degree.
#
#  Output:
#
#    real A(n,n): the companion matrix.
#
  import numpy as np

  np1 = len ( p )
  n = np1 - 1

  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n - 1 ):
    A[i,i+1] = 1.0

  for j in range ( 0, n ):
    A[n-1,j] = - p[j] / p[n]

  return A

def companion_monomial_test ( ):

#*****************************************************************************80
#
## companion_monomial_test() tests companion_monomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.polynomial.polynomial import polyroots
  from scipy.linalg import eigvals
  import numpy as np

  print ( '' )
  print ( 'companion_monomial_test():' )
  print ( '  companion_monomial() computes the companion matrix' )
  print ( '  of a polynomial p(x) in the monomial basis.' )

  p = np.array ( [ 6.0, 5.0, 4.0, 3.0, 2.0, 1.0 ] )

  polynomial_monomial_print ( p, '  p(x)' )
#
#  Get roots directly.
#
  polynomial_monomial_print ( p, '  Monomial p(x)' )
  r1 = polyroots ( p )
  print ( '' )
  print ( '  Roots of p(x):' )
  print ( r1 )

  A = companion_monomial ( p )

  print ( '' )
  print ( '  Monomial companion matrix A(p):' )

  print ( A )

  r = eigvals ( A )
  print ( '' )
  print ( '  Eigenvalues of A(p):' )
  print ( r )

  return

def chebyshev_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## chebyshev_to_monomial_matrix(): convert Chebyshev polynomial to monomial form.
#
#  Discussion:
#
#    1     0     -1      0       1     0     -1    0
#    0     1      0     -3       0     5      0   -7
#    0     0      2      0      -8     0     18    0
#    0     0      0      4       0   -20      0   56
#    0     0      0      0       8     0    -48    0
#    0     0      0      0       0    16      0 -112
#    0     0      0      0       0     0     32    0
#    0     0      0      0       0     0      0   64
#
#  Recursion:
#
#    T(0,X) = 1,
#    T(1,X) = X,
#    T(N,X) = 2 * X * T(N-1,X) - T(N-2,X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2024
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
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(n,n), the matrix.
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

def h_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## h_to_monomial_matrix(): physicist's Hermite to monomial conversion matrix.
#
#  Example:
#
#    N = 11
#
#      1  .  -2   .    12     .    -120     .   1680     .   -30240
#      .  2   .  12     .   120      .  -1680      . 30240        .
#      .  .   4   .   -48     .     720     . -13440     .   302400
#      .  .   .   8     .  -160       .  3360   .   -80640        .
#      .  .   .   .    16     .    -480     .  13440     .  -403200
#      .  .   .   .     .    32       . -1344      . 48384        .
#      .  .   .   .     .     .      64     .  -3584     .   161280
#      .  .   .   .     .     .       .   128      . -9216        .
#      .  .   .   .     .     .       .     .    256     .   -23040
#      .  .   .   .     .     .       .     .      .   512        .
#      .  .   .   .     .     .       .     .      .     .     1024
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2024
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

def laguerre_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## laguerre_to_monomial_matrix() converts from Laguerre to monomial form.
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
#    22 February 2024
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
#    integer N: the order of the matrix.
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

def legendre_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## legendre_to_monomial_matrix(): Legendre coefficient conversion matrix.
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
#    21 June 2019
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

def polynomial_chebyshev_print ( c, label ):

#*****************************************************************************80
#
## polynomial_chebyshev_print() prints a polynomial in the Chebyshev basis.
#
#  Discussion:
#
#    The form of a Chebyshev polynomial is:
#
#      p(x) = c(0)*T0(x) + c(1)*T(1)(x) + ... + c(n)*T(n)(x)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real C(1:D+1): the polynomial.
#
#    character LABEL: an optional title.
#
  import numpy as np

  d = len ( c ) - 1

  print ( '' )
  if ( 0 < len ( label ) ):
    print ( label, ' = ' )

  if ( d < 0 ):
    print ( '  Zero polynomial' )
    return

  if ( np.all ( c == 0 ) ):
    print ( '  0' )
    return

  for i in range ( d, -1, -1 ):

    if ( c[i] != 0 ):
 
      print ( '       + ', c[i], '* T' + str ( i ) + '(x)' )

  return

def polynomial_gegenbauer_print ( c, label ):

#*****************************************************************************80
#
## polynomial_gegenbauer_print() prints a polynomial in the Gegenbauer basis.
#
#  Discussion:
#
#    The form of a Gegenbauer polynomial is:
#
#      p(x) = c(0)*C0(x) + c(1)*C(1)(x) + ... + c(n)*C(n)(x)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real C(1:D+1): the polynomial.
#
#    character LABEL: an optional title.
#
  import numpy as np

  d = len ( c ) - 1

  print ( '' )
  if ( 0 < len ( label ) ):
    print ( label, ' = ' )

  if ( d < 0 ):
    print ( '  Zero polynomial' )
    return

  if ( np.all ( c == 0 ) ):
    print ( '  0' )
    return

  for i in range ( d, -1, -1 ):

    if ( c[i] != 0 ):
 
      print ( '       + ', c[i], '* C' + str ( i ) + '(x)' )

  return

def polynomial_hermite_print ( c, label ):

#*****************************************************************************80
#
## polynomial_hermite_print() prints a polynomial in the Hermite basis.
#
#  Discussion:
#
#    The form of a Hermite polynomial is:
#
#      p(x) = c(0)*H0(x) + c(1)*H(1)(x) + ... + c(n)*H(n)(x)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real C(1:D+1): the polynomial.
#
#    character LABEL: an optional title.
#
  import numpy as np

  d = len ( c ) - 1

  print ( '' )
  if ( 0 < len ( label ) ):
    print ( label, ' = ' )

  if ( d < 0 ):
    print ( '  Zero polynomial' )
    return

  if ( np.all ( c == 0 ) ):
    print ( '  0' )
    return

  for i in range ( d, -1, -1 ):

    if ( c[i] != 0 ):
 
      print ( '       + ', c[i], '* H' + str ( i ) + '(x)' )

  return

def polynomial_laguerre_print ( c, label ):

#*****************************************************************************80
#
## polynomial_laguerre_print() prints a polynomial in the Laguerre basis.
#
#  Discussion:
#
#    The form of a Laguerre polynomial is:
#
#      p(x) = c(0)*L0(x) + c(1)*L(1)(x) + ... + c(n)*L(n)(x)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real C(1:D+1): the polynomial.
#
#    character LABEL: an optional title.
#
  import numpy as np

  d = len ( c ) - 1

  print ( '' )
  if ( 0 < len ( label ) ):
    print ( label, ' = ' )

  if ( d < 0 ):
    print ( '  Zero polynomial' )
    return

  if ( np.all ( c == 0 ) ):
    print ( '  0' )
    return

  for i in range ( d, -1, -1 ):

    if ( c[i] != 0 ):
 
      print ( '       + ', c[i], '* L' + str ( i ) + '(x)' )

  return

def polynomial_legendre_print ( c, label ):

#*****************************************************************************80
#
## polynomial_legendre_print() prints a polynomial in the Legendre basis.
#
#  Discussion:
#
#    The form of a Legendre polynomial is:
#
#      p(x) = c(0)*L0(x) + c(1)*L(1)(x) + ... + c(n)*L(n)(x)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 April 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real C(1:D+1): the polynomial.
#
#    character LABEL: an optional title.
#
  import numpy as np

  d = len ( c ) - 1

  print ( '' )
  if ( 0 < len ( label ) ):
    print ( label, ' = ' )

  if ( d < 0 ):
    print ( '  Zero polynomial' )
    return

  if ( np.all ( c == 0 ) ):
    print ( '  0' )
    return

  for i in range ( d, -1, -1 ):

    if ( c[i] != 0 ):
 
      print ( '       + ', c[i], '* P' + str ( i ) + '(x)' )

  return

def polynomial_monomial_print ( c, label ):

#*****************************************************************************80
#
## polynomial_monomial_print() prints a polynomial in monomial basis.
#
#  Discussion:
#
#    The monomial form of a polynomial is:
#
#      p(x) = c(0)*x^0 + c(1)*x + ... + c(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 October 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real C(1:D+1): the polynomial.
#
#    character LABEL: an optional title.
#
  import numpy as np

  d = len ( c ) - 1

  print ( '' )
  if ( 0 < len ( label ) ):
    print ( label, ' = ' )

  if ( d < 0 ):
    print ( '  Zero polynomial' )
    return

  if ( np.all ( c == 0 ) ):
    print ( '  0' )
    return

  for i in range ( d, -1, -1 ):

    if ( c[i] != 0 ):
 
      print ( '       + ', c[i], '* x^' + str ( i ) )

  return

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
  companion_matrix_test ( )
  timestamp ( )

