#! /usr/bin/env python3
#
def change_polynomial ( value, target, coin_num ):

#*****************************************************************************80
#
## change_polynomial() solves the change making problem using a polynomial algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer VALUE(VALUE_NUM), the value of each coin.
#
#    integer TARGET, the maximum desired sum.
#
#    integer COIN_NUM: the exact number of coins to use.
#
#  Output:
#
#    integer A(1:TARGET+1): A(I+1) is the number of sequences of COIN_NUM
#    coins (respecting order) which total the sum of I.
#
  import numpy as np

  a = np.zeros ( target + 1 )

  if ( coin_num <= 0 ):
    return a

  value_num = len ( value )
  for i in range ( 0, value_num ):
    j = value[i]
    a[j] = a[j] + 1

  if ( coin_num == 1 ):
    return a
  
  p = a.copy()
  for i in range ( 1, coin_num ):
    a = polynomial_multiply ( a, p )

  return a
 
def change_polynomial_test ( ):

#*****************************************************************************80
#
## change_polynomial_test() tests change_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'change_polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  change_polynomial() uses a polynomial algorithm to count' )
  print ( '  the number of ways of using a given number of coins to make a sum.' )

  value = np.array ( [ 1, 5, 10, 25 ] )
  target = 75
  coin_num = 3

  a1 = change_polynomial ( value, target, coin_num )
#
#  Adding a coin of value 0 allows us to count ways of using 0 through coin_num coins.
#
  value = np.array ( [ 0, 1, 5, 10, 25 ] )
  target = 75
  coin_num = 3

  a2 = change_polynomial ( value, target, coin_num )

  print ( '' )
  print ( '  Sum  3 coins  0/1/2/3 coins' )
  print ( '' )
  for i in range ( 0, target + 1 ):
    print ( '  %2d     %2d     %2d' % ( i, a1[i], a2[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'change_polynomial_test():' )
  print ( '  Normal end of execution.' )

  return

def polynomial_multiply ( p, q ):

#*****************************************************************************80
#
## polynomial_multiply() multiplies two polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real p(*), q(*): all the coefficients of two polynomials, zero or nonzero.
#
#  Output:
#
#    real r(*): all the coefficients of the product polynomial.
#
  import numpy as np

  pn = len ( p ) - 1
  while ( p[pn] == 0 and 0 < pn ):
    pn = pn - 1

  qn = len ( q ) - 1
  while ( q[qn] == 0 and 0 < qn ):
    qn = qn - 1

  rn = qn + pn + 1
  r = np.zeros ( rn )
  for i in range ( 0, pn + 1 ):
    for j in range ( 0, qn + 1 ):
      k = i + j
      r[k] = r[k] + p[i] * q[j]

  return r

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
  change_polynomial_test ( )
  timestamp ( )

