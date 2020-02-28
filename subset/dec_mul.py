#! /usr/bin/env python
#
def dec_mul ( mantissa1, exponent1, mantissa2, exponent2, dec_digit ):

#*****************************************************************************80
#
## DEC_MUL multiplies two decimals.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    The routine computes
#
#      MANTISSA * 10^EXPONENT 
#      = ( MANTISSA1 * 10^EXPONENT1) * (MANTISSA2 * 10^EXPONENT2)
#      = ( MANTISSA1 * MANTISSA2 ) * 10^( EXPONENT1 + EXPONENT2 )
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
#    Input, integer MANTISSA1, EXPONENT1, the first multiplier.
#
#    Input, integer MANTISSA2, EXPONENT2, the second multiplier.
#
#    Input, integer DEC_DIGIT, the number of decimal digits.
#
#    Output, integer MANTISSA, EXPONENT, the product.
#
  import numpy as np
  from dec_round import dec_round
  from i4_huge import i4_huge
  from r8_to_dec import r8_to_dec

  i_max = i4_huge ( )
#
#  The result is zero if either MANTISSA1 or MANTISSA2 is zero.
#
  if ( mantissa1 == 0 or mantissa2 == 0 ):
    mantissa = 0
    exponent = 0
    return mantissa, exponent
#
#  The result is simple if either MANTISSA1 or MANTISSA2 is one.
#
  if ( abs ( mantissa1 ) == 1 or abs ( mantissa2 ) == 1 ):
    mantissa = mantissa1 * mantissa2
    exponent = exponent1 + exponent2
    return mantissa, exponent

  temp = np.log ( abs ( mantissa1 ) ) + np.log ( abs ( mantissa2 ) )

  if ( temp < np.log ( i_max ) ):

    mantissa = mantissa1 * mantissa2
    exponent = exponent1 + exponent2

  else:

    dval = mantissa1 * mantissa2

    mantissa3, exponent3 = r8_to_dec ( dval, dec_digit )

    mantissa = mantissa3
    exponent = exponent3 + ( exponent1 + exponent2 )

  mantissa, exponent = dec_round ( mantissa, exponent, dec_digit )

  return mantissa, exponent

def dec_mul_test ( ):

#*****************************************************************************80
#
## DEC_MUL_TEST tests DEC_MUL.
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
  print ( 'DEC_MUL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DEC_MUL multiplies two decimals.' )

  dec_digit = 2

  atop = 14
  abot = -4
  btop = 16
  bbot = 2

  ctop, cbot = dec_mul ( atop, abot, btop, bbot, dec_digit )

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
  print ( 'DEC_MUL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dec_mul_test ( )
  timestamp ( )
