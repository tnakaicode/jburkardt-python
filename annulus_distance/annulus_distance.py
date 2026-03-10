#! /usr/bin/env python3
#
def annulus_distance_test ( ):

#*****************************************************************************80
#
## annulus_distance_test() tests annulus_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 September 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'annulus_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test annulus_distance()' )

  n = 10000
  pc = np.array ( [ 0.0, 0.0 ] )
  r2 = 1.0
  for r1 in [ 0.0, 0.1, 0.2, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.99 ]:
    mu, var = annulus_distance_stats ( n, pc, r1, r2 )
    print ( '' )
    print ( '  Using N = ', n, ' sample points,' )
    print ( '  R1 = ', r1, ' R2 = ', r2 )
    print ( '  Estimated mean distance = ', mu )
    print ( '  Estimated variance      = ', var )

  print ( '' )

  n = 10000
  pc = np.array ( [ 0.0, 0.0 ] )
  r2 = 1.0
  for r1 in [ 0.0, 0.1, 0.2, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.99 ]:
    annulus_distance_histogram ( n, pc, r1, r2 )
    filename = 'annulus_distance_histogram_' + str(r1) + '_' + str(r2) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'annulus_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def annulus_distance_histogram ( n, pc, r1, r2 ):

#*****************************************************************************80
#
## annulus_distance_histogram() histograms annulus distance statistics.
#
#  Discussion:
#
#    A circular annulus with center PC, inner radius R1 and
#    outer radius R2, is the set of points P so that
#
#      R1^2 <= (P(1)-PC(1))^2 + (P(2)-PC(2))^2 <= R2^2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points to generate.
#
#    real PC(2), the center.
#
#    real R1, R2, the inner and outer radii.
#
  import matplotlib.pyplot as plt
  import numpy as np

  p = annulus_sample ( n, pc, r1, r2 )
  q = annulus_sample ( n, pc, r1, r2 )

  t = np.linalg.norm ( p - q, ord = 2, axis = 1 )

  plt.clf ( )
  plt.hist ( t, bins = 20, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  label = 'Point distances in annulus, r1 = %g, r2 = %g'  % ( r1, r2 )
  plt.title ( label )

  return

def annulus_distance_stats ( n, pc, r1, r2 ):

#*****************************************************************************80
#
## annulus_distance_stats() estimates annulus distance statistics.
#
#  Discussion:
#
#    A circular annulus with center PC, inner radius R1 and
#    outer radius R2, is the set of points P so that
#
#      R1^2 <= (P(1)-PC(1))^2 + (P(2)-PC(2))^2 <= R2^2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points to generate.
#
#    real PC(2), the center.
#
#    real R1, R2, the inner and outer radii.
#
#  Output:
#
#    real MU, VAR, the estimated mean and variance of the
#    distance between two random points on the ellipse.
#
  import numpy as np

  p = annulus_sample ( n, pc, r1, r2 )
  q = annulus_sample ( n, pc, r1, r2 )

  t = np.linalg.norm ( p - q, ord = 2, axis = 1 )

  mu = np.mean ( t )
  var = np.var ( t )

  return mu, var

def annulus_sample ( n, pc, r1, r2 ):

#*****************************************************************************80
#
## annulus_sample() samples a circular annulus.
#
#  Discussion:
#
#    A circular annulus with center PC, inner radius R1 and
#    outer radius R2, is the set of points P so that
#
#      R1^2 <= (P(1)-PC(1))^2 + (P(2)-PC(2))^2 <= R2^2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Peter Shirley,
#    Nonuniform Random Point Sets Via Warping,
#    Graphics Gems, Volume III,
#    edited by David Kirk,
#    AP Professional, 1992, 
#    ISBN: 0122861663,
#    LC: T385.G6973.
#
#  Input:
#
#    integer N, the number of points to generate.
#
#    real PC(2), the center.
#
#    real R1, R2, the inner and outer radii.
#
#  Output:
#
#    real P(N,2), sample points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  theta = 2.0 * np.pi * rng.random ( n )

  v = rng.random ( n )

  r = np.sqrt ( ( 1.0 - v ) * r1 * r1 \
       +                v   * r2 * r2 )

  p = np.zeros ( [ n, 2 ] )
  p[:,0] = pc[0] + r * np.cos ( theta )
  p[:,1] = pc[1] + r * np.sin ( theta )

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
  annulus_distance_test ( )
  timestamp ( )

