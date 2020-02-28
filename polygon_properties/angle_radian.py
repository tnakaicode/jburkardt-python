#! /usr/bin/env python
#
def angle_radian ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## ANGLE_RADIAN returns the angle swept out between two rays.
#
#  Discussion:
#
#    Except for the zero angle case, it should be true that
#
#      ANGLE_RADIAN(P1,P2,P3) + ANGLE_RADIAN(P3,P2,P1) = 2 * PI
#
#        P1
#        /
#       /
#      /
#     /
#    P2--------->P3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X1, Y1, X2, Y2, X3, Y3, define the rays
#    P1 - P2 and P3 - P2 which in turn define the angle.
#
#    Output, real VALUE, the angle swept out by the rays, measured
#    in radians.  0 <= VALUE < 2*PI.  If either ray has zero length,
#    then VALUE is set to 0.
#
  import numpy as np
  from r8_atan import r8_atan

  p = np.zeros ( 2 )

  p[0] = ( x3 - x2 ) * ( x1 - x2 ) \
       + ( y3 - y2 ) * ( y1 - y2 )

  p[1] = ( x3 - x2 ) * ( y1 - y2 ) \
       - ( y3 - y2 ) * ( x1 - x2 )

  if ( p[0] == 0.0 and p[1] == 0.0 ):
    value = 0.0
    return value

  value = r8_atan ( p[1], p[0] )

  if ( value < 0.0 ):
    value = value + 2.0 * np.pi

  return value

def angle_radian_test ( ):

#*****************************************************************************80
#
## ANGLE_RADIAN_TEST tests ANGLE_RADIAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n_angle = 12

  print ( '' )
  print ( 'ANGLE_RADIAN_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ANGLE_RADIAN computes an angle in radians;' )
  print ( '' )
  print ( '           X           Y       Theta  atan2(y,x)  ANGLE_RADIAN' )
  print ( '' )

  x2 = 0.0
  y2 = 0.0
  x3 = 1.0
  y3 = 0.0

  for i in range ( 0, n_angle + 1 ):

    thetad = float ( i ) * 360.0       / float ( n_angle )
    thetar = float ( i ) * 2.0 * np.pi / float ( n_angle )

    x1 = np.cos ( thetar )
    y1 = np.sin ( thetar )

    t1 = np.arctan2 ( y1, x1 )

    t2 = angle_radian ( x1, y1, x2, y2, x3, y3 )

    print ( '  %10f  %10f  %10f  %10f  %10f' \
      % ( x1, y1, thetad, t1, t2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  angle_radian_test ( )
  timestamp ( )

