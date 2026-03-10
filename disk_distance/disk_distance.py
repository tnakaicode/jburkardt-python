#! /usr/bin/env python3
#
def disk_distance_compare ( n, rng ):

#*****************************************************************************80
#
## disk_distance_compare() compares disk distance PDF's.
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
    p = disk_unit_sample ( rng )
    q = disk_unit_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )

  d = np.linspace ( 0.0, 2.0, 101 )
  dh = d / 2.0
  pdf = ( 16.0 / np.pi ) * dh * ( np.arccos ( dh ) - dh * np.sqrt ( 1.0 - dh**2 ) )
  pdf = pdf / 2.0
  plt.plot ( d, pdf, 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Relative frequency -->' )
  plt.title ( 'Compare observed and theoretical PDF' )
  filename = 'disk_distance_compare.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
 
  return

def disk_distance_histogram ( n, rng ):

#*****************************************************************************80
#
## disk_distance_histogram() histograms disk distance statistics.
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
    p = disk_unit_sample ( rng )
    q = disk_unit_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points in a unit disk' )
  filename = 'disk_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
 
  return

def disk_distance_pdf ( ):

#*****************************************************************************80
#
## disk_distance_pdf() plots the PDF for the disk distance problem.
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
#  Reference:
#
#    John Hammersley,
#    The distribution of distance in a hypersphere,
#    The Annals of Mathematical Statistics,
#    Volume 21, Number 3, pages 447-452, 1950.
#
  import matplotlib.pyplot as plt
  import numpy as np

  d = np.linspace ( 0.0, 2.0, 101 )
#
#  The PDF is typically given in terms of a normalized distance 0 <= Lambda <= 1.
#  We prefer to look at the physical distance 0 <= D <= 2.
#  To exploit the formula in its original form, we need to divide D by 2 first,
#  evaluate the PDF, and then divide that by 2.
#
  dh = d / 2.0
  pdf = ( 16.0 / np.pi ) * dh * ( np.arccos ( dh ) - dh * np.sqrt ( 1.0 - dh**2 ) )
  pdf = pdf / 2.0

  plt.plot ( d, pdf, 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Probability -->' )
  plt.title ( 'PDF for distance between pairs of random points in disk' )
  filename = 'disk_distance_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def disk_distance_stats ( n, rng ):

#*****************************************************************************80
#
## disk_distance_stats() estimates disk distance statistics.
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
    p = disk_unit_sample ( rng )
    q = disk_unit_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  mu = np.mean ( t )
  var = np.var ( t )

  print ( '' )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Exact mean distance     = %g' % ( 128 / 45 / np.pi ) )
  print ( '  Estimated variance      = %g' % ( var ) )
  print ( '  Exact variance          = %g' % ( ( 2025 * np.pi**2 - 128**2 ) / 45**2 / np.pi**2 ) )

  return mu, var

def disk_distance_test ( ):

#*****************************************************************************80
#
## disk_distance_test() tests disk_distance().
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
  print ( 'disk_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test disk_distance().' )

  rng = default_rng ( )

  n = 10000
  mu, var = disk_distance_stats ( n, rng )

  n = 10000
  disk_distance_histogram ( n, rng )

  disk_distance_pdf ( )

  n = 10000
  disk_distance_compare ( n, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def disk_unit_sample ( rng ):

#*****************************************************************************80
#
## disk_unit_sample() returns a randomly selected point from the unit disk.
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
#    the disk of radius 1 and center (0,0).
#
  import numpy as np

  theta = 2.0 * np.pi * rng.random ( )
  r = np.sqrt ( rng.random ( ) )
  p = np.array ( [ r * np.cos ( theta ), r * np.sin ( theta ) ] )

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
  disk_distance_test ( )
  timestamp ( )

