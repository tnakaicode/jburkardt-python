#! /usr/bin/env python3
#
def dijkstra_distance ( nv, ohd ):

#*****************************************************************************80
#
## DIJKSTRA_DISTANCE uses Dijkstra's minimum distance algorithm.
#
#  Discussion:
#
#    We essentially build a tree.  We start with only node 0 connected
#    to the tree, and this is indicated by setting CONNECTED(0) = 1.
#
#    We initialize MIND(I) to the one step distance from node 0 to node I.
#    
#    Now we search among the unconnected nodes for the node MV whose minimum
#    distance is smallest, and connect it to the tree.  For each remaining
#    unconnected node I, we check to see whether the distance from 0 to MV
#    to I is less than that recorded in MIND(I), and if so, we can reduce
#    the distance.
#
#    After NV-1 steps, we have connected all the nodes to 0, and computed
#    the correct minimum distances.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    Original C version by Norm Matloff, CS Dept, UC Davis.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, integer OHD(NV,NV), the distance of the direct link between
#    nodes I and J.
#
#    Output, integer MIND(NV), the minimum distance from node 1 to each node.
#
  import numpy as np
  from sys import exit
#
#  Start out with only node 1 connected to the tree.
#
  connected = np.zeros (nv, dtype = bool )

  connected[0] = True
  for i in range ( 1, nv ):
    connected[i] = False
#
#  Initialize the minimum distance to the one-step distance.
#
  mind = np.zeros ( nv )
  for i in range ( 1, nv ):
    mind[i] = ohd[0,i]
#  
#  Attach one more node on each iteration.
#
  for step in range ( 1, nv ):
#
#  Find the nearest unconnected node.
#
    md, mv = find_nearest ( nv, mind, connected )

    if ( mv == - 1 ):
      print ( '' )
      print ( 'DIJKSTRA_DISTANCE - Fatal error!' )
      print ( '  Search terminated early.' )
      print ( '  Graph might not be connected.' )
      exit ( 'DIJKSTRA_DISTANCE - Fatal error!' )
#
#  Mark this node as connected.
#
    connected[mv] = True
#
#  Having determined the minimum distance to node MV, see if
#  that reduces the minimum distance to other nodes.
#
    mind = update_mind ( nv, mv, connected, ohd, mind )

  return mind

def dijkstra_distance_test ( ):

#*****************************************************************************80
#
## DIJKSTRA_DISTANCE_TEST tests DIJKSTRA_DISTANCE.
#
#  Discussion:
#
#    Given the distance matrix that defines a graph, we seek a list
#    of the minimum distances between node 0 and all other nodes.
#
#    This program sets up a small example problem and solves it.
#
#    The correct minimum distances are:
#
#      0   35   15   45   49   41
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    Original C version by Norm Matloff, CS Dept, UC Davis.
#    Python version by John Burkardt.
#
  import platform

  i4_huge = 2147483647

  print ( '' )
  print ( 'DIJKSTRA_DISTANCE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIJKSTRA_DISTANCE uses Dijkstra\'s algorithm to determine the minimum' )
  print ( '  distance from node 0 to each node in a graph,' )
  print ( '  given the distances between each pair of nodes.' )
#
#  Initialize the problem data.
#
  nv = 6
  ohd = init ( )
#
#  Print the distance matrix.
#
  print ( '' )
  print ( '  Distance matrix:' )
  print ( '' )
  for i in range ( 0, nv ):
    for j in range ( 0, nv ):
      if ( ohd[i,j] == i4_huge ):
        print ( '  Inf', end = '' )
      else:
        print ( '  %3d' % ( ohd[i,j] ), end = '' )
    print ( '' )
#
#  Carry out the algorithm.
#
  mind = dijkstra_distance ( nv, ohd )
#
#  Print the results.
#
  i4vec_transpose_print ( nv, mind, '  Distance to node 0:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIJKSTRA_DISTANCE_TEST' )
  print ( '  Normal end of execution.' )
  return

def find_nearest ( nv, mind, connected ):

#*****************************************************************************80
#
## FIND_NEAREST finds the nearest unconnected node.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    Original C version by Norm Matloff, CS Dept, UC Davis.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, integer NV, the number of nodes.
#
#    Input, integer MIND(NV), the currently computed minimum distance from
#    node 1 to each node.
#
#    Input, integer CONNECTED(NV), is 1 for each connected node, whose 
#    minimum distance to node 1 has been determined.
#
#    Output, integer D, the distance from node 1 to the nearest 
#    unconnected node.
#
#    Output, integer V, the index of the nearest unconnected node.
#
  i4_huge = 2147483647 

  d = i4_huge
  v = -1
  for i in range ( 0, nv ):
    if ( not connected[i] and mind[i] <= d ):
      d = mind[i]
      v = i

  return d, v

