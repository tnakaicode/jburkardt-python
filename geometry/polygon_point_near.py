#! /usr/bin/env python
#
def polygon_point_near ( n, v, p ):

#*****************************************************************************80
#
## POLYGON_POINT_NEAR computes the nearest point on a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real V(2,N), the polygon vertices.
#
#    Input, real P(2), the point whose nearest polygon point
#    is to be determined.
#
#    Output, real PN(2), the nearest point to P.
#
#    Output, real DIST, the distance from the point to the polygon.
#
  import numpy as np
  from i4_wrap import i4_wrap
  from segment_point_near import segment_point_near
#
#  Find the distance to each of the line segments that make up the edges
#  of the polygon.
#
  dist = float ( 'inf' )

  pn = np.zeros ( 2 )
  p1 = np.zeros ( 2 )
  p2 = np.zeros ( 2 )

  for j in range ( 0, n ):

    jp1 = i4_wrap ( j + 1, 0, n - 1 )

    p1[0] = v[0,j]
    p1[1] = v[1,j]
    p2[0] = v[0,jp1]
    p2[1] = v[1,jp1]

    pn2, dist2, tval = segment_point_near ( p1, p2, p )

    if ( dist2 < dist ):
      dist = dist2
      pn[0] = pn2[0]
      pn[1] = pn2[1]

  return pn, dist

def polygon_point_near_test ( ):

#*****************************************************************************80
#
## POLYGON_POINT_NEAR_TEST tests POLYGON_POINT_NEAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print

  n = 3
 
  p_test = np.array ( [ \
    [ 4.0, 2.0, -2.0 ], \
    [ 5.0, 3.0, -1.0 ] ] )

  v = np.array ( [ \
    [ 1.0, 4.0, 2.0 ], \
    [ 1.0, 3.0, 5.0 ] ] )

  print ( '' )
  print ( 'POLYGON_POINT_NEAR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_POINT_NEAR computes nearest point on polygon.' )

  r8mat_transpose_print ( 2, n, v, '  Vertices of polygon:' )

  print ( '' )
  print ( '       X             Y             XN             YN' )
  print ( '' )

  p = np.zeros ( 2 )

  for test in range ( 0, 3 ):

    p[0] = p_test[0,test]
    p[1] = p_test[1,test]
    pn, dist = polygon_point_near ( n, v, p )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( p[0], p[1], pn[0], pn[1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_POINT_NEAR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_point_near_test ( )
  timestamp ( )
