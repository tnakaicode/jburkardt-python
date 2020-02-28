#! /usr/bin/env python
#
def dec_div ( mantissa1, exponent1, mantissa2, exponent2, dec_digit ):

#*****************************************************************************80
#
## DEC_DIV divides two decimal values.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    The routine computes
#
#      MANTISSA * 10^EXPONENT
#      = ( MANTISSA1 * 10^EXPONENT1 ) / ( MANTISSA2 * 10^EXPONENT2 )
#      = ( MANTISSA1 / MANTISSA2 ) * 10^( EXPONENT1 - EXPONENT2 )
#
#    while avoiding integer overflow.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer MANTISSA1, EXPONENT1, the numerator.
#
#    Input, integer MANTISSA2, EXPONENT2, the denominator.
#
#    Input, integer DEC_DIGIT, the number of decimal digits.
#
#    Output, integer MANTISSA, EXPONENT, the result.
#
  from r8_to_dec import r8_to_dec
  from sys import exit
#
#  First special case, top fraction is 0.
#
  if ( mantissa1 == 0 ):
    mantissa = 0
    exponent = 0
    return mantissa, exponent
#
#  First error, bottom of fraction is 0.
#
  if ( mantissa2 == 0 ):
    print ( '' )
    print ( 'DEC_DIV - Fatal error!' )
    print ( '  Denominator is zero.' )
    exit ( 'DEC_DIV - Fatal error!' )
#
#  Second special case, result is 1.
#
  if ( mantissa1 == mantissa2 and exponent1 == exponent2 ):
    mantissa = 1
    exponent = 0
    return mantissa, exponent
#
#  Third special case, result is power of 10.
#
  if ( mantissa1 == mantissa2 ):
    mantissa = 1
    exponent = exponent1 - exponent2
    return mantissa, exponent
#
#  Fourth special case: MANTISSA1/MANTISSA2 is exact.
#
  if ( ( mantissa1 // mantissa2 ) * mantissa2 == mantissa1 ):
    mantissa = ( mantissa1 // mantissa2 )
    exponent = exponent1 - exponent2
    return mantissa, exponent
#
#  General case.
#
  dval = float ( mantissa1 ) / float ( mantissa2 )

  mantissa3, exponent3 = r8_to_dec ( dval, dec_digit )

  mantissa = mantissa3
  exponent = exponent3 + exponent1 - exponent2

  return mantissa, exponent

def dec_div_test ( ):

#*****************************************************************************80
#
## DEC_DIV_TEST tests DEC_DIV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from dec_to_s import dec_to_s

  print ( '' )
  print ( 'DEC_DIV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DEC_DIV divides two decimals.' )

  dec_digit = 3

  atop = 523
  abot = -1
  btop = 134
  bbot = 2

  ctop, cbot = dec_div ( atop, abot, btop, bbot, dec_digit )

  print ( '' )
  print ( '  Number of decimal places is %d' % ( dec_digit ) )
  print ( '' )

  string = dec_to_s ( atop, abot )
  print ( '  A = %s' % ( string ) )
  string = dec_to_s ( btop, bbot )
  print ( '  B = %s' % ( string ) )
  string = dec_to_s ( ctop, cbot )
  print ( '  C = %s' % ( string ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DEC_DIV_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dec_div_test ( )
  timestamp ( )
