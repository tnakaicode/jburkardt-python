#! /usr/bin/env python
#
def ncc_compute ( n ):

#*****************************************************************************80
#
## NCC_COMPUTE computes a Newton-Cotes Closed quadrature rule.
#
#  Discussion:
#
#    For the interval [-1,+1], the Newton-Cotes Closed quadrature rule
#    estimates
#
#      Integral ( -1 <= X <= +1 ) F(X) dX
#
#    using N abscissas X and weights W:
#
#      sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
#
#    For the CLOSED rule, the abscissas are equally spaced, and include
#    the end points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np
  from nc_compute_weights import nc_compute_weights
  from r8vec_linspace import r8vec_linspace

  x_min = -1.0
  x_max = +1.0
  x = r8vec_linspace ( n, x_min, x_max )

  if ( n == 1 ):

    w = np.zeros ( n )
    w[0] = x_max - x_min

  else:

    w = nc_compute_weights ( n, x_min, x_max, x )

  return x, w

def ncc_compute_test ( ):

#*****************************************************************************80
#
## NCC_COMPUTE_TEST tests NCC_COMPUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NCC_COMPUTE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NCC_COMPUTE computes a Newton-Cotes Closed quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = ncc_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NCC_COMPUTE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  ncc_compute_test ( )
  timestamp ( )

