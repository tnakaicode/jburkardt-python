#! /usr/bin/env python3
#
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
#    29 December 2022
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
  from math import sqrt

  if ( n != int ( n ) ):
    raise Exception ( 'is_prime3(): input n is not an integer!' )

  if ( n <= 1 ):
    value = False
    return value

  if ( ( n == 2 ) or ( n == 3 ) ):
    value = True
    return value

  if ( ( ( n % 2 ) == 0 ) or ( ( n % 3 ) == 0 ) ):
    value = False
    return value

  sqrt_n = int ( sqrt ( n ) )

  for i in range ( 5, sqrt_n + 1, 6 ):
    if ( ( ( n % i ) == 0 ) or ( ( n % ( i + 2 ) ) == 0 ) ):
      value = False
      return value

  value = True
  return value

def pi_values ( n_data ):

#*****************************************************************************80
#
## pi_values() returns values of the Pi function.
#
#  Discussion:
#
#    Pi[n] is the number of primes less than or equal to n.
#
#    In Mathematica, the function can be evaluated by:
#
#      PrimePi[n]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_data.  The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer N_data.  On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    integer N, the argument.
#
#    integer P, the value of the function.
#
  import numpy as np

  n_max = 21

  n_vec = np.array ( [ \
            1, \
            2, \
            4, \
            8, \
           16, \
           32, \
           64, \
          128, \
          256, \
          512, \
         1024, \
         2048, \
         4096, \
         8192, \
        16384, \
        32768, \
        65536, \
       131072, \
       262144, \
       524288, \
      1048576 ] )

  p_vec = np.array ( [ \
             0, \
             1, \
             2, \
             4, \
             6, \
            11, \
            18, \
            31, \
            54, \
            97, \
           172, \
           309, \
           564, \
          1028, \
          1900, \
          3512, \
          6542, \
         12251, \
         23000, \
         43390, \
         82025  ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    p = 0
  else:
    n = n_vec[n_data]
    p = p_vec[n_data]
    n_data = n_data + 1

  return n_data, n, p

def prime_pi_plot ( ):

#*****************************************************************************80
#
## prime_pi_plot() plots pi(n) versus x/log(x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  
  n_vec = np.array ( [ \
            2, \
            4, \
            8, \
           16, \
           32, \
           64, \
          128, \
          256, \
          512, \
         1024, \
         2048, \
         4096, \
         8192, \
        16384, \
        32768, \
        65536, \
       131072, \
       262144, \
       524288, \
      1048576 ] )
      
  logn = np.log ( n_vec )

  pi_vec = np.array ( [ \
             1, \
             2, \
             4, \
             6, \
            11, \
            18, \
            31, \
            54, \
            97, \
           172, \
           309, \
           564, \
          1028, \
          1900, \
          3512, \
          6542, \
         12251, \
         23000, \
         43390, \
         82025  ] )
         
  nlogn = n_vec / logn
  
  plt.clf ( )
  plt.plot ( n_vec, pi_vec, 'b-', linewidth = 3 )
  plt.plot ( n_vec, nlogn, 'r-', linewidth = 3 )
  plt.legend ( [ 'Pi(n)', 'n/log(n)' ] )
  plt.grid ( True )
  plt.xlabel ( '<-- n -->' )
  plt.ylabel ( 'Pi(n)' )
  plt.title ( r'$\Pi(n) \approx \frac{n}{\log(n)}$' )
  filename = 'prime_pi.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return
  
def prime_pi1 ( n ):

#*****************************************************************************80
#
## prime_pi1() evaluates prime(n), the number of primes less than or equal to n.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2022
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
#    integer value: the value of pi(n).
#
  if ( n != int ( n ) ):
    raise Exception ( 'prime_pi1(): input n is not an integer!' )

  value = 0
  for i in range ( 1, n + 1 ):
    value = value + is_prime3 ( i )

  return value

def prime_pi2 ( n ):

#*****************************************************************************80
#
## prime_pi2() evaluates prime(n), the number of primes less than or equal to n.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2022
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
#    integer value: the value of pi(n).
#
  from sympy import isprime

  if ( n != int ( n ) ):
    raise Exception ( 'prime_pi2(): input n is not an integer!' )

  value = 0
  for i in range ( 1, n + 1 ):
    value = value + isprime ( i )

  return value

def prime_pi_test ( ):

#*****************************************************************************80
#
## prime_pi_test() tests prime_pi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'prime_pi_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test prime_pi()' )

  prime_pi1_test ( )
  prime_pi2_test ( )
  prime_pi_plot ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'prime_pi_test():' )
  print ( '  Normal end of execution.' )

  return

def prime_pi1_test ( ):

#*****************************************************************************80
#
## prime_pi1_test() tests prime_pi1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'prime_pi1_test():' )
  print ( '  Test prime_pi1()' )
  print ( '           n          Pi(n)          prime_pi1(n)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, pi1 = pi_values ( n_data )

    if ( n_data == 0 ):
      break

    pi2 = prime_pi1 ( n )

    print ( '%12d  %10d  %10d' % ( n, pi1, pi2 ) )

  return

def prime_pi2_test ( ):

#*****************************************************************************80
#
## prime_pi2_test() tests prime_pi2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'prime_pi2_test():' )
  print ( '  Test prime_pi2()' )
  print ( '           n          Pi(n)          prime_pi2(n)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, pi1 = pi_values ( n_data )

    if ( n_data == 0 ):
      break

    pi2 = prime_pi2 ( n )

    print ( '%12d  %10d  %10d' % ( n, pi1, pi2 ) )

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
  prime_pi_test ( )
  timestamp ( )

