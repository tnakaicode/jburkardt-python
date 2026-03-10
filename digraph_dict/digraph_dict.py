#! /usr/bin/env python3
#
def digraph_dict_test ( ):

#*****************************************************************************80
#
## digraph_dict_test() tests digraph_dict().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 April 2023
#
#  Author:
#
#    Original code by Bernd Klein,
#    Modifications by John Burkardt
#
#  Reference:
#
#    Bernd Klein,
#    Graph Theory and Graphs in Python,
#    https://python-course.eu/applications-python/graphs-python.php
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'digraph_dict_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Some simple functions for a directed graph ("digraph")' )
  print ( '  defined using a Python dictionary:' )
  print ( '  digraph = { from0: [ to0, to1, ... tok], from1:[], ...}' )

  digraph = digraph_dict_example1 ( )
  print ( '' )
  print ( '  The digraph:' )
  print ( digraph )

  nodes = digraph_dict_nodes_all ( digraph )
  print ( '' )
  print ( '  The nodes:' )
  print ( nodes )

  edges = digraph_dict_edges_all ( digraph )
  print ( '' )
  print ( '  The edges:' )
  print ( edges )

  digraph_dict_plot ( digraph )

  isolated = digraph_dict_find_isolated_nodes ( digraph )
  print ( '' )
  print ( '  The isolated nodes:' )
  print ( isolated )

  print ( '' )
  print ( '  Add node "c":' )
  digraph = digraph_dict_add_node ( digraph, 'c' )
  print ( '  Add node "h":' )
  digraph = digraph_dict_add_node ( digraph, 'h' )
  print ( '  Updated node list:' )
  nodes = digraph_dict_nodes_all ( digraph )
  print ( nodes )

  print ( '' )
  print ( '  Add edge "a->f":' )
  digraph = digraph_dict_add_edge ( digraph, [ 'a', 'f' ] )
  edges = digraph_dict_edges_all ( digraph )
  print ( '  Updated edge list.' )
  print ( edges )

  print ( '' )
  print ( '  List all edges from node "c":' )
  edges = digraph_dict_edges_node_from ( digraph, 'c' )
  print ( edges )
#
#  "reach"
#
  print ( '' )
  print ( '  What nodes can we reach from "e"?' )
  reach = digraph_dict_reach_node ( digraph, 'e' )
  print ( reach )
  print ( '' )
  print ( '  What nodes can we reach from "f"?' )
  reach = digraph_dict_reach_node ( digraph, 'f' )
  print ( reach )

  print ( '' )
  print ( '  List all edges to node "c":' )
  edges = digraph_dict_edges_node_to ( digraph, 'c' )
  print ( edges )
#
#  Path from one node to another.
#
  print ( '' )
  print ( '  Seek path from "a" to "d"' )
  path = digraph_dict_path_find ( digraph, "a", "d" )
  print ( path )
#
#  Shortest path from one node to another.
#
  print ( '' )
  print ( '  Seek shortest path from "a" to "d"' )
  path = digraph_dict_shortest_path ( digraph, "a", "d" )
  print ( path )
#
#  Terminate.
#
  print ( '' )
  print ( 'digraph_dict_test():' )
  print ( '  Normal end of execution.' )

  return

def digraph_dict_add_edge ( digraph, e ):
  n0 = e[0]
  n1 = e[1]
  if ( n0 in digraph ):
    digraph[n0].append ( n1 )
  else:
    digraph[n0] = [ n1 ]
  return digraph

def digraph_dict_add_node ( digraph, n ):
  if ( n not in digraph ):
    digraph[n] = []
  else:
    print ( 'Node', n, 'is already in the digraph.' )
  return digraph

def digraph_dict_edges_all ( digraph ):
  edges = []
  for node in digraph.keys ( ):
    for dest in digraph[node]:
      edges.append ( [ node, dest ] )
  return edges

def digraph_dict_edges_node_from ( digraph, node ):
  edges = []
  if ( node in digraph.keys ( ) ):
    for dest in digraph[node]:
      edges.append ( [ node, dest ] )
  else:
    print ( node, 'is not a node of this digraph!' )
  return edges

def digraph_dict_edges_node_to ( digraph, node ):
  edges = []
  for src in digraph.keys ( ):
    if ( node in digraph[src] ):
      edges.append ( [ src, node ] )
  return edges

def digraph_dict_example1 ( ):
  digraph = { 
    "a" : [ "c", "e" ],
    "b" : [ "d" ],
    "c" : [ "b", "e" ], 
    "d" : [ "a" ], 
    "e" : [ "d" ], 
    "f" : [ ]
   }
  return digraph

def digraph_dict_find_isolated_nodes ( digraph ):
  isolated = list()
  for node in digraph:
    if ( not digraph[node] ):
      isolated.append ( node )
  return isolated

def digraph_dict_nodes_all ( digraph ):
  nodes = list ( digraph.keys ( ) )
  return nodes

def digraph_dict_path_find ( digraph, start_node, end_node, path = None ):
#  digraph_dict_path_find() seeks a path from start_node to end_node.
#
#  Discussion:
#
#    If a path is found, it is not necessarily the shortest path.
#
  if ( path == None ):
    path = []
  path = path + [ start_node ]
  if ( start_node == end_node ):
    return path
  if ( start_node not in digraph ):
    return None
  for node in digraph[start_node]:
    if ( node not in path ):
      extended_path = digraph_dict_path_find ( digraph, node, end_node, path )
      if ( extended_path ):
        return extended_path
  return None

def digraph_dict_plot ( digraph ):
  from graphviz import Digraph
  edges = digraph_dict_edges_all ( digraph )
  nodes = digraph_dict_nodes_all ( digraph )
  dot = Digraph ( format = 'png' )
  for n in nodes:
    dot.node ( n )
  for e in edges:
    dot.edge ( e[0], e[1] )
  dot.render ( 'digraph.dot', view = False )
  filename = 'digraph.dot.png'
  print ( '  Graphics saved as "%s"' % ( filename ) )
  return

def digraph_dict_reach_node ( G, node ):
#
## digraph_dict_reach_node() returns the nodes reachable from a given node.
#
  reach = [ node ]
  more = True
  while ( more ):
    more = False
    for n in reach:
      for dest in G[n]:
        if ( not dest in reach ):
          reach = reach + [ dest ]
          more = True
  return reach

def digraph_dict_shortest_path ( graph, node1, node2 ):
  path_list = [[node1]]
  path_index = 0
  # This set keeps track of previously visited nodes
  previous_nodes = {node1}
  if node1 == node2:
    return path_list[0]
  while path_index < len(path_list):
    current_path = path_list[path_index]
    last_node = current_path[-1]
    next_nodes = graph[last_node]
    # Search goal node
    if node2 in next_nodes:
      current_path.append(node2)
      return current_path
    # Add new paths
    for next_node in next_nodes:
      if not next_node in previous_nodes:
        new_path = current_path[:]
        new_path.append(next_node)
        path_list.append(new_path)
        # To avoid backtracking
        previous_nodes.add(next_node)
    # Continue to next path in list
    path_index += 1
  # No path was found
  return []

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

if ( __name__ == "__main__" ):
  timestamp ( )
  digraph_dict_test ( )
  timestamp ( )

