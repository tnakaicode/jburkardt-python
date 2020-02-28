#! /usr/bin/env python
#
def angle_degree ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## ANGLE_DEGREE returns the degree angle defined by three points.
#
#  Discussion:
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
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X1, Y1, X2, Y2, X3, Y3, the coordinates of the points
#    P1, P2, P3.
#
#    Output, real VALUE, the angle swept out by the rays, measured
#    in degrees.  0 <= VALUE < 360.  If either ray has zero length,
#    then VALUE is set to 0.
#
  import numpy as np

  x = ( x3 - x2 ) * ( x1 - x2 ) + ( y3 - y2 ) * ( y1 - y2 )

  y = ( x3 - x2 ) * ( y1 - y2 ) - ( y3 - y2 ) * ( x1 - x2 )

  if ( x == 0.0 and y == 0.0 ):
    value = 0.0
    return value

  value = np.arctan2 ( y, x )

  if ( value < 0.0 ):
    value = value + 2.0 * np.pi

  value = 180.0 * value / np.pi

  return value

def angle_degree_test ( ):

#*****************************************************************************80
#
## ANGLE_DEGREE_TEST tests ANGLE_DEGREE.
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
  print ( 'ANGLE_DEGREE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ANGLE_DEGREE computes an angle;' )
  print ( '' )
  print ( '           X           Y       Theta  atan2(y,x)  ANGLE_DEGREE' )
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

    t1 = np.arctan2 ( y1, x1 ) * 180.0 / np.pi

    t2 = angle_degree ( x1, y1, x2, y2, x3, y3 )

    print ( '  %10f  %10f  %10f  %10f  %10f' \
      % ( x1, y1, thetad, t1, t2 ) )

  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  angle_degree_test ( )
  timestamp ( )

