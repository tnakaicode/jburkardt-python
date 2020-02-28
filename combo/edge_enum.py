#! /usr/bin/env python
#
def edge_enum ( node_num ):

#*****************************************************************************80
#
## EDGE_ENUM enumerates the maximum number of edges in a graph on NODE_NUM nodes.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NODE_NUM, the number of nodes in the graph.
#    N_NODE must be positive.
#
#    Output, integer EDGE_NUM, the maximum number of edges in a graph
#    on N_NODE nodes.
#
  edge_num = ( node_num * ( node_num - 1 ) ) / 2

  return edge_num

def edge_enum_test ( ):

#*****************************************************************************80
#
## EDGE_ENUM_TEST tests EDGE_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'EDGE_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EDGE_ENUM enumerates the maximum number of edges' )
  print ( '  possible in a graph of NODE_NUM nodes.' )
  print ( '' )
  print ( '   NODE_NUM    EDGE_NUM(max)' )
  print ( '' )

  for node_num in range ( 1, 11 ):
    edge_num = edge_enum ( node_num )
    print ( '         %2d      %6d' % ( node_num, edge_num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EDGE_ENUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  edge_enum_test ( )
  timestamp ( )
