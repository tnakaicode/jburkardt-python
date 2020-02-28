#! /usr/bin/env python
#
def ksubset_colex_rank ( k, n, t ):

#*****************************************************************************80
#
## KSUBSET_COLEX_RANK computes the colex rank of a K subset.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2015
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
#    element of the K subset.  The elements must be listed in DESCENDING order.
#
#    Output, integer RANK, the rank of the subset.
#
  from i4_choose import i4_choose
  from ksubset_colex_check import ksubset_colex_check
  from sys import exit
#
#  Check.
#
  check = ksubset_colex_check ( k, n, t )

  if ( not check ):
    print ( '' )
    print ( 'KSUBSET_COLEX_RANK - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'KSUBSET_COLEX_RANK - Fatal error!' )

  rank = 0

  for i in range ( 0, k ):
    rank = rank + i4_choose ( t[i] - 1, k - i )

  return rank

def ksubset_colex_rank_test ( ):

#*****************************************************************************80
#
## KSUBSET_COLEX_RANK_TEST tests KSUBSET_COLEX_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2015
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
  t = np.array ( [ 5, 3, 1 ] )

  print ( '' )
  print ( 'KSUBSET_COLEX_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUBSET_COLEX_RANK ranks K-subsets of an N set,' )
  print ( '  using the colexicographic ordering.' )

  i4vec_transpose_print ( k, t, '  The element to be ranked:' )

  rank = ksubset_colex_rank ( k, n, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d.' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUBSET_COLEX_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksubset_colex_rank_test ( )
  timestamp ( )
 
