#! /usr/bin/env python
#
def chebyshev1_integral ( expon ):

#*****************************************************************************80
#
## CHEBYSHEV1_INTEGRAL evaluates a monomial Chebyshev type 1 integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= +1 ) x^n / sqrt ( 1 - x^2 ) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2016
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
  import numpy as np
#
#  Get the exact value of the integral.
#
  if ( ( expon % 2 ) == 0 ):

    top = 1
    bot = 1
    for i in range ( 2, expon + 1, 2 ):
      top = top * ( i - 1 )
      bot = bot *   i
	
    exact = np.pi * top / bot;

  else:

    exact = 0.0;
	
  return exact

def chebyshev1_integral_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV1_INTEGRAL_TEST tests CHEBYSHEV1_INTEGRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHEBSHEV1_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHEBYSHEV1_INTEGRAL returns Chebyshev1 integrals of monomials:' )
  print ( '  M(k) = integral ( -1 <= x <= 1 ) x^k / sqrt ( 1 - x^2 ) dx' )
  print ( '' )
  print ( '     K            M(K)' )
  print ( '' )
  for k in range ( 0, 11 ):
    print ( '  %4d  %14.6g' % ( k, chebyshev1_integral ( k ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBSHEV1_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  chebyshev1_integral_test ( )
  timestamp ( )
