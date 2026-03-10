#! /usr/bin/env python3
#
def graph_class_test ( ):

#*****************************************************************************80
#
## graph_class_test() tests graph_class().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'graph_class_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test graph_class()' )

  shortest_path_test ( 'Boston', 'Chicago' )
#
#  Terminate.
#
  print ( '' )
  print ( 'graph_class_test():' )
  print ( '  Normal end of execution.' )

  return

def buildCityGraph ( graphType ):

#*****************************************************************************80
#
## buildCityGraph() creates an example graph.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2023
#
#  Author:
#
#    John Burkardt
#
  g = graphType ( )

  for name in ( 'Boston', 'Providence', 'New York', 'Chicago',
    'Denver', 'Phoenix', 'Los Angeles' ):
    g.addNode ( Node(name) )

  g.addEdge ( Edge ( g.getNode('Boston'),      g.getNode('Providence') ) )
  g.addEdge ( Edge ( g.getNode('Boston'),      g.getNode('New York') ) )
  g.addEdge ( Edge ( g.getNode('Providence'),  g.getNode('Boston') ) )
  g.addEdge ( Edge ( g.getNode('Providence'),  g.getNode('New York') ) )
  g.addEdge ( Edge ( g.getNode('New York'),    g.getNode('Chicago') ) )
  g.addEdge ( Edge ( g.getNode('Chicago'),     g.getNode('Denver') ) )
  g.addEdge ( Edge ( g.getNode('Chicago'),     g.getNode('Phoenix') ) )
  g.addEdge ( Edge ( g.getNode('Denver'),      g.getNode('Phoenix') ) )
  g.addEdge ( Edge ( g.getNode('Denver'),      g.getNode('New York') ) )
  g.addEdge ( Edge ( g.getNode('Los Angeles'), g.getNode('Boston') ) )
  return g

def BFS ( graph, start, end, toPrint = False ):

#*****************************************************************************80
#
## BFS() implements a breadth-first search of a graph.
#
#  Discussion:
#
#    Explore all paths using n hops before exploring 
#    any path with n+1 hops.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2023
#
#  Author:
#
#    John Burkardt
#
  initPath = [ start ]
  pathQueue = [ initPath ]
  while len ( pathQueue ) != 0:
    tmpPath = pathQueu.pop ( 0 )
    if toPrint:
      print ( 'Current BFS path:' )
      path_print ( tmpPath )
    lastNode = tmpPath[-1]
    if lastNode == end:
      return tmpPath
    for nextNode in graph.childrenOf ( lastNode ):
      if nextNode not in tmpPath:
        newPath = tmpPath + [ nextNode ]
        pathQueue.append ( newPath )
  return None

def DFS ( graph, start, end, path, shortest, toPrint = False ):

#*****************************************************************************80
#
## DFS() implements a depth-first search of a graph.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2023
#
#  Author:
#
#    John Burkardt
#
  path = path + [ start ]

  if toPrint:
    path_print ( path )

  if start == end:
    return path
  for node in graph.childrenOf ( start ):
    if node not in path:
      if shortest == None or len ( path ) < len ( shortest ):
        newPath = DFS ( graph, node, end, path, shortest, toPrint )
        if newPath != None:
          shortest = newPath
    elif toPrint:
      print ( 'Already visited', node )
  return shortest

def shortest_path ( graph, source, destination, toPrint = False ):

#*****************************************************************************80
#
## shortest_path() seeks the shortest path from one node to another.
#
#  Discussion:
#
#    All edges have length one.  The shortest path is the path involving
#    the fewest number of edges.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    graph: the graph.
#
#    source: the starting node.
#
#    destination: the final node.
#
#    toPrint: True if the depth first search should print out its progress.
#
#  Output:
#
#    path: the shortest path.
#
  path = DFS ( graph, source, destination, [], None, toPrint )

  return path

class Digraph ( object ):

#*****************************************************************************80
#
## Digraph() defines the directed graph class.
#
  def __init__( self ):
    self.edges = {}
  def addNode ( self, node ):
    if node in self.edges:
      raise ValueError ( 'Duplicate node' )
    else:
      self.edges[node] = []
  def addEdge ( self, edge ):
    src = edge.getSource ( )
    dest = edge.getDestination ( )
    if not ( src in self.edges and dest in self.edges ):
      raise ValueError ( 'Node not in graph' )
    self.edges[src].append ( dest )
  def childrenOf ( self, node ):
    return self.edges[node]
  def hasNode ( self, node ):
    return node in self.edges
  def getNode ( self, name ):
    for n in self.edges:
      if n.getName() == name:
        return n
    raise NameError ( name )
  def __str__ ( self ):
    result = ''
    for src in self.edges:
      for dest in self.edges[src]:
        result = result + src.getName() + '->' + dest.getName() + '\n'
#
#  Omit final newline.
#
    return result[:-1] 

class Edge ( object ):

#*****************************************************************************80
#
## Edge()...
#
  def __init__ ( self, src, dest ):
    self.src = src
    self.dest = dest
  def getSource ( self ):
    return self.src
  def getDestination ( self ):
    return self.dest
  def __str__ ( self ):
    return self.src.getname() + '->' + self.dest.getname()

class Graph ( object ):

#*****************************************************************************80
#
## Graph() defines the undirected graph class.
#
  def addEdge ( self, edge ):
    Digraph.addEdge ( self, edge )
    rev = Edge ( edge.getDestination(), edge.getSource() )
    Digraph.addEdge ( self, rev )

class Node ( object ):

#*****************************************************************************80
#
## Node() defines the node class.
#
  def __init__ ( self, name ):
    self.name = name
  def getName ( self ):
    return self.name
  def __str__ ( self ):
    return self.name

def shortest_path_test ( source, destination ):

#*****************************************************************************80
#
## shortest_path_test() tests shortest_path().
#
#  Discussion:
#
#    All edges have length one.  The shortest path is the path involving
#    the fewest number of edges.
#
#    The shortest path is printed out.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    source: the starting node.
#
#    destination: the final node.
#
  print ( '' )
  print ( 'shortest_path_test():' )
  print ( '  Find shortest path from', source, 'to', destination )

  g = buildCityGraph ( Digraph )

  path = shortest_path ( g, g.getNode(source), g.getNode(destination), toPrint = False )

  if ( not path ):
    print ( '  There is no path from', source, 'to', destination )
  else:
    print ( '' )
    path_print ( path )

  return

def path_print ( path ):

#*****************************************************************************80
#
## path_print prints a path.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    path: a path
#
  path_len = len ( path )

  for i in range ( 0, path_len - 1 ):
    print ( '  ', path[i], '-->', path[i+1] )

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

if ( __name__ == "__main__" ):
  timestamp ( )
  graph_class_test ( )
  timestamp ( )

