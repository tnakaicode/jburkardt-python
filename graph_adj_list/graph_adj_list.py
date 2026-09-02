#! /usr/bin/env python3
#
def graph_adj_list_test ( ):

#*****************************************************************************80
#
## graph_adj_list_test() tests graph_adj_list().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'graph_adj_list_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test graph_adj_list().' )

  graph_adj_list_to_adj_test ( )
  graph_adj_list_to_arc_test ( )
  graph_adj_to_adj_list_test ( )
  graph_arc_to_adj_list_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'graph_adj_list_test():' )
  print ( '  Normal end of execution.' )

  return

def graph_adj_list_print ( title, AP, AL ):

#*****************************************************************************80
#
## graph_adj_list_print() prints an adjacency list.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string title: a title.
#
#    integer AP(node_num+1): the index of the first edge for each node.
#
#    integer AL(edge_num): the list of ending nodes for each edge.
#
  print ( '' )
  print ( '  ' + title )
  print ( '' )

  node_num = len ( AP ) - 1
  edge_num = len ( AL )

  for node_i in range ( 0, node_num ):
    print ( '  %2d:' % ( node_i ), end = '' )
    
    for k in range ( AP[node_i], AP[node_i+1] ):
      node_j = AL[k]
      print ( ' %2d' % ( node_j ), end = '' )
    print ( '' )

  return

def graph_adj_list_to_adj ( AP, AL ):

#*****************************************************************************80
#
## graph_adj_list_to_adj() converts an adjacency list to an adjacency matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer AP(node_num+1): the index of the first edge for each node.
#
#    integer AL(edge_num): the list of ending nodes for each edge.
#
#  Output:
#
#    integer A(node_num,node_num), the adjacency matrix.
#
  import numpy as np

  node_num = len ( AP ) - 1
  edge_num = len ( AL )

  A = np.zeros ( [ node_num, node_num ], dtype = int )

  for node_i in range ( 0, node_num ):
    for edge in range ( AP[node_i], AP[node_i+1] ):
      node_j = AL[edge]
      A[node_i,node_j] = 1

  return A

def graph_adj_list_to_adj_test ( ):

#*****************************************************************************80
#
## graph_adj_list_to_adj_test() tests graph_adj_list_to_adj().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  AP = np.array ( [ \
    1,  8, 12, 15, 17, 19, 21, 23, 26,  29, \
   33, 35, 37, 39 ] )

  AL = np.array ( [ \
    2, 3, 4, 5, 6, 7, 8, 1, 5, 6, \
    8, 1, 4, 7, 1, 3, 1, 2, 1, 2, \
    1, 3, 1, 2, 9, 8,10,13, 9,11, \
   12,13,10,12,10,11, 9,10 ] )
#
#  Shift from 1-based to 0-based indexing.
#
  AP = AP - 1
  AL = AL - 1

  print ( '' )
  print ( 'graph_adj_list_to_adj_test():' )
  print ( '  graph_adj_list_to_adj() converts a graph adjacency list' )
  print ( '  representation of a graph to an adjacency matrix.' )

  edge_num = len ( AL )
  node_num = len ( AP ) - 1
  print ( '' )
  print ( '  Number of edges is ', edge_num )
  print ( '  Number of nodes is ', node_num )

  graph_adj_list_print ( 'The adjacency list', AP, AL )

  A = graph_adj_list_to_adj ( AP, AL )

  print ( '' )
  print ( '  The adjacency matrix:' )
  pprint.pprint ( A )

  return

def graph_adj_list_to_arc ( AP, AL ):

#*****************************************************************************80
#
## graph_adj_list_to_arc() converts an adjacency list to an arc list.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer AP(node_num+1): the index of the first edge for each node.
#
#    integer AL(edge_num): the list of ending nodes for each edge.
#
#  Output:
#
#    integer L(edge_num,2): the arc list.
#
  import numpy as np

  edge_num = len ( AL )
  node_num = len ( AP ) - 1

  L = np.zeros ( [ edge_num, 2 ], dtype = int )

  edge_num = 0
  for node_i in range ( 0, node_num ):
    for k in range ( AP[node_i], AP[node_i+1] ):
      node_j = AL[edge_num]
      L[edge_num,0] = node_i
      L[edge_num,1] = node_j
      edge_num = edge_num + 1

  return L

