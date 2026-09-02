#! /usr/bin/env python3
#
def tsp_dantzig42_test ( ):

#*****************************************************************************80
#
## tsp_dantzig42_test() tests tsp_dantzig42().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'tsp_dantzig42_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )

  print ( '  Test tsp_dantzig42(), which returns the Dantzig 42 city' )
  print ( '  traveling salesperson problem challenge data.' )

  n = 42

  dantzig42_order = tsp_dantzig42_order ( )
  dantzig42_order = dantzig42_order - 1

  dantzig42_xy = tsp_dantzig42_xy ( )

  print ( '' )
  print ( '  City coordinates:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %8.4g  %8.4g' % ( i, dantzig42_xy[i,0], dantzig42_xy[i,1] ) )
#
#  Report the cost.
#
  cost = tsp_tour_cost ( n, dantzig42_xy, dantzig42_order )
  print ( '' )
  print ( '  Cost of round trip=', cost )
#
#  Copy the city locations in TSP order.
#
  x2 = np.zeros ( [ n, 2 ] )
 
  for i in range ( 0, n ):
    i2 = dantzig42_order[i]
    x2[i,:] = dantzig42_xy[i2,:]
#
#  Display the locations.
#
  tsp_display ( "dantzig42", n, x2 )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_dantzig42_test():' )
  print ( '  Normal end of execution.' )

  return

def tsp_dantzig42_order ( ):

#*****************************************************************************80
#
## tsp_dantzig42_order() returns the ordering for the Dantzig 42 city TSP challenge.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer dantzig42_order[42]: the 1-based optimal tour order.
#
  import numpy as np

  dantzig42_order = np.array ( [ \
    42, 41, 40, 39, 38, 37, 36, 35, 34, 33, \
    32, 31, 30, 29, 28, 27, 26, 25, 24, 23, \
    22, 21, 20, 19, 18, 17, 16, 15, 14, 13, \
    12, 11, 10,  9,  8,  7,  6,  5,  4,  3, \
     2,  1 ], dtype = int )

  return dantzig42_order

def tsp_dantzig42_xy ( ):

#*****************************************************************************80
#
## tsp_dantzig42_xy() returns the location data for the Dantzig 42 city TSP challenge.
#
#  Discussion:
#
#    The original values 
#
#     [ 147.5,  36.0 ],
#     [ 154.5,  45.0 ],
#
#    were adjusted to 
#
#     [ 147.0,  36.0 ],
#     [ 154.0,  45.0 ],
#
#    so that all coordinates are integers.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 July 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real tsp_dantzig42_xy(42,2): the x and y coordinates of the cities.
#
  import numpy as np

  dantzig42_xy = np.array ( [ \
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

  return dantzig42_xy

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

def tsp_tour_cost ( n, x, order ):

#*****************************************************************************80
#
## tsp_tour_cost() evaluates the cost of a TSP tour.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of cities.
#
#    real x(n,:): the city coordinates.
#
#    integer order(n): the order in which the cities are visited.
#
#  Output:
#
#    real cost: the cost of the route.
#
  import numpy as np

  cost = 0.0
  i1 = n - 1
  for i2 in range ( 0, n ):
    cost = cost + np.linalg.norm ( x[order[i1],:] - x[order[i2],:] )
    i1 = i2

  return cost

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
  tsp_dantzig42_test ( )
  timestamp ( )

