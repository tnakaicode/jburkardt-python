#! /usr/bin/env python3
#
def square_circles_packing_test ( ):

#*****************************************************************************80
#
## square_circles_packing_test() tests square_circles_packing().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 August 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' );
  print ( 'square_circles_packing_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test square_circles_packing().' )

  C = np.array ( [ 0.0, 0.0 ] )
  R = 0.5
  r = 0.010

  c_try, c_park, density_obs = square_circles_packing ( C, R, r )

  print ( '' )
  print ( '  Number of "cars" parked  = ', c_park )
  print ( '  Number of parking trials = ', c_try )
  print ( '  density_obs            = ', density_obs )
  print ( '  jamming density =        ', 0.547 )
#
#  Terminate.
#
  print ( '' )
  print ( 'square_circles_packing_test()' )
  print ( '  Normal end of execution.' )

  return

def square_circles_packing ( C, R, r ):

#*****************************************************************************80
#
## square_circles_packing() randomly fills a square with smaller circles.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real C, R: the center and radius of the enclosing square.
#
#    real r: the radius of the inserted circles.
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
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )
#
#  I'd prefer to store the circle centers in a 2D array, but 
#  trying to remember and properly use numpy's rules is maddening.
#
  x_list = np.empty ( 0 )
  y_list = np.empty ( 0 )
  c_try = 0
  c_park = 0
#
#  If we don't park a circle within this many tries, give up.
#
  guard = 500

  while ( guard ):

    c_try = c_try + 1
#
#  Pick a random possible circle within the big square.
#
    Rm = R - r
    cx = - Rm + 2.0 * Rm * rng.random ( )
    cy = - Rm + 2.0 * Rm * rng.random ( )
#
#  Compute the minimum distance to the existing circles.
#
    if ( x_list.size == 0 ):
      c_min = 2.0 * r
    else:
      c_min = np.min ( np.hypot ( x_list - cx, y_list - cy ) )
#
#  If the chosen spot is large enough, park!
#
    if ( 2.0 * r <= c_min ):
      guard = 5000
      c_park = c_park + 1
      x_list = np.append ( x_list, cx )
      y_list = np.append ( y_list, cy )
    else:
      guard = guard - 1
#
#  Compute maximum and observed parked-car densities.
#
  density_obs = ( c_park * np.pi * r**2 ) / ( np.pi * R**2 )

  return c_try, c_park, density_obs

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
  square_circles_packing_test ( )
  timestamp ( )

