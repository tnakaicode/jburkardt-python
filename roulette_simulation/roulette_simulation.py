#! /usr/bin/env python3
#
def bet_black ( ):

#*****************************************************************************80
#
## bet_black() returns the roulette pockets for a bet on black.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer set B(L), the pockets.
#
  b = { \
     2,  4,  6,  8, 10, \
    11, 13, 15, 17, 20, \
    22, 24, 26, 28, 29, \
    31, 33, 35 }

  return b

def bet_column1 ( ):

#*****************************************************************************80
#
## bet_column1() returns the roulette pockets for a bet on column 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer set B(L), the pockets.
#
  b = { 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34 }

  return b

def bet_column2 ( ):

#*****************************************************************************80
#
## bet_column2() returns the roulette pockets for a bet on column2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer set B(L), the pockets.
#
  b = { 2, 5, 8, 11, 14, 17, 10, 23, 26, 29, 32, 35 }

  return b

def bet_column3 ( ):

#*****************************************************************************80
#
## bet_column3() returns the roulette pockets for a bet on column3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer set B(L), the pockets.
#
  b = { 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36 }

  return b

def bet_even ( ):

#*****************************************************************************80
#
## bet_even() returns the roulette pockets for a bet on even.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer set B(L), the pockets.
#
  b = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36 }

  return b

def bet_high ( ):

#*****************************************************************************80
#
## bet_high() returns the roulette pockets for a bet on high.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer set B(L), the pockets.
#
  b = { 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36 }

  return b

def bet_low ( ):

#*****************************************************************************80
#
## bet_low() returns the roulette pockets for a bet on low.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer set B(L), the pockets.
#
  b = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 }

  return b

def bet_odd ( ):

#*****************************************************************************80
#
## bet_odd() returns the roulette pockets for a bet on odd.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer set B(L), the pockets.
#
  b = { 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35 }

  return b

def bet_red ( ):

#*****************************************************************************80
#
## bet_red() returns the roulette pockets for a bet on red.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer set B(L), the pockets.
#
  b = { \
     1,  3,  5,  7,  9, \
    12, 14, 16, 18, 19, \
    21, 23, 25, 27, 30, \
    32, 34, 36 }

  return b

def i4vec_sorted_unique_hist ( n, a ):

#*****************************************************************************80
#
## i4vec_sorted_unique_hist() histograms unique elements of a sorted I4VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of A.
#
#    integer A(N), the array to examine.  The elements of A
#    should have been sorted.
#
#  Output:
#
#    integer UNIQUE_NUM, the number of unique elements of A.
#
#    integer AUNIQ(UNIQUE_NUM), the unique elements of A.
#
#    integer ACOUNT(UNIQUE_NUM), the number of times each element
#    of AUNIQ occurs in A.
#
  import numpy as np

  auniq = np.unique ( a )
  unique_num = len ( auniq )
  acount = np.zeros ( unique_num )
#
#  Start taking statistics.
#
  k = 0
  acount[k] = 1

  for i in range ( 1, n ):

    if ( a[i] == auniq[k] ):

      acount[k] = acount[k] + 1

    else:

      k = k + 1
      acount[k] = 1

  return unique_num, auniq, acount

def i4vec_sorted_unique_hist_test ( rng ):

#*****************************************************************************80
#
## i4vec_sorted_unique_hist_test() tests i4vec_sorted_unique_hist_test().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_sorted_unique_hist_test():' )
  print ( '  i4vec_sorted_unique_hist_test() is given a sorted array' )
  print ( '  of integers, and returns the number of unique values,' )
  print ( '  the unique values, and their frequency.' )

  n = 50
  a = 0
  b = 10
 
  v1 = rng.integers ( low = a, high = b, size = n, endpoint = True )

  v2 = rng.integers ( low = a, high = b, size = n, endpoint = True )

  v3 = np.zeros ( n, dtype = np.int32 )

  v3 = v1 * v2

  v3 = np.sort ( v3 )

  print ( '' )
  print ( '  The sorted vector' )
  print ( v3 )

  unique_num, unique_value,  unique_freq = i4vec_sorted_unique_hist ( n, v3 )

  print ( '' )
  print ( '  Unique values and frequencies:' )
  print ( np.c_ [ unique_value, unique_freq ] )

  return

