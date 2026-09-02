#! /usr/bin/env python3
#
def tsp_att48_test ( ):

#*****************************************************************************80
#
## tsp_att48_test() tests tsp_att48().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'tsp_att48_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )

  print ( '  Test tsp_att48(), which returns the AT&T 48 city' )
  print ( '  traveling salesperson problem challenge data.' )

  n = 48

  att48_order = tsp_att48_order ( )
  att48_order = att48_order - 1

  att48_xy = tsp_att48_xy ( )

  print ( '' )
  print ( '  City coordinates:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %8.4g  %8.4g' % ( i, att48_xy[i,0], att48_xy[i,1] ) )
#
#  Report the cost.
#
  cost = tsp_tour_cost ( n, att48_xy, att48_order )
  print ( '' )
  print ( '  Cost of round trip=', cost )
#
#  Copy the city locations in TSP order.
#
  x2 = np.zeros ( [ n, 2 ] )
 
  for i in range ( 0, n ):
    i2 = att48_order[i]
    x2[i,:] = att48_xy[i2,:]
#
#  Display the locations.
#
  tsp_display ( "att48", n, x2 )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_att48_test():' )
  print ( '  Normal end of execution.' )

  return

def tsp_att48_order ( ):

#*****************************************************************************80
#
## tsp_att48_order() returns the location data for the AT&T 48 city TSP challenge.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer att48_order[48]: the 1-based optimal tour order.
#
  import numpy as np

  att48_order = np.array ( [ \
     1,  8, 38, 31, 44, 18,  7, 28,  6, 37, \
    19, 27, 17, 43, 30, 36, 46, 33, 20, 47, \
    21, 32, 39, 48,  5, 42, 24, 10, 45, 35, \
     4, 26,  2, 29, 34, 41, 16, 22,  3, 23, \
    14, 25, 13, 11, 12, 15, 40,  9 ], dtype = int )

  return att48_order

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

def tsp_att48_xy ( ):

#*****************************************************************************80
#
## tsp_att48_xy() returns the location data for the AT&T 48 city TSP challenge.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real tsp_att48_xy(48,2): the x and y coordinates of the cities.
#
  import numpy as np

  att48_xy = np.array ( [ \
    [ 6734, 1453 ], \
    [ 2233,   10 ], \
    [ 5530, 1424 ], \
    [  401,  841 ], \
    [ 3082, 1644 ], \
    [ 7608, 4458 ], \
    [ 7573, 3716 ], \
    [ 7265, 1268 ], \
    [ 6898, 1885 ], \
    [ 1112, 2049 ], \
    [ 5468, 2606 ], \
    [ 5989, 2873 ], \
    [ 4706, 2674 ], \
    [ 4612, 2035 ], \
    [ 6347, 2683 ], \
    [ 6107,  669 ], \
    [ 7611, 5184 ], \
    [ 7462, 3590 ], \
    [ 7732, 4723 ], \
    [ 5900, 3561 ], \
    [ 4483, 3369 ], \
    [ 6101, 1110 ], \
    [ 5199, 2182 ], \
    [ 1633, 2809 ], \
    [ 4307, 2322 ], \
    [  675, 1006 ], \
    [ 7555, 4819 ], \
    [ 7541, 3981 ], \
    [ 3177,  756 ], \
    [ 7352, 4506 ], \
    [ 7545, 2801 ], \
    [ 3245, 3305 ], \
    [ 6426, 3173 ], \
    [ 4608, 1198 ], \
    [   23, 2216 ], \
    [ 7248, 3779 ], \
    [ 7762, 4595 ], \
    [ 7392, 2244 ], \
    [ 3484, 2829 ], \
    [ 6271, 2135 ], \
    [ 4985,  140 ], \
    [ 1916, 1569 ], \
    [ 7280, 4899 ], \
    [ 7509, 3239 ], \
    [   10, 2676 ], \
    [ 6807, 2993 ], \
    [ 5185, 3258 ], \
    [ 3023, 1942 ] ] )

  return att48_xy

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
  tsp_att48_test ( )
  timestamp ( )

