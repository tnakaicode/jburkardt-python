#! /usr/bin/env python
#
def tree_unrank ( rank, n ):

#*****************************************************************************80
#
## TREE_UNRANK unranks a tree.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
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
#    Input, integer RANK, the rank of the tree.
#
#    Input, integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    Output, integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#
  from pruefer_to_tree import pruefer_to_tree
  from pruefer_unrank import pruefer_unrank
  from sys import exit
  from tree_enum import tree_enum
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'TREE_UNRANK - Fatal error!' )
    print ( '  Input N is illegal.' )
    exit ( 'TREE_UNRANK - Fatal error!' )

  tree_num = tree_enum ( n );

  if ( rank < 0 or tree_num < rank ):
    print ( '' )
    print ( 'TREE_UNRANK - Fatal error!' )
    print ( '  The input rank is illegal.' )
    exit ( 'TREE_UNRANK - Fatal error!' )
#
#  Unrank the Pruefer code.
#
  p = pruefer_unrank ( rank, n )
#
#  Convert the Pruefer code to a tree.
#
  t = pruefer_to_tree ( n, p )

  return t

def tree_unrank_test ( ):

#*****************************************************************************80
#
## TREE_UNRANK_TEST tests TREE_UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4mat_print import i4mat_print

  n = 4

  print ( '' )
  print ( 'TREE_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TREE_UNRANK unranks trees.' )

  n = 4

  rank = 8

  t = tree_unrank ( rank, n )

  i4mat_print ( 2, n - 1, t, '  The element of rank 8:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TREE_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tree_unrank_test ( )
  timestamp ( )
 
