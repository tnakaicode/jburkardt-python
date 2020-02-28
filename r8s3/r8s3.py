#! /usr/bin/env python3
#
def r8s3_diagonal ( m, n, nz_num, sym, row, col, a ):

#*****************************************************************************80
#
## R8S3_DIAGONAL reorders a square R8S3 matrix so diagonal entries are first.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#    This routine reorders the entries of A so that the first N entries
#    are exactly the diagonal entries of the matrix, in order.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, 
#    and 1 if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input/output, integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    Input/output, real A(NZ_NUM), the nonzero elements 
#    of the matrix.
#
  found = 0

  for k in range ( 0, nz_num ):

    while ( row[k] == col[k] ):

      if ( row[k] == k ):
        found = found + 1
        break

      i = row[k]

      j = row[i]
      row[i] = row[k]
      row[k] = j

      j = col[i]
      col[i] = col[k]
      col[k] = j

      t    = a[i]
      a[i] = a[k]
      a[k] = t
 
      found = found + 1

      if ( min ( m, n ) <= found ):
        break

    if ( min ( m, n ) <= found ):
      break

  if ( found < min ( m, n ) ):
    print ( '' )
    print ( 'R8S3_DIAGONAL - Warning!' )
    print ( '  Number of diagonal entries expected was %d' % ( min ( m, n ) ) )
    print ( '  Number found was %d' % ( found ) )

  return row, col, a

def r8s3_diagonal_test ( ):

