#! /usr/bin/env python3
#
def box_distance_test ( ):

#*****************************************************************************80
#
## box_distance_test() tests box_distance().
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
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'box_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test box_distance().' )

  a = 1.0
  b = 1.0
  c = 1.0
  mu_exact = box_distance_mean ( a, b, c )
  print ( '' )
  print ( '  For a = b = c, box_distance_mean() should be 0.661707182...' )
  print ( '  Computed value was', mu_exact )

  n = 10000
  a = 1.0
  b = 1.0
  c = 1.0
  mu, var, moment2 = box_distance_stats ( n, a, b, c, rng )
  mu_exact = box_distance_mean ( a, b, c )
  print ( '' )
  print ( '  Using N = ', n, ' sample points,' )
  print ( '  Short side a =           ', a )
  print ( '  Medium side b =           ', b )
  print ( '  Long side c =             ', c )
  print ( '  Estimated mean distance = ', mu )
  print ( '  Exact mean distance     = ', mu_exact )
  print ( '  Estimated variance      = ', var )
  print ( '  Estimated second moment = ', moment2 );
  print ( '  Exact second moment     = ', ( a**2 + b**2 + c**2 ) / 6.0 )
#
  n = 10000
  a = 1.0
  b = 3.0
  c = 5.0
  mu, var, moment2 = box_distance_stats ( n, a, b, c, rng )
  mu_exact = box_distance_mean ( a, b, c )
  print ( '' )
  print ( '  Using N = ', n, ' sample points,' )
  print ( '  Short side a =           ', a )
  print ( '  Medium side b =           ', b )
  print ( '  Long side c =             ', c )
  print ( '  Estimated mean distance = ', mu )
  print ( '  Exact mean distance     = ', mu_exact )
  print ( '  Estimated variance      = ', var )
  print ( '  Estimated second moment = ', moment2 );
  print ( '  Exact second moment     = ', ( a**2 + b**2 + c**2 ) / 6.0 )
#
  n = 10000
  a = 1.0
  b = 3.0
  c = 5.0
  plt.clf ( )
  box_distance_histogram ( n, a, b, c, rng )
  filename = 'box_distance_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'box_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def box_distance_histogram ( n, a, b, c, rng ):

#*****************************************************************************80
#
## box_distance_histogram() histograms box distance statistics.
#
#  Discussion:
#
#    The box has sides of length a <= b <= c.
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
#    integer n: the number of pairs of sample points to use.
#
#    real a, b, c: the length of the sides.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  p = box_sample ( n, a, b, c, rng )
  q = box_sample ( n, a, b, c, rng )
  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p[i,:] - q[i,:] )

  dmin = 0.0
  dmax = np.sqrt ( a**2 + b**2 + c**2 )
  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  s = 'Distance two random points, box' + str ( a ) + ' x ' + str ( b ) + ' x ' + str ( c )
  plt.title ( s )

  return

def box_distance_mean ( a, b, c ):

