#! /usr/bin/env python
#
def edge_degree ( n_node, n_edge, t ):

#*****************************************************************************80
#
## EDGE_DEGREE returns the degree of the nodes of a graph stored by edges.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N_NODE, the number of nodes in the graph.
#    N_NODE must be positive.
#
#    Input, integer N_EDGE, the number of edges in the graph.
#    N_EDGE must be positive.
#
#    Input, integer T(2,N_EDGE), describes the edges of the tree
#    as pairs of nodes.
#
#    Output, integer D(N_NODE), the degree of each node.
#
  import numpy as np
  from edge_check import edge_check
  from sys import exit
#
#  Check.
#
  check = edge_check ( n_node, n_edge, t )

  if ( not check ):
    print ( '' )
    print ( 'EDGE_DEGREE - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'EDGE_DEGREE - Fatal error!' )
#
#  Compute the degree of each node.
#
  d = np.zeros ( n_node )

  for j in range ( 0, n_edge ):
    d[t[0,j]-1] = d[t[0,j]-1] + 1;
    d[t[1,j]-1] = d[t[1,j]-1] + 1;

  return d

def edge_degree_test ( ):

#*****************************************************************************80
#
## EDGE_DEGREE_TEST tests EDGE_DEGREE.
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
  from i4vec_print import i4vec_print

  print ( '' )
  print ( 'EDGE_DEGREE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EDGE_DEGREE determines the degree of each node in a graph.' )

  node_num = 5
  edge_num = 5
  edge = np.array ( [ \
    [ 1, 2, 2, 3, 4 ], \
    [ 2, 3, 4, 4, 5 ] ] )

  i4mat_print ( 2, edge_num, edge, '  The edge array:' )

  d = edge_degree ( node_num, edge_num, edge );

  i4vec_print ( node_num, d, '  The degree vector:' );
#
#  Terminate.
#
  print ( '' )
  print ( 'EDGE_DEGREE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  edge_degree_test ( )
  timestamp ( )
 
