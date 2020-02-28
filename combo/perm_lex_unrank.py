#! /usr/bin/env python
#
def perm_lex_unrank ( rank, n ):

#*****************************************************************************80
#
## PERM_LEX_UNRANK computes the permutation of given lexicographic rank.
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
#    Input, integer RANK, the rank of the permutation.
#
#    Input, integer N, the number of values being permuted.
#    N must be positive.
#
#    Output, integer P(N), describes the permutation.
#
  import numpy as np
  from i4_factorial import i4_factorial
  from perm_enum import perm_enum
  from sys import exit
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'PERM_LEX_UNRANK - Fatal error!' )
    print ( '  Input N is illegal.' )
    exit ( 'PERM_LEX_UNRANK - Fatal error!' )

  nperm = perm_enum ( n )

  if ( rank < 0 or nperm < rank ):
    print ( '' )
    print ( 'PERM_LEX_UNRANK - Fatal error!' )
    print ( '  The input rank is illegal.' )
    exit ( 'PERM_LEX_UNRANK - Fatal error!' )

  p = np.zeros ( n )

  p[n-1] = 1

  for j in range ( 1, n ):

    d = ( rank % i4_factorial ( j + 1 ) ) // i4_factorial ( j )
    rank = rank - d * i4_factorial ( j )
    p[n-1-j] = d + 1

    for i in range ( n - j, n ):

      if ( d < p[i] ):
        p[i] = p[i] + 1

  return p

def perm_lex_unrank_test ( ):

#*****************************************************************************80
#
## PERM_LEX_UNRANK_TEST tests PERM_LEX_UNRANK.
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
  import platform
  from perm_print import perm_print

  n = 4

  print ( '' )
  print ( 'PERM_LEX_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_LEX_UNRANK unranks' )
  print ( '  permutations using the lexicographic ordering.' )

  rank = 12

  p = perm_lex_unrank ( rank, n )

  perm_print ( n, p, '  The element of rank 12:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_LEX_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_lex_unrank_test ( )
  timestamp ( )
 
