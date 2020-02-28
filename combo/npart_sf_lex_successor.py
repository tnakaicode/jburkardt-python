#! /usr/bin/env python
#
def npart_sf_lex_successor ( n, npart, a, rank ):

#*****************************************************************************80
#
## NPART_SF_LEX_SUCCESSOR computes SF NPART partition.
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
#    N must be positive.
#
#    Input, integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    Input/output, integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.  The values in A must be in DESCENDING order.
#
#    Input/output, integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  from i4vec_part2 import i4vec_part2
  from part_sf_check import part_sf_check
  from sys import exit
#
#  Return the first element.
#
  if ( rank == -1 ):
    a = i4vec_part2 ( n, npart )
    rank = 0
    return a, rank
#
#  Check.
#
  check = part_sf_check ( n, npart, a )

  if ( not check ):
    print ( '' )
    print ( 'NPART_SF_LEX_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'NPART_SF_LEX_SUCCESSOR - Fatal error!' )
#
#  Find the last entry that is 2 or more.
#
  for i in range ( npart - 1, -1, -1 ):
    if ( 1 < a[i] ):
      indx = i
      break
#
#  As long as the last nonunit occurs after the first position,
#  have it donate 1 to the left.
#
  if ( 0 < indx ):

    a[indx] = a[indx] - 1
    a[indx-1] = a[indx-1] + 1
    indx = indx - 1

    while ( True ):

      if ( indx <= 0 ):
        break

      if ( a[indx] <= a[indx-1] ):
        break

      temp      = a[indx]
      a[indx]   = a[indx-1]
      a[indx-1] = temp

      indx = indx - 1
#
#  Sum the tail.
#
    temp = 0
    for i in range ( indx + 1, npart ):
      temp = temp + a[i]
      a[i] = 0
    temp = int ( temp )
#
#  Partition the tail sum equally over the tail.
#
    j = 0
    for i in range ( 0, temp ):
      a[indx+1+j] = a[indx+1+j] + 1
      j = j + 1
      if ( npart - indx - 1 <= j ):
        j = 0

    rank = rank + 1
#
#  If A(2) through A(NPART) are 1, then this is the last element.
#  Return the first one.
#
  else:

    a = i4vec_part2 ( n, npart )
    rank = 0

  return a, rank

def npart_sf_lex_successor_test ( ):

#*****************************************************************************80
#
## NPART_SF_LEX_SUCCESSOR_TEST tests NPART_SF_LEX_SUCCESSOR
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
  from npart_enum import npart_enum

  npart = 3
  n = 12

  print ( '' )
  print ( 'NPART_SF_LEX_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NPART_SF_LEX_SUCCESSOR lists' )
  print ( '  Partitions of N with NPART parts' )
  print ( '  in standard form.' )

  npartitions = npart_enum ( n, npart )

  print ( '' )
  print ( '  For N = %d' % ( n ) )
  print ( '  and NPART = %d' % ( npart ) )
  print ( '  the number of partitions is %d' % ( npartitions ) )
  print ( '' )
#
#  List.
#
  t = np.zeros ( npart )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = npart_sf_lex_successor ( n, npart, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( npart, t, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'NPART_SF_LEX_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  npart_sf_lex_successor_test ( )
  timestamp ( )
 
