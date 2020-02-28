#! /usr/bin/env python
#
def dec_round ( mantissa, exponent, dec_digit ):

#*****************************************************************************80
#
## DEC_ROUND rounds a decimal fraction to a given number of digits.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    The routine takes an arbitrary decimal fraction makes sure that
#    MANTISSA has no more than DEC_DIGIT digits.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer MANTISSA, EXPONENT, the coefficient and exponent
#    of a decimal fraction.
#
#    Input, integer DEC_DIGIT, the number of decimal digits.
#
#    Output, integer MANTISSA, EXPONENT, the rounded data.
#    MANTISSA has no more than DEC_DIGIT decimal digits.
#
  if ( mantissa == 0 ):
    exponent = 0
    return mantissa, exponent

  while ( 10 ** dec_digit <= abs ( mantissa ) ):
    mantissa = int ( round ( mantissa / 10.0 ) )
    exponent = exponent + 1
#
#  Absorb trailing 0's into the exponent.
#
  while ( ( mantissa // 10 ) * 10 == mantissa ):
    mantissa = mantissa // 10
    exponent = exponent + 1

  return mantissa, exponent

def dec_round_test ( ):

#*****************************************************************************80
#
## DEC_ROUND_TEST tests DEC_ROUND.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_test = 7
  d_test = np.array ( [ 1, 2, 3, 4, 2, 3, 4 ] )
  exponent_test = np.array ( [ -1,  -1, -1, -1, 2, 2, 2 ] )
  mantissa_test = np.array ( [ 523, 523, 523, 523, 6340, 6340, 6340 ] )

  print ( '' )
  print ( 'DEC_ROUND_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DEC_ROUND "rounds" a decimal to a number of digits.' )
  print ( '' )
  print ( '           -----Before-------  -----After--------' )
  print ( '  Digits   Mantissa  Exponent  Mantissa  Exponent' )
  print ( '' )

  for i in range ( 0, n_test ):

    dec_digit = d_test[i]

    mantissa = mantissa_test[i]
    exponent = exponent_test[i]

    mantissa, exponent = dec_round ( mantissa, exponent, dec_digit )

    print ( '  %6d  %6d  %6d      %6d  %6d' \
      % ( dec_digit, mantissa_test[i], exponent_test[i], mantissa, exponent ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DEC_ROUND_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dec_round_test ( )
  timestamp ( )

