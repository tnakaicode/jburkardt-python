#! /usr/bin/env python3
#
def line_distance_compare ( n ):

#*****************************************************************************80
#
## line_distance_compare() compares the observed and theoretical PDF's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2019
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
    p = line_unit_sample ( )
    q = line_unit_sample ( )
    t[i] = np.abs ( p - q )

  bins = 20
  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )

  d = np.linspace ( 0.0, 1.0, 101 )
  pdf = 2.0 * ( 1.0 - d )
  plt.plot ( d, pdf, 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Relative frequency -->' )
  plt.title ( 'Compare observed and theoretical PDF' )
  filename = 'line_distance_compare.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def line_distance_histogram ( n ):

#*****************************************************************************80
#
## line_distance_histogram() histograms the data.
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
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = line_unit_sample ( )
    q = line_unit_sample ( )
    t[i] = np.abs ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Relative frequency -->' )
  plt.title ( 'Distance between random point pairs in a unit line segment' )
  filename = 'line_distance_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def line_distance_pdf ( ):

#*****************************************************************************80
#
## line_distance_pdf() plots the PDF for the line distance problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Weisstein,
#    "Line Line Picking." 
#    From MathWorld--A Wolfram Web Resource.,
#    http://mathworld.wolfram.com/LineLinePicking.html
#
  import matplotlib.pyplot as plt
  import numpy as np

  d = np.linspace ( 0.0, 1.0, 101 )

  pdf = 2.0 * ( 1.0 - d )

  plt.plot ( d, pdf, 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Probability -->' )
  plt.title ( 'PDF for distance of random points pairs in unit line segment' )
  filename = 'line_distance_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def line_distance_stats ( n ):

#*****************************************************************************80
#
## line_distance_stats() estimates line distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2019
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
#    distance between two random points in the unit line segment.
#
  import numpy as np

  t = np.zeros ( n )

  for i in range ( 0, n ):
    p = line_unit_sample ( )
    q = line_unit_sample ( )
    t[i] = np.abs ( p - q )

  mu = np.mean ( t )
  var = np.var ( t )

  mu_exact = 1.0 / 3.0
  var_exact = 1.0 / 18.0
  print ( '' )
  print ( '  Using N = %d sample points.' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Exact mean distance     = %g' % ( mu_exact ) )
  print ( '  Estimated variance      = %g' % ( var ) )
  print ( '  Exact variance          = %g' % ( var_exact ) )

  return mu, var

def line_distance_test ( ):

#*****************************************************************************80
#
## line_distance_test() tests line_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'line_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test line_distance().' )

  n = 10000
  mu, var = line_distance_stats ( n )

  n = 10000
  line_distance_histogram ( n )

  line_distance_pdf ( )

  n = 10000
  line_distance_compare ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'line_distance_test:' )
  print ( '  Normal end of execution.' )

  return

def line_unit_sample ( ):

#*****************************************************************************80
#
## line_unit_sample() returns a randomly selected point in the unit line segment.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real P(1,1), a point selected uniformly at random from
#    the interior of the unit line segment.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  p = rng.random ( )

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

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  line_distance_test ( )
  timestamp ( )

