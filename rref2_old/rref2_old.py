#! /usr/bin/env python3
#
def rref2_test ( ):

#*****************************************************************************80
#
## rref2_test() tests rref2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rref2_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test rref(), which analyzes matrices using the' )
  print ( '  reduced row echelon form (RREF)' )

  is_rref_test ( )
  rref_columns_test ( )
  rref_compute_test ( )
  rref_determinant_test ( )
  rref_inverse_test ( )
  rref_rank_test ( )
  rref_solve_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'rref2_test():' )
  print ( '  Normal end of execution.' )

  return

def is_rref_test ( ):

#*****************************************************************************80
#
## is_rref_test() tests is_rref().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'is_rref_test():' )
  print ( '  is_rref() reports whether a matrix is in reduced row echelon format.' )
#
#  Zero rows must come last.
#
  A0 = np.array ( [    \
    [ 1, 0, 0, 9, 4 ], \
    [ 0, 0, 1, 0, 8 ], \
    [ 0, 0, 0, 0, 0 ], \
    [ 0, 0, 0, 1, 0 ]  \
  ] )
#
#  First nonzero must be to right of first nonzero in previous row.
#
  A1 = np.array ( [    \
    [ 1, 0, 0, 9, 4 ], \
    [ 0, 0, 0, 1, 0 ], \
    [ 0, 0, 1, 0, 8 ], \
    [ 0, 0, 0, 0, 0 ] \
  ] )
#
#  First nonzero must be a 1.
#
  A2 = np.array ( [    \
    [ 1, 0, 0, 9, 4 ], \
    [ 0, 1, 0, 2, 8 ], \
    [ 0, 0, 3, 0, 0 ], \
    [ 0, 0, 0, 0, 0 ] \
  ] )
#
#  First nonzero must only nonzero in its column.
#
  A3 = np.array ( [    \
    [ 1, 0, 3, 9, 4 ], \
    [ 0, 1, 0, 2, 8 ], \
    [ 0, 0, 1, 0, 0 ], \
    [ 0, 0, 0, 0, 0 ] \
  ] )
#
#  RREF example.
#
  A4 = np.array ( [    \
    [ 1, 0, 3, 0, 4 ], \
    [ 0, 1, 2, 0, 8 ], \
    [ 0, 0, 0, 1, 0 ], \
    [ 0, 0, 0, 0, 0 ] \
  ] )

  for A, A_name in [ [ A0, 'A0' ], [ A1, 'A1' ], [ A2, 'A2' ], [ A3, 'A3' ], [ A4, 'A4' ] ]:
    print ( '' )
    print ( '  ' + A_name + ':' )
    print ( A )
    print ( '  is_rref(' + A_name + ') = ', is_rref ( A ) )

  return

def is_rref ( A ):

#*****************************************************************************80
#
## is_rref() determines if a matrix is in reduced row echelon format.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    A[m,n]: a numpy array defining a matrix.
#
#  Output:
#
#    is_ref: True if A is in reduced row echelon form.
#
  m, n = A.shape

  c = -1

  for r in range ( 0, m ):
#
#  Increment the first legal column for next pivot.
#
    c = c + 1
#
#  Search for pivot p in this row.
#  If none, set p = n.
#
    p = n
    for j in range ( 0, n ):
      if ( A[r,j] != 0.0 ):
        p = j
        break
#
#  If p == n, go to next row.
#
    if ( p == n ):
      continue
#
#  If p is too early, fail.
#
    if ( p < c ):
      return False
#
#  Accept p as new c.
#
    c = p
#
#  If A(r,c) is not 1, fail
#
    if ( A[r,c] != 1.0 ):
      return False
#
#  If A(r,c) is not the only nonzero in column c, fail
#
    for i in range ( 0, m ):
      if ( i != r ):
        if ( A[i,c] != 0.0 ):
          return False

  return True

def rref_columns ( A ):

#*****************************************************************************80
#
## rref_columns() uses reduced row echelon form (RREF) for column independence.
#
#  Discussion:
#
#    The RREF process will identify columns that are linear combinations of
#    previous columns.
#
#    This function will return a matrix containing only the linearly
#    independent columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), the matrix to be analyzed.
#
#  Output:
#
#    real A_COLUMNS(M,N2), a matrix whose N2 columns are the linearly
#    independent columns of A.
#
  import numpy as np

  A_REF, a_cols = rref_compute ( A )

  A_COLUMNS = A[:,a_cols]

  return A_COLUMNS

def rref_columns_test ( ):

