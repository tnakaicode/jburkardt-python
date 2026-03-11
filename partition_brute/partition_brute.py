#! /usr/bin/env python3
#
def partition_brute ( n, w ):

#*****************************************************************************80
#
## partition_brute() approaches the partition problem using brute force.
#
#  Discussion:
#
#    We are given a set of N integers W.
#
#    We seek to partition W into subsets W0 and W1, such that the subsets
#    have equal sums.
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
#    10 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the set.
#
#    integer W(N), the integers.
#
#  Output:
#
#    bool C(N), indicates the proposed solution.
#    C(I) is True or False if weight I is or is not in the left set of the
#    partition.
#
#    integer DISCREPANCY, the discrepancy.
#
  import numpy as np

  w_sum = np.sum ( w )

  c = np.zeros ( n, dtype = np.int32 )
  discrepancy = w_sum

  d = np.zeros ( n, dtype = np.int32 )

  rank = -1

  while ( True ):

    d, rank = subset_next ( n, d, rank )

    if ( rank == -1 ):
      break

    p_sum = 0
    for i in range ( 0, n ):
      if ( d[i] ):
        p_sum = p_sum + w[i]

    d_discrepancy = abs ( w_sum - 2 * p_sum )

    if ( d_discrepancy < discrepancy ):
      discrepancy = d_discrepancy
      for i in range ( 0, n ):
        c[i] = d[i]

    if ( discrepancy == 0 ):
      break

  return c, discrepancy

def partition_brute_test01 ( n, w ):

#*****************************************************************************80
#
## partition_brute_test01() tests partition_brute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of weights.
#
#    integer W(N), a set of weights.
#
  print ( '' )
  print ( 'partition_brute_test01():' )
  print ( '  partition_brute() seeks a balanced partition using brute force.' )
  print ( '  Partition a set of N integers W so that the subsets' )
  print ( '  have equal sums.' )

  c, discrepancy = partition_brute ( n, w )

  print ( '' )
  print ( '     I        W0        W1' )
  print ( '' )
  w0_sum = 0
  w1_sum = 0
  for i in range ( 0, n ):
    if ( c[i] ):
      w0_sum = w0_sum + w[i]
      print ( '  %4d  %8d' % ( i, w[i] ) )
    else:
      w1_sum = w1_sum + w[i]
      print ( '  %4d            %8d' % ( i, w[i] ) )

  print ( '        --------  --------' )
  print ( '        %8d  %8d' % ( w0_sum, w1_sum ) )
  print ( '' )
  print ( '  Discrepancy = %d' % ( discrepancy ) )

  return

def partition_count ( n, w ):

#*****************************************************************************80
#
## partition_count() counts the solutions to a partition problem.
#
#  Discussion:
#
#    We are given a set of N integers W.
#
#    We seek to partition W into subsets W0 and W1, such that the subsets
#    have equal sums.
#
#    The "discrepancy" is the absolute value of the difference between the
#    two sums, and will be zero if we have solved the problem.
#
#    For a given set of integers, there may be zero, one, or many solutions.
#
#    In the case where the weights are distinct, the count returned by this
#    function may be regarded as twice as big as it should be, since the
#    partition (W0,W1) is counted a second time as (W1,W0).  A more serious
#    overcount can occur if the set W contains duplicate elements - in the
#    extreme case, W might be entirely 1's, in which case there is really
#    only one (interesting) solution, but this function will count many.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the size of the set.
#
#    integer W(N), the integers.
#
#  Output:
#
#    integer COUNT, the number of solutions.
#
  import numpy as np

  w_sum = np.sum ( w )

  c = np.zeros ( n, dtype = bool )
  rank = -1
  count = 0

  while ( True ):

    c, rank = subset_next ( n, c, rank )

    if ( rank == -1 ):
      break

    p_sum = 0
    for i in range ( 0, n ):
      if ( c[i] ):
        p_sum = p_sum + w[i]

    discrepancy = abs ( w_sum - 2 * p_sum )

    if ( discrepancy == 0 ):
      count = count + 1

  return count

def partition_count_test ( n, w ):

