#! /usr/bin/env python3
#
def tsp_greedy ( filename ):

#*****************************************************************************80
#
## tsp_greedy() seeks an optimal traveling salesperson path by the greedy method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file containing the distance
#    matrix information.  This is an optional input.  If it is not provided,
#    the program will prompt for it.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tsp_greedy():' )
  print ( '  For the traveling salesperson problem, find a "greedy"' )
  print ( '  solution by choosing a starting city, and then constructing' )
  print ( '  the tour by always moving to the nearest unvisited city.' )
#
#  Get the distance table.
#
  distance = np.loadtxt ( filename )
#
#  Approve the distance table.
#
  dims = distance.shape

  m = dims[0]
  n = dims[1]

  if ( m != n ):
    print ( '' )
    print ( 'tsp_greedy(): Fatal error!' )
    print ( '  The MxN distance matrix must be square.' )
    print ( '  Your matrix has M = %d, N = %d', m, n )
    raise Exception ( 'tsp_greedy(): Fatal error!' )

  v = np.diagonal ( distance )
  test = np.linalg.norm ( v )

  if ( 0.0 < test ):
    print ( '' )
    print ( 'tsp_greedy(): Fatal error!' )
    print ( '  The distance matrix must have zero diagonal.' )
    print ( '  Your matrix has ||diag(D)|| = %g', test )
    raise Exception ( 'tsp_brute - Fatal error!' )

  test = np.linalg.norm ( distance - distance.transpose ( ) )

  if ( 0.0 < test ):
    print ( '' )
    print ( 'tsp_greedy(): Fatal error!' )
    print ( '  The distance matrix must be symmetric.' )
    print ( '  Your matrix has ||D-D''|| = %g' % ( test ) )
    raise Exception ( 'tsp_brute - Fatal error!' )
#
#  Print the distance matrix.
#
  print ( '' )
  print ( '  The city-to-city distance matrix:' )
  print ( '' )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print ( '  %4g' % ( distance[i,j] ), end = '' )
    print ( '' )
#
#  Initialize the best cost and tour.
#
  cost_best = np.inf
  p_best = np.arange ( n )
#
#  Let each city be the starting point.
#
  for start in range ( 0, n ):

    p = path_greedy ( n, distance, start )
    cost = path_cost ( n, distance, p )

    if ( cost < cost_best ):
      p_best = p.copy()
      cost_best = cost
      print ( '  Greedy tour starting at city', start, ' costs ', cost )
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
    print ( '  %4d    %2d  %2d  %14.6g' \
      % ( i2, p_best[i1], p_best[i2], distance[p_best[i1],p_best[i2]] ) )

  print ( '  ----    --  --  --------------' )
  print ( '  Total:          %14.6g' % ( cost_best ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_greedy():' )
  print ( '  Normal end of execution.' )

  return

def path_cost ( n, distance, p ):

#*****************************************************************************80
#
## path_cost() evaluates the cost of a round trip.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of cities.
#
#    real DISTANCE(N,N), the city to city distance table.
#
#    integer P(N), a permutation of 1:N, the route.
#
#  Output:
#
#    real COST, the cost of the route.
#
  cost = 0.0
  i1 = n - 1
  for i2 in range ( 0, n ):
    cost = cost + distance[p[i1],p[i2]]
    i1 = i2

  return cost

def path_greedy ( n, distance, start ):

#*****************************************************************************80
#
## path_greedy() finds a greedy route for a given start.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of cities.
#
#    real DISTANCE(N,N), the city to city distance table.
#
#    integer START, the starting city.
#
#  Output:
#
#    integer P(N), a greedy route that starts at START.
#
  import numpy as np

  p = np.zeros ( n, dtype = int )
  p[0] = start

  d = distance.copy ( )
  d[:,start] = np.inf

  for i in range ( 0, n ):
    d[i,i] = np.inf

  c1 = start
  for j in range ( 1, n ):
    c2 = np.argmin ( d[c1,:] )
    p[j] = c2
    d[:,c2] = np.inf
    c1 = c2

  return p

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
  import numpy as np
  import platform

  timestamp ( )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  tsp_greedy ( 'five.txt' )
  tsp_greedy ( 'fifteen.txt' )
  tsp_greedy ( 'seventeen.txt' )
  tsp_greedy ( 'fortyeight.txt' )
  timestamp ( )