#*****************************************************************************80
#
## rref_columns_test() tests rref_columns().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rref_columns_test():' )
  print ( '  rref_columns() uses the reduced row echelon form (RREF)' )
  print ( '  of a matrix to find the linearly independent columns.' )

  m = 7
  n = 4

  A = np.array ( [ \
        [ 1,  2, 3, 1 ], \
        [ 2,  4, 9, 3 ], \
        [ 3,  6, 0, 0 ], \
        [ 4,  8, 0, 2 ], \
        [ 5, 10, 6, 6 ], \
        [ 6, 12, 6, 3 ], \
        [ 7, 14, 2, 1 ] ] )

  print ( '' )
  print ( '  Matrix A:' )
  print ( A )

  A_COLUMNS = rref_columns ( A )
  m, n2 = A_COLUMNS.shape
  print ( '' )
  print ( '  Number of independent columns is ', n2 )
  print ( '' )
  print ( '  Independent columns of A:' )
  print ( A_COLUMNS )

  return

def rref_compute ( A ):

#*****************************************************************************80
#
## rref_compute() computes the reduced row echelon form of a matrix.
#
#  Discussion:
#
#    A rectangular matrix is in row reduced echelon form if:
#
#    * The leading nonzero entry in each row has the value 1.
#
#    * All entries are zero above and below the leading nonzero entry 
#      in each row.
#
#    * The leading nonzero in each row occurs in a column to
#      the right of the leading nonzero in the previous row.
#
#    * Rows which are entirely zero occur last.
#
#  Example:
#
#    M = 4, N = 7
#
#    Matrix A:
#
#     1    3    0    2    6    3    1
#    -2   -6    0   -2   -8    3    1
#     3    9    0    0    6    6    2
#    -1   -3    0    1    0    9    3
#
#    RREF(A):
#
#     1    3    0    0    2    0    0
#     0    0    0    1    2    0    0
#     0    0    0    0    0    1   1/3
#     0    0    0    0    0    0    0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Cullen,
#    An Introduction to Numerical Linear Algebra,
#    PWS Publishing Company, 1994,
#    ISBN: 978-0534936903,
#    LC: QA185.D37.C85.
#
#  Input:
#
#    real A(M,N), the matrix to be analyzed. 
#
#  Output:
#
#    real B(M,N), the reduced row echelon form of the matrix.
#
#    integer a_cols(*): the columns for which a pivot entry was found.
#
  import numpy as np

  B = A.copy ( )
#
#  Ensure the matrix elements are floating-point for division.
#
  B = B.astype ( float )

  m, n = B.shape
#
#  Initialize rank to 0.
#
  a_cols = np.zeros ( 0, dtype = int )
#
#  Search for a pivot for each column, starting with column C = 0.
#
  c = 0
#
#  Start the search for a pivot in row R = 0.
#
  r = 0

  tol = np.sqrt ( np.finfo(float).eps )

  while ( True ):
#
#  Find row index P of maximum element in subvector A(R:M,C).
#
    pval = np.max ( np.abs ( B[r:m,c] ) )
    p = np.argmax ( np.abs ( B[r:m,c] ) )
#
#  Adjust value of P as an entry in full vector A(0:M,C).
#
    p = p + r
#
#  If A(r:m,c) was all zero, there is no pivot for this column.
#  Here, we use a tolerance TOL instead of checking for an exact zero.
#
    if ( np.abs ( pval ) <= tol ):

      B[p,c] = 0
#
#  Increment the column index for the next search.
#
      c = c + 1
#
#  If there are no more columns to search, terminate the algorithm.
#
      if ( n <= c ):
        break
#
#  Restart loop with the next column index.
#
      continue
#
#  A pivot was found.  Increase rank by 1.
#
    a_cols = np.append ( a_cols, c )
#
#  Swap rows R and P.
#  This ASININE failure to copy when using "=" is murderous.
#
    temp     = B[r,c:n].copy( )
    B[r,c:n] = B[p,c:n].copy ( )
    B[p,c:n] = temp.copy ( )
#
#  Normalize row R so that A(r,c) = 1.
#
    B[r,c:n] = B[r,c:n] / B[r,c]
    B[r,c] = 1.0
#
#  Eliminate nonzeros in column C using multiples of row R, except for A(R,C).
#
    for i in range ( 0, m ):
      if ( i != r ):
        B[i,c:n] = B[i,c:n] - B[i,c] * B[r,c:n]
        B[i,c] = 0.0
#
#  Increment C, but terminate if we reached the value C=N.
#
    if ( c + 1 < n ):
      c = c + 1
    else:
      break
#
#  Increment R, but terminate if we reached the value R=M.
#
    if ( r + 1 < m ):
      r = r + 1
    else:
      break

  return B, a_cols

def rref_compute_test ( ):

