#! /usr/bin/env python
#
def ch_to_digit ( c ):

#*****************************************************************************80
#
## CH_TO_DIGIT returns the integer value of a base 10 digit.
#
#  Example:
#
#     C   DIGIT
#    ---  -----
#    '0'    0
#    '1'    1
#    ...  ...
#    '9'    9
#    ' '    0
#    'X'   -1
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
#    Input, character C, the decimal digit, '0' through '9' or blank
#    are legal.
#
#    Output, integer DIGIT, the corresponding integer value.  If C was
#    'illegal', then DIGIT is -1.
#
  i0 = ord ( '0' )
  i9 = ord ( '9' )
  ic = ord ( c )

  if ( i0 <= ic and ic <= i9 ):

    digit = ic - i0

  elif ( c == ' ' ):

    digit = 0

  else:

    digit = -1

  return digit

def ch_to_digit_test ( ):

#*****************************************************************************80
#
## CH_TO_DIGIT_TEST tests CH_TO_DIGIT.
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
  from digit_to_ch import digit_to_ch

  print ( '' )
  print ( 'CH_TO_DIGIT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CH_TO_DIGIT: character -> decimal digit' )
  print ( '' )
 
  for i in range ( -2, 12 ):
    c = digit_to_ch ( i )
    i2 = ch_to_digit ( c )
    print ( '  %8d  "%c"  %8d' % ( i, c, i2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CH_TO_DIGIT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ch_to_digit_test ( )
  timestamp ( )

