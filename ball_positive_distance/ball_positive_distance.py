#! /usr/bin/env python3
#
def ball_positive_distance_histogram ( n ):

#*****************************************************************************80
#
## ball_positive_distance_histogram() histograms unit positive ball distances.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of samples to use.
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np

  rng = default_rng ( )

  t = np.zeros ( n )

  for i in range ( 0, n ):
    p = ball_positive_sample ( rng )
    q = ball_positive_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points in a unit positive ball' )
  filename = 'ball_positive_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def ball_positive_distance_stats ( n ):

#*****************************************************************************80
#
## ball_positive_distance_stats() estimates unit positive ball distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2023
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
#    distance between two random points in the unit ball.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = ball_positive_sample ( rng )
    q = ball_positive_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  mu = np.mean ( t )
  var = np.var ( t )

  print ( '' )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Estimated variance      = %g' % ( var ) )

  return mu, var

def ball_positive_distance_test ( ):

#*****************************************************************************80
#
## ball_positive_distance_test() tests ball_positive_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ball_positive_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ball_positive_distance().' )

  n = 10000
  [ mu, var ] = ball_positive_distance_stats ( n )

  n = 10000
  ball_positive_distance_histogram ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'ball_positive_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def ball_positive_sample ( rng ):

#*****************************************************************************80
#
## ball_positive_sample() returns sample points in the unit positive ball.
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
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(3), the point.
#
  import numpy as np

  x = rng.standard_normal ( size = 3 )
#
#  Normalize the vector.
#
  x = np.abs ( x ) / np.linalg.norm ( x )
#
#  Now compute a value to map the point ON the sphere INTO the sphere.
#
  r = rng.random ( )
 
  x = r ** ( 1.0 / 3.0 ) * x

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
  ball_positive_distance_test ( )
  timestamp ( )

