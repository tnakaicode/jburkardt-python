#! /usr/bin/env python
#
def edge_check ( n_node, n_edge, t ):

#*****************************************************************************80
#
## EDGE_CHECK checks a graph stored by edges.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer  N_NODE, the number of nodes in the graph.
#
#    Input, integer N_EDGE, the number of edges in the graph.
#
#    Input, integer T(2,N_EDGE), describes the edges of the tree
#    as pairs of nodes.
#
#    Output, integer CHECK
#    1, the data is legal.
#    0, the data is not legal. 
#
  check = True

  if ( n_node < 0 ):
    check = False
    return check

  if ( n_edge < 0 ):
    check = False
    return check
#
#  Every edge must join two legal nodes.
#
  for i in range ( 0, 2 ):
    for j in range ( 0, n_edge ):
      if ( t[i,j] < 1 or n_node < t[i,j] ):
        check = False
        return check
#
#  Every edge must join distinct nodes.
#
  for j in range ( 0, n_edge ):
    if ( t[0,j] == t[1,j] ):
      check = False
      return check
#
#  Every edge must be distinct.
#
  for j in range ( 0, n_edge - 1 ):
    for j2 in range ( j + 1, n_edge ):
      if ( t[0,j] == t[0,j2] and t[1,j] == t[1,j2] ):
        check = False
        return check
      elif ( t[0,j] == t[1,j2] and t[1,j] == t[0,j2] ):
        check = False
        return check

  return check

def edge_check_test ( ):

#*****************************************************************************80
#
## EDGE_CHECK_TEST tests EDGE_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  print ( '' )
  print ( 'EDGE_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EDGE_CHECK checks a graph described by edges.' )
  print ( '' )
  print ( '  Check?  Nodes  Edges    EdgeList' )
  
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      node_num = -5
      edge_num = 3
      edge_list = np.array ( [ \
        [ 1, 2, 3 ], \
        [ 2, 3, 1 ] ] )
    elif ( test == 2 ):
      node_num = 3
      edge_num = -1
      edge_list = np.array ( [ \
        [ 1, 2, 3 ], \
        [ 2, 3, 1 ] ] )
    elif ( test == 3 ):
      node_num = 3
      edge_num = 3
      edge_list = np.array ( [ \
        [ 1, 2, 3 ], \
        [ 2, 3, 4 ] ] )
    elif ( test == 4 ):
      node_num = 3
      edge_num = 3
      edge_list = np.array ( [ \
        [ 1, 2, 3 ], \
        [ 2, 2, 1 ] ] )
    elif ( test == 5 ):
      node_num = 3
      edge_num = 3
      edge_list = np.array ( [ \
        [ 1, 2, 2 ], \
        [ 2, 3, 1 ] ] )
    elif ( test == 6 ):
      node_num = 3
      edge_num = 3
      edge_list = np.array ( [ \
        [ 1, 2, 3 ], \
        [ 2, 3, 1 ] ] )

    print ( '' )
    check = edge_check ( node_num, edge_num, edge_list )
    print ( '      %2d     %2d     %2d' % ( check, node_num, edge_num ) )
    i4mat_print ( 2, edge_num, edge_list, '  Edge list of graph:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'EDGE_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  edge_check_test ( )
  timestamp ( )
 
