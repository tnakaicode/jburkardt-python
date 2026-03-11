#! /usr/bin/env python3
#
def binom ( n, k ):

#*****************************************************************************80
#
## binom() computes the binomial coefficient.
#
#  Discussion:
#
#    This is ACM algorithm 160 translated.
#
#    It calculates the number of combinations of N things taken K at a time.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    Bill Buckles, Matthew Lybanon
#
#  Reference:
#
#    Bill Buckles, Matthew Lybanon,
#    Algorithm 515: Generation of a Vector from the Lexicographical Index,
#    ACM Transactions on Mathematical Software,
#    Volume 3, Number 2, June 1977, pages 180-182.
#
#  Input:
#
#    integer N, K, the arguments for the binomial coefficient.
#
#  Output:
#
#    integer VALUE, the binomial coefficient.
#

#
#  Force the input arguments to be integers.
#
  n = int ( n )
  k = int ( k )

  k1 = k
  p = n - k1

  if ( k1 < p ):
    p = k1
    k1 = n - p

  if ( p == 0 ):
    r = 1
  else:
    r = k1 + 1

  for i in range ( 2, p + 1 ):
    r = ( r * ( k1 + i ) ) // i

  value = int ( r )

  return value

def comb ( n, p, l ):

#*****************************************************************************80
#
## comb() selects a subset of order P from a set of order N.
#
#  Discussion:
#
#    This subroutine finds the combination set of N things taken
#    P at a time for a given lexicographic index.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    Bill Buckles, Matthew Lybanon
#
#  Reference:
#
#    Bill Buckles, Matthew Lybanon,
#    Algorithm 515: Generation of a Vector from the Lexicographical Index,
#    ACM Transactions on Mathematical Software,
#    Volume 3, Number 2, June 1977, pages 180-182.
#
#  Input:
#
#    integer N, the number of things in the set.
#
#    integer P, the number of things in each combination.
#    0 < P < N.
#
#    integer L, the lexicographic index of the 
#    desired combination.  1 <= L <= choose(N,P).
#
#  Output:
#
#    integer C(P), the combination set.
#
  import numpy as np

  c = np.zeros ( p, dtype = int )
#
#  Special case: P = 1
#
  if ( p == 1 ):
    c[0] = l
    return c
#
#  Initialize lower bound index.
#
  k = 0
#
#  Select elements in ascending order.
#
  p1 = p - 1
  c[0] = 0

  for i in range ( 1, p1 + 1 ):
#
#  Update lower bound as the previously selected element.
#
    if ( 1 < i ):
      c[i-1] = c[i-2]
#
#  Check validity of each entry.
#
    while ( True ):

      c[i-1] = c[i-1] + 1
      r = binom ( n - c[i-1], p - i )
      k = k + r

      if ( l <= k ):
        break

    k = k - r

  c[p-1] = c[p1-1] + l - k

  return c

def comb_test01 ( ):

#*****************************************************************************80
#
## comb_test01() tests comb() by generating all 3-subsets of a 5 set.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5
  k = 3
  lmax = binom ( n, k )

  print ( '' )
  print ( 'comb_test01():' )
  print ( '  Generate all K-subsets of an N set.' )
  print ( '  K = %d' % ( k ) )
  print ( '  N = %d' % ( n ) )
  print ( '  LMAX = %d' % ( lmax ) )

  if ( not i4_choose_check ( n, k ) ):
    print ( '' )
    print ( 'comb_test01 - Warning!' )
    print ( '  The binomial coefficient cannot be' )
    print ( '  computed in integer arithmetic for' )
    print ( '  this choice of parameters.' )
    return

  print ( '' )

  for l in range ( 1, lmax + 1 ):
    c = comb ( n, k, l )
    print ( '  %6d:  ' % ( l ) ),
    for i in range ( 0, k ):
      print ( '  %6d' % ( c[i] ) ),
    print ( '' )

  return

def comb_test02 ( rng ):

