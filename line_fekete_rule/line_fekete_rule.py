#! /usr/bin/env python3
#
def line_fekete_rule_test ( ):

#*****************************************************************************80
#
## line_fekete_rule_test() tests line_fekete_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'line_fekete_rule_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test line_fekete_rule().' )

  for m in [ 5, 11, 21, 41 ]:
    line_fekete_bos_levenberg_test ( m )
    line_fekete_chebyshev_test ( m )
    line_fekete_legendre_test ( m )
    line_fekete_monomial_test ( m )
#
#  Terminate.
#
  print ( '' )
  print ( 'line_fekete_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def cheby_van1 ( m, a, b, n, x ):

#*****************************************************************************80
#
## cheby_van1() returns the Chebyshev Vandermonde-like matrix for [A,B].
#
#  Discussion:
#
#    Normally, the Chebyshev polynomials are defined on -1 <= XI <= +1.
#    Here, we assume the Chebyshev polynomials have been defined on the
#    interval A <= X <= B, using the mapping
#      XI = ( - ( B - X ) + ( X - A ) ) / ( B - A )
#    so that
#      ChebyAB(A,BX) = Cheby(XI).
#
#    if ( I == 1 ) then
#      V(1,1:N) = 1
#    elseif ( I == 2 ) then
#      V(2,1:N) = XI(1:N)
#    else
#      V(I,1:N) = 2.0 * XI(1:N) * V(I-1,1:N) - V(I-2,1:N)
#
#  Example:
#
#    M = 5, A = -1, B = +1, N = 5, X = ( 1, 2, 3, 4, 5 )
#
#    1  1   1    1    1
#    1  2   3    4    5
#    1  7  17   31   49
#    1 26  99  244  485
#    1 97 577 1921 4801
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    Stability analysis of algorithms for solving confluent
#    Vandermonde-like systems,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 11, 1990, pages 23-41.
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    real A, B, the interval.
#
#    integer N, the number of values in X.
#
#    real X(N), the abscissas.
#
#  Output:
#
#    real V(M,N), the matrix.
#
  import numpy as np
#
#  Compute the normalized abscissas in [-1,+1].
#
  xi = ( - ( b - x     )   \
         + (     x - a ) ) \
       /   ( b     - a )
#
#  Compute the matrix.
#
  v = np.zeros ( [ m, n ] )

  v[0,:] = 1.0
  v[1,:] = xi.copy ( )

  for i in range ( 2, m ):
    v[i,:] = 2.0 * xi * v[i-1,:] - v[i-2,:]

  return v

def compressed_solve ( A, b ):

#*****************************************************************************80
#
## compressed_solve() seeks a solution to an underdetermined system with maximal zeros.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(m,n): the matrix.  It must be the case that m <= n.
#
#    real b(m): the right hand side.
#
#  Output:
#
#    real x(n): a solution of the system A*x=b, with the maximal number
#    of zero entries.
#
  from scipy.linalg import qr
  import numpy as np

  m, n = A.shape
#
#  Get the QR factorization, with pivoting: A(:,P) = Q * R
#  P is a reordering of the columns of A which reduces fillin in R.
#
  Q, R, p = qr ( A, pivoting = True )
#
#  Form and solve the reduced system:
#
  r = np.linalg.matrix_rank ( A )
  y = np.matmul ( np.transpose ( Q[:,0:r] ), b )
#
#  Start with a full vector of zeros.
#  Compute the solution of the reduced system and patch it into the full vector.
#
  x = np.zeros ( n )
  x[p[0:r]] = np.linalg.solve ( R[0:r,0:r], y )

  return x

def legendre_van ( m, a, b, n, x ):

#*****************************************************************************80
#
## legendre_van() returns the Legendre Vandermonde-like matrix for [A,B].
#
#  Discussion:
#
#    Normally, the Legendre polynomials are defined on -1 <= XI <= +1.
#    Here, we assume the Legendre polynomials have been defined on the
#    interval A <= X <= B, using the mapping
#      XI = ( - ( B - X ) + ( X - A ) ) / ( B - A )
#    so that
#      Lab(A,BX) = L(XI).
#
#    if ( I = 1 ) then
#      V(1,1:N) = 1
#    else if ( I = 2 ) then
#      V(2,1:N) = XI(1:N)
#    else
#      V(I,1:N) = ( (2*I-1) * XI(1:N) * V(I-1,1:N) - (I-1)*V(I-2,1:N) ) / I
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#
#    real A, B, the limits of the interval.
#
#    integer N, the number of columns of the matrix.
#
#    real X(N), the abscissas.
#
#  Output:
#
#    real V(M,N), the matrix.
#
  import numpy as np
#
#  Compute the normalized abscissas in [-1,+1].
#
  xi = ( - ( b - x     )   \
         + (     x - a ) ) \
       /   ( b     - a )
#
#  Set up the matrix.
#
  v = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):

    if ( i == 0 ):
      v[i,:] = 1.0
    elif ( i == 1 ):
      v[i,:] = xi.copy ( )
    else:
      v[i,:] = ( ( 2 * i + 1 ) * xi[:] * v[i-1,:]   \
               + (   - i     ) *         v[i-2,:] ) \
               / (     i + 1 )

  return v

