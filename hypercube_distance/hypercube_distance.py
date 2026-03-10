#! /usr/bin/env python3
#
def hypercube_distance_histogram ( m, n, rng ):

#*****************************************************************************80
#
## hypercube_distance_histogram() histograms hypercube distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2022
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
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  p1 = rng.random ( size = [ n, m ] )
  p2 = rng.random ( size = [ n, m ] )

  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p1[i,:] - p2[i,:] )

  bins = 20
  plt.hist ( t, bins = bins, rwidth = 0.95, \
    range = np.array ( [ 0.0, np.sqrt ( float ( m ) ) ] ), density = True )

  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  title_string = 'Distance between random points in a unit ' + str ( m ) + ' cube'
  plt.title ( title_string )

  return

def hypercube_distance_stats ( m, n, rng ):

#*****************************************************************************80
#
## hypercube_distance_stats() estimates hypercube distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2022
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
#    rng(): the current random number generator.
#
#  Output:
#
#    real MU, VAR, the estimated mean and variance of the
#    distance between two random points in the unit hypercube.
#
  import numpy as np

  p1 = rng.random ( size = [ n, m ] )
  p2 = rng.random ( size = [ n, m ] )

  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p1[i] - p2[i] )

  mu = np.mean ( t )
  var = np.var ( t )

  return mu, var

def hypercube_distance_test ( ):

#*****************************************************************************80
#
## hypercube_distance_test() tests hypercube_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 January 2021
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
  print ( 'hypercube_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hypercube_distance()' )

  rng = default_rng ( )

  print ( '' )
  print ( '   M      N      Mu        Var' )
  print ( '' )
  n = 10000
  for m in range ( 2, 11 ):
    mu, var = hypercube_distance_stats ( m, n, rng )
    print ( '  %2d  %4d  %8.4f  %8.4f' % ( m, n, mu, var ) )

  print ( '' )
  n = 10000
  for m in range ( 2, 11 ):
    hypercube_distance_histogram ( m, n, rng )
    filename = 'hypercube_distance_histogram_' + str ( m ) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.show ( block = False )
    plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hypercube_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def hypercube_unit_sample ( m, n, rng ):

#*****************************************************************************80
#
## hypercube_unit_sample() returns N random points in the unit hypercube.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 March 2022
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
#    rng(): the current random number generator.
#
#  Output:
#
#    real T(M,N), N random points in the M-dimensional unit hypercube.
#
  import numpy as np

  p = rng.random ( size = [ m, n ] )

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
  hypercube_distance_test ( )
  timestamp ( )

