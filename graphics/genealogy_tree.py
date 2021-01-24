#! /usr/bin/env python3
#
def genealogy_tree ( ):

#*****************************************************************************80
#
## genealogy_tree plots a binary tree. 
#
#  Discussion:
#
#    A binary tree is a connected directed graph, with no circuits, in which 
#    each node has at most two "descendants".
# 
#    To use this example, you need to have installed graphviz and pydotplus.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 May 2019
#
#  Author:
#
#    John Burkardt
#
  from graphviz import Digraph
  import platform

  print ( '' )
  print ( 'genealogy_tree:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot a tree illustrating a genealogy' )
  print ( '' )

  dot = Digraph ( comment = 'A binary tree', format = 'png' )
#
#  Specify the nodes, giving each an internal code, and a label.
#
  dot.attr ( 'node', shape = 'egg' )
  dot.node ( '1', 'Alan' )
  dot.node ( '2', 'Bert' )
  dot.node ( '3', 'Chad' )
  dot.node ( '4', 'Dian' )
  dot.node ( '5', 'Enid' )
  dot.node ( '6', 'Fran' )
  dot.node ( '7', 'Gert' )
  dot.node ( '8', 'Hank' )
  dot.node ( '9', 'Iona' )
  dot.node ( '10', 'Jean' )
  dot.node ( '11', 'Kate' )
  dot.node ( '12', 'Lynn' )
#
#  Specify the edges as connections between two nodes.
#
  dot.edge ( '1', '2' )
  dot.edge ( '1', '3' )

  dot.edge ( '2', '4' )
  dot.edge ( '2', '6' )

  dot.edge ( '3', '5' )
  dot.edge ( '3', '10' )

  dot.edge ( '4', '7' )
  dot.edge ( '4', '8' )
  dot.edge ( '4', '9' )

  dot.edge ( '5', '11' )
  dot.edge ( '5', '12' )

  print ( dot.source )
#
#  Save graph to a file, and optionally display an image to the screen.
#
  dot.render ( 'genealogy_tree.dot', view = False )

  filename = 'genealogy_tree.dot.png'
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'genealogy_tree:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  genealogy_tree ( )
  timestamp ( )
