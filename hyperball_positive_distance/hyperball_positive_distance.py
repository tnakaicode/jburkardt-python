#! /usr/bin/env python3
#
def hyperball_positive_distance_histogram ( m, n ):

#*****************************************************************************80
#
## hyperball_positive_distance_histogram() histograms unit positive hyperball distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of samples to use.
#
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = hyperball_positive_sample ( m )
    q = hyperball_positive_sample ( m )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points in a unit positive hyperball' )
  filename = 'hyperball_positive_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def hyperball_positive_distance_stats ( m, n ):

#*****************************************************************************80
#
## hyperball_positive_distance_stats() estimates unit positive hyperball distance statistics.
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
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of sample points to use.
#
#  Output:
#
#    real MU, VAR, the estimated mean and variance of the
#    distance between two random points in the unit positive hyperball.
#
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = hyperball_positive_sample ( m )
    q = hyperball_positive_sample ( m )
    t[i] = np.linalg.norm ( p - q )

  mu = np.mean ( t )
  var = np.var ( t )

  print ( '' )
  print ( '  Using M = %d spatial dimension.' % ( m ) )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Estimated variance      = %g' % ( var ) )

  return mu, var

def hyperball_positive_distance_test ( ):

#*****************************************************************************80
#
## hyperball_positive_distance_test() tests hyperball_positive_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hyperball_positive_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hyperball_positive_distance().' )

  m = 20
  n = 10000
  mu, var = hyperball_positive_distance_stats ( m, n )

  m = 20
  n = 10000
  hyperball_positive_distance_histogram ( m, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'hyperball_positive_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def hyperball_positive_sample ( m ):

#*****************************************************************************80
#
## hyperball_positive_sample() returns sample points in the unit positive hyperball.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 August 2023
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
#    integer M, the spatial dimension.
#
#  Output:
#
#    real X(M), the point.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  x = rng.standard_normal ( size = m )
#
#  Normalize the vector.
#
  x = np.abs ( x ) / np.linalg.norm ( x )
#
#  Now compute a value to map the point ON the hypersphere INTO the hypersphere.
#
  r = rng.random ( )
 
  x = r ** ( 1.0 / m ) * x

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
  hyperball_positive_distance_test ( )
  timestamp ( )


