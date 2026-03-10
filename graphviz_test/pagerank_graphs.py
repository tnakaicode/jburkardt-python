#! /usr/bin/env python3
#
def pagerank_graphs ( ):

#*****************************************************************************80
#
## pagerank_graphs() makes some plots for a discussion of PageRank.
#
#  Discussion:
#
#    To use this example, you need to have installed graphviz and pydotplus.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'pagerank_graphs():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Plot a web of connections as a directed graph.' )
  print ( '' )

  dot = Digraph ( comment = 'pagerank_plot1', format = 'png' )
#
#  Specify the nodes, giving each an internal code, and a label.
#
  dot.node ( '0', '0' )
  dot.node ( '1', '1' )
  dot.node ( '2', '2' )
  dot.node ( '3', '3' )
  dot.node ( '4', '4' )
  dot.node ( '5', '5' )
  dot.node ( '6', '6' )
#
#  Specify the edges as connections between two nodes.
#
  dot.edge ( '0', '1' )
  dot.edge ( '0', '5' )

  dot.edge ( '1', '2' )

  dot.edge ( '2', '0' )
  dot.edge ( '2', '3' )

  dot.edge ( '3', '0' )

  dot.edge ( '4', '2' )

  print ( dot.source )
#
#  Save graph to a file, and display an image to the screen.
#
  dot.render ( 'pagerank_plot1.dot', view = True )

  filename = 'pagerank_plot1.dot.png'
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  PLOT #2
#
  dot = Digraph ( comment = 'pagerank_plot2', format = 'png' )
#
#  Specify the nodes, giving each an internal code, and a label.
#
  dot.node ( '0', '0' )
  dot.node ( '1', '1' )
  dot.node ( '2', '2' )
  dot.node ( '3', '3' )
  dot.node ( '4', '4' )
  dot.node ( '5', '5' )
  dot.node ( '6', '6' )
#
#  Specify the edges as connections between two nodes.
#
  dot.edge ( '0', '1', '0.5', fontcolor = 'red' )
  dot.edge ( '0', '5', '0.5', fontcolor = 'red' )

  dot.edge ( '1', '2', '1.0', fontcolor = 'red' )

  dot.edge ( '2', '0', '0.5', fontcolor = 'red' )
  dot.edge ( '2', '3', '0.5', fontcolor = 'red' )

  dot.edge ( '3', '0', '1.0', fontcolor = 'red' )

  dot.edge ( '4', '2', '1.0', fontcolor = 'red' )

  dot.edge ( '5', '5', '1.0', fontcolor = 'red' )

  dot.edge ( '6', '6', '1.0', fontcolor = 'red' )

  print ( dot.source )
#
#  Save graph to a file, and display an image to the screen.
#
  dot.render ( 'pagerank_plot2.dot', view = True )

  filename = 'pagerank_plot2.dot.png'
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'pagerank_graphs:' )
  print ( '  Normal end of execution.' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  pagerank_graphs ( )
  timestamp ( )

