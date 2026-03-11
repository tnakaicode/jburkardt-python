#! /usr/bin/env python3
#
def permutation_distance_test ( ):

#*****************************************************************************80
#
## permutation_distance_test() tests permutation_distance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'permutation_distance_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test permutation_distance()' )

  rng = default_rng ( )

  permutation_distance_histogram ( 50, 10000, rng )
  permutation_distance_stats_test ( rng )
  permutation_distance_ulam_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'permutation_distance_test():' )
  print ( '  Normal end of execution.' )

  return

def permutation_ascending_subsequence ( p ):

#*****************************************************************************80
#
## permutation_ascending_subsequence() computes the longest ascending subsequence of permutation.
#
#  Discussion:
#
#    Although this routine is intended to be applied to a permutation,
#    it will work just as well for an arbitrary vector.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 June 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(N), the permutation to be examined.
#
#  Output:
#
#    integer SUB(LENGTH), a longest increasing subsequence of A.
#
  import numpy as np

  n = len ( p )
  top = np.zeros ( n + 1, dtype = np.int32 )
  top_prev = np.zeros ( n + 1, dtype = np.int32 )

  length = 0

  if ( n <= 0 ):
    sub = np.zeros ( length )
    return sub

  for i in range ( 0, n ):

    k = 0

    for j in range ( 1, length + 1 ):
      if ( p[i] <= p[top[j]] ):
        k = j
        break

    if ( k == 0 ):
      length = length + 1
      k = length

    top[k] = i
    top_prev[i] = top[k-1]
#
#  Construct the subsequence.
#
  sub = np.zeros ( length, dtype = np.int32 )

  j = top[length]
  sub[length-1] = p[j]

  for i in range ( length - 2, -1, -1 ):
    j = top_prev[j]
    sub[i] = p[j]

  return sub

def permutation_distance_histogram ( m, n, rng ):

#*****************************************************************************80
#
## permutation_distance_histogram() histograms permutation distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the order of the permutations.
#
#    integer N, the number of samples to use.
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  t = np.zeros ( n )

  for i in range ( 0, n ):
    p1 = rng.permutation ( m )
    p2 = rng.permutation ( m )
    t[i] = permutation_distance_ulam ( p1, p2 )

  bins = m + 1
  plt.clf ( )
  plt.hist ( t, bins = m + 1, rwidth = 0.95, density = True )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.ylabel ( '<-- Frequency -->' )
  title_string = ( 'Ulam distance between random permutations of order %d' % ( m ) )
  plt.title ( title_string )
  filename = 'permutation_distance_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return
 
def permutation_distance_stats ( m, n, rng ):

#*****************************************************************************80
#
## permutation_distance_stats() estimates permutation distance statistics.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the permutation order.
#
#    integer N, the number of samples to consider.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real MU, VAR, the estimated mean and variance of the
#    distance between two random permutations of order N.
#
  import numpy as np

  t = np.zeros ( n )

  for i in range ( 0, n ):
    p1 = rng.permutation ( m )
    p2 = rng.permutation ( m )
    t[i] = permutation_distance_ulam ( p1, p2 )

  mu = np.mean ( t )
  var = np.var ( t )

  return mu, var
 
def permutation_distance_stats_test ( rng ):

#*****************************************************************************80
#
## permutation_distance_stats_test() tests permutation_distance_stats().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'permutation_distance_stats_test():' )
  print ( '  Test permutation_distance_stats().' )

  n = 10000
  print ( '  Using N = ', n, ' sample permutations.' )
  print ( '  Permutation order is M' )
  print ( '  Compute mean and variance of Ulam permutation distance.' )
  print ( '' )

  print ( '   M   Mean   Predicted Variance' )
  print ( '' )
  bob = np.linspace ( 1, 40, 40 )
  mu = np.zeros ( 40 )
  for m in range ( 0, 40 ):
    mu[m], variance = permutation_distance_stats ( m + 1, n, rng )
    print ( '  %2d  %g  %g  %g' \
      % ( m + 1, mu[m], mu[m] - ( m + 1 ) + 2.0 * np.sqrt ( mu[m] ), variance ) )

  plt.clf ( )
  plt.plot ( bob, mu, 'bo', linewidth = 3 )
  plt.plot ( bob, bob-2*np.sqrt(bob), 'r-', linewidth = 3 )
  plt.grid ( True )
  filename = 'permutation_distance_stats.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def permutation_distance_ulam ( a, b ):

#*****************************************************************************80
#
## permutation_distance_ulam() computes the Ulam distance of two permutations.
#
#  Discussion:
#
#    The permutations have a common length N, and are reorderings of the
#    integer 1 through N.
#
#    If we let L(P) be the length of the longest ascending subsequence 
#    of a permutation P, then the Ulam distance between A and B is
#
#      N - L ( A * inverse ( B ) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(N), B(N), the permutations to be examined.
#
#  Output:
#
#    integer K, the Ulam metric distance between A and B.
#
  binv = permutation_inverse ( b )

  c = permutation_multiply ( a, binv )

  subseq = permutation_ascending_subsequence ( c )

  n = permutation_order ( a )
  sub_n = permutation_order ( subseq )

  k = n - sub_n

  return k

