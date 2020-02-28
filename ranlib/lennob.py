#! /usr/bin/env python
#
def lennob ( s ):

#*****************************************************************************80
#
## LENNOB returns the length of a character string to the last nonblank.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S, a string.
#
#    Output, integer LEN_TRIM, the length of the string to the last nonblank.
#
  n = len ( s )

  for i in range ( n - 1, -1, -1 ):
    if ( s[i] != ' ' ):
      value = i + 1
      return value

  value = 0
  return value

def lennob_test ( ):

#*****************************************************************************80
#
## LENNOB_TEST tests LENNOB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LENNOB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LENNOB returns the length of string to the last nonblank.' )
  print ( '' )
  print ( '  LEN  LENNOB  ---------S---------' )
  print ( '' )

  s = 'Hi, Bob!'
  l1 = len ( s )
  l2 = lennob ( s )
  print ( '   %2d          %2d  "%s"' % ( l1, l2, s[0:l1] ) )

  s = '  How   are   you?     '
  l1 = len ( s )
  l2 = lennob ( s )
  print ( '   %2d          %2d  "%s"' % ( l1, l2, s[0:l1] ) )

  s = '    '
  l1 = len ( s )
  l2 = lennob ( s )
  print ( '   %2d          %2d  "%s"' % ( l1, l2, s[0:l1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LENNOB_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lennob_test ( )
  timestamp ( )