def line_fekete_bos_levenberg_test ( m ):

#*****************************************************************************80
#
## line_fekete_bos_levenberg_test(): Bos Levenberg code for Fekete points.
#
#  Discussion:
#
#    I wanted to run the code in the Bos Levenberg paper for
#    comparison with mine.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Len Bos, Norm Levenberg,
#    On the calculation of approximate Fekete points: the univariate case,
#    Electronic Transactions on Numerical Analysis,
#    Volume 30, pages 377-397, 2008.
#
#  Input:
#
#    integer M, the dimension of the polynomial space.
#    In the paper, M is 21.
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np
  import pprint

  rng = default_rng ( )

  a = -1.0
  b = +1.0
  n = 1000
  x = np.linspace ( a, b, n )

  print ( '' )
  print ( 'line_fekete_bos_levenberg_test():' )
  print ( '  Seek Fekete points in [', a, ',', b, ']' )
  print ( '  using', n, 'equally spaced sample points' )
  print ( '  for polynomial space of dimension M =', m )
  print ( '  with the Chebyshev basis' )
  print ( '  and weight 1/sqrt(1-x^2) (Bos-Levenberg approach).' )

  A = cheby_van1 ( m, a, b, n, x )
  b = rng.uniform ( size = m )
  y = compressed_solve ( A, b )
  xf = x[y != 0.0 ]
  nf = len ( xf )

  if ( nf < 25 ):
    print ( '' )
    print ( '  Fekete points (Bos-Levenberg):' )
    pprint.pprint ( xf )

  yf = np.ones ( nf )

  plt.clf ( )
  plt.plot ( xf, yf, '*' )
  plt.title ( 'Estimated Fekete points, Bos-Levenberg' )
  plt.grid ( True )
  filename = 'line_fekete_bos_levenberg.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def line_fekete_chebyshev ( m, a, b, n, x ):

#*****************************************************************************80
#
## line_fekete_chebyshev() computes approximate Fekete points in an interval [A,B].
#
#  Discussion:
#
#    We use the Chebyshev basis.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Len Bos, Norm Levenberg,
#    On the calculation of approximate Fekete points: the univariate case,
#    Electronic Transactions on Numerical Analysis, 
#    Volume 30, pages 377-397, 2008.
#    
#  Input:
#
#    integer M, the number of basis polynomials.
#
#    real A, B, the endpoints of the interval.
#
#    integer N, the number of sample points.
#    M <= N.
#
#    real X(N), the coordinates of the sample points.
#
#  Output:
#
#    integer NF, the number of Fekete points.
#    If the computation is successful, NF = M.
#
#    real XF(NF), the coordinates of the Fekete points.
#
#    real WF(NF), the weights of the Fekete points.
#
#    real VF(NF,N), the nonsingular Vandermonde submatrix.
#
  import numpy as np
  import pprint

  if ( n < m ):
    print ( '' )
    print ( 'line_fekete_chebyshev(): Fatal error!' )
    print ( '  N = ', n, ' < M = ', m )
    raise Exception ( 'line_fekete_chebyshev(): Fatal error!' )
#
#  Compute the Chebyshev-Vandermonde matrix.
#
  V = cheby_van1 ( m, a, b, n, x )
#
#  MOM(I) = Integral ( A <= x <= B ) Tab(A,B,Ix) dx
#
  mom = np.zeros ( m )
  mom[0] = np.pi * ( b - a ) / 2.0
#
#  Get the weights W.
#
  w = compressed_solve ( V, mom )
#
#  Select the data associated with nonzero weights.
#
  ind = w != 0.0

  nf = np.sum ( ind )
  xf = x[ind]
  wf = w[ind]
  VF = ( V[:,ind] ).T

  return nf, xf, wf, VF

def line_fekete_chebyshev_test ( m ):

