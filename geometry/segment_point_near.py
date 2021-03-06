#! /usr/bin/env python
#
def segment_point_near ( p1, p2, p ):

#*****************************************************************************80
#
## SEGMENT_POINT_NEAR finds the line segment point nearest a point in 2D.
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
#    25 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real P1(2,1), P2(2,1), the endpoints of the line segment.
#
#    Input, real P(2,1), the point whose nearest neighbor
#    on the line segment is to be determined.
#
#    Output, real PN(2,1), the point on the line segment which is
#    nearest the point (X,Y).
#
#    Output, real DIST, the distance from the point to the
#    nearest point on the line segment.
#
#    Output, real T, the relative position of the point (XN,YN)
#    to the points (X1,Y1) and (X2,Y2).
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

  return pn, dist, t

def segment_point_near_test ( ):

#*****************************************************************************80
#
## SEGMENT_POINT_NEAR_TEST tests SEGMENT_POINT_NEAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 July 2018
#
#  Author:
#
#    John Burkardt
#
  from r8vec_uniform_01 import r8vec_uniform_01

  test_num = 3
  seed = 123456789

  print ( '' )
  print ( 'SEGMENT_POINT_NEAR_TEST' )
  print ( '  SEGMENT_POINT_NEAR computes the nearest point' )
  print ( '  from a line segment to a point in 2D.' )

  for test in range ( 0, test_num ):

    p1, seed = r8vec_uniform_01 ( 2, seed )
    p2, seed = r8vec_uniform_01 ( 2, seed )
    p, seed = r8vec_uniform_01 ( 2, seed )

    pn, dist, t = segment_point_near ( p1, p2, p )

    print ( '' )
    print ( '  TEST = %d' % ( test ) )
    print ( '  P1 =   %12f  %12f' % ( p1[0], p1[1] ) )
    print ( '  P2 =   %12f  %12f' % ( p2[0], p2[1] ) )
    print ( '  P =    %12f  %12f' % ( p[0], p[1] ) )
    print ( '  PN =   %12f  %12f' % ( pn[0], pn[1] ) )
    print ( '  DIST = %12f' % ( dist ) )
    print ( '  T =    %12f' % ( t ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SEGMENT_POINT_NEAR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  segment_point_near_test ( )
  timestamp ( )


