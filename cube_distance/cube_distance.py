#! /usr/bin/env python3
#
def cube_distance_compare ( n, rng ):

#*****************************************************************************80
#
## cube_distance_compare() compares cube distance PDF's.
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
    p = cube_unit_sample ( rng )
    q = cube_unit_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )

  n = 101
  d = np.linspace ( 0.0, np.sqrt ( 3.0 ), n )
#
#  np.where will FAIL without extra parentheses here!
#
  pdf = np.zeros ( n )

  i1 = np.where ( ( 0.0             <= d ) & ( d <= 1.0 ) )
  i2 = np.where ( ( 1.0             <  d ) & ( d <= np.sqrt ( 2.0 ) ) )
  i3 = np.where ( ( np.sqrt ( 2.0 ) <  d ) & ( d <= np.sqrt ( 3.0 ) ) )

  pdf[i1] = - d[i1]**2 * ( ( d[i1] - 8.0 ) * d[i1]**2 + np.pi * ( 6.0 * d[i1] - 4.0 ) )

  pdf[i2] = \
      2.0 * d[i2] * \
      ( \
        ( d[i2]**2 - 8.0 * np.sqrt ( d[i2]**2 - 1.0 ) + 3.0 ) * d[i2]**2 \
        - 4.0 * np.sqrt ( d[i2]**2 - 1.0 ) \
        + 12.0 * d[i2]**2 * np.arccos ( 1.0 / d[i2] ) \
        + np.pi * ( 3.0 - 4.0 * d[i2] ) - 0.5 \
      )

  pdf[i3] = \
      d[i3] * \
      ( \
        ( 1.0 + d[i3]**2 ) \
        * ( 6.0 * np.pi + 8.0 * np.sqrt ( d[i3]**2 - 2.0 ) - 5.0 - d[i3]**2 ) \
        - 16.0 * d[i3] * np.arcsin ( 1.0 / ( np.sqrt ( 2 - 2 / d[i3]**2 ) ) ) \
        + 16.0 * d[i3] * np.arctan ( d[i3] * np.sqrt ( d[i3]**2 - 2.0 ) ) \
        - 24.0 * ( d[i3]**2 + 1.0 ) * np.arctan ( np.sqrt ( d[i3]**2 - 2.0 ) ) \
      )

  plt.plot ( d, pdf, 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Relative frequency -->' )
  plt.title ( 'Compare observed and theoretical PDF' )
  filename = 'cube_distance_compare.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def cube_distance_histogram ( n, rng ):

#*****************************************************************************80
#
## cube_distance_histogram() histograms cube distance statistics.
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
    p = cube_unit_sample ( rng )
    q = cube_unit_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points in a unit cube' )
  filename = 'cube_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def cube_distance_pdf ( ):

#*****************************************************************************80
#
## cube_distance_pdf() plots the PDF for the cube distance problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein,
#    Cube Line Picking,
#    From MathWorld--A Wolfram Web Resource.,
#    https://mathworld.wolfram.com/CubeLinePicking.html
#
  import matplotlib.pyplot as plt
  import numpy as np

  n = 101
  d = np.linspace ( 0.0, np.sqrt ( 3.0 ), n )
#
#  np.where will FAIL without extra parentheses here!
#
  pdf = np.zeros ( n )

  i1 = np.where ( ( 0.0             <= d ) & ( d <= 1.0 ) )
  i2 = np.where ( ( 1.0             <  d ) & ( d <= np.sqrt ( 2.0 ) ) )
  i3 = np.where ( ( np.sqrt ( 2.0 ) <  d ) & ( d <= np.sqrt ( 3.0 ) ) )

  pdf[i1] = - d[i1]**2 * ( ( d[i1] - 8.0 ) * d[i1]**2 + np.pi * ( 6.0 * d[i1] - 4.0 ) )

  pdf[i2] = \
      2.0 * d[i2] * \
      ( \
        ( d[i2]**2 - 8.0 * np.sqrt ( d[i2]**2 - 1.0 ) + 3.0 ) * d[i2]**2 \
        - 4.0 * np.sqrt ( d[i2]**2 - 1.0 ) \
        + 12.0 * d[i2]**2 * np.arccos ( 1.0 / d[i2] ) \
        + np.pi * ( 3.0 - 4.0 * d[i2] ) - 0.5 \
      )

  pdf[i3] = \
      d[i3] * \
      ( \
        ( 1.0 + d[i3]**2 ) \
        * ( 6.0 * np.pi + 8.0 * np.sqrt ( d[i3]**2 - 2.0 ) - 5.0 - d[i3]**2 ) \
        - 16.0 * d[i3] * np.arcsin ( 1.0 / ( np.sqrt ( 2 - 2 / d[i3]**2 ) ) ) \
        + 16.0 * d[i3] * np.arctan ( d[i3] * np.sqrt ( d[i3]**2 - 2.0 ) ) \
        - 24.0 * ( d[i3]**2 + 1.0 ) * np.arctan ( np.sqrt ( d[i3]**2 - 2.0 ) ) \
      )

  plt.plot ( d, pdf, 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Probability -->' )
  plt.title ( 'PDF for distance between pairs of random points in unit cube' )
  filename = 'cube_distance_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def cube_distance_stats ( n, rng ):

#*****************************************************************************80
#
## cube_distance_stats() estimates cube distance statistics.
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
#    integer N, the number of sample points to use.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real MU, VAR, the estimated mean and variance of the
#    distance between two random points in the unit cube.
#
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = cube_unit_sample ( rng )
    q = cube_unit_sample ( rng )
    t[i] = np.linalg.norm ( p - q )

  mu = np.mean ( t )
  var = np.var ( t )

  mu_exact = ( 4.0 + 17.0 * np.sqrt ( 2.0 ) - 6.0 * np.sqrt ( 3.0 ) \
    + 21.0 * np.log ( 1.0 + np.sqrt ( 2.0 ) ) \
    + 42.0 * np.log ( 2.0 + np.sqrt ( 3.0 ) ) - 7.0 * np.pi ) \
    / 105.0 
  print ( '' )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Exact mean distace =      %g' % ( mu_exact ) )
  print ( '  Estimated variance      = %g' % ( var ) )

  return mu, var

def cube_distance_test ( ):

#*****************************************************************************80
#
## cube_distance_test() tests cube_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2019
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'cube_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test cube_distance().' )

  rng = default_rng ( )

  n = 10000
  mu, var = cube_distance_stats ( n, rng )

  n = 10000
  cube_distance_histogram ( n, rng )

  cube_distance_pdf ( )

  n = 10000
  cube_distance_compare ( n, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'cube_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def cube_unit_sample ( rng ):

#*****************************************************************************80
#
## cube_unit_sample() returns a randomly selected point in the unit cube.
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
#    real P(3), a point selected uniformly at random from
#    the interior of the unit cube.
#
  import numpy as np

  p = rng.random ( size = 3 )

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
  cube_distance_test ( )
  timestamp ( )

