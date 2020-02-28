#! /usr/bin/env python
#
def r8ut_indicator ( m, n ):

#*****************************************************************************80
#
## R8UT_INDICATOR sets up a R8UT indicator matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#    M and N must be positive.
#
#    Output, real A(M,N), the R8UT matrix.
#
  import numpy as np
  from i4_log_10 import i4_log_10

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = r8ut_zeros ( m, n )
  for i in range ( 0, m ):
    jhi = min ( i, n )
    for j in range ( i, n ):
      a[i,j] = float ( fac * i + j )

  return a

def r8ut_indicator_test ( ):

#*****************************************************************************80
#
## R8UT_INDICATOR_TEST tests R8UT_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8UT_INDICATOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8UT_INDICATOR sets up an indicator matrix in R8UT format' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a = r8ut_indicator ( m, n )

  r8ut_print ( m, n, a, '  The indicator matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8UT_INDICATOR_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ut_mm ( n, a, b ):

#*****************************************************************************80
#
## R8UT_MM computes C = A * B, where A and B are R8UT matrices.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    The product C will also be an upper trangular matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrices.
#    N must be positive.
#
#    Input, real A(N,N), B(N,N), the factors.
#
#    Output, real C(N,N), the product.
#
  c = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      for k in range ( i, j + 1 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def r8ut_mm_test ( ):

#*****************************************************************************80
#
## R8UT_MM_TEST tests R8UT_MM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5
 
  print ( '' )
  print ( 'R8UT_MM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8UT_MM computes C = A * B for R8UT matrices.' )
 
  a = r8ut_zeros ( n, n )
  for i in range ( 0, n ):
    for j in range ( i, n ):
      a[i,j] = 1.0

  r8ut_print ( n, n, a, '  The matrix A:' )

  c = r8ut_mm ( n, a, a )
  r8ut_print ( n, n, c, '  The product C = A * A' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8UT_MM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ut_mtm ( n, a, b ):

#*****************************************************************************80
#
## R8UT_MTM computes C = A' * B, where A and B are R8UT matrices.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    The product C will NOT be an R8UT matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrices.
#    N must be positive.
#
#    Input, real A(N,N), B(N,N), the factors.
#
#    Output, real C(N,N), the product.
#
  c = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      k_hi = min ( i + 1, j + 1 )
      for k in range ( 0, k_hi ):
        c[i,j] = c[i,j] + a[k,i] * b[k,j]

  return c

def r8ut_mtm_test ( ):

#*****************************************************************************80
#
## R8UT_MTM_TEST tests R8UT_MTM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8ge import r8ge_print

  n = 5
 
  print ( '' )
  print ( 'R8UT_MTM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8UT_MTM computes C = A\' * B for R8UT matrices.' )
 
  a = r8ut_zeros ( n, n )
  for i in range ( 0, n ):
    for j in range ( i, n ):
      a[i,j] = 1.0

  r8ut_print ( n, n, a, '  The matrix A:' )

  c = r8ut_mtm ( n, a, a )
  r8ge_print ( n, n, c, '  The product C = A\' * A' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8UT_MTM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ut_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## R8UT_MTV multiplies a vector by a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Input, real A(M,N), the R8UT matrix.
#
#    Input, real X(M), the vector to be multiplied by A.
#
#    Output, real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    jhi = min ( i + 1, m )
    for j in range ( 0, jhi ):
      b[i] = b[i] + x[j] * a[j,i]

  return b

def r8ut_mtv_test ( ):

#*****************************************************************************80
#
## R8UT_MTV_TEST tests R8UT_MTV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  m = 5
  n = 4

  print ( '' )
  print ( 'R8UT_MTV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8UT_MTV computes a matrix product b=A\'*x for an R8UT matrix.' )

  a = r8ut_indicator ( m, n )
  r8ut_print ( m, n, a, '  The matrix A:' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  The vector X:' )

  b = r8ut_mtv ( m, n, a, x )
  r8vec_print ( n, b, '  The vector b=A''*x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8UT_MTV_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ut_mv ( m, n, a, x ):

#*****************************************************************************80
#
## R8UT_MV multiplies a R8UT matrix times a vector.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Input, real A(M,N), the R8UT matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( i, n ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8ut_mv_test ( ):

#*****************************************************************************80
#
## R8UT_MV_TEST tests R8UT_MV
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  m = 5
  n = 4

  print ( '' )
  print ( 'R8UT_MV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8UT_MV computes a product b=A*x for an R8UT matrix.' )

  a = r8ut_indicator ( m, n )
  r8ut_print ( m, n, a, '  The R8UT matrix A:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  Vector x:' )

  b = r8ut_mv ( m, n, a, x )
  r8vec_print ( m, b, '  Vector b = A*x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8UT_MV_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ut_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8UT_PRINT prints a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2006
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Input, real A(M,N), the R8UT matrix.
#
#    Input, string TITLE, a title to be printed.
#
  r8ut_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ut_print_test ( ):

#*****************************************************************************80
#
## R8UT_PRINT_TEST tests R8UT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8UT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8UT_PRINT prints an R8UT matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [  0.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [  0.0,  0.0, 33.0, 34.0, 35.0, 36.0 ], 
    [  0.0,  0.0,  0.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ut_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8UT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ut_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8UT_PRINT_SOME prints some of a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Input, real A(M,N), the R8UT matrix.
#
#    Input, integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ' ),
    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )
#
#  Determine the range of the rows in this strip.
#
    inc = j2hi + 1 - j2lo
    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )
    i2hi = min ( i2hi, j2hi )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( j < i ):
          print ( '              ' ),
        else:
          print ( '%12g  ' % ( a[i,j] ) ),

      print ( '' )

def r8ut_print_some_test ( ):

#*****************************************************************************80
#
## R8UT_PRINT_SOME_TEST tests R8UT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8UT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8UT_PRINT_SOME prints some of an R8UT matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [  0.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [  0.0,  0.0, 33.0, 34.0, 35.0, 36.0 ], 
    [  0.0,  0.0,  0.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ut_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8UT matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8UT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ut_sl ( n, a, b ):

#*****************************************************************************80
#
## R8UT_SL solves a linear system A*x=b with an R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    No factorization of the upper triangular matrix is required.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real A(N,N), the R8UT matrix.
#
#    Input, real B(N), the right hand side.
#
#    Output, real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )
  
  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( n - 1, -1, -1 ):
    x[j] = x[j] / a[j,j]
    for i in range ( 0, j ):
      x[i] = x[i] - a[i,j] * x[j]

  return x

def r8ut_sl_test ( ):

#*****************************************************************************80
#
## R8UT_SL_TEST tests R8UT_SL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 5

  print ( '' )
  print ( 'R8UT_SL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8UT_SL solves a linear system A*x=b with R8UT matrix' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = float ( j + 1 )

  r8ut_print ( n, n, a, '  The upper triangular matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ut_mv ( n, n, a, x )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8ut_sl ( n, a, b )

  r8vec_print ( n, x, '  Solution:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8UT_SL_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ut_slt ( n, a, b ):

#*****************************************************************************80
#
## R8UT_SLT solves a linear system A'*x=b with an R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    No factorization of the upper triangular matrix is required.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real A(N,N), the R8UT matrix.
#
#    Input, real B(N), the right hand side.
#
#    Output, real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( 0, n ):
    x[j] = x[j] / a[j,j]
    for i in range ( j + 1, n ):
      x[i] = x[i] - x[j] * a[j,i]

  return x

def r8ut_slt_test ( ):

#*****************************************************************************80
#
## R8UT_SLT_TEST tests R8UT_SLT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 5

  print ( '' )
  print ( 'R8UT_SLT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8UT_SLT solves a linear system A''x=b with R8UT matrix' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = float ( j + 1 )

  r8ut_print ( n, n, a, '  The upper triangular matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ut_mtv ( n, n, a, x )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8ut_slt ( n, a, b )

  r8vec_print ( n, x, '  Solution to transposed system:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8UT_SLT_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ut_zeros ( m, n ):

#*****************************************************************************80
#
## R8GE_ZEROS zeroes an R8GE matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  return a

def r8ut_zeros_test ( ):

#*****************************************************************************80
#
## R8UT_ZEROS_TEST tests R8UT_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8UT_ZEROS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8UT_ZEROS zeros out space for an R8UT matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8ut_zeros ( m, n )

  r8ut_print ( m, n, a, '  Matrix A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8UT_ZEROS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8ut_indicator_test ( )
  r8ut_mm_test ( )
  r8ut_mtm_test ( )
  r8ut_mtv_test ( )
  r8ut_mv_test ( )
  r8ut_print_test ( )
  r8ut_print_some_test ( )
  r8ut_sl_test ( )
  r8ut_slt_test ( )
  r8ut_zeros_test ( )
  timestamp ( )