#*****************************************************************************80
#
## comb_test02() tests comb() by generating 10 random 3-subsets of a 10 set.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 5
  k = 3
  lmax = binom ( n, k )

  print ( '' )
  print ( 'comb_test02():' )
  print ( '  Generate all K-subsets of an N set.' )
  print ( '  K = %d' % ( k ) )
  print ( '  N = %d' % ( n ) )
  print ( '  LMAX = %d' % ( lmax ) )

  if ( not i4_choose_check ( n, k ) ):
    print ( '' )
    print ( 'comb_test02 - Warning!' )
    print ( '  The binomial coefficient cannot be' )
    print ( '  computed in integer arithmetic for' )
    print ( '  this choice of parameters.' )
    return

  print ( '' )

  for i in range ( 0, 10 ):
    l = rng.integers ( low = 1, high = lmax, endpoint = True )
    c = comb ( n, k, l )
    print ( '  %6d:  ' % ( l ) ),
    for i in range ( 0, k ):
      print ( '  %6d' % ( c[i] ) ),
    print ( '' )

  return

def comb_test03 ( rng ):

#*****************************************************************************80
#
## comb_test03() tests comb() by generating 10 random 3-subsets of a 25 set.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 25
  k = 3
  lmax = binom ( n, k )

  print ( '' )
  print ( 'comb_test03():' )
  print ( '  Generate 10 random K-subsets of an N set.' )
  print ( '  K = %d' % ( k ) )
  print ( '  N = %d' % ( n ) )
  print ( '  LMAX = %d' % ( lmax ) )

  if ( not i4_choose_check ( n, k ) ):
    print ( '' )
    print ( 'comb_test03(): Warning!' )
    print ( '  The binomial coefficient cannot be' )
    print ( '  computed in integer arithmetic for' )
    print ( '  this choice of parameters.' )
    return

  print ( '' )

  for i in range ( 0, 10 ):
    l = rng.integers ( low = 1, high = lmax, endpoint = True )
    c = comb ( n, k, l )
    print ( '  %6d:  ' % ( l ) ),
    for i in range ( 0, k ):
      print ( '  %6d' % ( c[i] ) ),
    print ( '' )

  return
 
def comb_test04 ( rng ):

#*****************************************************************************80
#
## comb_test04() tests comb() by generating 10 random 3-subsets of a 100 set.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 100
  k = 3
  lmax = binom ( n, k )

  print ( '' )
  print ( 'comb_test04():' )
  print ( '  Generate 10 random K-subsets of an N set.' )
  print ( '  K = %d' % ( k ) )
  print ( '  N = %d' % ( n ) )
  print ( '  LMAX = %d' % ( lmax ) )

  if ( not i4_choose_check ( n, k ) ):
    print ( '' )
    print ( 'comb_test04(): Warning!' )
    print ( '  The binomial coefficient cannot be' )
    print ( '  computed in integer arithmetic for' )
    print ( '  this choice of parameters.' )
    return

  print ( '' )

  for i in range ( 0, 10 ):
    l = rng.integers ( low = 1, high = lmax, endpoint = True )
    c = comb ( n, k, l )
    print ( '  %6d:  ' % ( l ) ),
    for i in range ( 0, k ):
      print ( '  %6d' % ( c[i] ) ),
    print ( '' )

  return

def comb_test05 ( rng ):

#*****************************************************************************80
#
## comb_test05() tests comb() by generating 10 random 10-subsets of a 100 set.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 100
  k = 10
  lmax = binom ( n, k )

  print ( '' )
  print ( 'comb_test05():' )
  print ( '  Generate 10 random K-subsets of an N set.' )
  print ( '  K = %d' % ( k ) )
  print ( '  N = %d' % ( n ) )
  print ( '  LMAX = %d' % ( lmax ) )
  print ( '' )
  print ( '  Note that this function is already' )
  print ( '  failing because LMAX is negative.' )
  print ( '  The combinatorial coefficient C(100,10)' )
  print ( '  is too large to store in an integer.' )
  print ( '' )
  print ( '  Although the program continues to give' )
  print ( '  results, they cannot be relied on!' )

  if ( not i4_choose_check ( n, k ) ):
    print ( '' )
    print ( 'comb_test05(): Warning!' )
    print ( '  The binomial coefficient cannot be' )
    print ( '  computed in integer arithmetic for' )
    print ( '  this choice of parameters.' )
    return

  print ( '' )

  for i in range ( 0, 10 ):
    l = rng.integers ( low = 1, high = lmax, endpoint = True )
    c = comb ( n, k, l )
    print ( '  %6d:  ' % ( l ) ),
    for i in range ( 0, k ):
      print ( '  %6d' % ( c[i] ) ),
    print ( '' )

  return

