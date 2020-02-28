#! /usr/bin/env python
#
def partn_successor ( n, nmax, npart, a, rank ):

#*****************************************************************************80
#
## PARTN_SUCCESSOR computes partitions whose largest part is NMAX.
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
#    Input, integer NMAX, the maximum size of any part of the
#    partition.  1 <= NMAX <= N.
#
#    Input/output, integer NPART, the number of parts of the
#    partition.  1 <= NPART <= N.
#
#    Input/output, integer A(N), contains the partition.
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
  import numpy as np
  from partn_sf_check import partn_sf_check
  from sys import exit
  from i4vec_transpose_print import i4vec_transpose_print
#
#  Return the first element.
#
  if ( rank == -1 ):

    npart = n + 1 - nmax
    a[0] = nmax
    for i in range ( 1, npart ):
      a[i] = 1
    rank = 0
    return npart, a, rank
#
#  Check.
#
  check = partn_sf_check ( n, nmax, npart, a )

  if ( not check ):
    print ( '' )
    print ( 'PARTN_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'PARTN_SUCCESSOR - Fatal error!' )
#
#  If there are at least two parts, and the next to last is not NMAX,
#  then rob the last part and pay the next to the last part.
#  Then, if the next to last part is too big, swap it leftwards.
#
  if ( 1 < npart ):

    if ( a[npart-2] < nmax ):

      a[npart-1] = a[npart-1] - 1
      a[npart-2] = a[npart-2] + 1
      index = npart - 1

      while ( True ):

        if ( index <= 1 ):
          break

        if ( a[index-1] <= a[index-2] ):
          break

        temp       = a[index-2]
        a[index-2] = a[index-1]
        a[index-1] = temp

        index = index - 1
#
#  Sum the tail.
#
      temp = 0
      for i in range ( index, npart ):
        temp = temp + a[i]
        a[i] = 0
      temp = int ( temp )
#
#  Spread the sum as 1's.
#
      npart = index + temp
      for i in range ( index, npart ):
        a[i] = 1
      rank = rank + 1
      return npart, a, rank
#
#  Otherwise, we've reached the last item.
#  Return the first one.
#
  else:

    npart = n + 1 - nmax
    a[0] = nmax
    for i in range ( 1, npart ):
      a[i] = 1
    rank = 0
    return npart, a, rank

  return npart, a, rank

def partn_successor_test ( ):

#*****************************************************************************80
#
## PARTN_SUCCESSOR_TEST tests PARTN_SUCCESSOR.
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

  n = 11
  nmax = 4

  print ( '' )
  print ( 'PARTN_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PARTN_SUCCESSOR lists partitions of N with maximum element NMAX.' )
  print ( '' )
  print ( '  Here, N = %d' % ( n ) )
  print ( '  NMAX = %d' % ( nmax ) )
  print ( '' )
#
#  List.
#
  npart = 0
  t = np.zeros ( n )
  rank = -1

  while ( True ):

    rank_old = rank

    npart, t, rank = partn_successor ( n, nmax, npart, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( npart, t, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PARTN_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  partn_successor_test ( )
  timestamp ( )
 
