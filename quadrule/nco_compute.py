#! /usr/bin/env python
#
def nco_compute ( n ):

#*****************************************************************************80
#
## NCO_COMPUTE computes a Newton-Cotes Open quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= +1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
#
#    For the OPEN rule, the abscissas do not include the end points.
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
  from nc_compute_weights import nc_compute_weights
  from r8vec_linspace import r8vec_linspace

  x_min = -1.0
  x_max =  1.0
  x = r8vec_linspace ( n, x_min, x_max )

  w = nc_compute_weights ( n, x_min, x_max, x )

  return x, w

def nco_compute_test ( ):

#*****************************************************************************80
#
## NCO_COMPUTE_TEST tests NCO_COMPUTE.
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
  print ( 'NCO_COMPUTE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NCO_COMPUTE computes a Newton-Cotes Open quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = nco_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NCO_COMPUTE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  nco_compute_test ( )
  timestamp ( )

