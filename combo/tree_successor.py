#! /usr/bin/env python
#
def tree_successor ( n, t, rank ):

#*****************************************************************************80
#
## TREE_SUCCESSOR returns the successor of a tree.
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
#    Input/output, integer T(2,N-1), describes the edges of the
#    tree as pairs of nodes.  On output, the input tree has been replaced
#    by its successor.
#
#    Input/output, integer RANK, the rank of the tree.
#
  import numpy as np
  from pruefer_successor import pruefer_successor
  from pruefer_to_tree import pruefer_to_tree
  from sys import exit
  from tree_check import tree_check
  from tree_to_pruefer import tree_to_pruefer
#
#  Return the first element.
#
  if ( rank == -1 ):
    p = np.ones ( n - 2, dtype = np.int32 )
    t = pruefer_to_tree ( n, p )
    rank = 0
    return t, rank
#
#  Check the tree.
#
  check = tree_check ( n, t );

  if ( not check ):
    print ( '' )
    print ( 'TREE_SUCCESSOR - Fatal error!' )
    print ( '  Input tree is illegal.' )
    exit ( 'TREE_SUCCESSOR - Fatal error!' )
#
#  Convert the tree to a Pruefer code.
#
  p = tree_to_pruefer ( n, t )
#
#  Find the successor of the Pruefer code.
#
  p, rank = pruefer_successor ( n, p, rank )
#
#  Convert the Pruefer code to the tree.
#
  t = pruefer_to_tree ( n, p )

  return t, rank

def tree_successor_test ( ):

#*****************************************************************************80
#
## TREE_SUCCESSOR_TEST tests TREE_SUCCESSOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'TREE_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TREE_SUCCESSOR lists trees.' )

  t = np.array ( [ 2, n - 1 ], dtype = np.int32 )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = tree_successor ( n, t, rank )

    if ( rank <= rank_old ):
      break

    print ( '%5d  ' % ( rank ), end = '' )
    for j in range ( 0, n - 1 ):
      print ( '%5d' % ( t[0,j] ), end = '' )
    print ( '' )
    print ( '       ', end = '' )
    for j in range ( 0, n - 1 ):
      print ( '%5d' % ( t[1,j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TREE_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tree_successor_test ( )
  timestamp ( )
 
