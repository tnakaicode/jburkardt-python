#! /usr/bin/env python
#
def digit_to_ch ( digit ):

#*****************************************************************************80
#
## DIGIT_TO_CH returns the character representation of a decimal digit.
#
#  Example:
#
#    DIGIT   C
#    -----  ---
#      0    '0'
#      1    '1'
#    ...    ...
#      9    '9'
#     17    '*'
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer DIGIT, the digit value between 0 and 9.
#
#    Output, character C, the corresponding character, or '*' if DIGIT
#    was illegal.
#
  if ( 0 <= digit and digit <= 9 ):
    i0 = ord ( '0' )
    c = chr ( i0 + digit )
  else:
    c = '*'

  return c

def digit_to_ch_test ( ):

#*****************************************************************************80
#
## DIGIT_TO_CH_TEST tests DIGIT_TO_CH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from ch_to_digit import ch_to_digit

  print ( '' )
  print ( 'DIGIT_TO_CH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIGIT_TO_CH: decimal digit -> character.' )
  print ( '' )
 
  for i in range ( -2, 12 ):
    c = digit_to_ch ( i )
    i2 = ch_to_digit ( c )
    print ( '  %8d  "%c"  %8d' % ( i, c, i2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIGIT_TO_CH_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  digit_to_ch_test ( )
  timestamp ( )

