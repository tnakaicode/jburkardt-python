#! /usr/bin/env python
#
def polygon_area_2 ( n, v ):

#*****************************************************************************80
#
## POLYGON_AREA_2 computes the area of a polygon.
#
#  Discussion:
#
#    The area is the sum of the areas of the triangles formed by
#    node N with consecutive pairs of nodes.
#
#    If the vertices are given in counterclockwise order, the area
#    will be positive.  If the vertices are given in clockwise order,
#    the area will be negative.
#
#    Thanks to Martin Pineault for noticing that an earlier version
#    of this routine would not correctly compute the area of a nonconvex
#    polygon.
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
#  Reference:
#
#    Adrian Bowyer, John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Parameters:
#
#    Input, integer N, the number of vertices of the polygon.
#
#    Input, real V(2,N), the vertices.
#
#    Output, real AREA, the area of the polygon.
#
  import numpy as np
  from triangle_area import triangle_area

  area = 0.0

  for i in range ( 0, n - 2 ):

    t = np.array ( [ [ v[0,i], v[0,i+1], v[0,n-1] ], \
                     [ v[1,i], v[1,i+1], v[1,n-1] ] ] )

    area_triangle = triangle_area ( t )

    area = area + area_triangle

  return area

def polygon_area_2_test ( ):

#*****************************************************************************80
#
## POLYGON_AREA_2_TEST tests POLYGON_AREA_2.
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

  test_num = 2
  area_exact_test = np.array ( [ 2.0, 6.0 ] )
  n_test = np.array ( [ 4, 8 ] )

  print ( '' )
  print ( 'POLYGON_AREA_2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_AREA_2 computes the area of a polygon.' )

  for test in range ( 0, test_num ):

    n = n_test[test]
    area_exact = area_exact_test[test]

    if ( test == 0 ):

      v = np.array ( [ \
        [ 1.0, 2.0, 1.0, 0.0 ], \
        [ 0.0, 1.0, 2.0, 1.0 ] ] )

    elif ( test == 1 ):

      v = np.array ( [ \
        [ 0.0, 3.0, 3.0, 2.0, 2.0, 1.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 3.0, 3.0, 1.0, 1.0, 2.0, 2.0 ] ] )

    print ( '' )
    print ( '  Number of polygonal vertices = %d' % ( n ) )

    r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

    area = polygon_area_2 ( n, v )

    print ( '' )
    print ( '  Exact area is        %g' % ( area_exact ) )
    print ( '  The computed area is %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_AREA_2_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_area_2_test ( )
  timestamp ( )
