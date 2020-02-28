#! /usr/bin/env python
#
def perm_tj_unrank ( rank, n ):

#*****************************************************************************80
#
## PERM_TJ_UNRANK computes the permutation of given Trotter-Johnson rank.
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
    print ( 'PERM_TJ_UNRANK - Fatal error!' )
    print ( '  Input N is illegal.' )
    exit ( 'PERM_TJ_UNRANK - Fatal error!' )

  nperm = perm_enum ( n )

  if ( rank < 0 or nperm < rank ):
    print ( '' )
    print ( 'PERM_TJ_UNRANK - Fatal error!' )
    print ( '  The input rank is illegal.' )
    exit ( 'PERM_TJ_UNRANK - Fatal error!' )

  p = np.zeros ( n, dtype = np.int32 )

  p[0] = 1
  r2 = 0

  for j in range ( 2, n + 1 ):
#
#  Replace this ratio of factorials!
#
    r1 = ( rank * i4_factorial ( j ) ) // i4_factorial ( n )
    k = r1 - j * r2

    if ( ( r2 % 2 ) == 0 ):
      jhi = j - k
    else:
      jhi = k + 1

    for i in range ( j - 1, jhi - 1, -1 ):
      p[i] = p[i-1]
    p[jhi-1] = j

    r2 = r1

  return p

def perm_tj_unrank_test ( ):

#*****************************************************************************80
#
## PERM_TJ_UNRANK_TEST tests PERM_TJ_UNRANK.
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
  print ( 'PERM_TJ_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_TJ_UNRANK unranks' )
  print ( '  permutations using the Trotter-Johnson ordering.' )

  rank = 12

  p = perm_tj_unrank ( rank, n )

  perm_print ( n, p, '  The element of rank 12:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_TJ_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_tj_unrank_test ( )
  timestamp ( )