#*****************************************************************************80
#
## box_distance_mean() returns the exact mean of the box distance.
#
#  Discussion:
#
#    The box has sides of length a <= b <= c.
#
#    For a = b = 1, we should get 
#    mu = ( 4 + 17 sqrt(2) - 6 sqrt(3) + 21 log(1+sqrt(2)) + 84 log(1+sqrt(3))
#      - 42 log(2) - 7 pi ) / 105 = 0.661707182...
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Johan Philip,
#    The probability distribution of the distance between two random
#    points in a box,
#    https://people.kth.se/~johanph/habc.pdf
#
#  Input:
#
#    real a, b, c: the length of the sides.
#
#  Output:
#
#    real mu: the exact mean distance between two random points in the box.
#
  import numpy as np

  r =  np.sqrt ( a**2 + b**2 + c**2 );
  r1 = np.sqrt (       b**2 + c**2 );
  r2 = np.sqrt ( a**2       + c**2 );
  r3 = np.sqrt ( a**2 + b**2       );

  mu = r / 15.0 \
     - 7.0 * ( r - r1 ) * r1**2 / 90.0 / a**2 \
     - 7.0 * ( r - r2 ) * r2**2 / 90.0 / b**2 \
     - 7.0 * ( r - r3 ) * r3**2 / 90.0 / c**2 \
     + 4.0 * ( a**7 + b**7 + c**7 - r1**7 - r2**7 - r3**7 + r**7 ) \
     / 315.0 / a**2 / b**2 / c**2 \
     + ( b**6 * np.arcsinh ( a / b ) + c**6 * np.arcsinh ( a / c ) \
     - r1**2 * ( r1**4 - 8.0 * b**2 * c**2 ) * np.arcsinh ( a / r1 ) ) \
     / 30.0 / a / b**2 / c**2 \
     + ( c**6 * np.arcsinh ( b / c ) + a**6 * np.arcsinh ( b / a ) \
     - r2**2 * ( r2**4 - 8.0 * c**2 * a**2 ) * np.arcsinh ( b / r2 ) ) \
     / 30.0 / a**2 / b / c**2 \
     + ( a**6 * np.arcsinh ( c / a ) + b**6 * np.arcsinh ( c / b ) \
     - r3**2 * ( r3**4 - 8.0 * a**2 * b**2 ) * np.arcsinh ( c / r3 ) ) \
     / 30.0 / a**2 / b**2 / c \
     - 2.0 * ( a**4 * np.arcsin ( b * c / r2 / r3 ) \
             + b**4 * np.arcsin ( c * a / r3 / r1 ) \
             + c**4 * np.arcsin ( a * b / r1 / r2 ) ) / 15.0 / a / b / c;

  return mu

def box_distance_stats ( n, a, b, c, rng ):

#*****************************************************************************80
#
## box_distance_stats() estimates box distance statistics.
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
#    integer n: the number of pairs of sample points to use.
#
#    real a, b, c: the length of the sides.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real mu, var: the estimated mean and variance of the
#    distance between two random points.
#
#    real moment2: the estimated second moment.
#
  import numpy as np

  p = box_sample ( n, a, b, c, rng )
  q = box_sample ( n, a, b, c, rng )
  t = np.zeros ( n )
  for i in range ( 0, n ):
    t[i] = np.linalg.norm ( p[i,:] - q[i,:] )

  mu = np.mean ( t )
  var = np.var ( t )
  moment2 = np.sum ( t**2 ) / n

  return mu, var, moment2

def box_sample ( n, a, b, c, rng ):

#*****************************************************************************80
#
## box_sample() samples points from a box.
#
#  Discussion:
#
#    The box has sides of length a <= b <= c.
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
#    integer n: the number of sample points.
#
#    real a, b, c: the lengths of the sides.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real P(n,3): randomly selected points.
#
  import numpy as np

  S = np.array ( [ \
    [     a, 0.0, 0.0 ], \
    [   0.0,   b, 0.0 ], \
    [   0.0, 0.0,   c ] ] )

  R = rng.random ( size = [ n, 3 ] )

  P = np.matmul ( R, S )

  return P

def box_unit_distance_mean ( ):

#*****************************************************************************80
#
## box_unit_distance_mean() returns the exact mean of the unit box distance.
#
#  Discussion:
#
#    The box has sides of length a <= b <= c.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Johan Philip,
#    The probability distribution of the distance between two random
#    points in a box,
#    https://people.kth.se/~johanph/habc.pdf
#
#  Output:
#
#    real mu: the exact mean distance between two random points in the unit box.
#
  import numpy as np

  mu = ( 4.0 \
    + 17.0 * np.sqrt ( 2.0 ) \
    - 6.0 * np.sqrt ( 3.0 ) \
    + 21.0 * np.log ( 1.0 + np.sqrt ( 2.0 ) ) \
    + 84.0 * np.log ( 1.0 + np.sqrt ( 3.0 ) ) \
    - 42.0 * np.log ( 2.0 ) \
    - 7.0 * np.pi ) / 105.0

  return mu

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
  box_distance_test ( )
  timestamp ( )

