#! /usr/bin/env python
#
def subset_colex_successor ( n, t, rank ):

#*****************************************************************************80
#
## SUBSET_COLEX_SUCCESSOR computes the subset colexicographic successor.
#
#  Discussion:
#
#    In the original code, there is a last element with no successor.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
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
#    Input, integer N, the number of elements in the master set.
#    N must be positive.
#
#    Input/output, integer T(N), describes a subset.  T(I) is 0 if
#    the I-th element of the master set is not in the subset, and is
#    1 if the I-th element is part of the subset.
#    On input, T describes a subset.
#    On output, T describes the next subset in the ordering.
#    If the input T was the last in the ordering, then the output T
#    will be the first.
#
#    Input/output, integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  from subset_check import subset_check
  from sys import exit
#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, n ):
      t[i] = 0
    rank = 0
    return t, rank
#
#  Check.
#
  check = subset_check ( n, t );

  if ( not check ):
    print ( '' )
    print ( 'SUBSET_COLEX_SUCCESSOR - Fatal error!' )
    print ( '  The subset is not legal.' )
    exit ( 'SUBSET_COLEX_SUCCESSOR - Fatal error!\n' )

  for i in range ( 0, n ):

    if ( t[i] == 0 ):
      t[i] = 1
      rank = rank + 1
      return t, rank
    else:
      t[i] = 0

  rank = 0

  return t, rank

def subset_colex_successor_test ( ):

#*****************************************************************************80
#
## SUBSET_COLEX_SUCCESSOR_TEST tests SUBSET_COLEX_SUCCESSOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 5

  print ( '' )
  print ( 'SUBSET_COLEX_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_COLEX_SUCCESSOR lists subsets of a set,' )
  print ( '  using the colexicographic ordering.' )

  t = np.zeros ( n )
  rank = -1

  while ( True ):

    rank_old = rank

    t, rank = subset_colex_successor ( n, t, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( n, t, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_COLEX_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_colex_successor_test ( )
  timestamp ( )
 
