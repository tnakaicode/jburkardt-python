#! /usr/bin/env python3
#
def quad_test ( ):

#*****************************************************************************80
#
## quad_test() tests the scipy() quadrature function quad().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import quad

  print ( '' )
  print ( 'quad_test():' )
  print ( '  Use quad() to integrate a Bessel function jv(2.5,x).' )

  xmin = 0.0
  xmax = 4.5
  result, err = quad ( integrand, xmin, xmax )
  print ( '  Integral estimate is ', result )
  print ( '  Error estimate is    ', err )

  return

def integrand ( x ):
  from scipy.special import jv
  value = jv ( 2.5, x )
  return value

if ( __name__ == "__main__" ):
  quad_test ( )

