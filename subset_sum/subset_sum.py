#! /usr/bin/env python3
#
def backup_one ( n, u, told ):

#*****************************************************************************80
#
## BACKUP_ONE seeks the last 1 in the subarray U(1:TOLD-1).
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    16 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the full size of the U array.
#
#    Input, integer U(N), the array to be checked.
#
#    Input, integer TOLD, a value between 1 and N; entries TOLD
#    through N are to be ignored.
#
#    Output, integer T, the highest index in U, between 0 and TOLD-1,
#    for which U is 1.  If no such value is found, T is -1.
#
  t = -1

  for i in range ( told - 1, -1, -1 ):
    if ( u[i] == 1 ):
      t = i;
      break

  return t

def subset_next ( n, t, rank ):

#*****************************************************************************80
#
## SUBSET_NEXT computes the subset lexicographic successor.
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
#    I don't care what you do with this code.
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
#  Parameters:
#
#    Input, integer N, the number of elements in the master set.
#    N must be positive.
#
#    Input/output, bool T(N), describes a subset.  T(I) is False if
#    the I-th element of the master set is not in the subset, and is
#    True if the I-th element is part of the subset.
#    On input, T describes a subset.
#    On output, T describes the next subset in the ordering.
#
#    Input/output, integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
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
      t[i] = True;
      rank = rank + 1;
      return t, rank

    t[i] = False

  rank = -1

  return t, rank

def subset_next_test ( ):

#*****************************************************************************80
#
## SUBSET_NEXT_TEST tests SUBSET_NEXT.
#
#  Licensing:
#
#    I don't care what you do with this code.
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
  import platform

  print ( '' )
  print ( 'SUBSET_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_NEXT generates all subsets of an N set.' )

  print ( '' )
  n = 5
  t = np.zeros ( n, dtype = np.bool )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def subset_sum_count ( n, w, t ):

#*****************************************************************************80
#
## SUBSET_SUM_COUNT counts solutions to the subset sum problem in a given range.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    10 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of weights.
#
#    Input, integer W(N), a set of weights.
#
#    Input, integer T, the target value.
#
#    Output, integer COUNT, the number of solutions found in this range.
#
  import numpy as np
  from sys import exit

  count = 0

  s = np.zeros ( n, dtype = np.bool )
  rank = -1

  while ( True ):

    s, rank = subset_next ( n, s, rank )

    if ( rank == -1 ):
      break

    t2 = 0
    for i in range ( 0, n ):
      if ( s[i] ):
        t2 = t2 + w[i]

    if ( t2 == t ):
      count = count + 1

  return count

def subset_sum_count_test ( n, w, t ):

#*****************************************************************************80
#
## SUBSET_SUM_COUNT_TEST tests SUBSET_SUM_COUNT.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of weights.
#
#    Input, integer W(N), a set of weights. 
#
#    Input, integer T, the target value.
#
#    Input, integer R(2), the lower and upper limits to be searched.
#    If this argument is omitted, the entire range, [0, 2^N-1 ] will
#    be searched.
#
  print ( '' )
  print ( 'SUBSET_SUM_COUNT_TEST:' )
  print ( '  SUBSET_SUM_COUNT counts solutions to the subset sum problem.' )
  print ( '' )
  print ( '  Seek a subset of W that sums to T.' )
  print ( '' )
  print ( '  Target value T = %d' % ( t ) )
  print ( '' )
  print ( '   I       W(I)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %8d' % ( i, w[i] ) )

  count = subset_sum_count ( n, w, t )

  print ( '' )
  print ( '  Number of solutions is %d.' % ( count ) )

  return count

def subset_sum_count_tests ( ):

#*****************************************************************************80
#
## SUBSET_SUM_COUNT_TESTS tests SUBSET_SUM_COUNT_TEST.
#
#  Licensing:
#
#    I don't care what you do with this code.
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
  import platform

  print ( '' )
  print ( 'SUBSET_SUM_COUNT_TESTS:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_SUM_COUNT_TEST calls SUBSET_SUM_COUNT with a' )
  print ( '  particular set of weights and target.' )
#
#  Problem #1.
#
  n = 8
  w = np.array ( [ 15, 22, 14, 26, 32, 9, 16, 8 ] )
  t = 53
  count = subset_sum_count_test ( n, w, t )
