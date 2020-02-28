#! /usr/bin/env python
#
def partition_greedy ( n, a ):

#*****************************************************************************80
#
## PARTITION_GREEDY attacks the partition problem with a greedy algorithm.
#
#  Discussion:
#
#    Given a collection of N not necessarily distinct positive integers A(I),
#    it is desired to partition the values into two groups, whose sums are
#    as close as possible.
#
#  Algorithm:
#
#    Begin with sets 1 and 2 empty.
#
#    Process the data in descending order of magnitude.
#
#    The next item A(I) is added to set 1 or set 2, whichever has the
#    smallest current sum.
#
#    Stop as soon as all items have been allocated.
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
#    Brian Hayes,
#    The Easiest Hard Problem,
#    American Scientist,
#    Volume 90, Number 2, March-April 2002, pages 113-117.
#
#  Parameters:
#
#    Input, integer N, the number of values.  N must be positive.
#
#    Input/output, integer A(N), a collection of positive values.
#    On output, A has been sorted into descending order.
#
#    Output, integer INDX(N), is 0 if A(I) is part of
#    set 0, and 1 if it is assigned to set 1.
#
  import numpy as np
  from i4vec_sort_insert_d import i4vec_sort_insert_d

  sums = np.zeros ( 2 )
  indx = np.zeros ( n )

  a = i4vec_sort_insert_d ( n, a )

  for i in range ( 0, n ):

    if ( sums[0] < sums[1] ):
      j = 0
    else:
      j = 1

    indx[i] = j
    sums[j] = sums[j] + a[i]

  return a, indx

def partition_greedy_test ( ):

#*****************************************************************************80
#
## PARTITION_GREEDY_TEST tests PARTITION_GREEDY.
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

  n = 10

  print ( '' )
  print ( 'PARTITION_GREEDY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PARTITION_GREEDY partitions an integer vector into' )
  print ( '  two subsets with nearly equal sum.' )

  for test in range ( 0, 2 ):

    if ( test == 0 ):
      a = np.array ( [ 2, 10, 3, 8, 5, 7, 9, 5, 3, 2 ] )
    elif ( test == 1 ):
      a = np.array ( [ 771, 121, 281, 854, 885, 734, 486, 1003, 83, 62 ] )

    a, indx = partition_greedy ( n, a )

    print ( '' )
    print ( '  Data set #%d partitioned:' % ( test ) )
    print ( '' )

    sums = np.zeros ( 2 )

    for i in range ( 0, n ):

      if ( indx[i] == 0 ):
        sums[0] = sums[0] + a[i]
        print ( '  %4d' % ( a[i] ) )
      else:
        print ( '        %4d' % ( a[i] ) )
        sums[1] = sums[1] + a[i]

    print ( '' )
    print ( '  Sums:' )
    print ( '' )
    print ( '  %4d  %4d' % ( sums[0], sums[1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PARTITION_GREEDY_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  partition_greedy_test ( )
  timestamp ( )
 
