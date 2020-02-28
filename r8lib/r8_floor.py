#! /usr/bin/env python3
#
def r8_floor ( x ):

#*****************************************************************************80
#
## R8_FLOOR rounds an R8 down to the nearest integral R8.
#
#  Example:
#
#    X         Value
#
#   -1.1      -2.0
#   -1.0      -1.0
#   -0.9      -1.0
#   -0.1      -1.0
#    0.0       0.0
#    0.1       0.0
#    0.9       0.0
#    1.0       1.0
#    1.1       1.0
#    2.9       2.0
#    3.0       3.0
#    3.14159   3.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number to be rounded down.
#
#    Output, real VALUE, the rounded value of X.
#
  from math import floor

  value = floor ( x )

  return value

def r8_floor_test ( ):

#*****************************************************************************80
#
## R8_FLOOR_TEST tests R8_FLOOR.
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
  print ( 'R8_FLOOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FLOOR returns the "floor" of a real number.' )
  print ( '' )
  print ( '        X           R8_FLOOR(X)' )
  print ( '' )

  seed = 123456789

  for test in range ( 1, 11 ):
    x, seed = r8_uniform_ab ( -10.0, +10.0, seed )
    x2 = r8_floor ( x )
    print ( '  %12f  %12f' % ( x, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FLOOR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_floor_test ( )
  timestamp ( )
