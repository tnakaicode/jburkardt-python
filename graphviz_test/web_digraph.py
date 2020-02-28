#! /usr/bin/env python3
#
def web_digraph ( ):

#*****************************************************************************80
#
## web_digraph plots a web of connections as a directed graph.
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
#    01 May 2019
#
#  Author:
#
#    John Burkardt
#
  from graphviz import Digraph
  import platform

  print ( '' )
  print ( 'web_digraph:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot a web of connections as a directed graph.' )
  print ( '' )

  dot = Digraph ( comment = 'A network', format = 'png' )
#
#  Specify the nodes, giving each an internal code, and a label.
#
  dot.node ( '1', 'Alpha' )
  dot.node ( '2', 'Beta' )
  dot.node ( '3', 'Gamma' )
  dot.node ( '4', 'Delta' )
  dot.node ( '5', 'Epsilon' )
  dot.node ( '6', 'Zeta' )
#
#  Specify the edges as connections between two nodes.
#
  dot.edge ( '1', '5', '0.1' )
  dot.edge ( '1', '6', '0.9' )

  dot.edge ( '2', '1', '0.3' )
  dot.edge ( '2', '3', '0.4' )
  dot.edge ( '2', '4', '0.3' )

  dot.edge ( '3', '4', '0.6' )
  dot.edge ( '3', '5', '0.4' )

  dot.edge ( '4', '5', '1.0' )

  dot.edge ( '5', '1', '0.2' )
  dot.edge ( '5', '6', '0.8' )

  dot.edge ( '6', '4', '1.0' )

  print ( dot.source )
#
#  Save graph to a file, and display an image to the screen.
#
  dot.render ( 'web_digraph.dot', view = True )

  filename = 'web_digraph.dot.png'
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'web_digraph:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  web_digraph ( )
  timestamp ( )

