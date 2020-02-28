#! /usr/bin/env python
#
def polygon_centroid_2 ( n, v ):

#*****************************************************************************80
#
## POLYGON_CENTROID_2 computes the centroid of a polygon.
#
#  Discussion:
#
#    The centroid is the area-weighted sum of the centroids of
#    disjoint triangles that make up the polygon.
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
#    Adrian Bowyer and John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Parameters:
#
#    Input, integer N, the number of sides of the polygon.
#
#    Input, real V(2,N), the coordinates of the vertices.
#
#    Output, real CENTROID(2), the coordinates of the centroid.
#
  import numpy as np
  from triangle_area import triangle_area

  area = 0.0
  centroid = np.zeros ( 2 )

  for i in range ( 0, n - 2 ):

    t = np.array ( [ [ v[0,i], v[0,i+1], v[0,n-1] ], \
                     [ v[1,i], v[1,i+1], v[1,n-1] ] ] )

    area_triangle = triangle_area ( t )

    area = area + area_triangle

    centroid[0] = centroid[0] + ( v[0,i] + v[0,i+1] + v[0,n-1] ) * area_triangle / 3.0
    centroid[1] = centroid[1] + ( v[1,i] + v[1,i+1] + v[1,n-1] ) * area_triangle / 3.0

  if ( area == 0.0 ):
    centroid[0] = v[0]
    centroid[1] = v[1]
  else:
    centroid[0] = centroid[0] / area
    centroid[1] = centroid[1] / area

  return centroid

def polygon_centroid_2_test ( ):

#*****************************************************************************80
#
## POLYGON_CENTROID_2_TEST tests POLYGON_CENTROID_2.
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
  from r8vec_print import r8vec_print

  n = 4
  v = np.array ( [ \
    [ 1.0, 2.0, 1.0, 0.0 ], \
    [ 0.0, 1.0, 2.0, 1.0 ] ] )

  print ( '' )
  print ( 'POLYGON_CENTROID_2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_CENTROID_2 computes the centroid of a polygon.' )

  r8mat_transpose_print ( 2, n, v, '  The polygon vertices:' )

  centroid = polygon_centroid_2 ( n, v )

  r8vec_print ( 2, centroid, '  POLYGON_CENTROID_2:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_CENTROID_2_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_centroid_2_test ( )
  timestamp ( )
