#! /usr/bin/env python
#
def part_sf_conjugate ( n, npart, a ):

#*****************************************************************************80
#
## PART_SF_CONJUGATE computes the conjugate of a partition.
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
#    Input, integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    Input, integer A(N), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#    Output, integer NPART2, the number of parts of the conjugate
#    partition.
#
#    Output, integer B(N), contains the conjugate partition.
#
  import numpy as np
  from part_sf_check import part_sf_check
  from sys import exit
#
#  Check.
#
  check = part_sf_check ( n, npart, a )

  if ( not check ):
    print ( '' )
    print ( 'PART_SF_CONJUGATE - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'PART_SF_CONJUGATE - Fatal error!' )

  npart2 = a[0]
  b = np.zeros ( npart2, dtype = np.int32 )

  for i in range ( 0, npart ):
    for j in range ( 0, a[i] ):
      b[j] = b[j] + 1

  return npart2, b

def part_sf_conjugate_test ( ):

#*****************************************************************************80
#
## PART_SF_CONJUGATE_TEST tests PART_SF_CONJUGATE.
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
  from part_successor import part_successor

  n = 8

  print ( '' )
  print ( 'PART_SF_CONJUGATE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PART_SF_CONJUGATE produces the conjugate of a partition.' )
  print ( '' )
  print ( '  Partitions of N = %d' % ( n ) )

#
#  List.
#
  npart = 0
  t = np.zeros ( n, dtype = np.int32 )
  rank = -1

  while ( True ):

    rank_old = rank

    npart, t, rank = part_successor ( n, npart, t, rank )

    if ( rank <= rank_old ):
      break

    print ( '' )
    print ( '  %d' % ( rank ) )
    i4vec_transpose_print ( npart, t, '' )

    npartb, b = part_sf_conjugate ( n, npart, t )

    i4vec_transpose_print ( npartb, b, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PART_SF_CONJUGATE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  part_sf_conjugate_test ( )
  timestamp ( )
 
