#! /usr/bin/env python3
#
def prime_fermat_test ( ):

#*****************************************************************************80
#
## prime_fermat_test() tests prime_fermat().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'prime_fermat_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )

  print ( '  prime_fermat() applies Fermat\'s primality test to an integer.' )

  k = 3
  print ( '' )
  print ( '  The test will be repeated with ', k, ' different bases.' )
  print ( '' )

  for n in [ 11, 15, 221 ]:

    value = is_prime_fermat ( n, k )
    if ( value ):
      print ( '  ', n, ' may be a prime.' )
    else:
      print ( '  ', n, ' is definitely not a prime.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'prime_fermat_test():' )
  print ( '  Normal end of execution.' )

  return

def gcd ( i, j ):

#*****************************************************************************80
#
## gcd() finds the greatest common divisor of I and J.
#
#  Discussion:
#
#    Only the absolute values of I and J are
#    considered, so that the result is always nonnegative.
#
#    If I or J is 0, i4_gcd is returned as max ( 1, abs ( I ), abs ( J ) ).
#
#    If I and J have no common factor, i4_gcd is returned as 1.
#
#    Otherwise, using the Euclidean algorithm, i4_gcd is the
#    largest common factor of I and J.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, two numbers whose greatest common divisor
#    is desired.
#
#  Output:
#
#    integer VALUE, the greatest common divisor of I and J.
#
  value = 1
#
#  Return immediately if either I or J is zero.
#
  if ( i == 0 ):
    value = max ( 1, abs ( j ) )
    return value
  elif ( j == 0 ):
    value = max ( 1, abs ( i ) )
    return value
#
#  Set IP to the larger of I and J, IQ to the smaller.
#  This way, we can alter IP and IQ as we go.
#
  ip = max ( abs ( i ), abs ( j ) )
  iq = min ( abs ( i ), abs ( j ) )
#
#  Carry out the Euclidean algorithm.
#
  while ( True ):

    ir = ( ip % iq )

    if ( ir == 0 ):
      break

    ip = iq
    iq = ir

  value = iq

  return value

def is_prime_fermat ( n, k ):

#*****************************************************************************80
#
## is_prime_fermat() applies Fermat's test for primality.
#
#  Discussion:
#
#    The test is only probabilistic.
#    If the input n is a prime, is_prime(n) will be true.
#    If n is not prime, then is_prime(n) is probably false.
#    Reliability can be increased by increasing the value of k, which
#    repeats the test with different bases.
#    However, there are some values of n which are not prime, but for
#    which is_prime(n) will always return true.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2024
#
#  Author:
#
#    Original C++ code on Geeks for Geeks.
#    This version by John Burkardt.
#
#  Reference:
#
#    Thomas Cormen, Charles Leiserson, Ronald Rivest, Clifford Stein,
#    Introduction to Algorithms,
#    Section 31.8: Primality testing,
#    MIT Press McGraw-Hill, 2001.
#
#  Input:
#
#    integer n: the value to be tested.
#
#    integer k: the number of times the test is to be carried out.
#
#  Output:
#
#    boolean value: true if n passed the Fermat test.
#
  from numpy.random import default_rng

  rng = default_rng ( )

  if ( n <= 1 or n == 4 ):
    value = False
    return value

  if ( n <= 3 ):
    value = True
    return value
#
#  Do the test k times.
#
  for i in range ( 0, k ):
#
#  Pick a random number in [2..n-2]  
#
    a = rng.integers ( low = 2, high = n - 2, endpoint = True )      
# 
#  Checking that a and n are co-prime.
#
    if ( gcd ( n, a ) != 1 ):
      value = False
      return value
#
#  Check Fermat's little theorem.
#
    if ( prime_power ( a, n - 1, n ) != 1 ):
      value = False
      return value
 
  value = True

  return value

def prime_power ( a, n, p ):

#*****************************************************************************80
#
## prime_power() computes a^n mod p.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 September 2024
#
#  Author:
#
#    Original C++ code on Geeks for Geeks.
#    This version by John Burkardt.
#
#  Input:
#
#    integer a: the base.
#
#    integer n: the power.
#
#    integer p: the calculation is to be done mod p.
#
#  Output:
#
#    integer value: the value of a^n mod p.
#
  value = 1
#
#  Reduce a if p <= a.
#
  a = ( a % p )
 
  while ( 0 < n ):
#
#  If n is odd, multiply by a.
#
    if ( ( n % 2 ) == 1 ):
      value = ( ( value * a ) % p )
#
#  Divide n by 2.
#
    n = n // 2
    a = ( ( a * a ) % p )

  return value

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
  prime_fermat_test ( )
  timestamp ( )

