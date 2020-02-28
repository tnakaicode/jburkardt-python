#! /usr/bin/env python3
#
def haar_1d ( n, x ):

#*****************************************************************************80
#
## HAAR_1D computes the Haar transform of a vector.
#
#  Discussion:
#
#    For the classical Haar transform, N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int N, the dimension of the vector.
#
#    Input, double X[N], the vector to be transformed.
#
#    Output, double U[N], the transformed vector.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = np.zeros ( n, dtype = np.float64 )
#
#  Determine K, the largest power of 2 such that K <= N.
#
  k = 1
  while ( k * 2 <= n ):
    k = k * 2
  
  while ( 1 < k ):

    k = k // 2

    v[0:k]   = ( u[0:2*k-1:2] + u[1:2*k:2] ) / s
    v[k:2*k] = ( u[0:2*k-1:2] - u[1:2*k:2] ) / s

    u[0:2*k] = v[0:2*k].copy ( )

  return u

def haar_1d_inverse ( n, x ):

#*****************************************************************************80
#
## HAAR_1D_INVERSE computes the inverse Haar transform of a vector.
#
#  Discussion:
#
#    For the classical Haar transform, N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int N, the dimension of the vector.  
#
#    Input, double X[N], the vector to be transformed.
#
#    Output, double U[N], the transformed vector.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = np.zeros ( n )

  k = 1
  while ( k * 2 <= n ):

    v[0:2*k-1:2] = ( u[0:k] + u[0+k:k+k] ) / s
    v[1:2*k:2]   = ( u[0:k] - u[0+k:k+k] ) / s

    u[0:2*k] = v[0:2*k].copy ( )
    k = k * 2

  return u

def haar_1d_test ( ):

#*****************************************************************************80
#
## HAAR_1D_TEST tests HAAR_1D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'HAAR_1D_TEST' )
  print ( '  HAAR_1D computes the Haar transform of a vector.' )
#
#  Random data.
#
  n = 16
  seed = 123456789
  u, seed = r8vec_uniform_01 ( n, seed )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  Constant signal.
#
  n = 8
  u = np.ones ( n )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  Linear signal.
#
  n = 16
  u = np.linspace ( 1, n, n )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  Quadratic data.
#
  n = 8
  u = np.array ( [ \
    25.0, 16.0,  9.0,  4.0,  1.0, \
     0.0,  1.0,  4.0 ] )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )
#
#  N not a power of 2.
#
  n = 99
  seed = 123456789
  u, seed = r8vec_uniform_01 ( n, seed )

  v = haar_1d ( n, u )

  w = haar_1d_inverse ( n, v )

  print ( '' )
  print ( '   i      U(i)        H(U)(i)  Hinv(H(U))(i)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %10f  %10f  %10f' % ( i, u[i], v[i], w[i] ) )

  return

def haar_2d ( m, n, x ):

#*****************************************************************************80
#
## HAAR_2D computes the Haar transform of an array.
#
#  Discussion:
#
#    For the classical Haar transform, M and N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int M, N, the dimensions of the array.
#
#    Input, double X[M*N], the array to be transformed.
#
#    Output, double U[M*N], the transformed array.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = u.copy ( )
#
#  Determine K, the largest power of 2 such that K <= M.
#
  k = 1
  while ( k * 2 <= m ):
    k = k * 2
#
#  Transform all columns.
#
  while ( 1 < k ):

    k = k // 2

    v[  0:  k,0:n] = ( u[0:2*k-1:2,0:n] + u[1:2*k:2,0:n] ) / s
    v[k+0:k+k,0:n] = ( u[0:2*k-1:2,0:n] - u[1:2*k:2,0:n] ) / s

    u[0:2*k,0:n] = v[0:2*k,0:n].copy ( )
#
#  Determine K, the largest power of 2 such that K <= N.
#
  k = 1
  while ( k * 2 <= n ):
    k = k * 2
#
#  Transform all rows.
#
  while ( 1 < k ):

    k = k // 2

    v[0:m,  0:  k] = ( u[0:m,0:2*k-1:2] + u[0:m,1:2*k:2] ) / s
    v[0:m,k+0:k+k] = ( u[0:m,0:2*k-1:2] - u[0:m,1:2*k:2] ) / s

    u[0:m,0:2*k] = v[0:m,0:2*k].copy ( )

  return u

def haar_2d_inverse ( m, n, x ):

#*****************************************************************************80
#
## HAAR_2D_INVERSE inverts the Haar transform of an array.
#
#  Discussion:
#
#    For the classical Haar transform, M and N should be a power of 2.
#    However, this is not required here.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int M, N, the dimensions of the array.
#
#    Input, double X[M*N], the array to be transformed.
#
#    Output, double U[M*N], the transformed array.
#
  import numpy as np

  u = x.copy ( )

  s = np.sqrt ( 2.0 )

  v = u.copy ( )
#
#  Inverse transform of all rows.
#
  k = 1

  while ( k * 2 <= n ):

    v[0:m,0:2*k-1:2] = ( u[0:m,0:k] + u[0:m,0+k:k+k] ) / s
    v[0:m,1:2*k:2]   = ( u[0:m,0:k] - u[0:m,0+k:k+k] ) / s

    u[0:m,0:2*k] = v[0:m,0:2*k].copy ( )

    k = k * 2
