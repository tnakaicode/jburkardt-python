#! /usr/bin/env python3
#
def graph_adj_test ( ):

#*****************************************************************************80
#
## graph_adj_test() tests graph_adj().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'graph_adj_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test graph_adj().' )

  graph_adj_degree_test ( )
  graph_adj_distance_from_node_test ( )
  graph_adj_edge_count_test ( )
  graph_adj_edge_select_test ( )
  graph_adj_is_eulerian_test ( )
  graph_adj_is_nodewise_connected_test ( )
  graph_adj_random_test ( )
  graph_adj_transitive_closure_test ( )
  graph_adj_walks_test ( )
  matrix_is_adjacency_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'graph_adj_test():' )
  print ( '  Normal end of execution.' )

  return

def graph_adj_degree ( A ):

#*****************************************************************************80
#
## graph_adj_degree() computes the degree of each node.
#
#  Discussion:
#
#    The degree of a node is the number of edges that are incident on it.
#
#    A self edge increases the degree of a node by 2.
#
#    The sum of the degrees of the nodes is twice the number of edges.
#
#    The generalized case, where A(I,J) can be greater than 1, indicating
#    the existence of 2 or more distinct edges between nodes I and J,
#    will be properly handled by this routine.  
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,node_num): the adjacency information.
#
#  Output:
#
#    integer degree(node_num): the degree of the nodes.
#
  import numpy as np

  degree = np.sum ( A + np.transpose ( A ), axis = 1 ) // 2

  return degree

def graph_adj_degree_test ( ):

#*****************************************************************************80
#
## graph_adj_degree_test() tests graph_adj_degree().
#
#  Diagram:
#
#    5--2--10--1--3--6
#           |  |  | /
#           8  |  9
#           |  |  
#           4--7  
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'graph_adj_degree_test():' )
  print ( '  graph_adj_degree() computes the degree of the nodes;' )

  A = np.array ( [ \
    [0,0,1,0,0,0,1,0,0,1 ], \
    [0,0,0,0,1,0,0,0,0,1 ], \
    [1,0,0,0,0,1,0,0,1,0 ], \
    [0,0,0,0,0,0,1,1,0,0 ], \
    [0,1,0,0,0,0,0,0,0,0 ], \
    [0,0,1,0,0,0,0,0,1,0 ], \
    [1,0,0,1,0,0,0,0,0,0 ], \
    [0,0,0,1,0,0,0,0,0,1 ], \
    [0,0,1,0,0,1,0,0,0,0 ], \
    [1,1,0,0,0,0,0,1,0,0 ] \
  ] )
   
  print ( '' )
  print ( '  The graph adjacency matrix:' )
  print ( A )

  degree = graph_adj_degree ( A )

  print ( '' )
  print ( '  The node degrees:' )
  print ( degree )
 
  return

def graph_adj_distance_from_node ( A, node_k ):

#*****************************************************************************80
#
## graph_adj_distance_from_node() computes distance from node to all nodes.
#
#  Discussion:
#
#    The distance is measured by the number of links in the shortest path
#    starting at node k.
#
#    distance(node_k) = 0
#    distance(node_p) = Inf if node p is unreachable from node k.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,node_num): the adjacency information.
#
#    integer node_k: a specific node of the graph.
#
#  Output:
#
#    integer distance(node_num): the distance of each node to node k.
#
  import numpy as np

  node_num = A.shape[0]
#
#  Set up distance.
#
  distance = np.inf * np.ones ( node_num )
  d = 0
  distance[node_k] = d
#
#  NEW holds the nodes we have just reached on this step.
#
  new = [ node_k ]
#
#  As long as we found at least one neighbor at distance D,
#  seek new neighbors at distance D+1.
#
  while ( 0 < len ( new ) ):

    old = new.copy ( )
    new = np.zeros ( 0, dtype = int )
    d = d + 1
#
#  For each node J that we found on the previous step...
#
    for k in range ( 0, len ( old ) ):
      j = old[k]
#
#  ...look for adjacent neighbors I...
#
      for i in range ( 0, node_num ):

        if ( A[i,j] == 1 ):
