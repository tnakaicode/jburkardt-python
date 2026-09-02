#! /usr/bin/env python3
#
def test_graph_adj_test ( ):

#*****************************************************************************80
#
## test_graph_adj_test() tests test_graph_adj().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_graph_adj_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test test_graph_adj().' )

  graph_adj_print ( 'bush', graph_adj_bush )
  graph_adj_print ( 'coxeter', graph_adj_coxeter )
  graph_adj_print ( 'cube', graph_adj_cube )
  graph_adj_print ( 'diamond', graph_adj_diamond )
  graph_adj_print ( 'dodecahedron', graph_adj_dodecahedron )
  m = 4
  n = 5
  graph_adj_print ( 'knight', graph_adj_knight, m, n )
  graph_adj_print ( 'museum', graph_adj_museum )
  graph_adj_print ( 'octahedron', graph_adj_octahedron )
  graph_adj_print ( 'petersen', graph_adj_petersen )
  graph_adj_print ( 'sauer', graph_adj_sauer )
  graph_adj_print ( 'twig', graph_adj_twig )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_graph_adj_test():' )
  print ( '  Normal end of execution.' )

  return

def graph_adj_bush ( ):

#*****************************************************************************80
#
## graph_adj_bush() sets up the adjacency matrix for the bush graph.
#
#  Discussion:
#
#    The graph has 7 nodes and 6 arcs.  It is a tree.
#
#        6   3
#        |   |
#    1---4---5---2
#        |
#        7
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(7,7): the adjacency matrix.  
#
  import numpy as np

  L = np.array ( [ \
    [ 1, 4 ], \
    [ 2, 5 ], \
    [ 3, 5 ], \
    [ 4, 5 ], \
    [ 4, 6 ], \
    [ 4, 7 ] ], dtype = int )

  L = L - 1

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_coxeter ( ):

#*****************************************************************************80
#
## graph_adj_coxeter() sets up the adjacency matrix for the Coxeter graph.
#
#  Discussion:
#
#    The graph has 28 nodes.
#    The graph has 42 edges or 84 arcs.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A(node_num,node_num): the adjacency matrix.  
#
  import numpy as np

  L = np.array ( [ \
       [ 0,  1],
       [ 0,  7],
       [ 0,  9],
       [ 0, 10],
       [ 0, 27],
       [ 1,  0],
       [ 1,  2],
       [ 1,  8],
       [ 1, 19],
       [ 1, 20],
       [ 1, 22],
       [ 2,  1],
       [ 2,  3],
       [ 2,  6],
       [ 2, 11],
       [ 3,  2],
       [ 3,  4],
       [ 3, 24],
       [ 3, 27],
       [ 4,  3],
       [ 4,  5],
       [ 4, 13],
       [ 4, 25],
       [ 5,  4],
       [ 5,  6],
       [ 5, 15],
       [ 5, 26],
       [ 6,  2],
       [ 6,  5],
       [ 6,  7],
       [ 6, 15],
       [ 7,  0],
       [ 7,  6],
       [ 7,  8],
       [ 8,  1],
       [ 8,  7],
       [ 8,  9],
       [ 8, 15],
       [ 9,  0],
       [ 9,  8],
       [ 9, 10],
       [10,  0],
       [10,  9],
       [10, 11],
       [10, 17],
       [11,  2],
       [11, 10],
       [11, 12],
       [11, 18],
       [12, 11],
       [12, 13],
       [12, 19],
       [13,  4],
       [13, 12],
       [13, 14],
       [13, 17],
       [14, 13],
       [14, 15],
       [14, 21],
       [14, 23],
       [14, 24],
       [15,  5],
       [15,  6],
       [15,  8],
       [15, 14],
       [15, 16],
       [15, 22],
       [16, 15],
       [16, 17],
       [16, 20],
       [16, 25],
       [17, 10],
       [17, 13],
       [17, 16],
       [17, 18],
       [18, 11],
       [18, 17],
       [18, 19],
       [18, 27],
       [19,  1],
       [19, 12],
       [19, 18],
       [19, 20],
       [20,  1],
       [20, 16],
       [20, 19],
       [20, 21],
       [21, 14],
       [21, 20],
       [21, 22],
       [22,  1],
       [22, 15],
       [22, 21],
       [22, 23],
       [23, 14],
       [23, 22],
       [23, 24],
       [24,  3],
       [24, 14],
       [24, 23],
       [24, 25],
       [25,  4],
       [25, 16],
       [25, 24],
       [25, 26],
       [26,  5],
       [26, 25],
       [26, 27],
       [27,  0],
       [27,  3],
       [27, 18],
       [27, 26]], dtype = int )

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_cube ( ):

