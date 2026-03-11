#! /usr/bin/env python3
#
def prime_miller_rabin_test ( ):

#*****************************************************************************80
#
## prime_miller_rabin_test() tests prime_miller_rabin().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 September 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'prime_miller_rabin_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  prime_miller_rabin() tests an integer for primality.' )
  print ( '  The test is always true for a prime.' )
  print ( '  The test is usually false for a composite number.' )

  for k in [ 1, 3, 5 ]:

    print ( ' ' )
    print ( '  Apply the test', k, ' times.' )

    print ( '' )
    print ( '       n  prime  miller' )
    print ( '' )
    for n, is_prime in [ \
      [ 3,     True ], \
      [ 30,    False ], \
      [ 561,   False ], \
      [ 1105,  False ], \
      [ 1729,  False ], \
      [ 13441, True ], \
      [ 13443, False ] ]:
      value = is_prime_miller_rabin ( n, k )
      print ( '  %6d  %5s  %5s' % ( n, is_prime, value ) ) 
#
#  Terminate.
#
  print ( '' )
  print ( 'prime_miller_rabin_test():' )
  print ( '  Normal end of execution.' )

  return

def is_prime_miller_rabin ( n, k = 5 ): 

#*****************************************************************************80
#
## is_prime_miller_rabin() applies the Miller-Rabin test k times to an integer n.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the value to be tested.
#
#    integer k: the number of times to test n.
#
#  Output:
#
#    logical value: True if n passed the test every time.
#
  if ( n <= 1 ):
    return False

  if ( n <= 3 ):
    return True

  if ( n % 2 == 0 ):
    return False
    
  d = n - 1
  while ( d % 2 == 0 ):
    d //= 2
    
  for tests in range ( k ):
    if ( not miller_rabin_test ( d, n ) ):
      return False

  return True

def miller_rabin_test ( d, n ):

#*****************************************************************************80
#
## miller_rabin_test() applies the Miller-Rabin test to an integer n.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 September 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer d: initially set to n-1, but factors of 2 have been
#    divided out.
#
#    integer n: the integer to be tested.
#
#  Output:
#
#    logical value:
#
  import random
#
#  Pick a base randomly: 2 <= a <= n-2.
#
  a = random.randint ( 2, n - 2 )
#
#  x = a^d mod n
#
  x = pow ( a, d, n )

  if ( x == 1 or x == n - 1 ):
    return True

  while ( d != n - 1 ):
    x = ( x * x ) % n
    d = d * 2
    if ( x == 1 ):
      return False
    if ( x == n - 1 ):
      return True

  return False

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
  prime_miller_rabin_test ( )
  timestamp ( )

