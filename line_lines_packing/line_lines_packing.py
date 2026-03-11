#! /usr/bin/env python3
#
def line_lines_packing_test ( ):

#*****************************************************************************80
#
## line_lines_packing_test() tests line_lines_packing().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' );
  print ( 'line_lines_packing_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test line_lines_packing().' )

  x_min = 0.0
  x_max = 100.0
  c_width = 1.0

  c_try, c_park, density_obs, density_max = line_lines_packing ( x_min, x_max, \
    c_width )

  print ( '' )
  print ( '  Number of "cars" parked  = ', c_park )
  print ( '  Number of parking trials = ', c_try )
  print ( '  density_max            = ', density_max )
  print ( '  density_obs            = ', density_obs )
  print ( '  Renyi parking constant = ', 0.7475979202 )
#
#  Terminate.
#
  print ( '' )
  print ( 'line_lines_packing_test()' )
  print ( '  Normal end of execution.' )

  return

def line_lines_packing ( x_min, x_max, c_width ):

#*****************************************************************************80
#
## line_lines_packing() randomly fills a parking area with cars.
#
#  Discussion:
#
#    The code which tries to randomly pack as many non-overlapping equal 
#    line segments as possible into a larger line segment,
#    estimating Renyi's parking constant of 0.7475979202.
#
#    When the length of the parking area (larger line segment) is 
#    reasonably greater than the length of an individual car 
#    (the smaller line segments), then on average about 3/4 of the
#    parking area will be used before there are no more open spots.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x_min, x_max: the endpoints of the line segment.
#
#    real c_width: the length of a car.
#
#  Output:
#
#    integer c_try: the number of times a random car tried to park.
#
#    integer c_park: the number of times a random car was able to park.
#
#    real density_obs: the final density of parked cars, between 0 and 1.
#    This will typically be close to Renyi's parking constant.
#
#    real density_max: the theoretical maximum density of cars per
#    parking area, between 0 and 1.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  c_rad = c_width / 2.0
  c_list = np.empty ( 0 )
  c_park = 0
  c_try = 0
  c_latest = 0
#
#  Loop, trying to park one more car at a time, avoiding the previously
#  parked ones.
#
  while ( True ):

    c_try = c_try + 1
#
#  Try to park at a random position.
#
    r = rng.random ( )
    c = x_min + c_rad + r * ( x_max - x_min - 2.0 * c_rad )
#
#  Compute the minimum distance to the parked cars.
#
    if ( c_list.size == 0 ):
      c_min = 2.0 * c_rad
    else:
      c_min = np.min ( np.abs ( c_list - c ) )
#
#  If the chosen spot is large enough, park!
#
    if ( 2.0 * c_rad <= c_min ):
      c_park = c_park + 1
      c_latest = c_try
      c_list = np.append ( c_list, c )
#
#  Otherwise, if we have gone "long enough" without success, give up.
#
    elif ( c_latest + 10000 < c_try ):
      break
#
#  Compute maximum and observed parked-car densities.
#
  density_max = 1.0 / 2.0 / c_rad
  density_obs = c_park / ( x_max - x_min )

  return c_try, c_park, density_obs, density_max

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
  line_lines_packing_test ( )
  timestamp ( )

