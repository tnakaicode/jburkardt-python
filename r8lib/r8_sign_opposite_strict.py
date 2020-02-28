#! /usr/bin/env python3
#
def r8_sign_opposite_strict ( r1, r2 ):

#*****************************************************************************80
#
## R8_SIGN_OPPOSITE_STRICT is TRUE if two R8's are strictly of opposite sign.
#
#  Discussion:
#
#    This test could be coded numerically as
#
#      if ( r1 * r2 < 0.0 ) then ...
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
#    Input, real R1, R2, the values to check.
#
#    Output, logical R8_SIGN_OPPOSITE_STRICT, is TRUE if ( R1 < 0 and 0 < R2 )
#    or ( R2 < 0 and 0 < R1 ).
#
  value = ( r1 < 0.0 and 0.0 < r2 ) or ( r2 < 0.0 and 0.0 < r1 );

  return value

def r8_sign_opposite_strict_test ( ):

#*****************************************************************************80
#
## R8_SIGN_OPPOSITE_STRICT_TEST tests R8_SIGN_OPPOSITE_STRICT.
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
  print ( 'R8_SIGN_OPPOSITE_STRICT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SIGN_OPPOSITE_STRICT is TRUE if two R8\'s have opposite signs.' )
  print ( '' )
  print ( '        R1        R2        OppositeStrict(R1,R2)?' )
  print ( '' )

  seed = 123456789
  for test in range ( 0, 21 ):

    if ( ( test % 4 ) == 0 ):
      r1 = 0.0
    else:
      r1, seed = r8_uniform_ab ( -10.0, +10.0, seed )

    if ( ( test % 10 ) == 0 ):
      r2 = 0.0
    else:
      r2, seed = r8_uniform_ab ( -10.0, +10.0, seed )
    s = r8_sign_opposite_strict ( r1, r2 )
    print ( '  %8.4f  %8.4f  %s' % ( r1, r2, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SIGN_OPPOSITE_STRICT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_sign_opposite_strict_test ( )
  timestamp ( )
 
