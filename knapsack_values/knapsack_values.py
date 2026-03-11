#! /usr/bin/env python3
#
def knapsack_values_test ( ):

#*****************************************************************************80
#
## knapsack_values_test() tests knapsack_values().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'knapsack_values_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test knapsack_values().' )

  n_data = 0

  while ( True ):

    [ n_data, n, v, w, s, k ] = knapsack_values ( n_data )

    if ( n_data == 0 ):
      break

    d = v / w

    print ( '' )
    print ( '  Problem #', n_data )
    print ( '  Number of items is ', n )
    print ( '  Knapsack weight limit is ', k )
    print ( '' )
    print ( '   Item 0/1  Value  Weight  Density' )
    print ( '' )
    for i in range ( 0, n ):
      print ( '  %5d  %2d  %8.0f  %8.0f  %7.2f' % ( i, s[i], v[i], w[i], d[i] ) )
    print ( '' )
    print ( '  Taken  %2d  %8.0f  %8.0f  %7.2f' % ( \
      np.sum ( s ), \
      np.dot ( s, v ), \
      np.dot ( s, w ), \
      np.dot ( s, v ) / np.dot ( s, w ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'knapsack_values_test():' )
  print ( '  Normal end of execution.' )
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

if ( __name__ == "__main__" ):
  timestamp ( )
  knapsack_values_test ( )
  timestamp ( )
