#! /usr/bin/env python3
#

def subset_sum_test ( ):

#*****************************************************************************80
#
## subset_sum_test tests subset_sum().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
  import platform

  print ( '' )
  print ( 'subset_sum_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test subset_sum().' )

  subset_next_test ( )
  subset_sum_count_tests ( )
  subset_sum_find_tests ( )
  subset_sum_table_tests ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'subset_sum_test():' )
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
      t[i] = True;
      rank = rank + 1;
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
  import platform

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

def subset_sum_count ( n, w, t ):

#*****************************************************************************80
#
## subset_sum_count() counts solutions to the subset sum problem in a given range.
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
#    integer T, the target value.
#
#  Output:
#
#    integer COUNT, the number of solutions found in this range.
#
  import numpy as np

  count = 0

  s = np.zeros ( n, dtype = bool )
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
## subset_sum_count_test() tests subset_sum_count().
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
#  Input:
#
#    integer N, the number of weights.
#
#    integer W(N), a set of weights. 
#
#    integer T, the target value.
#
#    integer R(2), the lower and upper limits to be searched.
#    If this argument is omitted, the entire range, [0, 2^N-1 ] will
#    be searched.
#
  print ( '' )
  print ( 'subset_sum_count_test():' )
  print ( '  subset_sum_count() counts solutions to the subset sum problem.' )
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
## subset_sum_count_tests() tests subset_sum_count_test().
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
  print ( 'subset_sum_count_tests():' )
  print ( '  subset_sum_count_test() calls subset_sum_count() with a' )
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

  return

def subset_sum_find ( n, w, t ):

#*****************************************************************************80
#
## subset_sum_find() seeks a subset of a set that has a given sum.
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
#    integer T, the target value.
#
#  Output:
#
#    bool S(N), the indices of the weights used to make the combination.
#
  import numpy as np

  s = np.zeros ( n, dtype = bool )
  s2 = np.zeros ( n, dtype = bool )
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
## subset_sum_find_test() tests subset_sum_find().
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
#    integer T, the target value.
#
  print ( '' )
  print ( 'subset_sum_find_test():' )
  print ( '  subset_sum_find() seeks a subset of W that sums to T.' )
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
## subset_sum_find_tests() tests subset_sum_find_test().
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
  print ( 'subset_sum_find_tests():' )
  print ( '  subset_sum_find_test() calls subset_sum_find() with a' )
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

  return

def subset_sum_table ( t, n, w ):

#*****************************************************************************80
#
## subset_sum_table() sets a subset sum table.
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
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer T, the target value.
#
#    integer N, the number of weights.
#
#    integer W(N), the weights.
#
#  Output:
#
#    integer TABLE(T+1), the subset sum table.  TABLE(I) is 0 if the
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
## subset_sum_table_test() tests subset_sum_table().
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
#  Input:
#
#    integer T, the target value.
#
#    integer N, the number of weights.
#
#    integer W(N), a set of weights.
#
  print ( '' )
  print ( 'subset_sum_table_test():' )
  print ( '  subset_sum_table() seeks a subset of W that sums to T.' )
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
## subset_sum_table_tests() tests subset_sum_table_test().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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

  print ( '' )
  print ( 'subset_sum_table_tests:' )
  print ( '  subset_sum_table_test calls SUBSET_SUM_TABLE with a' )
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

  return

def subset_sum_table_to_list ( t, table ):

#*****************************************************************************80
#
## subset_sum_table_to_list() converts a subset sum table to a list.
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
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer T, the target value.
#
#    integer TABLE(T), the subset sum table.
#
#  Output:
#
#    integer M, the number of items in the list.
#
#    integer INDEX(M), the list of weights that form the sum.
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
  subset_sum_test ( )
  timestamp ( )

