#! /usr/bin/env python3
#
def ellipse_distance_histogram ( n, a, b, rng ):

#*****************************************************************************80
#
## ellipse_distance_histogram() histograms ellipse distance statistics.
#
#  Discussion:
#
#    The ellipse will be assumed to have the form:
#
#      (x/a)^2 + (y/b)^2 = 1
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
#    real A, B, the ellipse parameters.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  p = ellipse_sample ( n, a, b, rng )
  q = ellipse_sample ( n, a, b, rng )

  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p[i] - q[i] )

  tmax = max ( np.abs ( a ), np.abs ( b ) )
  bins = 20
  plt.hist ( t, bins = bins, rwidth = 0.95, \
    range = np.array ( [ 0.0, tmax ] ), density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  label = 'Pairwise point distances on ellipse with a = ' \
    + str ( a ) + ', b = ' + str ( b )
  plt.title ( label )

  return

def ellipse_distance_stats ( n, a, b, rng ):

#*****************************************************************************80
#
## ellipse_distance_stats() estimates ellipse distance statistics.
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
#    real A, B, the ellipse parameters.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real MU, VAR, the estimated mean and variance of the
#    distance between two random points on the ellipse.
#
  import numpy as np

  p = ellipse_sample ( n, a, b, rng )
  q = ellipse_sample ( n, a, b, rng )

  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p[i] - q[i] )

  mu = np.mean ( t )
  var = np.var ( t )

  return mu, var

def ellipse_distance_test ( ):

#*****************************************************************************80
#
## ellipse_distance_test() tests ellipse_distance().
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
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'ellipse_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ellipse_distance()' )

  rng = default_rng ( )

  n = 10000
  a = 4.0
  b = 2.5
  mu, var = ellipse_distance_stats ( n, a, b, rng )
  print ( '' )
  print ( '  Using N =', n, 'sample points' )
  print ( '  Estimated mean distance = ', mu )
  print ( '  Estimated variance      = ', var )

  n = 10000
  a = 4.0
  b = 2.5
  ellipse_distance_histogram ( n, a, b, rng )
  filename = 'ellipse_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ellipse_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def ellipse_sample ( n, a, b, rng ):

#*****************************************************************************80
#
## ellipse_sample() returns randomly selected points on an ellipse.
#
#  Discussion:
#
#    The ellipse is assumed to have the equation:
#
#      (x/a)^2 + (y/b)^2 = 1
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
#    integer N, the number of points to compute.
#
#    real A, B: the ellipse parameters:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real P(N,2), points uniformly distributed on the perimeter of the ellipse.
#
  import numpy as np

  p = rng.random ( size = [ n, 2 ] )
  p[:,0] = a * p[:,0]
  p[:,1] = b * p[:,1]

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
  ellipse_distance_test ( )
  timestamp ( )


