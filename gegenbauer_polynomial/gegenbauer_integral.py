#! /usr/bin/env python3
#
def gegenbauer_integral ( expon, alpha ):

#*****************************************************************************80
#
## GEGENBAUER_INTEGRAL evaluates the integral of a monomial with Gegenbauer weight.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= +1 ) x^EXPON (1-x^2)^ALPHA dx
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
#    Input, integer EXPON, the exponent.
#
#    Input, real ALPHA, the exponent of (1-X^2) in the weight factor.
#
#    Output, real VALUE, the value of the integral.
#
  from r8_gamma import r8_gamma
  from r8_hyper_2f1 import r8_hyper_2f1

  if ( ( expon % 2 ) == 1 ):
    value = 0.0
    return value

  c = expon

  arg1 = - alpha
  arg2 =   1.0 + c
  arg3 =   2.0 + alpha + c
  arg4 = - 1.0

  value1 = r8_hyper_2f1 ( arg1, arg2, arg3, arg4 )

  value = 2.0 * r8_gamma ( 1.0 + c ) * r8_gamma ( 1.0 + alpha ) \
    * value1 / r8_gamma ( 2.0 + alpha  + c )

  return value

def gegenbauer_integral_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_INTEGRAL_TEST tests GEGENBAUER_INTEGRAL.
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

  alpha = 0.25

  print ( '' )
  print ( 'GEGENBAUER_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEGENBAUER_INTEGRAL evaluates' )
  print ( '  Integral ( -1 < x < +1 ) x^n * (1-x*x)^alpha dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = gegenbauer_integral ( n, alpha )

    print ( '  %8d  %24.16g' % ( n, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  gegenbauer_integral_test ( )
  timestamp ( )

