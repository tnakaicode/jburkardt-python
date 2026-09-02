#! /usr/bin/env python3
#
def test_graph_arc_test ( ):

#*****************************************************************************80
#
## test_graph_arc_test() tests test_graph_arc().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'test_graph_arc_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test test_graph_arc().' )

  graph_arc_print ( 'bush', graph_arc_bush )
  graph_arc_print ( 'coxeter', graph_arc_coxeter )
  graph_arc_print ( 'cube', graph_arc_cube )
  graph_arc_print ( 'diamond', graph_arc_diamond )
  graph_arc_print ( 'dodecahedron', graph_arc_dodecahedron )
  m = 4
  n = 5
  graph_arc_print ( 'knight', graph_arc_knight, m, n )
  graph_arc_print ( 'museum', graph_arc_museum )
  graph_arc_print ( 'octahedron', graph_arc_octahedron )
  graph_arc_print ( 'petersen', graph_arc_petersen )
  graph_arc_print ( 'sauer', graph_arc_sauer )
  graph_arc_print ( 'twig', graph_arc_twig )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_graph_arc_test():' )
  print ( '  Normal end of execution.' )

  return

def graph_arc_bush ( ):

#*****************************************************************************80
#
## graph_arc_bush() sets up the arc list for the bush graph.
#
#  Discussion:
#
#    The graph has 7 nodes.
#    The graph has 6 edges or 12 arcs.
#    The graph is a tree.
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
#    01 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(arc_num,2): the arc list.  
#
  import numpy as np

  L = np.array ( [ \
   [ 1, 4 ], \
   [ 2, 5 ], \
   [ 3, 5 ], \
   [ 4, 1 ], \
   [ 4, 5 ], \
   [ 4, 6 ], \
   [ 4, 7 ], \
   [ 5, 2 ], \
   [ 5, 3 ], \
   [ 5, 4 ], \
   [ 6, 4 ], \
   [ 7, 4 ] ], dtype = int )

  L = L - 1

  return L

def graph_arc_coxeter ( ):

#*****************************************************************************80
#
## graph_arc_coxeter() sets up the arc list for the Coxeter graph.
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
#    integer L(arc_num,2): the arc list.  
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

  return L

def graph_arc_cube ( ):

#*****************************************************************************80
#
## graph_arc_cube() sets up the arc list for the cube graph.
#
#  Discussion:
#
#    There are 8 nodes.  
#    There are 12 edges or 24 arcs.
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
#    01 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(arc_num,2): the arc list.
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
   [ 4, 8 ], \
   [ 5, 1 ], \
   [ 5, 2 ], \
   [ 5, 4 ], \
   [ 6, 1 ], \
   [ 6, 2 ], \
   [ 6, 3 ], \
   [ 7, 2 ], \
   [ 7, 3 ], \
   [ 7, 4 ], \
   [ 8, 1 ], \
   [ 8, 3 ], \
   [ 8, 4 ] ], dtype = int )

  L = L - 1

  return L

def graph_arc_diamond ( ):

#*****************************************************************************80
#
## graph_arc_example_diamond() returns the graph of a "diamond" 3D shape.
#
#  Discussion:
#
#    The graph has 10 nodes.
#    The graph has 20 edges or 40 arcs.
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
#    01 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(arc_num,2): the arc list.
#
  import numpy as np

  L = np.array ( [ \
  [  1,  2 ], \
  [  1,  3 ], \
  [  1,  4 ], \
  [  1,  5 ], \
  [  2,  1 ], \
  [  2,  3 ], \
  [  2,  5 ], \
  [  2,  6 ], \
  [  3,  1 ], \
  [  3,  2 ], \
  [  3,  4 ], \
  [  3,  7 ], \
  [  4,  1 ], \
  [  4,  3 ], \
  [  4,  5 ], \
  [  4,  8 ], \
  [  5,  1 ], \
  [  5,  2 ], \
  [  5,  4 ], \
  [  5,  9 ], \
  [  6,  2 ], \
  [  6,  7 ], \
  [  6,  9 ], \
  [  6, 10 ], \
  [  7,  3 ], \
  [  7,  6 ], \
  [  7,  8 ], \
  [  7, 10 ], \
  [  8,  4 ], \
  [  8,  7 ], \
  [  8,  9 ], \
  [  8, 10 ], \
  [  9,  5 ], \
  [  9,  6 ], \
  [  9,  8 ], \
  [  9, 10 ], \
  [ 10,  6 ], \
  [ 10,  7 ], \
  [ 10,  8 ], \
  [ 10,  9 ] ], dtype = int )

  L = L - 1

  return L

def graph_arc_dodecahedron ( ):

