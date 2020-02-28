#! /usr/bin/env python
#
def part_successor ( n, npart, a, rank ):

#*****************************************************************************80
#
## PART_SUCCESSOR computes the lexicographic partition successor.
#
#  Discussion:
#
#    PART_SUCCESSOR is "inspired by" the GenPartitions algorithm,
#    but instead of relying on recursion, generates the partitions
#    one at a time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
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
  from part_sf_check import part_sf_check
  from sys import exit
#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, n ):
      a[i] = 1
    npart = n
    rank = 0
    return npart, a, rank
#
#  Check.
#
  check = part_sf_check ( n, npart, a )

  if ( not check ):
    print ( '' )
    print ( 'PART_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'PART_SUCCESSOR - Fatal error!' )
#
#  If possible, increment the first intermediate position that
#  is less than its left hand neighbor, and has at least one
#  right hand neighbor.
#
  ihi = npart - 1

  for i in range ( ihi - 1, 0, -1 ):

    if ( a[i] < a[i-1] ):
      asum = 0
      for j in range ( i + 1, npart ):
        asum = asum + a[j]
      asum = asum - 1
      a[i] = a[i] + 1
      for j in range ( i + 1, npart ):
        a[j] = 0
      npart = int ( i + 1 + asum )
      for j in range ( i + 1, npart ):
        a[j] = 1
      rank = rank + 1
      return npart, a, rank
#
#  A) there are two or more parts
#  Increment the first, replace the rest by 1's.
#
  if ( 2 <= npart ):
    a[0] = a[0] + 1
    for i in range ( 1, npart ):
      a[i] = 0
    npart = int ( n - a[0] + 1 )
    for i in range ( 1, npart ):
      a[i] = 1
    rank = rank + 1
#
#  B) there is only one part.
#  We've reached the last item.
#  Return the first one.
#
  elif ( npart == 1 ):
    for i in range ( 0, n ):
      a[i] = 1
    npart = n
    rank = 0

  return npart, a, rank

def part_successor_test ( ):

#*****************************************************************************80
#
## PART_SUCCESSOR_TEST tests PART_SUCCESSOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 8

  print ( '' )
  print ( 'PART_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PART_SUCCESSOR produces partitions of N,' )
  print ( '' )
  print ( '  Partitions of N = %d' % ( n ) )
  print ( '' )
#
#  List.
#
  npart = 0
  t = np.zeros ( n )
  rank = -1

  while ( True ):

    rank_old = rank

    npart, t, rank = part_successor ( n, npart, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( npart, t, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PART_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  part_successor_test ( )
  timestamp ( )
 