#
#  ...and if node I hasn't been reached yet:
#  mark that is has been reached,
#  add it to list,
#  and increase the count of nodes we have reached.
#
          if ( distance[i] == np.inf ):
            distance[i] = d
            new = np.append ( new, i )

  return distance

def graph_adj_distance_from_node_test ( ):

#*****************************************************************************80
#
## graph_adj_distance_from_node_test() tests graph_adj_distance_from_node().
#
#  Diagram:
#
#    5--2--10--1--3--6
#           |  |  | /
#           8  |  9
#           |  |  
#           4--7  
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'graph_adj_distance_from_node_test():' )
  print ( '  graph_adj_distance_from_node() computes the distance' )
  print ( '  from one node to all other nodes in a graph;' )

  A = np.array ( [ \
    [0,0,1,0,0,0,1,0,0,1 ], \
    [0,0,0,0,1,0,0,0,0,1 ], \
    [1,0,0,0,0,1,0,0,1,0 ], \
    [0,0,0,0,0,0,1,1,0,0 ], \
    [0,1,0,0,0,0,0,0,0,0 ], \
    [0,0,1,0,0,0,0,0,1,0 ], \
    [1,0,0,1,0,0,0,0,0,0 ], \
    [0,0,0,1,0,0,0,0,0,1 ], \
    [0,0,1,0,0,1,0,0,0,0 ], \
    [1,1,0,0,0,0,0,1,0,0 ] \
  ] )
   
  print ( '' )
  print ( '  The graph adjacency matrix:' )
  print ( A )

  node_k = 6
  distance = graph_adj_distance_from_node ( A, node_k )

  print ( '' )
  print ( '  Distance from node', node_k )
  print ( distance )
 
  return

def graph_adj_edge_count ( A ):

#*****************************************************************************80
#
## graph_adj_edge_count() counts the edges in a graph.
#
#  Discussion:
#
#    Self-edges are allowed.
#
#    The adjacency matrix is assumed to be symmetric, so all edges
#    except self-edges will appear twice.
#
#    The resulting sum must count the self-edges double, and then divide
#    the number of edges counted by 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,node_num): the adjacency information.
#
#  Output:
#
#    integer edge_num: the number of edges in the graph.
#
  import numpy as np

  edge_num = np.sum ( np.sum ( A ) ) + np.sum ( np.diag ( A ) )

  edge_num = edge_num // 2

  return edge_num

def graph_adj_edge_count_test ( ):

#*****************************************************************************80
#
## graph_adj_edge_count_test() tests graph_adj_edge_count().
#
#  Diagram:
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
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'graph_adj_edge_count_test():' )
  print ( '  graph_adj_edge_count() counts edges in a graph.' )

  A = graph_adj_example_bush ( )

  print ( '' )
  print ( '  Adjacency matrix for bush example:' )
  print ( A )

  edge_num = graph_adj_edge_count ( A )

  print ( '' )
  print ( '  Number of edges is', edge_num )

  return

def graph_adj_edge_select ( A ):

#*****************************************************************************80
#
## graph_adj_edge_select() returns one edge from a graph.
#
#  Discussion:
#
#    This function returns the first edge it encounters.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 February 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,node_num): the adjacency matrix for the graph.
#
#  Output:
#
#    integer ni, nj: the endpoints of an edge of the graph.
#    If no edge was found, ni and nj are -1.
#
  node_num = A.shape[0]

  ni = -1
  nj = -1

  for i in range ( 0, node_num ):
    for j in range ( 0, node_num ):
      if ( A[i,j] != 0 ):
        ni = i
        nj = j
        break

  return ni, nj

def graph_adj_edge_select_test ( ):

#*****************************************************************************80
#
## graph_adj_edge_select_test() tests graph_adj_edge_select().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'graph_adj_edge_select_test():' )
  print ( '  graph_adj_edge_select() selects an edge from' )
  print ( '  a graph defined by an adjacency matrix.' )

  A = graph_adj_example_bush ( )

  print ( '' )
  print ( '  Adjacency matrix for bush example' )
  print ( A )

  ni, nj = graph_adj_edge_select ( A )

  print ( '' )
  print ( '  An edge of this graph extends from' )
  print ( '  node', ni, 'to node', nj )

  return

