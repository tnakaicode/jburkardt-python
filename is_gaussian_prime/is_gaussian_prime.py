#! /usr/bin/env python3
#
def gaussian_prime_complex_values ( n_data ):

#*****************************************************************************80
#
## gaussian_prime_complex_values() returns values of complex Gaussian primes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 January 2023
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
#    complex p: a Gaussian prime.
#
  import numpy as np

  n_max = 18

  p_vec = np.array ( [ \
    -5-4j, \
    -5-2j, \
    -5+2j, \
    -4-5j, \
    -3-2j, \
    -3+0j, \
    -2-5j, \
    -2-1j, \
    -1-2j, \
    -1-1j, \
     0+3j, \
     1-4j, \
     1-2j, \
     1-1j, \
     2-3j, \
     3+0j, \
     4+1j, \
     5+4j ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    p = 0 + 0j
  else:
    p = p_vec[n_data]
    n_data = n_data + 1

  return n_data, p

def gaussian_prime_real_values ( n_data ):

#*****************************************************************************80
#
## gaussian_prime_real_values() returns values of real Gaussian primes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 January 2023
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
#    real p: a Gaussian prime.
#
  import numpy as np

  n_max = 18

  p_vec = np.array ( [ \
      3, \
      7, \
     11, \
     19, \
     23, \
     31, \
     43, \
     47, \
     59, \
     67, \
     71, \
     79, \
     83, \
    103, \
    211, \
    307, \
    419, \
    503 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    p = 0 + 0j
  else:
    p = p_vec[n_data]
    n_data = n_data + 1

  return n_data, p

def is_gaussian_prime_complex_test ( ):

#*****************************************************************************80
#
## gaussian_prime_complex_test() tests is_gaussian_prime_complex().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'is_gaussian_prime_complex_test():' )
  print ( '  is_gaussian_prime() decides if a complex integer' )
  print ( '  is a Gaussian prime.' )
  print ( '' )
  print ( '           p          is_gaussian_prime(p)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, p = gaussian_prime_complex_values ( n_data )

    if ( n_data == 0 ):
      break

    tf = is_gaussian_prime ( p )

    if ( tf ):
      ch = ' True'
    else:
      ch = 'False'

    print ( '(%d,%d)  %s' % ( p.real, p.imag, ch ) )

  return

def is_gaussian_prime_generic_test ( ):

#*****************************************************************************80
#
## is_gaussian_prime_generic_test() tests is_gaussian_prime().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'is_gaussian_prime_generic_test():' )
  print ( '  is_gaussian_prime() determines whether a complex number c' )
  print ( '  is a Gaussian prime.' )
  print ( '' )
  print ( '           c          is_gaussian_prime(c)      Correct result' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, c, tf1 = is_gaussian_prime_values ( n_data )

    if ( n_data == 0 ):
      break

    tf2 = is_gaussian_prime ( c )

    if ( tf1 ):
      ch1 = ' True'
    else:
      ch1 = 'False'

    if ( tf2 ):
      ch2 = ' True'
    else:
      ch2 = 'False'

    print ( '(%g,%g),  %s  %s' % ( c.real, c.imag, ch1, ch2 ) )

  return

def is_gaussian_prime ( c ):

#*****************************************************************************80
#
## is_gaussian_prime() reports whether a complex number is a Gaussian prime.
#
#  Discussion:
#
#    Let c be a complex number of the form c = a + bi.
#
#    Then c is a Gaussian prime if 
#      * a and b are integers 
#    and
#      * a is 0 and |b| is prime and |b| mod 4 is 3 or
#      * b is 0 and |a| is prime and |a| mod 4 is 3 or
#      * neither a nor b is zero, and a^2+b^2 is prime.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex c: the number to be tested.
#
#  Output:
#
#    logical value: true if c is a Gaussian prime.
#
  from sympy import isprime

  a = int ( abs ( c.real ) )
  b = int ( abs ( c.imag ) )
#
#  A and B must be integers.
#
  if ( c.real != round ( c.real ) ):
    value = False

  elif ( c.imag != round ( c.imag ) ):
    value = False
#
#  If one is zero, the other must be a prime with remainder 3 mod 4.
#
  elif ( a == 0 ):
    value = ( isprime ( b ) and ( ( b % 4 ) == 3 ) )

  elif ( b == 0 ):
    value = ( isprime ( a ) and ( ( a % 4 ) == 3 ) )
#
#  If both are nonzero, then a^2+b^2 must be prime.
#
  else:
    value = isprime ( a * a + b * b )

  return value

def is_gaussian_prime_real_test ( ):

#*****************************************************************************80
#
## is_gaussian_prime_real_test() tests is_gaussian_prime_real().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2023
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'is_gaussian_prime_real_test():' )
  print ( '  is_gaussian_prime_real() determines if a real integer' )
  print ( '  is a Gaussian prime.' )
  print ( '' )
  print ( '           p          is_gaussian_prime(p)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, p = gaussian_prime_real_values ( n_data )

    if ( n_data == 0 ):
      break

    tf = is_gaussian_prime ( p )

    if ( tf ):
      ch = ' True'
    else:
      ch = 'False'

    print ( '%d  %s' % ( p, ch ) )

  return

def is_gaussian_prime_test ( ):

#*****************************************************************************80
#
## is_gaussian_prime_test() tests is_gaussian_prime().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'is_gaussian_prime_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test is_gaussian_prime()' )

  is_gaussian_prime_real_test ( )
  is_gaussian_prime_complex_test ( )
  is_gaussian_prime_generic_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'is_gaussian_prime_test():' )
  print ( '  Normal end of execution.' )

  return

def is_gaussian_prime_values ( n_data ):

#*****************************************************************************80
#
## is_gaussian_prime_values() returns some values of the is_gaussian_prime() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n_data: The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data: On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    complex c: a value to be checked.
#
#    boolean tf: is True if c is a Gaussian prime.
#
  import numpy as np

  n_max = 24;

  c_vec = np.array ( [ \
          0+0j, \
          3+0j, \
          2+0j, \
          7+0j, \
         12+0j, \
         11+0j, \
        509+0j, \
        503+0j, \
        2.5+0j, \
    -5-4j, \
       6j, \
    -4-5j, \
     4-3j, \
    -3-2j, \
    -3+3j, \
    -2-5j, \
    +1+5j, \
    -1-2j, \
     3+1j, \
     1-4j, \
       1j, \
     2-3j, \
     7+3j, \
     4+1j ] )

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
            True, \
            False, \
            True ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    c = 0 + 0j
    tf = False
  else:
    c = c_vec[n_data]
    tf = tf_vec[n_data]
    n_data = n_data + 1

  return n_data, c, tf

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
  is_gaussian_prime_test ( )
  timestamp ( )


