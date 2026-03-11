#! /usr/bin/env python3
#
def sympy_polynomial ( ):

#*****************************************************************************80
#
## sympy_polynomial() uses sympy() to perform polynomial operations.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
  from sympy import apart
  from sympy import expand
  from sympy import factor
  from sympy import symbols

  print ( '' )
  print ( 'sympy_polynomial():' )
  print ( '  Demonstrate some polynomial operations.' )
  print ( '' )

  x = symbols ( 'x' )

  p = x**2 - 5 * x + 6
  q = 3 * x - 2

  print ( '  p(x) = ', p )
  print ( '  p(7) = ', p.subs(x,7) )
  print ( '  p.factor() = ', p.factor() )
  print ( '  p**2 = ', p**2 )
  print ( '  p**2.expand = ', (p**2).expand ( ) )

  print ( '  q(x) = ', q )
  print ( '  p + q = ', p + q )
  print ( '  p * q = ', p * q )
  print ( '  p * q.expand = ', ( p * q ).expand ( ) )
  print ( '  p / q = ', p / q )
  print ( '  apart ( p / q ) = ', apart ( p / q ) )

  r = ( x + 1 ) * ( x - 2 ) * ( x - 3 )
  print ( '  r(x) = ', r )
  print ( '  r.expand ( ) = ', r.expand ( ) )

  return

if ( __name__ == "__main__" ):
  sympy_polynomial ( )