def permutation_distance_ulam_test ( rng ):

#*****************************************************************************80
#
## permutation_distance_ulam_test() tests permutation_distance_ulam().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10

  print ( '' )
  print ( 'permutation_distance_ulam():' )
  print ( '  permutation_distance_ulam() computes the Ulam metric distance' )
  print ( '  between two permutations of (1,...,N).' )

  p1 = rng.permutation ( n )
  permutation_print ( p1, '  Permutation P1' )
  p2 = rng.permutation ( n )
  permutation_print ( p2, '  Permutation P2' )
  p3 = rng.permutation ( n )
  permutation_print ( p3, '  Permutation P3' )

  k11 = permutation_distance_ulam ( p1, p1 )
  k12 = permutation_distance_ulam ( p1, p2 )
  k21 = permutation_distance_ulam ( p2, p1 )
  k13 = permutation_distance_ulam ( p1, p3 )
  k23 = permutation_distance_ulam ( p2, p3 )

  print ( '' )
  print ( '  K(P1,P1) should be 0.' )
  print ( '' )
  print ( '  K(P1,P1) = ', k11 )
  print ( '' )
  print ( '  K(P1,P2) should equal K(P2,P1).' )
  print ( '' )
  print ( '  K(P1,P2) = ', k12 )
  print ( '  K(P2,P1) = ', k21 )
  print ( '' )
  print ( '  K(P1,P3) <= K(P1,P2) + K(P2,P3).' )
  print ( '' )
  print ( '  K(P1,P3) = ', k13 )
  print ( '  K(P1,P2) = ', k12 )
  print ( '  K(P2,P3) = ', k23 )
  print ( '  K(P1,P2) + K(P2,P3) = ', k12 + k23 )

  return

def permutation_inverse ( p1 ):

#*****************************************************************************80
#
## permutation_inverse() inverts a permutation of (0,...,N-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 September 202
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects being permuted.
#
#    integer P1(N), the permutation.
#
#  Output:
#
#    integer P2(N), the inverse permutation
#
  import numpy as np

  n = permutation_order ( p1 )

  p2 = np.zeros ( n, dtype = np.int32 )
  p2 = p1 + 1
 
  s = 1

  for i in range ( 1, n + 1 ):

    i1 = p2[i-1]

    while ( i < i1 ):
      i2 = p2[i1-1]
      p2[i1-1] = - i2
      i1 = i2

    s = - np.sign ( p2[i-1] )
    p2[i-1] = np.sign ( s ) * np.abs ( p2[i-1] )

  for i in range ( 1, n + 1 ):

    i1 = - p2[i-1]

    if ( 0 <= i1 ):

      i0 = i

      while ( True ):

        i2 = p2[i1-1]
        p2[i1-1] = i0

        if ( i2 < 0 ):
          break

        i0 = i1
        i1 = i2

  for i in range ( 0, n ):
    p2[i] = p2[i] - 1

  return p2

def permutation_multiply ( p1, p2 ):

#*****************************************************************************80
#
## permutation_multiply() "multiplies" two permutations of (0,...,N-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P1(N), P2(N), the permutations.
#
#  Output:
#
#    integer P3(N), the product permutation.
#
  import numpy as np

  n = permutation_order ( p1 )

  p3 = np.zeros ( n )

  for i in range ( 0, n ):
    p3[i] = p2[p1[i]]

  return p3

def permutation_order ( a ):

#*****************************************************************************80
#
## permutation_order() returns the order of a permutation.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A(N), the permutation.
#
#  Output:
#
#    integer N, the order of the permutation.
#
  n = len ( a )

  return n

def permutation_print ( p, title ):

#*****************************************************************************80
#
## permutation_print() prints a permutation of (0,...,N-1).
#
#  Example:
#
#    Input:
#
#      P = 6 1 3 0 4 2 5
#
#    Printed output:
#
#      "This is the permutation:"
#
#      0 1 2 3 4 5 6
#      6 1 3 0 4 2 5
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P(N), the permutation, in standard index form.
#
#    string TITLE, the title.
#
  n = permutation_order ( p )

  inc = 20

  print ( '' )
  print ( title )

  for ilo in range ( 0, n, inc ):
    ihi = min ( n, ilo + inc )

    print ( '' )
    print ( '  ' ),
      
    for i in range ( ilo, ihi ):
      print ( '%4d' % ( i ) ),
    print ( '' )

    print ( '  ' ),
    for i in range ( ilo, ihi ):
      print ( '%4d' % ( p[i] ) ),
    print ( '' )

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
  permutation_distance_test ( )
  timestamp ( )


