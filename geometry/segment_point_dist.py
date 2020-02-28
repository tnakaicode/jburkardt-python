#! /usr/bin/env python
#
def segment_point_dist ( p1, p2, p ):

#*****************************************************************************80
#
## SEGMENT_POINT_DIST: distance ( line segment, point ) in 2D.
#
#  Discussion:
#
#    A line segment is the finite portion of a line that lies between
#    two points.
#
#    The nearest point will satisfy the condition
#
#      PN = (1-T) * P1 + T * P2.
#
#    T will always be between 0 and 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real P1(2), P2(2), the endpoints of the line segment.
#
#    Input, real P(2), the point whose nearest neighbor on the line
#    segment is to be determined.
#
#    Output, real DIST, the distance from the point to the line segment.
#
  import numpy as np
#
#  If the line segment is actually a point, then the answer is easy.
#
  if ( p1[0] == p2[0] and p1[1] == p2[1] ):

    t = 0.0

  else:

    bot = ( p2[0] - p1[0] ) ** 2 + ( p2[1] - p1[1] ) ** 2

    t = ( ( p[0] - p1[0] ) * ( p2[0] - p1[0] ) \
        + ( p[1] - p1[1] ) * ( p2[1] - p1[1] ) ) / bot

    t = max ( t, 0.0 )
    t = min ( t, 1.0 )

  pn = np.zeros ( 2 )

  pn[0] = p1[0] + t * ( p2[0] - p1[0] )
  pn[1] = p1[1] + t * ( p2[1] - p1[1] )

  dist = np.sqrt ( ( pn[0] - p[0] ) ** 2 + ( pn[1] - p[1] ) ** 2 )

  return dist

def segment_point_dist_test ( ):

#*****************************************************************************80
#
## SEGMENT_POINT_DIST_TEST tests SEGMENT_POINT_DIST;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'SEGMENT_POINT_DIST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SEGMENT_POINT_DIST computes the distance from a point to a line segment.' )

  p1 = np.array ( [ 1.0, 2.0 ] )
  p2 = np.array ( [ 3.0, 4.0 ] )

  r8vec_print ( 2, p1, '  Segment endpoint 1:' )
  r8vec_print ( 2, p2, '  Segment endpoint 2:' )

  p = np.array ( [ 2.0, 3.0 ] )
  dist = segment_point_dist ( p1, p2, p )
  r8vec_print ( 2, p, '  Test point P' )
  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  p = np.array ( [ 4.0, 5.0 ] )
  dist = segment_point_dist ( p1, p2, p )
  r8vec_print ( 2, p, '  Test point P' )
  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  p = np.array ( [ 1.0, 4.0 ] )
  dist = segment_point_dist ( p1, p2, p )
  r8vec_print ( 2, p, '  Test point P' )
  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )

  p = np.array ( [ 0.0, 0.0 ] )
  dist = segment_point_dist ( p1, p2, p )
  r8vec_print ( 2, p, '  Test point P' )
  print ( '' )
  print ( '  Distance to segment = %g' % ( dist ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SEGMENT_POINT_DIST_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  segment_point_dist_test ( )
  timestamp ( )

