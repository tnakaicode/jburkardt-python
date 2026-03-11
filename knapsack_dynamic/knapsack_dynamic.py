#! /usr/bin/env python3
#
def knapsack_dynamic_test ( ):

#*****************************************************************************80
#
## knapsack_dynamic_test() tests knapsack_dynamic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'knapsack_dynamic_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test knapsack_dynamic().' )

  n_data = 0

  while ( True ):

    n_data, n, v, w, s, k = knapsack_values ( n_data )

    if ( n_data == 0 ):
      break
#
#  Some problems are too large.
#
    if ( 20 < n ):
      continue

    knapsack_dynamic_test01 ( v, w, k )
#
#  Terminate.
#
  print ( '' )
  print ( 'knapsack_dynamic_test():' )
  print ( '  Normal end of execution.' )

  return

def knapsack_dynamic ( v, w, k ):

#*****************************************************************************80
#
## knapsack_dynamic() uses dynamic programming to solve a knapsack problem.
#
#  Discussion:
#
#    All data must be integers.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 November 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer v(n): the profit of each item.
#
#    integer w(n): the weight of each item.
#
#    integer k: the knapsack capacity.
#
#  Output:
#
#    integer item(): the list of item to be taken.
#
  import numpy as np

  m = knapsack_dynamic_table ( v, w, k )

  n = len ( v )
  item = np.array ( [], dtype = int )
  k2 = k

  for i in range ( n - 1, -1, -1 ):
    if ( m[i,k2] < m[i+1,k2] ):
      k2 = k2 - w[i]
      item = np.append ( item, i )

  return item

def knapsack_dynamic_table ( v, w, k ):

#*****************************************************************************80
#
## knapsack_dynamic_table() computes a knapsack problem dynamic programming table.
#
#  Discussion:
#
#    All data must be integers.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer v(n): the profit of each item.
#
#    integer w(n): the weight of each item.
#
#    integer k: the knapsack capacity.
#
#  Output:
#
#    m(0:n,0:k): m(i,j) is the maximum value of the items 
#    that can be stored in the knapsack, selecting from the first 
#    i items, with a weight no more than j.
#
  import numpy as np

  n = len ( v )

  m = np.zeros ( [ n + 1, k + 1 ] )
#
#  Consider object i...
#
  for i in range ( 0, n ):
#
#  Consider the weight limit j from 0 through k.
#
    for j in range ( 0, k + 1 ):
#
#  If item i weighs more than j, then it can't be used.
#
      if ( j < w[i] ):
        m[i+1,j] = m[i,j]
#
#  If item i weighs no more than j, 
#  then it could be used along with the best solution for weight j-w[i].
#  If this gives a better result, update.
#
      else:
        m[i+1,j] = max ( m[i,j], m[i,j-w[i]] + v[i] )
#
#  The value in m[n,k] is the highest profit using n items for a total
#  weight no more than k.
#
  return m

def knapsack_dynamic_test01 ( v, w, k ):

#*****************************************************************************80
#
## knapsack_dynamic_test01() tests knapsack_dynamic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer v(n): the value of each item.
#
#    integer w(n): the weight of each item.
#
#    integer k: the maximum weight capacity for the knapsack.
#
  n = len ( v )

  print ( '' )
  print ( '  Number of items is', n )
  print ( '  Knapsack capacity is', k )
  print ( '  Item values: ' )
  print ( v )
  print ( '  Item weights:' )
  print ( w )

  item = knapsack_dynamic ( v, w, k )
  d = v / w

  print ( '' )
  print ( '   #  Index  Value  Weight  Density' )
  print ( '' )
  v_total = 0
  w_total = 0
  item_num = len ( item )
  for i in range ( 0, item_num ):
    j = item[i]
    print ( '  %2d     %2d   %5d  %5d  %8.2f' % ( i, item[i], v[j], w[j], d[j] ) )
    v_total = v_total + v[j]
    w_total = w_total + w[j]

  d_total = v_total / w_total
  print ( '         --   -----  -----' )
  print ( '  Total: %2d   %5d  %5d  %8.2f' % ( item_num, v_total, w_total, d_total ) )

  return

def knapsack_values ( n_data ):

