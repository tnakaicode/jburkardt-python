#! /usr/bin/env python
#
def gen_hermite_integral ( expon, alpha ):

#*****************************************************************************80
#
## GEN_HERMITE_INTEGRAL evaluates a monomial generalized Hermite integral.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -oo < x < +oo ) x^n |x|^alpha exp(-x^2) dx
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
#    Input, int EXPON, the exponent of the monomial.
#
#    Input, real ALPHA, the exponent of |X| in the integral.
#    -1.0 < ALPHA.
#
#    Output, real VALUE, the value of the integral.
#
# from math import gamma
  from r8_gamma import r8_gamma
  from r8_huge import r8_huge

  if ( ( expon % 2 ) == 1 ):

    value = 0.0

  else:

    a = alpha + float ( expon )

    if ( a <= -1.0 ):

      value = - r8_huge ( )

    else:

      arg = ( a + 1.0 ) / 2.0
      value = r8_gamma ( arg )

  return value

def gen_hermite_integral_test ( ):

#*****************************************************************************80
#
## GEN_HERMITE_INTEGRAL_TEST tests GEN_HERMITE_INTEGRAL.
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
  print ( 'GEN_HERMITE_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEN_HERMITE_INTEGRAL evaluates' )
  print ( '  Integral ( -oo < x < +oo ) exp(-x^2) x^n |x|^alpha dx' )
  print ( '' )
  print ( '  Use ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '         N         Value' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = gen_hermite_integral ( n, alpha )

    print ( '  %8d  %24.16g' % ( n, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEN_HERMITE_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  gen_hermite_integral_test ( )
  timestamp ( )

