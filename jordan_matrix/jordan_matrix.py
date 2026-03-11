#! /usr/bin/env python3
#
def jordan_matrix_test ( ):

#*****************************************************************************80
#
## jordan_matrix_test() tests jordan_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'jordan_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  jordan_matrix() returns a random Jordan matrix.' )

  for i in range ( 0, 10 ):
    n = rng.integers ( low = 3, high = 8, endpoint = True )
    print ( '' )
    print ( '  Random Jordan matrix', i, 'will have order n =', n )
    A = jordan_matrix_random ( n, rng )
    print ( '' )
    print ( A )
#
#  Terminate.
#
  print ( '' )
  print ( 'jordan_matrix_test():' )
  print ( '  Normal end of execution.' )

  return

def compnz_random ( n, k, rng ):

#*****************************************************************************80
#
## compnz_random() selects a random composition of the integer N into K nonzero parts.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis and Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the integer to be decomposed.
#
#    integer K, the number of parts in the composition.
#    K must be no greater than N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(K), the parts of the composition.
#
  import numpy as np

  a = np.zeros ( k, dtype = np.int32 )

  if ( 1 < n and 1 < k ):
    b = ksub_random2 ( n - 1, k - 1, rng )

  for i in range ( 0, k - 1 ):
    a[i] = b[i]

  a[k-1] = n
  l = 0

  for i in range ( 0, k ):
    m = a[i]
    a[i] = a[i] - l - 1
    l = m

  for i in range ( 0, k ):
    a[i] = a[i] + 1

  return a

def jordan_matrix_random ( n, rng ):

#*****************************************************************************80
#
## jordan_matrix_random() returns a Jordan matrix with random eigenvalues.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real A, the random Jordan matrix.
#
  import numpy as np
#
#  Choose K, number of distinct eigenvalues, biased towards N.
#
  k = rng.integers ( low = 0, high = n**2, endpoint = False )
  k = int ( np.sqrt ( k ) ) + 1
#
#  Choose K nonzero multiplicities S that sum to N.
#
  s = compnz_random ( n, k, rng )
#
#  Choose EV, K distinct real eigenvalues between -2*N and +2*N.
#
  ev = ksub_random2 ( n + 1, k, rng )
  ev = np.sort ( ev )
  ev = 4.0 * ( ev - 1.0 ) - 2.0 * n
#
#  Construct Jordan matrix.
#  With 80 per cent probability, include a superdiagonal 1.
#
  A = np.zeros ( [ n, n ] )
  i = 0
  for block in range ( 0, k ):
    for ii in range ( 0, s[block] ):
      A[i,i] = ev[block]
      if ( ii < s[block] - 1 ):
        if ( rng.random ( ) <= 0.80 ):
          A[i,i+1] = 1.0
      i = i + 1

  return A

def ksub_random2 ( n, k, rng ):

#*****************************************************************************80
#
## ksub_random2() selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    This algorithm is designated Algorithm RKS2 in the reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#    A Bebbington,
#    A simple method of drawing a sample without replacement,
#    Journal of Applied Statistics,
#    Volume 24, 1975, page 136.
#
#  Input:
#
#    integer N, the size of the set from which subsets are drawn.
#
#    integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer A(K).  A(I) is the I-th element of the
#    output set.
#
  import numpy as np

  if ( k < 0 ):
    print ( '' )
    print ( 'ksub_random2(): Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 < K is required!' )
    raise Exception ( 'ksub_random2(): Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'ksub_random2(): Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  K <= N is required!' )
    raise Exception ( 'ksub_random2(): Fatal error!' )

  a = np.zeros ( k, dtype = np.int32 )

  if ( k == 0 ):
    return a

  need = k
  have = 0

  available = n
  candidate = 0

  while ( True ):

    candidate = candidate + 1

    r = rng.random ( )

    if ( available * r <= need ):

      need = need - 1;
      a[have] = candidate
      have = have + 1

      if ( need <= 0 ):
        break

    available = available - 1

  return a

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
  jordan_matrix_test ( )
  timestamp ( )

