#! /usr/bin/env python
#
def subsetsum_swap ( n, a, sum_desired ):

#*****************************************************************************80
#
## SUBSETSUM_SWAP seeks a solution of the subset sum problem by swapping.
#
#  Discussion:
#
#    Given a collection of N not necessarily distinct positive integers A(I),
#    and a positive integer SUM_DESIRED, select a subset of the values so that
#    their sum is as close as possible to SUM_DESIRED without exceeding it.
#
#  Algorithm:
#
#    Start with no values selected, and SUM_ACHIEVED = 0.
#
#    Consider each element A(I):
#
#      If A(I) is not selected and SUM_ACHIEVED + A(I) <= SUM_DESIRED,
#        select A(I).
#
#      If A(I) is still not selected, and there is a selected A(J)
#      such that SUM_GOT < SUM_ACHIEVED + A(I) - A(J),
#        select A(I) and deselect A(J).
#
#      If no items were selected on this sweep,
#        exit.
#      Otherwise,
#        repeat the search.
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
#    Input, integer N, the number of values.  N must be positive.
#
#    Input/output, integer A(N), a collection of positive values.
#    On output, A has been sorted into descending order.
#
#    Input, integer SUM_DESIRED, the desired sum.
#
#    Output, integer INDEX(N) INDEX(I) is 1 if A(I) is part of the
#    sum, and 0 otherwise.
#
#    Output, integer SUM_ACHIEVED, the sum of the selected
#    elements.
#
  import numpy as np
  from i4vec_sort_insert_d import i4vec_sort_insert_d
#
#  Initialize.
#
  sum_achieved = 0

  index = np.zeros ( n )
#
#  Sort into descending order.
#
  a = i4vec_sort_insert_d ( n, a )

  while ( True ):

    nmove = 0

    for i in range ( 0, n ):

      if ( index[i] == 0 ):

        if ( sum_achieved + a[i] <= sum_desired ):
          index[i] = 1
          sum_achieved = sum_achieved + a[i]
          nmove = nmove + 1
          continue

      if ( index[i] == 0 ):

        for j in range ( 0, n ):

          if ( index[j] == 1 ):

            if ( sum_achieved < sum_achieved + a[i] - a[j] and \
              sum_achieved + a[i] - a[j] <= sum_desired ):
              index[j] = 0
              index[i] = 1
              nmove = nmove + 2
              sum_achieved = sum_achieved + a[i] - a[j]
              break

    if ( nmove <= 0 ):
      break

  return a, index, sum_achieved

def subsetsum_swap_test ( ):

#*****************************************************************************80
#
## SUBSETSUM_SWAP_TEST tests SUBSETSUM_SWAP.
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

  n = 7

  sum_desired = 17

  print ( '' )
  print ( 'SUBSETSUM_SWAP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSETSUM_SWAP seeks a solution of the subset' )
  print ( '  sum problem using pair swapping.' )
  print ( '' )
  print ( '  The desired sum is %d' % ( sum_desired ) )

  a = np.array ( [ 12, 8, 11, 30, 8, 3, 7 ] )

  a, index, sum_achieved = subsetsum_swap ( n, a, sum_desired )

  print ( '' )
  print ( '    A(I), INDEX(I)' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %5d  %5d' % ( a[i], index[i] ) )

  print ( '' )
  print ( '  The achieved sum is %d' % ( sum_achieved ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSETSUM_SWAP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subsetsum_swap_test ( )
  timestamp ( )
 