def graph_adj_example_bush ( ):

#*****************************************************************************80
#
## graph_adj_example_bush() defines the bush graph example.
#
#  Diagram:
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
#    28 February 2023
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer A[7,7]: the adjacency information for the graph.  
#
  import numpy as np

  A = np.array ( [ \
   [ 0, 0, 0, 1, 0, 0, 0 ], \
   [ 0, 0, 0, 0, 1, 0, 0 ], \
   [ 0, 0, 0, 0, 1, 0, 0 ], \
   [ 1, 0, 0, 0, 1, 1, 1 ], \
   [ 0, 1, 1, 1, 0, 0, 0 ], \
   [ 0, 0, 0, 1, 0, 0, 0 ], \
   [ 0, 0, 0, 1, 0, 0, 0 ] ] )

  return A

def graph_adj_is_eulerian ( A ):

#*****************************************************************************80
#
## graph_adj_is_eulerian() determines if a graph is Eulerian.
#
#  Discussion:
#
#    An edgewise-connected graph is circuit Eulerian if no node 
#    has odd degree;
#
#    An edgewise-connected graph is path Eulerian if at most two nodes 
#    have odd degree;
#
#    It is allowed for some nodes to have zero degree.  We are only
#    interested in using all the edges, not in visiting all the nodes.
#
#    If a graph is circuit Eulerian, then it is possible to start 
#    from any node and trace an Eulerian circuit, which uses every edge 
#    exactly once, and returns to the starting node.
#
#    If a graph is path Eulerian, then it is possible to start 
#    from a node of odd degree and trace an Eulerian path, which uses 
#    every edge exactly once, and finishes at the other node of odd degree.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,node_num): the adjacency matrix for the graph.
#
#  Output:
#
#    logical circuit_eulerian: true if the graph is circuit Eulerian.
#
#    logical path_eulerian: true if the graph is path Eulerian.
#
  import numpy as np
#
#  Actually, you need EDGEWISE connectivity, not NODEWISE!
#
  connected = graph_adj_is_nodewise_connected_depth ( A )

  if ( not connected ):
    circuit_eulerian = False
    path_eulerian = False
    return circuit_eulerian, path_eulerian

  degree = np.sum ( A + np.transpose ( A ), axis = 1 ) // 2

  odd_degree_count = np.sum ( ( degree % 2 ) == 1 )

  circuit_eulerian = ( odd_degree_count == 0 )

  path_eulerian = ( odd_degree_count <= 2 )

  return circuit_eulerian, path_eulerian

def graph_adj_is_eulerian_test ( ):

