#! /usr/bin/env python
#
def ncoh_compute ( n ):

#*****************************************************************************80
#
## NCOH_COMPUTE computes a Newton-Cotes "open half" quadrature rule.
#
#  Discussion:
#
#    The input value N is used to define N equal subintervals of [-1,+1].
#    The I-th abscissa is the center of the I-th subinterval.
#
#    The integral:
#
#      Integral ( X_MIN <= X <= X_MAX ) F(X) dx
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2015
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

  x = np.zeros ( n )

  x_min = -1.0
  x_max =  1.0

  for i in range ( 0, n ):
    x[i] = ( float ( 2 * n - 2 * i - 1 ) * x_min   \
           + float (         2 * i + 1 ) * x_max ) \
           / float ( 2 * n             )

  w = nc_compute_weights ( n, x_min, x_max, x )

  return x, w

def ncoh_compute_test ( ):

#*****************************************************************************80
#
## NCOH_COMPUTE_TEST tests NCOH_COMPUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NCOH_COMPUTE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NCOH_COMPUTE computes a Newton-Cotes Open Half quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = ncoh_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NCOH_COMPUTE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  ncoh_compute_test ( )
  timestamp ( )

