#! /usr/bin/env python3
#
def square_distance_compare ( n ):

#*****************************************************************************80
#
## square_distance_compare compares observed and theoretical PDF's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of samples to use.
#
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = square_unit_sample ( )
    q = square_unit_sample ( )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )

  n = 101
  d = np.linspace ( 0.0, np.sqrt ( 2.0 ), n )

  pdf = np.zeros ( n )

  i1 = np.where ( d <= 1.0 )
  pdf[i1] = 2 * d[i1] * ( d[i1]**2 - 4 * d[i1] + np.pi )

  i2 = np.where ( 1.0 < d )
  pdf[i2] = 2 * d[i2] * (4 * np.sqrt ( d[i2]**2 - 1 ) - ( d[i2]**2 + 2 - np.pi ) \
      - 4.0 * np.arctan ( np.sqrt ( d[i2]**2 - 1 ) ) )

  plt.plot ( d, pdf, 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Compare observed and theoretical PDF' )
  filename = 'square_distance_compare.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def square_distance_histogram ( n ):

#*****************************************************************************80
#
## square_distance_histogram histograms square distance statistics.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of samples to use.
#
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = square_unit_sample ( )
    q = square_unit_sample ( )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points in a unit square' )
  filename = 'square_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def square_distance_pdf ( ):

#*****************************************************************************80
#
## square_distance_pdf plots the PDF for the square distance problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#    Eric Weisstein,
#    "Square Line Picking." 
#    From MathWorld--A Wolfram Web Resource.,
#    http://mathworld.wolfram.com/SquareLinePicking.html
#
  import matplotlib.pyplot as plt
  import numpy as np

  n = 101
  d = np.linspace ( 0.0, np.sqrt ( 2.0 ), n )

  pdf = np.zeros ( n )

  i1 = np.where ( d <= 1.0 )
  pdf[i1] = 2 * d[i1] * ( d[i1]**2 - 4 * d[i1] + np.pi )

  i2 = np.where ( 1.0 < d )
  pdf[i2] = 2 * d[i2] * (4 * np.sqrt ( d[i2]**2 - 1 ) - ( d[i2]**2 + 2 - np.pi ) \
      - 4.0 * np.arctan ( np.sqrt ( d[i2]**2 - 1 ) ) )

  plt.plot ( d, pdf, 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Probability -->' )
  plt.title ( 'PDF for distance between pairs of random points in unit square' )
  filename = 'square_distance_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def square_distance_stats ( n ):

#*****************************************************************************80
#
## square_distance_stats estimates square distance statistics.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of sample points to use.
#
#    Output, real MU, VAR, the estimated mean and variance of the
#    distance between two random points in the unit square.
#
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = square_unit_sample ( )
    q = square_unit_sample ( )
    t[i] = np.linalg.norm ( p - q )

  mu = np.sum ( t ) / n
  if ( 1 < n ):
    var = np.sum ( ( t - mu ) ** 2 ) / ( n - 1 )
  else:
    var = 0.0

  mu_exact = ( np.sqrt ( 2.0 ) + 2.0 + 5.0 * np.log ( 1.0 + np.sqrt ( 2.0 ) ) ) / 15.0
  var_exact = ( 69.0 - 4.0 * np.sqrt ( 2.0 ) \
    - 10.0 * ( 2.0 + np.sqrt ( 2.0 ) ) * np.arcsinh ( 1.0 ) \
    - 25.0 * ( np.arcsinh ( 1.0 ) )**2 ) / 225.0
  print ( '' )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Exact mean distance     = %g' % ( mu_exact ) )
  print ( '  Estimated variance      = %g' % ( var ) )
  print ( '  Exact variance          = %g' % ( var_exact ) )

  return mu, var

def square_distance_test ( ):

#*****************************************************************************80
#
## square_distance_test tests square_distance.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 May 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'square_distance_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test square_distance.' )

  n = 10000
  mu, var = square_distance_stats ( n )

  n = 10000
  square_distance_histogram ( n )

  square_distance_pdf ( )

  n = 10000
  square_distance_compare ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'square_distance_test:' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def square_unit_sample ( ):

#*****************************************************************************80
#
## square_unit_sample returns a randomly selected point in the unit square.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real P(2), a point selected uniformly at random from
#    the interior of the unit square.
#
  import numpy as np

  p = np.random.rand ( 2 )

  return p

def timestamp ( ):

#*****************************************************************************80
#
## timestamp prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  square_distance_test ( )
  timestamp ( )


