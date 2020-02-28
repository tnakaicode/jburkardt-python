#! /usr/bin/env python
#
def subset_lex_rank ( n, t ):

#*****************************************************************************80
#
## SUBSET_LEX_RANK computes the lexicographic rank of a subset.
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
#    Input, integer N, the number of items in the master set.
#    N must be positive.
#
#    Input, integer T(N), the subset.  If T(I) = 0, item I is
#    not in the subset if T(I) = 1, item I is in the subset.
#
#    Output, integer RANK, the rank of the subset.
#
  from subset_check import subset_check
  from sys import exit
#
#  Check.
#
  check = subset_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'SUBSET_LEX_RANK - Fatal error!' )
    print ( '  The subset is not legal.' )
    exit ( 'SUBSET_LEX_RANK - Fatal error!' )

  rank = 0

  for i in range ( 0, n ):

    if ( t[i] == 1 ):
      rank = rank + 2 ** ( n - 1 - i )

  return rank

def subset_lex_rank_test ( ):

#*****************************************************************************80
#
## SUBSET_LEX_RANK_TEST tests SUBSET_LEX_RANK.
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
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 5

  print ( '' )
  print ( 'SUBSET_LEX_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_LEX_RANK ranks subsets of a set,' )
  print ( '  using the lexicographic ordering.' )

  t = np.array ( [ 0, 1, 0, 1, 0 ] )
  i4vec_transpose_print ( n, t, '  The element:' )

  rank = subset_lex_rank ( n, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_LEX_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_lex_rank_test ( )
  timestamp ( )
 
