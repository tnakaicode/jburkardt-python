#! /usr/bin/env python3
#
def rectangle_distance_test ( ):

#*****************************************************************************80
#
## rectangle_distance_test() tests rectangle_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'rectangle_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test rectangle_distance().' )

  a = 1.0
  b = 3.0

  n = 10000
  mu, var = rectangle_distance_stats ( n, a, b )
  a = min ( a, b )
  b = max ( a, b )
  d = np.sqrt ( a**2 + b**2 )
  mu_exact = ( 1.0 / 15.0 ) * \
    ( \
        a**3 / b**3 + b**3 / a**3 + d * ( 3.0 - a**2 / b**3 - b**2 / a**3 ) \
      + 2.5 * \
      ( \
          b**2 / a * np.log ( ( a + d ) / b ) \
        + a**2 / b * np.log ( ( b + d ) / a ) \
      ) \
    )
  print ( '' )
  print ( '  Using N = ', n, ' sample points,' )
  print ( '  Short rectangle side a =  ', a )
  print ( '  Long rectangle side b =   ', b )
  print ( '  Estimated mean distance = ', mu )
  print ( '  Exact mean distance     = ', mu_exact )
  print ( '  Estimated variance      = ', var )
 
  n = 10000
  plt.clf ( )
  rectangle_distance_histogram ( n, a, b )
  filename = 'rectangle_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  plt.clf ( )
  rectangle_distance_pdf ( a, b )
  filename = 'rectangle_distance_pdf.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  plt.clf ( )
  n = 10000
  rectangle_distance_histogram ( n, a, b )
  rectangle_distance_pdf ( a, b )
  filename = 'rectangle_distance_compare.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'rectangle_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def rectangle_distance_histogram ( n, a, b ):

#*****************************************************************************80
#
## rectangle_distance_histogram() histograms rectangle distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of pairs of sample points to use.
#
#    real a, b: the length of the two sides.
#
  import matplotlib.pyplot as plt
  import numpy as np

  p = rectangle_sample ( n, a, b )
  q = rectangle_sample ( n, a, b )
  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p[i,:] - q[i,:] )

  dmin = 0.0
  dmax = np.sqrt ( a**2 + b**2 )
  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  s = 'Distance two random points, rectangle' + str ( a ) + ' x ' + str ( b )
  plt.title ( s )

  return

def rectangle_distance_pdf ( a, b ):

#*****************************************************************************80
#
## rectangle_distance_pdf() plots the PDF for the rectangle distance problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brahim Gaboune, Gilbert Laporte, Francois Soumis,
#    Expected Distances between Two Uniformly Distributed Random Points
#    in Rectangles and Rectangular Parallelipipeds,
#    The Journal of the Operational Research Society,
#    Volume 44, Number 5, May 1993, pages 513-519.
#    [This reference gives an INCOMPLETE version of PDF!]
#
#    A Mathai, P Moschopoulos, G Pederzoli,
#    Random points associated with rectangles,
#    Rendiconti del Circolo Matematico di Palermo,
#    Volume 47, Number II, pages 163-190, 1999.
#
#  Input:
#
#    real a, b: the length of the sides.
#
  import matplotlib.pyplot as plt
  import numpy as np

  n = 101
  d = np.linspace ( 0.0, np.sqrt ( a**2 + b**2 ), n )
  pdf = np.zeros ( n )
#
#  Guarantee a <= b.
#
  if ( b < a ):
    t = a
    a = b
    b = a

  s = d**2

  i1 = np.where ( ( 0.0  <= d ) & ( d <= a ) )
  i2 = np.where ( ( a    <  d ) & ( d <= b ) )
  i3 = np.where ( ( b    <  d ) & ( d <= np.sqrt ( a**2 + b**2 ) ) )

  pdf[i1] = \
    - 2.0 * d[i1] / a**2 / b \
    - 2.0 * d[i1] / a / b**2 \
    + np.pi / a / b \
    + d[i1]**2 / a**2 / b**2

  pdf[i2] = \
    - 2.0 * d[i2] / a**2 / b \
    - 1.0 / b**2 \
    + 2.0 * np.arcsin ( a / d[i2] ) / a / b \
    + 2.0 * np.sqrt ( d[i2]**2 - a**2 ) / a**2 / b

  pdf[i3] = \
    - 1.0 / b**2 \
    + 2.0 * np.arcsin ( a / d[i3] ) / a / b \
    + 2.0 * np.sqrt ( d[i3]**2 - a**2 ) / a**2 / b \
    - 1.0 / a**2 \
    + 2.0 * np.arcsin ( b / d[i3] ) / a / b \
    + 2.0 * np.sqrt ( d[i3]**2 - b**2 ) / a / b**2 \
    - np.pi / a / b \
    - d[i3]**2 / a**2 / b**2

  pdf = 2.0 * d * pdf

  plt.plot ( d, pdf, 'r-', 'linewidth', 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Probability -->' )
  plt.title ( 'PDF for distance between pairs of random points in rectangle' )

  return

def rectangle_distance_stats ( n, a, b ):

#*****************************************************************************80
#
## rectangle_distance_stats() estimates rectangle distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of pairs of sample points to use.
#
#    real a, b: the length of the two sides.
#
#  Output:
#
#    real mu, var: the estimated mean and variance of the
#    distance between two random points in the rectangle.
#
  import numpy as np

  p = rectangle_sample ( n, a, b )
  q = rectangle_sample ( n, a, b )
  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p[i,:] - q[i,:] )

  mu = np.mean ( t )
  var = np.var ( t )

  return mu, var

def rectangle_sample ( n, a, b ):

#*****************************************************************************80
#
## rectangle_sample() samples points from a rectangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of sample points.
#
#    real a, b: the lengths of the two sides of the rectangle.
#
#  Output:
#
#    real P(n,2): randomly selected points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  S = np.array ( [ \
    [   a, 0.0 ], \
    [   0.0, b ] ] )

  R = rng.random ( size = [ n, 2 ] )

  P = np.matmul ( R, S )

  return P

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
  rectangle_distance_test ( )
  timestamp ( )



