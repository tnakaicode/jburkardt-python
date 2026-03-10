#! /usr/bin/env python3
#
def hypercube_surface_distance_histogram ( n, d ):

#*****************************************************************************80
#
## hypercube_surface_distance_histogram() histograms hypercube surface distance statistics.
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
#    integer N, the number of samples to use.
#
#    integer D, the spatial dimension.
#
  import matplotlib.pyplot as plt
  import numpy as np

  p1 = hypercube_surface_sample ( n, d )
  p2 = hypercube_surface_sample ( n, d )
  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p1[i,:] - p2[i,:] )    

  bins = 40
  plt.hist ( t, bins = bins, rwidth = 0.95, \
    range = np.array ( [ 0.0, np.sqrt ( float ( d ) ) ] ), density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  title_string = \
    'Distance between random points on ' + str ( d ) + '-dimensional hypercube surface'
  plt.title ( title_string )
  return

def hypercube_surface_distance_stats ( n, d ):

#*****************************************************************************80
#
## hypercube_surface_distance_stats() estimates hypercube surface distance statistics.
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
#    integer N, the number of sample points to use.
#
#    integer D, the spatial dimension.
#
#  Output:
#
#    real MU, VAR, the estimated mean and variance of the
#    distance between two random points on the surface of the unit hypercube.
#
  import numpy as np

  p1 = hypercube_surface_sample ( n, d )
  p2 = hypercube_surface_sample ( n, d )
  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p1[i,:] - p2[i,:] )    

  mu = np.mean ( t )
  var = np.var ( t )

  return mu, var

def hypercube_surface_distance_test ( ):

#*****************************************************************************80
#
## hypercube_surface_distance_test() tests hypercube_surface_distance().
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
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'hypercube_surface_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hypercube_surface_distance()' )
  print ( '' )
  print ( '    D       Mu      Var' )
  print ( '' )
  n = 10000
  for d in range ( 2, 7 ):
    dmu, dvar = hypercube_surface_distance_stats ( n, d )
    print ( '  %2d  %8.4f  %8.4f' % ( d, dmu, dvar ) )

  n = 10000
  d = 5
  hypercube_surface_distance_histogram ( n, d )
  filename =  'hypercube_surface_distance_d' + str ( d ) + '_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hypercube_surface_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def hypercube_surface_sample ( n, d ):

#*****************************************************************************80
#
## hypercube_surface_sample() randomly selects points on the surface of a hypercube.
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
#    integer N, the number of points to sample.
#
#    integer D, the spatial dimension.
#
#  Output:
#
#    real P(N,D), N points selected uniformly at random from
#    the surface of the unit hypercube in D dimensions.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  p = rng.random ( size = [ n, d ] )

  for i in range ( 0, n ):
    j = rng.integers ( low = 0, high = d, endpoint = False )
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
  hypercube_surface_distance_test ( )
  timestamp ( )


