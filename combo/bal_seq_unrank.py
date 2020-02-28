#! /usr/bin/env python
#
def bal_seq_unrank ( rank, n ):

#*****************************************************************************80
#
## BAL_SEQ_UNRANK unranks a balanced sequence.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2015
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
#    Input, integer RANK, the rank of the balanced sequence.
#
#    Input, integer N, the number of 0's (and 1's) in the sequence.
#
#    Output, integer T(2*N), a balanced sequence.
#
#    Output, 
#
  import numpy as np
  from bal_seq_enum import bal_seq_enum
  from mountain import mountain
  from sys import exit
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'BAL_SEQ_UNRANK - Fatal error!' )
    print ( '  Input N is illegal.' )
    error ( 'BAL_SEQ_UNRANK - Fatal error!' )

  nseq = bal_seq_enum ( n )

  if ( rank < 0 or nseq < rank ):
    print ( '' )
    print ( 'BAL_SEQ_UNRANK - Fatal error!' )
    print ( '  The input rank is illegal.' )
    exit ( 'BAL_SEQ_UNRANK - Fatal error!' )

  y = 0
  low = 0

  t = np.zeros ( 2 * n, dtype = np.int32 )

  for x in range ( 1, 2 * n + 1 ):

    m = mountain ( n, x, y + 1 )

    if ( rank <= low + m - 1 ):
      y = y + 1
      t[x-1] = 0
    else:
      low = low + m
      y = y - 1
      t[x-1] = 1

  return t

def bal_seq_unrank_test ( ):

#*****************************************************************************80
#
## BAL_SEQ_UNRANK_TEST tests BAL_SEQ_UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'BAL_SEQ_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BAL_SEQ_UNRANK unranks a balanced sequence of N items.' )

  rank = 21
  n = 5

  t = bal_seq_unrank ( rank, n )

  print ( '' )
  print ( '  Rank = %d' % ( rank ) )
  print ( '' )
  print ( '  The element of that rank is:' )
  i4vec_transpose_print ( 2 * n, t, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BAL_SEQ_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bal_seq_unrank_test ( )
  timestamp ( )