#*****************************************************************************80
#
## graph_arc_dodecahedron(): arc list for the dodecahedron graph.
#
#  Discussion:
#
#    There are 20 nodes.
#    There are 30 edges or 60 arcs.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(arc_num,2): the arc list.
#
  import numpy as np

  L = np.array ( [ \
   [  1,  2 ], \
   [  1,  5 ], \
   [  1,  6 ], \
   [  2,  1 ], \
   [  2,  3 ], \
   [  2,  8 ], \
   [  3,  2 ], \
   [  3,  4 ], \
   [  3, 10 ], \
   [  4,  3 ], \
   [  4,  5 ], \
   [  4, 12 ], \
   [  5,  1 ], \
   [  5,  4 ], \
   [  5, 14 ], \
   [  6,  1 ], \
   [  6,  7 ], \
   [  6, 15 ], \
   [  7,  6 ], \
   [  7,  8 ], \
   [  7, 17 ], \
   [  8,  2 ], \
   [  8,  7 ], \
   [  8,  9 ], \
   [  9,  8 ], \
   [  9, 10 ], \
   [  9, 16 ], \
   [ 10,  3 ], \
   [ 10,  9 ], \
   [ 10, 11 ], \
   [ 11, 10 ], \
   [ 11, 12 ], \
   [ 11, 20 ], \
   [ 12,  4 ], \
   [ 12, 11 ], \
   [ 12, 13 ], \
   [ 13, 12 ], \
   [ 13, 14 ], \
   [ 13, 19 ], \
   [ 14,  5 ], \
   [ 14, 13 ], \
   [ 14, 15 ], \
   [ 15,  6 ], \
   [ 15, 14 ], \
   [ 15, 18 ], \
   [ 16,  9 ], \
   [ 16, 17 ], \
   [ 16, 20 ], \
   [ 17,  7 ], \
   [ 17, 16 ], \
   [ 17, 18 ], \
   [ 18, 15 ], \
   [ 18, 17 ], \
   [ 18, 19 ], \
   [ 19, 13 ], \
   [ 19, 18 ], \
   [ 19, 20 ], \
   [ 20, 11 ], \
   [ 20, 16 ], \
   [ 20, 19 ] ], dtype = int )

  L = L - 1

  return L

def graph_arc_knight ( m, n ):

#*****************************************************************************80
#
## graph_arc_knight() returns the arc list for a knight's move chess board. 
#
#  Discussion:
#
#    There are MxN nodes.
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
#    The arc list is simply a table of all nodes paired in this way.
#
#    For the 4x5 board above, the arc list begins:
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
#    01 May 2026
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
#    integer L(arc_num,2): the pairs of nodes connected by a knight move.
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

  return L

def graph_arc_museum ( ):

#*****************************************************************************80
#
## graph_arc_museum() sets up the arc list for the museum graph.
#
#  Discussion:
#
#    The graph has 18 nodes.
#    The graph has 17 edges or 34 arcs.
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
#    01 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L[17,2]: the arc list.
#
  import numpy as np

  L = np.array ( [ \
  [  1,  7 ], \
  [  2,  3 ], \
  [  2,  8 ], \
  [  3,  2 ], \
  [  4,  5 ], \
  [  5,  4 ], \
  [  5,  6 ], \
  [  5, 11 ], \
  [  6,  5 ], \
  [  7,  1 ], \
  [  7, 13 ], \
  [  8,  2 ], \
  [  8,  9 ], \
  [  8, 14 ], \
  [  9,  8 ], \
  [  9, 10 ], \
  [  9, 15 ], \
  [ 10,  9 ], \
  [ 11,  5 ], \
  [ 11, 12 ], \
  [ 11, 17 ], \
  [ 12, 11 ], \
  [ 12, 18 ], \
  [ 13,  7 ], \
  [ 13, 14 ], \
  [ 14,  8 ], \
  [ 14, 13 ], \
  [ 15,  9 ], \
  [ 15, 16 ], \
  [ 16, 15 ], \
  [ 16, 17 ], \
  [ 17, 11 ], \
  [ 17, 16 ], \
  [ 18, 12 ] ], dtype = int )

  L = L - 1

  return L

def graph_arc_octahedron ( ):

#*****************************************************************************80
#
## graph_arc_octahedron() sets up the octahedron arc list.
#
#  Discussion:
#
#    The graph has 8 nodes.
#    The graph has 12 edges or 24 arcs.
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
#    01 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(arc_num,2): the arc list.
#
  import numpy as np

  L = np.array ( [ \
   [ 1, 2 ], \
   [ 1, 6 ], \
   [ 1, 8 ], \
   [ 2, 1 ], \
   [ 2, 3 ], \
   [ 2, 5 ], \
   [ 3, 2 ], \
   [ 3, 4 ], \
   [ 3, 8 ], \
   [ 4, 3 ], \
   [ 4, 5 ], \
   [ 4, 7 ], \
   [ 5, 2 ], \
   [ 5, 4 ], \
   [ 5, 6 ], \
   [ 6, 1 ], \
   [ 6, 5 ], \
   [ 6, 7 ], \
   [ 7, 4 ], \
   [ 7, 6 ], \
   [ 7, 8 ], \
   [ 8, 1 ], \
   [ 8, 3 ], \
   [ 8, 7 ] ], dtype = int )

  L = L - 1

  return L

def graph_arc_petersen ( ):

