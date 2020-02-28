#! /usr/bin/env python
#
def bal_seq_rank ( n, t ):

#*****************************************************************************80
#
## BAL_SEQ_RANK ranks a balanced sequence.
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
#    Input, integer N, the number of 0's (and 1's) in the sequence.
#    N must be positive.
#
#    Input, integer T(2*N), a balanced sequence.
#
#    Output, integer RANK, the rank of the balanced sequence.
#
  from bal_seq_check import bal_seq_check
  from mountain import mountain
  from sys import exit
#
#  Check.
#
  check = bal_seq_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'BAL_SEQ_RANK - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'BAL_SEQ_RANK - Fatal error!' )

  y = 0
  rank = 0

  for x in range ( 1, 2 * n ):

    if ( t[x-1] == 0 ):
      y = y + 1
    else:
      mxy = mountain ( n, x, y + 1 )
      rank = rank + mxy
      y = y - 1

  return rank

def bal_seq_rank_test ( ):

#*****************************************************************************80
#
## BAL_SEQ_RANK_TEST tests BAL_SEQ_RANK.
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
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'BAL_SEQ_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BAL_SEQ_RANK ranks balanced sequences of N items.' )

  n = 5
  t = np.array ( [ 0, 0, 1, 0, 1, 1, 0, 0, 1, 1 ] )
  rank = bal_seq_rank ( n, t )

  print ( '' )
  print ( '  The element to be ranked is:' )
  i4vec_transpose_print ( 2 * n, t, '' )

  print ( '' )
  print ( '  Computed rank: %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BAL_SEQ_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bal_seq_rank_test ( )
  timestamp ( )
