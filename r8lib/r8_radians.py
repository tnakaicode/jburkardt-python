#! /usr/bin/env python3
#
def r8_radians ( degrees ):

#*****************************************************************************80
#
## R8_RADIANS converts an angle from degree to radian measure.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real RADIANS, the angle measurement in degrees.
#
#    Output, real VALUE, the angle measurement in radians.
#
  import numpy as np

  value = degrees * np.pi / 180.0

  return value

def r8_radians_test ( ):

#*****************************************************************************80
#
## R8_RADIANS_TEST tests R8_RADIANS.
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
  import numpy as np
  import platform

  test_num = 12

  print ( '' )
  print ( 'R8_RADIANS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_RADIANS converts an angle from degrees to radians.' )
  print ( '' )
  print ( '	 Degrees         Radians' )
  print ( '' )
  for test in range ( 0, 13 ):
    d = 180.0 * test / 12.0
    r = r8_radians ( d )
    print ( '  %14f  %14f' % ( d, r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_RADIANS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_radians_test ( )
  timestamp ( )
 
