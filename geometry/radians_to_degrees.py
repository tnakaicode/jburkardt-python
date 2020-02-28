#! /usr/bin/env python
#
def radians_to_degrees ( radians ):

#*****************************************************************************80
#
## RADIANS_TO_DEGREES converts an angle from radians to degrees.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real RADIANS, an angle in radians.
#
#    Output, real VALUE, the equivalent angle in degrees.
#
  import numpy as np

  value = ( radians / np.pi ) * 180.0

  return value

def radians_to_degrees_test ( ):

#*****************************************************************************80
#
## RADIANS_TO_DEGREES_TEST tests RADIANS_TO_DEGREES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2018
#
#  Author:
#
#    John Burkardt
#
  from degrees_to_radians import degrees_to_radians

  print ( '' )
  print ( 'RADIANS_TO_DEGREES_TEST' )
  print ( '  RADIANS_TO_DEGREES converts an angle from radians' )
  print ( '  to degrees;' )
  print ( '' )
  print ( '  Degrees     Radians     Degrees' )
  print ( '' )

  for i in range ( -2, 15 ):
    angle_deg = float ( 30 * i )
    angle_rad = degrees_to_radians ( angle_deg )
    angle_deg2 = radians_to_degrees ( angle_rad )
    print ( '  %10f  %10f  %10f' % ( angle_deg, angle_rad, angle_deg2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  radians_to_degrees_test ( )
  timestamp ( )