#*****************************************************************************80
#
## graph_arc_petersen() sets up the arc list for the Petersen graph.
#
#  Discussion:
#
#    The graph has 10 nodes.
#    The graph has 15 edges or 30 arcs.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer arc(arc_num,2): the arc list.  
#
  import numpy as np

  L = np.array ( [ \
  [  1,  2 ], \
  [  1,  5 ], \
  [  1,  6 ], \
  [  2,  1 ], \
  [  2,  3 ], \
  [  2,  7 ], \
  [  3,  2 ], \
  [  3,  4 ], \
  [  3,  8 ], \
  [  4,  3 ], \
  [  4,  5 ], \
  [  4,  9 ], \
  [  5,  1 ], \
  [  5,  4 ], \
  [  5, 10 ], \
  [  6,  1 ], \
  [  6,  7 ], \
  [  6, 10 ], \
  [  7,  2 ], \
  [  7,  6 ], \
  [  7,  8 ], \
  [  7, 10 ], \
  [  8,  3 ], \
  [  8,  7 ], \
  [  8, 10 ], \
  [  9,  4 ], \
  [ 10,  5 ], \
  [ 10,  6 ], \
  [ 10,  7 ], \
  [ 10,  8 ] ], dtype = int )

  L = L - 1

  return L

def graph_arc_sauer ( ):

#*****************************************************************************80
#
## graph_arc_sauer() returns the arc list for the Sauer web.
#
#  Discussion:
#
#    The graph has 15 nodes.
#    The graph has 31 edges or 62 arcs.
#
#    This matrix appears on page 564 of the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2026
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
#    integer L(arc_num,2): the arc list.
#
  import numpy as np

  L = np.array ( [ \
  [  1,  2 ], \
  [  1,  5 ], \
  [  1,  9 ], \
  [  2,  1 ], \
  [  2,  3 ], \
  [  2,  5 ], \
  [  2,  7 ], \
  [  3,  2 ], \
  [  3,  4 ], \
  [  3,  6 ], \
  [  3,  8 ], \
  [  4,  3 ], \
  [  4,  8 ], \
  [  4, 12 ], \
  [  5,  1 ], \
  [  5,  2 ], \
  [  5,  9 ], \
  [  5, 10 ], \
  [  6,  3 ], \
  [  6,  9 ], \
  [  6, 10 ], \
  [  6, 11 ], \
  [  7,  2 ], \
  [  7, 10 ], \
  [  7, 11 ], \
  [  7, 12 ], \
  [  8,  3 ], \
  [  8,  4 ], \
  [  8, 11 ], \
  [  8, 12 ], \
  [  9,  1 ], \
  [  9,  5 ], \
  [  9,  6 ], \
  [  9, 10 ], \
  [  9, 13 ], \
  [ 10,  5 ], \
  [ 10,  6 ], \
  [ 10,  7 ], \
  [ 10,  9 ], \
  [ 10, 13 ], \
  [ 10, 14 ], \
  [ 11,  6 ], \
  [ 11,  7 ], \
  [ 11,  8 ], \
  [ 11, 12 ], \
  [ 11, 14 ], \
  [ 11, 15 ], \
  [ 12,  4 ], \
  [ 12,  7 ], \
  [ 12,  8 ], \
  [ 12, 11 ], \
  [ 12, 15 ], \
  [ 13,  9 ], \
  [ 13, 10 ], \
  [ 13, 14 ], \
  [ 14, 10 ], \
  [ 14, 11 ], \
  [ 14, 13 ], \
  [ 14, 15 ], \
  [ 15, 11 ], \
  [ 15, 12 ], \
  [ 15, 14 ] ], dtype = int )

  L = L - 1

  return L

def graph_arc_twig ( ):

#*****************************************************************************80
#
## graph_arc_twig() sets up the arc list for the twig graph.
#
#  Discussion:
#
#    The graph has 3 nodes.
#    The graph has 2 edges or 4 arcs.
#
#    1---2---3
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L[arc_num,2]: the arc list.
#
  import numpy as np

  L = np.array ( [ \
    [ 1, 2 ], \
    [ 2, 1 ], \
    [ 2, 3 ], \
    [ 3, 2 ] ], dtype = int )

  L = L - 1

  return L

def graph_arc_print ( graph_title, graph_list, m = None, n = None ):

#*****************************************************************************80
#
## graph_arc_print() prints the arc list of a graph.
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
#    function: a function which returns the arc list of the graph.
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
  print ( 'graph_arc_print():' )
  print ( '  Print definition of "' + graph_title + '"' )

  if ( m == None and n == None ):
    L = graph_list ( )
  elif ( n == None ):
    L = graph_list ( m, m )
  else:
    L = graph_list ( m, n )

  arc_num = L.shape[0]
  node_num = np.max ( L ) + 1

  print ( '' )
  print ( '  Number of nodes = ', node_num )
  print ( '  Number of edges = ', arc_num )

  print ( '' )
  print ( '  arc list L:' )
  pprint.pprint ( L )

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
  test_graph_arc_test ( )
  timestamp ( )

