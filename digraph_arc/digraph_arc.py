#! /usr/bin/env python3
#
def digraph_arc_test ( ):

#*****************************************************************************80
#
## digraph_arc_test() tests digraph_arc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'digraph_arc_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test digraph_arc(), which implements digraph algorithms' )
  print ( '  using an arc list representation.' )

  digraph_adj_to_arc_test ( )
  digraph_arc_degree_test ( )
  digraph_arc_is_eulerian_test ( )
  digraph_arc_to_adj_test ( )
  digraph_arc_to_star_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'digraph_arc_test():' )
  print ( '  Normal end of execution.' )

  return

def digraph_adj_to_arc ( A ):

#*****************************************************************************80
#
## digraph_adj_to_arc() converts digraph from adjacency to arc list form.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,node_num), the adjacency information.
#    A(I,J) is 1 if there is a direct link from node I to node J.
#
#  Output:
#
#    integer L(edge_num,2), the arc list 
#    of the digraph.
#
  import numpy as np

  node_num = A.shape[0]
  edge_num = np.count_nonzero ( A )
  L = np.zeros ( [ edge_num, 2 ] )

  edge_id = 0;

  for j in range ( 0, node_num ):
    for i in range ( 0, node_num ):
      if ( A[i,j] != 0 ):
        L[edge_id,0] = i
        L[edge_id,1] = j
        edge_id = edge_id + 1

  return L

def digraph_arc_degree ( L ):

#*****************************************************************************80
#
## digraph_arc_degree() determines the degree of the nodes of a digraph.
#
#  Discussion:
#
#    The in degree is the number of edges that terminate at a node.
#    The out degree is the number of edges that begin at a node.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer L(edge_num,2), the arc list.
#
#  Output:
#
#    integer INDEGREE(node_num), OUTDEGREE(node_num), the
#    indegree and outdegree of each node, that is, the number of edges that end
#    with the node, and the number of edges that begin with it.
#
  import numpy as np

  edge_num = L.shape[0]
  node_num = np.max ( L ) + 1

  indegree = np.zeros ( node_num )
  outdegree = np.zeros ( node_num )

  for edge_id in range ( 0, edge_num ):

    node_out = L[edge_id,0]
    outdegree[node_out] = outdegree[node_out] + 1

    node_in = L[edge_id,1]
    indegree[node_in] = indegree[node_in] + 1

  return indegree, outdegree

def digraph_arc_example_cycler ( ):

#*****************************************************************************80
#
## digraph_arc_example_cycler() returns the arc list for a 9-node example.
#
#  Diagram:
#  
#           A
#           V
#    9--><--7---<--3--><---4
#    |            /|      /
#    V           A |     /
#    |          /  |    /
#    5----<----1   V   A
#    |        /    |  /
#    V       A     | /
#    |      /      |/
#    2-->---8---<--6
#     \------>----/
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer L(16,2), the arc list.
#
  import numpy as np

  arc_num = 16

  L = np.array ( [ \
    [ 0,     2 ], \
    [ 0,     4 ], \
    [ 1,     5 ], \
    [ 1,     7 ], \
    [ 2,     3 ], \
    [ 2,     5 ], \
    [ 2,     6 ], \
    [ 3,     2 ], \
    [ 4,     1 ], \
    [ 5,     3 ], \
    [ 5,     7 ], \
    [ 6,     6 ], \
    [ 6,     8 ], \
    [ 7,     0 ], \
    [ 8,     4 ], \
    [ 8,     6 ] ] )

  return L

def digraph_arc_is_eulerian ( L ):

