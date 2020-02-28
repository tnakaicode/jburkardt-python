#! /usr/bin/env python
#
def degrees_to_radians ( degrees ):

#*****************************************************************************80
#
## DEGREES_TO_RADIANS converts an angle from degrees to radians.
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
#    Input, real DEGREES, an angle in degrees.
#
#    Output, real VALUE, the equivalent angle in radians.
#
  import numpy as np

  value = ( degrees / 180.0 ) * np.pi

  return value

def degrees_to_radians_test ( ):

#*****************************************************************************80
#
## DEGREES_TO_RADIANS_TEST tests DEGREES_TO_RADIANS.
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
  from radians_to_degrees import radians_to_degrees

  print ( '' )
  print ( 'DEGREES_TO_RADIANS_TEST' )
  print ( '  DEGREES_TO_RADIANS converts an angle from degrees' )
  print ( '  to radians;' )
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
  degrees_to_radians_test ( )
  timestamp ( )

