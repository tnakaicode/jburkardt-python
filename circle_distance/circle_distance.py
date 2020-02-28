#! /usr/bin/env python3
#
def circle_distance_compare ( n ):

#*****************************************************************************80
#
## circle_distance_compare compares observed and theoretical PDF's.
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
    p = circle_unit_sample ( )
    q = circle_unit_sample ( )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )

  r = 1.0
  d = np.linspace ( 0.0, 2.0, 101 )
  d = d[0:100]
  pdf = ( 1.0 / np.pi ) * 1.0 / np.sqrt ( 1.0 - 0.25 * d**2 / r**2 )
  plt.plot ( d, pdf, 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Relative Frequency -->' )
  plt.title ( 'Compare observed and theoretical PDF' )
  filename = 'circle_distance_compare.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )
 
  return

def circle_distance_histogram ( n ):

#*****************************************************************************80
#
## circle_distance_histogram histograms circle distance statistics.
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
    p = circle_unit_sample ( )
    q = circle_unit_sample ( )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points on a unit circle' )
  filename = 'circle_distance_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )
 
  return

def circle_distance_pdf ( ):

#*****************************************************************************80
#
## circle_distance_pdf plots the PDF for the circle distance problem.
#
#  Discussion:
#
#    The reference gives the formula as:
#
#      pdf = ( 1.0 / pi ) * 1.0 ./ sqrt ( 1.0 - 0.5 * d.^2 / r.^2 ) 
#
#    but the correct formula is:
#
#      pdf = ( 1.0 / pi ) * 1.0 ./ sqrt ( 1.0 - 0.25 * d.^2 / r.^2 ) 
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
#    Panagiotis Siridopoulos,
#    The N-Sphere Chord Length Distribution,
#    ARXIV,
#    https://arxiv.org/pdf/1411.5639.pdf
#
  import matplotlib.pyplot as plt
  import numpy as np

  r = 1.0
  d = np.linspace ( 0.0, 2.0, 101 )
#
#  PDF goes to infinity at d = 2*r so omit last value.
#
  d = d[0:100]

  pdf = ( 1.0 / np.pi ) * 1.0 / np.sqrt ( 1.0 - 0.25 * d**2 / r**2 )

  plt.plot ( d, pdf, 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Probability -->' )
  plt.title ( 'PDF for distance between pairs of random points on circle' )
  filename = 'circle_distance_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def circle_distance_stats ( n ):

#*****************************************************************************80
#
## circle_distance_stats estimates circle distance statistics.
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
#    distance between two random points on the unit circle.
#
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = circle_unit_sample ( )
    q = circle_unit_sample ( )
    t[i] = np.linalg.norm ( p - q )

  mu = np.sum ( t ) / n
  if ( 1 < n ):
    var = np.sum ( ( t - mu ) ** 2 ) / ( n - 1 )
  else:
    var = 0.0

  mu_exact = 4.0 / np.pi
  print ( '' )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Exact mean distance     = %g' % ( mu_exact ) )
  print ( '  Estimated variance      = %g' % ( var ) )

  return mu, var

def circle_distance_test ( ):

#*****************************************************************************80
#
## circle_distance_test tests circle_distance.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'circle_distance_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test circle_distance.' )

  n = 10000
  mu, var = circle_distance_stats ( n )

  n = 10000
  circle_distance_histogram ( n )

  circle_distance_pdf ( )

  n = 10000
  circle_distance_compare ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'circle_distance_test:' )
  print ( '  Normal end of execution.' )

  return

def circle_unit_sample ( ):

#*****************************************************************************80
#
## circle_unit_sample returns a randomly selected point on the unit circle.
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
#    Output, real P(2,1), a point selected uniformly at random from
#    the circle of radius 1 and center (0,0).
#
  import numpy as np

  theta = 2.0 * np.pi * np.random.rand ( 1 )
  p = np.array ( [ np.cos ( theta ), np.sin ( theta ) ] )

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
  circle_distance_test ( )
  timestamp ( )
