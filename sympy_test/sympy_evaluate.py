#! /usr/bin/env python3
#
def sympy_evaluate ( ):

#*****************************************************************************80
#
## sympy_evaluate() uses sympy() to evaluate a function.
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
  from sympy import lambdify
  from sympy import symbols
  import numpy
  import numpy as np

  print ( '' )
  print ( 'sympy_evaluate():' )
  print ( '  Show ways of evaluating the symbolic humps() function.' )
  print ( '' )

  x = symbols ( 'x' )

  humps = 100 / ( ( 10 * x - 3 )**2 + 1 ) \
        + 100 / ( ( 10 * x - 9 )**2 + 4 ) \
        - 6
#
#  subs(x,y) replaces "x" by "y".
#  "y" can be a symbol, an expression, or a number.
#
  y = symbols ( 'y' )
  humps_y = humps.subs ( x, y )
  print ( '  humps.subs(x,y) = ', humps_y )

  humps_cosy = humps.subs ( x, cos(y) )
  print ( '  humps.subs(x,cos(y)) = ', humps_cosy )

  humps_1 = humps.subs ( x, 1 )
  print ( '  humps.subs(x,1) = ', humps_1 )
#
#  lambdify() creates a numpy function from a symbolic expression.
#
  z = np.linspace ( 0.0, 2.0, 5 )
  humps_lambda = lambdify ( x, humps, 'numpy' )
  humps_lambda ( z )
  print ( '  humps(z) = ', humps_lambda ( z ) )

  return

if ( __name__ == "__main__" ):
  sympy_evaluate ( )

