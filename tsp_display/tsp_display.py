#! /usr/bin/env python3
#
def tsp_display_test ( ):

#*****************************************************************************80
#
## tsp_display_test() tests tsp_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'tsp_display_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Display the cities and route solving a traveling' )
  print ( '  salesman problem (TSP).' )

  prefix = 'dantzig42'
  print ( '  Dataset is "' + prefix + '"' )

  n = 42 

  order = np.array ( [ \
    42, 41, 40, 39, 38, 37, 36, 35, 34, 33, \
    32, 31, 30, 29, 28, 27, 26, 25, 24, 23, \
    22, 21, 20, 19, 18, 17, 16, 15, 14, 13, \
    12, 11, 10,  9,  8,  7,  6,  5,  4,  3, \
     2,  1 ], dtype = int )

  order = order - 1

  x = np.array ( [ \
      [ 170.0,  85.0 ], \
      [ 166.0,  88.0 ], \
      [ 133.0,  73.0 ], \
      [ 140.0,  70.0 ], \
      [ 142.0,  55.0 ], \
      [ 126.0,  53.0 ], \
      [ 125.0,  60.0 ], \
      [ 119.0,  68.0 ], \
      [ 117.0,  74.0 ], \
      [  99.0,  83.0 ], \
      [  73.0,  79.0 ], \
      [  72.0,  91.0 ], \
      [  37.0,  94.0 ], \
      [   6.0, 106.0 ], \
      [   3.0,  97.0 ], \
      [  21.0,  82.0 ], \
      [  33.0,  67.0 ], \
      [   4.0,  66.0 ], \
      [   3.0,  42.0 ], \
      [  27.0,  33.0 ], \
      [  52.0,  41.0 ], \
      [  57.0,  59.0 ], \
      [  58.0,  66.0 ], \
      [  88.0,  65.0 ], \
      [  99.0,  67.0 ], \
      [  95.0,  55.0 ], \
      [  89.0,  55.0 ], \
      [  83.0,  38.0 ], \
      [  85.0,  25.0 ], \
      [ 104.0,  35.0 ], \
      [ 112.0,  37.0 ], \
      [ 112.0,  24.0 ], \
      [ 113.0,  13.0 ], \
      [ 125.0,  30.0 ], \
      [ 135.0,  32.0 ], \
      [ 147.0,  18.0 ], \
      [ 147.0,  36.0 ], \
      [ 154.0,  45.0 ], \
      [ 157.0,  54.0 ], \
      [ 158.0,  61.0 ], \
      [ 172.0,  82.0 ], \
      [ 174.0,  87.0 ], ] )
#
#  Create the circuit data with transposition, reordering and wrap-around.
#
  x2 = np.zeros ( [ n, 2 ] )

  for i in range ( 0, n ):
    i2 = order[i]
    x2[i,:] = x[i2,:]
#
#  Send the data to the plotter.
#
  tsp_display ( prefix, n, x2 )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_display_test():' )
  print ( '  Normal end of execution.' )

  return

def tsp_display ( prefix, n, x ):

#*****************************************************************************80
#
## tsp_display() plots cities and a tour connecting them.
#
#  Discussion:
#
#    The code automatically appends a final stop at the first city.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 July 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string prefix: a string that defines the name of
#    the problem.  It is also used to create file names needed for
#    input to gnuplot.
#
#    integer n: the number of cities.
#
#    real x(n,2): the x and y coordinates of the cities.
#
  import matplotlib.pyplot as plt
  import numpy as np

  plt.clf ( )
  plt.plot ( x[:,0], x[:,1], 'm.', markersize = 20 )
  x = np.append ( x, [ x[0,0], x[0,1] ] )
  x = np.reshape ( x, [n+1,2] )
  plt.plot ( x[:,0], x[:,1], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->' )
  plt.ylabel ( '<-- Y -->' )
  plt.title ( prefix )
  filename = prefix + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

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
  tsp_display_test ( )
  timestamp ( )

