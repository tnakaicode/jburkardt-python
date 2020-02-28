#! /usr/bin/env python3
#
def alphabet_binary_tree ( ):

#*****************************************************************************80
#
## alphabet_binary_tree plots a binary tree. 
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
#    01 May 2019
#
#  Author:
#
#    John Burkardt
#
  from graphviz import Digraph
  import platform

  print ( '' )
  print ( 'alphabet_binary_tree:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot an alphabetizing binary tree.' )
  print ( '' )

  dot = Digraph ( comment = 'A binary tree', format = 'png' )
#
#  Specify the nodes, giving each an internal code, and a label.
#
  dot.attr ( 'node', shape = 'box' )
  dot.node ( '1', 'A-Z' )
  dot.node ( '2', 'A-M' )
  dot.node ( '3', 'N-Z' )

  dot.node ( '4', 'A-F' )
  dot.node ( '5', 'G-M' )
  dot.node ( '6', 'N-S' )
  dot.node ( '7', 'T-Z' )

  dot.node ( '8', 'A-C' )
  dot.node ( '9', 'D-F' )
  dot.node ( '10', 'G-I' )
  dot.node ( '11', 'J-M' )
  dot.node ( '12', 'N-P' )
  dot.node ( '13', 'Q-S' )
  dot.node ( '14', 'T-V' )
  dot.node ( '15', 'W-Z' )

  dot.node ( '16', 'A' )
  dot.node ( '17', 'B-C' )
  dot.node ( '18', 'D' )
  dot.node ( '19', 'E-F' )
  dot.node ( '20', 'G' )
  dot.node ( '21', 'H-I' )
  dot.node ( '22', 'J-K' )
  dot.node ( '23', 'L-M' )
  dot.node ( '24', 'N' )
  dot.node ( '25', 'O-P' )
  dot.node ( '26', 'Q' )
  dot.node ( '27', 'R-S' )
  dot.node ( '28', 'T' )
  dot.node ( '29', 'U-V' )
  dot.node ( '30', 'W-X' )
  dot.node ( '31', 'Y-Z' )

  dot.node ( '32', 'B' )
  dot.node ( '33', 'C' )
  dot.node ( '34', 'E' )
  dot.node ( '35', 'F' )
  dot.node ( '36', 'H' )
  dot.node ( '37', 'I' )
  dot.node ( '38', 'J' )
  dot.node ( '39', 'K' )
  dot.node ( '40', 'L' )
  dot.node ( '41', 'M' )
  dot.node ( '42', 'O' )
  dot.node ( '43', 'P' )
  dot.node ( '44', 'R' )
  dot.node ( '45', 'S' )
  dot.node ( '46', 'U' )
  dot.node ( '47', 'V' )
  dot.node ( '48', 'W' )
  dot.node ( '49', 'X' )
  dot.node ( '50', 'Y' )
  dot.node ( '51', 'Z' )

#
#  Specify the edges as connections between two nodes.
#
  dot.edge ( '1', '2' )
  dot.edge ( '1', '3' )

  dot.edge ( '2', '4' )
  dot.edge ( '2', '5' )
  dot.edge ( '3', '6' )
  dot.edge ( '3', '7' )

  dot.edge ( '4', '8' )
  dot.edge ( '4', '9' )
  dot.edge ( '5', '10' )
  dot.edge ( '5', '11' )
  dot.edge ( '6', '12' )
  dot.edge ( '6', '13' )
  dot.edge ( '7', '14' )
  dot.edge ( '7', '15' )

  dot.edge ( '8', '16' )
  dot.edge ( '8', '17' )
  dot.edge ( '9', '18' )
  dot.edge ( '9', '19' )
  dot.edge ( '10', '20' )
  dot.edge ( '10', '21' )
  dot.edge ( '11', '22' )
  dot.edge ( '11', '23' )
  dot.edge ( '12', '24' )
  dot.edge ( '12', '25' )
  dot.edge ( '13', '26' )
  dot.edge ( '13', '27' )
  dot.edge ( '14', '28' )
  dot.edge ( '14', '29' )
  dot.edge ( '15', '30' )
  dot.edge ( '15', '31' )

  dot.edge ( '17', '32' )
  dot.edge ( '17', '33' )
  dot.edge ( '19', '34' )
  dot.edge ( '19', '35' )
  dot.edge ( '21', '36' )
  dot.edge ( '21', '37' )
  dot.edge ( '22', '38' )
  dot.edge ( '22', '39' )
  dot.edge ( '23', '40' )
  dot.edge ( '23', '41' )
  dot.edge ( '25', '42' )
  dot.edge ( '25', '43' )
  dot.edge ( '27', '44' )
  dot.edge ( '27', '45' )
  dot.edge ( '29', '46' )
  dot.edge ( '29', '47' )
  dot.edge ( '30', '48' )
  dot.edge ( '30', '49' )
  dot.edge ( '31', '50' )
  dot.edge ( '31', '51' )

  print ( dot.source )
#
#  Save graph to a file, and optionally display an image to the screen.
#
  dot.render ( 'alphabet_binary_tree.dot', view = False )

  filename = 'alphabet_binary_tree.dot.png'
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'alphabet_binary_tree:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  alphabet_binary_tree ( )
  timestamp ( )
