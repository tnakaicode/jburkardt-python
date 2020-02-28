#! /usr/bin/env python3
#
def grid_generate ( m, n, center, seed ):

#*****************************************************************************80
#
## GRID_GENERATE generates a grid dataset.
#
#  Discussion:
#
#    N points are needed in an M dimensional space.
#
#    The points are to lie on a uniform grid of side N_SIDE.
#
#    Unless the N = N_SIDE^M for some N_SIDE, we can't use all the
#    points on a grid.  What we do is find the smallest N_SIDE
#    that's big enough, and randomly omit some points.
#
#    If N_SIDE is 4, then the choices in 1D are:
#
#    A: 0,   1/3, 2/3, 1
#    B: 1/5, 2/5, 3/5, 4/5
#    C: 0,   1/4, 2/4, 3/4
#    D: 1/4, 2/4, 3/4, 1
#    E: 1/8, 3/8, 5/8, 7/8
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of points to generate.
#
#    Input, integer CENTER, specifies the 1D grid centering:
#    1: first point is 0.0, last point is 1.0
#    2: first point is 1/(N+1), last point is N/(N+1)
#    3: first point is 0, last point is (N-1)/N
#    4: first point is 1/N, last point is 1
#    5: first point is 1/(2*N), last point is (2*N-1)/(2*N)
#
#    Input, integer SEED, the random number seed.
#
#    Output, real R(M,N), the points.
#
#    Output, integer SEED, the updated random number seed.
#
  import numpy as np
#
#  Find the dimension of the smallest grid with N points.
#
  n_side = grid_side ( m, n )
#
#  We need to select N points out of N_SIDE^M set.
#
  n_grid = n_side ** m
#
#  Generate a random subset of N items from a set of size N_GRID.
#
  rank_list, seed = ksub_random2 ( n_grid, n, seed )
#
#  Must make one dummy call to TUPLE_NEXT_FAST with RANK = 0.
#
  base = np.zeros ( m )
  rank = -1

  tuple, base = tuple_next_fast ( n_side, m, rank, base )
#
#  Now generate the appropriate indices, and "center" them.
#
  r = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    rank = rank_list[j] - 1

    tuple, base = tuple_next_fast ( n_side, m, rank, base )

    for i in range ( 0, m ):

      if ( center == 1 ):
        r[i,j] = float (     tuple[i] - 1 ) / float (     n_side - 1 )
      elif ( center == 2 ):
        r[i,j] = float (     tuple[i]     ) / float (     n_side + 1 )
      elif ( center == 3 ):
        r[i,j] = float (     tuple[i] - 1 ) / float (     n_side     )
      elif ( center == 4 ):
        r[i,j] = float (     tuple[i]     ) / float (     n_side     )
      elif ( center == 5 ):
        r[i,j] = float ( 2 * tuple[i] - 1 ) / float ( 2 * n_side     )

  return r, seed

def grid_generate_test ( center, seed ):

