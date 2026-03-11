#! /usr/bin/env python3
#
def is_prime_test ( ):

#*****************************************************************************80
#
## is_prime_test() tests is_prime().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'is_prime_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test is_prime()' )

  isprime_test ( )
  is_prime1_test ( )
  is_prime2_test ( )
  is_prime3_test ( )
  is_prime4_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'is_prime_test():' )
  print ( '  Normal end of execution.' )

  return

def is_prime1 ( n ):

#*****************************************************************************80
#
## is_prime1() reports whether an integer is prime.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the value to be tested.
#
#  Output:
#
#    logical value: true if n is a prime.
#
#    integer d: the number of times the mod function was used.
#
  if ( n != int ( n ) ):
    raise Exception ( 'is_prime1(): input n is not an integer!' )

  d = 0

  if ( n <= 0 ):
    value = False
    return value, d

  if ( n == 1 ):
    value = False
    return value, d

  value = True
  for i in range ( 2, n ):
    d = d + 1
    if ( ( n % i ) == 0 ):
      value = False

  return value, d

def is_prime1_test ( ):

#*****************************************************************************80
#
## is_prime1_test() tests is_prime1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'is_prime1_test():' )
  print ( '  is_prime1() returns values of the is_prime() function.' )
  print ( '' )
  print ( '           n          is_prime(n)          is_prime1(n)   mod values' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, tf1 = is_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    tf2, d = is_prime1 ( n )

    print ( '%12d  %5s  %5s  %12d' % ( n, tf1, tf2, d ) )

  return

def is_prime2 ( n ):

#*****************************************************************************80
#
## is_prime2() reports whether an integer is prime.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the value to be tested.
#
#  Output:
#
#    logical value: true if n is a prime.
#
#    integer d: the number of times the mod function was used.
#
  d = 0

  if ( n != int ( n ) ):
    raise Exception ( 'is_prime2(): input n is not an integer!' )

  if ( n <= 0 ):
    value = False
    return value, d

  if ( n == 1 ):
    value = False
    return value, d

  value = True
  for i in range ( 2, n ):
    d = d + 1
    if ( ( n % i ) == 0 ):
      value = False
      break

  return value, d

def is_prime2_test ( ):

#*****************************************************************************80
#
## is_prime2_test() tests is_prime2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'is_prime2_test():' )
  print ( '  is_prime2() returns values of the is_prime() function.' )
  print ( '' )
  print ( '           n          is_prime(n)          is_prime2(n)   mod values' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, tf1 = is_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    tf2, d = is_prime2 ( n )

    print ( '%12d  %5s  %5s  %12d' % ( n, tf1, tf2, d ) )

  return

def is_prime3 ( n ):

#*****************************************************************************80
#
## is_prime3() reports whether an integer is prime.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the value to be tested.
#
#  Output:
#
#    logical value: true if n is a prime.
#
#    integer d: the number of times the mod function was used.
#
  from math import sqrt

  d = 0

  if ( n != int ( n ) ):
    raise Exception ( 'is_prime3(): input n is not an integer!' )

  if ( n <= 0 ):
    value = False
    return value, d

  if ( n == 1 ):
    value = False
    return value, d

  n_sqrt = int ( sqrt ( n ) )

  for i in range ( 2, n_sqrt + 1 ):
    d = d + 1
    if ( ( n % i ) == 0 ):
      value = False
      return value, d

  value = True

  return value, d

def is_prime3_test ( ):

#*****************************************************************************80
#
## is_prime3_test() tests is_prime3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'is_prime3_test():' )
  print ( '  is_prime3() returns values of the is_prime() function.' )
  print ( '' )
  print ( '           n          is_prime(n)          is_prime3(n)   mod values' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, tf1 = is_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    tf2, d = is_prime3 ( n )

    print ( '%12d  %5s  %5s  %12d' % ( n, tf1, tf2, d ) )

  return

def is_prime4 ( n ):

#*****************************************************************************80
#
## is_prime4() reports whether an integer is prime.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the value to be tested.
#
#  Output:
#
#    logical value: true if n is a prime.
#
#    integer d: the number of times the mod function was used.
#
  from math import sqrt

  d = 0

  if ( n != int ( n ) ):
    raise Exception ( 'is_prime4(): input n is not an integer!' )

  if ( n <= 1 ):
    value = False
    return value, d

  if ( ( n == 2 ) or ( n == 3 ) ):
    value = True
    return value, d

  d = d + 1
  if ( ( n % 2 ) == 0 ):
    value = False
    return value, d

  d = d + 1
  if ( ( n % 3 ) == 0 ):
    value = False
    return value, d

  sqrt_n = int ( sqrt ( n ) )

  for i in range ( 5, sqrt_n + 1, 6 ):
    d = d + 1
    if ( ( n % i ) == 0 ):
      value = False
      return value, d
    d = d + 1
    if ( ( n % ( i + 2 ) ) == 0 ):
      value = False
      return value, d

  value = True

  return value, d

def is_prime4_test ( ):

#*****************************************************************************80
#
## is_prime4_test() tests is_prime4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 January 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'is_prime4_test():' )
  print ( '  is_prime4() returns values of the is_prime() function.' )
  print ( '' )
  print ( '           n          is_prime(n)          is_prime4(n)   mod values' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, tf1 = is_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    tf2, d = is_prime4 ( n )

    print ( '%12d  %5s  %5s  %12d' % ( n, tf1, tf2, d ) )

  return

def isprime_test ( ):

#*****************************************************************************80
#
## isprime_test() tests isprime().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2022
#
#  Author:
#
#    John Burkardt
#
  from sympy import isprime

  print ( '' )
  print ( 'isprime_test():' )
  print ( '  isprime() returns values of the is_prime() function.' )
  print ( '' )
  print ( '           n          is_prime(n)          isprime(n)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, tf1 = is_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    tf2 = isprime ( n )

    print ( '%12d  %5s  %5s' % ( n, tf1, tf2 ) )

  return

def is_prime_values ( n_data ):

#*****************************************************************************80
#
## is_prime_values() returns some values of the is_prime() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n_data: The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data: On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    integer n: a value to be checked.
#
#    boolean tf: is True if n is prime.
#
  import numpy as np

  n_max = 22;

  n_vec = np.array ( [ \
          1, \
          2, \
         12, \
          3, \
         91, \
         53, \
        437, \
        311, \
       1333, \
        719, \
      16483, \
       7919, \
     223609, \
      81799, \
     873599, \
     800573, \
    5693761, \
    7559173, \
   90166053, \
   69600977, \
    6110601, \
  145253029 ] )

  tf_vec = np.array ( [ \
            False, \
            True, \
            False, \
            True, \
            False, \
            True, \
            False, \
            True, \
            False, \
            True, \
            False, \
            True, \
            False, \
            True, \
            False, \
            True, \
            False, \
            True, \
            False, \
            True, \
            False, \
            True ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    tf = False
  else:
    n = n_vec[n_data]
    tf = tf_vec[n_data]
    n_data = n_data + 1

  return n_data, n, tf

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
  is_prime_test ( )
  timestamp ( )