#*****************************************************************************80
#
## graph_adj_is_eulerian_test() tests graph_adj_is_eulerian().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'graph_adj_is_eulerian_test( ):' )
  print ( '  graph_adj_is_eulerian() determines whether a graph' )
  print ( '  is eulerian.' )

  A = np.array ( [ \
    [0,0,1,0,0,0,1,0,0,1 ], \
    [0,0,0,0,1,0,0,0,0,1 ], \
    [1,0,0,0,0,1,0,0,1,0 ], \
    [0,0,0,0,0,0,1,1,0,0 ], \
    [0,1,0,0,0,0,0,0,0,0 ], \
    [0,0,1,0,0,0,0,0,1,0 ], \
    [1,0,0,1,0,0,0,0,0,0 ], \
    [0,0,0,1,0,0,0,0,0,1 ], \
    [0,0,1,0,0,1,0,0,0,0 ], \
    [1,1,0,0,0,0,0,1,0,0 ] ] )

  print ( '' )
  print ( '  Matrix A:' )
  print ( A )

  circuit_eulerian, path_eulerian = graph_adj_is_eulerian ( A )
  print ( '  circuit_eulerian = ', circuit_eulerian )
  print ( '  path_eulerian    = ', path_eulerian )

  B = np.array ( [ \
    [0,0,1,0,1,0,1,0,0,1 ], \
    [0,0,0,0,1,0,0,0,0,1 ], \
    [1,0,0,0,0,1,0,0,1,0 ], \
    [0,0,0,0,0,0,1,1,0,0 ], \
    [1,1,0,0,0,0,0,0,0,0 ], \
    [0,0,1,0,0,0,0,0,1,0 ], \
    [1,0,0,1,0,0,0,0,0,0 ], \
    [0,0,0,1,0,0,0,0,0,1 ], \
    [0,0,1,0,0,1,0,0,0,0 ], \
    [1,1,0,0,0,0,0,1,0,0 ] ] )

  print ( '' )
  print ( '  Matrix B:' )
  print ( B )

  circuit_eulerian, path_eulerian = graph_adj_is_eulerian ( B )
  print ( '  circuit_eulerian = ', circuit_eulerian )
  print ( '  path_eulerian    = ', path_eulerian )

  C = np.array ( [ \
    [0,0,1,0,1,0,1,0,0,1 ], \
    [0,0,0,0,1,0,0,0,0,1 ], \
    [1,0,0,0,0,1,0,0,1,1 ], \
    [0,0,0,0,0,0,1,1,0,0 ], \
    [1,1,0,0,0,0,0,0,0,0 ], \
    [0,0,1,0,0,0,0,0,1,0 ], \
    [1,0,0,1,0,0,0,0,0,0 ], \
    [0,0,0,1,0,0,0,0,0,1 ], \
    [0,0,1,0,0,1,0,0,0,0 ], \
    [1,1,1,0,0,0,0,1,0,0 ] ] )

  print ( '' )
  print ( '  Matrix C:' )
  print ( C )

  circuit_eulerian, path_eulerian = graph_adj_is_eulerian ( C )
  print ( '  circuit_eulerian = ', circuit_eulerian )
  print ( '  path_eulerian    = ', path_eulerian )

  return

def graph_adj_is_nodewise_connected_breadth ( A ):

#*****************************************************************************80
#
## graph_adj_is_nodewise_connected_breadth() determines if a graph is nodewise connected.
#
#  Discussion:
#
#    A graph is (nodewise) connected if, from every node, there is a path
#    to any other node.
#
#    This function performs a breadth-first search of the graph.  
#    The nodes of the graph are to be collected into levels.
#    Let node 1 be level 1.
#    Level 2 is the immediate neigbors of level 1 not in any previous level.
#    Level k+1 is the immediate neighbors of level k not in any previous level.
#    If a given level produces no nodes, we stop.
#    If, after stopping, we have encountered all nodes, the graph is connected.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,node_num): the adjacency matrix for the graph.
#
#  Output:
#
#    logical connected: is true if the graph is connected.
#
  import numpy as np

  value = matrix_is_adjacency ( A )

  if ( not value ):
    print ( '' )
    print ( 'graph_adj_is_nodewise_connected_breadth(): Fatal error!' )
    print ( '  The input is not a legal adjacency matrix.' )
    raise Exception ( 'graph_adj_is_nodewise_connected_breadth(): Fatal error!' )

  node_num = A.shape[0]
#
#  visited(i) is 1 if node I has been reached.
#  roster(i) contains a list of the nodes as they are reached.
#
  roster = np.zeros ( node_num, dtype = int )
  visited = np.zeros ( node_num, dtype = bool )
#
#  Start at node 1.
#
  visited[0] = True
  roster[0] = 0
  ilo = 0
  ihi = 0
#
#  From the batch of nodes found last time, roster(ilo:ihi),
#  look for unfound neighbors, and store their indices in roster(jlo:jhi).
#
  while ( True ):

    jlo = ihi + 1
    jhi = ihi
#
#  Consider all nodes found on previous pass.
#
    for ii in range ( ilo, ihi + 1 ):

      i = roster[ii]
#
#  For each new node I, consider its J-th neighbor.
#
      for j in range ( 0, node_num ):

        if ( not ( A[i,j] == 0 ) ):

          if ( not visited[j] ):
            jhi = jhi + 1
            roster[jhi] = j
            visited[j] = True
