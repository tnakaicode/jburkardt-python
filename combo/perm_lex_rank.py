#! /usr/bin/env python
#
def perm_lex_rank ( n, p ):

#*****************************************************************************80
#
## PERM_LEX_RANK computes the lexicographic rank of a permutation.
#
#  Discussion:
#
#    The original code altered the input permutation.  
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
  import numpy as np
  from i4_factorial import i4_factorial
  from perm_check import perm_check
  from sys import exit
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM_LEX_RANK - Fatal error!' )
    print ( '  The input array is illegal.' )
    error ( 'PERM_LEX_RANK - Fatal error!' )

  p2 = np.zeros ( n )
  for i in range ( 0, n ):
    p2[i] = p[i]

  rank = 0

  for j in range ( 0, n ):

    rank = rank + ( p2[j] - 1 ) * i4_factorial ( n - j )

    for i in range ( j + 1, n ):
      if ( p2[j] < p2[i] ):
        p2[i] = p2[i] - 1

  return rank

def perm_lex_rank_test ( ):

#*****************************************************************************80
#
## PERM_LEX_RANK_TEST tests PERM_LEX_RANK.
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
  print ( 'PERM_LEX_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_LEX_RANK ranks' )
  print ( '  permutations using the lexicographic ordering.' )

  p = np.array ( [ 3, 1, 2, 4 ] )
  perm_print ( n, p, '  Element to be ranked:' )

  rank = perm_lex_rank ( n, p )
  print ( '' )
  print ( '  The rank is computed to be %d.' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_LEX_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_lex_rank_test ( )
  timestamp ( )
 