def graph_adj_list_to_arc_test ( ):

#*****************************************************************************80
#
## graph_adj_list_to_arc_test() tests graph_adj_list_to_arc().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  AP = np.array ( [ \
    1,  8, 12, 15, 17, 19, 21, 23, 26,  29, \
   33, 35, 37, 39 ] )

  AL = np.array ( [ \
    2, 3, 4, 5, 6, 7, 8, 1, 5, 6, \
    8, 1, 4, 7, 1, 3, 1, 2, 1, 2, \
    1, 3, 1, 2, 9, 8,10,13, 9,11, \
   12,13,10,12,10,11, 9,10 ] )
#
#  Shift from 1-based to 0-based indexing.
#
  AP = AP - 1
  AL = AL - 1

  print ( '' )
  print ( 'graph_adj_list_to_arc_test():' )
  print ( '  graph_adj_list_to_arc() converts a graph adjacency list' )
  print ( '  representation of a graph to an arc list.' )

  edge_num = len ( AL )
  node_num = len ( AP ) - 1
  print ( '' )
  print ( '  Number of edges is ', edge_num )
  print ( '  Number of nodes is ', node_num )

  graph_adj_list_print ( 'The adjacency list', AP, AL )

  L = graph_adj_list_to_arc ( AP, AL )

  print ( '' )
  print ( '  The arc list:' )
  pprint.pprint ( L )

  return

def graph_adj_to_adj_list ( A ):

#*****************************************************************************80
#
## graph_adj_to_adj_list() converts an adjacency matrix to an adjacency list.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,node_num), the adjacency matrix.
#
#  Output:
#
#    integer AP(node_num+1): the index of the first edge for each node.
#
#    integer AL(edge_num): the list of ending nodes for each edge.
#
  import numpy as np

  node_num = A.shape[0]
  edge_num = np.sum ( A )

  AP = np.zeros ( node_num + 1, dtype = int )
  AL = np.zeros ( edge_num, dtype = int )

  k = 0
  AP[0] = 0
  for node_i in range ( 0, node_num ):
    for node_j in range ( 0, node_num ):
      if ( A[node_i,node_j] != 0 ):
        AL[k] = node_j
        k = k + 1
    AP[node_i+1] = k

  return AP, AL

def graph_adj_to_adj_list_test ( ):

#*****************************************************************************80
#
## graph_adj_to_adj_list_test() tests graph_adj_to_adj_list().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  A = np.array ( [ \
    [0,1,1,1,1,1,1,1,0,0,0,0,0], \
    [1,0,0,0,1,1,0,1,0,0,0,0,0], \
    [1,0,0,1,0,0,1,0,0,0,0,0,0], \
    [1,0,1,0,0,0,0,0,0,0,0,0,0], \
    [1,1,0,0,0,0,0,0,0,0,0,0,0], \
    [1,1,0,0,0,0,0,0,0,0,0,0,0], \
    [1,0,1,0,0,0,0,0,0,0,0,0,0], \
    [1,1,0,0,0,0,0,0,1,0,0,0,0], \
    [0,0,0,0,0,0,0,1,0,1,0,0,1], \
    [0,0,0,0,0,0,0,0,1,0,1,1,1], \
    [0,0,0,0,0,0,0,0,0,1,0,1,0], \
    [0,0,0,0,0,0,0,0,0,1,1,0,0], \
    [0,0,0,0,0,0,0,0,1,1,0,0,0] ] )

  print ( '' )
  print ( 'graph_adj_to_adj_list_test():' )
  print ( '  graph_adj_to_adj_list() converts an adjacency matrix' )
  print ( '  to an adjacency list.' )

  edge_num = np.sum ( A )
  node_num = A.shape[0]

  print ( '' )
  print ( '  Number of nodes is ', node_num )
  print ( '  Number of edges is ', edge_num )

  print ( '' )
  print ( '  The adjacency matrix:' )
  pprint.pprint ( A )

  AP, AL = graph_adj_to_adj_list ( A )

  graph_adj_list_print ( 'The adjacency list', AP, AL )

  return

