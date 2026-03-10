#! /usr/bin/env python3
#
def circle_positive_distance_test ( ):

#*****************************************************************************80
#
## circle_positive_distance_test() tests circle_positive_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2023
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'circle_positive_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test circle_positive_distance().' )

  rng = default_rng ( )

  n = 10000
  mu, var = circle_positive_distance_stats ( n, rng )

  n = 10000
  circle_positive_distance_histogram ( n, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'circle_positive_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def circle_positive_distance_histogram ( n, rng ):

#*****************************************************************************80
#
## circle_positive_distance_histogram() histograms positive circle distance statistics.
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

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = circle_positive_sample ( rng )
    q = circle_positive_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  plt.clf ( )
  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points on a unit positive circle' )
  filename = 'circle_positive_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
 
  return

def circle_positive_distance_stats ( n, rng ):

#*****************************************************************************80
#
## circle_positive_distance_stats() estimates positive circle distance statistics.
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
#    integer n: the number of sample points to use.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real mu, var: the estimated mean and variance of the
#    distance between two random points on the unit circle.
#
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = circle_positive_sample ( rng )
    q = circle_positive_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  mu = np.mean ( t )
  var = np.var ( t )

  mu_exact = 4.0 / np.pi
  print ( '' )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Exact mean distance     = %g' % ( mu_exact ) )
  print ( '  Estimated variance      = %g' % ( var ) )

  return mu, var

def circle_positive_sample ( rng ):

#*****************************************************************************80
#
## circle_positive_sample() selects a random point on the positive unit circle.
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
#    rng(): the current random number generator.
#
#  Output:
#
#    real p(2): a point selected uniformly at random from
#    the circle of radius 1 and center (0,0).
#
  import numpy as np

  theta = 2.0 * np.pi * rng.random ( )
  x = np.abs ( np.cos ( theta ) )
  y = np.abs ( np.sin ( theta ) )

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
  circle_positive_distance_test ( )
  timestamp ( )