#*****************************************************************************80
#
## rref_compute_test() tests rref_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rref_compute_test():' )
  print ( '  rref_compute() is a user-written code to compute the' )
  print ( '  reduced row echelon form (RREF) of a matrix.' )

  A = np.array ( [ \
    [  1,  3,  0,  2,  6,  3,  1 ], \
    [ -2, -6,  0, -2, -8,  3,  1 ], \
    [  3,  9,  0,  0,  6,  6,  2 ], \
    [ -1, -3,  0,  1,  0,  9,  3 ] ] )

  print ( '' )
  print ( '  Matrix A:' )
  print ( A )

  A1, a_cols = rref_compute ( A )

  print ( '' )
  print ( '  rref_compute(A):' )
  print ( A1 )

  print ( '' )
  print ( '  a_cols:' )
  print ( a_cols )

  return

def rref_determinant ( A ):

#*****************************************************************************80
#
## rref_determinant() uses reduced row echelon form (RREF) to compute a determinant.
#
#  Discussion:
#
#    The procedure will fail if A is not square.
#
#    This is simply a demonstration of how the RREF can be used to compute
#    the determinant.  There are better ways to compute the inverse, 
#    including d = np.linalg.det ( A )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N,N), a square matrix.
#
#  Output:
#
#    real A_DET: the determinant.
#
  import numpy as np

  m, n = A.shape

  if ( m != n ):
    print ( '' )
    print ( 'rref_determinant(): Fatal error!' )
    print ( '  Input matrix is not square.' )
    raise Exception ( 'rref_determinant(): Fatal error!' )
#
#  Do an RREF on A.
#
  ARREF, a_cols = rref_compute ( A )
#
#  Compute product of diagonal entries.
#
  a_det = 1.0
  for i in range ( 0, n ):
    a_det = a_det * ARREF[i,i]

  return a_det

def rref_determinant_test ( ):

#*****************************************************************************80
#
## rref_determinant_test() tests rref_determinant().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rref_determinant_test():' )
  print ( '  rref_determinant() uses the reduced row echelon form ' )
  print ( '  of a square matrix to compute the determinant.' )

  n = 4

  A = np.array ( [ \
     [ 5,  7,  6,  5 ], \
     [ 7, 10,  8,  7 ], \
     [ 6,  8, 10,  9 ], \
     [ 5,  7,  9, 10 ] ] )
  print ( '' )
  print ( '  Matrix A:' )
  print ( A )

  a_det = rref_determinant ( A )
  print ( '' )
  print ( '  Estimated determinant of A = :', a_det )
  print ( '' )
  print ( '  np.linalg.det(A) = ', np.linalg.det ( A ) )

  return

def rref_inverse ( A ):

#*****************************************************************************80
#
## rref_inverse() uses reduced row echelon form (RREF) to compute an inverse.
#
#  Discussion:
#
#    The procedure will fail if A is not square, or not invertible.
#
#    This is simply a demonstration of how RREF can be used to compute
#    the inverse.  But:
#    * there are better ways to compute the inverse, including
#      B = inv ( A )
#    * the inverse matrix is usually not the appropriate tool for solving
#      linear systems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N,N), a square, invertible matrix.
#
#  Output:
#
#    real AINV(N,N), the inverse of A, computed using the rref_compute().
#
  import numpy as np

  m, n = A.shape

  if ( m != n ):
    print ( '' )
    print ( 'rref_inverse(): Fatal error!' )
    print ( '  Input matrix is not square.' )
    raise Exception ( 'rref_inverse(): Fatal error!' )
#
#  First do an RREF on A alone.
#  The second argument is the independent columns found in the input matrix.
#
  ARREF, a_cols = rref_compute ( A )

  if ( len ( a_cols ) < n ):
    print ( '' )
    print ( 'rref_inverse(): Warning!' )
    print ( '  The input matrix seems to be singular.' )
    print ( '  The inverse could not be computed.' )
    raise Exception ( '  The input matrix seems to be singular.' )
#
#  If A has N independent columns, append the identity and repeat the RREF.
#
  AI = np.hstack ( [ A, np.eye(m,n) ] )

  AIRREF, a_cols = rref_compute ( AI )
#
#  The last N columns of AIRREF are the inverse.
#
  AINV = AIRREF[0:m,n:2*n]

  return AINV

def rref_inverse_test ( ):

