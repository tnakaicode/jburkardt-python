#! /usr/bin/env python3
#
def sympy_integral ( ):

#*****************************************************************************80
#
## sympy_integral() uses sympy() to compute definite and indefinite integrals.
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
  from sympy import exp
  from sympy import integrate
  from sympy import oo
  from sympy import symbols

  print ( '' )
  print ( 'sympy_integral():' )
  print ( '  Demonstrate the computation of definite and indefinite integrals.' )
  print ( '' )

  x = symbols ( 'x' )

  humps = 100 / ( ( 10 * x - 3 )**2 + 1 ) \
        + 100 / ( ( 10 * x - 9 )**2 + 4 ) \
        - 6

  humps_anti = integrate ( humps, x )
  print ( '  humps antiderivative = ', humps_anti )

  humps_def = integrate ( humps, ( x, 0, 2 ) )
  print ( '  humps integral 0 to 2 = ', humps_def )
  print ( '  humps integral 0 to 2 (numeric) = ', humps_def.evalf() )

  print ( '' )
  print ( '  f = exp ( - x )' )
  f = exp ( - x )
  f_anti = integrate ( f, x )
  f_def = integrate ( f, ( x, 0, oo ) )
  print ( '  f antiderivative = ', f_anti )
  print ( '  f integral 0 to oo = ', f_def )

  y = symbols ( 'y' )
  double = exp ( - x**2 - y**2 )
  double_def = integrate ( double, ( x, -oo, oo ), ( y, -oo, oo ) )
  print ( '' )
  print ( '  double = exp ( - x**2 - y**2 )' )
  print ( '  double integral -oo < x < 00, -oo < y < oo = ', double_def )

  return

if ( __name__ == "__main__" ):
  sympy_integral ( )

