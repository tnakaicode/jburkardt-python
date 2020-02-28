#! /usr/bin/env python
#
def ksubset_lex_unrank ( rank, k, n ):

#*****************************************************************************80
#
## KSUBSET_LEX_UNRANK computes the K subset of given lexicographic rank.
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
#    Input, integer RANK, the rank of the K subset.
#
#    Input, integer K, the number of elements each K subset must
#    have.  0 <= K <= N.
#
#    Input, integer N, the number of elements in the master set.
#    N must be positive.
#
#    Output, integer T(K), describes the K subset of the given
#    rank.  T(I) is the I-th element.  The elements must be listed in
#    ascending order.
#
  import numpy as np
  from i4_choose import i4_choose
  from ksubset_enum import ksubset_enum
  from sys import exit
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'KSUBSET_LEX_RANK - Fatal error!' )
    print ( '  Input N is illegal.' )
    exit ( 'KSUBSET_LEX_UNRANK - Fatal error!' )

  t = np.zeros ( k )

  if ( k == 0 ):
    return t

  if ( k < 0 or n < k ):
    print ( '' )
    print ( 'KSUBSET_LEX_RANK - Fatal error!' )
    print ( '  Input K is illegal.' )
    exit ( 'KSUBSET_LEX_UNRANK - Fatal error!' )

  nksub = ksubset_enum ( k, n )

  if ( rank < 0 or nksub < rank ):
    print ( '' )
    print ( 'KSUBSET_LEX_UNRANK - Fatal error!' )
    print ( '  Input rank is illegal.' )
    exit ( 'KSUBSET_LEX_UNRANK - Fatal error!' )

  x = 1

  for i in range ( 1, k + 1 ):

    while ( i4_choose ( n - x, k - i ) <= rank ):
      rank = rank - i4_choose ( n - x, k - i )
      x = x + 1

    t[i-1] = x
    x = x + 1

  return t

def ksubset_lex_unrank_test ( ):

#*****************************************************************************80
#
## KSUBSET_LEX_UNRANK_TEST tests KSUBSET_LEX_UNRANK.
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
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  k = 3
  n = 5

  print ( '' )
  print ( 'KSUBSET_LEX_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUBSET_LEX_UNRANK unranks K-subsets of an N set,' )
  print ( '  using the lexicographic ordering.' )

  rank = 5

  t = ksubset_lex_unrank ( rank, k, n )

  i4vec_transpose_print ( k, t, '  The element of rank 5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUBSET_LEX_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksubset_lex_unrank_test ( )
  timestamp ( )
 