#*****************************************************************************80
#
## GRID_GENERATE_TEST tests GRID_GENERATE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
  import platform

  m = 2
  n = 10

  print ( '' )
  print ( 'GRID_GENERATE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GRID_GENERATE randomly chooses a given number of' )
  print ( '  points on a uniform grid.' )
  print ( '' )
  print ( '  Spatial dimension =  %d' % ( m ) )
  print ( '  Number of points =   %d' % ( n ) )
  print ( '  Random number SEED = %d' % ( seed ) )
  print ( '  Centering option =   %d' % ( center ) )

  x, seed = grid_generate ( m, n, center, seed )

  r8mat_transpose_print ( m, n, x, '  Grid points:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'GRID_GENERATE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def grid_generate_tests ( ):

#*****************************************************************************80
#
## GRID_GENERATE_TESTS tests GRID_GENERATE_TEST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'GRID_GENERATE_TESTS:' )
  print ( '  GRID_GENERATE_TEST generates a specific grid.' )

  center = 1
  seed = 123456789

  grid_generate_test ( center, seed )

  print ( '' )
  print ( '  Repeat with a different seed from the first run.' )

  seed = 987654321
  grid_generate_test ( center, seed )

  print ( '' )
  print ( '  Repeat with the same seed as the first run.' )

  seed = 123456789
  grid_generate_test ( center, seed )

  print ( '' )
  print ( '  Repeat with different centering values.' )

  for center in range ( 1, 6 ):
    seed = 123456789
    grid_generate_test ( center, seed )
#
#  Terminate.
#
  print ( '' )
  print ( 'GRID_GENERATE_TESTS:' )
  print ( '  Normal end of execution.' )
  return

def grid_side ( m, n ):

#*****************************************************************************80
#
## GRID_SIDE finds the smallest M-D grid containing at least N points.
#
#  Discussion:
#
#    Each coordinate of the grid will have N_SIDE distinct values.
#    Thus the total number of points in the grid is N_SIDE**M.
#    This routine seeks the smallest N_SIDE such that N <= N_SIDE**M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, integer N, the number of points to generate.
#
#    Output, integer N_SIDE, the length of one side of the smallest
#    grid in M dimensions that contains at least N points.
#
  if ( n <= 0 ):

    n_side = 0

  elif ( m <= 0 ):

    n_side = -1

  else:

    exponent = 1.0 / float ( m )

    n_side = int ( ( float ( n ) ) ** exponent )

    if ( ( n_side ** m ) < n ):
      n_side = n_side + 1

  return n_side

def grid_side_test ( ):

#*****************************************************************************80
#
## GRID_SIDE_TEST tests GRID_SIDE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GRID_SIDE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GRID_SIDE returns the smallest N_SIDE, such that' )
  print ( '  N <= NSIDE^M' )

  print ( '' )
  print ( '  M      N  NSIDE  NSIDE^M' )

  for m in range ( 2, 5 ):
    print ( '' )
    for n in [ 10, 100, 1000, 10000 ]:
      n_side = grid_side ( m, n )
      print ( '  %1d  %5d  %5d  %5d' % ( m, n, n_side, n_side ** m ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GRID_SIDE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def grid_test ( ):

#*****************************************************************************80
#
## GRID_TEST tests the GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GRID_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the GRID library.' )

  grid_generate_tests ( )
  grid_side_test ( )
  tuple_next_fast_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'GRID_TEST:' )
  print ( '  Normal end of execution.' )
  return

def ksub_random2 ( n, k, seed ):

#*****************************************************************************80
#
## KSUB_RANDOM2 selects a random subset of size K from a set of size N.
#
#  Discussion:
#
#    This algorithm is designated Algorithm RKS2 in the reference.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the size of the set from which subsets are drawn.
#
#    Input, integer K, number of elements in desired subsets.  K must
#    be between 0 and N.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer A(K).  A(I) is the I-th element of the
#    output set.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  if ( k < 0 ):
    print ( '' )
    print ( 'KSUB_RANDOM - Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 < K is required!' )
    exit ( 'KSUB_RANDOM - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'KSUB_RANDOM - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  K <= N is required!' )
    exit ( 'KSUB_RANDOM - Fatal error!' )

  a = np.zeros ( k )

  if ( k == 0 ):
    return a

  need = k
  have = 0

  available = n
  candidate = 0

  while ( True ):

    candidate = candidate + 1

    r, seed = r8_uniform_01 ( seed )

    if ( available * r <= need ):

      need = need - 1;
      a[have] = candidate
      have = have + 1

      if ( need <= 0 ):
        break

    available = available - 1

  return a, seed

def ksub_random2_test ( ):

#*****************************************************************************80
#
## KSUB_RANDOM2_TEST tests KSUB_RANDOM2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  k = 3
  n = 5

  print ( '' )
  print ( 'KSUB_RANDOM2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUB_RANDOM2 generates a random K subset of an N set.' )
  print ( '  Set size is N =    %d' % ( n ) )
  print ( '  Subset size is K = %d' % ( k ) )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):

    a, seed = ksub_random2 ( n, k, seed )

    for j in range ( 0, k ):
      print ( '  %3d' % ( a[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUB_RANDOM2_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT prints an R8MAT, transposed.
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
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_TEST tests R8MAT_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_TRANSPOSE_PRINT prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME_TEST tests R8MAT_TRANSPOSE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_TRANSPOSE_PRINT_SOME prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## R8MAT_WRITE writes an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8mat_write_test ( ):

#*****************************************************************************80
#
## R8MAT_WRITE_TEST tests R8MAT_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R8MAT_WRITE_TEST:' )
  print ( '  Test R8MAT_WRITE, which writes an R8MAT to a file.' )

  filename = 'r8mat_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 1.1, 1.2, 1.3 ), \
    ( 2.1, 2.2, 2.3 ), \
    ( 3.1, 3.2, 3.3 ), \
    ( 4.1, 4.2, 4.3 ), \
    ( 5.1, 5.2, 5.3 ) ) )
  r8mat_write ( filename, m, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## R8_UNIFORM_01 returns a unit pseudorandom R8.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r8_uniform_01 = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      R8_UNIFORM_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2013
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
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#    Output, real R, a random value between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_01 - Fatal error!' )

  k = floor ( seed / 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )
  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789
  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
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

def tuple_next_fast ( m, n, rank, base ):

#*****************************************************************************80
#
## TUPLE_NEXT_FAST computes the next element of a tuple space, "fast".
#
#  Discussion:
#
#    The elements are N vectors.  Each entry is constrained to lie
#    between 1 and M.  The elements are produced one at a time.
#    The first element is
#      (1,1,...,1)
#    and the last element is
#      (M,M,...,M)
#    Intermediate elements are produced in lexicographic order.
#
#    This code was written as a possibly faster version of TUPLE_NEXT.
#
#  Example:
#
#    N = 2,
#    M = 3
#
#    INPUT        OUTPUT
#    -------      -------
#    Rank          X
#    ----          ----
#   -1            -1 -1
#
#    0             1  1
#    1             1  2
#    2             1  3
#    3             2  1
#    4             2  2
#    5             2  3
#    6             3  1
#    7             3  2
#    8             3  3
#    9             1  1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the maximum entry in each component.
#    M must be greater than 0.
#
#    Input, integer N, the number of components.
#    N must be greater than 0.
#
#    Input, integer RANK, indicates the rank of the tuples.
#    Typically, 0 <= RANK < N^M values greater than this are
#    legal and meaningful, being equivalent to the corresponding
#    value mod N^M.  RANK < 0 indicates that this is the first
#    call for the given values of (M,N).  Initialization is done,
#    and X is set to a dummy value.
#
#    Input/output, integer BASE(N), a bookkeeping array needed by 
#    this procedure.  The user should allocate space for this array, but
#    should not alter it between successive calls.
#
#    Output, integer X(N), the next tuple of the given rank,
#    or a dummy value if initialization is being done.
#
  import numpy as np
  from sys import exit

  x = np.zeros ( n, dtype = np.int32 )

  if ( rank < 0 ):

    if ( m <= 0 ):
      print ( '' )
      print ( 'TUPLE_NEXT_FAST - Fatal error!' )
      print ( '  M <= 0 is illegal.' )
      print ( '  M = %d' % ( m ) )
      exit ( 'TUPLE_NEXT_FAST - Fatal error!' )

    if ( n <= 0 ):
      print ( '' )
      print ( 'TUPLE_NEXT_FAST - Fatal error!' )
      print ( '  N <= 0 is illegal.' )
      print ( '  N = %d' % ( n ) )
      exit ( 'TUPLE_NEXT_FAST - Fatal error!' )

    base[n-1] = 1
    for i in range ( n - 2, -1, -1 ):
      base[i] = base[i+1] * m

    for i in range ( 0, n ):
      x[i] = -1

  else:

    for i in range ( 0, n ):
      x[i] = ( ( rank // base[i] ) % m ) + 1

  return x, base

def tuple_next_fast_test ( ):

#*****************************************************************************80
#
## TUPLE_NEXT_FAST_TEST tests TUPLE_NEXT_FAST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 2
  m = 3

  print ( '' )
  print ( 'TUPLE_NEXT_FAST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TUPLE_NEXT_FAST returns the next "tuple", that is,' )
  print ( '  a vector of N integers, each between 1 and M.' )
  print ( '' )
  print ( '  M = %d' % ( m ) )
  print ( '  N = %d' % ( n ) )
  print ( '' )
#
#  Initialize.
#
  rank = -1
  base = np.zeros ( n )
  x, base = tuple_next_fast ( m, n, rank, base )

  rank_max = ( m ** n ) - 1

  for rank in range ( 0, rank_max + 1 ):

    x, base = tuple_next_fast ( m, n, rank, base )

    print ( '%4d  ' % ( rank ), end = '' )
    for j in range ( 0, n ):
      print ( '%10d  ' % ( x[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TUPLE_NEXT_FAST_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  grid_test ( )
  timestamp ( )

