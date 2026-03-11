#! /usr/bin/env python3
#
def sympy_limit ( ):

#*****************************************************************************80
#
## sympy_limit() uses sympy() to evaluate limits.
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
  from sympy import limit
  from sympy import log
  from sympy import oo
  from sympy import sin
  from sympy import symbols

  print ( '' )
  print ( 'sympy_limit():' )
  print ( '  Demonstrate the sympy limit() operations.' )
  print ( '' )

  x = symbols ( 'x' )
  result = limit ( sin ( x ) / x, x, 0 )
  print ( '  limit ( sin ( x ) / x ) as x -> 0 = ', result )

  result = limit ( log ( x ) / x, x, oo )
  print ( '  limit ( log ( x ) / x ) as x -> oo = ', result )

  n = symbols ( 'n' )
  expr = ( 1 + x / n )**n
  result = limit ( expr, n, oo )
  print ( '  limit ( ( 1 + x/n )**n ) as n -> oo = ', result )

  return

if ( __name__ == "__main__" ):
  sympy_limit ( )

