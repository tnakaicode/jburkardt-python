#! /usr/bin/env python3
#
def subset_sum_swap_test ( ):

#*****************************************************************************80
#
## subset_sum_swap_test() tests subset_sum_swap().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'subset_sum_swap_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test subset_sum_swap().' )

  subset_sum_swap_tests ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'subset_sum_swap_test():' )
  print ( '  Normal end of execution.' )

  return

def subset_sum_swap_tests ( ):

#*****************************************************************************80
#
## subset_sum_swap_tests() defines a series of subset sum problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
#
#  Problem #1.
#
  n = 8
  w = np.array ( [ 15, 22, 14, 26, 32, 9, 16, 8 ] )
  t = 53
  subset_sum_swap_try ( n, w, t )
#
#  Problem #2.
#
  n = 10
  w = np.array ( [ 267, 493, 869,  961, 1000, 1153, 1246, 1598, 1766, 1922 ] )
  t = 5842
  subset_sum_swap_try ( n, w, t )
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
  subset_sum_swap_try ( n, w, t )
#
#  Problem #4.
#
  n = 10
  w = np.array ( [ 41, 34, 21, 20,  8,  7,  7,  4,  3,  3 ] )
  t = 50
  subset_sum_swap_try ( n, w, t )
#
#  Problem #5.
#
  n = 9
  w = np.array ( [ 81, 80, 43, 40, 30, 26, 12, 11, 9 ] )
  t = 100
  subset_sum_swap_try ( n, w, t )
#
#  Problem #6.
#
  n = 6
  w = np.array ( [ 1, 2, 4, 8, 16, 32 ] )
  t = 22
  subset_sum_swap_try ( n, w, t )
#
#  Problem #7.
#
  n = 10
  w = np.array ( [ 25, 27, 3, 12, 6, 15, 9, 30, 21, 19 ] )
  t = 50
  subset_sum_swap_try ( n, w, t )

  return

def subset_sum_swap_try ( n, w, t ):

#*****************************************************************************80
#
## subset_sum_swap_try() tries the swap code for a given subset_sum problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( '  Target value: ', t )
  
  print ( '' )
  print ( '  Available weights' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  ', w[i] )

  a, index, sum_achieved = subset_sum_swap ( n, w, t )

  print ( '' )
  print ( '  Selected weights' )
  print ( '' )

  for i in range ( 0, n ):
    if ( index[i] == 1 ):
      print ( '  ', a[i] )

  print ( '' )
  print ( '  The target was      ', t )
  print ( '  The achieved sum is ', sum_achieved )
  print ( '  The defect is       ', t - sum_achieved )

  return

def subset_sum_swap ( n, a, sum_desired ):

#*****************************************************************************80
#
## subset_sum_swap() seeks a solution of the subset sum problem by swapping.
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
#        end the search
#      Otherwise,
#        repeat the search.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the number of values.  N must be positive.
#
#    integer A(N), a collection of positive values.
#
#    integer SUM_dESIRED, the desired sum.
#
#  Output:
#
#    integer A(N), a collection of positive values, sorted into descending order.
#
#    integer INDEX(N) INDEX(I) is 1 if A(I) is part of the
#    sum, and 0 otherwise.
#
#    integer SUM_ACHIEVED, the sum of the selected elements.
#
  import numpy as np
#
#  Initialize.
#
  sum_achieved = 0

  index = np.zeros ( n )
#
#  Sort into descending order.
#
  np.sort ( a )
  np.flip ( a )

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

if ( __name__ == '__main__' ):
  timestamp ( )
  subset_sum_swap_test ( )
  timestamp ( )

