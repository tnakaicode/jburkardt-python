#! /usr/bin/env python3
#
def closest_point_brute_test ( ):

#*****************************************************************************80
#
## closest_point_brute_test() tests closest_point_brute().
#
#  Discussion:
#
#    We are given R, a set of NR points in M dimensions.
#
#    We are given S, a point in M dimensions.
#
#    We seek the index J of the point R(J)
#    which is nearest to S over all points in R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Local:
#
#    integer M, the spatial dimension.
#
#    integer NR, the number of data points.
#
#    real R(M,NR), the data points.
#
#    real S(M), the sample point. 
#
  from numpy.random import default_rng
  from time import perf_counter
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'closest_point_brute_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test closest_point_brute().' )

  m = 2
  print ( '  Spatial dimension m = ', m )

  print ( '' )
  print ( '  Timing closest_point_brute():' )
  print ( '' )
  nr = 1

  while ( nr <= 65536 ):

    r = rng.random ( [ nr, m ] )
    s = rng.random ( m )
 
    seconds = perf_counter ( )
    near_index, near_dist = closest_point_brute ( m, nr, r, s )
    dt = perf_counter ( ) - seconds

    print ( '%5d  %5d  %8.2g  %8.2g' % ( nr, near_index, near_dist, dt ) )

    nr = nr * 2
#
#  Terminate.
#
  print ( '' )
  print ( 'closest_point_brute_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

  return

def closest_point_brute ( m, nr, r, s ):

#*****************************************************************************80
#
## closest_point_brute() finds the nearest R point to an S point.
#
#  Discussion:
#
#    We are given R, a set of NR points in M dimensions.
#
#    We are given S, a point in M dimensions.
#
#    We seek the index J of the point R(J)
#    which is nearest to S over all points in R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer NR, the number of cell generators.
#
#    real R(nr,m), the cell generators.
#
#    real S(M), the point to be checked.
#
#  Output:
#
#    integer near_index: the index of the nearest cell generator.
#
  import numpy as np

  near_dist = np.inf
  near_index = -1

  for jr in range ( 0, nr ):

    dist = np.linalg.norm ( r[jr,:] - s )

    if ( dist < near_dist ):
      near_dist = dist
      near_index = jr

  return near_index, near_dist

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
  closest_point_brute_test ( )
  timestamp ( )

