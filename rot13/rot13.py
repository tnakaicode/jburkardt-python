#! /usr/bin/env python3
#
def ch_to_rot13 ( ch ):

#*****************************************************************************80
#
## CH_TO_ROT13 converts a character to its ROT13 equivalent.
#
#  Discussion:
#
#    Two applications of CH_TO_ROT13 to a character will return the original.!
#
#    As a further scrambling, digits are similarly rotated using
#    a "ROT5" scheme.
#
#  Example:
#
#    Input:  Output:
#
#    a       n
#    C       P
#    J       W
#    1       6
#    5       0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, character CH, the character to be converted.
#
#    Output, character VALUE, the ROT13 equivalent of the character.
#
  i = ord ( ch )
#
#  [0:4] -> [5:9]
#
  if ( 48 <= i and i <= 52 ):
    value = i + 5
#
#  [5:9] -> [0:4]
#
  elif ( 53 <= i and i <= 57 ):
    value = i - 5
#
#  [A:M] -> [N:Z]
#
  elif ( 65 <= i and i <= 77 ):
    value = i + 13
#
#  [N:Z] -> [A:M]
#
  elif ( 78 <= i and i <= 90 ):
    value = i - 13
#
#  [a:m] -> [n:z]
#
  elif ( 97 <= i and i <= 109 ):
    value = i + 13
#
#  [n:z] -> [a:m]
#
  elif ( 110 <= i and i <= 122 ):
    value = i - 13
  else:
    value = i
 
  value = chr ( value )

  return value

def ch_to_rot13_test ( ):

