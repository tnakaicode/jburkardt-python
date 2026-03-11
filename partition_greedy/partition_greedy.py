#! /usr/bin/env python3
#
def partition_greedy ( w ):

#*****************************************************************************80
#
## partition_greedy() approaches the partition problem using a greedy algorithm.
#
#  Discussion:
#
#    We are given a set of N integers W.
#
#    We seek to partition W into subsets such that the subsets
#    have sums that are equal, or else as nearly equal as possible.
#
#    The "discrepancy" is the absolute value of the difference between the
#    two sums, and will be zero if we have solved the problem.
#
#    For a given set of integers, there may be zero, one, or many solutions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer W(N), the integers.
#
#  Output:
#
#    integer X(N), indicates the proposed solution.
#    X(I) is 0 for items in set 0 and 1 for items in set 1.
#
  import numpy as np

  n = len ( w )

  index = np.argsort ( w )
  x = np.zeros ( n, dtype = int )

  s0_sum = 0.0
  s1_sum = 0.0
  for i in range ( n - 1, -1, -1 ):
    j = index[i]
    if ( s0_sum < s1_sum ):
      x[j] = 0
      s0_sum = s0_sum + w[j]
    else:
      x[j] = 1
      s1_sum = s1_sum + w[j]

  return x

def partition_greedy_test01 ( w ):

#*****************************************************************************80
#
## partition_greedy_test01() tests partition_greedy() on particular data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer W(N), a set of weights.
#
  print ( '' )
  print ( 'partition_greedy_test01():' )
  print ( '  partition_greedy() seeks a balanced partition using a greedy method.' )
  print ( '  Partition a set of N integers W so that the subsets' )
  print ( '  have equal sums.' )

  x = partition_greedy ( w )

  print ( '' )
  print ( '     I        W0        W1' )
  print ( '' )
  n = len ( w )
  w0_sum = 0
  w1_sum = 0
  for i in range ( 0, n ):
    if ( x[i] == 0 ):
      w0_sum = w0_sum + w[i]
      print ( '  %4d  %8d' % ( i, w[i] ) )
    else:
      w1_sum = w1_sum + w[i]
      print ( '  %4d            %8d' % ( i, w[i] ) )
  print ( '        --------  --------' )
  print ( '        %8d  %8d' % ( w0_sum, w1_sum ) )
  print ( '' )
  print ( '  Discrepancy = ', w1_sum - w0_sum )

  return

def partition_greedy_test ( ):

#*****************************************************************************80
#
## partition_greedy_test() tests partition_greedy().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'partition_greedy_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test partition_greedy().' )

  test_num = 6
#
#  Find individual solutions.
#
  for test in range ( 0, test_num ):

    if ( test == 0 ):
      w = np.array ( [ 19, 17, 13, 9, 6 ] )
    elif ( test == 1 ):
      w = np.array ( [ 484, 114, 205, 288, 506, 503, 201, 127, 410 ] )
    elif ( test == 2 ):
      w = np.array ( [ 771, 121, 281, 854, 885, 734, 486, 1003, 83, 62 ] )
    elif ( test == 3 ):
      w = np.array ( [ 2, 10, 3, 8, 5, 7, 9, 5, 3, 2 ] )
    elif ( test == 4 ):
      w = np.array ( [ 3, 4, 3, 1, 3, 2, 3, 2, 1 ] )
    elif ( test == 5 ):
      w = np.array ( [ 8, 7, 6, 5, 4 ] )

    partition_greedy_test01 ( w )
#
#  Terminate.
#
  print ( '' )
  print ( 'partition_greedy_test():' )
  print ( '  Normal end of execution.' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == "__main__" ):
  timestamp ( )
  partition_greedy_test ( )
  timestamp ( )

