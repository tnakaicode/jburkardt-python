#! /usr/bin/env python
#
def laguerre_integral ( expon ):

#*****************************************************************************80
#
## LAGUERRE_INTEGRAL evaluates a monomial Laguerre integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 <= x < +oo ) x^n * exp ( -x ) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer EXPON, the exponent.
#    0 <= EXPON.
#
#    Output, real EXACT, the value of the integral.
#
  from r8_factorial import r8_factorial

  exact = r8_factorial ( expon )

  return exact

def laguerre_integral_test ( ):

#*****************************************************************************80
#
## LAGUERRE_INTEGRAL_TEST tests LAGUERRE_INTEGRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LAGUERRE_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LAGUERRE_INTEGRAL evaluates' )
  print ( '  Integral ( 0 < x < oo ) x^n * exp(-x) dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = laguerre_integral ( n )

    print ( '  %8d  %24.16g' % ( n, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGUERRE_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  laguerre_integral_test ( )
  timestamp ( )

