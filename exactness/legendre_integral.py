#! /usr/bin/env python
#
def legendre_integral ( p ):

#*****************************************************************************80
#
## LEGENDRE_INTEGRAL evaluates a monomial Legendre integral.
#
#  Discussion:
#
#    To test a Legendre quadrature rule, we use it to approximate the
#    integral of a monomial:
#
#      integral ( -1 <= x <= +1 ) x^p dx
#
#    This routine is given the value of the exponent, and returns the
#    exact value of the integral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 May 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P, the power.
#
#    Output, real S, the value of the exact integral.
#
  if ( ( p % 2 ) == 0 ):
    s = 2.0 / ( p + 1 )
  else:
    s = 0.0
	
  return s

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
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LEGENDRE_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LEGENDRE_INTEGRAL returns Legendre integrals of monomials:' )
  print ( '  M(k) = integral ( -1 <= x <= 1 ) x^k dx' )
  print ( '' )
  print ( '     K            M(K)' )
  print ( '' )
  for k in range ( 0, 11 ):
    print ( '  %4d  %14.6g' % ( k, legendre_integral ( k ) ) )
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
 
