#! /usr/bin/env python3
#
def i4_to_digits_binary ( i, n ):

#*****************************************************************************80
#
## i4_to_digits_binary() produces the binary digits of an I4.
#
#  Discussion:
#
#    An I4 is an integer.
#
#  Example:
#
#     I    N     C               Binary
#    --  ---   ---         ------------
#     0    1   0                      0
#     0    2   0, 0                  00
#     1    3   1, 0, 0              100
#     2    3   0, 1, 0              010
#     3    3   1, 1, 0              011
#     4    3   0, 0, 1              100
#     8    3   0, 0, 0           (1)000
#     8    5   0, 0, 0, 1, 0      01000
#    -8    5   0, 0, 0, 1, 0  (-) 01000
#
#     0    3   0, 0, 0
#     1    3   1, 0, 0
#     2    3   0, 1, 0
#     3    3   1, 1, 0
#     4    3   0, 0, 1
#     5    3   1, 0, 1
#     6    3   0, 1, 1
#     7    3   1, 1, 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, an integer to be represented.
#
#    integer N, the number of binary digits to produce.
#
#  Output:
#
#    integer C(N), the first N binary digits of I,
#    with C(1) being the units digit.
#
  import math
  import numpy as np

  i_copy = math.floor ( abs ( i ) )

  c = np.zeros ( n )

  for j in range ( 0, n ):

    c[j] = math.floor ( i_copy % 2 )
    i_copy = math.floor ( i_copy / 2 )

  return c

def subset_sum_brute ( n, weight, target ):

#*****************************************************************************80
#
## subset_sum_brute() seeks a subset of a set that has a given sum.
#
#  Discussion:
#
#    This function tries to compute a target value as the sum of
#    a selected subset of a given set of weights.
#
#    This function works by brute force, that is, it tries every
#    possible subset to see if it sums to the desired value.
#
#    Given N weights, every possible selection can be described by 
#    one of the N-digit binary numbers from 0 to 2^N-1.
#
#    It is possible that there may be multiple solutions of the problem.  
#    This function will only return the first solution found.
#
#  Example:
#
#    c = subset_sum_brute ( 6, [1 2 4 8 16 32], 22 )
#
#    c = [ 0 1 1 0 1 0 ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 July 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of weights.
#
#    integer WEIGHT(N), a set of weights.
#
#    integer TARGET, the target value.
#
#  Output:
#
#    integer CHOOSE(N), contains a 1 for each weight that is
#    chosen, 0 for weights not chosen.  If no solution was found,
#    all entries are -1.
#
  import numpy as np
#
#  Iterate through all possible combinations in the provided range.
#
  for i in range ( 0, 2**n ):
#
#  Find the combination of weights represented by the current attempt.
#
    choose = i4_to_digits_binary ( i, n )
#
#  Sum the chosen weights.
#
    w_sum = np.dot ( choose, weight )
#
#  If the sum matches the target, return the combination.
#
    if ( w_sum == target ):
      return choose
    
  choose = -1 * np.ones ( n )

  return choose

def subset_sum_brute_test01 ( ):

#*****************************************************************************80
#
## subset_sum_brute_test01() tests the subset_sum_brute program.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2012
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'subset_sum_brute_test01():' )
  print ( '  Test the subset_sum_brute function, which looks for a selection' )
  print ( '  from a set of weights that adds up to a given target.' )
#
#  Define the problem data.
#
  target = 2463098
  print ( '' )
  print ( '  Target value:' )
  print ( '      ', target )

  weight = np.array ( [ \
    518533, 1037066, 2074132, 1648264, 796528, \
   1593056,  686112, 1372224,  244448, 488896, \
    977792, 1955584, 1411168,  322336, 644672, \
   1289344,   78688,  157376,  314752, 629504, \
   1259008 ] )

  n = len ( weight )
  
  print ( '' )
  print ( '   I      W(I)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %8d' % ( i, weight[i] ) )

  choose = subset_sum_brute ( n, weight, target )

  if ( choose[0] == -1 ):
    print ( '' )
    print ( '  No solution was found.' )
  else:
    print ( '' )
    print ( '   I*     W*' )
    print ( '' )
    w_sum = 0
    for i in range ( 0, n ):
      if ( choose[i] == 1 ):
        print ( '  %2d  %8d' % ( i, weight[i] ) )
        w_sum = w_sum + weight[i]
    print ( '' )
    print ( ' Sum  ', w_sum )

  return

def subset_sum_brute_test ( ):

#*****************************************************************************80
#
## subset_sum_brute_test() tests subset_sum_brute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'subset_sum_brute_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test subset_sum_brute().' )

  subset_sum_brute_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'subset_sum_brute_test():' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  subset_sum_brute_test ( )
  timestamp ( )

