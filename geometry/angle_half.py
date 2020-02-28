#! /usr/bin/env python
#
def angle_half ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## ANGLE_HALF finds half an angle.
#
#  Discussion:
#
#    The original angle is defined by the sequence of points P1, P2 and P3.
#
#    The point P4 is calculated so that:
#
#      (P1,P2,P4) = (P1,P2,P3) / 2
#
#        P1
#        /
#       /   P4
#      /  .
#     / .
#    P2--------->P3
#
#    Thanks to Cesar Fraga Bobis for pointing out a typographical error in
#    a previous version of this routine.
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
#    Input, real X1, Y1, X2, Y2, X2, Y3, points defining the angle.
#
#    Input, real P4(2), a point defining the half angle.
#    The vector P4 - P2 will have unit norm.
#
  import numpy as np

  p4 = np.zeros ( 2 )

  norm12 = np.sqrt ( ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2 )
  norm32 = np.sqrt ( ( x3 - x2 ) ** 2 + ( y3 - y2 ) ** 2 ) 

  x4 = 0.5 * ( ( x1 - x2 ) / norm12 + ( x3 - x2 ) / norm32 )

  y4 = 0.5 * ( ( y1 - y2 ) / norm12 + ( y3 - y2 ) / norm32 )

  norm = np.sqrt ( x4 ** 2 + y4 ** 2 )

  p4[0] = x2 + x4 / norm
  p4[1] = y2 + y4 / norm

  return p4

def angle_half_test ( ):

#*****************************************************************************80
#
## ANGLE_HALF_TEST tests ANGLE_HALF.
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
  from angle_radian import angle_radian

  n_angle = 12

  print ( '' )
  print ( 'ANGLE_HALF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ANGLE_HALF is given P1, P2, P3, forming an angle;' )
  print ( '  It finds P4 so P4, P2, P3 is half the angle.' )
  print ( '' )
  print ( '  Original Angle    Half Angle' )
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

    p4 = angle_half ( x1, y1, x2, y2, x3, y3 )
    x4 = p4[0]
    y4 = p4[1]

    t3 = angle_radian ( x4, y4, x2, y2, x3, y3 )

    print ( '  %10f  %10f' % ( t2, t3 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  angle_half_test ( )
  timestamp ( )

