#! /usr/bin/env python3
#
def disk_triangle_picking_test ( ):

#*****************************************************************************80
#
## disk_triangle_picking_test() tests disk_triangle_picking().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 February 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk_triangle_picking_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  disk_triangle_picking() estimates the average area of' )
  print ( '  a random triangle in the unit disk.' )

  n = 1000
  area_average = disk_triangle_picking ( n )
  print ( '  Using', n, 'trials, the average triangle area is ', area_average )
  exact = 35 / 48 / np.pi
  print ( '  Exact value is ', exact )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk_triangle_picking_test():' )
  print ( '  Normal end of execution.' )
  return

def disk_triangle_picking ( n ):

#*****************************************************************************80
#
## disk_triangle_picking(): estimate area of random triangle in unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 February 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of trials.
#
  import numpy as np

  area_average = 0.0

  for test in range ( 0, n ):
    theta = np.random.uniform ( 0.0, 2.0 * np.pi, size = 3 )
    r = np.sqrt ( np.random.uniform ( 0.0, 1.0, size = 3 ) )
    x0 = r[0] * np.cos ( theta[0] )
    y0 = r[0] * np.sin ( theta[0] )
    x1 = r[1] * np.cos ( theta[1] )
    y1 = r[1] * np.sin ( theta[1] )
    x2 = r[2] * np.cos ( theta[2] )
    y2 = r[2] * np.sin ( theta[2] )
    s0 = np.linalg.norm ( [ x0 - x1, y0 - y1 ] )
    s1 = np.linalg.norm ( [ x1 - x2, y1 - y2 ] )
    s2 = np.linalg.norm ( [ x2 - x0, y2 - y0 ] )
    s = 0.5 * ( s0 + s1 + s2 )
    area = np.sqrt ( s * ( s - s0 ) * ( s - s1 ) * ( s - s2 ) )
    area_average = area_average + area

  area_average = area_average / n

  return area_average

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

if ( __name__ == "__main__" ):
  timestamp ( )
  disk_triangle_picking_test ( )
  timestamp ( )

