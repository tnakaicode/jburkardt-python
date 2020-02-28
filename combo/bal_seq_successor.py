#! /usr/bin/env python
#
def bal_seq_successor ( n, t, rank ):

#*****************************************************************************80
#
## BAL_SEQ_SUCCESSOR computes the lexical balanced sequence successor.
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
#    Input, integer N, the number of 0's (and 1's) in the sequence.
#    N must be positive.
#
#    Input/output, integer T(2*N), on input, a balanced sequence,
#    and on output, its lexical successor.
#
#    Input/output, integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  from bal_seq_check import bal_seq_check
  from sys import exit
#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, n ):
      t[i] = 0
    for i in range ( n, 2 * n ):
      t[i] = 1
    rank = 0
    return t, rank
#
#  Check.
#
  check = bal_seq_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'BAL_SEQ_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'BAL_SEQ_SUCCESSOR - Fatal error!' )
#
#  After the I-th 0 there is a 'slot' with the capacity to
#  hold between 0 and I ones.
#
#  The first element of the sequence has all the 1's cowering
#  behind the N-th 0.
#
#  We seek to move a 1 to the left, and to do it lexically,
#  we will move a 1 to the rightmost slot that is under capacity.
#
#  Find the slot.
#
  slot = 0
  slot_index = 0
  slot_ones = 0

  open = 0
  open_index = 0

  for i in range ( 1, 2 * n + 1 ):

    if ( t[i-1] == 0 ):

      if ( 0 < slot ):
        if ( slot_ones < slot ):
          open = slot
          open_index = slot_index

      slot = slot + 1
      slot_index = i

    else:

      slot_ones = slot_ones + 1
#
#  If OPEN is not 0, then preserve the string up to the OPEN-th 0,
#  preserve the 1's that follow, but then write a 1, then
#  all the remaining 0's and all the remaining 1's.
#
  if ( open != 0 ):

    j = open_index + 1

    while ( t[j-1] == 1 ):
      j = j + 1

    t[j-1] = 1

    for i in range ( open + 1, n + 1 ):
      j = j + 1
      t[j-1] = 0

    for i in range ( j + 1, 2 * n + 1 ):
      t[i-1] = 1
#
#  If OPEN is 0, the last element was input.
#  Return the first one.
#
  else:

    for i in range ( 0, n ):
      t[i] = 0
    for i in range ( n, 2 * n ):
      t[i] = 1
    rank = 0
    return t, rank

  rank = rank + 1

  return t, rank

def bal_seq_successor_test ( ):

#*****************************************************************************80
#
## BAL_SEQ_SUCCESSOR_TEST tests BAL_SEQ_SUCCESSOR.
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

  print ( '' )
  print ( 'BAL_SEQ_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BAL_SEQ_SUCCESSOR lists balanced sequences of N items, one at a time.' )

  n = 5
  t = np.zeros ( 2 * n )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = bal_seq_successor ( n, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( 2 * n, t, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BAL_SEQ_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bal_seq_successor_test ( )
  timestamp ( )

