#! /usr/bin/env python
#
def legendre_integral ( expon ):

#*****************************************************************************80
#
## LEGENDRE_INTEGRAL evaluates a monomial Legendre integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= +1 ) x^n dx
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
#
#    Output, real EXACT, the value of the exact integral.
#
  if ( ( expon % 2 ) == 0 ):

    exact = 2.0 / float ( expon + 1 )
	
  else:

    exact = 0.0
	
  return exact

def legendre_integral_test ( ):

#*****************************************************************************80
#
## LEGENDRE_INTEGRAL_TEST tests LEGENDRE_INTEGRAL.
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
  print ( 'LEGENDRE_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LEGENDRE_INTEGRAL evaluates' )
  print ( '  Integral ( -1 < x < +1 ) x^n dx' )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = legendre_integral ( n )

    print ( '  %8d  %24.16g' % ( n, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LEGENDRE_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  legendre_integral_test ( )
  timestamp ( )

