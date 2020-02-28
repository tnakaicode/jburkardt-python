#! /usr/bin/env python
#
def perm_tj_rank ( n, p ):

#*****************************************************************************80
#
## PERM_TJ_RANK computes the Trotter-Johnson rank of a permutation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 December 2015
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
#    Input, integer N, the number of values being permuted.
#    N must be positive.
#
#    Input, integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#    Output, integer RANK, the rank of the permutation.
#
  from perm_check import perm_check
  from sys import exit
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM_TJ_RANK - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'PERM_TJ_RANK - Fatal error!' )

  rank = 0

  for j in range ( 2, n + 1 ):

    k = 1
    i = 0

    while ( p[i] != j ):
      if ( p[i] < j ):
        k = k + 1
      i = i + 1
    
    if ( ( rank % 2 ) == 0 ):
      rank = j * rank + j - k
    else:
      rank = j * rank + k - 1

  return rank

def perm_tj_rank_test ( ):

#*****************************************************************************80
#
## PERM_TJ_RANK_TEST tests PERM_TJ_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from perm_print import perm_print

  n = 4

  print ( '' )
  print ( 'PERM_TJ_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_TJ_RANK ranks' )
  print ( '  permutations using the Trotter-Johnson ordering.' )

  p = np.array ( [ 4, 3, 2, 1 ] )
  perm_print ( n, p, '  Element to be ranked:' )

  rank = perm_tj_rank ( n, p )
  print ( '' )
  print ( '  The rank is computed to be %d.' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_TJ_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_tj_rank_test ( )
  timestamp ( )
 