#
#  Problem #2.
#
  n = 10
  w = np.array ( [ 267, 493, 869,  961, 1000, 1153, 1246, 1598, 1766, 1922 ] )
  t = 5842
  count = subset_sum_count_test ( n, w, t )
#
#  Problem #3.
#
  n = 21
  w = np.array ( [  \
         518533, 1037066, 2074132, 1648264, 796528, \
        1593056,  686112, 1372224,  244448, 488896, \
         977792, 1955584, 1411168,  322336, 644672, \
        1289344,   78688,  157376,  314752, 629504, \
        1259008 ] )
  t = 2463098
  count = subset_sum_count_test ( n, w, t )
#
#  Problem #4.
#
  n = 10
  w = np.array ( [ 41, 34, 21, 20,  8,  7,  7,  4,  3,  3 ] )
  t = 50
  count = subset_sum_count_test ( n, w, t )
#
#  Problem #5.
#
  n = 9
  w = np.array ( [ 81, 80, 43, 40, 30, 26, 12, 11, 9 ] )
  t = 100
  count = subset_sum_count_test ( n, w, t )
#
#  Problem #6.
#
  n = 6
  w = np.array ( [ 1, 2, 4, 8, 16, 32 ] )
  t = 22
  count = subset_sum_count_test ( n, w, t )
#
#  Problem #7.
#
  n = 10
  w = np.array ( [ 25, 27, 3, 12, 6, 15, 9, 30, 21, 19 ] )
  t = 50
  count = subset_sum_count_test ( n, w, t )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_SUM_COUNT_TESTS:' )
  print ( '  Normal end of execution.' )
  return

def subset_sum_find ( n, w, t ):

#*****************************************************************************80
#
## SUBSET_SUM_FIND seeks a subset of a set that has a given sum.
#
#  Discussion:
#
#    This function tries to compute a target value as the sum of
#    a selected subset of a given set of weights.
#
#    This function works by brute force, that is, it tries every
#    possible subset to see if it sums to the desired value.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    10 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of weights.
#
#    Input, integer W(N), a set of weights.
#
#    Input, integer T, the target value.
#
#    Output, bool S(N), the indices of the weights used to make the combination.
#
  import numpy as np
  from sys import exit

  s = np.zeros ( n, dtype = np.bool )
  s2 = np.zeros ( n, dtype = np.bool )
  rank = -1

  while ( True ):

    s2, rank = subset_next ( n, s2, rank )

    if ( rank == -1 ):
      break

    t2 = 0
    for i in range ( 0, n ):
      if ( s2[i] ):
        t2 = t2 + w[i]

    if ( t2 == t ):
      for i in range ( 0, n ):
        s[i] = s2[i]
      return s

  return s

def subset_sum_find_test ( n, w, t ):

#*****************************************************************************80
#
## SUBSET_SUM_FIND_TEST tests SUBSET_SUM_FIND.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    10 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of weights.
#
#    Input, integer W(N), a set of weights.
#
#    Input, integer T, the target value.
#
  print ( '' )
  print ( 'SUBSET_SUM_FIND_TEST:' )
  print ( '  SUBSET_SUM_FIND seeks a subset of W that sums to T.' )
  print ( '' )
  print ( '  Target value T = %d' % ( t ) )
  print ( '' )
  print ( '   I       W(I)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %8d' % ( i, w[i] ) )

  c = subset_sum_find ( n, w, t )

  m = 0
  for i in range ( 0, n ):
    if ( c[i] ):
      m = m + 1

  print ( '' )

  if ( m == 0 ):
    print ( '  No solution was found.' )
  else:
    print ( '  %d = ' % ( t ) ),
    for i in range ( 0, n ):
      if ( c[i] ):
        print ( ' + %d' % ( w[i] ) ),
    print ( '' )

  return

def subset_sum_find_tests ( ):

#*****************************************************************************80
#
## SUBSET_SUM_FIND_TESTS tests SUBSET_SUM_FIND_TEST.
#
#  Licensing:
#
#    I don't care what you do with this code.
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
  import platform

  print ( '' )
  print ( 'SUBSET_SUM_FIND_TESTS:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_SUM_FIND_TEST calls SUBSET_SUM_FIND with a' )
  print ( '  particular set of weights and target.' )
