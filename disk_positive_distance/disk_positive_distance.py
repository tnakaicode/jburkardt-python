#! /usr/bin/env python3
#
def disk_positive_distance_histogram ( n, rng ):

#*****************************************************************************80
#
## disk_positive_distance_histogram() histograms positive disk distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 August 2023
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

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = disk_positive_sample ( rng )
    q = disk_positive_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points in a unit positive disk' )
  filename = 'disk_positive_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
 
  return

def disk_positive_distance_stats ( n, rng ):

#*****************************************************************************80
#
## disk_positive_distance_stats() estimates disk distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 August 2023
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
#    distance between two random points in the unit disk.
#
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = disk_positive_sample ( rng )
    q = disk_positive_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  mu = np.mean ( t )
  var = np.var ( t )

  print ( '' )
  print ( '  Using N = ', n, ' sample points,' )
  print ( '  Estimated mean distance = ', mu )
  print ( '  Estimated variance      = ', var )

  return mu, var

def disk_positive_distance_test ( ):

#*****************************************************************************80
#
## disk_positive_distance_test() tests disk_positive_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2019
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk_positive_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test disk_distance().' )

  rng = default_rng ( )
  n = 10000
  mu, var = disk_positive_distance_stats ( n, rng )

  n = 10000
  disk_positive_distance_histogram ( n, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk_positive_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def disk_positive_sample ( rng ):

#*****************************************************************************80
#
## disk_positive_sample() uniformly samples the unit positive disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real P[2]: a point selected uniformly at random from
#    the positive disk of radius 1 and center (0,0).
#
  import numpy as np

  theta = 0.5 * np.pi * rng.random ( )
  r = np.sqrt ( rng.random ( ) )
  x = np.abs ( r * np.cos ( theta ) )
  y = np.abs ( r * np.sin ( theta ) )
  p = np.array ( [ x, y ] )

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
#    06 April 2013
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
  disk_positive_distance_test ( )
  timestamp ( )

