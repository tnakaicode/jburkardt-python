#! /usr/bin/env python3
#
def r8_unswap3 ( x, y, z ):

#*****************************************************************************80
#
## R8_UNSWAP3 unswaps three R8's.
#
#  Example:
#
#    Input:
#
#      X = 2, Y = 3, Z = 1
#
#    Output:
#
#      X = 1, Y = 2, Z = 3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, Y, Z, three values to be swapped.
#
#    Output, real X, Y, Z, the swapped values.
#
  w = z
  z = y
  y = x
  x = w

  return x, y, z

def r8_unswap3_test ( ):

#*****************************************************************************80
#
## R8_UNSWAP3_TEST tests R8_UNSWAP3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_swap3 import r8_swap3

  print ( '' )
  print ( 'R8_UNSWAP3_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNSWAP3 unswaps three reals.' )

  x = 1.0
  y = 3.14159
  z = 1952.0

  print ( '' )
  print ( '  Data :    %g  %g  %g' % ( x, y, z ) )
  x, y, z = r8_swap3 ( x, y, z )

  print ( '  Swap :    %g  %g  %g' % ( x, y, z ) )

  x, y, z = r8_unswap3 ( x, y, z )
  print ( '  Unswap :  %g  %g  %g' % ( x, y, z ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNSWAP3_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_unswap3_test ( )
  timestamp ( )