#*****************************************************************************80
#
## CH_TO_ROT13_TEST tests CH_TO_ROT13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CH_TO_ROT13_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CH_TO_ROT13 "encodes" characters using ROT13' )
  print ( '  (and digits using ROT5).' )
  print ( '  A second application of the function returns the' )
  print ( '  original character.' )

  s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  s1_length = len ( s1 )
  s2 = ''
  s3 = ''

  for i in range ( 0, s1_length ):
    s2 = s2 + ch_to_rot13 ( s1[i] )
    s3 = s3 + ch_to_rot13 ( s2[i] )

  print ( '' )
  print ( '            CH  : %s' % ( s1 ) )
  print ( '      ROT13(CH) : %s' % ( s2 ) )
  print ( 'ROT13(ROT13(CH)): %s' % ( s3 ) )

  s1 = 'CH_TO_ROT13 "encodes" characters using ROT13'
  s1_length = len ( s1 )
  s2 = ''
  s3 = ''

  for i in range ( 0, s1_length ):
    s2 = s2 + ch_to_rot13 ( s1[i] )
    s3 = s3 + ch_to_rot13 ( s2[i] )

  print ( '' )
  print ( '            CH  : %s' % ( s1 ) )
  print ( '      ROT13(CH) : %s' % ( s2 ) )
  print ( 'ROT13(ROT13(CH)): %s' % ( s3 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CH_TO_ROT13_TEST:' )
  print ( '  Normal end of execution.' )
  return

def rot13_test ( ):

#*****************************************************************************80
#
## ROT13_TEST tests the ROT13 library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ROT13_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the ROT13 library.' )

  ch_to_rot13_test ( )
  s_quote_test ( )
  s_to_rot13_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROT13_TEST:' )
  print ( '  Normal end of execution.' )
  return

def s_quote ( s1, mark ):

#*****************************************************************************80
#
## S_QUOTE "quotes" a string.
#
#  Discussion:
#
#    Actually, it simply puts the string MARK before and after the string S1.
#
#    Sometimes, when you print a string, you want to put quote marks around it.
#    This is one way to do that.
#
#  Examples:
#
#    S1        MARK  S2
#    --------  ----  ----------
#    Hi, Bob!  "     "Hi, Bob!"
#    De        Loop  LoopDeLoop
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   30 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S1, a string to be "quoted".
#
#    Input, string MARK, the "quote mark".
#
#    Output, string S2, the "quoted" string.
#
  s2 = mark + s1 + mark

  return s2

def s_quote_test ( ):

#*****************************************************************************80
#
## S_QUOTE_TEST tests S_QUOTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'S_QUOTE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  S_QUOTE quotes a string S1 with a mark MARK.' )
  print ( '' )
  print ( '  ----S1----  ---MARK---  ----S2----' )
  print ( '' )

  s1 = 'Hi, Bob!'
  mark = '"'
  s2 = s_quote ( s1, mark )
  print ( '  %-10s  %-10s  %-10s' % ( s1, mark, s2 ) )

  s1 = 'De'
  mark = 'Loop'
  s2 = s_quote ( s1, mark )
  print ( '  %-10s  %-10s  %-10s' % ( s1, mark, s2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'S_QUOTE_TEST' )
  print ( '  Normal end of execution.' )
  return

def s_to_rot13 ( s1 ):

#*****************************************************************************80
#
## S_TO_ROT13 "rotates" the alphabetical characters in a string by 13 positions.
#
#  Discussion:
#
#    Two applications of the routine will return the original string.
#
#  Examples:
#
#    Input:                      Output:
#
#    abcdefghijklmnopqrstuvwxyz  nopqrstuvwxyzabcdefghijklm
#    Cher                        Pure
#    James Thurston Howell       Wnzrf Guhefgba Ubjryy
#    0123456789                  56789012345
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   30 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S1, a string to be "rotated".
#
#    Output, string S2, the rotated string.
#
  s1_length = len ( s1 )
  s2 = ''

  for i in range ( 0, s1_length ):
    s2 = s2 + ch_to_rot13 ( s1[i] )
 
  return s2

def s_to_rot13_test ( ):

#*****************************************************************************80
#
## S_TO_ROT13_TEST tests S_TO_ROT13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'S_TO_ROT13_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  S_TO_ROT13 applies the ROT13 cipher to a string.' )

  print ( '' )
  print ( '  S2 = S_TO_ROT13 ( S1 ).' )
  print ( '' )
  print ( '  -------------------S1-------------------  -------------------S2-------------------' )
  print ( '' )

  s1 = 'abcdefghijklmnopqrstuvwxyz'
  s2 = s_to_rot13 ( s1 )
  s1 = s_quote ( s1, '"' )
  s2 = s_quote ( s2, '"' )
  print ( '  %-40s  %-40s' % ( s1, s2 ) )

  s1 = 'Cher'
  s2 = s_to_rot13 ( s1 )
  s1 = s_quote ( s1, '"' )
  s2 = s_quote ( s2, '"' )
  print ( '  %-40s  %-40s' % ( s1, s2 ) )

  s1 = 'James Thurston Howell III'
  s2 = s_to_rot13 ( s1 )
  s1 = s_quote ( s1, '"' )
  s2 = s_quote ( s2, '"' )
  print ( '  %-40s  %-40s' % ( s1, s2 ) )

  s1 = 'The bill is $1,205,837.49 so pay now!'
  s2 = s_to_rot13 ( s1 )
  s1 = s_quote ( s1, '"' )
  s2 = s_quote ( s2, '"' )
  print ( '  %-40s  %-40s' % ( s1, s2 ) )

  print ( '' )
  print ( '  S2 = S_TO_ROT13 ( S1 ).' )
  print ( '  S3 = S_TO_ROT13 ( S2 ).' )
  print ( '' )
  print ( '  -------------------S1-------------------  -------------------S3-------------------' )
  print ( '' )

  s1 = 'abcdefghijklmnopqrstuvwxyz'
  s2 = s_to_rot13 ( s1 )
  s3 = s_to_rot13 ( s2 )
  s1 = s_quote ( s1, '"' )
  s3 = s_quote ( s3, '"' )
  print ( '  %-40s  %-40s' % ( s1, s3 ) )

  s1 = 'Cher'
  s2 = s_to_rot13 ( s1 )
  s3 = s_to_rot13 ( s2 )
  s1 = s_quote ( s1, '"' )
  s3 = s_quote ( s3, '"' )
  print ( '  %-40s  %-40s' % ( s1, s3 ) )

  s1 = 'James Thurston Howell III'
  s2 = s_to_rot13 ( s1 )
  s3 = s_to_rot13 ( s2 )
  s1 = s_quote ( s1, '"' )
  s3 = s_quote ( s3, '"' )
  print ( '  %-40s  %-40s' % ( s1, s3 ) )

  s1 = 'The bill is $1,205,837.49 so pay now!'
  s2 = s_to_rot13 ( s1 )
  s3 = s_to_rot13 ( s2 )
  s1 = s_quote ( s1, '"' )
  s3 = s_quote ( s3, '"' )
  print ( '  %-40s  %-40s' % ( s1, s3 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'S_TO_ROT13_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  rot13_test ( )
  timestamp ( )