def i4vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## I4VEC_TRANSPOSE_PRINT prints an I4VEC "transposed".
#
#  Example:
#
#    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
#    TITLE = 'My vector:  '
#
#    My vector:
#
#       1    2    3    4    5
#       6    7    8    9   10
#      11
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  if ( 0 < n ):
    for i in range ( 0, n ):
      print ( '%8d' % ( a[i] ), end = '' )
      if ( ( i + 1 ) % 10 == 0 or i == n - 1 ):
        print ( '' )
  else:
    print ( '  (empty vector)' )

  return

def i4vec_transpose_print_test ( ):

#*****************************************************************************80
#
## I4VEC_TRANSPOSE_PRINT_TEST tests I4VEC_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4VEC_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_TRANSPOSE_PRINT prints an I4VEC' )
  print ( '  with 5 entries to a row, and an optional title.' )

  n = 12
  a = np.zeros ( n, dtype = np.int32 )
  
  for i in range ( 0, n ):
    a[i] = i + 1

  i4vec_transpose_print ( n, a, '  My array:  ' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_TRANSPOSE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def init ( ):

#*****************************************************************************80
#
## INIT initializes the problem data.
#
#  Discussion:
#
#    The graph uses 6 nodes, and has the following diagram and
#    distance matrix:
#
#    N1--15--N3-100--N4           0   40   15  Inf  Inf  Inf
#      \      |     /            40    0   20   10   25    6
#       \     |    /             15   20    0  100  Inf  Inf
#        40  20  10             Inf   10  100    0  Inf  Inf
#          \  |  /              Inf   25  Inf  Inf    0    8
#           \ | /               Inf    6  Inf  Inf    8    0
#            N2
#            / \
#           /   \
#          6    25
#         /       \
#        /         \
#      N6----8-----N5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    Original C version by Norm Matloff, CS Dept, UC Davis.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Output, int OHD(NV,NV), the distance of the direct link between
#    nodes I and J.
#
  import numpy as np

  i4_huge = 2147483647

  nv = 6
  ohd = np.zeros ( [ nv, nv ] )

  for i in range ( 0, nv ):
    for j in range ( 0, nv ):
      ohd[i,j] = i4_huge
    ohd[i,i] = 0

  ohd[0,1] = 40
  ohd[1,0] = 40
  ohd[0,2] = 15
  ohd[2,0] = 15
  ohd[1,2] = 20
  ohd[2,1] = 20
  ohd[1,3] = 10
  ohd[3,1] = 10
  ohd[1,4] = 25
  ohd[4,1] = 25
  ohd[2,3] = 100
  ohd[3,2] = 100
  ohd[1,5] = 6
  ohd[5,1] = 6
  ohd[4,5] = 8
  ohd[5,4] = 8

  return ohd

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def update_mind ( nv, mv, connected, ohd, mind ):

#*****************************************************************************80
#
## UPDATE_MIND updates the minimum distance vector.
#
#  Discussion:
#
#    We've just determined the minimum distance to node MV.
#
#    For each node I which is not connected yet,
#    check whether the route from node 1 to MV to I is shorter
#    than the currently known minimum distance.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 January 2016
#
#  Author:
#
#    Original C version by Norm Matloff, CS Dept, UC Davis.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, integer MV, the node whose minimum distance to node 1
#    has just been determined.
#
#    Input, integer CONNECTED(NV), is 1 for each connected node, whose 
#    minimum distance to node 1 has been determined.
#
#    Input, integer OHD(NV)(NV), the distance of the direct link between
#    nodes I and J.
#
#    Input, integer MIND(NV), the currently computed minimum distances
#    from node 1 to each node.
#
#    Output, integer MIND(NV), the currently computed minimum distances
#    from node 1 to each node.
#
  i4_huge = 2147483647

  for i in range ( 0, nv ):
    if ( not connected[i] ):
      if ( ohd[mv,i] < i4_huge ):
        mind[i] = min ( mind[i], mind[mv] + ohd[mv,i] )

  return mind

if ( __name__ == '__main__' ):
  timestamp ( )
  dijkstra_distance_test ( )
  timestamp ( )

