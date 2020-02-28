#! /usr/bin/env python
#
def polygon_contains_point_2 ( n, v, p ):

#*****************************************************************************80
#
## POLYGON_CONTAINS_POINT_2 finds if a point is inside a convex polygon.
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
#    Input, integer N, the number of nodes or vertices in the polygon.
#    N must be at least 3.
#
#    Input, real V(2,N), the coordinates of the vertices of the polygon.
#
#    Input, real P(2), the coordinates of the point to be tested.
#
#    Output, logical INSIDE, is TRUE if the point is inside the polygon.
#
  import numpy as np
  from triangle_contains_point_1 import triangle_contains_point_1

  inside = False
#
#  A point is inside a convex polygon if and only if it is inside
#  one of the triangles formed by X(1),Y(1) and any two consecutive
#  points on the polygon's circumference.
#
  t = np.zeros ( [ 2, 3 ] )

  t[0,0] = v[0,0]
  t[1,0] = v[1,0]

  for i in range ( 1, n - 1 ):

    t[0,1] = v[0,i]
    t[1,1] = v[1,i]
    t[0,2] = v[0,i+1]
    t[1,2] = v[1,i+1]

    inside = triangle_contains_point_1 ( t, p )

    if ( inside ):
      break

  return inside

def polygon_contains_point_2_test ( ):

#*****************************************************************************80
#
## POLYGON_CONTAINS_POINT_2_TEST tests POLYGON_CONTAINS_POINT_2.
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
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print

  n = 5
  test_num = 4

  p_test = np.array ( [ \
    [ 1.0, 3.0, 0.0, 0.5 ], \
    [ 1.0, 4.0, 2.0, -0.25 ] ] )

  v = np.array ( [ \
    [ 0.0, 1.0, 2.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 2.0, 2.0 ] ] )
 
  p = np.zeros ( 2 )

  print ( '' )
  print ( 'POLYGON_CONTAINS_POINT_2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_CONTAINS_POINT_2 determines if' )
  print ( '  a point is in a polygon.' )

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  print ( '' )
  print ( '          P          Inside' )
  print ( '' )

  for test in range ( 0, test_num ):
 
    p[0] = p_test[0,test]
    p[1] = p_test[1,test]
 
    inside = polygon_contains_point_2 ( n, v, p )

    print ( '  %14.6g  %14.6g    %d' % ( p[0], p[1], inside ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_CONTAINS_POINT_2_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_contains_point_2_test ( )
  timestamp ( )