#
#  Problem #1.
#
  n = 8
  w = np.array ( [ 15, 22, 14, 26, 32, 9, 16, 8 ] )
  t = 53
  subset_sum_find_test ( n, w, t )
#
#  Problem #2.
#
  n = 10
  w = np.array ( [ 267,  493,  869,  961, 1000, 1153, 1246, 1598, 1766, 1922 ] )
  t = 5842
  subset_sum_find_test ( n, w, t )
#
#  Problem #3.
#
  n = 21
  w = np.array ( [  \
         518533, 1037066, 2074132, 1648264, 796528, \
        1593056,  686112, 1372224,  244448, 488896, \
         977792, 1955584, 1411168,  322336, 644672, \
        1289344,   78688,  157376,  314752, 629504, \
        1259008 ] )
  t = 2463098
  subset_sum_find_test ( n, w, t )
#
#  Problem #4.
#
  n = 10
  w = np.array ( [ 41, 34, 21, 20,  8,  7,  7,  4,  3,  3 ] )
  t = 50
  subset_sum_find_test ( n, w, t )
#
#  Problem #5.
#
  n = 9
  w = np.array ( [ 81, 80, 43, 40, 30, 26, 12, 11, 9 ] )
  t = 100
  subset_sum_find_test ( n, w, t )
#
#  Problem #6.
#
  n = 6
  w = np.array ( [ 1, 2, 4, 8, 16, 32 ] )
  t = 22
  subset_sum_find_test ( n, w, t )
#
#  Problem #7.
#
  n = 10
  w = np.array ( [ 25, 27, 3, 12, 6, 15, 9, 30, 21, 19 ] )
  t = 50
  subset_sum_find_test ( n, w, t )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_SUM_FIND_TESTS:' )
  print ( '  Normal end of execution.' )
  return

def subset_sum_next ( s, n, v, more, u, t ):
 
#*****************************************************************************80
#
## SUBSET_SUM_NEXT seeks, one at a time, subsets of V that sum to S.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    16 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer S, the desired sum.
#
#    Input, integer N, the number of values.
#
#    Input, integer V(N), the values.
#    These must be nonnegative, and sorted in ascending order.  
#    Duplicate values are allowed.
#
#    Input, logical MORE, should be set to FALSE before the first call.
#    Thereafter, it should be the output value of the previous call.
#
#    Input, integer U(N), should be set to 0 before the first call.
#    Thereafter, it should be the output value of the previous call.
#
#    Input, integer T, should be set to 0 before the first call.
#    Thereafter, it should be the output value of the previous call.
#
#    Output, logical MORE, is TRUE if a new solution has been returned in U.
#    Process this solution, and call again if more solutions should be sought.
#
#    Output, integer U(N), if MORE is true, U indexes the solution values.
#
#    Output, integer T, if MORE is true, T is the highest index of the selected values.
#
  import numpy as np

  if ( not more ):
  
    t = -1
    u = np.zeros ( n )

  else:
  
    more = False
    u[t] = 0

    t = backup_one ( n, u, t )
      
    if ( t < 0 ):
      return more, u, t

    u[t] = 0
    t = t + 1
    u[t] = 1
    
  while ( True ):

    su = np.dot ( u, v )
  
    if ( su < s and t < n - 1 ):

      t = t + 1
      u[t] = 1

    else:

      if ( su == s ):
        more = True;
        return more, u, t

      u[t] = 0

      t = backup_one ( n, u, t )
      
      if ( t < 0 ):
        break

      u[t] = 0
      t = t + 1
      u[t] = 1

  return more, u, t

def subset_sum_next_test ( s, n, v ):

#*****************************************************************************80
#
## SUBSET_SUM_NEXT_TEST tests the SUBSET_SUM_NEXT library.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    16 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer S, the desired sum.
#
#    Input, integer N, the number of values.
#
#    Input, integer V(N), the values.
#    These must be nonnegative, and sorted in ascending order.  
#    Duplicate values are allowed.
#
  import numpy as np

  print ( '' )
  print ( 'SUBSET_SUM_NEXT_TEST:' )
  print ( '  SUBSET_SUM_NEXT finds the "next" subset of the values' )
  print ( '  which sum to the desired total S.' )

  more = False
  u = np.zeros ( n )
  t = 0
  
  print ( '' )
  print ( '  Desired sum S = %d' % ( s ) )
  print ( '  Number of targets = %d' % ( n ) )
  print ( '  Targets:' ),
  for i in range ( 0, n ):
    print ( ' %d' % ( v[i] ) ),
  print ( '' )
  print ( '' )

  k = 0
  
  while ( True ):
    more, u, t = subset_sum_next ( s, n, v, more, u, t )
    if ( not more ):
      break
    k = k + 1
    print ( '  %d:  %d = ' % ( k, s ) ),
    plus = False
    for i in range ( 0, n ):
      if ( u[i] != 0 ):
        if ( plus ):
          print ( '+' ),
        print ( '%d' % ( v[i] ) ),
        plus = True
    print ( '' )
  
  return