#*****************************************************************************80
#
## line_fekete_chebyshev_test() seeks Fekete points in [-1,+1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Len Bos, Norm Levenberg,
#    On the calculation of approximate Fekete points: the univariate case,
#    Electronic Transactions on Numerical Analysis,
#    Volume 30, pages 377-397, 2008.
#
#  Input:
#
#    integer M, the dimension of the polynomial space.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import pprint

  n = 1000
  a = -1.0
  b = +1.0
  x = np.linspace ( a, b, n )

  print ( '' )
  print ( 'line_fekete_chebyshev_test():' )
  print ( '  Seek Fekete points in [', a, ',', b, ']' )
  print ( '  using', n, 'equally spaced sample points' )
  print ( '  for polynomials of degree M =', m )
  print ( '  with the Chebyshev basis' )
  print ( '  and weight 1/sqrt(1-x^2).' )

  nf, xf, wf, vf = line_fekete_chebyshev ( m, a, b, n, x )
  wf_sum = np.sum ( wf )

  print ( '' )
  print ( '  NF =', nf )
  print ( '  Sum(WF) =', wf_sum )

  if ( nf < 25 ):
    print ( '' )
    print ( '  Fekete points (Chebyshev basis):' )
    pprint.pprint ( xf )

  yf = np.ones ( nf )

  plt.clf ( )
  plt.plot ( xf, yf, '*' )
  plt.title ( 'Fekete points, Chebyshev basis' )
  plt.grid ( True )
  filename = 'line_fekete_chebyshev.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def line_fekete_legendre ( m, a, b, n, x ):

#*****************************************************************************80
#
## line_fekete_legendre() computes approximate Fekete points in an interval [A,B].
#
#  Discussion:
#
#    We use the uniform weight and the Legendre basis.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Len Bos, Norm Levenberg,
#    On the calculation of approximate Fekete points: the univariate case,
#    Electronic Transactions on Numerical Analysis, 
#    Volume 30, pages 377-397, 2008.
#    
#  Input:
#
#    integer M, the number of basis polynomials.
#
#    real A, B, the endpoints of the interval.
#
#    integer N, the number of sample points.
#    M <= N.
#
#    real X(N), the coordinates of the sample points.
#
#  Output:
#
#    integer NF, the number of Fekete points.
#    If the computation is successful, NF = M.
#
#    real XF(NF), the coordinates of the Fekete points.
#
#    real WF(NF), the weights of the Fekete points.
#
#    real VF(NF,N), the nonsingular Vandermonde submatrix.
#
  import numpy as np
  import pprint

  if ( n < m ):
    print ( '' )
    print ( 'line_fekete_legendre(): Fatal error!' )
    print ( '  n < m.' )
    raise Exception ( 'line_fekete_legendre(): Fatal error!' )
#
#  Compute the Legendre-Vandermonde matrix.
#
  V = legendre_van ( m, a, b, n, x )
#
#  "Moments" of shifted scaled Legendre polynomials, 
#    MOM(i) = integral ( A <= X <= B ) Lab(A,B,IX) dx
#
  mom = np.zeros ( m )
  mom[0] = b - a
#
#  Solve for weights.
#
# w = np.linalg.solve ( V, mom )
# w, _, _, _  = np.linalg.lstsq ( V, mom, rcond = None )
  w = compressed_solve ( V, mom )
  ind =  w != 0.0

  nf = np.sum ( ind )
  xf = x[ind]
  if ( nf < 25 ):
    print ( '' )
    print ( '  Fekete points (Legendre basis):' )
    pprint.pprint ( xf )
  wf = w[ind]
  Vf = ( V[:,ind] ).T

  return nf, xf, wf, Vf

def line_fekete_legendre_test ( m ):

#*****************************************************************************80
#
## line_fekete_legendre_test() seeks Fekete points in [-1,+1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the dimension of the polynomial space.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import pprint

  n = 5001
  a = -1.0
  b = +1.0
  x = np.linspace ( a, b, n )

  print ( '' )
  print ( 'line_fekete_legendre_test():' )
  print ( '  Seek Fekete points in [', a, ',', b, ']' )
  print ( '  using', n, 'equally spaced sample points' )
  print ( '  for polynomials of degree M =', m )
  print ( '  with the Legendre basis and uniform weight.' )

  nf, xf, wf, vf = line_fekete_legendre ( m, a, b, n, x )
  wf_sum = np.sum ( wf )

  print ( '' )
  print ( '  NF =', nf )
  print ( '  Sum(WF) =', wf_sum )
  print ( '' )
  print ( '  Fekete points (Legendre basis):' )
  pprint.pprint ( xf )

  yf = np.ones ( nf )

  plt.clf ( )
  plt.plot ( xf, yf, '*' )
  plt.title ( 'Fekete points, Legendre basis' )
  plt.grid ( True )
  filename = 'line_fekete_legendre.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def line_fekete_monomial ( m, a, b, n, x ):

