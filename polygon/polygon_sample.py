#! /usr/bin/env python3
#
def polygon_sample ( nv, v, n, seed ):

#*****************************************************************************80
#
## POLYGON_SAMPLE uniformly samples a polygon.
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
#    Input, integer NV, the number of vertices.
#
#    Input, real V(2,NV), the vertices of the polygon, listed in
#    counterclockwise order.
#
#    Input, integer N, the number of points to create.
#
#    Input/output, integer SEED, a seed for the random
#    number generator.
#
#    Output, real S(2,N), the points.
#
  import numpy as np
  from polygon_triangulate import polygon_triangulate
  from r8_uniform_01 import r8_uniform_01
  from r8vec_uniform_01 import r8vec_uniform_01
  from triangle_area import triangle_area
#
#  Triangulate the polygon.
#
  x = np.zeros ( nv )
  y = np.zeros ( nv )
  for j in range ( 0, nv ):
    x[j] = v[0,j]
    y[j] = v[1,j]

  triangles = polygon_triangulate ( nv, x, y )
#
#  Determine the areas of each triangle.
#
  area_triangle = np.zeros ( nv - 2 )

  area_polygon = 0.0
  for i in range ( 0, nv - 2 ):
    area_triangle[i] = triangle_area ( \
      v[0,triangles[i,0]], v[1,triangles[i,0]], \
      v[0,triangles[i,1]], v[1,triangles[i,1]], \
      v[0,triangles[i,2]], v[1,triangles[i,2]] )
    area_polygon = area_polygon + area_triangle[i]
#
#  Normalize the areas.
#
  area_relative = np.zeros ( nv - 1 )

  for i in range ( 0, nv - 2 ):
    area_relative[i] = area_triangle[i] / area_polygon
#
#  Replace each area by the sum of itself and all previous ones.
#
  area_cumulative = np.zeros ( nv - 2 )

  area_cumulative[0] = area_relative[0]
  for i in range ( 1, nv - 2 ):
    area_cumulative[i] = area_relative[i] + area_cumulative[i-1]

  s = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
#
#  Choose triangle I at random, based on areas.
#
    area_percent, seed = r8_uniform_01 ( seed )

    for k in range ( 0, nv - 2 ):

      i = k

      if ( area_percent <= area_cumulative[k] ):
        break
#
#  Now choose a point at random in triangle I.
#
    r, seed = r8vec_uniform_01 ( 2, seed )

    if ( 1.0 < r[0] + r[1] ):
      r[0] = 1.0 - r[0]
      r[1] = 1.0 - r[1]

    s[0,j] = ( 1.0 - r[0] - r[1] ) * v[0,triangles[i,0]] \
                   + r[0]          * v[0,triangles[i,1]] \
                          + r[1]   * v[0,triangles[i,2]]

    s[1,j] = ( 1.0 - r[0] - r[1] ) * v[1,triangles[i,0]] \
                   + r[0]          * v[1,triangles[i,1]] \
                          + r[1]   * v[1,triangles[i,2]]

  return s, seed

def polygon_sample_test ( ):

#*****************************************************************************80
#
## POLYGON_SAMPLE_TEST tests POLYGON_SAMPLE.
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
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print

  n = 20
  nv = 6
  v = np.array ( [ \
    [ 0.0, 2.0, 2.0, 1.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 1.0, 2.0, 1.0 ] ] )

  print ( '' )
  print ( 'POLYGON_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_SAMPLE samples a polygon.' )

  seed = 123456789

  x, seed = polygon_sample ( nv, v, n, seed )

  r8mat_transpose_print ( 2, n, x, '  Sample points:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_sample_test ( )
  timestamp ( )

