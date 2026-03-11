#! /usr/bin/env python3
#
def knapsack_random_test ( ):

#*****************************************************************************80
#
## knapsack_random_test() tests knapsack_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'knapsack_random_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test knapsack_random()' )

  subset_random_test ( )
  knapsack_random_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'knapsack_random_test():' )
  print ( '  Normal end of execution.' )
  return

def knapsack_random_test01 ( ):

#*****************************************************************************80
#
## knapsack_random_test01() tests knapsack_random().
#
#  Discussion:
#
#    In the knapsack problem, a knapsack of capacity K is given,
#    as well as N items, with the I-th item of value V(I) and weight W(I).
#
#    A selection is "feasible" if the total weight is no greater than K.
#
#    A selection is "optimal" if it is feasible, and the total value of
#    the selected items is not exceeded for any other feasible selection
#
#    This code simply chooses a selection at random, determines if it is
#    feasible, and if so, reports the total value of the selection.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 November 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'knapsack_random_test01():' )
  print ( '  knapsack_random() randomly selects a subset of n items' )
  print ( '  and considers it as a solution to a knapsack problem.' )
  print ( '  Maximize profit without exceeding weight limit.' )

  n = 5
  v = np.array ( [  24,  13,  23,  15,  16 ] )
  w = np.array ( [  12,   7,  11,   8,   9 ] )
  k = 26

  print ( '' )
  print ( '  Number of items is ', n )
  print ( '  Value array ', v )
  print ( '  Weight array ', w )
  print ( '  Weight limit is ', k )

  for test in range ( 0, 10 ):

    c_test = knapsack_random ( n )
    v_test = np.dot ( c_test, v )
    w_test = np.dot ( c_test, w )
    if ( 0.0 < w_test ):
      r_test = v_test / w_test
    else:
      r_test = 0.0

    print ( '' )
    print ( '  Selected items:', c_test )
    if ( k < w_test ):
      print ( '  Weight ', w_test, ' exceeds weight limit ', k )
    else:
      print ( '  Weight ', w_test )
      print ( '  Value ', v_test )
      print ( '  Ratio ', r_test )

  return

def knapsack_random ( n ):

#*****************************************************************************80
#
## knapsack_random() returns a random possible solution of a knapsack problem.
#
#  Discussion:
#
#    The subset is represented as a vector of binary digits.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the total number of items in the set.
#
#  Output:
#
#    integer c[n]: a subset.  Item i is in the subset if c[i] = 1.
#
  c = subset_random ( n )

  return c

def subset_random ( n ):

#*****************************************************************************80
#
## subset_random() returns a random subset of n items.
#
#  Discussion:
#
#    The subset is represented as a vector of binary digits.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the total number of items in the set.
#
#  Output:
#
#    integer c[n]: a subset.  Item i is in the subset if c[i] = 1.
#
  from numpy.random import default_rng

  rng = default_rng ( )

  c = rng.choice ( [ 0, 1 ], size = n )

  return c

def subset_random_test ( ):

#*****************************************************************************80
#
## subset_random_test() tests subset_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'subset_random_test():' )
  print ( '  Test subset_random()' )
  print ( '' )

  n = 5
  print ( '  Subsets will be of size n = ', n )
  print ( '' )

  for test in range ( 0, 10 ):
    c = subset_random ( n )
    index = subset_to_rank ( c )
    print ( index, ':', c )

  return

def subset_to_rank ( c ):

#*****************************************************************************80
#
## subset_to_rank() returns the rank of a subset().
#
#  Discussion:
#
#    The subset is described by a binary vector of n digits.
#    The units digit is the last one.
#    Reading from right to left, we add selected powers of 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer s(n): the subset.
#
#  Output:
#
#    integer index: the rank of the subset.
#
  n = len ( c )
  index = 0
  power2 = 1
  for i in range ( n - 1, -1, -1 ):
    index = index + c[i] * power2
    power2 = power2 * 2

  return index

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

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  knapsack_random_test ( )
  timestamp ( )

