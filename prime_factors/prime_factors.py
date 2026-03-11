#! /usr/bin/env python3
#
def prime_factors_test ( ):

#*****************************************************************************80
#
## prime_factors_test() tests prime_factors().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'prime_factors_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test prime_factors().' )

  for n in [ 61, 75, 3628800, 123456789 ]:
    factors = prime_factors ( n )
    print ( '' )
    print ( '  Prime factors of', n )
    print ( factors )
#
#  Terminate.
#
  print ( '' )
  print ( 'prime_factors_test():' )
  print ( '  Normal end of execution.' )

  return

def prime_factors ( n ):

#*****************************************************************************80
#
## prime_factors() returns the prime factors of an integer.
#
#  Discussion:
#
#    Repeated factors will be listed multiple times.
#    For instance, 75 = 3 * 5 * 5 so
#    factors = [ 3, 5, 5 ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: a number whose prime factorization is desired.
#
#  Output:
#
#    integer factors{}: a list of the prime factors of n.
#
  if ( type ( n ) != int ):
    raise Exception ( 'prime_factors(): Input n is not an integer.' )

  if ( n < 1 ):
    raise Exception ( 'prime_factors(): Input integer n is less than 1.' )

  i = 2
  factors = []

  while ( i * i <= n ):

    if ( n % i ):
      i = i + 1
    else:
      n //= i
      factors.append(i)
#
#  This happens if n is prime.
#
  if ( 1 < n ):
    factors.append(n)

  return factors

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
  prime_factors_test ( )
  timestamp ( )

