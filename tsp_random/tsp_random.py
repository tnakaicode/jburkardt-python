#! /usr/bin/env python3
#
def tsp_random ( filename, sample_num ):

#*****************************************************************************80
#
## tsp_random() seeks an optimal traveling salesperson solution using sampling.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file containing the distance table.
#
#    integer SAMPLE_NUM, the number of samples to choose.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'tsp_random():' )
  print ( '  Solve small traveling salesperson problems using' )
  print ( '  a sampling method.' )
#
#  Read the distance table.
#
  distance = distance_from_file ( filename )

  n = distance.shape[0]
#
#  Get the number of samples.
#
  print ( '' )
  print ( '  Number of samples requested is', sample_num )
#
#  Initialize the least cost and best route.
#
  cost_best = np.inf
  p_best = np.zeros ( n )
  print ( '' )

  for sample in range ( 0, sample_num ):
#
#  Choose a random starting route.
#
    p = rng.permutation ( n )
#
#  Compute the cost.
#
    cost = path_cost ( n, distance, p )

    if ( cost < cost_best ):
      p_best = p.copy ( )
      cost_best = cost
      print ( '  Sample %d: cost = %g' % ( sample, cost ) )
#
#  Report.
#
  print ( '' )
  print ( '  Number of samples tried was', sample_num )
  print ( '' )
  print ( '  The best itinerary found:' )
  print ( '' )
  print ( '  Step  From  To        Distance' )
  print ( '' )
  for i1 in range ( 0, n ):
    i2 = ( ( i1 + 1 ) % n )
    print ( '  %4d    %2d  %2d  %14.6g' \
      % ( i1, p_best[i1], p_best[i2], distance [ p_best[i1], p_best[i2] ] ) )
  print ( '  ----    --  --  --------------' )
  print ( '  cost:           %14.6g' % ( cost_best ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_random():' )
  print ( '  Normal end of execution.' )

  return

def distance_from_file ( filename ):

#*****************************************************************************80
#
## distance_from_file() reads a distance table from a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the file containing the distance table.
#
  import numpy as np

  distance = np.loadtxt ( filename )
#
#  Approve the distance table.
#
  m, n = distance.shape

  if ( m != n ):
    print ( '' )
    print ( 'distance_from_file(): Fatal error!' )
    print ( '  The distance matrix D must be square.' )
    print ( '  Your matrix has M = ', m, ', N = ', n )
    raise Exception ( 'distance_from_file(): Fatal error!' )

  if ( n < 4 ):
    print ( '' )
    print ( 'distance_from_file(): Fatal error!' )
    print ( '  This problem is too small!' )
    print ( '  The number of cities N must be at least 4.' )
    print ( '  Your matrix has N =', n )
    raise Exception ( 'distance_from_file(): Fatal error!' )

  v = np.diag ( distance )
  test = np.linalg.norm ( v )

  if ( 0.0 < test ):
    print ( '' )
    print ( 'distance_from_file(): Fatal error!' )
    print ( '  The distance matrix D must have zero diagonal.' )
    print ( '  Your matrix has |diag(D)| =', test )
    raise Exception ( 'distance_from_file(): Fatal error!' )

  test = np.linalg.norm ( distance - np.transpose ( distance ) )

  if ( 0.0 < test ):
    print ( '' )
    print ( 'distance_from_file(): Fatal error!' )
    print ( '  The distance matrix D must be symmetric.' )
    print ( '  Your matrix has |D-D''| = ', test )
    raise Exception ( 'distance_from_file(): Fatal error!' )
#
#  Print the distance matrix.
#
  print ( '' )
  print ( '  The city-to-city distance matrix D:' )
  print ( '' )

  print ( distance )

  return distance

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
#    29 October 2022
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
    cost = cost + distance [ p[i1], p[i2] ]
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

def tsp_random_test ( ):

#*****************************************************************************80
#
## tsp_random_test() tests tsp_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tsp_random_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test tsp_random().' )

  tsp_random ( 'five.txt', 500 )
  tsp_random ( 'fifteen.txt', 100000 )
  tsp_random ( 'seventeen.txt', 100000 )
  tsp_random ( 'fortyeight.txt', 10000 )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_random_test():' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  tsp_random_test ( )
  timestamp ( )

