#! /usr/bin/env python3
#
def hypersphere_distance_compare ( m, n ):

#*****************************************************************************80
#
## hypersphere_distance_compare compares hypersphere distance PDFs.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of samples to use.
#
  from scipy.special import beta
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = hypersphere_unit_sample ( m )
    q = hypersphere_unit_sample ( m )
    t[i] = np.linalg.norm ( p - q )
  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )

  d = np.linspace ( 0.0, 2.0, 101 )
  pdf = d / beta ( ( m - 1 ) / 2, 0.5 ) * ( d**2 - 0.25 * d**4 ) ** ( ( m - 3 ) / 2 )
  plt.plot ( d, pdf, 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Relative frequency -->' )
  plt.title ( 'Compare observed and theoretical PDFs' )
  filename = 'hypersphere_distance_compare.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def hypersphere_distance_histogram ( m, n ):

#*****************************************************************************80
#
## hypersphere_distance_histogram histograms hypersphere distance statistics.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of samples to use.
#
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = hypersphere_unit_sample ( m )
    q = hypersphere_unit_sample ( m )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points on a unit hypersphere' )
  filename = 'hypersphere_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def hypersphere_distance_pdf ( m ):

#*****************************************************************************80
#
## hypersphere_distance_pdf plots the PDF for the hypersphere distance problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 May 2019
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
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
  from scipy.special import beta
  import matplotlib.pyplot as plt
  import numpy as np

  d = np.linspace ( 0.0, 2.0, 101 )

  pdf = d / beta ( ( m - 1 ) / 2, 0.5 ) * ( d**2 - 0.25 * d**4 ) ** ( ( m - 3 ) / 2 )

  plt.plot ( d, pdf, 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Probability -->' )
  plt.title ( 'PDF for pairwise distance of random points on unit hypersphere' )
  filename = 'hypersphere_distance_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def hypersphere_distance_stats ( m, n ):

#*****************************************************************************80
#
## hypersphere_distance_stats estimates hypersphere distance statistics.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 May 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of sample points to use.
#
#    Output, real MU, VAR, the estimated mean and variance of the
#    distance between two random points on the unit sphere.
#
  from scipy.special import gamma
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = hypersphere_unit_sample ( m )
    q = hypersphere_unit_sample ( m )
    t[i] = np.linalg.norm ( p - q )

  mu = np.sum ( t ) / n
  if ( 1 < n ):
    var = np.sum ( ( t - mu )**2 ) / ( n - 1 )
  else:
    var = 0.0

  mu_exact = np.sqrt ( 2.0 )
  var_exact = 2.0 - 2.0**( 2 * m - 2 ) * gamma ( m / 2 )**4 / np.pi \
    / gamma ( m - 0.5 )**2
  print ( '' )
  print ( '  Using M = %d spatial dimension' % ( m ) )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Exact mean distance     = %g' % ( mu_exact ) )
  print ( '  Estimated variance      = %g' % ( var ) )
  print ( '  Exact variance          = %g' % ( var_exact ) )

  return mu, var

def hypersphere_distance_test ( ):

#*****************************************************************************80
#
## hypersphere_distance_test tests hypersphere_distance.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 May 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hypersphere_distance_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test hypersphere_distance.' )

  m = 20
  n = 10000
  mu, var = hypersphere_distance_stats ( m, n )

  m = 20
  n = 10000
  hypersphere_distance_histogram ( m, n )

  m = 20
  hypersphere_distance_pdf ( m )

  m = 20
  n = 10000
  hypersphere_distance_compare ( m, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'hypersphere_distance_test:' )
  print ( '  Normal end of execution.' )

  return

def hypersphere_unit_sample ( m ):

#*****************************************************************************80
#
## hypersphere_unit_sample returns sample points on the unit hypersphere.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 May 2019
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
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real X(M,1), the point.
#
  import numpy as np

  x = np.random.randn ( m )
#
#  Normalize the vector.
#
  x = x / np.linalg.norm ( x )

  return x

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
  hypersphere_distance_test ( )
  timestamp ( )

