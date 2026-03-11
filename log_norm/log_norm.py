#! /usr/bin/env python3
#
def log_norm ( A, p ):

#*****************************************************************************80
#
## log_norm() evaluates the matrix logarithmic norm for the l1, l2 and loo norms.
#
#  Discussion:
#
#    The matrix logarithmic norm is not a norm.  It can have a negative value.
#    However, it is useful in estimating error growth in solving systems
#    of differential equations, because of the necessity of estimating the
#    quantity exp(A*t).
#
#    If mu = log_norm ( A, p ), then
#      || exp(A*t) ||_p <= exp ( mu * t )
#    This result applies even when the matrix A is non-normal.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time dependent advection-diffusion-reaction equations,
#    Springer, 2003,
#    ISBN13: 978-3-662-09017-6.
#
#    Gustaf Soderlind,
#    The logarithmic norm: History and modern theory,
#    BIT Numerical Mathematics,
#    Volume 46, pages 631-652, 2006.
#
#  Input:
#
#    real/complex A(N,N), the matrix whose norm is to be evaluated.
#
#    real P, indicates the P-norm to be used.
#    1: the L1 norm
#    2: the L2 norm
#    Inf: the Loo norm
#
#  Output:
#
#    real MU, the logarithmic norm of the matrix.
#
  import numpy as np

  if ( p == 1 ):

    B = np.abs ( A ) - np.diag ( np.diag ( np.abs ( A ) ) )
    c = np.real ( np.diag ( A ) )
    d = np.sum ( B, 0 )
    mu = np.max ( np.real ( c + d ) )

  elif ( p == 2 ):

    B = 0.5 * ( A + np.conjugate ( np.transpose ( A ) ) )
    c = np.linalg.eigvals ( B )
    mu = np.max ( np.real ( c ) )

  elif ( p == np.inf ):

    B = np.abs ( A ) - np.diag ( np.diag ( np.abs ( A ) ) )
    c = np.real ( np.diag ( A ) )
    d = np.sum ( B, 1 )
    mu = np.max ( np.real ( c + d ) )

  else:

    print ( '' )
    print ( 'log_norm(): Fatal error!' )
    print ( '  Illegal value of second argument "p" = ', p )
    print ( '  Legal values are 1, 2 and Inf' )
    raise Exception ( 'log_norm(): Fatal error!' )
 
  return mu

def log_norm_test ( ):

#*****************************************************************************80
#
## log_norm_test() tests log_norm().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'log_norm_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test log_norm()' )
  print ( '' )

  for k in range ( 1, 6 ):
    A = test_matrix ( k )
    Ap1 = np.linalg.norm ( A, 1 ) 
    Ap2 = np.linalg.norm ( A, 2 )
    Apoo = np.linalg.norm ( A, np.inf )
    Al1 = log_norm ( A, 1 )
    Al2 = log_norm ( A, 2 )
    Aloo = log_norm ( A, np.inf )
    print ( '  Test matrix:' )
    print ( A )
    print ( '  p norms    %8.4f  %8.4f  %8.4f' % ( Ap1, Ap2, Apoo ) )
    print ( '  log norms: %8.4f  %8.4f  %8.4f' % ( Al1, Al2, Aloo ) )
    lam = np.linalg.eigvals ( A )
    print ( '  eigenvalues:' )
    print ( lam )
#
#  Terminate.
#
  print ( '' )
  print ( 'log_norm_test():' )
  print ( '  Normal end of execution.' )

  return

def test_matrix ( k ):

#*****************************************************************************80
#
## test_matrix() returns a test matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Guang-Da Hu, Mingzhu Liu,
#    The weighted logarithmic matrix norm and bounds for the matrix exponential,
#    Linear Algebra and Its Applications,
#    Volume 390, pages 145-154, 2004.
#
#    Guang-Da Hu, Taketomo Mitsui,
#    Bounds of the matrix eigenvalues and its exponential by Lyapunov equation,
#    Kybernetika,
#    Volume 48, pages 865-874, 2012.
#
#  Input:
#
#    integer K, the index of the matrix.
#    1 <= K <= 5.
#
#  Output:
#
#    real/complex A(N,N), the matrix.
#
  import numpy as np

  if ( k == 1 ):
    A = np.array ( [ \
      [ -0.8,  0.4,  0.2 ], \
      [  1.0, -3.0,  2.0 ], \
      [  0.0,  1.0, -1.0 ] ] )
  elif ( k == 2 ):
    A = np.array ( [ \
     [  5.0,  6.0,  3.0 ], \
     [ -2.0,  7.0,  4.0 ], \
     [ 13.0,  9.0, -1.0 ] ] )
  elif ( k == 3 ):
    A = np.array ( [ \
     [  1.0,  2.0,  1.0 ], \
     [ -2.0,  0.0,  3.0 ], \
     [ -1.0, -3.0,  0.0 ] ] )
  elif ( k == 4 ):
    A = np.array ( [ \
     [  4.0+7.0j,  -10.0-3.0j,   1.0+6.0j ], \
     [ -7.0+1.0j,    4.0+6.0j,  -2.0+3.0j ], \
     [ -5.0+2.0j,    4.0+11.0j, -3.0-6.0j ] ] )
  elif ( k == 5 ):
    A = np.array ( [ \
     [ -2.0,  0.0,  0.0 ], \
     [  0.0, -1.0,  0.0 ], \
     [  0.0,  0.0, -0.5 ] ] )
  else:
    print ( '' )
    print ( 'test_matrix(): Fatal error!' )
    print ( '  Illegal input value for k = ', k )
    print ( '  Legal values are 1 <= k <= 5.' )
    raise Exception ( 'test_matrix(): Fatal error!' )

  return A

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

if ( __name__ == "__main__" ):
  timestamp ( )
  log_norm_test ( )
  timestamp ( )

