#! /usr/bin/env python
#
def ksubset_revdoor_rank ( k, n, t ):

#*****************************************************************************80
#
## KSUBSET_REVDOOR_RANK computes the revolving door rank of a K subset.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2011
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
    print ( 'KSUBSET_REVDOOR_RANK - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'KSUBSET_REVDOOR_RANK - Fatal error!' )

  if ( ( k % 2 ) == 0 ):

    rank = 0

  else:

    rank = - 1

  s = 1

  for i in range ( k, 0, -1 ):
    rank = rank + s * i4_choose ( t[-1], i )
    s = - s

  return rank

def ksubset_revdoor_rank_test ( ):

#*****************************************************************************80
#
## KSUBSET_REVDOOR_RANK_TEST tests KSUBSET_REVDOOR_RANK.
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
  print ( 'KSUBSET_REVDOOR_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUBSET_REVDOOR_RANK ranks K-subsets of an N set' )
  print ( '  using the revolving door ordering.' )

  t = np.array ( [ 2, 4, 5 ] )
  i4vec_transpose_print ( k, t, '  The K-subset to be ranked:' )

  rank = ksubset_revdoor_rank ( k, n, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUBSET_REVDOOR_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksubset_revdoor_rank_test ( )
  timestamp ( )
 
