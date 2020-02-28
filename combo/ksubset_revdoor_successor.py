#! /usr/bin/env python
#
def ksubset_revdoor_successor ( k, n, t, rank ):

#*****************************************************************************80
#
#% KSUBSET_REVDOOR_SUCCESSOR computes the K subset revolving door successor.
#
#  Discussion:
#
#    After numerous attempts to implement the algorithm published in
#    Kreher and Stinson, the Nijenhuis and Wilf version was implemented
#    instead.  The K and S algorithm is supposedly based on the N and W one.
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
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms for Computers and Calculators,
#    Second Edition,
#    Academic Press, 1978,
#    ISBN: 0-12-519260-6,
#    LC: QA164.N54.
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
#    Input/output, integer T(K), describes a K subset.  T(I) is the
#    I-th element.  The elements must be listed in ascending order.
#    On input, T describes a K subset.
#    On output, T describes the next K subset in the ordering.
#    If the input T was the last in the ordering, then the output T
#    will be the first.
#
#    Input/output, integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  from ksubset_lex_check import ksubset_lex_check
  from sys import exit
#
#  Return the first element.
#
  if ( rank == - 1 ):
    for i in range ( 0, k ):
      t [i] = i + 1
    rank = 0
    return t, rank
#
#  Check.
#
  check = ksubset_lex_check ( k, n, t )

  if ( not check ):
    print ( '' )
    print ( 'KSUBSET_REVDOOR_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'KSUBSET_RECDOOR_SUCCESSOR - Fatal error!' )

  j = 0

  while ( True ):

    if ( 0 < j or ( k % 2 ) == 0 ):

      j = j + 1

      if ( k < j ):
        t[k-1] = k
        rank = 0
        return t, rank

      if ( t[j-1] != j ):

        t[j-1] = t[j-1] - 1

        if ( j != 1 ):
          t[j-2] = j - 1

        rank = rank + 1
        return t, rank

    j = j + 1

    if ( j < k ):
      if ( t[j-1] != t[j] - 1 ):
        break
    else:
      if ( t[j-1] != n ):
        break

  t[j-1] = t[j-1] + 1

  if ( j != 1 ):
    t[j-2] = t[j-1] - 1

  rank = rank + 1

  return t, rank

def ksubset_revdoor_successor_test ( ):

#*****************************************************************************80
#
## KSUBSET_REVDOOR_SUCCESSOR_TEST tests KSUBSET_REVDOOR_?.
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
  print ( 'KSUBSET_REVDOOR_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUBSET_REVDOOR_SUCCESSOR lists K-subsets of an N set' )
  print ( '  using the revolving door ordering.' )
  print ( '' )

  t = np.zeros ( k )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = ksubset_revdoor_successor ( k, n, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( k, t, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUBSET_REVDOOR_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksubset_revdoor_successor_test ( )
  timestamp ( )
 