def i4_choose_check ( n, k ):

#*****************************************************************************80
#
## i4_choose_check() reports whether the binomial coefficient can be computed.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, K, the binomial parameters.
#
#  Output:
#
#    bool CHECK is:
#    TRUE, if C(N,K) < maximum integer.
#    FALSE, otherwise.
#
  from scipy.special import gammaln
  import numpy as np

  i4_huge = 2147483647

  i4_huge_log = np.log ( i4_huge )

  choose_nk_log = \
      gammaln ( n + 1 ) \
    - gammaln ( k + 1 ) \
    - gammaln ( n - k + 1 )

  check = ( choose_nk_log < i4_huge_log )
        
  return check

def i4_choose_check_test ( ):

#*****************************************************************************80
#
## i4_choose_check_test() tests i4_choose_check().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  k_test = np.array ( [ 3, 999, 3, 10 ] )
  n_test = np.array ( [ 10, 1000, 100, 100 ] )

  print ( '' )
  print ( 'i4_choose_check_test():' )
  print ( '  i4_choose_check() checks whether C(N,K)' )
  print ( '  can be computed with integer arithmetic' )
  print ( '  or not.' )
  print ( '' )
  print ( '     N     K    CHECK?    i4_choose' )
  print ( '' )
 
  for i in range ( 0, 4 ):
    n = n_test[i]
    k = k_test[i]
    check = i4_choose_check ( n, k )
    print ( '  %4d  %4d        %d' % ( n, k, check ), end = '' )
    if ( check ):
      cnk = i4_choose ( n, k )
      print ( '        %d' % ( cnk ) )
    else:
      print ( '   Not computable' )

  return

def i4_choose ( n, k ):

#*****************************************************************************80
#
## i4_choose() computes the binomial coefficient C(N,K) as an I4.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in integer arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    ML Wolfson, HV Wright,
#    Algorithm 160:
#    Combinatorial of M Things Taken N at a Time,
#    Communications of the ACM,
#    Volume 6, Number 4, April 1963, page 161.
#
#  Input:
#
#    integer N, K, are the values of N and K.
#
#  Output:
#
#    integer VALUE, the number of combinations of N
#    things taken K at a time.
#
  mn = min ( k, n - k )
  mx = max ( k, n - k )

  if ( mn < 0 ):

    value = 0

  elif ( mn == 0 ):

    value = 1

  else:

    value = mx + 1

    for i in range ( 2, mn + 1 ):
      value = ( value * ( mx + i ) ) / i

  return value

def i4_choose_test ( ):

#*****************************************************************************80
#
## i4_choose_test() tests i4_choose().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_choose_test():' )
  print ( '  i4_choose() evaluates C(N,K).' )
  print ( '' )
  print ( '       N       K     CNK' )

  for n in range ( 0, 5 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = i4_choose ( n, k )

      print ( '  %6d  %6d  %6d' % ( n, k, cnk ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def toms515_test ( ):

#*****************************************************************************80
#
## toms515_test() tests toms515().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'toms515_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test toms515().' )

  rng = default_rng ( )

  comb_test01 ( )
  comb_test02 ( rng )
  comb_test03 ( rng )
  comb_test04 ( rng )
  comb_test05 ( rng )

  i4_choose_test ( )
  i4_choose_check_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'toms515_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  toms515_test ( )
  timestamp ( )
 