#*****************************************************************************80
#
## line_fekete_monomial() computes approximate Fekete points in an interval [A,B].
#
#  Discussion:
#
#    We use the uniform weight and the monomial basis:
#
#      P(j) = x^(j-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alvise Sommariva, Marco Vianello,
#    Computing approximate Fekete points by QR factorizations of Vandermonde 
#    matrices,
#    Computers and Mathematics with Applications,
#    Volume 57, 2009, pages 1324-1336.
#    
#  Input:
#
#    integer M, the number of basis polynomials.
#
#    real A, B, the endpoints of the interval.
#
#    integer N, the number of sample points.
#    M <= N.
#
#    real X(N), the coordinates of the sample points.
#
#  Output:
#
#    integer NF, the number of Fekete points.
#    If the computation is successful, NF = M.
#
#    real XF(NF), the coordinates of the Fekete points.
#
#    real WF(NF), the weights of the Fekete points.
#
#    real VF(NF,M), the nonsingular Vandermonde submatrix.
#
  import numpy as np
  import pprint

  if ( n < m ):
    print ( '' )
    print ( 'line_fekete_monomial(): Fatal error!' )
    print ( '  n < m.' )
    raise Exception ( 'line_fekete_monomial(): Fatal error!' )
#
#  Moments of monomials:
#
  mom = line_monomial_moments ( a, b, m )
#
#  Form the rectangular Vandermonde matrix V for the polynomial basis.
#
  V = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    if ( i == 0 ):
      V[i,:] = 1.0
    else:
      V[i,:] = V[i-1,:] * x
#
#  Solve the system for the weights W.
#
# w = np.linalg.solve ( V, mom )
# w, _, _, _  = np.linalg.lstsq ( V, mom, rcond = None )
  w = compressed_solve ( V, mom )
#
#  Locate nonzero W's.
#
  ind = w != 0.0
#
#  Retain data associated with nonzero W's.
#
  nf = np.sum ( ind )
  xf = x[ind]
  if ( nf < 25 ):
    print ( '' )
    print ( '  Fekete points (monomial basis):' )
    pprint.pprint ( xf )
  wf = w[ind]
  Vf = ( V[:,ind] ).T

  return nf, xf, wf, Vf

def line_fekete_monomial_test ( m ):

#*****************************************************************************80
#
## line_fekete_monomial_test() seeks Fekete points in [-1,+1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alvise Sommariva, Marco Vianello,
#    Computing approximate Fekete points by QR factorizations of Vandermonde 
#    matrices,
#    Computers and Mathematics with Applications,
#    Volume 57, 2009, pages 1324-1336.
#
#  Input:
#
#    integer M, the dimension of the polynomial space.  
#    A sample value would be m=5.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import pprint

  n = 5001
  a = -1.0
  b = +1.0

  x = np.linspace ( a, b, n )

  print ( '' )
  print ( 'line_fekete_monomial_test():' )
  print ( '  Seek Fekete points in [', a, ',', b, ']' )
  print ( '  using', n, 'equally spaced sample points', n )
  print ( '  for polynomials of degree M =', m )
  print ( '  using the monomial basis and uniform weight.' )

  nf, xf, wf, vf = line_fekete_monomial ( m, a, b, n, x )
  wf_sum = np.sum ( wf )

  print ( '' )
  print ( '  NF =', nf )
  print ( '  Sum(WF) =', wf_sum )
  print ( '' )
  print ( '  Fekete points (Monomial basis):' )
  pprint.pprint ( xf )

  yf = np.ones ( nf )

  plt.clf ( )
  plt.plot ( xf, yf, '*' )
  plt.title ( 'Fekete points, Monomial basis' )
  plt.grid ( True )
  filename = 'line_fekete_monomial.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def line_monomial_moments ( a, b, m ):

#*****************************************************************************80
#
## line_monomial_moments() computes monomial moments in [A,B].
#
#  Discussion:
#
#    We use the uniform weight and the shifted and scaled monomial basis:
#
#      P(a,b,ix) = xi(a,bx)^(i-1)
#       xi(a,bx) = ( - ( b - x ) + ( x - a ) ) / ( b - a )
#
#    The i-th moment is
#
#      mom(i) = integral ( a <= x <= b ) P(a,b,ix) dx
#             = integral ( a <= x <= b ) xi(a,bx)^(i-1) dx
#             = 0.5 * ( b - a ) * integral ( -1 <= xi <= +1 ) xi^(i-1) dxi
#             = 0.5 * ( b - a ) * xi^i / i | ( -1 <= xi <= +1 )
#             = 0.5 * ( b - a ) * ( 1 - (-1)^i ) / i
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the endpoints of the interval.
#
#    integer M, the number of basis polynomials.
#
#  Output:
#
#    real MOM(M), the moments.
#
  import numpy as np

  mom = np.zeros ( m )

  for i in range ( 0, m ):
    mom[i] = ( b - a ) * ( ( i + 1 ) % 2 ) / ( i + 1 )

  return mom

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
  line_fekete_rule_test ( )
  timestamp ( )

