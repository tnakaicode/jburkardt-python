#! /usr/bin/env python3
#
def tsp_nearest_test ( ):

#*****************************************************************************80
#
## tsp_nearest_test() tests tsp_nearest().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'tsp_nearest_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  For the traveling salesperson problem, find a' )
  print ( '  solution by choosing a starting city, and then constructing' )
  print ( '  the tour by always moving to the nearest unvisited city.' )
#
#  Get the distance table.
#
  x = np.array ( [ \
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

  n = x.shape[0]
#
#  Request the nearest neighbor estimate.
#
  order, cost = tsp_nearest ( x )
#
#  Report.
#
  print ( '' )
  print ( '  The best itinerary found:' )
  print ( '' )
  print ( '  Step  From  To        Distance' )
  print ( '' )

  for i1 in range ( 0, n ):
    i2 = ( ( i1 + 1 ) % n )
    d = np.linalg.norm ( x[order[i1],:] - x[order[i2],:] )
    print ( '  %4d    %2d  %2d  %14.6g' % ( i2, order[i1], order[i2], d ) )

  print ( '  ----    --  --  --------------' )
  print ( '  Total:          %14.6g' % ( cost ) )
#
#  Display the final solution.
#
  x2 = np.zeros ( [ n, 2 ] )

  for i in range ( 0, n ):
    i2 = order[i]
    x2[i,:] = x[i2,:]
#
#  Send the data to the plotter.
#
  prefix = 'tsp_nearest'
  tsp_display ( prefix, n, x2 )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_nearest_test():' )
  print ( '  Normal end of execution.' )

  return

def tsp_nearest ( x ):

#*****************************************************************************80
#
## tsp_nearest() seeks an optimal traveling salesperson path by the nearest neighbor method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x[n,2]: the coordinates of the cities.
#
#  Output:
#
#    integer order_best[n]: the order in which cities are visited.
#
#    real cost_test: the length of the round trip.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tsp_nearest():' )
  print ( '  For the traveling salesperson problem, find a' )
  print ( '  solution by choosing a starting city, and then constructing' )
  print ( '  the tour by always moving to the nearest unvisited city.' )

  n = x.shape[0]
#
#  Initialize the best cost and tour.
#
  cost_best = np.inf
  order_best = np.arange ( n )
#
#  Let each city be the starting point.
#
  for start in range ( 0, n ):

    order = tsp_path_nearest ( n, x, start )
    cost = tsp_tour_cost ( n, x, order )

    if ( cost < cost_best ):
      order_best = order.copy()
      cost_best = cost
      print ( '  Tour starting at city', start, ' costs ', cost )

  return order_best, cost_best

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

def tsp_path_nearest ( n, x, start ):

#*****************************************************************************80
#
## tsp_path_nearest() finds a nearest neighbor route for a given start.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of cities.
#
#    real x[n,2]: the city coordinates.
#
#    integer START, the starting city.
#
#  Output:
#
#    integer order[n]:, a route that starts at START.
#
  import numpy as np
#
#  Set up distance matrix
#
  d = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      d[i,j] = np.linalg.norm ( x[i,:] - x[j,:] )

  d[:,start] = np.inf

  for i in range ( 0, n ):
    d[i,i] = np.inf
#
#  Build the order array.
#
  order = np.zeros ( n, dtype = int )
  order[0] = start

  c1 = start
  for j in range ( 1, n ):
    c2 = np.argmin ( d[c1,:] )
    order[j] = c2
    d[:,c2] = np.inf
    c1 = c2

  return order

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
  tsp_nearest_test ( )
  timestamp ( )

