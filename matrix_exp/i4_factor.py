#! /usr/bin/env python
#
def i4_factor ( n ):

#*****************************************************************************80
#
## I4_FACTOR factors an integer into prime factors.
#
#  Discussion:
#
#    N = NLEFT * Product ( 1 <= I <= NFACTOR ) FACTOR(I)^EXPONENT(I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the integer to be factored.  N may be positive,
#    negative, or 0.
#
#    Output, integer NFACTOR, the number of prime factors of N discovered
#    by the routine.
#
#    Output, integer FACTOR(NFACTOR), the prime factors of N.
#
#    Output, integer EXPONENT(NFACTOR).  EXPONENT(I) is the power of
#    the FACTOR(I) in the representation of N.
#
#    Output, integer NLEFT, the factor of N that the routine could not
#    divide out.  If NLEFT is 1, then N has been completely factored.
#    Otherwise, NLEFT represents factors of N involving large primes.
#
  import numpy as np
  from prime import prime

  nfactor = 0

  factor_list = []
  exponent_list = []

  nleft = n

  if ( n == 0 ):
    factor = np.zeros ( 0 )
    exponent = np.zeros ( 0 )
    return nfactor, factor, exponent, nleft

  if ( abs ( n ) == 1 ):
    nfactor = 1
    factor_list.append ( 1 )
    exponent_list.append ( 0 )
    factor = np.ones ( 1 )
    exponent = np.zeros ( 1 )
    return nfactor, factor, exponent, nleft
#
#  Find out how many primes we stored.
#
  maxprime = prime ( -1 )
#
#  Try dividing the remainder by each prime.
#
  for i in range ( 1, maxprime + 1 ):

    p = prime ( i )

    if ( ( abs ( nleft ) ) % p == 0 ):

      nfactor = nfactor + 1
      factor_list.append ( p )
      exponent_list.append ( 0 )

      while ( True ):

        exponent_list[nfactor-1] = exponent_list[nfactor-1] + 1
        nleft = ( nleft // p )

        if ( ( abs ( nleft ) ) % p != 0 ):
          break

      if ( abs ( nleft ) == 1 ):
        break

  factor = np.zeros ( nfactor )
  exponent = np.zeros ( nfactor )
  for i in range ( 0, nfactor ):
    factor[i] = factor_list[i]
    exponent[i] = exponent_list[i]
  return nfactor, factor, exponent, nleft

def i4_factor_test ( ):

#*****************************************************************************80
#
## I4_FACTOR_TEST tests I4_FACTOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_FACTOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_FACTOR factors an integer.' )

  n = 2 * 2 * 17 * 37

  print ( '' )
  print ( '  The integer is %d' % ( n ) )

  nfactor, factor, power, nleft = i4_factor ( n )

  print ( '' )
  print ( '  Prime representation:' )
  print ( '' )
  print ( '  I, FACTOR(I), POWER(I)' )
  print ( '' )
  if ( abs ( nleft ) != 1 ):
    print ( '  %6d  %6d  (UNFACTORED PORTION)' % ( 0, nleft ) )

  for i in range ( 0, nfactor ):
    print ( '  %6d  %6d  %6d' % ( i, factor[i], power[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_FACTOR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_factor_test ( )
  timestamp ( )

