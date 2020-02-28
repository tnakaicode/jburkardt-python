#! /usr/bin/env python
#
def npart_rsf_lex_unrank ( rank, n, npart ):

#*****************************************************************************80
#
## NPART_RSF_LEX_UNRANK unranks an RSF NPART partition in the lex ordering.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
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
#    Input, integer RANK, the rank of the partition.
#
#    Input, integer N, the integer to be partitioned.
#    N must be positive.
#
#    Input, integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    Output, integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.
#
  import numpy as np
  from npart_enum import npart_enum
  from npart_table import npart_table
  from sys import exit
#
#  Check.
#
  if ( n <= 0 ):
    print ( '' )
    print ( 'NPART_RSF_LEX_UNRANK - Fatal error!' )
    print ( '  The input N is illegal.' )
    exit ( 'NPART_RSF_LEX_UNRANK - Fatal error!' )

  if ( npart < 1 or n < npart ):
    print ( '' )
    print ( 'NPART_RSF_LEX_UNRANK - Fatal error!' )
    print ( '  The input NPART is illegal.' )
    exit ( 'NPART_RSF_LEX_UNRANK - Fatal error!' )

  npartitions = npart_enum ( n, npart )

  if ( rank < 0 or npartitions < rank ):
    print ( '' )
    print ( 'NPART_RSF_LEX_UNRANK - Fatal error!' )
    print ( '  The input rank is illegal.' )
    exit ( 'NPART_RSF_LEX_UNRANK - Fatal error!' )
#
#  Get the table of partitions of N with NPART parts.
#
  p = npart_table ( n, npart )

  a = np.zeros ( npart )
  npartcopy = npart

  while ( 0 < n ):

    if ( rank < p[n-1,npartcopy-1] ):
      a[npart-npartcopy] = a[npart-npartcopy] + 1
      n = n - 1
      npartcopy = npartcopy - 1
    else:
      for i in range ( 0, npartcopy ):
        a[npart-1-i] = a[npart-1-i] + 1
      rank = rank - p[n-1,npartcopy-1]
      n = n - npartcopy

  return a

def npart_rsf_lex_unrank_test ( ):

#*****************************************************************************80
#
## NPART_RSF_LEX_UNRANK_TEST tests NPART_RSF_LEX_UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  npart = 3
  n = 12

  print ( '' )
  print ( 'NPART_RSF_LEX_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NPART_RSF_LEX_UNRANK unranks' )
  print ( '  partitions of N with NPART parts' )
  print ( '  in reverse standard form.' )

  rank = 4

  t = npart_rsf_lex_unrank ( rank, n, npart )

  i4vec_transpose_print ( npart, t, '  The element of rank 4:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'NPART_RSF_LEX_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  npart_rsf_lex_unrank_test ( )
  timestamp ( )
 