#*****************************************************************************80
#
## graph_adj_cube() sets up the adjacency matrix for the cube graph.
#
#  Diagram:
#
#      4-----7
#     /|    /|
#    8-----3 |
#    | |   | |
#    | 5---|-2
#    |/    |/
#    1-----6
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(12,2): the adjacency matrix.
#
  import numpy as np

  L = np.array ( [ \
    [ 1, 5 ], \
    [ 1, 6 ], \
    [ 1, 8 ], \
    [ 2, 5 ], \
    [ 2, 6 ], \
    [ 2, 7 ], \
    [ 3, 6 ], \
    [ 3, 7 ], \
    [ 3, 8 ], \
    [ 4, 5 ], \
    [ 4, 7 ], \
    [ 4, 8 ] ], dtype = int )

  L = L - 1

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_diamond ( ):

#*****************************************************************************80
#
## graph_adj_example_diamond() returns the graph of a "diamond" 3D shape.
#
#  Discussion:
#
#    The graph has 20 edges and 10 nodes.
#
#        1
#      /| |\
#     / | | \
#    2--3-4--5--(2)
#    |  | |  |
#    6--7-8--9--(6)
#     \ | | /
#      \| |/
#       10
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(20,2): the adjacency matrix.
#
  import numpy as np

  L = np.array ( [ \
    [ 1,  2 ], \
    [ 1,  3 ], \
    [ 1,  4 ], \
    [ 1,  5 ], \
    [ 2,  6 ], \
    [ 3,  7 ], \
    [ 4,  8 ], \
    [ 5,  9 ], \
    [ 6, 10 ], \
    [ 7, 10 ], \
    [ 8, 10 ], \
    [ 9, 10 ], \
    [ 2,  3 ], \
    [ 3,  4 ], \
    [ 4,  5 ], \
    [ 5,  2 ], \
    [ 6,  7 ], \
    [ 7,  8 ], \
    [ 8,  9 ], \
    [ 9,  6 ] ], dtype = int )

  L = L - 1

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_dodecahedron ( ):

#*****************************************************************************80
#
## graph_adj_dodecahedron(): adjacency matrix for the dodecahedron graph.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(30,2): the adjacency matrix.
#
  import numpy as np

  L = np.array ( [ \
    [ 1,2 ], \
    [ 1,5 ], \
    [ 1,6 ], \
    [ 2,3 ], \
    [ 2,8 ], \
    [ 3,4 ], \
    [ 3,10 ], \
    [ 4,5 ], \
    [ 4,12 ], \
    [ 5,14 ], \
    [ 6,7 ], \
    [ 6,15 ], \
    [ 7,8 ], \
    [ 7,17 ], \
    [ 8,9 ], \
    [ 9,10 ], \
    [ 9,16 ], \
    [ 10,11 ], \
    [ 11,12 ], \
    [ 11,20 ], \
    [ 12,13 ], \
    [ 13,14 ], \
    [ 13,19 ], \
    [ 14,15 ], \
    [ 15,18 ], \
    [ 16,17 ], \
    [ 16,20 ], \
    [ 17,18 ], \
    [ 18,19 ], \
    [ 19,20 ] ], dtype = int )

  L = L - 1

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_knight ( m, n ):

