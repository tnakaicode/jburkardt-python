#! /usr/bin/env python3
#
def hankel_pds_cholesky_lower ( n, lii, liim1 ):

#*****************************************************************************80
#
## HANKEL_PDS_CHOLESKY_LOWER returns L such that L*L' is Hankel PDS.
#
#  Discussion:
#
#    In other words, H = L * L' is a positive definite symmetric matrix
#    with the property that H is constant along antidiagonals, so that
#
#      H(I+J) = h(k-1), for 1 <= I, J <= N, 1 <= K <= 2*N-1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2017
#
#  Author:
#
#    S Al-Homidan, M Alshahrani.
#    Python implementation by John Burkardt.
#
#  Reference:
#
#    S Al-Homidan, M Alshahrani,
#    Positive Definite Hankel Matrices Using Cholesky Factorization,
#    Computational Methods in Applied Mathematics,
#    Volume 9, Number 3, pages 221-225, 2009.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real LII(N), values to be used in L(I,I), for 1 <= I <= N.
#
#    Input, real LIIM1(N-1), values to be used in L(I+1,I) for 1 <= I <= N-1.
#
#    Output, real L(N,N), the lower Cholesky factor.
#
  import numpy as np

  l = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    l[i,i] = lii[i]

  for i in range ( 0, n - 1 ):
    l[i+1,i] = liim1[i]

  for i in range ( 2, n ):
    for j in range ( 0, i - 1 ):

      if ( ( ( i + j ) % 2 ) == 0 ):
        q = int ( ( i + j ) / 2 )
        r = q
      else:
        q = int ( ( i + j - 1 ) / 2 )
        r = q + 1

      alpha = 0.0
      for s in range ( 0, q + 1 ):
        alpha = alpha + l[q,s] * l[r,s]

      beta = 0.0
      for t in range ( 0, j ):
        beta = beta + l[i,t] * l[j,t]

      l[i,j] = ( alpha - beta ) / l[j,j]

  return l

def hankel_pds_cholesky_lower_test01 ( ):

#*****************************************************************************80
#
## HANKEL_PDS_CHOLESKY_LOWER_TEST01 tests HANKEL_PDS_CHOLESKY_LOWER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'HANKEL_PDS_CHOLESKY_LOWER_TEST01' )
  print ( '  HANKEL_PDS_CHOLESKY_LOWER computes a lower Cholesky' )
  print ( '  matrix L such that the matrix H = L * L\' is a' )
  print ( '  positive definite (symmetric) Hankel matrix.' )

  n = 5
  lii = np.ones ( n )
  liim1 = np.ones ( n - 1 )

  l = hankel_pds_cholesky_lower ( n, lii, liim1 )

  r8mat_print ( n, n, l, '  The Cholesky factor L:' )

  h = np.dot ( l, l.transpose ( ) )

  r8mat_print ( n, n, h, '  The Hankel matrix H = L * L\':' )

  n = 5
  lii = np.zeros ( n )
  for i in range ( 0, n ):
    lii[i] = float ( i + 1 )

  liim1 = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    liim1[i] = n - float ( i + 1 )

  l = hankel_pds_cholesky_lower ( n, lii, liim1 )

  r8mat_print ( n, n, l, '  The Cholesky factor L:' )

  h = np.dot ( l, l.transpose ( ) )

  r8mat_print ( n, n, h, '  The Hankel matrix H = L * L\':' )

  n = 5
  seed = 123456789
  lii, seed = r8vec_uniform_01 ( n, seed )
  liim1, seed = r8vec_uniform_01 ( n - 1, seed )

  l = hankel_pds_cholesky_lower ( n, lii, liim1 )

  r8mat_print ( n, n, l, '  The Cholesky factor L:' )

  h = np.dot ( l, l.transpose ( ) )

  r8mat_print ( n, n, h, '  The Hankel matrix H = L * L\':' )

  return

def hankel_pds_cholesky_lower_test02 ( ):

