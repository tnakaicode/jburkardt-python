#! /usr/bin/env python
#
def tree_to_pruefer ( n, t ):

#*****************************************************************************80
#
## TREE_TO_PRUEFER converts a tree to a Pruefer code.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
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
#    Input, integer N, the number of nodes in the tree.
#    N must be positive.
#
#    Input, integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#
#    Output, integer P(N-2), the Pruefer code for the tree.
#
  import numpy as np
  from edge_degree import edge_degree
  from sys import exit
  from tree_check import tree_check
#
#  Check.
#
  check = tree_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'TREE_TO_PRUEFER - Fatal error!' )
    print ( '  Input tree is illegal.' )
    exit ( 'TREE_TO_PRUEFER - Fatal error!' )
#
#  Compute the degree of each node.
#
  d = edge_degree ( n, n - 1, t )

  p = np.zeros ( n - 1, dtype = np.int32 )
#
#  Make a copy of T.
#
  t2 = np.zeros ( [ 2, n - 1 ], dtype = np.int32 )

  for i in range ( 0, 2 ):
    for j in range ( 0, n - 1 ):
      t2[i,j] = t[i,j]
#
#  Delete N-1 nodes of degree 1.
#
  for j in range ( 0, n - 2 ):
#
#  Find a node of degree 1.
#
    x = n
    while ( d[x-1] != 1 ):
      x = x - 1
#
#  Find its neighbor.
#
    k = 0

    while ( True ):

      if ( t2[0,k] == x ):
        y = t2[1,k]
        break

      if ( t2[1,k] == x ):
        y = t2[0,k]
        break

      k = k + 1
#
#  Store the neighbor.
#
    p[j] = y
#
#  Delete the edge from the tree.
#
    d[x-1] = d[x-1] - 1
    d[y-1] = d[y-1] - 1

    t2[0,k] = - t2[0,k]
    t2[1,k] = - t2[1,k]

  return p

def tree_to_pruefer_test ( ):

#*****************************************************************************80
#
## TREE_TO_PRUEFER_TEST tests TREE_TO_PRUEFER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_uniform_ab import i4_uniform_ab
  from i4mat_print import i4mat_print
  from i4vec_transpose_print import i4vec_transpose_print
  from pruefer_enum import pruefer_enum
  from pruefer_to_tree import pruefer_to_tree
  from pruefer_unrank import pruefer_unrank

  n = 5
  seed = 123456789
  test_num = 5

  print ( '' )
  print ( 'TREE_TO_PRUEFER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TREE_TO_PRUEFER converts a tree to a Pruefer code.' )

  pruefer_num = pruefer_enum ( n )

  i4_lo = 0
  i4_hi = pruefer_num - 1

  for test in range ( 0, test_num ):
#
#  Pick a "random" Pruefer code.
#
    rank, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )

    p = pruefer_unrank ( rank, n )

    i4vec_transpose_print ( n - 2, p, '  Pruefer code:' )
#
#  Convert the Pruefer code to a tree.
#
    t = pruefer_to_tree ( n, p )

    i4mat_print ( 2, n - 1, t, '  Edge list for corresponding tree:' )
#
#  Convert the tree to a Pruefer code.
#
    p = tree_to_pruefer ( n, t )

    i4vec_transpose_print ( n - 2, p, '  Recovered Pruefer code:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TREE_TO_PRUEFER_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tree_to_pruefer_test ( )
  timestamp ( )
