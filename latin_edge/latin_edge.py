#! /usr/bin/env python3
#
def latin_edge ( dim_num, point_num ):

#*****************************************************************************80
#
## latin_edge() returns edge points in a Latin square.
#
#  Discussion:
#
#    In each spatial dimension, there will be exactly one
#    point with the coordinate value
#
#      ( 0, 1, 2, ..., point_num-1 ) / ( point_num - 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer dim_num, the spatial dimension.
#
#    integer point_num, the number of points, which should be at least 2!
#
#  Output:
#
#    real x(dim_num,point_num), the points.
#
  from numpy.random import default_rng
  import numpy as np

  x = np.zeros ( [ dim_num, point_num ] )

  if ( point_num == 1 ):

    x = x + 0.5

  else:

    rng = default_rng ( )

    for i in range ( 0, dim_num ):

      perm = rng.permutation ( point_num )

      x[i,:] = perm / ( point_num - 1 )

  return x

def latin_edge_test01 ( ):

#*****************************************************************************80
#
## latin_edge_test01() tests latin_edge().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 November 2022
#
#  Author:
#
#    John Burkardt
#
  dim_num = 2
  point_num = 11

  print ( '' )
  print ( 'latin_edge_test01():' )
  print ( '  latin_edge() chooses a Latin cell arrangement,' )
  print ( '  which includes the edge points.' )
  print ( '' )
  print ( '  Spatial dimension =', dim_num )
  print ( '  Number of points = ', point_num )
 
  x = latin_edge ( dim_num, point_num )

  print ( '' )
  print ( '  The Latin Edge Square points:' )
  print ( '' )
  print ( x )

  return

def latin_edge_test ( ):

#*****************************************************************************80
#
## latin_edge_test() tests latin_edge().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'latin_edge_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test latin_edge().' )

  latin_edge_test01 ( )
  latin_edge_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'latin_edge_test():' )
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
  latin_edge_test ( )
  timestamp ( )

