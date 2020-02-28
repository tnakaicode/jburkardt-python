#! /usr/bin/env python
#
def gen_laguerre_integral ( expon, alpha ):

#*****************************************************************************80
#
## GEN_LAGUERRE_INTEGRAL evaluates a monomial generalized Laguerre integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( 0 <= x < +oo ) x^n * x^alpha * exp ( -x ) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
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
#    Input, real ALPHA, the exponent of X in the weight function.
#
#    Output, real EXACT, the value of the integral.
#
  from r8_gamma import r8_gamma

  arg = alpha + float ( expon + 1 )

  exact = r8_gamma ( arg )
 
  return exact

def gen_laguerre_integral_test ( ):

#*****************************************************************************80
#
## GEN_LAGUERRE_INTEGRAL_TEST tests GEN_LAGUERRE_INTEGRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  alpha = 0.5

  print ( '' )
  print ( 'GEN_LAGUERRE_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEN_LAGUERRE_INTEGRAL evaluates' )
  print ( '  Integral ( 0 < x < +oo ) exp(-x) x^n x^alpha dx' )
  print ( '' )
  print ( '  Use ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = gen_laguerre_integral ( n, alpha )

    print ( '  %8d  %24.16g' % ( n, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEN_LAGUERRE_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  gen_laguerre_integral_test ( )
  timestamp ( )

