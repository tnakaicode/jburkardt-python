#! /usr/bin/env python
#
def ksubset_lex_successor ( k, n, t, rank ):

#*****************************************************************************80
#
## KSUBSET_LEX_SUCCESSOR computes the K subset lexicographic successor.
#
#  Discussion:
#
#    In the original code, there is a last element with no successor.
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
#    have. 1 <= K <= N.
#
#    Input, integer N, the number of elements in the master set.
#    N must be positive.
#
#    Input/output, integer T(K), describes a K subset.  T(I) is
#    the I-th element.  The elements must be listed in ascending order.
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
  if ( rank == -1 ):
    for i in range ( 0, k ):
      t[i] = i + 1
    rank = 0
    return t, rank
#
#  Check.
#
  check = ksubset_lex_check ( k, n, t )

  if ( not check ):
    print ( '' )
    print ( 'KSUBSET_LEX_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'KSUBSET_LEX_SUCCESSOR - Fatal error!' )

  isave = -1

  for i in range ( k, 0, -1 ):
    if ( t[i-1] != n - k + i ):
      isave = i
      break
#
#  The last K subset was input.
#  Return the first one.
#
  if ( isave == -1 ):

    for i in range ( 0, k ):
      t[i] = i + 1
    rank = 0

  else:

    for j in range ( k, isave - 1, -1 ):
      t[j-1] = t[isave-1] + 1 + j - isave

    rank = rank + 1

  return t, rank

def ksubset_lex_successor_test ( ):

#*****************************************************************************80
#
## KSUBSET_LEX_SUCCESSOR_TEST tests KSUBSET_LEX_SUCCESSOR.
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
  print ( 'KSUBSET_LEX_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUBSET_LEX_SUCCESSOR lists K-subsets of an N set,' )
  print ( '  using the lexicographic ordering.' )

  t = np.zeros ( k )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = ksubset_lex_successor ( k, n, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( k, t, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUBSET_LEX_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksubset_lex_successor_test ( )
  timestamp ( )
 
