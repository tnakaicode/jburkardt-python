#! /usr/bin/env python
#
def chebyshev2_compute ( n ):

#*****************************************************************************80
#
## CHEBYSHEV2_COMPUTE computes a Gauss-Chebyshev type 2 quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X)  sqrt ( 1 - x^2 )  dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Parameters:
#
#    Input, integer N, the order.
#    N must be greater than 0.
#
#    Output, real X(N,1), the abscissas.
#
#    Output, real W(N,1), the weights.
#
  import numpy as np
  from sys import exit

  if ( n < 1 ):
    print ( '' )
    print ( 'CHEBYSHEV2_COMPUTE - Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    exit ( 'CHEBYSHEV2_COMPUTE - Fatal error!' )

  x = np.zeros ( n )
  w = np.zeros ( n )

  for i in range ( 0, n ):
    angle = np.pi * float ( n - i ) / float ( n + 1 )
    w[i] = np.pi / float ( n + 1 ) * ( np.sin ( angle ) ) ** 2
    x[i] = np.cos ( angle )

  return x, w

def chebyshev2_compute_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV2_COMPUTE_TEST tests CHEBYSHEV2_COMPUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHEBYSHEV2_COMPUTE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHEBYSHEV2_COMPUTE computes' )
  print ( '  a Chebyshev Type 2 quadrature rule over [-1,1].' )
  print ( '' )
  print ( '     Index       X                       W' )

  for n in range ( 1, 11 ):

    x, w = chebyshev2_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBYSHEV2_COMPUTE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chebyshev2_compute_test ( )
  timestamp ( )

