#! /usr/bin/env python3
#
def sympy_series ( ):

#*****************************************************************************80
#
## sympy_series() uses sympy() to manipulate Taylor series.
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
  from sympy import cos
  from sympy import exp
  from sympy import log
  from sympy import series
  from sympy import sin
  from sympy import symbols

  print ( '' )
  print ( 'sympy_series():' )
  print ( '  Demonstrate Taylor series expansion.' )

  x = symbols ( 'x' )
#
#  Expand around x=0 with remainder x^4.
#
  result = series ( exp ( sin ( x ) ), x, 0, 4 )
  print ( '' )
  print ( '  Order 4 series around x=0 for exp(sin(x))' )
  print ( result )
#
#  Expand around x=1 with remainder x^6.
#
  result = series ( log ( x ), x, 1, 3 )
  print ( '' )
  print ( '  Order 3 series around x=1 for log(x)' )
  print ( result )
#
#  Expand around x=1 with remainder x^6.
#
  result = series ( (1+x)*exp(x), x, 0, 4 )
  print ( '' )
  print ( '  Order 4 series around x=0 for (1+x)e^x' )
  print ( result )
#
#  Expand around x=1 with remainder x^6.
#
  result = series ( exp(x)/cos(x), x, 0, 6 )
  print ( '' )
  print ( '  Order 6 series around x=0 for e^x/cos(x)' )
  print ( result )
  
  return

if ( __name__ == "__main__" ):
  sympy_series ( )