#*****************************************************************************80
#
## knapsack_values() returns samples of the knapsack problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 November 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n_data: the user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data: on each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    integer n: the number of items
#
#    v[n]: the value of each item;
#
#    w[n]: the weight of each item;
#
#    s[n]: 1 if the item is used in the optimal solution, 0 otherwise.
#
#    k: the weight capacity of the knapsack.
#
  import numpy as np

  n_max = 10

  if ( n_data == n_max ):
    n_data = 0
    n = 0
    v = []
    w = []
    s = []
    k = 0
    return n_data, n, v, w, s, k

  n_data = n_data % n_max

  if ( n_data == 0 ):

    n = 5
    v = np.array ( [  24,  13,  23,  15,  16 ] )
    w = np.array ( [  12,   7,  11,   8,   9 ] )
    s = np.array ( [   0,   1,   1,   1,   0 ] )
    k = 26

  elif ( n_data == 1 ):

    n = 6
    v = np.array ( [  50,  50,  64,  46,  50,   5 ] )
    w = np.array ( [  56,  59,  80,  64,  75,  17 ] )
    s = np.array ( [   1,   1,   0,   0,   1,   0 ] )
    k = 190

  elif ( n_data == 2 ):

    n = 6
    v = np.array ( [  175, 90, 20, 50, 10, 200 ] )
    w = np.array ( [  10,   9,  4,  2,  1,  20 ] )
    s = np.array ( [   1,   1,  0,  0,  1,   0 ] )
    k = 20

  elif ( n_data == 3 ):
 
    n = 7
    v = np.array ( [  70,  20,  39,  37,   7,   5,  10 ] )
    w = np.array ( [  31,  10,  20,  19,   4,   3,   6 ] )
    s = np.array ( [   1,   0,   0,   1,   0,   0,   0 ] )
    k = 50

  elif ( n_data == 4 ):
 
    n = 7
    v = np.array ( [ 442, 525, 511, 593, 546, 564, 617 ] )
    w = np.array ( [  41,  50,  49,  59,  55,  57,  60 ] )
    s = np.array ( [   1,   0,   0,   1,   0,   0,   1 ] )
    k = 170

  elif ( n_data == 5 ):

    n = 8
    v = np.array ( [ 350, 400, 450,  20,  70,   8,   5,   5 ] )
    w = np.array ( [  25,  35,  45,   5,  25,   3,   2,   2 ] )
    s = np.array ( [   1,   0,   1,   1,   1,   0,   1,   1 ] )
    k = 104

  elif ( n_data == 6 ):

    n = 10
    v = np.array ( [ 505, 352, 458, 220, 354, 414, 498, 545, 473, 543 ] )
    w = np.array ( [  23,  26,  20,  18,  32,  27,  29,  26,  30,  27 ] )
    s = np.array ( [   1,   0,   0,   1,   0,   0,   0,   1,   0,   0 ] )
    k = 67

  elif ( n_data == 7 ):

    n = 10
    v = np.array ( [  92,  57,  49,  68,  60,  43,  67,  84,  87,  72 ] )
    w = np.array ( [  23,  31,  29,  44,  53,  38,  63,  85,  89,  82 ] )
    s = np.array ( [   1,   1,   1,   1,   0,   1,   0,   0,   0,   0 ] )
    k = 165

  elif ( n_data == 8 ):

    n = 15
    v = np.array ( [  135, 139, 149, 150, 156, 163, 173, 184, 192, 201, \
                      210, 214, 221, 229, 240 ] )
    w = np.array ( [   70,  73,  77,  80,  82,  87,  90,  94,  98, 106, \
                      110, 113, 115, 118, 120 ] )
    s = np.array ( [    1,   0,   1,   0,   1,   0,   1,   1,   1,   0, \
                        0,   0,   0,   1,   1 ] )
    k = 750

  elif ( n_data == 9 ):

    n = 24
    v = np.array ( [  825594, 1677009, 1676628, 1523970,  943972, \
                       97426,   69666, 1296457, 1679693, 1902996, \
                     1844992, 1049289, 1252836, 1319836,  953277, \
                     2067538,  675367,  853655, 1826027,   65731, \
                      901489,  577243,  466257,  369261 ] )
    w = np.array ( [  382745,  799601,  909247,  729069,  467902, \
                       44328,   34610,  698150,  823460,  903959, \
                      853665,  551830,  610856,  670702,  488960, \
                      951111,  323046,  446298,  931161,   31385, \
                      496951,  264724,  224916,  169684 ] )
    s = np.array ( [       1,       1,       0,       1,       1, \
                           1,       0,       0,       0,       1, \
                           1,       0,       1,       0,       0, \
                           1,       0,       0,       0,       0, \
                           0,       1,       1,       1 ] )
    k = 6404180

  n_data = n_data + 1

  return n_data, n, v, w, s, k

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
  knapsack_dynamic_test ( )
  timestamp ( )

