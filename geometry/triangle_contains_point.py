#! /usr/bin/env python
#
def triangle_contains_point ( t, p ):

#*****************************************************************************80
#
## TRIANGLE_CONTAINS_POINT finds if a point is inside a triangle in 2D.
#
#  Discussion:
#
#    The routine assumes that the vertices are given in counter-clockwise
#    order.  If the triangle vertices are actually given in clockwise
#    order, this routine will behave as though the triangle contains
#    no points whatsoever!
#
#    The routine determines if a point P is "to the right of" each of the lines
#    that bound the triangle.  It does this by computing the cross product
#    of vectors from a vertex to its next vertex, and to P.
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
#    The vertices should be given in counter clockwise order.
#
#    Input, real P(2,1), the point to be checked.
#
#    Output, logical INSIDE, is TRUE if the point is inside
#    the triangle or on its boundary.
#
  from i4_wrap import i4_wrap

  inside = True

  for j in range ( 0, 3 ):

    jp1 = i4_wrap ( j + 1, 0, 2 )

    if ( 0.0 < ( p[0] - t[0,j] ) * ( t[1,jp1] - t[1,j] ) \
             - ( p[1] - t[1,j] ) * ( t[0,jp1] - t[0,j] ) ):
      inside = False
      return inside

  return inside

def triangle_contains_point_test ( ):

#*****************************************************************************80
#
## TRIANGLE_CONTAINS_POINT_TEST tests TRIANGLE_CONTAINS_POINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 June 2006
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print

  test_num = 7

  p_test = np.array ( [ \
    [ 0.25,   0.75,   1.00,  11.00,   0.00,   0.50,  0.60 ], \
    [ 0.25,   0.25,   1.00,   0.50,   1.00, -10.00,  0.60 ] ] )

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  p = np.zeros ( 2 )

  print ( '' )
  print ( 'TRIANGLE_CONTAINS_POINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_CONTAINS_POINT reports if a point' )
  print ( '  is inside a triangle' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( '     X       Y     Inside' )
  print ( '' )

  for j in range ( 0, test_num ):

    p[0] = p_test[0,j]
    p[1] = p_test[1,j]

    inside = triangle_contains_point ( t, p )

    print ( '  %10g  %10g  %s' % ( p[0], p[1], inside ) )
#
#  Make a copy of the triangle with vertices in reverse order.
#
  print ( '' )
  print ( '  Repeat the test, but reverse the triangle vertex ordering.' )
 
  t2 = np.zeros ( [ 2, 3 ] )
  for j in range ( 0, 3 ):
    for i in range ( 0, 2 ):
      t2[i,j] = t[i,2-j]

  r8mat_transpose_print ( 2, 3, t2, '  Triangle vertices (reversed):' )

  print ( '' )
  print ( '     X       Y     Inside' )
  print ( '' )

  for j in range ( 0, test_num ):

    p[0] = p_test[0,j]
    p[1] = p_test[1,j]

    inside = triangle_contains_point ( t2, p )

    print ( '  %10g  %10g  %s' % ( p[0], p[1], inside ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_CONTAINS_POINT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_contains_point_test ( )
  timestamp ( )

