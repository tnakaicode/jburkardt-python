#! /usr/bin/env python3
#
def euclid_test ( ):

#*****************************************************************************80
#
## euclid_test() tests euclid().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'euclid_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test euclid( ).' )

  gcd_test ( )
  gcd1_test ( )
  gcd2_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'euclid_test():' )
  print ( '  Normal end of execution.' )

  return

def gcd1 ( a, b ):

#*****************************************************************************80
#
## gcd1() computes the greatest common divisor of two integers.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer a, b: two integers whose gcd is desired.  Neither value should be 0.
#
#  Output:
#
#    integer g: the GCD of a and b.
#
  if ( not ( a == int ( a ) ) ):
    raise Exception ( 'gcd1(): input a is not an integer!' )

  if ( a == 0 ):
    raise Exception ( 'gcd1(): input a is zero!' )

  if ( not ( b == int ( b ) ) ):
    raise Exception ( 'gcd1(): input b is not an integer!' )

  if ( b == 0 ):
    raise Exception ( 'gcd1(): input b is zero!' )
#
#  Clean up input.
#
  a = abs ( a )
  b = abs ( b )

  c = max ( a, b )
  d = min ( a, b )
#
#  Until equal, subtract smaller from larger.
#
  while ( c != d ):

    if ( c < d ):
      d = d - c
    else:
      c = c - d

  g = c

  return g

def gcd1_test ( ):

#*****************************************************************************80
#
## gcd1_test() tests gcd1().
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
  print ( '' )
  print ( 'gcd1_test():' )
  print ( '  gcd1(m,n) computes the greatest common divisor of M and N.' )
  print ( '' )
  print ( '         m         n     gcd(m,n) gcd1(m,n)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, m, n, f1 = gcd_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = gcd1 ( m, n )

    print ( '  %8d  %8d  %8d  %8d' % ( m, n, f1, f2 ) )

  return

def gcd2 ( a, b ):

#*****************************************************************************80
#
## gcd1() computes the greatest common divisor of two integers.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer a, b: two integers whose gcd is desired.  Neither value should be 0.
#
#  Output:
#
#    integer g: the GCD of a and b.
#
  if ( not ( a == int ( a ) ) ):
    raise Exception ( 'gcd2(): input a is not an integer!' )

  if ( a == 0 ):
    raise Exception ( 'gcd2(): input a is zero!' )

  if ( not ( b == int ( b ) ) ):
    raise Exception ( 'gcd2(): input b is not an integer!' )

  if ( b == 0 ):
    raise Exception ( 'gcd2(): input b is zero!' )
#
#  Clean up input.
#
  a = abs ( a )
  b = abs ( b )

  c = max ( a, b )
  d = min ( a, b )
#
#  Replace larger of (a,b) by a mod b.
#
  while ( True ):

    if ( c < d ):
      d = ( d % c )
      if ( d == 0 ):
        g = c
        break
    else:
      c = ( c % d )
      if ( c == 0 ):
        g = d
        break

  return g

def gcd2_test ( ):

#*****************************************************************************80
#
## gcd2_test() tests gcd2().
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
  print ( '' )
  print ( 'gcd2_test():' )
  print ( '  gcd2(m,n) computes the greatest common divisor of M and N.' )
  print ( '' )
  print ( '         m         n     gcd(m,n) gcd2(m,n)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, m, n, f1 = gcd_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = gcd2 ( m, n )

    print ( '  %8d  %8d  %8d  %8d' % ( m, n, f1, f2 ) )

  return

def gcd_test ( ):

#*****************************************************************************80
#
## gcd_test() tests gcd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2022
#
#  Author:
#
#    John Burkardt
#
  from math import gcd

  print ( '' )
  print ( 'gcd_test():' )
  print ( '  gcd(m,n) computes the greatest common divisor of M and N.' )
  print ( '' )
  print ( '         m         n     gcd(m,n) gcd(m,n)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, m, n, f1 = gcd_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = gcd ( m, n )

    print ( '  %8d  %8d  %8d  %8d' % ( m, n, f1, f2 ) )

  return

def gcd_values ( n_data ):

#*****************************************************************************80
#
## gcd_values() returns values of the greatest common divisor function.
#
#  Discussion:
#
#    f = gcd(m,n) if f divides m and n evenly, and no larger integer does.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n_data: the user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data: on each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    integer M, N, the arguments of the function.
#
#    integer F, the value of the function.
#
  import numpy as np

  n_max = 10

  f_vec = np.array ( [ 
    1,  2,  3,  4,  5, \
    6,  7,  8,  9, 10 ] )
  m_vec = np.array ( [ 
    17,    4, 291,    100,    55, \
    30, 2058,  24, 326880, 65610 ] )
  n_vec = np.array ( [ 
    35, 138322, 294,     64,    625, \
    66,    679,  40, 131769, 146410 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    m = 0
    n = 0
    f = 0
  else:
    m = m_vec[n_data]
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, m, n, f

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
  euclid_test ( )
  timestamp ( )


