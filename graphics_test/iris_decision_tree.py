#! /usr/bin/env python3
#
def iris_decision_tree ( ):

#*****************************************************************************80
#
## iris_decision_tree plots a decision tree for iris classification.
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
#    03 May 2019
#
#  Author:
#
#    John Burkardt
#
  from graphviz import Digraph
  import platform

  print ( '' )
  print ( 'iris_decision_tree:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot a decision tree for the iris classification task.' )
  print ( '' )

  dot = Digraph ( comment = 'A network', format = 'png' )
#
#  Specify the nodes, giving each an internal code, and a label.
#
  dot.node ( '1', 'Test petal length' )
  dot.node ( '2', 'Test petal width' )
  dot.node ( '3', 'Test petal length' )
  dot.node ( '4', 'Test petal width' )
  dot.node ( '5', 'setosa' )
  dot.node ( '6', 'versicolor' )
  dot.node ( '7', 'virginica' )
  dot.node ( '8', 'virginica' )
  dot.node ( '9', 'virginica' )
#
#  Specify the edges as connections between two nodes.
#
  dot.edge ( '1', '5', 'petal length < 2.45' )
  dot.edge ( '1', '2', '2.45 <= petal length' )

  dot.edge ( '2', '3', 'petal width < 1.75' )
  dot.edge ( '2', '9', '1.75 <= petal width' )

  dot.edge ( '3', '4', 'petal length < 4.95' )
  dot.edge ( '3', '8', '4.95 <= petal length' )

  dot.edge ( '4', '6', 'petal width < 1.65' )
  dot.edge ( '4', '7', '1.65 <= petal width' )

  print ( dot.source )
#
#  Save graph to a file, and optionally display an image to the screen.
#
  dot.render ( 'iris_decision_tree.dot', view = False )

  filename = 'iris_decision_tree.dot.png'
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'iris_decision_tree:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  iris_decision_tree ( )
  timestamp ( )

