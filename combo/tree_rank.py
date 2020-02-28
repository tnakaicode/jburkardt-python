#! /usr/bin/env python
#
def tree_rank ( n, t ):

#*****************************************************************************80
#
## TREE_RANK ranks a tree.
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
#    N must be at least 3.
#
#    Input, integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#
#    Output, integer RANK, the rank of the tree.
#
  from pruefer_rank import pruefer_rank
  from sys import exit
  from tree_check import tree_check
  from tree_to_pruefer import tree_to_pruefer
#
#  Check the tree.
#
  check = tree_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'TREE_RANK - Fatal error!' )
    print ( '  Input tree is illegal.' )
    exit ( 'TREE_RANK - Fatal error!' )
#
#  Convert the tree to a Pruefer code.
#
  p = tree_to_pruefer ( n, t )
#
#  Find the rank of the Pruefer code.
#
  rank = pruefer_rank ( n, p )

  return rank

def tree_rank_test ( ):

#*****************************************************************************80
#
## TREE_RANK_TEST tests TREE_RANK.
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
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  n = 4

  print ( '' )
  print ( 'TREE_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TREE_RANK ranks trees.' )

  n = 4

  t = np.array ( [ \
    [ 4, 3, 3 ], \
    [ 1, 2, 1 ] ] )

  i4mat_print ( 2, n - 1, t, '  The element:' )

  rank = tree_rank ( n, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d:' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TREE_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tree_rank_test ( )
  timestamp ( )
