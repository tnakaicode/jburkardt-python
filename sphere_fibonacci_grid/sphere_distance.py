#! /usr/bin/env python3
#
def sphere_distance_compare ( n ):

#*****************************************************************************80
#
## sphere_distance_compare compares sphere distance PDF's.
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
#    Input, integer N, the number of samples to use.
#
  from scipy.special import beta
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = sphere_unit_sample ( )
    q = sphere_unit_sample ( )
    t[i] = np.linalg.norm ( p - q )
  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )

  d = np.linspace ( 0.0, 2.0, 101 )
  pdf = d / beta ( 1.0, 0.5 )
  plt.plot ( d, pdf, 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Relative frequency -->' )
  plt.title ( 'Compare observed and theoretical PDFs' )
  filename = 'sphere_distance_compare.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def sphere_distance_histogram ( n ):

#*****************************************************************************80
#
## sphere_distance_histogram histograms sphere distance statistics.
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
#    Input, integer N, the number of samples to use.
#
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = sphere_unit_sample ( )
    q = sphere_unit_sample ( )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points on a unit sphere' )
  filename = 'sphere_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def sphere_distance_pdf ( ):

#*****************************************************************************80
#
## sphere_distance_pdf plots the PDF for the sphere distance problem.
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
  from scipy.special import beta
  import matplotlib.pyplot as plt
  import numpy as np

  d = np.linspace ( 0.0, 2.0, 101 )

  pdf = d / beta ( 1.0, 0.5 )

  plt.plot ( d, pdf, 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Probability -->' )
  plt.title ( 'PDF for distance between pairs of random points on unit sphere' )
  filename = 'sphere_distance_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def sphere_distance_stats ( n ):

#*****************************************************************************80
#
## sphere_distance_stats estimates sphere distance statistics.
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
#    Input, integer N, the number of sample points to use.
#
#    Output, real MU, VAR, the estimated mean and variance of the
#    distance between two random points on the unit sphere.
#
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = sphere_unit_sample ( )
    q = sphere_unit_sample ( )
    t[i] = np.linalg.norm ( p - q )

  mu = np.sum ( t ) / n
  if ( 1 < n ):
    var = np.sum ( ( t - mu )**2 ) / ( n - 1 )
  else:
    var = 0.0

  mu_exact = 4.0 / 3.0
  var_exact = 2.0 / 9.0
  print ( '' )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Exact mean distance     = %g' % ( mu_exact ) )
  print ( '  Estimated variance      = %g'% ( var ) )
  print ( '  Exact variance          = %g' % ( var_exact ) )

  return mu, var

def sphere_distance_test ( ):

#*****************************************************************************80
#
## sphere_distance_test tests sphere_distance.
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
  print ( 'sphere_distance_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test sphere_distance.' )

  n = 10000
  mu, var = sphere_distance_stats ( n )

  n = 10000
  sphere_distance_histogram ( n )

  sphere_distance_pdf ( )

  n = 10000
  sphere_distance_compare ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'sphere_distance_test:' )
  print ( '  Normal end of execution.' )

  return

def sphere_unit_sample ( ):

#*****************************************************************************80
#
## sphere_unit_sample returns sample points on the unit sphere.
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
#    Output, real X(3), the point.
#
  import numpy as np

  x = np.random.randn ( 3 )
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
  sphere_distance_test ( )
  timestamp ( )

