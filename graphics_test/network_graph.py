#! /usr/bin/env python3
#
def network_graph ( ):

#*****************************************************************************80
#
## network_graph plots a network as an undirected graph.
#
#  Discussion:
#
#    To use this example, you need to have installed graphviz and pydotplus.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 April 2019
#
#  Author:
#
#    John Burkardt
#
  from graphviz import Graph
  import platform

  print ( '' )
  print ( 'network_graph:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot a graph, of nodes connected by edges.' )
  print ( '' )

  dot = Graph ( comment = 'A network', format = 'png' )
#
#  Specify the nodes, giving each an internal code, and a label.
#
  dot.node ( '1', 'A' )
  dot.node ( '2', 'B' )
  dot.node ( '3', 'C' )
  dot.node ( '4', 'D' )
  dot.node ( '5', 'E' )
  dot.node ( '6', 'F' )
  dot.node ( '7', 'G' )
  dot.node ( '8', 'H' )
  dot.node ( '9', 'I' )
  dot.node ( '10', 'J' )
  dot.node ( '11', 'K' )
#
#  Specify the edges as connections between two nodes.
#
  dot.edge ( '1', '1' )
  dot.edge ( '1', '2' )
  dot.edge ( '1', '3' )
  dot.edge ( '2', '4' )
  dot.edge ( '2', '5' )
  dot.edge ( '3', '4' )
  dot.edge ( '4', '5' )
  dot.edge ( '4', '6' )
  dot.edge ( '5', '6' )
  dot.edge ( '5', '7' )
  dot.edge ( '5', '8' )
  dot.edge ( '6', '7' )
  dot.edge ( '7', '8' )
  dot.edge ( '8', '9' )
  dot.edge ( '9', '10' )
  dot.edge ( '9', '11' )
  dot.edge ( '10', '11' )

  print ( dot.source )
#
#  Save graph to a file, and optionally display an image to the screen.
#
  dot.render ( 'network_graph.dot', view = False )

  filename = 'network_graph.dot.png'
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'network_graph:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  network_graph ( )
  timestamp ( )