#*****************************************************************************80
#
## digraph_arc_is_eulerian() determines if a digraph is Eulerian.
#
#  Discussion:
#
#    A digraph is Eulerian if there exists a circuit through the graph
#    which uses every edge once.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer node_num, the number of nodes.
#
#    integer edge_num, the number of edges.
#
#    integer L(edge_num,2), the edge list.
#
#  Output:
#
#    integer answer.
#    0, the digraph is not Eulerian.
#    1, the digraph is Eulerian, but the starting and ending nodes differ.
#    2, the digraph is Eulerian, and there is a closed Euler circuit.
#
  import numpy as np

  node_num = np.max ( L ) + 1

  indegree, outdegree = digraph_arc_degree ( L )

  n_plus = 0
  n_minus = 0

  for i in range ( 0, node_num ):

    if ( indegree[i] == outdegree[i] ):
      continue
    elif ( n_plus == 0 and indegree[i] == outdegree[i] + 1 ):
      n_plus = 1
    elif ( n_minus == 0 and indegree[i] == outdegree[i] - 1 ):
      n_minus = 1
    else:
      answer = 0
      return answer

  if ( n_plus == 0 and n_minus == 0 ):
    answer = 2
  elif ( n_plus == 1 and n_minus == 1 ):
    answer = 1
  else:
    print ( '' )
    print ( 'digraph_arc_is_eulerian(): Fatal error!' )
    print ( '  The algorithm failed.' )
    raise Exception ( 'digraph_arc_is_eulerian(): Fatal error!' )

  return answer

def digraph_adj_to_arc_test ( ):

#*****************************************************************************80
#
## digraph_adj_to_arc_test() tests digraph_adj_to_arc()
#
#    1->---2-->---3
#    |     |      |
#    A     V      V
#    |     |      |
#    6--<--5--<---4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  node_num = 6
  edge_num = 6

  print ( '' )
  print ( 'digraph_adj_to_arc_test():' )
  print ( '  digraph_adj_to_arc() converts a digraph in' )
  print ( '  adjacency form to arc list form' )

  A = np.array ( [ \
    [ 0,     1,     0,     0,     0,     0 ], \
    [ 0,     0,     1,     0,     0,     0 ], \
    [ 0,     0,     0,     1,     0,     0 ], \
    [ 0,     0,     0,     0,     1,     0 ], \
    [ 0,     0,     0,     0,     0,     1 ], \
    [ 0,     1,     0,     0,     0,     0 ] ] )

  print ( '' )
  print ( '  The digraph adjacency matrix:' )
  pprint.pprint ( A )

  L = digraph_adj_to_arc ( A )

  print ( '' )
  print ( '  The digraph edge list:' )
  pprint.pprint ( L )

  return

def digraph_arc_degree_test ( ):

#*****************************************************************************80
#
## digraph_arc_degree_test() tests digraph_arc_degree().
#
#  5--2--10--1--3--6
#         |  |  | /
#         8  |  9
#         |  |
#         4--7
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'digraph_arc_degree_test():' )
  print ( '  digraph_arc_degree() computes the degree of the nodes,' )

  L = np.array ( [ \
    [ 0,     2 ], \
    [ 0,     6 ], \
    [ 0,     9 ], \
    [ 1,     4 ], \
    [ 1,     9 ], \
    [ 2,     5 ], \
    [ 2,     8 ], \
    [ 3,     6 ], \
    [ 3,     7 ], \
    [ 5,     8 ], \
    [ 7,     9 ] ] )

  print ( '' )
  print ( '  The digraph arc list:' )
  pprint.pprint (  L )

  indegree, outdegree = digraph_arc_degree ( L )

  D = np.transpose ( np.stack ( [ indegree, outdegree ] ) )
  print ( '  The in- and out- degrees:' )
  pprint.pprint ( D )

  return

def digraph_arc_is_eulerian_test ( ):

#*****************************************************************************80
#
## digraph_arc_is_eulerian_test() tests digraph_arc_is_eulerian().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  L = np.array ( [ \
    [ 0,     1 ], \
    [ 2,     0 ], \
    [ 0,     3 ], \
    [ 4,     0 ], \
    [ 1,     2 ], \
    [ 3,     1 ], \
    [ 1,     4 ], \
    [ 3,     2 ], \
    [ 2,     4 ], \
    [ 4,     3 ] ] )

  print ( '' )
  print ( 'digraph_arc_is_eulerian_test()' )
  print ( '  digraph_arc_is_eulerian() checks if a digraph' )
  print ( '  has (at least one) Euler circuit.' )

  print ( '' )
  print ( '  The digraph arc list:' )
  pprint.pprint ( L )

  answer = digraph_arc_is_eulerian ( L )

  if ( answer == 0 ):
    print ( '  The digraph is NOT eulerian.' )
  elif ( answer == 1 ):
    print ( '  The digraph has an eulerian path,' )
    print ( '  but not an eulerian circuit.' )
  elif ( answer == 2 ):
    print ( '  The digraph has an eulerian circuit.' )

  return

