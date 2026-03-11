#! /usr/bin/env python3
#
def latin_center ( dim_num, point_num ):

#*****************************************************************************80
#
## latin_center() returns center points in a Latin square.
#
#  Discussion:
#
#    In each spatial dimension, there will be exactly one
#    point with the coordinate value
#
#      ( 1, 3, 5, ..., 2*point_num-1 ) / ( 2 * point_num )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer dim_num: the spatial dimension.
#
#    integer point_num: the number of points.
#
#  Output:
#
#    real x(point_num,dim_num,point_num): the points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  x = np.zeros ( [ point_num, dim_num ] )

  for j in range ( 0, dim_num ):

    perm = rng.permutation ( point_num )

    for i in range ( 0, point_num ):
      x[i,j] = ( 2.0 * perm[i] + 1.0 ) / ( 2.0 * point_num )

  return x

def latin_center_test01 ( ):

#*****************************************************************************80
#
## latin_center_test01() tests latin_center().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  dim_num = 2
  point_num = 10

  print ( '' )
  print ( 'latin_center_test01():' )
  print ( '  latin_center() chooses a Latin cell arrangement,' )
  print ( '  and returns the centers of those cells.' )
  print ( '' )
  print ( '  Spatial dimension = ', dim_num )
  print ( '  Number of points =  ', point_num )

  x = latin_center ( dim_num, point_num )

  x = x[np.lexsort(x.T[::-1])]

  print ( '' )
  print ( '  The Latin center points:' )
  print ( '' )
  print ( x )

  return

def latin_center_test ( ):

#*****************************************************************************80
#
## latin_center_test() tests latin_center().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'latin_center_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test latin_center().' )

  latin_center_test01 ( )

  latin_center_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'latin_center_test():' )
  print ( '  Normal end of execution.' )

  return

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
  latin_center_test ( )
  timestamp ( )