#
#  Inverse transform of all columns.
#
  k = 1

  while ( k * 2 <= m ):

    v[0:2*k-1:2,0:n] = ( u[0:k,0:n] + u[0+k:k+k,0:n] ) / s
    v[1:2*k:2,0:n]   = ( u[0:k,0:n] - u[0+k:k+k,0:n] ) / s

    u[0:2*k,0:n] = v[0:2*k,0:n].copy ( )

    k = k * 2

  return u

def haar_2d_test ( ):

#*****************************************************************************80
#
## HAAR_2D_TEST tests HAAR_2D..
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'HAAR_2D_TEST' )
  print ( '  HAAR_2D computes the Haar transform of an array.' )
  print ( '  HAAR_2D_INVERSE inverts the transform.' )
#
#  Demonstrate successful inversion.
#
  m = 16
  n = 4
  seed = 123456789
  u, seed = r8mat_uniform_01 ( m, n, seed )

  r8mat_print ( m, n, u, '  Input array U:' )

  v = haar_2d ( m, n, u )

  r8mat_print ( m, n, v, '  Transformed array V:' )

  w = haar_2d_inverse ( m, n, v )

  r8mat_print ( m, n, w, '  Recovered array W:' )
#
#  M, N not powers of 2.
#
  m = 37
  n = 53
  seed = 123456789
  u, seed = r8mat_uniform_01 ( m, n, seed )

  v = haar_2d ( m, n, u )

  w = haar_2d_inverse ( m, n, v )

  err = r8mat_diff_frobenius ( m, n, u, w )

  print ( '' )
  print ( '  M = %d, N = %d, ||haar_2d_inverse(haar_2d(u))-u|| = %g' \
    % ( m, n, err ) )

  return

def r8mat_diff_frobenius ( m, n, a, b ):

#*****************************************************************************80
#
## R8MAT_DIFF_FROBENIUS: Frobenius norm of the difference of two R8MAT's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
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
#    Input, real A(M,N), B(M,N), the matrices for which we
#    are to compute the Frobenius norm of the difference.
#
#    Output, real DIF, the Frobenius norm of A-B.
#
  import numpy as np

  diff = np.sqrt ( np.sum ( np.sum ( ( a[0:m,0:n] - b[0:m,0:n] ) ** 2 ) ) )

  return diff

def r8mat_diff_frobenius_test ( ):

#*****************************************************************************80
#
## R8MAT_DIFF_FROBENIUS_TEST tests R8MAT_DIFF_FROBENIUS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_DIFF_FROBENIUS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_DIFF_FROBENIUS computes the Frobenius norm of' )
  print ( '  the difference of two R8MATs.' )

  m = 2
  n = 3

  a = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], \
    [ 21.0, 22.0, 23.0 ] ] )

  b = np.array ( [ \
    [ 10.0, 13.0, 12.0 ], \
    [ 23.0, 21.0, 24.0 ] ] )

  c = a - b

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )
  r8mat_print ( m, n, c, '  C = A-B:' )

  diff = r8mat_diff_frobenius ( m, n, a, b )

  print ( '' )
  print ( '  Frobenius norm ||A-B|| = %g' % ( diff ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_DIFF_FROBENIUS_TEST' )
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

def r8mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_01 returns a unit pseudorandom R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
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
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.
#
#    Output, real R(M,N), an array of random values between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8MAT_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8MAT_UNIFORM_01 - Fatal error!' )

  r = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = seed * 4.656612875E-10

  return r, seed

def r8mat_uniform_01_test ( ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_01_TEST tests R8MAT_UNIFORM_01.
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
  from r8mat_print import r8mat_print

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'R8MAT_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_UNIFORM_01 computes a random R8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8mat_uniform_01 ( m, n, seed )

  r8mat_print ( m, n, v, '  Random R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_diff_norm ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_DIFF_NORM returns the L2 norm of the difference of R8VEC's.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), B(N), the vectors.
#
#    Output, real VALUE, the L2 norm of A - B.
#
  import numpy as np

  value = np.sqrt ( np.sum ( ( a[0:n] - b[0:n] ) ** 2 ) )

  return value

def r8vec_diff_norm_test ( ):

#*****************************************************************************80
#
## R8VEC_DIFF_NORM_TEST tests R8VEC_DIFF_NORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_DIFF_NORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_DIFF_NORM: L2 norm of the difference of two R8VECs.' )

  n = 6
  v = np.array ( [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0 ], dtype = np.float64 )
  w = np.array ( [ 1.0, 2.0, 3.0, 5.0, 5.0, 6.0 ], dtype = np.float64 )
  
  print ( '' )
  print ( '  I    V[I]  W[I]' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '%2d  %f  %f' % ( i, v[i], w[i] ) )

  d = r8vec_diff_norm ( n, v, w )

  print ( '' )
  print ( '  L2 norm of vector difference ||V-W|| is %g' % ( d ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_DIFF_NORM_TEST:' )
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
  from r8vec_print import r8vec_print

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

def haar_test ( ):

#*****************************************************************************80
#
## HAAR_TEST tests the HAAR library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'HAAR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the HAAR library.' )

  haar_1d_test ( )
  haar_2d_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'HAAR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  haar_test ( )
  timestamp ( )