#*****************************************************************************80
#
## R8S3_DIAGONAL_TEST tests R8S3_DIAGONAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nz_num = 20

  col = np.array ( [ \
    4, 5, 1, 1, 2, 3, 3, 4, 0, 5, \
    3, 5, 4, 0, 5, 2, 0, 1, 0, 2 ], dtype = np.int32 )

  row = np.array ( [ \
    0, 2, 3, 5, 4, 1, 5, 2, 0, 1, \
    3, 5, 4, 3, 3, 2, 5, 1, 2, 3 ], dtype = np.int32 )

  print ( '' )
  print ( 'R8S3_DIAGONAL_TEST' )
  print ( '  R8S3_DIAGONAL rearranges an R8S3 matrix' )
  print ( '  so that the diagonal is listed first.' )

  m = 6
  n = 6
  sym = 0

  print ( '' )
  print ( '  Matrix order M =         %d' % ( m ) )
  print ( '  Matrix order N =         %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM =    %d' % ( sym ) )

  a = r8s3_indicator ( m, n, nz_num, sym, row, col )

  print ( '' )
  print ( '  Before rearrangement:' )
  print ( '         K    ROW(K)    COL(K)      A(K)' )
  print ( '' )
  for k in range ( 0, nz_num ):
    print ( '  %8d  %8d  %8d  %14.6g' % ( k, row[k], col[k], a[k] ) )

  row, col, a = r8s3_diagonal ( m, n, nz_num, sym, row, col, a )

  print ( '' )
  print ( '  After rearrangement:' )
  print ( '         K    ROW(K)    COL(K)      A(K)' )
  print ( '' )
  for k in range ( 0, nz_num ):
    print ( '  %8d  %8d  %8d  %14.6g' % ( k, row[k], col[k], a[k] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_DIAGONAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_dif2 ( m, n, nz_num, sym ):

#*****************************************************************************80
#
## R8S3_DIF2 sets up an R8S3 second difference matrix.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero entries.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, 
#    and 1 if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Output, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column
#    indices of the nonzero elements.
#
#    Output, real A(NZ_NUM), the indicator matrix.
#
  import numpy as np

  if ( sym == 1 ):
    nz_num = 2 * n - 1
  elif ( m == n ):
    nz_num = 3 * n - 2
  else:
    nz_num = 3 * n - 1

  row = np.zeros ( nz_num, dtype = np.int32 )
  col = np.zeros ( nz_num, dtype = np.int32 )
  a = np.zeros ( nz_num, dtype = np.float64 )

  k = 0
#
#  Diagonal entries.
#
  for j in range ( 0, n ):

    i = j
    row[k] = i
    col[k] = j
    a[k] = 2.0
    k = k + 1
#
#  Offdiagonal nonzeros, by column.
#
  for j in range ( 0, n ):

    if ( sym != 1 ):
      if ( 0 < j ):
        i = j - 1
        row[k] = i
        col[k] = j
        a[k] = -1.0
        k = k + 1

    if ( j + 1 <= m - 1 ):
      i = j + 1
      row[k] = i
      col[k] = j
      a[k] = -1.0
      k = k + 1

  return row, col, a

def r8s3_dif2_test ( ):

#*****************************************************************************80
#
## R8S3_DIF2_TEST tests R8S3_DIF2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8S3_DIF2_TEST' )
  print ( '  R8S3_DIF2 sets an R8S3 matrix to the second difference.' )

  m = 5
  n = 5
  nz_num = 3 * n - 2
  sym = 0

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  r8s3_print ( m, n, nz_num, sym, row, col, a, '  R8S3 matrix A:' )

  m = 5
  n = 5
  nz_num = 2 * n - 1
  sym = 1

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  r8s3_print ( m, n, nz_num, sym, row, col, a, '  R8S3 matrix A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_DIF2_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_indicator ( m, n, nz_num, sym, row, col ):

#*****************************************************************************80
#
## R8S3_INDICATOR sets up a R8S3 indicator matrix.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero entries.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, and 1
#    if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    Output, real A(NZ_NUM), the indicator matrix.
#
  import numpy as np
  from i4_log_10 import i4_log_10

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( nz_num, dtype = np.float64 )

  for k in range ( 0, nz_num ):
    i = row[k]
    j = col[k]
    a[k] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8s3_indicator_test ( ):

#*****************************************************************************80
#
## R8S3_INDICATOR_TEST tests R8S3_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 6
  n = 6
  nz_num = 20
  row = np.array ( [0,2,3,5,4,1,5,2,0,1,3,5,4,3,3,2,5,1,2,3], dtype = np.int32 )
  col = np.array ( [4,5,1,1,2,3,3,4,0,5,3,5,4,0,5,2,0,1,0,2], dtype = np.int32 )
  sym = 0

  print ( '' )
  print ( 'R8S3_INDICATOR_TEST' )
  print ( '  R8S3_INDICATOR sets an R8S3 indicator matrix.' )
  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  a = r8s3_indicator ( m, n, nz_num, sym, row, col )

  r8s3_print ( m, n, nz_num, sym, row, col, a, '  Matrix A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_INDICATOR_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_jac_sl ( n, nz_num, sym, row, col, a, b, x, it_max ):

#*****************************************************************************80
#
## R8S3_JAC_SL solves an R8S3 system using Jacobi iteration.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#    This routine REQUIRES that the matrix be square, that the matrix
#    have nonzero diagonal entries, and that the first N entries of
#    the array A be exactly the diagonal entries of the matrix, in order.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, 
#    and 1 if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column 
#    indices of the nonzero elements.
#
#    Input, real A(NZ_NUM), the nonzero elements of the matrix.
#
#    Input, real B(N), the right hand side of the linear system.
#
#    Input/output, real X(N), an approximate solution 
#    to the system.
#
#    Input, integer IT_MAX, the maximum number of iterations.
#
  import numpy as np

  x_new = np.zeros ( n )

  for it_num in range ( 0, it_max ):
#
#  Initialize to right hand side.
#
    for i in range ( 0, n ):
      x_new[i] = b[i]
#
#  Subtract off-diagonal terms.
#
    for k in range ( n, nz_num ):
      i = row[k]
      j = col[k]
      x_new[i] = x_new[i] - a[k] * x[j]
      if ( sym == 1 ):
        x_new[j] = x_new[j] - a[k] * x[i]
#
#  Update.
#
    for i in range ( 0, n ):
      x[i] = x_new[i] / a[i]

  return x

def r8s3_jac_sl_test ( ):

#*****************************************************************************80
#
## R8S3_JAC_SL_TEST tests R8S3_JAC_SL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8S3_JAC_SL_TEST' )
  print ( '  R8S3_JAC_SL uses Jacobi iteration to solve a linear system' )
  print ( '  with an R8S3 matrix.' )

  m = 10
  n = 10
  nz_num = 3 * n - 2
  sym = 0
  it_max = 25

  print ( '' )
  print ( '  Matrix order M =         %8d' % ( m ) )
  print ( '  Matrix order N =         %8d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %8d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %8d' % ( sym ) )
  print ( '  Iterations per         = %8d' % ( it_max ) )
#
#  Set the matrix values.
#
  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Solving A * x = b.' )
  print ( '' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8s3_mv ( n, n, nz_num, sym, row, col, a, x )
#
#  Set the starting solution.
#
  x = np.zeros ( n )
#
#  Solve the linear system.
#
  for i in range ( 0, 3 ):

    x = r8s3_jac_sl ( n, nz_num, sym, row, col, a, b, x, it_max )

    r8vec_print ( n, x, '  Current solution estimate:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_JAC_SL_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_mtv ( m, n, nz_num, sym, row, col, a, x ):

#*****************************************************************************80
#
## R8S3_MTV multiplies an R8VEC times an R8S3 matrix.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, 
#    and 1 if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column
#    indices of the nonzero elements.
#
#    Input, real A(NZ_NUM), the nonzero elements of the matrix.
#
#    Input, real X(M), the vector to be multiplied by A'.
#
#    Output, real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for k in range ( 0, nz_num ):
    i = col[k]
    j = row[k]
    b[i] = b[i] + a[k] * x[j]
#
#  Handle the symmetric option.
#
  if ( sym == 1 and m == n ):
    for k in range ( 0, nz_num ):
      i = row[k]
      j = col[k]
      if ( i != j ):
        b[i] = b[i] + a[k] * x[j]

  return b

def r8s3_mtv_test ( ):

#*****************************************************************************80
#
## R8S3_MTV_TEST tests R8S3_MTV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8S3_MTV_TEST' )
  print ( '  R8S3_MTV computes b=A\'*x, where A is an R8S3 matrix.' )

  m = 5
  n = 4
  if ( m == n ):
    nz_num = 3 * n - 2
  else:
    nz_num = 3 * n - 1
  sym = 0

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M =         %d' % ( m ) )
  print ( '  Matrix order N =         %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM =    %d' % ( sym ) )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  x:' )

  b = r8s3_mtv ( m, n, nz_num, sym, row, col, a, x )

  r8vec_print ( n, b, '  b=A\'*x:' )
#
#  Try symmetric option.
#
  m = 5
  n = 5
  nz_num = 2 * n - 1
  sym = 1

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M =         %d' % ( m ) )
  print ( '  Matrix order N =         %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM =    %d' % ( sym ) )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  x:' )

  b = r8s3_mtv ( m, n, nz_num, sym, row, col, a, x )

  r8vec_print ( n, b, '  b=A\'*x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_MTV_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_mv ( m, n, nz_num, sym, row, col, a, x ):

#*****************************************************************************80
#
## R8S3_MV multiplies an R8S3 matrix by an R8VEC.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, 
#    and 1 if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column 
#    indices of the nonzero elements.
#
#    Input, real A(NZ_NUM), the nonzero elements of the matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for k in range ( 0, nz_num ):
    i = row[k]
    j = col[k]
    b[i] = b[i] + a[k] * x[j]
#
#  Handle the symmetric option.
#
  if ( sym == 1 and m == n ):
    for k in range ( 0, nz_num ):
      i = col[k]
      j = row[k]
      if ( i != j ):
        b[i] = b[i] + a[k] * x[j]

  return b

def r8s3_mv_test ( ):

#*****************************************************************************80
#
## R8S3_MV_TEST tests R8S3_MV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8S3_MV_TEST' )
  print ( '  R8S3_MV computes b=A*x, where A is an R8S3 matrix.' )

  m = 5
  n = 4
  if ( m == n ):
    nz_num = 3 * n - 2
  else:
    nz_num = 3 * n - 1
  sym = 0

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M =         %d' % ( m ) )
  print ( '  Matrix order N =         %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM =    %d' % ( sym ) )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )

  b = r8s3_mv ( m, n, nz_num, sym, row, col, a, x )

  r8vec_print ( m, b, '  b=A*x:' )
#
#  Try symmetric option.
#
  m = 5
  n = 5
  nz_num = 2 * n - 1
  sym = 1

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M =         %d' % ( m ) )
  print ( '  Matrix order N =         %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM =    %d' % ( sym ) )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )

  b = r8s3_mv ( m, n, nz_num, sym, row, col, a, x )

  r8vec_print ( m, b, '  b=A*x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_MV_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_print ( m, n, nz_num, sym, row, col, a, title ):

#*****************************************************************************80
#
## R8S3_PRINT prints a R8S3 matrix.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, and 1
#    if the matrix is symmetric.  The symmetric case only makes sense
#    if the matrix is also square, that is, M = N.  In this case, only
#    the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    Input, real A(NZ_NUM), the nonzero elements of the matrix.
#
#    Input, string TITLE, a title.
#
  r8s3_print_some ( m, n, nz_num, sym, row, col, a, 0, 0, m - 1, n - 1, title )

  return

def r8s3_print_test ( ):

#*****************************************************************************80
#
## R8S3_PRINT_TEST tests R8S3_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8S3_PRINT_TEST' )
  print ( '  R8S3_PRINT prints an R8S3 matrix.' )

  m = 5
  n = 5
  nz_num = 3 * n - 2
  sym = 0

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  r8s3_print ( m, n, nz_num, sym, row, col, a, '  R8S3 matrix A:' )

  m = 5
  n = 5
  nz_num = 2 * n - 1
  sym = 1

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  r8s3_print ( m, n, nz_num, sym, row, col, a, '  R8S3 matrix A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_print_some ( m, n, nz_num, sym, row, col, a, ilo, jlo, ihi, jhi, \
  title ):

#*****************************************************************************80
#
## R8S3_PRINT_SOME prints some of an R8S3 matrix.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M,  N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, and 1
#    if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW[NZ_NUM], COL[NZ_NUM], the row and column indices
#    of the nonzero elements.
#
#    Input, real A[NZ_NUM], the nonzero elements 
#    of the matrix.
#
#    Input, integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    Input, string TITLE, a title.
#
  import numpy as np

  incx = 5
  index = np.zeros ( incx, dtype = np.int32 )

  print ( '' )
  print ( title )
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):
    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )

    inc = j2hi + 1 - j2lo

    print ( '' )

    print ( '  Col: ', end = '' )
    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )
    print ( '  ---' )
#
#  Determine the range of the rows in this strip.
#
    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      nonzero = False
 
      for j2 in range ( 0, inc ):
        index[j2] = -1

      for k in range ( 0, nz_num ):

        if ( i == row[k] and j2lo <= col[k] and col[k] <= j2hi ):

          j2 = col[k] - j2lo + 1

          if ( a[k] != 0.0 ):
            index[j2-1] = k
            nonzero = True

        elif ( sym == 1 and m == n and i == col[k] and j2lo <= row[k] and row[k] <= j2hi ):

          j2 = row[k] - j2lo + 1

          if ( a[k] != 0.0 ):
            index[j2-1] = k
            nonzero = True

      if ( nonzero ):

        print ( '%5d ' % ( i ), end = '' )

        for j2 in range ( 0, inc ):

          if ( 0 <= index[j2] ):
            aij = a[index[j2]]
          else:
            aij = 0.0

          print ( '%14g' % ( aij ), end = '' )

        print ( '' )

  return

def r8s3_print_some_test ( ):

#*****************************************************************************80
#
## R8S3_PRINT_SOME_TEST tests R8S3_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8S3_PRINT_SOME_TEST' )
  print ( '  R8S3_PRINT_SOME prints some of an R8S3 matrix.' )

  m = 5
  n = 5
  nz_num = 3 * n - 2
  sym = 0

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  r8s3_print_some ( m, n, nz_num, sym, row, col, a, 2, 3, 4, 5, '  Rows 2:4, Cols 3:5:' )

  m = 5
  n = 5
  nz_num = 2 * n - 1
  sym = 1

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  r8s3_print_some ( m, n, nz_num, sym, row, col, a, 2, 3, 4, 5, '  Rows 2:4, Cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_PRINT_SOME_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_random ( m, n, nz_num, sym, row, col, seed ):

#*****************************************************************************80
#
## R8S3_RANDOM randomizes an R8S3 matrix.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero entries.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, and 1
#    if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    Input/output, integer SEED, a seed for the random number generator.
#
#    Output, real A(NZ_NUM), the indicator matrix.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  a = np.zeros ( nz_num, dtype = np.float64 )

  for k in range ( 0, nz_num ):
    i = row[k]
    j = col[k]
    a[k], seed = r8_uniform_01 ( seed )

  return a, seed

def r8s3_random_test ( ):

#*****************************************************************************80
#
## R8S3_RANDOM_TEST tests R8S3_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 6
  n = 6
  nz_num = 20
  row = np.array ( [0,2,3,5,4,1,5,2,0,1,3,5,4,3,3,2,5,1,2,3], dtype = np.int32 )
  col = np.array ( [4,5,1,1,2,3,3,4,0,5,3,5,4,0,5,2,0,1,0,2], dtype = np.int32 )
  sym = 0
  seed = 123456789

  print ( '' )
  print ( 'R8S3_RANDOM_TEST' )
  print ( '  R8S3_RANDOM randomizes an R8S3 indicator matrix.' )
  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  a, seed = r8s3_random ( m, n, nz_num, sym, row, col, seed )

  r8s3_print ( m, n, nz_num, sym, row, col, a, '  Matrix A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_RANDOM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_read ( input_file, m, n, nz_num ):

#*****************************************************************************80
#
## R8S3_READ reads a square R8S3 matrix from a file.
#
#  Discussion:
#
#    This routine needs the value of NZ_NUM, which can be determined
#    by a call to R8S3_READ_SIZE.
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string INPUT_FILE, the name of the file to be read.
#
#    Unused, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    Output, integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    Output, real A(NZ_NUM), the nonzero elements 
#    of the matrix.
#
  import numpy as np

  row = np.zeros ( nz_num, dtype = np.int32 )
  col = np.zeros ( nz_num, dtype = np.int32 )
  a = np.zeros ( nz_num, dtype = np.float64 )

  input_unit = open ( input_file, 'r' )

  k = 0

  for line in input_unit:
    words = line.split ( )
    row[k] = int ( words[0] )
    col[k] = int ( words[1] )
    a[k] = float ( words[2] )
    k = k + 1

  input_unit.close ( )

  return row, col, a

def r8s3_read_size ( input_file ):

#*****************************************************************************80
#
## R8S3_READ_SIZE reads the size of an R8S3 matrix from a file.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string INPUT_FILE, the name of the file to be read.
#
#    Output, integer M, N, the order of the matrix.
#
#    Output, integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
  import numpy as np

  input_unit = open ( input_file, 'r' )

  m = -1
  n = -1
  nz_num = 0

  for line in input_unit:
    words = line.split ( )
    i = int ( words[0] )
    m = max ( m, i )
    j = int ( words[1] )
    n = max ( n, j )
    nz_num = nz_num + 1

  input_unit.close ( )

  return m, n, nz_num

def r8s3_read_test ( ):

#*****************************************************************************80
#
## R8S3_READ_TEST tests R8S3_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8S3_READ_TEST' )
  print ( '  R8S3_READ_SIZE reads the size of an R8S3 matrix.' )
  print ( '  R8S3_READ reads the R8S3 matrix from a file.' )

  input_file = 'r8s3_matrix.txt'

  m, n, nz_num = r8s3_read_size ( input_file )
  sym = 0

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  row, col, a = r8s3_read ( input_file, m, n, nz_num )

  r8s3_print_some ( m, n, nz_num, sym, row, col, a, 1, 1, \
    10, 10, '  Initial 10x10 block of recovered R8S3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_READ_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_res ( m, n, nz_num, sym, row, col, a, x, b ):

#*****************************************************************************80
#
## R8S3_RES computes the residual R = B-A*X for R8S3 matrices.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, 
#    and 1 if the matrix is symmetric.  The symmetric case only makes sense
#    if the matrix is also square, that is, M = N.  In this case, only
#    the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column
#    indices of the nonzero elements.
#
#    Input, real A(NZ_NUM), the nonzero elements of the matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Input, real B(M), the desired result A * x.
#
#    Output, real R(M), the residual R = B - A * X.
#
  r = r8s3_mv ( m, n, nz_num, sym, row, col, a, x )

  for i in range ( 0, m ):
    r[i] = b[i] - r[i]

  return r

def r8s3_res_test ( ):

#*****************************************************************************80
#
## R8S3_RES_TEST tests R8S3_RES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8S3_RES_TEST' )
  print ( '  R8S3_MRES computes r=b-A*x, where A is an R8S3 matrix.' )

  m = 5
  n = 4
  if ( m == n ):
    nz_num = 3 * n - 2
  else:
    nz_num = 3 * n - 1
  sym = 0

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )

  b = r8s3_mv ( m, n, nz_num, sym, row, col, a, x )

  r = r8s3_res ( m, n, nz_num, sym, row, col, a, x, b )

  r8vec_print ( m, r, '  r=b-A*x:' )
#
#  Try symmetric option.
#
  m = 5
  n = 5
  nz_num = 2 * n - 1
  sym = 1

  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )

  b = r8s3_mv ( m, n, nz_num, sym, row, col, a, x )

  r = r8s3_res ( m, n, nz_num, sym, row, col, a, x, b )

  r8vec_print ( m, r, '  r=b-A*x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_RES_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_to_r8ge ( m, n, nz_num, sym, row, col, a_r8s3 ):

#*****************************************************************************80
#
## R8S3_TO_R8GE copies an R8S3 matrix to an R8GE matrix.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, 
#    and 1 if the matrix is symmetric.  The symmetric case only makes sense
#    if the matrix is also square, that is, M = N.  In this case, only
#    the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column
#    indices of the nonzero elements.
#
#    Input, real A_R8S3(NZ_NUM), the nonzero elements of the matrix.
#
#    Output, real A_R8GE(M,N), the R8GE matrix.
#
  import numpy as np

  a_r8ge = np.zeros ( [ m, n ] )

  for k in range ( 0, nz_num ):
    i = row[k]
    j = col[k]
    a_r8ge[i,j] = a_r8ge[i,j] + a_r8s3[k]
    if ( sym == 1 and m == n and i != j ):
      a_r8ge[j,i] = a_r8ge[j,i] + a_r8s3[k]

  return a_r8ge

def r8s3_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8S3_TO_R8GE_TEST tests R8S3_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  from r8ge import r8ge_print

  print ( '' )
  print ( 'R8S3_TO_R8GE_TEST' )
  print ( '  R8S3_TO_R8GE converts an R8S3 matrix to R8GE format.' )

  m = 5
  n = 5
  nz_num = 3 * n - 2
  sym = 0

  row, col, a_r8s3 = r8s3_dif2 ( m, n, nz_num, sym )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )

  r8s3_print ( m, n, nz_num, sym, row, col, a_r8s3, '  R8S3 matrix A:' )

  a_r8ge = r8s3_to_r8ge ( m, n, nz_num, sym, row, col, a_r8s3 )

  r8ge_print ( m, n, a_r8ge, '  R8GE matrix A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_TO_R8GE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_write ( m, n, nz_num, sym, row, col, a, output_file ):

#*****************************************************************************80
#
## R8S3_WRITE writes a square R8S3 matrix to a file.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    There is a symmetry option for square matrices.  If the symmetric storage
#    option is used, the format specifies that only nonzeroes on the diagonal
#    and lower triangle are stored.  However, this routine makes no attempt
#    to enforce this.  The only thing it does is to "reflect" any nonzero
#    offdiagonal value.  Moreover, no check is made for the erroneous case
#    in which both A(I,J) and A(J,I) are specified, but with different values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 September 2006
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, 
#    and 1 if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column 
#    indices of the nonzero elements.
#
#    Input, real A(NZ_NUM), the nonzero elements 
#    of the matrix.
#
#    Input, string OUTPUT_FILE, the name of the file to which
#    the information is to be written.
#
  output_unit = open ( output_file, 'w' )

  for k in range ( 0, nz_num ):
    s = '%d  %d  %g\n' % ( row[k], col[k], a[k] )
    output_unit.write ( s )

  output_unit.close ( )

  return

def r8s3_write_test ( ):

#*****************************************************************************80
#
## R8S3_WRITE_TEST tests R8S3_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8S3_WRITE_TEST' )
  print ( '  R8S3_WRITE writes an R8S3 matrix to a file.' )

  m = 100
  n = 100
  nz_num = 3 * n - 2
  sym = 0

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
  print ( '  Symmetry option SYM    = %d' % ( sym ) )
#
#  Set the matrix values.
#
  row, col, a = r8s3_dif2 ( m, n, nz_num, sym )
#
#  Print a bit of the matrix.
#
  r8s3_print_some ( m, n, nz_num, sym, row, col, a, 1, 1, \
    10, 10, '  Initial 10x10 block of R8S3 matrix:' )
#
#  Write the matrix to a file.
#
  output_file = 'r8s3_matrix.txt'

  r8s3_write ( m, n, nz_num, sym, row, col, a, output_file )

  print ( '' )
  print ( '  Matrix data written to "%s".' % ( output_file ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_WRITE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_zeros ( m, n, nz_num, sym, row, col ):

#*****************************************************************************80
#
## R8S3_ZEROS zeros an R8S3 matrix.
#
#  Discussion:
#
#    The R8S3 storage format corresponds to the sparse triplet format.
#
#    The R8S3 storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, integer NZ_NUM, the number of nonzero entries.
#
#    Input, integer SYM, is 0 if the matrix is not symmetric, and 1
#    if the matrix is symmetric.  If the matrix is symmetric, then
#    only the nonzeroes on the diagonal and in the lower triangle are stored.
#
#    Input, integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    Output, real A(NZ_NUM), the indicator matrix.
#
  import numpy as np

  a = np.zeros ( nz_num )

  return a

def r8s3_zeros_test ( ):

#*****************************************************************************80
#
## R8S3_ZEROS_TEST tests R8S3_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 4
  nz_num = 11
  row = np.array ( [0,1,2,3,0,1,1,2,3,4,4], dtype = np.int32 )
  col = np.array ( [0,1,2,3,3,0,2,3,1,0,1], dtype = np.int32 )
  sym = 0

  print ( '' )
  print ( 'R8S3_ZEROS_TEST' )
  print ( '  R8S3_ZEROS zeros out space for an R8S3 matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8s3_zeros ( m, n, nz_num, sym, row, col )

  r8s3_print ( m, n, nz_num, sym, row, col, a, '  Matrix A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_ZEROS_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8s3_test ( ):

#*****************************************************************************80
#
## R8S3_TEST tests the R8S3 library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8S3_TEST' )
  print ( '  Python version:' )
  print ( '  Test the R8S3 library.' )

  r8s3_diagonal_test ( )
  r8s3_dif2_test ( )
  r8s3_indicator_test ( )
  r8s3_jac_sl_test ( )
  r8s3_mtv_test ( )
  r8s3_mv_test ( )
  r8s3_print_test ( )
  r8s3_print_some_test ( )
  r8s3_random_test ( )
  r8s3_read_test ( )
  r8s3_res_test ( )
  r8s3_to_r8ge_test ( )
  r8s3_write_test ( )
  r8s3_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8S3_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8s3_test ( )
  timestamp ( )