def subset_sum_next_tests ( ):

#*****************************************************************************80
#
## SUBSET_SUM_NEXT_TESTS calls SUBSET_SUM_NEXT_TEST with various values.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    16 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'SUBSET_SUM_NEXT_TESTS:' )
  print ( '  SUBSET_SUM_NEXT_TEST solves the subset sum problem' )
  print ( '  for specific values of S, N and V.' )
  
  s = 9
  n = 5
  v = np.array ( [ 1, 2, 3, 5, 7 ] )
  subset_sum_next_test ( s, n, v )
  
  s = 8
  n = 9
  v = np.array ( [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] )
  subset_sum_next_test ( s, n, v )
#
#  What happens with a repeated target?
#
  s = 8
  n = 9
  v = np.array ( [ 1, 2, 3, 3, 5, 6, 7, 8, 9 ] )
  subset_sum_next_test ( s, n, v )
#
#  What happens with a target that needs all the values?
#
  s = 18
  n = 5
  v = np.array ( [ 1, 2, 3, 5, 7 ] )
  subset_sum_next_test ( s, n, v )
#
#  A larger S.
#
  s = 5842
  n = 10
  v = np.array ( [ 267, 493, 869, 961, 1000, 1153, 1246, 1598, 1766, 1922 ] )
  subset_sum_next_test ( s, n, v )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_SUM_NEXT_TESTS:' )
  print ( '  Normal end of execution.' )
  
  return

def subset_sum_table ( t, n, w ):

#*****************************************************************************80
#
## SUBSET_SUM_TABLE sets a subset sum table.
#
#  Discussion:
#
#    The subset sum problem seeks to construct the value T by summing a 
#    subset of the values W.
#
#    This function seeks a solution by constructing a table TABLE of length T,
#    so that TABLE(I) = J means that the sum I can be constructed, and that
#    the last member of the sum is an entry of W equal to J.
#
#  Example:
#
#    w = [ 1, 2, 4, 8, 16, 32 ]
#    t = 22
#
#    table = subset_sum ( w, t, r )
#    table = [ 1, 2, 2, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 
#      16, 16, 16, 16, 16, 16, 16 ]
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    11 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer T, the target value.
#
#    Input, integer N, the number of weights.
#
#    Input, integer W(N), the weights.
#
#    Output, integer TABLE(T+1), the subset sum table.  TABLE(I) is 0 if the
#    target value I cannot be formed.  It is J if the value I can be formed,
#    with the last term in the sum being the value J.
#
  import numpy as np

  table = np.zeros ( t + 1, dtype = np.int32 )

  for i in range ( 0, n ):
    for j in range ( t - w[i], -1, -1 ):

      if ( j == 0 ):
        if ( table[w[i]] == 0 ):
          table[w[i]] = w[i]
      elif ( table[j] != 0 and table[j+w[i]] == 0 ):
        table[j+w[i]] = w[i]
  
  return table

def subset_sum_table_test ( t, n, w ):

#*****************************************************************************80
#
## SUBSET_SUM_TABLE_TEST tests SUBSET_SUM_TABLE.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    09 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer T, the target value.
#
#    Input, integer N, the number of weights.
#
#    Input, integer W(N), a set of weights.
#
  print ( '' )
  print ( 'SUBSET_SUM_TABLE_TEST:' )
  print ( '  SUBSET_SUM_TABLE seeks a subset of W that sums to T.' )
  print ( '' )
  print ( '  Target value T = %d' % ( t ) )
  print ( '' )
  print ( '   I       W(I)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %8d' % ( i, w[i] ) )

  table = subset_sum_table ( t, n, w )

  print ( '' )

  if ( table[t] == 0 ):
    print ( '  No solution was found.' )
  else:
    m, list = subset_sum_table_to_list ( t, table )
    print ( '  %d =' % ( t ) ),
    for i in range ( 0, m ):
      if ( 0 < i ):
        print ( '+' ),
      print ( '%d' % ( list[i] ) ),
    print ( '' )

  return