#
#  If no neighbors were found on this pass, our search is complete.
#  The graph is connected if we encountered every node.
#
    if ( jhi < jlo ):
      connected = ( ihi == node_num - 1 )
      break
#
#  If neighbors were found, repeat the loop.
#
    ilo = jlo
    ihi = jhi

  return connected

def graph_adj_is_nodewise_connected_depth ( A ):

#*****************************************************************************80
#
## graph_adj_is_nodewise_connected_depth() determines if a graph is nodewise connected.
#
#  Discussion:
#
#    A graph is (nodewise) connected if, from every node, there is a path
#    to any other node.
#
#    This function performs a depth-first search of the graph.  
#    Add node 1 to the stack.
#    Repeat the following steps:
#      If the stack is empty, then if we have visited every node, the graph is connected.
#      The current node is defined as the last item on the stack.
#      Delete the last item on the stack.
#      Add all unvisited neighbor nodes of the current node to the stack.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,node_num), the adjacency matrix for the graph.
#
#  Output:
#
#    logical connected: is true if the graph is connected.
#
  import numpy as np

  value = matrix_is_adjacency ( A )
  if ( not value ):
    print ( '\n' );
    print ( 'graph_adj_is_nodewise_connected_depth(): Fatal error!\n' );
    print ( '  The input is not a legal adjacency matrix.\n' );  
    raise Exception ( 'graph_adj_is_nodewise_connected_depth(): Fatal error!\n' );

  node_num = A.shape[0]

  visited = np.zeros ( node_num, dtype = bool)
  stack = np.zeros ( node_num, dtype = int )

  step = 0
  stack_num = 0
  stack[stack_num] = 0

  while ( True ):
#
#  Seek a node on the stack that has not been visited.
#
    while ( True ):

      if ( stack_num == -1 ):
        connected = ( step == node_num )
        return connected

      node = stack[stack_num]
      stack_num = stack_num - 1
      if ( not visited[node] ):
        break
#
#  "Visit" the node.
#
    step = step + 1
    visited[node] = step
#
#  Stack each node j that is an immediate neighbor and unvisited.
#
    for j in range ( 0, node_num ):
      if ( A[node,j] == 1 and not visited[j] ):
        stack_num = stack_num + 1
        stack[stack_num] = j

def graph_adj_is_nodewise_connected_walks ( A ):

#*****************************************************************************80
#
## graph_adj_is_nodewise_connected_walks() determines if a graph is nodewise connected.
#
#  Discussion:
#
#    The function computes W(I,J), the number of walks of any length between
#    0 and node_num - 1, from any node i to any node j.
#
#    If any W(I,J) is zero, the graph is not nodewise connected.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  value = matrix_is_adjacency ( A )

  if ( not value ):
    print ( '' )
    print ( 'graph_adj_is_nodewise_connected_walks(): Fatal error!' )
    print ( '  The input is not a legal adjacency matrix.' )
    raise Exception ( 'graph_adj_is_nodewise_connected_walks(): Fatal error!' )
#
#  Compute the walks.
#
  W = graph_adj_walks ( A )
  connected = np.all ( np.all ( W != 0 ) )

  return connected

def graph_adj_is_nodewise_connected_test ( ):

