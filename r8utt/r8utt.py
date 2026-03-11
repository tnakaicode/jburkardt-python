#! /usr/bin/env python3
#
def r8utt_test ( ):

#*****************************************************************************80
#
## r8utt_test() tests r8utt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8utt_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8utt().' )

  r8utt_det_test ( )
  r8utt_indicator_test ( )
  r8utt_inverse_test ( )
  r8utt_mm_test ( )
  r8utt_mtm_test ( )
  r8utt_mtv_test ( )
  r8utt_mv_test ( )
  r8utt_print_test ( )
  r8utt_print_some_test ( )
  r8utt_random_test ( )
  r8utt_sl_test ( )
  r8utt_slt_test ( )
  r8utt_to_r8ge_test ( )
  r8utt_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8utt_test():' )
  print ( '  Normal end of execution.' )
  return
 
def r8utt_det ( n, a ):

#*****************************************************************************80
#
## r8utt_det() computes the determinant of a R8UTT matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the matrix.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = a[0] ** n

  return det

def r8utt_det_test ( ):

#*****************************************************************************80
#
## r8utt_det_test() tests r8utt_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8utt_det_test():' )
  print ( '  r8utt_det() computes the determinant of an R8UTT matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_random ( n )

  r8utt_print ( n, a, '  The matrix:' )
#
#  Compute the determinant.
#
  det = r8utt_det ( n, a )

  print ( '' )
  print ( '  The determinant = ', det )

  return

def r8utt_indicator ( n ):

#*****************************************************************************80
#
## r8utt_indicator() sets up a R8UTT indicator matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N), the matrix.
#
  import numpy as np

  a = np.zeros ( n )

  for j in range ( 0, n ):
    a[j] = float ( j + 1 )

  return a

def r8utt_indicator_test ( ):

#*****************************************************************************80
#
## r8utt_indicator_test() tests r8utt_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8utt_indicator_test():' )
  print ( '  r8utt_indicator() sets up an indicator matrix in R8UTT format' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_indicator ( n )

  r8utt_print ( n, a, '  The indicator matrix:' )

  return

def r8utt_inverse ( n, a ):

#*****************************************************************************80
#
## R8UTT_INVERSE computes the inverse of a R8UTT matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the matrix to be inverted.
#
#  Output:
#
#    real B(N), the inverse matrix.
#
  import numpy as np
#
#  Initialize B.
#
  d = 1.0 / a[0]
  b = np.zeros ( n )
  b[0] = d 
#
#  Set the strict upper triangle.
#
  p = np.zeros ( n )
  for i in range ( 1, n ):
    p[i] = a[i];
#
#  PN will hold powers of P.
#
  pn = np.zeros ( n )
  pn[0] = 1.0
#
#  Add N-1 powers of strict upper triangle.
#
  for j in range ( 1, n ):
    d = - d / a[0]
    pn = r8utt_mm ( n, p, pn )
    for i in range ( 0, n ):
      b[i] = b[i] + d  * pn[i]

  return b

def r8utt_inverse_test ( ):

#*****************************************************************************80
#
## R8UTT_INVERSE_TEST tests R8UTT_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8UTT_INVERSE_TEST' )
  print ( '  R8UTT_INVERSE computes the inverse of an R8UTT matrix.' )

  a = r8utt_random ( n )

  r8utt_print ( n, a, '  The matrix A:' )
#
#  Compute the inverse matrix B.
#
  b = r8utt_inverse ( n, a )

  r8utt_print ( n, b, '  The inverse matrix B:' )
#
#  Check
#
  c = r8utt_mm ( n, a, b )

  r8utt_print ( n, c, '  The product A * B:' )

  return

def r8utt_mm ( n, a, b ):

#*****************************************************************************80
#
## R8UTT_MM computes C = A * B, where A and B are R8UTT matrices.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrices.
#
#    real A(N), the first factor.
#
#    real B(N), the second factor.
#
#  Output:
#
#    real C(N), the product.
#
  import numpy as np

  c = np.zeros ( n )

  d = np.zeros ( n )

  for i in range ( 0, n ):
    d[n-1-i] = b[i]

  e = r8utt_mv ( n, a, d )

  for i in range ( 0, n ):
    c[i] = e[n-1-i]

  return c

def r8utt_mm_test ( ):

#*****************************************************************************80
#
## R8UTT_MM_TEST tests R8UTT_MM.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
 
  print ( '' )
  print ( 'R8UTT_MM_TEST' )
  print ( '  R8UTT_MM computes C = A * B for R8UTT matrices.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_random ( n )
  r8utt_print ( n, a, '  Factor A:' )
  b = r8utt_random ( n )
  r8utt_print ( n, b, '  Factor B:' )
  c = r8utt_mm ( n, a, b )
  r8utt_print ( n, c, '  The product C = A * B' )

  a_ge = r8utt_to_r8ge ( n, a )
  b_ge = r8utt_to_r8ge ( n, b )
  c_ge = np.matmul ( a_ge, b_ge )

  print ( '' )
  print ( '  The R8GE product C:' )
  print ( c_ge )

  return

def r8utt_mtm ( n, a, b ):

#*****************************************************************************80
#
## R8UTT_MTM computes C = A' * B, where A and B are R8UTT matrices.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#    Note that the result C is a dense matrix, of type R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrices.
#
#    real A(N), B(N), the factors.
#
#  Output:
#
#    real C(N,N), the product.
#
  import numpy as np

  c = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( 0, min ( i, j ) + 1 ):
        c[i,j] = c[i,j] + a[i-k] * b[j-k]

  return c

def r8utt_mtm_test ( ):

#*****************************************************************************80
#
## R8UTT_MTM_TEST tests R8UTT_MTM.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
 
  print ( '' )
  print ( 'R8UTT_MTM_TEST' )
  print ( '  R8UTT_MTM computes C = A\' * B for R8UTT matrices.' )
 
  a = r8utt_random ( n )
  r8utt_print ( n, a, '  The matrix A:' )
  b = r8utt_random ( n )
  r8utt_print ( n, b, '  The matrix B:' )

  c = r8utt_mtm ( n, a, b )

  print ( '' )
  print ( '  The product C = A\' * B:' )
  print ( c )
#
#  Compare with an R8GE calculation.
#
  a_ge = r8utt_to_r8ge ( n, a )
  b_ge = r8utt_to_r8ge ( n, b )

  c_ge = np.matmul ( np.transpose ( a_ge ), b_ge )
  print ( '' )
  print ( '  The R8GE product C = A\' * B:' )
  print ( c_ge )

  return

def r8utt_mtv ( n, a, x ):

#*****************************************************************************80
#
## R8UTT_MTV computes b = A'*x, where A is an R8UTT matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for d in range ( 0, n ):
    for j in range ( d, n ):
      i = j - d
      b[j] = b[j] + a[j-i] * x[i]

  return b

def r8utt_mtv_test ( ):

#*****************************************************************************80
#
## R8UTT_MTV_TEST tests R8UTT_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8UTT_MTV_TEST' )
  print ( '  R8UTT_MTV computes a matrix product b=A\'*x for an R8UTT matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_indicator ( n )
  r8utt_print ( n, a, '  The matrix A:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  The vector X:' )

  b = r8utt_mtv ( n, a, x )
  r8vec_print ( n, b, '  The vector b=A\'*x:' )

  return

def r8utt_mv ( n, a, x ):

#*****************************************************************************80
#
## R8UTT_MV computes b=A*x, where A is an R8UTT matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )

  for d in range ( 0, n ):
    for j in range ( d, n ):
      i = j - d
      b[i] = b[i] + a[j-i] * x[j]

  return b

def r8utt_mv_test ( ):

#*****************************************************************************80
#
## R8UTT_MV_TEST tests R8UTT_MV
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8UTT_MV_TEST' )
  print ( '  R8UTT_MV computes a product b=A*x for an R8UTT matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_indicator ( n )
  r8utt_print ( n, a, '  The R8UTT matrix A:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  Vector x:' )

  b = r8utt_mv ( n, a, x )
  r8vec_print ( n, b, '  Vector b = A*x:' )

  return

def r8utt_print ( n, a, title ):

#*****************************************************************************80
#
## R8UTT_PRINT prints a R8UTT matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the matrix.
#
#    string TITLE, a title to be printed.
#
  r8utt_print_some ( n, a, 0, 0, n - 1, n - 1, title )

  return

def r8utt_print_test ( ):

#*****************************************************************************80
#
## R8UTT_PRINT_TEST tests R8UTT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8UTT_PRINT_TEST' )
  print ( '  R8UTT_PRINT prints an R8UTT matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_indicator ( n )

  r8utt_print ( n, a, '  The matrix:' )

  return

def r8utt_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8UTT_PRINT_SOME prints some of a R8UTT matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8UTT matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#    1 <= ILO <= IHI <= N.
#    1 <= JLO <= JHI <= N.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )
    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )
#
#  Determine the range of the rows in this strip.
#
    print ( '' )
    print ( '  Row' )
    inc = j2hi + 1 - j2lo
    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, n - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( j < i ):
          print ( '              ', end = '' )
        else:
          print ( '%12g  ' % ( a[j-i] ), end = '' )

      print ( '' )

  return

def r8utt_print_some_test ( ):

#*****************************************************************************80
#
## R8UTT_PRINT_SOME_TEST tests R8UTT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 6

  print ( '' )
  print ( 'R8UTT_PRINT_SOME_TEST' )
  print ( '  R8UTT_PRINT_SOME prints some of an R8UTT matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_indicator ( n )

  r8utt_print_some ( n, a, 1, 4, 3, 6, '  Some of the matrix:' )

  return

def r8utt_random ( n ):

#*****************************************************************************80
#
## R8UTT_RANDOM randomizes an R8UTT matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#
#  Output:
#
#    real A(N), the R8UTT matrix.
#
  from numpy.random import default_rng

  rng = default_rng ( )

  a = rng.random ( size = n )

  return a

def r8utt_random_test ( ):

#*****************************************************************************80
#
## R8UTT_RANDOM_TEST tests R8UTT_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8UTT_RANDOM_TEST' )
  print ( '  R8UTT_RANDOM randomizes an R8UTT matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_random ( n )

  r8utt_print ( n, a, '  Matrix A:' )

  return

def r8utt_sl ( n, a, b ):

#*****************************************************************************80
#
## R8UTT_SL solves a linear system A*x=b with an R8UTT matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#    No factorization of the upper triangular matrix is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8UTT matrix.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( n - 1, -1, -1 ):
    x[j] = x[j] / a[0]
    for i in range ( 0, j ):
      x[i] = x[i] - a[j-i] * x[j]

  return x

def r8utt_sl_test ( ):

#*****************************************************************************80
#
## R8UTT_SL_TEST tests R8UTT_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8UTT_SL_TEST' )
  print ( '  R8UTT_SL solves a linear system A*x=b with R8UTT matrix' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_random ( n )

  r8utt_print ( n, a, '  Matrix A:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8utt_mv ( n, a, x )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8utt_sl ( n, a, b )

  r8vec_print ( n, x, '  Solution x:' )

  return

def r8utt_slt ( n, a, b ):

#*****************************************************************************80
#
## R8UTT_SLT solves a linear system A'*x=b with an R8UTT matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#    No factorization of the upper triangular matrix is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8UTT matrix.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( 0, n ):
    x[j] = x[j] / a[0]
    for i in range ( j + 1, n ):
      x[i] = x[i] - x[j] * a[i-j]

  return x

def r8utt_slt_test ( ):

#*****************************************************************************80
#
## R8UTT_SLT_TEST tests R8UTT_SLT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8UTT_SLT_TEST' )
  print ( '  R8UTT_SLT solves a linear system A\'x=b with R8UTT matrix' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_random ( n )

  r8utt_print ( n, a, '  Matrix A:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8utt_mtv ( n, a, x )

  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8utt_slt ( n, a, b )

  r8vec_print ( n, x, '  Solution x:' )

  return

def r8utt_to_r8ge ( n, a_utt ):

#*****************************************************************************80
#
## R8UTT_TO_R8GE copies an R8UTT matrix to an R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A_UTT(N), the R8UTT matrix.
#
#  Output:
#
#    real A_GE(N,N), the R8GE matrix.
#
  import numpy as np

  a_ge = np.zeros ( [ n, n ] )

  for d in range ( 0, n ):
    for j in range ( d, n ):
      i = j - d
      a_ge[i,j] = a_utt[j-i]

  return a_ge

def r8utt_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8UTT_TO_R8GE_TEST tests R8UTT_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8UTT_TO_R8GE_TEST' )
  print ( '  R8UTT_TO_R8GE converts an R8UTT matrix to R8GE format.' )

  a_utt = r8utt_random ( n )

  r8utt_print ( n, a_utt, '  The random R8UTT matrix:' )
 
  a_ge = r8utt_to_r8ge ( n, a_utt )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_ge )

  return

def r8utt_zeros ( n ):

#*****************************************************************************80
#
## R8UTT_ZEROS zeroes an R8UTT matrix.
#
#  Discussion:
#
#    The R8UTT storage format is used for an N by N upper triangular Toeplitz
#    matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N), the matrix.
#
  import numpy as np

  a = np.zeros ( n )

  return a

def r8utt_zeros_test ( ):

#*****************************************************************************80
#
## R8UTT_ZEROS_TEST tests R8UTT_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8UTT_ZEROS_TEST' )
  print ( '  R8UTT_ZEROS zeros out space for an R8UTT matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8utt_zeros ( n )

  r8utt_print ( n, a, '  The matrix:' )

  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

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
  r8utt_test ( )
  timestamp ( )

