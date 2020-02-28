#! /usr/bin/env python
#
def dec_to_r8 ( mantissa, exponent ):

#*****************************************************************************80
#
## DEC_TO_R8 converts a decimal to an R8.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer MANTISSA, EXPONENT, the coefficient and exponent
#    of the decimal value.
#
#    Output, real R, the equivalent real value.
#
  r = mantissa * ( 10 ** exponent )

  return r

def dec_to_r8_test ( ):

#*****************************************************************************80
#
## DEC_TO_R8_TEST tests DEC_TO_R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_to_dec import r8_to_dec
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'DEC_TO_R8_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DEC_TO_R8 converts a decimal to a real number.' )

  dec_digit = 5

  print ( '' )
  print ( '  The number of decimal digits is %d' % ( dec_digit ) )

  r8_lo = -10.0
  r8_hi = +10.0
  seed = 123456789

  print ( '' )
  print ( '     R   =>  A * 10^B  =>  R2' )
  print ( '' )

  for i in range ( 0, 10 ):
    r, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    a, b = r8_to_dec ( r, dec_digit )
    r2 = dec_to_r8 ( a, b )
    print ( '  %10.6f  %6d  %6d  %10.6f' % ( r, a, b, r2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DEC_TO_R8_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dec_to_r8_test ( )
  timestamp ( )

