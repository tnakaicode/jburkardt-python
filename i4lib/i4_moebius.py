#! /usr/bin/env python
#
def i4_moebius ( n ):

#*****************************************************************************80
#
## I4_MOEBIUS returns the value of MU(N), the Moebius function of N.
#
#  Discussion:
#
#    MU(N) is defined as follows:
#
#      MU(N) = 1 if N = 1
#              0 if N is divisible by the square of a prime
#              (-1)^K, if N is the product of K distinct primes.
#
#  First values:
#
#     N  MU(N)
#
#     1    1
#     2   -1
#     3   -1
#     4    0
#     5   -1
#     6    1
#     7   -1
#     8    0
#     9    0
#    10    1
#    11   -1
#    12    0
#    13   -1
#    14    1
#    15    1
#    16    0
#    17   -1
#    18    0
#    19   -1
#    20    0
#
#    As special cases, MU(N) is -1 if N is a prime, and MU(N) is 0
#    if N is a square, cube, etc.
#
#    The Moebius function MU(D) is related to Euler's totient 
#    function PHI(N):
#
#      PHI(N) = sum ( D divides N ) MU(D) * ( N / D ).
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
#    Input, integer N, the value to be analyzed.
#
#    Output, integer MU, the value of MU(N).
#    If N is less than or equal to 0, MU will be returned as -2.
#    If there was not enough internal space for factoring, MU
#    is returned as -3.
#
  from i4_factor import i4_factor

  if ( n <= 0 ):
    mu = -2
    return mu

  if ( n == 1 ):
    mu = 1
    return mu
#
#  Factor N.
#
  nfactor, factor, exponent, nleft =  i4_factor ( n  )

  if ( nleft != 1 ):
    print ( '' )
    print ( 'I4_MOEBIUS - Warning!' )
    print ( '  Not enough factorization space.' )
    mu = -3
    return mu

  mu = 1

  for i in range ( 0, nfactor ):

    mu = - mu

    if ( 1 < exponent[i] ):
      mu = 0
      return mu

  return mu

def i4_moebius_test ( ):

#*****************************************************************************80
#
## I4_MOEBIUS_TEST tests I4_MOEBIUS.
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
  from moebius_values import moebius_values

  print ( '' )
  print ( 'I4_MOEBIUS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_MOEBIUS evaluates the Moebius function:' )
  print ( '' )
  print ( '         N      Exact         I4_MOEBIUS(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c1 = moebius_values ( n_data )

    if ( n_data == 0 ):
      break

    c2 = i4_moebius ( n )

    print ( '  %8d  %12d  %12d' % ( n, c1, c2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_MOEBIUS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_moebius_test ( )
  timestamp ( )

