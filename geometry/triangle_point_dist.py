#! /usr/bin/env python
#
def triangle_point_dist ( t, p ):

#*****************************************************************************80
#
## TRIANGLE_POINT_DIST: distance ( triangle, point ) in 2D.
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
#    Input, real T(2,3), the triangle vertices.
#
#    Input, real P(2), the point to be checked.
#
#    Output, real DIST, the distance from the point to the
#    triangle.
#
  import numpy as np
  from i4_wrap import i4_wrap
  from segment_point_dist import segment_point_dist

  p1 = np.zeros ( 2 )
  p2 = np.zeros ( 2 )
#
#  Find the distance to each of the line segments.
#
  dist = float ( 'inf' )

  for j in range ( 0, 3 ):

    jp1 = i4_wrap ( j + 1, 0, 2 )

    p1[0] = t[0,j]
    p1[1] = t[1,j]

    p2[0] = t[0,jp1]
    p2[1] = t[1,jp1]

    dist2 = segment_point_dist ( p1, p2, p )

    if ( dist2 < dist ):
      dist = dist2

  return dist

def triangle_point_dist_test ( ):

#*****************************************************************************80
#
## TRIANGLE_POINT_DIST_TEST tests TRIANGLE_POINT_DIST.
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
  from r8mat_transpose_print import r8mat_transpose_print

  ntest = 7

  ptest = np.array ( [ \
    [ 0.25, 0.75, 1.00, 11.00, 0.00,  0.50,  0.60 ], \
    [ 0.25, 0.25, 1.00,  0.50, 1.00, -10.00, 0.60 ] ] )

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  p = np.zeros ( 2 )

  print ( '' )
  print ( 'TRIANGLE_POINT_DIST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_POINT_DIST computes the distance' )
  print ( '  between a point and a triangle.' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( '       P       DIST' )
  print ( '' )

  for j in range ( 0, ntest ):

    p[0] = ptest[0,j]
    p[1] = ptest[1,j]

    dist = triangle_point_dist ( t, p )

    print ( '  %10g  %10g  %10g' % ( p[0], p[1], dist ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_POINT_DIST_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_point_dist_test ( )
  timestamp ( )

