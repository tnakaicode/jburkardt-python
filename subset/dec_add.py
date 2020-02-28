#! /usr/bin/env python
#
def dec_add ( mantissa1, exponent1, mantissa2, exponent2, dec_digit ):

#*****************************************************************************80
#
#% DEC_ADD adds two decimal quantities.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    The routine computes
#
#      MANTISSA * 10^EXPONENT = 
#        MANTISSA1 * 10^EXPONENT1 
#      + MANTISSA2 * 10^EXPONENT2
#
#    while trying to avoid integer overflow.
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
#    Input, integer MANTISSA1, EXPONENT1, the first number to be added.
#
#    Input, integer MANTISSA2, EXPONENT2, the second number to be added.
#
#    Input, integer DEC_DIGIT, the number of decimal digits.
#
#    Output, integer MANTISSA, EXPONENT, the sum.
#
  from dec_round import dec_round

  if ( mantissa1 == 0 ):
    mantissa = mantissa2
    exponent = exponent2
    return mantissa, exponent
  elif ( mantissa2 == 0 ):
    mantissa = mantissa1
    exponent = exponent1
    return mantissa, exponent
  elif ( exponent1 == exponent2 ):
    mantissa = mantissa1 + mantissa2
    exponent = exponent1
    [ mantissa, exponent ] = dec_round ( mantissa, exponent, dec_digit )
    return mantissa, exponent
#
#  Line up the exponents.
#
  mantissa3 = mantissa1
  mantissa4 = mantissa2

  if ( exponent1 < exponent2 ):
    mantissa4 = mantissa4 * 10 ** ( exponent2 - exponent1 )
  elif ( exponent2 < exponent1 ):
    mantissa3 = mantissa3 * 10 ** ( exponent1 - exponent2 )
#
#  Add the coefficients.
#
  mantissa = mantissa3 + mantissa4
  exponent = min ( exponent1, exponent2 )
#
#  Clean up the result.
#
  mantissa, exponent = dec_round ( mantissa, exponent, dec_digit )

  return mantissa, exponent

def dec_add_test ( ):

#*****************************************************************************80
#
## DEC_ADD_TEST tests DEC_ADD.
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
  print ( 'DEC_ADD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DEC_ADD adds two decimals.' )

  dec_digit = 3

  atop = 128
  abot = -1
  btop = 438
  bbot = -2

  ctop, cbot = dec_add ( atop, abot, btop, bbot, dec_digit )

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
  print ( 'DEC_ADD_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dec_add_test ( )
  timestamp ( )
