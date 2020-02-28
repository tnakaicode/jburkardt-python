#! /usr/bin/env python
#
def hermite_integral ( p ):

#*****************************************************************************80
#
## HERMITE_INTEGRAL evaluates a monomial Hermite integral.
#
#  Discussion:
#
#    Integral ( -oo < x < +oo ) x^p exp(-x^2) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 November 2011
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
#    Output, real S, the value of the integral.
#
  import numpy as np
  from r8_factorial2 import r8_factorial2

  if ( ( p % 2 ) == 0 ):
    s = r8_factorial2 ( p - 1 ) * np.sqrt ( np.pi ) / 2.0 ** ( p // 2 )
  else:
    s = 0.0

  return s

def hermite_integral_test ( ):

#*****************************************************************************80
#
## HERMITE_INTEGRAL_TEST tests HERMITE_INTEGRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'HERMITE_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HERMITE_INTEGRAL returns Hermite integrals of monomials:' )
  print ( '  M(k) = integral ( -oo <= x <= +oo ) x^k exp(-x^2) dx' )
  print ( '' )
  print ( '     K            M(K)' )
  print ( '' )
  for k in range ( 0, 11 ):
    print ( '  %4d  %14.6g' % ( k, hermite_integral ( k ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HERMITE_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  hermite_integral_test ( )
  timestamp ( )
 
