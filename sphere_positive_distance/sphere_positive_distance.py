#! /usr/bin/env python3
#
def sphere_positive_distance_histogram ( n ):

#*****************************************************************************80
#
## sphere_positive_distance_histogram() histograms unit positive sphere distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2023
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

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = sphere_positive_sample ( )
    q = sphere_positive_sample ( )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points on a unit positive sphere' )
  filename = 'sphere_positive_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def sphere_positive_distance_stats ( n ):

#*****************************************************************************80
#
## sphere_positive_distance_stats() estimates sphere distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2023
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
#    real MU, VAR, the estimated mean and variance of the
#    distance between two random points on the unit positive sphere.
#
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = sphere_positive_sample ( )
    q = sphere_positive_sample ( )
    t[i] = np.linalg.norm ( p - q )

  mu = np.mean ( t )
  var = np.var ( t )

  print ( '' )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Estimated variance      = %g'% ( var ) )

  return mu, var

def sphere_positive_distance_test ( ):

#*****************************************************************************80
#
## sphere_positive_distance_test() tests sphere_positive_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'sphere_positive_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test sphere_positive_distance().' )

  n = 10000
  mu, var = sphere_positive_distance_stats ( n )

  n = 10000
  sphere_positive_distance_histogram ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'sphere_positive_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def sphere_positive_sample ( ):

#*****************************************************************************80
#
## sphere_positive_sample() returns sample points on the unit positive sphere.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Russell Cheng,
#    Random Variate Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998, pages 168.
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Wiley, 1986, page 232.
#
#  Output:
#
#    real X(3), the point.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  x = rng.standard_normal ( size = 3 )
#
#  Normalize the vector.
#
  x = np.abs ( x ) / np.linalg.norm ( x )

  return x

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

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  sphere_positive_distance_test ( )
  timestamp ( )

