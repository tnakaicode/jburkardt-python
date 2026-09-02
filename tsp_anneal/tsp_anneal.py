#! /usr/bin/env python3
#
def tsp_anneal_test ( ):

#*****************************************************************************80
#
## tsp_anneal_test() tests tsp_anneal().
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
  import numpy as np
  import platform
  import pprint

  print ( '' )
  print ( 'tsp_anneal_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test tsp_anneal(), which solves a traveling salesperson' )
  print ( '  problem (TSP) using simulated annealing.' )
#
#  Define the XY coordinates of the cities.
#
  x = tsp_dantzig42_xy ( )

  n = x.shape[0]

  temp_vec = np.array ( [ 1.0, 10.0, 100.0, 1000.0, 10000.0, 100000.0 ] )
  rate = 0.0001

  for temp in temp_vec:
    order, cost = tsp_anneal ( x, temp, rate )
    print ( '' )
    print ( '  temperature = ', temp )
    pprint.pprint ( order )
    print ( '  Path cost = ', cost )
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
  prefix = 'tsp_anneal'
  tsp_display ( prefix, n, x2 )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_anneal_test():' )
  print ( '  Normal end of execution.' )

  return

def tsp_anneal ( x, temp, rate ):

#*****************************************************************************80
#
## tsp_anneal() solves the traveling salesperson problem (TSP) using simulated annealing.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2026
#
#  Author:
#
#    Original R code by James Howard
#    This version by John Burkardt.
#
#  Reference:
#
#    James Howard,
#    Computational Methods for Numerical Analysis with R,
#    CRC Press, 2017,
#    ISBN13: 978-1-4987-2363-3.
#
#  Input:
#
#    real x(n,2): the coordinates of the cities.
#
#    real temp: the annealing temperature.
#    A default value is 100.
#
#    real rate: the annealing rate.
#    A default value is 0.0001
#
#  Output:
#
#    integer order_best(n): the optimal ordering.
#
#    real ybest: the length of the optimal round trip.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  trial_num = 5
  step = 1.0 - rate
#
#  N is the number of cities.
#
  n = x.shape[0]
#
#  Create n-vectors order_best, order_next, order_curr.
#
  order_best = range ( n )
  order_best = rng.permutation ( order_best )
  order_next = order_best.copy ( )
  order_curr = order_best.copy ( )
#
#  Compute the lengths ybest, ynext, ycurr.
#
  cost_best = tsp_tour_cost ( n, x, order_best )
  cost_next = cost_best
  cost_curr = cost_best
#
#  As the temperature decreases, repeatedly adjust the current path.
#
  while ( 1.0 < temp ):

    for trial in range ( 0, trial_num ):
#
#  Pick a path component i to swap with component i-1.
#
      i = rng.integers ( low = 0, high = n, endpoint = False )
      im1 = i - 1
      if ( im1 == -1 ):
        im1 = n - 1
#
#  Create the next path candidate, by swapping positions i and i-1.
#
      order_next = order_curr.copy ( )
#
#  Swap positions of cities i and i-1.
#
      temporary = order_next[i]
      order_next[i] = order_next[im1]
      order_next[im1] = temporary
#
#  Compute the path length.
#
      cost_next = tsp_tour_cost ( n, x, order_next )
#
#  Acceptance depends in part on the current "temperature".
#
      accept = np.exp ( - ( cost_next - cost_curr ) / temp )

      if ( cost_next < cost_curr or rng.random ( ) < accept ):
        order_curr = order_next.copy ( )
        cost_curr = cost_next

      if ( cost_next < cost_best ):
        order_best = order_curr.copy ( )
        cost_best = cost_curr
#
#  Decrease the temperature before next set of trials.
#
    temp = temp * step

  return order_best, cost_best

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
#    21 July 2026
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
#    The code automatically adds a final return to the first city.
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

if ( __name__ == '__main__' ):
  timestamp ( )
  tsp_anneal_test ( )
  timestamp ( )

