#! /usr/bin/env python
#
def triangle_contains_point_1 ( t, p ):

#*****************************************************************************80
#
## TRIANGLE_CONTAINS_POINT_1 finds if a point is inside a triangle.
#
#  Discussion:
#
#    It is conventional to list the triangle vertices in counter clockwise
#    order.  However, this routine does not require a particular order
#    for the vertices.
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
#    Input, real T(2,3), the triangle vertices.
#
#    Input, real P(2,1), the point to be checked.
#
#    Output, logical INSIDE, is TRUE if the point is inside
#    the triangle or on its boundary.
#
  from triangle_barycentric import triangle_barycentric

  xsi = triangle_barycentric ( t, p )

  if ( xsi[0] < 0.0 or xsi[1] < 0.0 or xsi[2] < 0.0 ):
    inside = False
  else:
    inside = True

  return inside

def triangle_contains_point_1_test ( ):

#*****************************************************************************80
#
## TRIANGLE_CONTAINS_POINT_1_TEST tests TRIANGLE_CONTAINS_POINT_1.
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
  print ( 'TRIANGLE_CONTAINS_POINT_1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_CONTAINS_POINT_1 reports if a point' )
  print ( '  is inside a triangle' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( '     X       Y     Inside' )
  print ( '' )

  for j in range ( 0, test_num ):

    p[0] = p_test[0,j]
    p[1] = p_test[1,j]

    inside = triangle_contains_point_1 ( t, p )

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

    inside = triangle_contains_point_1 ( t2, p )

    print ( '  %10g  %10g  %s' % ( p[0], p[1], inside ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_CONTAINS_POINT_1_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_contains_point_1_test ( )
  timestamp ( )