#*****************************************************************************80
#
## HANKEL_PDS_CHOLESKY_LOWER_TEST02 tests HANKEL_PDS_CHOLESKY_LOWER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'HANKEL_PDS_CHOLESKY_LOWER_TEST02' )
  print ( '  HANKEL_PDS_CHOLESKY_LOWER computes a lower Cholesky' )
  print ( '  matrix L such that the matrix H = L * L\' is a' )
  print ( '  positive definite (symmetric) Hankel matrix.' )

  n = 5
  lii = np.ones ( n )
  liim1 = np.ones ( n - 1 )

  l = hankel_pds_cholesky_lower ( n, lii, liim1 )

  r8mat_print ( n, n, l, '  The Cholesky factor L:' )

  h = np.dot ( l, l.transpose ( ) )

  r8mat_print ( n, n, h, '  The Hankel matrix H = L * L\':' )

  l2, flag = r8mat_cholesky_factor ( n, h )

  r8mat_print ( n, n, l2, '  The Cholesky factor L2 of H:' )

  h2 = np.dot ( l2, l2.transpose ( ) )

  r8mat_print ( n, n, h2, '  The Hankel matrix H2 = L2 * L2\':' )

  return

def r8mat_cholesky_factor ( n, a ):

#*****************************************************************************80
#
## R8MAT_CHOLESKY_FACTOR computes the Cholesky factor of a symmetric matrix.
#
#  Discussion:
#
#    The matrix must be symmetric and positive semidefinite.
#
#    For a positive semidefinite symmetric matrix A, the Cholesky factorization
#    is a lower triangular matrix L such that:
#
#      A = L * L'
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns of the matrix A.
#
#    Input, real A(N,N), the matrix.
#
#    Output, real C(N,N), the N by N lower triangular Cholesky factor.
#
#    Output, boolean FLAG:
#    False, no error occurred.
#    True, the matrix is not positive definite.
#
  import numpy as np

  flag = False

  c = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      c[i,j] = a[i,j]

  for j in range ( 0, n ):

    c[0:j,j] = 0.0

    for i in range ( j, n ):

      sum2 = c[j,i]
      for k in range ( 0, j ):
        sum2 = sum2 - c[j,k] * c[i,k]

      if ( i == j ):
        if ( sum2 <= 0.0 ):
          flag = True
          return c, flag
        else:
          c[i,j] = np.sqrt ( sum2 )
      else:
        if ( c[j,j] != 0.0 ):
          c[i,j] = sum2 / c[j,j]
        else:
          c[i,j] = 0.0

  return c, flag

def r8mat_cholesky_factor_test ( ):

#*****************************************************************************80
#
## R8MAT_CHOLESKY_FACTOR_TEST tests R8MAT_CHOLESKY_FACTOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'R8MAT_CHOLESKY_FACTOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_CHOLESKY_FACTOR determines the' )
  print ( '  lower triangular Cholesky factorization' )
  print ( '  of a positive definite symmetric matrix,' )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( j == i - 1 or j == i + 1 ):
        a[i,j] = -1.0

  r8mat_print ( n, n, a, '  Matrix to be factored:' )
#
#  Compute a Cholesky factor.
#
  l, flag = r8mat_cholesky_factor ( n, a )
  r8mat_print ( n, n, l, '  Cholesky factor L:' )
  d = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, d, '  Product L * L\':' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_CHOLESKY_FACTOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
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
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
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

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
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
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
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
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
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
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = np.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST:' )
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

def hankel_pds_test ( ):

#*****************************************************************************80
#
## HANKEL_PDS_TEST tests HANKEL_PDS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' );
  print ( 'HANKEL_PDS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the HANKEL_PDS library.' );

  hankel_pds_cholesky_lower_test01 ( )
  hankel_pds_cholesky_lower_test02 ( )
  r8mat_cholesky_factor_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8vec_print_test ( )
  r8vec_uniform_01_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'HANKEL_PDS_TEST' )
  print ( '  Normal end of execution.' )
  print ( '' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  hankel_pds_test ( )
  timestamp ( )

