#! /usr/bin/env python3
#
def gegenbauer_ek_compute ( n, alpha ):

#*****************************************************************************80
#
## GEGENBAUER_EK_COMPUTE: Elhay-Kautsky method for Gauss-Gegenbauer rule.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= 1 ) (1-x^2)^(alpha-1/2) * f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 November 2015
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Parameters:
#
#    Input, integer N, the order.
#
#    Input, real ALPHA, determines the exponent of (1-X^2)^(ALPHA-1/2).
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np
  from imtqlx import imtqlx
  from r8_gamma import r8_gamma
#
#  Define the zero-th moment.
#
  zemu = 2.0 ** ( 2.0 * alpha + 1.0 ) \
    * r8_gamma ( alpha + 1.0 ) \
    * r8_gamma ( alpha + 1.0 ) \
    / r8_gamma ( 2.0 * alpha + 2.0 )
#
#  Define the Jacobi matrix.
#
  x = np.zeros ( n )

  bj = np.zeros ( n )

  bj[0] = 4.0 * ( alpha + 1.0 ) ** 2 \
    / ( ( 2.0 * alpha + 3.0 ) * ( 2.0 * alpha + 2.0 ) ** 2 )

  for i in range ( 2, n ):
    abi = 2.0 * ( alpha + i )
    bj[i-1] = 4.0 * i * ( alpha + i ) ** 2 * ( 2.0 * alpha + i ) \
      / ( ( abi - 1.0 ) * ( abi + 1.0 ) * abi * abi )

  for i in range ( 0, n ):
    bj[i] = np.sqrt ( bj[i] )

  w = np.zeros ( n )

  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def gegenbauer_ek_compute_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_EK_COMPUTE_TEST compares GEGENBAUER_EK_COMPUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  alpha = 0.5

  print ( '' )
  print ( 'GEGENBAUER_EK_COMPUTE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEGENBAUER_EK_COMPUTE computes Gauss-Gegenbauer rules' )
  print ( '' )
  print ( '  Abscissas and weights for a generalized Gauss Gegenbauer rule' )
  print ( '  with ALPHA = %g' % ( alpha ) )
  print ( '  Integration interval is [-1,+1]' )

  for n in range ( 1, 11 ):

    x, w = gegenbauer_ek_compute ( n, alpha )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, w[i], x[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_EK_COMPUTE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gegenbauer_ek_compute_test ( )
  timestamp ( )
