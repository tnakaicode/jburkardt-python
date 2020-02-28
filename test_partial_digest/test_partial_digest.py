#! /usr/bin/env python3
#
def i4_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## I4_UNIFORM_AB returns a scaled pseudorandom I4.
#
#  Discussion:
#
#    The pseudorandom number will be scaled to be uniformly distributed
#    between A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C, the randomly chosen integer.
#
#    Output, integer SEED, the updated seed.
#
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge; 

  if ( seed == 0 ):
    print ( '' )
    print ( 'I4_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'I4_UNIFORM_AB - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
  a = round ( a )
  b = round ( b )

  r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
    +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
  value = round ( r )

  value = max ( value, min ( a, b ) )
  value = min ( value, max ( a, b ) )
  value = int ( value )

  return value, seed

def i4_uniform_ab_test ( ):

#*****************************************************************************80
#
## I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_UNIFORM_AB computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 21 ):
    j, seed = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_distances ( k, locate ):

#*****************************************************************************80
#
## I4VEC_DISTANCES computes a pairwise distance table.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer K, the number of objects.
#
#    Input, integer LOCATE(K), the obect locations.
#
#    Output, integer D(K*(K-1)/2), the pairwise distances.
#
  import numpy as np

  d = np.zeros ( k * ( k - 1 ) // 2 )

  l = 0
  for i in range ( 0, k ):
    for j in range ( i + 1, k ):
      d[l] = abs ( locate[i] - locate[j] )
      l = l + 1

  return d

def i4vec_distances_test ( ):

#*****************************************************************************80
#
## I4VEC_DISTANCES_TEST tests I4VEC_DISTANCES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4VEC_DISTANCES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_DISTANCES computes the pairwise distances between elements' )
  print ( '  of an I4VEC.' )

  n = 5
  locate = np.array ( [ 0, 3, 10, 20, 100 ], dtype = np.int32 )
  d = i4vec_distances ( n, locate )

  i4vec_print ( n, locate, '  Locations:' )
  i4vec_print ( n * ( n - 1 ) // 2, d, '  Distances:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_DISTANCES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## I4VEC_PRINT prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_test ( ):

#*****************************************************************************80
#
## I4VEC_PRINT_TEST tests I4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_PRINT prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def ksub_random ( n, k, seed ):

#*****************************************************************************80
#
## KSUB_RANDOM selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    Consider the set A(1:N) = 1, 2, 3, ... N.
#    Choose a random index I1 between 1 and N, and swap items A(1) and A(I1).
#    Choose a random index I2 between 2 and N, and swap items A(2) and A(I2).
#    repeat K times.
#    A(1:K) is your random K-subset.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2011
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the set from which subsets
#    are drawn.
#
#    Input, integer K, number of elements in desired subsets.
#    1 <= K <= N.
#
#    Input/output, integer SEED, a seed for the random
#    number generator.
#
#    Output, integer A(K), the indices of the randomly
#    chosen elements.
#
  import numpy as np
#
#  Let B index the set.
#
  b = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    b[i] = i
#
#  Choose item 1 from N things,
#  choose item 2 from N-1 things,
#  choose item K from N-K+1 things.
#
  for i in range ( 0, k ): 

    j, seed = i4_uniform_ab ( i, n - 1, seed )

    t    = b[i]
    b[i] = b[j]
    b[j] = t
#
#  Copy the first K elements.
#
  a = np.zeros ( k, dtype = np.int32 )
  for i in range ( 0, k ):
    a[i] = b[i]

  return a, seed

def ksub_random_test ( ):

#*****************************************************************************80
#
## KSUB_RANDOM_TEST tests KSUB_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  k = 3
  n = 100

  print ( '' )
  print ( 'KSUB_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUB_RANDOM generates a random K subset of an N set.' )
  print ( '  Set size is N =    %d' % ( n ) )
  print ( '  Subset size is K = %d' % ( k ) )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):

    a, seed = ksub_random ( n, k, seed )

    for j in range ( 0, k ):
      print ( '  %3d' % ( a[j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUB_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def test_partial_digest ( k, dmax, seed ):

#*****************************************************************************80
#
## TEST_PARTIAL_DIGEST returns a partial digest test problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer K, the number of objects.
#    K must be at least 2.
#
#    Input, integer DMAX, the maximum possible distance.
#    DMAX must be at least K-1.
#
#    Input/output, integer SEED, a seed for the random number
#    generator.
#
#    Output, integer LOCATE(K), the obect locations.
#
#    Output, integer D(K*(K-1)/2), the pairwise distances.
#
  import numpy as np
  from sys import exit
#
#  Check input.
#
  if ( k < 2 ):
    print ( '\n' )
    print ( 'TEST_PARTIAL_DIGEST - Fatal error!\n' )
    print ( '  Input K < 2.\n' )
    exit ( 'TEST_PARTIAL_DIGEST - Fatal error!' )

  if ( dmax < k - 1 ):
    print ( '\n' )
    print ( 'TEST_PARTIAL_DIGEST - Fatal error!\n' )
    print ( '  DMAX < K - 1.\n' )
    exit ( 'TEST_PARTIAL_DIGEST - Fatal error!' )
#
#  Select LOCATE, which is a random subset of the integers 0 through DMAX.
#
  locate, seed = ksub_random ( dmax - 1, k - 2, seed )
  locate = np.insert ( locate, 0, 0 )
  locate = np.append ( locate, dmax )
#
#  Compute K*(K+1)/2 pairwise distances.
#
  d = i4vec_distances ( k, locate )
 
  return locate, d, seed

def test_partial_digest_test ( ):

#*****************************************************************************80
#
## TEST_PARTIAL_DIGEST_TEST tests the TEST_PARTIAL_DIGEST library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'TEST_PARTIAL_DIGEST_TEST:' )
  print ( '  TEST_PARTIAL_DIGEST creates test problems for the' )
  print ( '  partial digest problem.' )
#
#  Request a sample problem.
#
  k = 6
  dmax = 20
  seed = 123456789

  print ( '' )
  print ( '  Number of nodes = %d' % ( k ) )
  print ( '  Maximum distance = %d' % ( dmax ) )
  
  locate, d, seed = test_partial_digest ( k, dmax, seed )
#
#  Sort the data.
#
  locate = np.sort ( locate )
  d = np.sort ( d )
#
#  Print the data.
#
  i4vec_print ( k, locate, '  Locations:' )
  i4vec_print ( k * ( k - 1 ) // 2, d, '  Distances:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TEST_PARTIAL_DIGEST_TEST:' )
  print ( '  Normal end of execution.' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  i4_uniform_ab_test ( )
  i4vec_distances_test ( )
  i4vec_print_test ( )
  ksub_random_test ( )
  test_partial_digest_test ( )
  timestamp_test ( )
  timestamp ( )
