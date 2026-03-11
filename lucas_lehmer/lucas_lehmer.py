#! /usr/bin/env python3
#
def lucas_lehmer_test ( ):

#*****************************************************************************80
#
## lucas_lehmer_test() tests lucas_lehmer().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 January 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'lucas_lehmer_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test lucas_lehmer().' )

  for n in [ 2, 3, 5, 7, 11, 13, 17, 19, 31, 61, 67, 89, 107, 127, 257, 2047 ]:
    prime = lucas_lehmer ( n )
    if ( prime ):
      print ( '  2^' + str ( n ) + '-1 is prime' )
    else:
      print ( '  2^' + str ( n ) + '-1 is NOT prime' )
#
#  Terminate.
#
  print ( '' )
  print ( 'lucas_lehmer_test():' )
  print ( '  Normal end of execution.' )

  return
def lucas_lehmer ( n ):

#*****************************************************************************80
#
## lucas_lehmer() determines whether a Mersenne number is prime.
#
#  Discussion:
#
#    A Mersenne number has the form Mn=2^n-1.
#    If n is not prime, then Mn is not prime.
#    There are many prime indices for which Mn is prime, but a prime
#    index n does not by itself guarantee that Mn is prime.
#
#    If n is the index of a Mersenne number Mn, and n is prime, 
#    then the Lucas-Lehmer test will show whether Mn is prime.
#
#    The lowest prime for which Mn is not prime is n=11.
#    Two other examples of n for which Mn is not prime are 67 and 257
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 January 2023
#
#  Author:
#
#    Original Python version by John D Cook.
#    This version by John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Searching for Mersenne primes,
#    https://www.johndcook.com/blog/2018/11/28/searching-for-mersenne-primes/
#    Posted 28 November 2018.
#
#  Input:
#
#    integer n: the index of the Mersenne number. 
#    Typically, n is prime.
#
#  Output:
#
#    logical prime: True if Mn is prime.
#
  if ( n == 2 ):
    return True

  Mn = 2**n - 1
  s = 4
  for _ in range ( n - 2 ):
    s = ( ( s * s - 2 ) % Mn )

  return ( s == 0 )

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
  lucas_lehmer_test ( )
  timestamp ( )