#*****************************************************************************80
#
## graph_adj_is_nodewise_connected_test() tests graph_adj_is_nodewise_connected().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'graph_adj_is_nodewise_connected_test( ):' )
  print ( '  A graph is to be checked for nodewise connectedness.' )
  print ( '  graph_adj_is_nodewise_connected_breadth() uses breadth-first search.' )
  print ( '  graph_adj_is_nodewise_connected_depth() uses depth-first search.' )
  print ( '  graph_adj_is_nodewise_connected_walks() counts the walks from node to node.' )

  A = np.array ( [ \
    [ 0, 1, 0, 1, 0, 0, 0, 0, 0 ], \
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 1, 0, 0, 1 ], \
    [ 1, 0, 0, 0, 1, 0, 1, 0, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 1, 0 ], \
    [ 0, 0, 1, 0, 0, 0, 0, 0, 1 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 1, 0 ], \
    [ 0, 0, 0, 0, 1, 0, 1, 0, 0 ], \
    [ 0, 0, 1, 0, 0, 1, 0, 0, 0 ] ] )

  acb = graph_adj_is_nodewise_connected_breadth ( A )
  acd = graph_adj_is_nodewise_connected_depth ( A )
  acw = graph_adj_is_nodewise_connected_walks ( A )

  print ( '' )
  print ( '  Results for graph A (not connected!)')
  print ( '    breadth: ', acb )
  print ( '    depth:   ', acd )
  print ( '    walks:   ', acw )

  B = np.array ( [ \
    [ 0, 1, 0, 1, 0, 0, 0, 0, 0 ], \
    [ 1, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 0, 0, 0, 1 ], \
    [ 1, 0, 0, 0, 1, 0, 1, 0, 0 ], \
    [ 0, 0, 0, 1, 0, 1, 0, 1, 0 ], \
    [ 0, 0, 0, 0, 1, 0, 0, 0, 1 ], \
    [ 0, 0, 0, 1, 0, 0, 0, 1, 0 ], \
    [ 0, 0, 0, 0, 1, 0, 1, 0, 0 ], \
    [ 0, 0, 1, 0, 0, 1, 0, 0, 0 ] ] )

  bcb = graph_adj_is_nodewise_connected_breadth ( B )
  bcd = graph_adj_is_nodewise_connected_depth ( B )
  bcw = graph_adj_is_nodewise_connected_walks ( B )

  print ( '' );
  print ( '  Results for graph B (connected!)')
  print ( '    breadth: ', bcb )
  print ( '    depth:   ', bcd )
  print ( '    walks:   ', bcw )

  return

def graph_adj_random ( node_num, prob ):

#*****************************************************************************80
#
## graph_adj_random() generates a random graph on a given number of nodes.
#
#  Discussion:
#
#    The user specifies the probability P that an edge will be generated
#    between any pair of nodes.
#
#    ADJ(I,J) is nonzero if there is an edge from node I to node J.  
#    ADJ(I,I) will always be 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer node_num: the number of nodes.
#
#    real prob: the probability that an edge will
#    be generated between any given pair of nodes.
#
#  Output:
#
#    integer A(node_num,node_num): the adjacency matrix.  
#
  import numpy as np

  if ( prob < 0.0 or 1.0 < prob ):
    print ( '' )
    print ( 'graph_adj_random(): Fatal error!' )
    print ( '  Input probability PROB is not between 0 and 1.' )
    raise Exception ( 'graph_adj_random(): Fatal error!' )

  P = np.random.rand ( node_num, node_num )
  P = np.tril ( P )
  P = ( P + np.transpose ( P ) )

  A = np.zeros ( [ node_num, node_num ], dtype = int )
  one = ( P <= prob )
  A[one] = 1

  return A

def graph_adj_random_test ( ):

#*****************************************************************************80
#
## graph_adj_random_test() tests graph_adj_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'graph_adj_random_test():' )
  print ( '  graph_adj_random() returns a random graph, for which the' )
  print ( '  probability of an edge between nodes I and J is PROB.' )

  node_num = 100
  graph_id = 0

  for prob in [ 0.25, 0.50, 0.75 ]:
    graph_id = graph_id + 1
    A = graph_adj_random ( node_num, prob )
    edge_num = graph_adj_edge_count ( A )
    edge_max = ( node_num * ( node_num - 1 ) ) // 2
    print ( '' )
    print ( '  Random graph #', graph_id )
    print ( '  node_num    = ', node_num )
    print ( '  edge_num    = ', edge_num )
    print ( '  edge_max    = ', edge_max )
    print ( '  ratio       = ', edge_num / edge_max )
    print ( '  prob        = ', prob )

  return

def graph_adj_transitive_closure ( A ):

