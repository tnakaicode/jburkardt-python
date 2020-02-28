#! /usr/bin/env python
#
def npart_rsf_lex_successor ( n, npart, a, rank ):

#*****************************************************************************80
#
## NPART_RSF_LEX_SUCCESSOR computes the RSF lex successor for NPART partitions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2016
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
#    Input, integer N, the integer to be partitioned.
#    N must be at least 1.
#
#    Input, integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    Input/output, integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#    Input/output, integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  from part_rsf_check import part_rsf_check
  from sys import exit
#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, npart ):
      a[i] = 1
    a[npart-1] = n - ( npart - 1 )
    rank = 0
    return a, rank
#
#  Check.
#
  check = part_rsf_check ( n, npart, a )
  if ( not check ):
    print ( '' )
    print ( 'NPART_RSF_LEX_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'NPART_RSF_LEX_SUCCESSOR - Fatal error!' )
#
#  Find the first index I for which A(NPART+1-I) + 1 < A(NPART).
#
  i = 2

  while ( True ):

    if ( npart < i ):
      break

    if ( a[npart+1-i-1] + 1 < a[npart-1] ):
      break

    i = i + 1
#
#  If no such index, we've reached the end of the line.
#
  if ( i == npart + 1 ):

    for i in range ( 0, npart ):
      a[i] = 1
    a[npart-1] = n - ( npart - 1 )
    rank = 0
    return a, rank
#
#  Otherwise, increment A(NPART+1-I), and adjust other entries.
#
  else:

    a[npart+1-i-1] = a[npart+1-i-1] + 1
    d = - 1

    for j in range ( i - 1, 1, -1 ):
      d = d + a[npart+1-j-1] - a[npart+1-i-1]
      a[npart+1-j-1] = a[npart+1-i-1]

    a[npart-1] = a[npart-1] + d

  rank = rank + 1

  return a, rank

def npart_rsf_lex_successor_test ( ):

#*****************************************************************************80
#
## NPART_RSF_LEX_SUCCESSOR_TEST tests NPART_RSF_LEX_SUCCESSOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  npart = 3
  n = 12

  print ( '' )
  print ( 'NPART_RSF_LEX_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NPART_RSF_LEX_SUCCESSOR lists' )
  print ( '  partitions of N with NPART parts' )
  print ( '  in reverse standard form.' )
  print ( '' )

  t = np.zeros ( npart )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = npart_rsf_lex_successor ( n, npart, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( npart, t, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'NPART_RSF_LEX_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  npart_rsf_lex_successor_test ( )
  timestamp ( )
 