#*****************************************************************************80
#
## rref_inverse_test() tests rref_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rref_inverse_test():' )
  print ( '  rref_inverse() uses the reduced row echelon form ' )
  print ( '  of a square matrix to compute its inverse.' )

  n = 4

  A = np.array ( [ \
     [ 5,  7,  6,  5 ], \
     [ 7, 10,  8,  7 ], \
     [ 6,  8, 10,  9 ], \
     [ 5,  7,  9, 10 ] ] )
  print ( '' )
  print ( '  Matrix A:' )
  print ( A )

  A_INV = rref_inverse ( A )
  print ( '' )
  print ( '  Estimated inverse of A, A_inv:' )
  print ( A_INV )

  print ( '' )
  print ( '  np.linalg.inv ( A ):' )
  print ( np.linalg.inv ( A ) )

  P = np.dot ( A_INV, A )
  print ( '' )
  print ( '  Product A_inv * A:' )
  print ( P )

  return

def rref_rank ( A ):

#*****************************************************************************80
#
## rref_rank() returns the rank of a matrix, using the reduced row echelon form.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), the matrix to be analyzed.
#
#  Output:
#
#    integer A_RANK, the estimated rank of A.
#    0 <= A_RANK <= min ( M, N ).
#
  import numpy as np

  A_REF, a_cols = rref_compute ( A )

  a_rank = len ( a_cols )

  return a_rank

def rref_rank_test ( ):

#*****************************************************************************80
#
## rref_rank_test() tests rref_rank().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rref_rank_test():' )
  print ( '  rref_rank() uses the reduced row echelon form ' )
  print ( '  of a matrix to estimate its rank.' )

  A = np.array ( [ \
    [ 1, -2, 3, -1 ], \
    [ 3, -6, 9, -3 ], \
    [ 0,  0, 0,  0 ], \
    [ 2, -2, 0,  1 ], \
    [ 6, -8, 6,  0 ], \
    [ 3,  3, 6,  9 ], \
    [ 1,  1, 2,  3 ] ] )

  print ( '' )
  print ( '  Matrix A:' )
  print ( A )

  a_rank = rref_rank ( A )
  print ( '' )
  print ( '  A has rank ', a_rank )

  print ( '  np.linalg.matrix_rank(A) ', np.linalg.matrix_rank ( A ) )

  return

def rref_solve ( A, b ):

#*****************************************************************************80
#
## rref_solve() uses reduced row echelon form (RREF) to solve a linear system.
#
#  Discussion:
#
#    A linear system A*x=b is given, where
#    A is an MxN1 matrix, possibly singular.
#    b is an Mx1 right hand side, or MxN2 collection of right hand sides.
#    x is the desired N1x1 solution, or N1xN2 collection of solutions.
#
#    The right hand sides are assumed to be consistent, that is,
#    each right hand side is assumed to be a linear combination of 
#    columns of A.  If this is not so, the procedure will still produce
#    a result x, but it will not satisfy the equation A*x=b. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N1), a matrix.
#
#    real B(M,N2), one or more right hand sides consistent with A.
#
#  Output:
#
#    real X(N1,N2), one or more solution vectors.
#
  import numpy as np

  m1, n1 = A.shape

# if ( b.ndim == 1 ):
#   b = np.atleast_2d ( b )
#   b = b.T

  m2, n2 = b.shape

  if ( m1 != m2 ):
    print ( '' )
    print ( 'rref_solve(): Fatal error!' )
    print ( '  B does not have the same number of rows as A.' )
    raise Exception ( 'rref_solve(): Fatal error!' )

  AI = np.hstack ( [ A, b ] )

  AIRREF, a_cols = rref_compute ( AI )

  x = AIRREF[0:n1,n1:n1+n2]

  return x

def rref_solve_test ( ):

#*****************************************************************************80
#
## rref_solve_test() tests rref_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'rref_solve_test():' )
  print ( '  rref_solve() uses the reduced row echelon form ' )
  print ( '  of a square matrix to solve a linear system.' )

  n = 4

  A = np.array ( [ \
     [ 5.0,  7.0,  6.0,  5.0 ], \
     [ 7.0, 10.0,  8.0,  7.0 ], \
     [ 6.0,  8.0, 10.0,  9.0 ], \
     [ 5.0,  7.0,  9.0, 10.0 ] ] )
  print ( '' )
  print ( '  Matrix A:' )
  print ( A )

  b = np.array ( [ \
    [ 57.0 ], \
    [ 79.0 ], \
    [ 88.0 ], \
    [ 86.0 ] ] )
  print ( '  Right hand side b:' )
  print ( b )

  x2 = rref_solve ( A, b )
  print ( '' )
  print ( '  Estimated solution:' )
  print ( x2 )

  print ( '' )
  print ( '  np.linalg.solve ( A, b ):' )
  print ( np.linalg.solve ( A,  b ) )

  b2 = np.dot ( A, x2 )
  print ( '' )
  print ( '  Product A * x:' )
  print ( b2 )

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
  rref2_test ( )
  timestamp ( )