def roulette_result ( m, n, rng ):

#*****************************************************************************80
#
## roulette_result() returns results from spins of the roulette wheel.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of pockets on a roulette wheel.
#    36, a fair roulette wheel.
#    37, a European roulette wheel.  Pocket 37 is "0".
#    38, a Las Vegas roulette wheel.  Pocket 37 is "0" and 38 is "00".
#
#    integer N, the number of results requested.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer V(N), N results, between 1 and M.
#
  v = rng.integers ( low = 1, high = m, size = n, endpoint = True )

  return v

def roulette_result_test ( rng ):

#*****************************************************************************80
#
## roulette_result_test() tests roulette_result().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'roulette_result_test():' )
  print ( '  roulette_result() returns results of N spins of a roulette' )
  print ( '  wheel with M = 36/37/38 pockets.' )

  m = 36
  n = m * 100

  print ( '' )
  print ( '  M = ', m )
  print ( '  N = ', n )
 
  v = roulette_result ( m, n, rng )

  v = np.sort ( v )

  bar_num, bar_value, bar_frequency = i4vec_sorted_unique_hist ( n, v )

  print ( '' )
  print ( '  Value, Frequency' )
  print ( np.c_ [ bar_value, bar_frequency ] )

  return

def roulette_simulation_test ( ):

#*****************************************************************************80
#
## roulette_simulation_test() tests roulette_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'roulette_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test roulette_simulation().' )

  rng = default_rng ( )

  roulette_result_test ( rng )
  roulette_value_test ( rng )
  i4vec_sorted_unique_hist_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'roulette_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def roulette_value ( m, n, v, bet, b ):

#*****************************************************************************80
#
## roulette_value() returns the value of a roulette bet.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of pockets on a roulette wheel.
#    36, a fair roulette wheel.
#    37, a European roulette wheel.  Pocket 37 is "0".
#    38, a Las Vegas roulette wheel.  Pocket 37 is "0" and 38 is "00".
#
#    integer N, the number of results requested.
#
#    integer V(N), N results, between 1 and M.
#
#    integer BET, the amount of the bet.
#
#    integer set B(L), the pockets in the bet.
#
#  Output:
#
#    integer X(N), the payoff for each result.
#
  import numpy as np

  l = len ( b )

  factor = ( 36 / l ) - 1

  x = np.zeros ( n )

  for i in range ( 0, n ):
    if ( v[i] in b ):
      x[i] = bet * factor
    else:
      x[i] = - bet

  return x

def roulette_value_test ( rng ):

#*****************************************************************************80
#
## roulette_value_test() tests roulette_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'roulette_value_test():' )
  print ( '  roulette_value() returns the value of N spins of a roulette' )
  print ( '  wheel with M = 36/37/38 pockets.' )
  print ( '' )
  print ( '  Here, we bet $10 on red every time.' )
  print ( '' )
  print ( '       M=36        M=37        M=38' )
  print ( '' )
#
#  Use a fair wheel, and spin in many times.
#
  for m in range ( 36, 39 ):

    n = m * 100

    v = roulette_result ( m, n, rng )
#
#  Bet $10 every time.
#
    bet = 10.0
#
#  Bet on red every time.
#
    b = bet_red ( )
#
#  What is the value of my bet on every turn?
#
    value = roulette_value ( m, n, v, bet, b )
#
#  What is the total return of my bets?
#
    result = np.sum ( value )

    print ( '  %10g' % ( result ), end = '' )

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
  roulette_simulation_test ( )
  timestamp ( )

