#! /usr/bin/env python
#
def ksubset_lex_rank ( k, n, t ):

#*****************************************************************************80
#
## KSUBSET_LEX_RANK computes the lexicographic rank of a K subset.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2015
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
#    Input, integer K, the number of elements each K subset must
#    have.  1 <= K <= N.
#
#    Input, integer N, the number of elements in the master set.
#    N must be positive.
#
#    Input, integer T(K), describes a K subset.  T(I) is the I-th
#    element.  The elements must be listed in ascending order.
#
#    Output, integer RANK, the rank of the K subset.
#
  from i4_choose import i4_choose
  from ksubset_lex_check import ksubset_lex_check
  from sys import exit
#
#  Check.
#
  check = ksubset_lex_check ( k, n, t )

  if ( not check ):
    print ( '' )
    print ( 'KSUBSET_LEX_RANK - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'KSUBSET_LEX_RANK - Fatal error!' )

  rank = 0

  for i in range ( 0, k ):

    if ( i == 0 ):
      tim1 = 0
    else:
      tim1 = t[i-1]

    if ( tim1 + 1 <= t[i] - 1 ):
      for j in range ( tim1 + 1, t[i] ):
        rank = rank + i4_choose ( n - j, k - 1 - i )

  return rank

def ksubset_lex_rank_test ( ):

#*****************************************************************************80
#
## KSUBSET_LEX_RANK_TEST tests KSUBSET_LEX_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  k = 3
  n = 5

  print ( '' )
  print ( 'KSUBSET_LEX_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUBSET_LEX_RANK ranks K-subsets of an N set,' )
  print ( '  using the lexicographic ordering.' )

  t = np.array ( [ 1, 4, 5 ] )
  i4vec_transpose_print ( k, t, '  The element to be ranked:' )

  rank = ksubset_lex_rank ( k, n, t )

  print ( '' )
  print ( '  The rank is computed as %d.' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUBSET_LEX_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksubset_lex_rank_test ( )
  timestamp ( )
 