def graph_arc_to_adj_list ( L ):

#*****************************************************************************80
#
## graph_arc_to_adj_list() converts an arc list to an adjacency list.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer L(edge_num,2): the arc list.
#
#  Output:
#
#    integer AP(node_num+1): the index of the first edge for each node.
#
#    integer AL(edge_num): the list of ending nodes for each edge.
#
  import numpy as np

  edge_num = L.shape[0]
  node_num = np.max ( L ) + 1
#
#  Sort the information in L.
#
  L = sortrows ( L )
#
#  Allocate arrays.
#
  AP = np.zeros ( node_num + 1, dtype = int )
  AL = np.zeros ( edge_num, dtype = int )
  AL[:] = L[:,1]
#
#  Record the first appearance of each node.
# 
  k = 0
  AP[0] = k
  node = 0

  for edge in range ( 0, edge_num ):
    while ( L[edge,0] != node ):
      node = node + 1
      AP[node] = edge

  node = node + 1
  AP[node] = edge_num
  
  return AP, AL

def graph_arc_to_adj_list_test ( ):

#*****************************************************************************80
#
## graph_arc_to_adj_list_test() tests graph_arc_to_adj_list().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  L = np.array ( [ \
   [  1,     2 ], \
   [  1,     3 ], \
   [  1,     4 ], \
   [  1,     5 ], \
   [  1,     6 ], \
   [  1,     7 ], \
   [  1,     8 ], \
   [  2,     1 ], \
   [  2,     5 ], \
   [  2,     6 ], \
   [  2,     8 ], \
   [  3,     1 ], \
   [  3,     4 ], \
   [  3,     7 ], \
   [  4,     1 ], \
   [  4,     3 ], \
   [  5,     1 ], \
   [  5,     2 ], \
   [  6,     1 ], \
   [  6,     2 ], \
   [  7,     1 ], \
   [  7,     3 ], \
   [  8,     1 ], \
   [  8,     2 ], \
   [  8,     9 ], \
   [  9,     8 ], \
   [  9,    10 ], \
   [  9,    13 ], \
   [ 10,     9 ], \
   [ 10,    11 ], \
   [ 10,    12 ], \
   [ 10,    13 ], \
   [ 11,    10 ], \
   [ 11,    12 ], \
   [ 12,    10 ], \
   [ 12,    11 ], \
   [ 13,     9 ], \
   [ 13,    10 ] ] )
#
#  Switch to 0-based indexing.
#
  L = L - 1

  print ( '' )
  print ( 'graph_arc_to_adj_list_test():' )
  print ( '  graph_arc_to_adj_list() converts an arc list' )
  print ( '  to an adjacency list.' )

  edge_num = L.shape[0]
  node_num = np.max ( L ) + 1

  print ( '' )
  print ( '  Number of nodes is ', node_num )
  print ( '  Number of edges is ', edge_num )

  print ( '' )
  print ( '  The arc list:' )
  pprint.pprint ( L )

  AP, AL = graph_arc_to_adj_list ( L )

  graph_adj_list_print ( 'The adjacency list', AP, AL )

  return

def sortrows ( x ):

#*****************************************************************************80
#
## sortrows() lexically sorts the rows of an array.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    array x[]: the array to be sorted.
#
#  Output:
#
#    array x[]: the sorted array.
#
  import numpy as np

  x = x[ np.lexsort ( x.T[::-1] ) ]

  return x

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
  graph_adj_list_test ( )
  timestamp ( )