def digraph_arc_to_adj_test ( ):

#*****************************************************************************80
#
## digraph_arc_to_adj_test() tests digraph_arc_to_adj().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  edge_num = 16
  node_num = 20

  print ( '' )
  print ( 'digraph_arc_to_adj_test():' )
  print ( '  digraph_arc_to_adj() converts an arclist' )
  print ( '  digraph to an adjacency digraph.' )

  L = digraph_arc_example_cycler ( )

  print ( '' )
  print ( '  The digraph arc list:' )
  pprint.pprint ( L )

  A = digraph_arc_to_adj ( L )

  print ( '' )
  print ( '  The digraph adjacency matrix:' )
  pprint.pprint ( A )

  return

def digraph_arc_to_star_test ( ):

#*****************************************************************************80
#
## digraph_arc_to_star_test() tests digraph_arc_to_star().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  edge_num = 16
  node_num = 20

  print ( '' )
  print ( 'digraph_arc_to_star_test():' )
  print ( '  digraph_arc_to_star() converts an arclist' )
  print ( '  digraph to a forward star representation.' )

  L = digraph_arc_example_cycler ( )

  print ( '' )
  print ( '  The digraph arc list:' )
  pprint.pprint ( L )

  arcfir, fwdarc = digraph_arc_to_star ( L )

  print ( '' )
  print ( '  The digraph forward star representation:' )
  print ( '  arcfir():' )
  pprint.pprint ( arcfir )
  print ( '  fwdarc():' )
  pprint.pprint ( fwdarc )

  return

def digraph_arc_to_adj ( L ):

#*****************************************************************************80
#
## digraph_arc_to_adj() converts arc list digraph to an adjacency digraph.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2026
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
#    integer A(node_num,node_num): the adjacency matrix.
#
  import numpy as np

  edge_num = L.shape[0]
  node_num = np.max ( L ) + 1

  A = np.zeros ( [ node_num, node_num ] )

  for edge_id in range ( 0, edge_num ):
    i = L[edge_id,0]
    j = L[edge_id,1]
    A[i,j] = 1

  return A

def digraph_arc_to_star ( L ):

#*****************************************************************************80
#
## digraph_arc_to_star() sets forward star representation of a digraph.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer L(edge_num,2) the I-th edge
#    extends from node L(I,1) to L(I,2).
#
#  Output:
#
#    integer ARCFIR(node_num+1) ARCFIR(I) is the number of
#    the first edge starting at node I in the forward star representation.
#
#    integer FWDARC(edge_num) FWDARC(I) is the ending node of
#    the I-th edge in the forward star representation.
#
  import numpy as np

  edge_num = L.shape[0]
  node_num = np.max ( L ) + 1
#
#  Set up the forward star representation.
#
  arcfir = np.zeros ( node_num + 1 )
  fwdarc = np.zeros ( edge_num )

  k = 0

  for i in range ( 0, node_num ):

    arcfir[i] = k

    for j in range ( 0, edge_num ):

      if ( L[j,0] == i ):
        fwdarc[k] = L[j,1]
        k = k + 1

  arcfir[node_num] = k

  return arcfir, fwdarc

def digraph_arc_weight_print ( L, wnode, title ):

#*****************************************************************************80
#
## digraph_arc_weight_print() prints out a weighted digraph from an edge list.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer L(edge_num,2), the beginning and end nodes of the edges.
#
#    real ( kind = rk8 ) WNODE(edge_num), the weights of the edges.
#
#    character ( len = * ) TITLE, a title.
#
  edge_num = L.shape[0]

  print ( '' )
  print ( title )
  print ( '' )

  for i in range ( 0, edge_num ):
    print ( '%8d    %8d%8d%14.6g' % ( i, L[i,0], L[i,1], wnode[i] ) )

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
  digraph_arc_test ( )
  timestamp ( )

