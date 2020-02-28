#! /usr/bin/env python3
#
def r8_sign_char ( r8 ):

#*****************************************************************************80
#
## R8_SIGN_CHAR returns the sign of an R8 as a character.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R8, the value whose sign is of interest.
#
#    Output, character C, is '-', '0', or '+'.

  if ( r8 < 0.0 ):
    c = '-'
  elif ( r8 == 0.0 ):
    c = '0'
  else:
    c = '+'

  return c

def r8_sign_char_test ( ):

#*****************************************************************************80
#
## R8_SIGN_CHAR_TEST tests R8_SIGN_CHAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'R8_SIGN_CHAR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SIGN_CHAR returns the sign of an R8 as a character.' )
  print ( '' )
  print ( '      R8      R8_SIGNCHAR(R8)' )
  print ( '' )

  seed = 123456789

  for test in range ( 0, 10 ):
    r8, seed = r8_uniform_ab ( -5.0, +5.0, seed )
    s = r8_sign_char ( r8 )
    print ( '  %10f    %s' % ( r8, s ) )
#
#  Terminate.
# 
  print ( '' )
  print ( 'R8_SIGN_CHAR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_sign_char_test ( )
  timestamp ( )
 
