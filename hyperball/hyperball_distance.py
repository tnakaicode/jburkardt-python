#! /usr/bin/env python3
#
def hyperball_distance_compare ( m, n ):

#*****************************************************************************80
#
## hyperball_distance_compare compares hyperball distance PDF's.
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
  from scipy.special import betainc
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = hyperball_unit_sample ( m )
    q = hyperball_unit_sample ( m )
    t[i] = np.linalg.norm ( p - q )
  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )

  d = np.linspace ( 0.0, 2.0, 101 )
  dh = d / 2.0
  x = 1.0 - dh**2
  a = ( m + 1 ) / 2.0
  b = 0.5
  pdf = 0.5 * 2**m * m * dh**(m-1) * betainc ( a, b, x )
  plt.plot ( d, pdf, 'r-', linewidth = 2 )

  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Relative frequency -->' )
  plt.title ( 'Compare observed and theoretical PDFs' )
  filename = 'hyperball_distance_compare.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def hyperball_distance_histogram ( m, n ):

#*****************************************************************************80
#
## hyperball_distance_histogram histograms hyperball distance statistics.
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
    p = hyperball_unit_sample ( m )
    q = hyperball_unit_sample ( m )
    t[i] = np.linalg.norm ( p - q )

  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  plt.title ( 'Distance between a pair of random points in a unit hyperball' )
  filename = 'hyperball_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def hyperball_distance_pdf ( m ):

#*****************************************************************************80
#
## hyperball_distance_pdf plots the PDF for the hyperball distance problem.
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
  from scipy.special import betainc
  import matplotlib.pyplot as plt
  import numpy as np

  d = np.linspace ( 0.0, 2.0, 101 )
  dh = d / 2.0
  x = 1.0 - dh**2
  a = ( m + 1 ) / 2.0
  b = 0.5
  pdf = 0.5 * 2**m * m * dh**(m-1) * betainc ( a, b, x )

  plt.plot ( d, pdf, 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Probability -->' )
  plt.title ( 'PDF for pairwise distance of random unit hyperball points' )
  filename = 'hyperball_distance_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )

  return

def hyperball_distance_stats ( m, n ):

#*****************************************************************************80
#
## hyperball_distance_stats estimates hyperball distance statistics.
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
#    distance between two random points in the unit hyperball.
#
  import numpy as np

  t = np.zeros ( n )
  for i in range ( 0, n ):
    p = hyperball_unit_sample ( m )
    q = hyperball_unit_sample ( m )
    t[i] = np.linalg.norm ( p - q )

  mu = np.sum ( t ) / n
  if ( 1 < n ):
    var = np.sum ( ( t - mu )**2 ) / ( n - 1 )
  else:
    var = 0.0

  print ( '' )
  print ( '  Using M = %d spatial dimension.' % ( m ) )
  print ( '  Using N = %d sample points,' % ( n ) )
  print ( '  Estimated mean distance = %g' % ( mu ) )
  print ( '  Estimated variance      = %g' % ( var ) )

  return mu, var

def hyperball_distance_test ( ):

#*****************************************************************************80
#
## hyperball_distance_test tests hyperball_distance.
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
  print ( 'hyperball_distance_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test hyperball_distance.' )

  m = 20
  n = 10000
  mu, var = hyperball_distance_stats ( m, n )

  m = 20
  n = 10000
  hyperball_distance_histogram ( m, n )

  hyperball_distance_pdf ( m )

  m = 20
  n = 10000
  hyperball_distance_compare ( m, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'hyperball_distance_test:' )
  print ( '  Normal end of execution.' )

  return

def hyperball_unit_sample ( m ):

#*****************************************************************************80
#
## hyperball_unit_sample returns sample points in the unit hyperball.
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
#    Output, real X(M), the point.
#
  import numpy as np

  x = np.random.randn ( m )
#
#  Normalize the vector.
#
  x = x / np.linalg.norm ( x )
#
#  Now compute a value to map the point ON the hypersphere INTO the hypersphere.
#
  r = np.random.rand ( )
 
  x = r ** ( 1.0 / m ) * x

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
  hyperball_distance_test ( )
  timestamp ( )