#*****************************************************************************80
#
## graph_adj_transitive_closure() generates the transitive closure of a graph.
#
#  Discussion:
#
#    The method is due to Stephen Warshall.
#
#    The transitive closure of a graph is a function REACH(I,J) so that
#
#      REACH(I,J) = 0 if node J cannot be reached from node I;
#                   1 if node J can be reached from node I.
#
#    This is an extension of the idea of adjacency.  REACH(I,J)=1 if
#    node J is adjacent to node I, or if node J is adjacent to a node
#    that is adjacent to node I, etc.
#
#    Note that if a graph is (node) connected, then its transitive closure
#    is the matrix that is 1 everywhere.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Sedgewick,
#    Algorithms,
#    Addison Wesley, 1983, page 425.
#
#  Input:
#
#    integer A(node_num,node_num): the adjacency for the graph.
#
#  Output:
#
#    integer C(node_num,node_num): the adjacency for the transitive closure.
#
  node_num = A.shape[0]

  C = A.copy ( )

  for i in range ( 0, node_num ):
    C[i,i] = 1

  for i in range ( 0, node_num ):
    for j in range ( 0, node_num ):
      if ( C[j,i] != 0 or C[i,j] != 0 ):
        for k in range ( 0, node_num ):
          if ( C[i,k] != 0 or C[k,i] != 0 ):
            C[j,k] = 1
            C[k,j] = 1

  return C

def graph_adj_transitive_closure_test ( ):

#*****************************************************************************80
#
## graph_adj_transitive_closure_test() tests graph_adj_transitive_closure().
#
#  Diagram:
#
#    1--5      2
#    | /|
#    |/ |      8--3--7
#    4  6
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  node_num = 8

  A = np.array ( [ \
    [1,0,0,1,1,0,0,0], \
    [0,1,0,0,0,0,0,0], \
    [0,0,1,0,0,0,1,1], \
    [1,0,0,1,1,0,0,0], \
    [1,0,0,1,1,1,0,0], \
    [0,0,0,0,1,1,0,0], \
    [0,0,1,0,0,0,1,0], \
    [0,0,1,0,0,0,0,1] ] )

  print ( '' )
  print ( 'graph_adj_transitive_closure_test():' )
  print ( '  graph_adj_transitive_closure() finds the transitive' )
  print ( '  closure of a graph;' )

  print ( '' )
  print ( '  Adjacency matrix A:' )
  print ( A )

  C = graph_adj_transitive_closure ( A )

  print ( '' )
  print ( '  Adjacency for transitive closure:' )
  print ( C )

  return

def graph_adj_walks ( A ):

#*****************************************************************************80
#
## graph_adj_walks() counts the walks between any pair of nodes.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(node_num,node_num): the adjacency matrix for the graph.
#
#  Output:
#
#    integer W(node_num,node_num): the number of walks between each pair of nodes.
#
  import numpy as np

  value = matrix_is_adjacency ( A )

  if ( not value ):
    print ( '' )
    print ( 'graph_adj_walks(): Fatal error!' )
    print ( '  The input is not a legal adjacency matrix.' )  
    raise Exception ( 'graph_adj_walks(): Fatal error!' )

  node_num = A.shape[0]

  for k in range ( 0, node_num ):
    if ( k == 0 ):
      Ak = np.eye ( node_num )
      W = Ak.copy ( )
    else:
      Ak = np.dot ( Ak, A )
      W = W + Ak

  return W

def graph_adj_walks_test ( ):

