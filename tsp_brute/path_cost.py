#! /usr/bin/env python
#
def path_cost ( n, distance, p ):

#*****************************************************************************80
#
## PATH_COST evaluates the cost of a round trip.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of cities.
#
#    Input, real DISTANCE(N,N), the city to city distance table.
#
#    Input, integer P(N), a permutation of 1:N, the route.
#
#    Output, real COST, the cost of the route.
#
  cost = 0.0
  i1 = n - 1
  for i2 in range ( 0, n ):
    cost = cost + distance [ p[i1], p[i2] ]
    i1 = i2

  return cost

def path_cost_test ( ):

#*****************************************************************************80
#
## PATH_COST_TEST tests PATH_COST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  distance = np.array ( [\
    [ 0.0,  3.0,  4.0,  2.0,  9.0 ],
    [ 3.0,  0.0,  4.0,  6.0,  3.0 ],
    [ 4.0,  4.0,  0.0,  5.0,  8.0 ],
    [ 2.0,  6.0,  5.0,  0.0,  6.0 ],
    [ 9.0,  3.0,  8.0,  6.0,  0.0 ] ] )

  p = np.array ( [ 0, 3, 2, 1, 4 ] )

  print ( '' )
  print ( 'PATH_COST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PATH_COST returns the cost of a traveling salesman itinerary.' )

  print ( '' )
  print ( '  Number of cities n = %d' % ( n ) )
  print ( '' )
  print ( '  Distance matrix:' )
  print ( '' )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print ( '  %4g' % ( distance[i,j] ), end = '' )
    print ( '' )

  print ( '' )
  print ( '  Itinerary:' )
  for i in range ( 0, n ):
    print ( '  %2d' % ( p[i] ), end = '' )
  print ( '' )

  cost = path_cost ( n, distance, p )

  print ( '' )
  print ( '  Cost of this path is %g' % ( cost ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PATH_COST_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  path_cost_test ( )
  timestamp ( )

