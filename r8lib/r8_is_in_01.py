#! /usr/bin/env python3
#
def r8_is_in_01 ( x ):

#*****************************************************************************80
#
## R8_IS_IN_01 is TRUE if the value is in the range [0,1].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the value.
#
#    Output, boolean VALUE, is TRUE if 0 <= X <= 1.
#
  value = ( 0.0 <= x and x <= 1.0 )

  return value

def r8_is_in_01_test ( ):

#*****************************************************************************80
#
## R8_IS_IN_01_TEST tests R8_IS_IN_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'R8_IS_IN_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_IS_IN_01 reports whether an R8 is in [0,1].' )
  print ( '' )
  print ( '      R8    R8_IS_IN_01?' )
  print ( '' )

  seed = 123456789
  for i in range ( 0, 10 ):
    r8, seed = r8_uniform_ab ( -1.0, 2.0, seed )
    check = r8_is_in_01 ( r8 )
    print ( '  %8.2f  %s' % ( r8, check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_IS_IN_01_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_is_in_01_test ( )
  timestamp ( )