def subset_sum_table_tests ( ):

#*****************************************************************************80
#
## SUBSET_SUM_TABLE_TESTS tests SUBSET_SUM_TABLE_TEST.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    11 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'SUBSET_SUM_TABLE_TESTS:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_SUM_TABLE_TEST calls SUBSET_SUM_TABLE with a' )
  print ( '  particular set of weights and target.' )
#
#  Problem #1.
#
  t = 53
  n = 8
  w = np.array ( [ 15, 22, 14, 26, 32, 9, 16, 8 ] )
  subset_sum_table_test ( t, n, w )
#
#  Problem #2.
#
  t = 5842
  n = 10
  w = np.array ( [   267,  493,  869,  961, 1000, 1153, 1246, 1598, 1766, 1922 ] )
  subset_sum_table_test ( t, n, w )
#
#  Problem #3.
#
  t = 2463098
  n = 21
  w = np.array ( [  \
         518533, 1037066, 2074132, 1648264, 796528, \
        1593056,  686112, 1372224,  244448, 488896, \
         977792, 1955584, 1411168,  322336, 644672, \
        1289344,   78688,  157376,  314752, 629504, \
        1259008 ] )
  subset_sum_table_test ( t, n, w )
#
#  Problem #4.
#
  t = 50
  n = 10
  w = np.array ( [ 41, 34, 21, 20,  8,  7,  7,  4,  3,  3 ] )
  subset_sum_table_test ( t, n, w )
#
#  Problem #5.
#
  t = 100
  n = 9
  w = np.array ( [ 81, 80, 43, 40, 30, 26, 12, 11, 9 ] )
  subset_sum_table_test ( t, n, w )
#
#  Problem #6.
#
  t = 22
  n = 6
  w = np.array ( [ 1, 2, 4, 8, 16, 32 ] )
  subset_sum_table_test ( t, n, w )
#
#  Problem #7.
#
  t = 50
  n = 10
  w = np.array ( [ 25, 27, 3, 12, 6, 15, 9, 30, 21, 19 ] )
  subset_sum_table_test ( t, n, w )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_SUM_TABLE_TESTS:' )
  print ( '  Normal end of execution.' )
  return

def subset_sum_table_to_list ( t, table ):

#*****************************************************************************80
#
## SUBSET_SUM_TABLE_TO_LIST converts a subset sum table to a list.
#
#  Discussion:
#
#    The subset sum problem seeks to construct the value T by summing a 
#    subset of the values W.
#
#    This function takes a table computed by subset_sum_table() and converts
#    it to the corresponding list of values that form the sum.
#
#  Example:
#
#    w = [ 1, 2, 4, 8, 16, 32 ]
#    t = 22
#
#    table = subset_sum ( w, t, r )
#    table = [ 1, 2, 2, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 
#      16, 16, 16, 16, 16, 16, 16 ]
#
#    index = subset_sum_table_to_list ( t, table )
#    index = [ 2, 4, 16 ]
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    11 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer T, the target value.
#
#    Input, integer TABLE(T), the subset sum table.
#
#    Output, integer M, the number of items in the list.
#
#    Output, integer INDEX(M), the list of weights that form the sum.
#    If no solution was found, then INDEX is an empty list.
#
  index = []

  m = 0
  i = t
  while ( 0 < i ):
    index.append ( table[i] )
    i = i - table[i]
    m = m + 1

  return m, index

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def subset_sum_test ( ):

#*****************************************************************************80
#
## SUBSET_SUM_TEST tests the SUBSET_SUM library.
#
#  Licensing:
#
#    I don't care what you do with this code.
#
#  Modified:
#
#    16 July 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SUBSET_SUM_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the SUBSET_SUM library.' )

  subset_next_test ( )
  subset_sum_count_tests ( )
  subset_sum_find_tests ( )
  subset_sum_next_tests ( )
  subset_sum_table_tests ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_SUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  subset_sum_test ( )
  timestamp ( )

