#! /usr/bin/env python
#
def ksubset_colex_unrank ( rank, k, n ):

#*****************************************************************************80
#
## KSUBSET_COLEX_UNRANK computes the K subset of given colex rank.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 November 2015
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
#    DESCENDING order.
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
    print ( 'KSUBSET_COLEX_UNRANK - Fatal error!' )
    print ( '  The input N = %d is illegal.' % ( n ) )
    exit ( 'KSUBSET_COLEX_UNRANK - Fatal error!' )

  if ( k == 0 ):
    t = np.zeros ( k )
    return t

  if ( k < 0 or n < k ):
    print ( '' )
    print ( 'KSUBSET_COLEX_UNRANK - Fatal error!' )
    print ( '  The input K = %d is illegal.' % ( k ) )
    exit ( 'KSUBSET_COLEX_UNRANK - Fatal error!' )

  nksub = ksubset_enum ( k, n )

  if ( rank < 0 or nksub < rank ):
    print ( '' )
    print ( 'KSUBSET_COLEX_UNRANK - Fatal error!' )
    print ( '  The input RANK = %d is illegal.' % ( rank ) )
    exit ( 'KSUBSET_COLEX_UNRANK - Fatal error!' )
 
  t = np.zeros ( k )

  x = n

  for i in range ( 0, k ):

    while ( rank < i4_choose ( x, k - i ) ):
      x = x - 1

    t[i] = x + 1
    rank = rank - i4_choose ( x, k - i )

  return t

def ksubset_colex_unrank_test ( ):

#*****************************************************************************80
#
## KSUBSET_COLEX_UNRANK_TEST tests KSUBSET_COLEX__UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print
  from ksubset_enum import ksubset_enum

  k = 3
  n = 5

  print ( '' )
  print ( 'KSUBSET_COLEX_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUBSET_COLEX_UNRANK unranks K-subsets of an N set,' )
  print ( '  using the colexicographic ordering:' )

  nksub = ksubset_enum ( k, n )
  rank = ( nksub // 2 )

  t = ksubset_colex_unrank ( rank, k, n )

  print ( '' )
  print ( '  The element of rank %d:' % ( rank ) )
  print ( '' )
  i4vec_print ( k, t, '  The element:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUBSET_COLEX_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksubset_colex_unrank_test ( )
  timestamp ( )

