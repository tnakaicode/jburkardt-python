#! /usr/bin/env python3
#
def polygon_distance_histogram ( n, nv, v ):

#*****************************************************************************80
#
## polygon_distance_histogram() histograms polygon distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of samples to use.
#
#    integer NV, the number of vertices.
#
#    real v[nv,2]: the vertices.
#
  import matplotlib.pyplot as plt
  import numpy as np

  p1 = polygon_sample ( nv, v, n )
  p2 = polygon_sample ( nv, v, n ) 

  d = np.zeros ( [ n, 2 ] )
  for i in range ( 0, n ):
    d[i] = np.linalg.norm ( p1[i] - p2[i] )

  bins = 20

  plt.clf ( )
  plt.hist ( d, bins, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points in a polygon' )

  return

def polygon_distance_histogram_test ( ):

#*****************************************************************************80
#
## polygon_distance_histogram_test() tests polygon_distance_histogram().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 December 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'polygon_distance_histogram_test()' )
  print ( '  Test polygon_distance_histogram().' )

  nv = 10

  v = np.array ( [ \
    [0.0, 0.0], \
    [0.5, 0.3], \
    [1.0, 0.0], \
    [0.7, 0.4], \
    [1.0, 0.6], \
    [0.6, 0.6], \
    [0.5, 1.0], \
    [0.4, 0.6], \
    [0.0, 0.6], \
    [0.3, 0.4] ] )

  print ( '' )
  print ( '  Polygonal vertices:' ) 
  print ( v )

  n = 10000
  plt.clf ( )
  polygon_distance_histogram ( n, nv, v )

  filename = 'polygon_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def polygon_distance_stats ( n, nv, v ):

#*****************************************************************************80
#
## polygon_distance_stats() estimates polygon distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of sample points to use.
#
#    integer NV, the number of vertices.
#
#    real v[nv,2]: the vertices.
#
#  Output:
#
#    real D_MEAN, D_VAR, D_MIN, D_MAX, the mean, variance,
#    minimum and maximum of the sample values.
#
  import numpy as np

  p1 = polygon_sample ( nv, v, n )
  p2 = polygon_sample ( nv, v, n ) 

  d = np.zeros ( [ n, 2 ] )
  for i in range ( 0, n ):
    d[i] = np.linalg.norm ( p1[i] - p2[i] )

  d_mean = np.mean ( d )
  d_var = np.var ( d )
  d_min = np.min ( d )
  d_max = np.max ( d )

  return d_mean, d_var, d_min, d_max

def polygon_distance_stats_test ( ):

#*****************************************************************************80
#
## polygon_distance_stats_test() tests polygon_distance_stats().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'polygon_distance_stats_test():' )
  print ( '  Test polygon_distance_stats().' )

  nv = 10

  v = np.array ( [ \
    [0.0, 0.0], \
    [0.5, 0.3], \
    [1.0, 0.0], \
    [0.7, 0.4], \
    [1.0, 0.6], \
    [0.6, 0.6], \
    [0.5, 1.0], \
    [0.4, 0.6], \
    [0.0, 0.6], \
    [0.3, 0.4] ] )

  print ( '' )
  print ( '  Polygonal vertices:' )
  print ( v )

  n = 10000
  d_mean, d_var, d_min, d_max = polygon_distance_stats ( n, nv, v )

  print ( '' )
  print ( '  N    =', n )
  print ( '  Min  =', d_min )
  print ( '  Mean =', d_mean )
  print ( '  Max  =', d_max )
  print ( '  Var  =', d_var )

  return

def polygon_distance_test ( ):

#*****************************************************************************80
#
## polygon_distance_test() tests polygon_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'polygon_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polygon_distance().' )

  polygon_sample_test ( )

  polygon_distance_stats_test ( )

  polygon_distance_histogram_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def polygon_sample ( nv, v, n ):

#*****************************************************************************80
#
## polygon_sample() uniformly samples a polygon.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NV, the number of vertices.
#
#    real v[nv,2]: the vertices.
#
#    integer N, the number of points to create.
#
#  Output:
#
#    real s[n,2], the points.
#
  from numpy.random import default_rng
  from polygon_triangulate import polygon_triangulate
  import numpy as np

  rng = default_rng ( )

  s = np.zeros ( [ n, 2 ] )
#
#  Triangulate the polygon.
#
  triangles = polygon_triangulate ( nv, v[:,0], v[:,1] )
#
#  Determine the areas of each triangle.
#
  area_triangle = np.zeros ( nv - 2 )

  for i in range ( 0, nv - 2 ):
    area_triangle[i] = triangle_area ( \
      v[triangles[i,0],0], v[triangles[i,0],1], \
      v[triangles[i,1],0], v[triangles[i,1],1], \
      v[triangles[i,2],0], v[triangles[i,2],1] )
#
#  Normalize the areas.
#
  area_polygon = np.sum ( area_triangle )

  area_relative = np.zeros ( nv - 2 )
  area_relative = area_triangle / area_polygon
#
#  Replace each area by the sum of itself and all previous ones.
#
  area_cumulative = np.zeros ( nv - 2 )
  area_cumulative[0] = area_relative[0]
  for i in range ( 1, nv - 2 ):
    area_cumulative[i] = area_relative[i] + area_cumulative[i-1]

  for j in range ( 0, n ):
#
#  Choose triangle I at random, based on areas.
#
    area_percent = rng.random ( )

    for k in range ( 0, nv - 2 ):

      i = k

      if ( area_percent <= area_cumulative[k] ):
        break
#
#  Now choose a point at random in triangle I.
#
    r = rng.random ( 2 )

    if ( 1.0 < np.sum ( r ) ):
      r = 1.0 - r

    s[j,0:2] = ( 1.0 - r[0] - r[1] ) * v[triangles[i,0],:] \
                     + r[0]          * v[triangles[i,1],:] \
                            + r[1]   * v[triangles[i,2],:]

  return s

def polygon_sample_test ( ):

#*****************************************************************************80
#
## polygon_sample_test() tests polygon_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 December 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'polygon_sample_test():' )
  print ( '  Test polygon_sample().' )

  nv = 10

  v = np.array ( [ \
    [0.0, 0.0], \
    [0.5, 0.3], \
    [1.0, 0.0], \
    [0.7, 0.4], \
    [1.0, 0.6], \
    [0.6, 0.6], \
    [0.5, 1.0], \
    [0.4, 0.6], \
    [0.0, 0.6], \
    [0.3, 0.4] ] )

  print ( '' )
  print ( '  Polygonal vertices:' )
  print ( v )

  npoly = 100
  p = polygon_sample ( nv, v, npoly )

  perimeter_x = np.append ( v[:,0], v[0,0] )
  perimeter_y = np.append ( v[:,1], v[0,1] )

  plt.clf ( )
  plt.plot ( perimeter_x, perimeter_y, 'k-', linewidth = 3 )
  plt.plot ( p[:,0], p[:,1], 'r*' )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- Y -->' )
  plt.title ( 'Polygon sample points' )
  plt.axis ( 'equal' )
  filename = 'polygon_sample_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

def triangle_area ( xa, ya, xb, yb, xc, yc ):

#*****************************************************************************80
#
## triangle_area() computes the signed area of a triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, the vertices.
#
#  Output:
#
#    real AREA, the signed area of the triangle.
#
  area = 0.5 * ( ( xb - xa ) * ( yc - ya ) \
               - ( xc - xa ) * ( yb - ya ) )

  return area

if ( __name__ == '__main__' ):
  timestamp ( )
  polygon_distance_test ( )
  timestamp ( )

