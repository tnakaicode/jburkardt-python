#! /usr/bin/env python
#
def triangle_point_near ( t, p ):

#*****************************************************************************80
#
## TRIANGLE_POINT_NEAR computes the nearest point on a triangle in 2D.
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
#    Input, real T(2,3), the triangle vertices.
#
#    Input, real P(2), the point whose nearest triangle point
#    is to be determined.
#
#    Output, real PN(2), the nearest point to P.
#
#    Output, real DIST, the distance from the point to the
#    triangle.
#
  import numpy as np
  from i4_wrap import i4_wrap
  from segment_point_near import segment_point_near

  pn = np.zeros ( 2 )
  p1 = np.zeros ( 2 )
  p2 = np.zeros ( 2 )
#
#  Find the distance to each of the line segments that make up the edges
#  of the triangle.
#
  dist = float ( 'inf' )

  for j in range ( 0, 3 ):

    jp1 = i4_wrap ( j + 1, 0, 2 )

    p1[0] = t[0,j]
    p1[1] = t[1,j]


    p2[0] = t[0,jp1]
    p2[1] = t[1,jp1]

    pn2, dist2, tval = segment_point_near ( p1, p2, p )

    if ( dist2 < dist ):
      dist = dist2;
      pn[0] = pn2[0]
      pn[1] = pn2[1]

  return pn, dist

def triangle_point_near_test ( ):

#*****************************************************************************80
#
## TRIANGLE_POINT_NEAR_TEST tests TRIANGLE_POINT_NEAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2010
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
    [ 0.25, 0.75, 1.00, 11.00, 0.00,   0.50, 0.60 ], \
    [ 0.25, 0.25, 1.00,  0.50, 1.00, -10.00, 0.60 ] ] )

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'TRIANGLE_POINT_NEAR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_POINT_NEAR computes the nearest' )
  print ( '  triangle point to a point.' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( '           P                PN' )
  print ( '' )

  p = np.zeros ( 2 )

  for j in range ( 0, ntest ):

    p[0] = ptest[0,j]
    p[1] = ptest[1,j]

    [ pn, dist ] = triangle_point_near ( t, p );

    print ( '  %10g  %10g    %10g  %10g' % ( p[0], p[1], pn[0], pn[1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_POINT_NEAR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_point_near_test ( )
  timestamp ( )
 
