#! /usr/bin/env python3
#
def cube_surface_distance_histogram ( n, rng ):

#*****************************************************************************80
#
## cube_surface_distance_histogram() histograms cube surface distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of samples to use.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  p1 = cube_surface_sample ( n, rng )
  p2 = cube_surface_sample ( n, rng )
  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p1[i] - p2[i] )

  bins = 40
  plt.hist ( t, bins = bins, rwidth = 0.95, \
    range = np.array ( [ 0.0, np.sqrt ( 3.0 ) ] ), density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between random points on unit cube surface' )

  return

def cube_surface_distance_stats ( n, rng ):

#*****************************************************************************80
#
## cube_surface_distance_stats() estimates cube surface distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of sample points to use.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real MU, VAR, the estimated mean and variance of the
#    distance between two random points on the surface of the unit cube.
#
  import numpy as np

  p1 = cube_surface_sample ( n, rng )
  p2 = cube_surface_sample ( n, rng )
  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p1[i] - p2[i] )

  mu = np.mean ( t )
  var = np.var ( t )

  return mu, var

def cube_surface_distance_test ( ):

#*****************************************************************************80
#
## cube_surface_distance_test() tests cube_surface_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'cube_surface_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test cube_surface_distance()' )

  rng = default_rng ( )

  print ( '' )
  print ( '  The mean distance between two random points on the surface' )
  print ( '  of a cube can be computed as:' )
  print ( '    mu = ( 5 mu_diff + mu_same ) / 6' )
  print ( '  where:' )
  print ( '    mu_diff = mean distance, points are on different faces' )
  print ( '    mu_same = mean distance, points are on same face.' )

  n = 10000
  dmu, dvar = cube_surface_distance_stats ( n, rng )
  dmu_diff_exact = 0.9263900551740467
  dmu_same_exact = ( 2.0 + np.sqrt ( 2.0 ) \
    + 5.0 * np.log ( 1.0 + np.sqrt ( 2.0 ) ) ) / 15.0
  dmu_exact = ( 5.0 * dmu_diff_exact + dmu_same_exact ) / 6.0
  print ( '' )
  print ( '  Using N =', n, 'sample points,' )
  print ( '  Exact mean distance (diff) =', dmu_diff_exact )
  print ( '  Exact mean distance (same) =', dmu_same_exact )
  print ( '  Exact mean distance        =', dmu_exact )
  print ( '  Estimated mean distance    =', dmu )
  print ( '  Estimated variance         =', dvar )

  n = 10000
  cube_surface_distance_histogram ( n, rng )
  filename = 'cube_surface_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'cube_surface_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def cube_surface_sample ( n, rng ):

#*****************************************************************************80
#
## cube_surface_sample() randomly selects points on the surface of a cube.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points to sample.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real P(N,3), N points selected uniformly at random from
#    the surface of the unit cube.
#
  import numpy as np

  p = rng.random ( size = [ n, 3 ] )

  for i in range ( 0, n ):
    j = rng.integers ( low = 0, high = 2, endpoint = True )
    s = rng.integers ( low = 0, high = 1, endpoint = True )
    p[i,j] = float ( s )

  return p

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

if ( __name__ == '__main__' ):
  timestamp ( )
  cube_surface_distance_test ( )
  timestamp ( )

