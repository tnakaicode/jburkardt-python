#! /usr/bin/env python3
#
def i4_log_10 ( i ):

#*****************************************************************************80
#
## i4_log_10() returns the integer part of the logarithm base 10 of ABS(X).
#
#  Example:
#
#        I  VALUE
#    -----  --------
#        0    0
#        1    0
#        2    0
#        9    0
#       10    1
#       11    1
#       99    1
#      100    2
#      101    2
#      999    2
#     1000    3
#     1001    3
#     9999    3
#    10000    4
#
#  Discussion:
#
#    i4_log_10 ( I ) + 1 is the number of decimal digits in I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose logarithm base 10 is desired.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm base 10 of
#    the absolute value of X.
#
  import numpy as np

  i = np.floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0
    ten_pow = 10

    i_abs = abs ( i )

    while ( ten_pow <= i_abs ):
      value = value + 1
      ten_pow = ten_pow * 10

  return value

def i4_log_10_test ( ) :

#*****************************************************************************80
#
## i4_log_10_test() tests i4_log_10().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ( '' )
  print ( 'i4_log_10_test' )
  print ( '  i4_log_10: whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )

  return

def r8ge_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8ge_print() prints an R8GE matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8ge_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ge_print_test ( ):

#*****************************************************************************80
#
## r8ge_print_test() tests r8ge_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8ge_print_test():' )
  print ( '  r8ge_print() prints an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print ( m, n, v, '  Here is an R8GE:' )

  return

def r8ge_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8ge_print_some() prints out a portion of an R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
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
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8ge_print_some_test ( ):

#*****************************************************************************80
#
## r8ge_print_some_test() tests r8ge_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'r8ge_print_some_test' )
  print ( '  r8ge_print_some prints some of an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print_some ( m, n, v, 0, 3, 2, 5, '  Rows 0:2, Cols 3:5:' )

  return

def r8ncf_print ( m, n, nz_num, rowcol, a, title ):

#*****************************************************************************80
#
## r8ncf_print() prints a R8NCF matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROWCOL(2,NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    string TITLE, a title.
#
  r8ncf_print_some ( m, n, nz_num, rowcol, a, 0, 0, m - 1, n - 1, title )

  return

def r8ncf_print_some ( m, n, nz_num, rowcol, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8ncf_print_some() prints some of a R8NCF matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROWCOL(2,NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
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

        if ( i == rowcol[0,k] and j2lo <= rowcol[1,k] and rowcol[1,k] <= j2hi ):

          j2 = rowcol[1,k] - j2lo + 1

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

def r8st_cg ( n, nz_num, row, col, a, b, x_init ):

#*****************************************************************************80
#
## r8st_cg() uses the conjugate gradient method on an r8st system.
#
#  Discussion:
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.
#
#    It is possible that a pair of indices (I,J) may occur more than
#    once.  Presumably, in this case, the intent is that the actual value
#    of A(I,J) is the sum of all such entries.  This is not a good thing
#    to do, but I seem to have come across this in MATLAB.
#
#    The r8st format is used by CSPARSE ("sparse triplet"), SLAP 
#    ("nonsymmetric SLAP triad"), by MATLAB, and by SPARSEKIT ("COO" format).
#
#    The matrix A must be a positive definite symmetric matrix.
#
#    The method is designed to reach the solution after N computational
#    steps.  However, roundoff may introduce unacceptably large errors for
#    some problems.  In such a case, calling the routine again, using
#    the computed solution as the new starting estimate, should improve
#    the results.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Frank Beckman,
#    The Solution of Linear Equations by the Conjugate Gradient Method,
#    in Mathematical Methods for Digital Computers,
#    edited by John Ralston, Herbert Wilf,
#    Wiley, 1967,
#    ISBN: 0471706892,
#    LC: QA76.5.R3.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    real B(N), the right hand side vector.
#
#    real X_INIT(N), an estimate for the solution, which may be 0.
#
#  Output:
#
#    real X(N), the approximate solution vector.
#
  import numpy as np

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = x_init[i]
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
  ap = r8st_mv ( n, n, nz_num, row, col, a, x )

  r = np.zeros ( n )
  for i in range ( 0, n ):
    r[i] = b[i] - ap[i]

  p = np.zeros ( n )
  for i in range ( 0, n ):
    p[i] = b[i] - ap[i]
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP=A*P.
#
    ap = r8st_mv ( n, n, nz_num, row, col, a, p )
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
    pap = np.dot ( p, ap )
    pr = np.dot ( p, r )

    if ( pap == 0.0 ):
      return x

    alpha = pr / pap
#
#  Set
#    X = X + ALPHA * P
#    R = R - ALPHA * AP.
#
    for i in range ( 0, n ):
      x[i] = x[i] + alpha * p[i]

    for i in range ( 0, n ):
      r[i] = r[i] - alpha * ap[i]
#
#  Compute the vector dot product
#    RAP = R*AP
#  Set
#    BETA = - RAP / PAP.
#
    rap = np.dot ( r, ap )

    beta = - rap / pap
#
#  Update the perturbation vector
#    P = R + BETA * P.
#
    for i in range ( 0, n ):
      p[i] = r[i] + beta * p[i]

  return x

def r8st_cg_test ( rng ):

#*****************************************************************************80
#
## r8st_cg_test() tests r8st_cg().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 July 2015
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
 
  print ( '' )
  print ( 'r8st_cg_test():' )
  print ( '  r8st_cg() applies CG to an r8st matrix.' )

  n = 10
  nz_num = 3 * n - 2
#
#  Set A to the [-1 2 -1] matrix.
#
  row, col, a = r8st_dif2 ( n, n, nz_num )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r8st_mv ( n, n, nz_num, row, col, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r8st_cg ( n, nz_num, row, col, a, b, x2 )
#
#  Compute the residual.
#
  r = r8st_res ( n, n, nz_num, row, col, a, x3, b )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = %d' % ( n ) )
  print ( '  Norm of residual ||Ax-b|| = %g' % ( r_norm ) )
  print ( '  Norm of error ||x1-x2|| = %g' % ( e_norm ) )

  return

def r8st_check ( m, n, nz_num, row, col ):

#*****************************************************************************80
#
## r8st_check() checks that a r8st matrix data structure is properly sorted.
#
#  Discussion:
#
#    This routine assumes that the data structure has been sorted,
#    so that the entries of ROW are ascending sorted, and that the
#    entries of COL are ascending sorted, within the group of entries
#    that have a common value of ROW.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.
#
#    The r8st format is used by CSPARSE ("sparse triplet"), SLAP
#    ("nonsymmetric SLAP triad"), by MATLAB, and by SPARSEKIT ("COO" format).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of
#    the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and
#    column indices of the nonzero elements.
#
#  Output:
#
#    bool CHECK, is TRUE if the matrix is properly defined.
#
  check = True
#
#  Check 1 <= ROW(*) <= M.
#
  for k in range ( 0, nz_num ):

    if ( row[k] < 0 or m <= row[k] ):
      check = False
      return check
#
#  Check 1 <= COL(*) <= N.
#
  for k in range ( 0, nz_num ):

    if ( col[k] < 0 or n <= col[k] ):
      check = False
      return check
#
#  Check that ROW(K) <= ROW(K+1).
#
  for k in range ( 0, nz_num - 1 ):

    if ( row[k+1] < row[k] ):
      check = False
      return check
#
#  Check that, if ROW(K) == ROW(K+1), that COL(K) < COL(K+1).
#
  for k in range ( 0, nz_num - 1 ):

    if ( row[k] == row[k+1] ):
      if ( col[k+1] <= col[k] ):
        check = False
        return check

  return check

def r8st_diagonal ( m, n, nz_num, row, col, a ):

#*****************************************************************************80
#
## r8st_diagonal() reorders an r8st matrix so diagonal entries are first.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    This routine reorders the entries of A so that the first N entries
#    are exactly the diagonal entries of the matrix, in order.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements 
#    of the matrix.
#
#  Output:
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the updated row and 
#    column indices of the nonzero elements.
#
#    real A(NZ_NUM), the updated nonzero elements 
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
    print ( 'r8st_diagonal - Warning!' )
    print ( '  Number of diagonal entries expected was %d' % ( min ( m, n ) ) )
    print ( '  Number found was %d' % ( found ) )

  return row, col, a

def r8st_diagonal_test ( ):

#*****************************************************************************80
#
## r8st_diagonal_test() tests r8st_diagonal().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
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
  print ( 'r8st_diagonal_test' )
  print ( '  r8st_diagonal rearranges an r8st matrix' )
  print ( '  so that the diagonal is listed first.' )

  m = 6
  n = 6

  print ( '' )
  print ( '  Matrix order M =         %d' % ( m ) )
  print ( '  Matrix order N =         %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  a = r8st_indicator ( m, n, nz_num, row, col )

  print ( '' )
  print ( '  Before rearrangement:' )
  print ( '         K    ROW(K)    COL(K)      A(K)' )
  print ( '' )
  for k in range ( 0, nz_num ):
    print ( '  %8d  %8d  %8d  %14.6g' % ( k, row[k], col[k], a[k] ) )

  row, col, a = r8st_diagonal ( m, n, nz_num, row, col, a )

  print ( '' )
  print ( '  After rearrangement:' )
  print ( '         K    ROW(K)    COL(K)      A(K)' )
  print ( '' )
  for k in range ( 0, nz_num ):
    print ( '  %8d  %8d  %8d  %14.6g' % ( k, row[k], col[k], a[k] ) )

  return

def r8st_dif2 ( m, n, nz_num ):

#*****************************************************************************80
#
## r8st_dif2() returns the DIF2 matrix in r8st format.
#
#  Example:
#
#    N = 5
#
#    2 -1  .  .  .
#   -1  2 -1  .  .
#    . -1  2 -1  .
#    .  . -1  2 -1
#    .  .  . -1  2
#
#  Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is a special case of the TRIS or tridiagonal scalar matrix.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is positive definite.
#
#    A is an M matrix.
#
#    A is weakly diagonally dominant, but not strictly diagonally dominant.
#
#    A has an LU factorization A = L * U, without pivoting.
#
#      The matrix L is lower bidiagonal with subdiagonal elements:
#
#        L(I+1,I) = -I/(I+1)
#
#      The matrix U is upper bidiagonal, with diagonal elements
#
#        U(I,I) = (I+1)/I
#
#      and superdiagonal elements which are all -1.
#
#    A has a Cholesky factorization A = L * L', with L lower bidiagonal.
#
#      L(I,I) =    sqrt ( (I+1) / I )
#      L(I,I-1) = -sqrt ( (I-1) / I )
#
#    The eigenvalues are
#
#      LAMBDA(I) = 2 + 2 * COS(I*PI/(N+1))
#                = 4 SIN^2(I*PI/(2*N+2))
#
#    The corresponding eigenvector X(I) has entries
#
#       X(I)(J) = sqrt(2/(N+1)) * sin ( I*J*PI/(N+1) ).
#
#    Simple linear systems:
#
#      x = (1,1,1,...,1,1),   A*x=(1,0,0,...,0,1)
#
#      x = (1,2,3,...,n-1,n), A*x=(0,0,0,...,0,n+1)
#
#    det ( A ) = N + 1.
#
#    The value of the determinant can be seen by induction,
#    and expanding the determinant across the first row:
#
#      det ( A(N) ) = 2 * det ( A(N-1) ) - (-1) * (-1) * det ( A(N-2) )
#                = 2 * N - (N-1)
#                = N + 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969,
#    ISBN: 0882756494,
#    LC: QA263.68
#
#    Morris Newman, John Todd,
#    Example A8,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    John Todd,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Birkhauser, 1980,
#    ISBN: 0817608117,
#    LC: QA297.T58.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#  Output:
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
  import numpy as np

  row = np.zeros ( nz_num, dtype = np.int32 )
  col = np.zeros ( nz_num, dtype = np.int32 )
  a = np.zeros ( nz_num, dtype = np.float64 )

  k = 0
  for i in range ( 0, m ):

    j = i - 1
    if ( 0 <= j and j < n ):
      row[k] = i
      col[k] = j
      a[k] = -1.0
      k = k + 1

    j = i
    if ( 0 <= j and j < n ):
      row[k] = i
      col[k] = j
      a[k] = 2.0
      k = k + 1

    j = i + 1
    if ( 0 <= j and j < n ):
      row[k] = i
      col[k] = j
      a[k] = -1.0
      k = k + 1

  return row, col, a

def r8st_dif2_test ( ):

#*****************************************************************************80
#
## r8st_dif2_test() tests r8st_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
  print ( 'r8st_dif2_test()' )
  print ( '  r8st_dif2() sets an r8st matrix to the second difference.' )

  m = 5
  n = 5
  nz_num = 3 * n - 2

  row, col, a = r8st_dif2 ( m, n, nz_num )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  r8st_print ( m, n, nz_num, row, col, a, '  r8st matrix A:' )

  return

def r8st_ij_to_k ( nz_num, row, col, i, j ):

#*****************************************************************************80
#
## r8st_ij_to_k() seeks the compressed index of the (I,J) entry of A.
#
#  Discussion:
#
#    If A(I,J) is nonzero, then its value is stored in location K.
#
#    This routine searches the r8st storage structure for the index K
#    corresponding to (I,J), returning -1 if no such entry was found.
#
#    This routine assumes that the data structure has been sorted,
#    so that the entries of ROW are ascending sorted, and that the
#    entries of COL are ascending sorted, within the group of entries
#    that have a common value of ROW.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.
#
#    The r8st format is used by CSPARSE ("sparse triplet"), SLAP
#    ("nonsymmetric SLAP triad"), by MATLAB, and by SPARSEKIT ("COO" format).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and
#    column indices of the nonzero elements.
#
#    integer I, J, the row and column indices of the
#    matrix entry.
#
#  Output:
#
#    integer K, the r8st index of the (I,J) entry.
#
  lo = 0
  hi = nz_num - 1

  while ( True ):

    if ( hi < lo ):
      k = -1
      break

    md = ( ( lo + hi ) // 2 )

    if ( row[md] < i or ( row[md] == i and col[md] < j ) ):
      lo = md + 1
    elif ( i < row[md] or ( row[md] == i and j < col[md] ) ):
      hi = md - 1
    else:
      k = md
      break

  return k

def r8st_ij_to_k_test ( ):

#*****************************************************************************80
#
## r8st_ij_to_k_test() tests r8st_ij_to_k().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 7
  n = 5
  nz_num = 10
  row = np.array ( [ 0, 0, 1, 1, 3, 3, 3, 4, 5, 6 ] )
  col = np.array ( [ 1, 4, 0, 4, 0, 1, 2, 3, 3, 0 ] )

  print ( '' )
  print ( 'r8st_ij_to_k_test()' )
  print ( '  r8st_ij_to_k() returns the r8st index of (I,J).' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )
  print ( '  Matrix nonzeros =  %d' % ( nz_num ) )

  check = r8st_check ( m, n, nz_num, row, col )

  if ( not check ):
    print ( '' )
    print ( 'r8st_check(): Warning!' )
    print ( '  The matrix is not in the proper sorted format.' )
    return

  print ( '' )
  print ( '         I         J         K' )
  print ( '' )
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = r8st_ij_to_k ( nz_num, row, col, i, j )
      print ( '  %8d  %8d  %8d' % ( i, j, k ) )

  return

def r8st_indicator ( m, n, nz_num, row, col ):

#*****************************************************************************80
#
## r8st_indicator() sets up a r8st indicator matrix.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#  Output:
#
#    real A(NZ_NUM), the indicator matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( nz_num, dtype = np.float64 )

  for k in range ( 0, nz_num ):
    i = row[k]
    j = col[k]
    a[k] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8st_indicator_test ( ):

#*****************************************************************************80
#
## r8st_indicator_test() tests r8st_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
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

  print ( '' )
  print ( 'r8st_indicator_test' )
  print ( '  r8st_indicator sets an r8st indicator matrix.' )
  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  a = r8st_indicator ( m, n, nz_num, row, col )

  r8st_print ( m, n, nz_num, row, col, a, '  Matrix A:' )

  return

def r8st_jac_sl ( n, nz_num, row, col, a, b, x, it_max ):

#*****************************************************************************80
#
## r8st_jac_sl() solves an r8st system using Jacobi iteration.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    This routine REQUIRES that the matrix be square, that the matrix
#    have nonzero diagonal entries, and that the first N entries of
#    the array A be exactly the diagonal entries of the matrix, in order.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column 
#    indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    real B(N), the right hand side of the linear system.
#
#    real X(N), an approximate solution 
#    to the system.
#
#    integer IT_MAX, the maximum number of iterations.
#
#  Output:
#
#    real X(N), an improved approximate solution 
#    to the system.
#
  import numpy as np

  x_new = np.zeros ( n )
#
#  Ensure that the matrix lists diagonal entries first.
#
  row, col, a = r8st_diagonal ( n, n, nz_num, row, col, a )

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
#
#  Update.
#
    for i in range ( 0, n ):
      x[i] = x_new[i] / a[i]

  return x

def r8st_jac_sl_test ( ):

#*****************************************************************************80
#
## r8st_jac_sl_test() tests r8st_jac_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8st_jac_sl_test()' )
  print ( '  r8st_jac_sl() uses Jacobi iteration to solve a linear system' )
  print ( '  with an r8st matrix.' )

  m = 10
  n = 10
  nz_num = 3 * n - 2
  it_max = 25

  print ( '' )
  print ( '  Matrix order M =         %8d' % ( m ) )
  print ( '  Matrix order N =         %8d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %8d' % ( nz_num ) )
  print ( '  Iterations per         = %8d' % ( it_max ) )
#
#  Set the matrix values.
#
  row, col, a = r8st_dif2 ( m, n, nz_num )

  print ( '' )
  print ( '  Solving A * x = b.' )
  print ( '' )

  title = 'Matrix A:'
  r8st_print ( m, n, nz_num, row, col, a, title )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
  print ( 'Solution x:' )
  print ( x )
#
#  Compute the corresponding right hand side.
#
  b = r8st_mv ( n, n, nz_num, row, col, a, x )
  print ( 'Right hand size b:' )
  print ( b )
#
#  Set the starting solution.
#
  x = np.zeros ( n )
#
#  Solve the linear system.
#
  for i in range ( 0, 3 ):

    x = r8st_jac_sl ( n, nz_num, row, col, a, b, x, it_max )

    r8vec_print ( n, x, '  Current solution estimate:' )

  return

def r8st_mtv ( m, n, nz_num, row, col, a, x ):

#*****************************************************************************80
#
## r8st_mtv() multiplies an R8VEC times an r8st matrix.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column
#    indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    real X(M), the vector to be multiplied by A'.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for k in range ( 0, nz_num ):
    i = col[k]
    j = row[k]
    b[i] = b[i] + a[k] * x[j]

  return b

def r8st_mtv_test ( ):

#*****************************************************************************80
#
## r8st_mtv_test() tests r8st_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8st_mtv_test' )
  print ( '  r8st_mtv computes b=A\'*x, where A is an r8st matrix.' )

  m = 5
  n = 4
  if ( m == n ):
    nz_num = 3 * n - 2
  else:
    nz_num = 3 * n - 1

  row, col, a = r8st_dif2 ( m, n, nz_num )

  print ( '' )
  print ( '  Matrix order M =         %d' % ( m ) )
  print ( '  Matrix order N =         %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  x:' )

  b = r8st_mtv ( m, n, nz_num, row, col, a, x )

  r8vec_print ( n, b, '  b=A\'*x:' )

  return

def r8st_mv ( m, n, nz_num, row, col, a, x ):

#*****************************************************************************80
#
## r8st_mv() multiplies an r8st matrix by an R8VEC.
#
#  Discussion:
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.
#
#    It is possible that a pair of indices (I,J) may occur more than
#    once.  Presumably, in this case, the intent is that the actual value
#    of A(I,J) is the sum of all such entries.  This is not a good thing
#    to do, but I seem to have come across this in MATLAB.
#
#    The r8st format is used by CSPARSE ("sparse triplet"), DLAP/SLAP 
#    ("nonsymmetric SLAP triad"), by MATLAB, and by SPARSEKIT ("COO" format).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of 
#    the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product vector A*X.
#
  import numpy as np

  b = np.zeros ( m, dtype = np.float64 )

  for k in range ( 0, nz_num ):

    i = row[k]
    j = col[k]
    b[i] = b[i] + a[k] * x[j]

  return b

def r8st_mv_test ( ):

#*****************************************************************************80
#
## r8st_mv_test() tests r8st_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8st_mv_test' )
  print ( '  r8st_mv computes b=A*x, where A is an r8st matrix.' )

  m = 5
  n = 4
  if ( m == n ):
    nz_num = 3 * n - 2
  else:
    nz_num = 3 * n - 1

  row, col, a = r8st_dif2 ( m, n, nz_num )

  print ( '' )
  print ( '  Matrix order M =         %d' % ( m ) )
  print ( '  Matrix order N =         %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )

  b = r8st_mv ( m, n, nz_num, row, col, a, x )

  r8vec_print ( m, b, '  b=A*x:' )

  return

def r8st_print ( m, n, nz_num, row, col, a, title ):

#*****************************************************************************80
#
## r8st_print() prints a r8st matrix.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    string TITLE, a title.
#
  r8st_print_some ( m, n, nz_num, row, col, a, 0, 0, m - 1, n - 1, title )

  return

def r8st_print_test ( ):

#*****************************************************************************80
#
## r8st_print_test() tests r8st_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8st_print_test' )
  print ( '  r8st_print prints an r8st matrix.' )

  m = 5
  n = 5
  nz_num = 3 * n - 2

  row, col, a = r8st_dif2 ( m, n, nz_num )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  r8st_print ( m, n, nz_num, row, col, a, '  r8st matrix A:' )

  return

def r8st_print_some ( m, n, nz_num, row, col, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8st_print_some() prints some of an r8st matrix.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M,  N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROW[NZ_NUM], COL[NZ_NUM], the row and column indices
#    of the nonzero elements.
#
#    real A[NZ_NUM], the nonzero elements 
#    of the matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
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

def r8st_print_some_test ( ):

#*****************************************************************************80
#
## r8st_print_some_test() tests r8st_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8st_print_some_test' )
  print ( '  r8st_print_some prints some of an r8st matrix.' )

  m = 5
  n = 5
  nz_num = 3 * n - 2

  row, col, a = r8st_dif2 ( m, n, nz_num )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  r8st_print_some ( m, n, nz_num, row, col, a, 2, 3, 4, 5, '  Rows 2:4, Cols 3:5:' )

  return

def r8st_random ( m, n, nz_num, row, col, rng ):

#*****************************************************************************80
#
## r8st_random() randomizes an r8st matrix.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(NZ_NUM), the indicator matrix.
#
  import numpy as np
 
  a = np.zeros ( nz_num, dtype = np.float64 )

  for k in range ( 0, nz_num ):
    i = row[k]
    j = col[k]
    a[k] = rng.random ( )

  return a

def r8st_random_test ( rng ):

#*****************************************************************************80
#
## r8st_random_test() tests r8st_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
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

  m = 6
  n = 6
  nz_num = 20
  row = np.array ( [0,2,3,5,4,1,5,2,0,1,3,5,4,3,3,2,5,1,2,3], dtype = np.int32 )
  col = np.array ( [4,5,1,1,2,3,3,4,0,5,3,5,4,0,5,2,0,1,0,2], dtype = np.int32 )

  print ( '' )
  print ( 'r8st_random_test()' )
  print ( '  r8st_random() randomizes an r8st indicator matrix.' )
  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  a = r8st_random ( m, n, nz_num, row, col, rng )

  r8st_print ( m, n, nz_num, row, col, a, '  Matrix A:' )

  return

def r8st_read ( input_file, m, n, nz_num ):

#*****************************************************************************80
#
## r8st_read() reads an r8st matrix from a file.
#
#  Discussion:
#
#    This routine needs the value of NZ_NUM, which can be determined
#    by a call to r8st_read_size.
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string INPUT_FILE, the name of the file to be read.
#
#    Unused, integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#  Output:
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements 
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

def r8st_read_size ( input_file ):

#*****************************************************************************80
#
## r8st_read_size() reads the size of an r8st matrix from a file.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string INPUT_FILE, the name of the file to be read.
#
#  Output:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in 
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

def r8st_read_test ( ):

#*****************************************************************************80
#
## r8st_read_test() tests r8st_read().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8st_read_test' )
  print ( '  r8st_read_size reads the size of an r8st matrix.' )
  print ( '  r8st_read reads the r8st matrix from a file.' )

  input_file = 'r8st_matrix.txt'

  m, n, nz_num = r8st_read_size ( input_file )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  row, col, a = r8st_read ( input_file, m, n, nz_num )

  r8st_print_some ( m, n, nz_num, row, col, a, 1, 1, \
    10, 10, '  Initial 10x10 block of recovered r8st matrix:' )

  return

def r8st_res ( m, n, nz_num, row, col, a, x, b ):

#*****************************************************************************80
#
## r8st_res() computes the residual R = B-A*X for r8st matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and 
#    column indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#    real B(M), the desired result A * x.
#
#  Output:
#
#    real R(M), the residual R = B - A * X.
#
  r = r8st_mv ( m, n, nz_num, row, col, a, x )

  for i in range ( 0, m ):
    r[i] = b[i] - r[i]

  return r

def r8st_res_test ( ):

#*****************************************************************************80
#
## r8st_res_test() tests r8st_res().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8st_res_test' )
  print ( '  r8st_res computes r=b-A*x, where A is an r8st matrix.' )

  m = 5
  n = 4
  if ( m == n ):
    nz_num = 3 * n - 2
  else:
    nz_num = 3 * n - 1

  row, col, a = r8st_dif2 ( m, n, nz_num )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )

  b = r8st_mv ( m, n, nz_num, row, col, a, x )

  r = r8st_res ( m, n, nz_num, row, col, a, x, b )

  r8vec_print ( m, r, '  r=b-A*x:' )

  return

def r8st_to_r8ge ( m, n, nz_num, row, col, a_r8st ):

#*****************************************************************************80
#
## r8st_to_r8ge() copies an r8st matrix to an R8GE matrix.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional bool
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column
#    indices of the nonzero elements.
#
#    real A_r8st(NZ_NUM), the nonzero elements of the matrix.
#
#  Output:
#
#    real A_r8ge(M,N), the R8GE matrix.
#
  import numpy as np

  a_r8ge = np.zeros ( [ m, n ] )

  for k in range ( 0, nz_num ):
    i = row[k]
    j = col[k]
    a_r8ge[i,j] = a_r8ge[i,j] + a_r8st[k]

  return a_r8ge

def r8st_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8st_to_r8ge_test() tests r8st_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8st_to_r8ge_test' )
  print ( '  r8st_to_r8ge converts an r8st matrix to R8GE format.' )

  m = 5
  n = 5
  nz_num = 3 * n - 2

  row, col, a_r8st = r8st_dif2 ( m, n, nz_num )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  r8st_print ( m, n, nz_num, row, col, a_r8st, '  r8st matrix A:' )

  a_r8ge = r8st_to_r8ge ( m, n, nz_num, row, col, a_r8st )

  r8ge_print ( m, n, a_r8ge, '  R8GE matrix A:' )

  return

def r8st_to_r8ncf ( m, n, nz_num, row, col, a_r8st ):

#*****************************************************************************80
#
## r8st_to_r8ncf() copies an r8st matrix to an R8NCF matrix.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column
#    indices of the nonzero elements.
#
#    real A_r8st(NZ_NUM), the nonzero elements of the matrix.
#
#  Output:
#
#    integer NZ_NUM, the number of nonzero elements in the DNCF matrix.
#
#    integer ROWCOL(2,NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    real A_r8ncf(M,N), the R8NCF matrix.
#
  import numpy as np

  rowcol = np.zeros ( [ 2, nz_num ], dtype = np.int32 )
  a_r8ncf = np.zeros ( nz_num )

  for k in range ( 0, nz_num ):
    rowcol[0,k] = row[k]
    rowcol[1,k] = col[k]
    a_r8ncf[k] = a_r8st[k]

  return nz_num, rowcol, a_r8ncf

def r8st_to_r8ncf_test ( ):

#*****************************************************************************80
#
## r8st_to_r8ncf_test() tests r8st_to_r8ncf().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8st_to_r8ncf_test' )
  print ( '  r8st_to_r8ncf converts an r8st matrix to R8NCF format.' )

  m = 5
  n = 5
  nz_num = 3 * n - 2

  row, col, a_r8st = r8st_dif2 ( m, n, nz_num )

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )

  r8st_print ( m, n, nz_num, row, col, a_r8st, '  r8st matrix A:' )

  nz_num, rowcol, a_r8ncf = r8st_to_r8ncf ( m, n, nz_num, row, col, a_r8st )

  r8ncf_print ( m, n, nz_num, rowcol, a_r8ncf, '  R8NCF matrix A:' )

  return

def r8st_write ( m, n, nz_num, row, col, a, output_file ):

#*****************************************************************************80
#
## r8st_write() writes an r8st matrix to a file.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 September 2006
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column 
#    indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements 
#    of the matrix.
#
#    string OUTPUT_FILE, the name of the file to which
#    the information is to be written.
#
  output_unit = open ( output_file, 'w' )

  for k in range ( 0, nz_num ):
    s = '%d  %d  %g\n' % ( row[k], col[k], a[k] )
    output_unit.write ( s )

  output_unit.close ( )

  return

def r8st_write_test ( ):

#*****************************************************************************80
#
## r8st_write_test() tests r8st_write().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8st_write_test' )
  print ( '  r8st_write writes an r8st matrix to a file.' )

  m = 100
  n = 100
  nz_num = 3 * n - 2

  print ( '' )
  print ( '  Matrix order M         = %d' % ( m ) )
  print ( '  Matrix order N         = %d' % ( n ) )
  print ( '  Matrix nonzeros NZ_NUM = %d' % ( nz_num ) )
#
#  Set the matrix values.
#
  row, col, a = r8st_dif2 ( m, n, nz_num )
#
#  Print a bit of the matrix.
#
  r8st_print_some ( m, n, nz_num, row, col, a, 1, 1, \
    10, 10, '  Initial 10x10 block of r8st matrix:' )
#
#  Write the matrix to a file.
#
  output_file = 'r8st_matrix.txt'

  r8st_write ( m, n, nz_num, row, col, a, output_file )

  print ( '' )
  print ( '  Matrix data written to "%s".' % ( output_file ) )

  return

def r8st_zeros ( m, n, nz_num, row, col ):

#*****************************************************************************80
#
## r8st_zeros() zeros an r8st matrix.
#
#  Discussion:
#
#    The r8st storage format corresponds to the SLAP Triad format.
#
#    The r8st storage format stores the row, column and value of each nonzero
#    entry of a sparse matrix.  The entries may be given in any order.  No
#    check is made for the erroneous case in which a given matrix entry is
#    specified more than once.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer ROW(NZ_NUM), COL(NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#  Output:
#
#    real A(NZ_NUM), the indicator matrix.
#
  import numpy as np

  a = np.zeros ( nz_num )

  return a

def r8st_zeros_test ( ):

#*****************************************************************************80
#
## r8st_zeros_test() tests r8st_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 September 2015
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

  print ( '' )
  print ( 'r8st_zeros_test' )
  print ( '  r8st_zeros zeros out space for an r8st matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8st_zeros ( m, n, nz_num, row, col )

  r8st_print ( m, n, nz_num, row, col, a, '  Matrix A:' )

  return

def r8st_test ( ):

#*****************************************************************************80
#
## r8st_test() tests r8st().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8st_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8st().' )

  rng = default_rng ( )

  r8st_cg_test ( rng )
  r8st_diagonal_test ( )
  r8st_dif2_test ( )
  r8st_ij_to_k_test ( )
  r8st_indicator_test ( )
  r8st_jac_sl_test ( )
  r8st_mtv_test ( )
  r8st_mv_test ( )
  r8st_print_test ( )
  r8st_print_some_test ( )
  r8st_random_test ( rng )
  r8st_read_test ( )
  r8st_res_test ( )
  r8st_to_r8ge_test ( )
  r8st_to_r8ncf_test ( )
  r8st_write_test ( )
  r8st_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8st_test():' )
  print ( '  Normal end of execution.' )
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
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## r8vec_indicator1_test() tests r8vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_indicator1_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_indicator1 returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

  return

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
  r8st_test ( )
  timestamp ( )
 
