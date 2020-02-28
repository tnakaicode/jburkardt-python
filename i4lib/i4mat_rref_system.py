#! /usr/bin/env python
#
def i4mat_rref_system ( m, n, a, b ):

#*****************************************************************************80
#
## I4MAT_RREF_SOLVE_SYSTEM sets up an augmented IRREF linear system.
#
#  Discussion:
#
#    An MxN linear system A*X = B is considered.
#
#    The matrix A and right hand side B are assumed to have been converted
#    to integer row-reduced echelon form (IRREF).
#
#    To create, if possible, a solvable NxN system, this function removes
#    trailing zero rows, and inserts where necessary, rows of the identity
#    matrix in A and zeros in B, corresponding to undetermined degrees of 
#    freedom, producing the NxN system:
#
#      A2 * X = B2
#
#    The function also indicates whether the initial system was inconsistent,
#    and identifies those rows of A2 that correspond to degrees of freedom.
#    
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the IRREF matrix A.
#
#    Input, integer A(M,N), the IRREF matrix to be analyzed. 
#
#    Input, integer B(M), the IRREF right hand side.
#
#    Output, integer A2(N,N), the modified IRREF matrix.
#
#    Output, integer B2(N), the modified IRREF right hand side.
#
#    Output, logical INCON, is TRUE if the system A*X=B is inconsistent.
#
#    Output, integer FREEDOM_NUM, the number of degrees of freedom.
#    If FREEDOM_NUM < 0, then there are no degrees of freedom and the
#    system is overdetermined.
#
#    Output, integer FREEDOM(FREEDOM_NUM), the indices of the degrees
#    of freedom, presuming 0 <= FREEDOM_NUM.
#
  import numpy as np
  from i4vec_identity_row import i4vec_identity_row
#
#  Determine 0 <= M2 <= M, the location of the last nonzero row in A.
#  If any zero row of A has a nonzero B, then the equations are inconsistent.
#
  m2 = m
  incon = False

  while ( 0 < m2 ):

    if ( np.any ( a[m2-1,0:n] != 0 ) ):
      break

    if ( b[m2-1] != 0 ):
      incon = True

    m2 = m2 - 1
#
#  Copying data in Python is obscure.
#  Copying submatrices in Numpy is doubly obscure.
#  Let's do something stupid, but correct!
#
  a2 = np.zeros ( [ n, n ] )
  b2 = np.zeros ( n )
  a2[0:m2,:] = a[0:m2,:]
  b2[0:m2] = b[0:m2]
#
#  Count the indeterminate variables.
#
  freedom_num = n - m2
#
#  If pivot in column J is missing,
#  modify matrix and right hand side.
#  Add J to list of indeterminate variables.
#
  freedom = []

  if ( 0 < freedom_num ):

    for j in range ( 0, n ):
      if ( m2 <= j ):
        row_j = i4vec_identity_row ( n, j )
        a2 = np.vstack ( ( a2[0:m2,0:n], row_j ) )
        b2 = np.concatenate ( ( b2[0:m2], [0] ) )
        freedom.append ( j )
        m2 = m2 + 1
      elif ( a2[j,j] == 0 ):
        row_j = i4vec_identity_row ( n, j )
        a2 = np.vstack ( ( a2[0:j,0:n], row_j, a2[j:m2,0:n] ) )
        b2 = np.concatenate ( ( b2[0:j], [0], b2[j:m2] ) )
        freedom.append ( j )
        m2 = m2 + 1

  return a2, b2, incon, freedom_num, freedom

def i4mat_rref_system_test ( ):

#*****************************************************************************80
#
## I4MAT_RREF_SYSTEM_TEST tests I4MAT_RREF_SYSTEM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print
  from i4mat_rref import i4mat_rref
  from i4vec_print import i4vec_print

  print ( '' )
  print ( 'I4MAT_RREF_SYSTEM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_RREF_SYSTEM computes the linear system associated' )
  print ( '  with an integer reduced row echelon form of an I4MAT.' )
#
#  "Wide" matrix.
#
  print ( '' )
  print ( '  Look at a "wide" matrix:' )

  m = 4
  n = 7

  a1 = np.array ( [ \
   [  1,  3, 0,  2,  6, 3, 1 ], \
   [ -2, -6, 0, -2, -8, 3, 1 ], \
   [  3,  9, 0,  0,  6, 6, 2 ], \
   [ -1, -3, 0,  1,  0, 9, 3 ] ] )

  i4mat_print ( m, n, a1, '  Input A1:' )

  a2, det = i4mat_rref ( m, n, a1 )

  print ( '' )
  print ( '  The pseudo-determinant = %d' % ( det ) )

  i4mat_print ( m, n, a2, '  A2, the IRREF of A1:' )

  b2 = np.array ( [ 1, 1, 1, 0 ] )
  i4vec_print ( m, b2, '  B2, the right hand side:' )

  a3, b3, incon, freedom_num, freedom = i4mat_rref_system ( m, n, a2, b2 )

  print ( '' )
  if ( incon ):
    print ( '  The original system is INCONSISTENT.' )
  else:
    print ( '  The original system is CONSISTENT.' )

  i4mat_print ( n, n, a3, '  A3, the augmented IRREF:' )
  i4vec_print ( n, b3, '  B3, the augmented RHS:' )
  i4vec_print ( freedom_num, freedom, '  Indices of degrees of freedom.' )
#
#  "Tall" matrix.
#
  print ( '' )
  print ( '  Look at a "tall" matrix:' )

  m = 7
  n = 4

  a1 = np.array ( [ \
    [ 1, -2, 3, -1 ], \
    [ 3, -6, 9, -3 ], \
    [ 0,  0, 0,  0 ], \
    [ 2, -2, 0,  1 ], \
    [ 6, -8, 6,  0 ], \
    [ 3,  3, 6,  9 ], \
    [ 1,  1, 2,  3 ] ] )

  i4mat_print ( m, n, a1, '  Input A1:' )

  a2, det = i4mat_rref ( m, n, a1 )

  print ( '' )
  print ( '  The pseudo-determinant = %d' % ( det ) )

  i4mat_print ( m, n, a2, '  A2, the IRREF of A1:' )

  b2 = np.ones ( m )
  i4vec_print ( m, b2, '  B2, the right hand side:' )

  a3, b3, incon, freedom_num, freedom = i4mat_rref_system ( m, n, a2, b2 )

  print ( '' )
  if ( incon ):
    print ( '  The original system is INCONSISTENT.' )
  else:
    print ( '  The original system is CONSISTENT.' )

  i4mat_print ( n, n, a3, '  A3, the augmented IRREF:' )
  i4vec_print ( n, b3, '  B3, the augmented RHS:' )
  i4vec_print ( freedom_num, freedom, '  Indices of degrees of freedom.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_RREF_SYSTEM_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_rref_system_test ( )
  timestamp ( )

