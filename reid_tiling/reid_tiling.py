#! /usr/bin/env python3
#
def reid_tiling ( ):

#*****************************************************************************80
#
## reid_tiling() computes tilings of the Reid region using RREF.
#
#  Discussion:
#
#    A region of 8 squares is to be covered by 4 dominos.
#
#    The requirement that each square be covered becomes 8 equations,
#    that there must be exactly one domino square covering each 
#    region square.
#
#    The right hand side b is of length 8, with each entry being a
#    1, reflecting the number of domino squares covering that region square.
#
#    There are exactly 10 distinct ways that a domino can be placed
#    on the region.  We regard each of these ways as a variable v(j).
#    
#    Our solution x(k) is a 1 if variable v(k) is used in the tiling
#    and 0 otherwise.
#
#    This can be formulated as an 8 x 10 underdetermined linear system
#    of the form A*x=b.  The RREF can be used to find the degrees of
#    freedom in the system.  We are free to set these x variables to 
#    0 or 1.  By considering every possible such combination, we uncover
#    four distinct legal solutions and the corresponding tiling patterns.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 April 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'reid_tiling():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  reid_tiling() uses the RREF to uncover tilings of the Reid polygon.' )
  print ( '' )
#
#  Step 1: Define Region:
#
#   1 1 0
#   1 1 1
#   1 1 1
#
#  These squares are indexed as
#
#    0 1 
#    2 3 4
#    5 6 7
#
  r_shape = np.ones ( [ 3, 3 ] )
  r_shape[0,2] = 0
  
  print ( '' )
  print ( '  Shape of the Reid polygon:' )
  print ( '' )
  print ( r_shape )
#
#  Step 2: Define Tile Shape:
#
  p_num = 1
  p_shapes = np.zeros ( [ 3, 3, p_num ] )

  p_shapes[0:2,0,0] = 1
#
#  Step 3: Report Tile Shapes:
#
#  1
#  1
#
  print ( '' )
  print ( '  Tile 0:' )
  print ( '' )
  print ( p_shapes[0:2,0,0] )
#
#  Define linear system A*x=b.
#
#  The rows are equations, each associated with a square.
#  Equation I specifies that square I is to be covered exactly 1 time.
#
#  Thus the right hand side is (1,1,1,1,1,1,1).
#
#  Column J indicates which of the squares 0 through 7 are covered
#  by tile J.
#
#  This linear system can be generated (the hard way) by careful
#  consideration of all possible positions and orientations of each tile.
#  Each column of this matrix represents such a position and orientation,
#  and the 1 values indicate the squares covered in that case.  Thus,
#  the first column says that this domino position covers squares 0 and 2.
#
  A = np.array ( [ \
    [1,0,0,0,0,1,0,0,0,0], \
    [0,0,1,0,0,1,0,0,0,0], \
    [1,1,0,0,0,0,1,0,0,0], \
    [0,0,1,1,0,0,1,1,0,0], \
    [0,0,0,0,1,0,0,1,0,0], \
    [0,1,0,0,0,0,0,0,1,0], \
    [0,0,0,1,0,0,0,0,1,1], \
    [0,0,0,0,1,0,0,0,0,1] ] )

  print ( '' )
  print ( '  The matrix A:' )
  print ( '' )
#
#  We need right hand side to be a column vector, hence double brackets.
#
  b = np.array (  [ [1],[1],[1],[1],[1],[1],[1],[1] ] )
#
#  Append b to A.
#
  Ab = np.hstack ( [ A, b ] )
#
#  Get RREF.
#
  RREF = rref_compute ( Ab )

  print ( '' )
  print ( '  The RREF of A+b' )
  print ( '' )
  print ( RREF )
#
#  We need a new matrix C that combines the RREF information with
#  dummy equations for the free variables.
#
  m = RREF.shape[0]
  np1 = RREF.shape[1]
  n = np1 - 1

  C = np.eye ( n )
  b_RREF = np.zeros ( n )
  f = np.arange ( n )
#
#  Active rows of RREF replace corresponding rows of C.
#  f records the "free" variables.
#
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( RREF[i,j] == 1.0 ):
        C[j,:] = RREF[i,0:n]
        b_RREF[j] = RREF[i,-1]
        for k in range ( len ( f ) ):
          if ( f[k] == j ):
            f = np.delete ( f, k )
            break

        break

  print ( '' )
  print ( '  The new linear system C:' )
  print ( '' )
  print ( C )

  print ( '' )
  print ( '  The free variable indices f:' )
  print ( '' )
  print ( f )

  nf = len ( f )
#
#  For nz = 0 through 4 (the number of tiles)
#    Set nz free variables to 1
#      Solve linear system
#        If all variables are 0 or 1, accept it.
#
  from itertools import combinations

  print ( '' )
  print ( '  Legal solutions:' )
  print ( '' )

  for nz in range ( 0, nf + 1 ):
    for combo in combinations ( f, nz ):
      bb = b_RREF.copy()
      for i in combo:
        bb[i] = 1
      x = np.linalg.solve ( C, bb )
      if ( np.all ( ( x == 0 ) | ( x == 1 ) ) ):
        print ( x )
  
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
#    27 December 2024
#
#  Author:
#
#    Original Python version by ChatGPT.
#    This version by John Burkardt.
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
  import numpy as np
#
#  Ensure the matrix elements are floating-point for division.
#
  A = A.astype ( float )
#
#  Get the array shape.
#
  rows, cols = A.shape
#
#  Set a tolerance for the size of a pivot value.
#
  tol = np.sqrt ( np.finfo(float).eps )
#
#  Start from the first row.
#
  row = 0
#
#  Seek a pivot for each column.
#
  for col in range ( cols ):
#
#  Exit if we have run out of rows to examine.
#
    if ( rows <= row ):
      break
#        
#  Find the pivot row.
#
    pivot_row = np.argmax ( np.abs ( A[row:rows, col] ) ) + row
#
#  Skip this column if all values are below the tolerance.
#
    if ( np.abs ( A[pivot_row, col] ) <= tol ):
      continue
#
#  Swap current row and pivot row.
#
    A[[row, pivot_row]] = A[[pivot_row, row]]
#  
#  Scale the pivot row to make the pivot element equal to 1.
#
    A[row] = A[row] / A[row, col]
#   
#  Eliminate the column below and above the pivot.
#
    for i in range ( rows ):
      if ( i != row ):
        A[i] = A[i] - A[i, col] * A[row]
#
#  Move to the next row.
#
    row = row + 1
    
  return A

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

if ( __name__ == "__main__" ):
  timestamp ( )
  reid_tiling ( )
  timestamp ( )

