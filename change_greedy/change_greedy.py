#! /usr/bin/env python3
#
def change_greedy_test ( ):

#*****************************************************************************80
#
## change_greedy_test() tests change_greedy().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'change_greedy_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test change_greedy().' )

  change_greedy_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'change_greedy_test():' )
  print ( '  Normal end of execution.' )

  return

def change_greedy ( value, target ):

#*****************************************************************************80
#
## change_greedy() solves the change making problem using a greedy algorithm.
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
#    integer VALUE(COIN_NUM), the value of each coin.
#
#    integer TARGET, the desired sum.
#
#  Output:
#
#    integer A(COIN_NUM): the number of each coin used by the greedy method.
#
  import math
  import numpy as np

  coin_num = len ( value )
#
#  Descending sort the coin values.
#
  index_sorted = np.argsort ( value )
  index_sorted = index_sorted[::-1]

  a = np.zeros ( coin_num )

  for i in range ( 0, coin_num ):
    coin = index_sorted[i]
    a[coin] = math.floor ( target / value[coin] )
    target = target - a[coin] * value[coin]

  return a
 
def change_greedy_test01 ( ):

#*****************************************************************************80
#
## change_greedy_test01() tests change_greedy().
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
  import numpy as np

  print ( '' )
  print ( 'change_greedy_test01():' )
  print ( '  change_greedy() uses the greedy algorithm to try to' )
  print ( '  find a collection of coins that equal a given sum T.' )

  test_num = 7

  coin_num_list = np.array ( [ \
    3, \
    5, \
    6, \
    7, \
    3, \
    6, \
    3 ] )

  coin_value_list = [ \
    [  5,  9, 13 ], \
    [  1,  4,  5,  8, 11 ], \
    [  1,  5, 10, 25, 50, 100 ], \
    [  1,  2,  6, 12, 24,  48,  60 ], \
    [  1,  3,  4 ], \
    [ 16, 17, 23, 24, 39,  40 ], \
    [  6,  9, 20 ] ]

  target_list = np.array ( [ \
    19, \
    29, \
    96, \
    96, \
     6, \
   100, \
    43 ] )

  for test in range ( 0, test_num ):

    coin_num = coin_num_list[test]
    coin_value = coin_value_list[test]
    target = target_list[test]

    print ( '' )
    print ( '  Test', test )

    a = change_greedy ( coin_value, target )

    print ( '' )
    for i in range ( 0, coin_num ):
      print ( '  %2d  %2d  %2d' % ( i, a[i], coin_value[i] ) )
    print ( '  Target = ', target )
    print ( '  Result = ', sum ( coin_value * a ) )

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
  change_greedy_test ( )
  timestamp ( )