#*****************************************************************************80
#
## partition_count_test() tests partition_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of weights.
#
#    integer W(N), a set of weights.
#
  print ( '' )
  print ( 'partition_count_test():' )
  print ( '  partition_count() counts the number of exact solutions' )
  print ( '  of the partition problem.' )

  count = partition_count ( n, w )

  print ( '' )
  print ( '     I        W' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %8d' % ( i, w[i] ) )
  print ( '' )
  print ( '  Number of solutions = %d' % ( count ) )

  return

def partition_brute_test ( ):

#*****************************************************************************80
#
## partition_brute_test() tests the partition_brute library.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'partition_brute_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test partition_brute().' )

  for test in range ( 0, 6 ):

    if ( test == 0 ):
      n = 5
      w = np.array ( [ 19, 17, 13, 9, 6 ] )
    elif ( test == 1 ):
      n = 9
      w = np.array ( [ 484, 114, 205, 288, 506, 503, 201, 127, 410 ] )
    elif ( test == 2 ):
      n = 10
      w = np.array ( [ 771, 121, 281, 854, 885, 734, 486, 1003, 83, 62 ] )
    elif ( test == 3 ):
      n = 10
      w = np.array ( [ 2, 10, 3, 8, 5, 7, 9, 5, 3, 2 ] )
    elif ( test == 4 ):
      n = 9
      w = np.array ( [ 3, 4, 3, 1, 3, 2, 3, 2, 1 ] )
    elif ( test == 5 ):
      n = 5
      w = np.array ( [ 8, 7, 6, 5, 4 ] )

    partition_brute_test01 ( n, w )

  for test in range ( 0, 6 ):

    if ( test == 0 ):
      n = 5
      w = np.array ( [ 19, 17, 13, 9, 6 ] )
    elif ( test == 1 ):
      n = 9
      w = np.array ( [ 484, 114, 205, 288, 506, 503, 201, 127, 410 ] )
    elif ( test == 2 ):
      n = 10
      w = np.array ( [ 771, 121, 281, 854, 885, 734, 486, 1003, 83, 62 ] )
    elif ( test == 3 ):
      n = 10
      w = np.array ( [ 2, 10, 3, 8, 5, 7, 9, 5, 3, 2 ] )
    elif ( test == 4 ):
      n = 9
      w = np.array ( [ 3, 4, 3, 1, 3, 2, 3, 2, 1 ] )
    elif ( test == 5 ):
      n = 5
      w = np.array ( [ 8, 7, 6, 5, 4 ] )

    partition_count_test ( n, w )

  subset_next_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'partition_brute_test():' )
  print ( '  Normal end of execution.' )
  return

def subset_next ( n, t, rank ):

#*****************************************************************************80
#
## subset_next() computes the subset lexicographic successor.
#
#  Discussion:
#
#    This is a lightly modified version of "subset_lex_successor()" from COMBO.
#
#  Example:
#
#    On initial call, N is 5 and the input value of RANK is -1.
#    Then here are the successive outputs from the program:
#
#   Rank   T1   T2   T3   T4   T5
#   ----   --   --   --   --   --
#      0    0    0    0    0    0
#      1    0    0    0    0    1
#      2    0    0    0    1    0
#      3    0    0    0    1    1
#     ..   ..   ..   ..   ..   ..
#     30    1    1    1    1    0
#     31    1    1    1    1    1
#     -1    0    0    0    0    0  <-- Reached end of cycle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2015
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
#  Input:
#
#    integer N, the number of elements in the master set.
#    N must be positive.
#
#    bool T(N), describes a subset.  T(I) is False if
#    the I-th element of the master set is not in the subset, and is
#    True if the I-th element is part of the subset.
#
#    integer RANK, the rank.
#    If RANK = -1 on then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#
#  Output:
#
#    bool T(N), describes the next subset. 
#
#    integer RANK, the rank.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was in which
#    case the output value of RANK is -1.
#

#
#  Return the first element.
#
  if ( rank == -1 ):
    rank = 0
    return t, rank

  for i in range ( n - 1, -1, -1 ):

    if ( not t[i] ):
      t[i] = True
      rank = rank + 1
      return t, rank

    t[i] = False

  rank = -1

  return t, rank

def subset_next_test ( ):

#*****************************************************************************80
#
## subset_next_test() tests subset_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'subset_next_test():' )
  print ( '  subset_next() generates all subsets of an N set.' )

  print ( '' )
  n = 5
  t = np.zeros ( n, dtype = bool )
  rank = -1
  
  while ( True ):
 
    t, rank = subset_next ( n, t, rank )
 
    if ( rank == -1 ):
      break

    k = 0

    for i in range ( 0, n ):

      if ( t[i] ):
        k = k + 1
        print ( '  %d' % ( i ) ),

    if ( k == 0 ):
      print ( '  (empty set)' ),

    print ( '' )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  partition_brute_test ( )
  timestamp ( )