#*****************************************************************************80
#
## graph_adj_walks_test() tests graph_adj_walks().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'graph_adj_walks_test( ):' )
  print ( '  Count the walks from node I to node J of any length.' )

  A = np.array ( [ \
    [0, 1, 0, 1, 0, 0, 0, 0, 0 ], \
    [1, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [0, 0, 0, 0, 0, 1, 0, 0, 1 ], \
    [1, 0, 0, 0, 1, 0, 1, 0, 0 ], \
    [0, 0, 0, 1, 0, 0, 0, 1, 0 ], \
    [0, 0, 1, 0, 0, 0, 0, 0, 1 ], \
    [0, 0, 0, 1, 0, 0, 0, 1, 0 ], \
    [0, 0, 0, 0, 1, 0, 1, 0, 0 ], \
    [0, 0, 1, 0, 0, 1, 0, 0, 0 ] ] )

  WA = graph_adj_walks ( A )

  print ( '' )
  print ( '  Walks for graph A:' )
  print ( WA )

  B = np.array ( [ \
    [0, 1, 0, 1, 0, 0, 0, 0, 0 ], \
    [1, 0, 0, 0, 0, 0, 0, 0, 0 ], \
    [0, 0, 0, 0, 0, 0, 0, 0, 1 ], \
    [1, 0, 0, 0, 1, 0, 1, 0, 0 ], \
    [0, 0, 0, 1, 0, 1, 0, 1, 0 ], \
    [0, 0, 0, 0, 1, 0, 0, 0, 1 ], \
    [0, 0, 0, 1, 0, 0, 0, 1, 0 ], \
    [0, 0, 0, 0, 1, 0, 1, 0, 0 ], \
    [0, 0, 1, 0, 0, 1, 0, 0, 0 ] ] )

  print ( '' )
  print ( '  Graph B:' )
  print ( B )

  WB = graph_adj_walks ( B )

  print ( '' )
  print ( '  Walks for graph B:' )
  print ( WB )

  return

def matrix_is_adjacency ( A ):

#*****************************************************************************80
#
## matrix_is_adjacency() checks whether a matrix is an adjacency matrix.
#
#  Discussion:
#
#    This function requires that:
#      A is 2-dimensional
#      A is square
#      A is symmetric
#      A has a zero diagonal
#      A only involves entries of 0 or 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A[*,*], the matrix.
#
#  Output:
#
#    logical VALUE: TRUE if A is an adjacency matrix.
#
  import numpy as np

  if ( A.ndim != 2 ):
    value = False
    return value

  m, n = A.shape
  if ( m != n ):
    value = False
    return value

  if ( np.any ( np.any ( A != np.transpose ( A ) ) ) ):
    value = False
    return value

  if ( any ( np.diag ( A ) != 0 ) ):
    value = False
    return value

  if ( np.any ( ( A != 0 ) & ( A != 1 ) ) ):
    value = False
    return value

  value = True

  return value

def matrix_is_adjacency_test ( ):

#*****************************************************************************80
#
## matrix_is_adjacency_test() tests matrix_is_adjacency().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 March 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'matrix_is_adjacency_test( ):' )
  print ( '  matrix_is_adjacency() requires that a matrix A be:' )
  print ( '  * square' )
  print ( '  * symmetric' )
  print ( '  * zero on the diagonal' )
  print ( '  * only have 0 or 1 as values.' )

  A = np.array ( [ \
    [0, 0, 1 ], \
    [0, 0, 1 ], \
    [1, 1, 0 ], \
    [0, 0, 1 ] ] )

  print ( '' )
  print ( '  Matrix A:' )
  print ( A )
  value = matrix_is_adjacency ( A )
  print ( '  matrix_is_adjacency(A) = ', value )

  B = np.array ( [ \
    [0, 0, 1 ], \
    [1, 0, 1 ], \
    [1, 1, 0 ] ] )

  print ( '' )
  print ( '  Matrix B:' )
  print ( B )
  value = matrix_is_adjacency ( B )
  print ( '  matrix_is_adjacency(B) = ', value )

  C = np.array ( [ \
    [1, 0, 1 ], \
    [0, 1, 1 ], \
    [1, 1, 1 ] ] )

  print ( '' )
  print ( '  Matrix C:' )
  print ( C )
  value = matrix_is_adjacency ( C )
  print ( '  matrix_is_adjacency(C) = ', value )

  D = np.array ( [ \
    [0, 1, 2 ], \
    [1, 0, 1 ], \
    [2, 1, 0 ] ] )

  print ( '' )
  print ( '  Matrix D:' )
  print ( D )
  value = matrix_is_adjacency ( D )
  print ( '  matrix_is_adjacency(D) = ', value )

  E = np.array ( [ \
    [0, 1, 1 ], \
    [1, 0, 1 ], \
    [1, 1, 0 ] ] )

  print ( '' )
  print ( '  Matrix E:' )
  print ( E )
  value = matrix_is_adjacency ( E )
  print ( '  matrix_is_adjacency(E) = ', value )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == "__main__" ):
  timestamp ( )
  graph_adj_test ( )
  timestamp ( )