#*****************************************************************************80
#
## graph_adj_knight() returns the adjacency matrix for a knight's move chess board. 
#
#  Discussion:
#
#    The MxN board is numbered left to right, top to bottom, as in:
#
#     1  2  3  4  5
#     6  7  8  9 10
#    11 12 13 14 15
#    16 17 18 19 20
#
#    Each square of the chess board is regarded as a node of a graph.  Two
#    nodes are connected (have an arc between them) if a single knight move
#    will transition from one node to the other.
#
#    The adjacency matrix is simply a table of all nodes paired in this way.
#
#    For the 4x5 board above, the adjacency matrix begins:
#
#     1    12
#     1     8
#     2    11
#     2    13
#     2     9
#     3     6
#     3    12
#     3    14
#     3    10
#     4     7
#     4    13
#     4    15
#     5     8
#     5    14
#     ...  ...
#    20     9
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer m, n: the number of rows and columns of the chess board.
#
#  Output:
#
#    integer L(edge_num,2): the pairs of nodes connected by a knight move.
#
  import numpy as np

  L = np.zeros ( [ 0, 2 ], dtype = int )

  node_id = 0
  edge_num = 0
#
#  Choose a vertical level.
#
  for y in range ( 0, m ):
#
#  Consider, from left to right, the nodes at this vertical level.
#
    for x in range ( 0, n ):
#
#  Consider the four ways in which the x coordinate can be changed.
#
      for x_inc in [ -2, -1, +1, +2 ]:
#
#  Consider the corresponding allowed change in y.
#
        y_up = 3 - abs ( x_inc )
        for y_inc in [ - y_up, y_up ]:
#
#  For each possible change, does the target node remain in the board?
#  If so, pair it with the starting node and add it to the list.
#
          if ( \
            0 <= x + x_inc     and \
                 x + x_inc < n and \
            0 <= y + y_inc     and \
                 y + y_inc < m ):
            node_jd = node_id + y_inc * n + x_inc
            edge_num = edge_num + 1
            L = np.append ( L, [ [ node_id, node_jd ] ], axis = 0 )

      node_id = node_id + 1

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_museum ( ):

#*****************************************************************************80
#
## graph_adj_museum() sets up the adjacency matrix for the museum graph.
#
#  Discussion:
#
#    The graph has 18 nodes and 17 arcs.
#    The graph is a tree.
#
#    1   2---3   4---5---6
#    |   |           |
#    7   8---9--10  11--12
#    |   |   |       |   |
#   13--14  15--16--17  18
#    
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L[17,2]: the adjacency matrix.
#
  import numpy as np

  L = np.array ( [ \
   [ 1,  7 ], \
   [ 2,  3 ], \
   [ 2,  8 ], \
   [ 4,  5 ], \
   [ 5,  6 ], \
   [ 5, 11 ], \
   [ 7, 13 ], \
   [ 8,  9 ], \
   [ 8, 14 ], \
   [ 9, 10 ], \
   [ 9, 15 ], \
   [11, 12 ], \
   [11, 17 ], \
   [12, 18 ], \
   [13, 14 ], \
   [15, 16 ], \
   [16, 17 ] ], dtype = int )

  L = L - 1

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_octahedron ( ):

#*****************************************************************************80
#
## graph_adj_octahedron() sets up the octahedron adjacency matrix.
#
#  Discussion:
#
#      1---2
#     /|   |\
#    8-+---+-3
#    | |   | |
#    7-+---+-4
#     \|   |/
#      6---5
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(12,2): the adjacency matrix.
#
  import numpy as np

  L = np.array ( [ \
   [ 1, 2 ], \
   [ 1, 6 ], \
   [ 1, 8 ], \
   [ 2, 3 ], \
   [ 2, 5 ], \
   [ 3, 4 ], \
   [ 3, 8 ], \
   [ 4, 5 ], \
   [ 4, 7 ], \
   [ 5, 6 ], \
   [ 6, 7 ], \
   [ 7, 8 ] ], dtype = int )

  L = L - 1

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_petersen ( ):

#*****************************************************************************80
#
## graph_adj_petersen() sets up the adjacency matrix for the Petersen graph.
#
#  Discussion:
#
#    The graph has 10 nodes and 15 arcs.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer arc(15,2): the adjacency matrix.  
#
  import numpy as np

  L = np.array ( [ \
    [ 1,  2 ], \
    [ 1,  5 ], \
    [ 1,  6 ], \
    [ 2,  3 ], \
    [ 2,  7 ], \
    [ 3,  4 ], \
    [ 3,  8 ], \
    [ 4,  5 ], \
    [ 4,  9 ], \
    [ 5, 10 ], \
    [ 6,  7 ], \
    [ 6, 10 ], \
    [ 7,  8 ], \
    [ 7, 10 ], \
    [ 8, 10 ] ], dtype = int )

  L = L - 1

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_sauer ( ):

