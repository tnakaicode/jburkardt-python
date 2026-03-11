#! /usr/bin/env python3
#
def square_surface_distance_histogram ( n ):

#*****************************************************************************80
#
## square_surface_distance_histogram() histograms square surface distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of samples to use.
#
  import matplotlib.pyplot as plt
  import numpy as np

  p1 = square_surface_sample ( n )
  p2 = square_surface_sample ( n )
  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p1[i] - p2[i] )

  bins = 40
  plt.hist ( t, bins = bins, rwidth = 0.95, \
    range = np.array ( [ 0.0, np.sqrt ( 2.0 ) ] ), density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between random points on unit square surface' )

  return

def square_surface_distance_stats ( n ):

#*****************************************************************************80
#
## square_surface_distance_stats() estimates square surface distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of sample points to use.
#
#  Output:
#
#    real DMU, DVAR, the estimated mean and variance of the
#    distance between two random points on the surface of the unit square.
#
  import numpy as np

  p1 = square_surface_sample ( n )
  p2 = square_surface_sample ( n )
  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p1[i] - p2[i] )

  mu = np.mean ( t )
  var = np.var ( t )

  return mu, var

def square_surface_distance_test ( ):

#*****************************************************************************80
#
## square_surface_distance_test() tests square_surface_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'square_surface_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test square_surface_distance()' )
  print ( '' )
  print ( '  The mean distance between two random points on the surface' )
  print ( '  of a square can be computed as:' )
  print ( '    mu = ( 3 mu_diff + mu_same ) / 4' )
  print ( '  where:' )
  print ( '    mu_diff = mean distance, points are on different sides' )
  print ( '    mu_same = mean distance, points are on same side.' )

  n = 10000
  dmu, dvar = square_surface_distance_stats ( n )
  dmu_diff_exact = ( 2.0 + np.sqrt ( 2.0 ) \
    + 5.0 * np.log ( 1.0 + np.sqrt ( 2.0 ) ) ) / 9.0
  dmu_same_exact = 1.0 / 3.0
  dmu_exact = ( 3.0 * dmu_diff_exact + dmu_same_exact ) / 4.0
  print ( '' )
  print ( '  Using N = ', n, ' sample points' )
  print ( '  Exact mean distance (diff) = ', dmu_diff_exact )
  print ( '  Exact mean distance (same) = ', dmu_same_exact )
  print ( '  Exact mean distance        = ', dmu_exact )
  print ( '  Estimated mean distance    = ', dmu )
  print ( '  Estimated variance         = ', dvar )

  n = 10000
  square_surface_distance_histogram ( n )
  filename = 'square_surface_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'square_surface_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def square_surface_sample ( n ):

#*****************************************************************************80
#
## square_surface_sample() randomly selects points on the surface of a square.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points to sample.
#
#  Output:
#
#    real P(N,2), N points selected uniformly at random from
#    the surface of the unit square.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  p = rng.random ( size = [ n, 2 ] )
  for i in range ( 0, n ):
    j = rng.integers ( low = 0, high = 1, endpoint = True )
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
  square_surface_distance_test ( )
  timestamp ( )

