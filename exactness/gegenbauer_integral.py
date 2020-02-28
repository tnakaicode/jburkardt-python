#! /usr/bin/env python
#
def gegenbauer_integral ( p, lam ):

#*****************************************************************************80
#
## GEGENBAUER_INTEGRAL evaluates a monomial integral with Gegenbauer weight.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x < +1 ) x^p * ( 1 - x^2 )^(lambda-1/2) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P, the exponent.
#    0 <= P.
#
#    Input, real LAM, the exponent term.
#    -1/2 < LAM.
#
#    Output, real S, the value of the integral.
#
  from r8_gamma import r8_gamma

  if ( ( p % 2 ) == 0 ):
    s = r8_gamma ( p / 2.0 + 0.5 ) * r8_gamma ( lam + 0.5 ) \
      / r8_gamma ( p / 2.0 + lam + 1.0 )
  else:
    s = 0.0

  return s

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
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  lam = 1.75

  print ( '' )
  print ( 'GEGENBAUER_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEGENBAUER_INTEGRAL returns Gegenbauer integrals of monomials:' )
  print ( '  M(k) = integral ( -1 <= x <= 1 ) (1-x^2)^(lambda-1/2) dx' )
  print ( '  Here, we use lambda = %g' % ( lam ) )
  print ( '' )
  print ( '     K            M(K)' )
  print ( '' )
  for k in range ( 0, 11 ):
    print ( '  %4d  %14.6g' % ( k, gegenbauer_integral ( k, lam ) ) )
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
 
