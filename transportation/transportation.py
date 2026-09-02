#! /usr/bin/env python3
#
def transportation_test ( ):

#*****************************************************************************80
#
## transportation_test() tests transportation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import pprint

  print ( '' )
  print ( 'transportation_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test transportation().' )

  m = 3
  n = 4

  print ( '' )
  print ( '  There are', m, 'sources and', n, 'destinations.' )
#
#  Define the cost matrix (m sources x n destinations)
#
  C = np.array ( [ \
    [ 2, 3, 1, 4 ], \
    [ 3, 2, 5, 1 ], \
    [ 4, 3, 2, 2 ] ] )

  print ( '' )
  print ( '  The cost matrix C:' )
  pprint.pprint ( C )
#
#  The supply vector.
#
  supply = np.array ( [ 20, 30, 25 ] )
  print ( '' )
  print ( '  The supply vector:' )
  pprint.pprint ( supply )
#
#  Demand vector.
#
  demand = np.array ( [ 10, 25, 30, 10 ] )
  print ( '' )
  print ( '  The demand vector:' )
  pprint.pprint ( demand )
#
#  Seek a transportation plan.
#
  X = transportation ( supply, demand, C )

  print ( '' )
  print ( '  Transportation matrix:' )
  pprint.pprint ( X )
#
#  Compute transportation cost by elementwise matrix multiplication.
#
  cost = np.sum ( X * C )
  print ( '' )
  print ( '  Transportation Cost ', cost )
#
#  Terminate.
#
  print ( '' )
  print ( 'transportation_test()' )
  print ( '  Normal end of execution.' )

  return

def transportation ( supply, demand, C ):

#*****************************************************************************80
#
## transportation() computes a good solution to the transportation problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Hitchcock,
#    The distribution of a product from several sources to numerous localities,
#    MIT Journal of Mathematics and Physics,
#    Volume 20, pages 224-230, 1941.
#
#  Input:
#
#    real supply(m): the amount of resource available from each supply site.
#
#    real demand(n): the amount of resource needed at each demand site.
#
#    real C(m,n): C(i,j) is the cost of shipping one unit from supply site i 
#    to demand site j.
#
#  Output:
#
#    real X(m,n): X(i,j) is the amount of resource to be shipped from supply
#    site i to demand site j.
#
  import numpy as np
#
#  Make temporary copies of supply and demand.
#
  s = supply.copy ( )
  d = demand.copy ( )
#
#  Initialize the allocation matrix.
#
  m, n = C.shape
  X = np.zeros ( [ m, n ] )

  while ( np.any ( s ) and np.any ( d ) ):
#
#  Find the lowest cost link in the system.
#
    minCost = np.inf
    for i in range ( 0, m ):
      for j in range ( 0, n ):
        if ( ( 0 < s[i] ) and ( 0 < d[j] ) ):
          if ( C[i,j] < minCost ):
            minCost = C[i,j]
            row = i
            col = j
#
#  Allocate as much as possible for this link.
#
    allocation = min ( s[row], d[col] )
    X[row,col] = allocation
#    
#  Reduce the supply and demand by the amount just shipped.
#
    s[row] = s[row] - allocation
    d[col] = d[col] - allocation

  return X

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
  transportation_test ( )
  timestamp ( )

