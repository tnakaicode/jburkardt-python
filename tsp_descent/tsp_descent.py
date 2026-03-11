#! /usr/bin/env python3
#
def tsp_descent ( filename ):

#*****************************************************************************80
#
## tsp_descent() seeks an optimal traveling salesperson (TSP) path using  descent.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2022
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
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'tsp_descent():' )
  print ( '  Solve a small traveling salesperson problem (TSP) using' )
  print ( '  a descent method, generating reversals and' )
  print ( '  transpositions of a random starting tour.' )
#
#  Read the distance table.
#
  distance = distance_from_file ( filename )

  n = distance.shape[0]
#
#  Choose a random starting route.
#
  p = rng.permutation ( n )
#
#  Save the cost.
#
  cost = path_cost ( n, distance, p )
#
#  Consider VARIATION_NUM variations.
#
  variation_num = 1000
  transpose_num = 0
  reversal_num = 0

  cities = np.arange ( 0, n )

  for variation in range ( 0, variation_num ):
#
#  Variation: transpose.
#
#  Pick two distinct itinerary indices that are not neighbors.
#
    while ( True ):
      c = rng.choice ( cities, size = 2, replace = False )
      i1 = np.min ( c )
      i2 = np.max ( c )
      if ( i1 + 1 < i2 ):
        break

    transpose_num = transpose_num + 1

    p2 = np.zeros ( n, dtype = int )
    p2[0:i1+1]    = p[0:i1+1]
    p2[i1+1]      = p[i2]
    p2[i1+2:i2+1] = p[i1+1:i2]
    p2[i2+1:n]    = p[i2+1:n]

    cost2 = path_cost ( n, distance, p2 )

    if ( cost2 < cost ):
      p = p2.copy ( )
      cost = cost2
      print ( '  Transpose %d: cost = %g' % ( transpose_num, cost ) )
#
#  Variation: reverse order.
#
#  Pick two distinct city indices.
#
    c = rng.choice ( cities, size = 2, replace = False )
    i1 = np.min ( c )
    i2 = np.max ( c )
#
#  The idiosyncratic Python indexing format makes it 
#  essentially impossible to reliably reverse an array segment!
#
    reversal_num = reversal_num + 1
#   p2 = [ p(1:i1-1), p(i2:-1:i1), p(i2+1:n) ]
    p2 = p.copy()
    p2[i1:i2+1] = np.flip ( p2[i1:i2+1] )

    cost2 = path_cost ( n, distance, p2 )

    if ( cost2 < cost ):
      p = p2.copy ( )
      cost = cost2
      print ( '  Reversal %d: cost = %g' % ( reversal_num, cost ) )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variations tried was', 2 * variation_num )
  print ( '' )
  print ( '  The best itinerary found:' )
  print ( '' )
  print ( '  Step  From  To        Distance' )
  print ( '' )
  for i1 in range ( 0, n ):
    i2 = ( i1 + 1 ) % n
    print ( '  %4d    %2d  %2d  %14.6g' \
      % ( i2, p[i1], p[i2], distance [ p[i1], p[i2] ] ) )
  print ( '  ----    --  --  --------------' )
  print ( '  cost:           %14.6g' % ( cost ) )

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
#    06 November 2022
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
    print ( '  Your matrix has M =', m, ', N =', n )
    raise Exception ( 'distance_from_file(): Fatal error!' )

  if ( n < 4 ):
    print ( '' )
    print ( 'distance_from_file(): Fatal error!' )
    print ( '  This problem is too small!' )
    print ( '  The number of cities N must be at least 4.' )
    print ( '  Your matrix has N = ', n )
    raise Exception ( 'distance_from_file(): Fatal error!' )

  v = np.diag ( distance )
  test = np.linalg.norm ( v )

  if ( 0.0 < test ):
    print ( '' )
    print ( 'distance_from_file(): Fatal error!' )
    print ( '  The distance matrix D must have zero diagonal.' )
    print ( '  Your matrix has |diag(D)| = ', test )
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
#    06 November 2022
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
#    integer P(N), a permutation of 0:N-1, the route.
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

def tsp_descent_test ( ):

#*****************************************************************************80
#
## tsp_descent_test() tests tsp_descent().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tsp_descent_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test tsp_descent().' )

  tsp_descent ( 'five.txt' )
  tsp_descent ( 'fifteen.txt' )
  tsp_descent ( 'seventeen.txt' )
  tsp_descent ( 'fortyeight.txt' )
#
#  Terminate.
#
  print ( '' )
  print ( 'tsp_descent_test():' )
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
  tsp_descent_test ( )
  timestamp ( )


