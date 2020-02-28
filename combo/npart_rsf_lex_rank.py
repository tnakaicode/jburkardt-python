#! /usr/bin/env python
#
def npart_rsf_lex_rank ( n, npart, a ):

#*****************************************************************************80
#
## NPART_RSF_LEX_RANK computes the lex rank of an RSF NPART partition.
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
#    Input, integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
#    Output, integer RANK, the rank of the partition.
#
  from i4vec_reverse import i4vec_reverse
  from npart_table import npart_table
  from part_rsf_check import part_rsf_check
  from sys import exit
#
#  Check.
#
  check = part_rsf_check ( n, npart, a )

  if ( not check ):
    print ( '' )
    print ( 'NPART_RSF_LEX_RANK - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'NPART_RSF_LEX_RANK - Fatal error!' )
#
#  Get the table of partitions of N with NPART parts.
#
  p = npart_table ( n, npart )
#
#  Copy the partition "backwards".
#
  b = i4vec_reverse ( npart, a )

  rank = 0

  while ( 0 < n and 0 < npart ):

    if ( b[npart-1] == 1 ):

      n = n - 1
      npart = npart - 1

    else:

      for i in range ( 0, npart ):
        b[i] = b[i] - 1
      rank = rank + p[n-1,npart-1]
      n = n - npart

  return rank

def npart_rsf_lex_rank_test ( ):

#*****************************************************************************80
#
## NPART_RSF_LEX_RANK_TEST tests NPART_RSF_LEX_RANK.
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

  npart = 3
  n = 12

  print ( '' )
  print ( 'NPART_RSF_LEX_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NPART_RSF_LEX_RANK ranks partitions of N with NPART parts' )
  print ( '  in reverse standard form.' )

  t = np.array ( [ 1, 5, 6 ] )
  i4vec_transpose_print ( npart, t, '  Element:' )

  rank = npart_rsf_lex_rank ( n, npart, t )

  print ( '' )
  print ( '  The rank of the element is computed as %d:' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NPART_RSF_LEX_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  npart_rsf_lex_rank_test ( )
  timestamp ( )
 