#*****************************************************************************80
#
## graph_adj_sauer() returns the adjacency matrix for the Sauer web.
#
#  Discussion:
#
#    15 nodes, 34 links.
#
#    This matrix appears on page 564 of the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Timothy Sauer,
#    Numerical Analysis,
#    Pearson, 2006,
#    ISBN: 0-321-26898-9,
#    LC: QA297.S348
#
#  Output:
#
#    integer L(34,2): the adjacency matrix.
#
  import numpy as np

  L = np.array ( [ \
   [  1,  2 ], \
   [  1,  9 ], \
   [  2,  3 ], \
   [  2,  5 ], \
   [  2,  7 ], \
   [  3,  2 ], \
   [  3,  6 ], \
   [  3,  8 ], \
   [  4,  3 ], \
   [  4, 12 ], \
   [  5,  1 ], \
   [  5, 10 ], \
   [  6, 10 ], \
   [  6, 11 ], \
   [  7, 10 ], \
   [  7, 11 ], \
   [  8,  4 ], \
   [  8, 11 ], \
   [  9,  5 ], \
   [  9,  6 ], \
   [  9, 10 ], \
   [ 10, 13 ], \
   [ 11, 15 ], \
   [ 12,  7 ], \
   [ 12,  8 ], \
   [ 12, 11 ], \
   [ 13,  9 ], \
   [ 13, 14 ], \
   [ 14, 10 ], \
   [ 14, 11 ], \
   [ 14, 13 ], \
   [ 14, 15 ], \
   [ 15, 12 ], \
   [ 15, 14 ] ], dtype = int )

  L = L - 1

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_twig ( ):

#*****************************************************************************80
#
## graph_adj_twig() sets up the adjacency matrix for the twig graph.
#
#  Discussion:
#
#    The graph has 3 nodes and 2 arcs.
#
#    1---2---3
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L[4,2]: the adjacency matrix.
#
  import numpy as np

  L = np.array ( [ \
    [ 1, 2 ], \
    [ 2, 1 ], \
    [ 2, 3 ], \
    [ 3, 2 ] ], dtype = int )

  L = L - 1

  A = graph_arc_to_adj ( L )

  return A

def graph_adj_print ( graph_title, graph_adj, m = None, n = None ):

#*****************************************************************************80
#
## graph_adj_print() prints the adjacency matrix of a graph.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string graph_title: a title for the graph.
#
#    function: a function which returns the adjacency matrix of the graph.
#
#    vargin: optional inputs.
#    If only one input, this is the value of m, the number of rows and
#    columns of the knight graph checkerboard.
#    If two inputs, these are the values of m and n, the number of rows and
#    the number of columns of the knight graph checkerboard.
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'graph_adj_print():' )
  print ( '  Print definition of "' + graph_title + '"' )

  if ( m == None and n == None ):
    A = graph_adj ( )
  elif ( n == None ):
    A = graph_adj ( m, m )
  else:
    A = graph_adj ( m, n )

  arc_num = np.count_nonzero ( A )
  node_num = A.shape[0]

  print ( '' )
  print ( '  Number of nodes = ', node_num )
  print ( '  Number of edges = ', arc_num )

  print ( '' )
  print ( '  adjacency matrix A:' )
  pprint.pprint ( A )

  return

def graph_arc_to_adj ( L ):

#*****************************************************************************80
#
## graph_arc_to_adj() converts an arc list to an adjacency matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer L(edge_num,2): the edge list.
#
#  Output:
#
#    integer A(node_num,node_num), the adjacency matrix.
#
  import numpy as np

  edge_num = L.shape[0]
  node_num = np.max ( L ) + 1

  A = np.zeros ( [ node_num, node_num ], dtype = int )

  for edge_id in range ( 0, edge_num ):
    i = L[edge_id,0]
    j = L[edge_id,1]
    A[i,j] = 1
    A[j,i] = 1

  edge_num = np.count_nonzero ( A )

  return A

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
  test_graph_adj_test ( )
  timestamp ( )

