#! /usr/bin/env python3
#
def knight_graph ( ):

#*****************************************************************************80
#
## knight_graph() plots the graph of knight moves in a puzzle.
#
#  Discussion:
#
#    To use this example, you need to have installed graphviz and pydotplus.
#
#    The following puzzle comes from the computer game "The 11th Hour".
#
#        A          1
#        B C        2 3
#        D E F      4 5 6
#      G H I J    7 8 9 10
#
#    A fragment of a chess board is given.  Black knights are positioned
#    at G and I, white knights at A and E.  The problem is to exchange the
#    white and black knights using a series of legal chess moves, and
#    remaining on the fragmentary board.  No captures are assumed, and
#    pieces can't move through each other.
#
#    The puzzle is very difficult to solve until a plot is made of the
#    adjacency graph that describes how each square of the board is 
#    connected to other squares by knight moves.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kenneth Chang,
#    Fields Medals in Mathematics Won by 4 under Age 40,
#    New York Times, 5 July 2022.
#
  from graphviz import Graph
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'knight_graph():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Plot a graph associated with a puzzle from "The 11th Hour"' )
  print ( '  involving interchanging 2 black and 2 white knights.' )
  print ( '' )

  dot = Graph ( comment = 'knight_graph', format = 'png' )
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
#
#  Specify the edges as connections between two nodes.
#  The connections involve knight moves.
#
  dot.edge ( '1', '5' )
  dot.edge ( '2', '6' )
  dot.edge ( '2', '7' )
  dot.edge ( '2', '9' )
  dot.edge ( '3', '8' )
  dot.edge ( '3', '10' )
  dot.edge ( '4', '10' )
  dot.edge ( '5', '7' )
  dot.edge ( '6', '8' )

  print ( dot.source )
#
#  Save graph to a file, and optionally display an image to the screen.
#
  dot.render ( 'knight_graph.dot', view = False )

  filename = 'knight_graph.dot.png'
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'knight_graph():' )
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
  knight_graph ( )
  timestamp ( )

