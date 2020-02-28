#! /usr/bin/env python
#
def i4mat_rref ( m, n, a ):

#*****************************************************************************80
#
## I4MAT_RREF computes the reduced row echelon form of an I4MAT.
#
#  Discussion:
#
#    If a matrix A contains only integer entries, then when it is transformed
#    to row reduced echelon form, it is likely that many entries will no longer
#    be integers, due to the elimination process.
#
#    In some cases, tiny arithmetic errors in this elimination process can
#    result in spurious, tiny nonzero values which can invalidate the
#    calculation, particular if the elimination is being done in an effort
#    to determine the rank of the matrix.  These serious errors can easily
#    occur in very small matrices, such as of size 7x10.
#
#    If we, instead, insist on using only integer operations on an integer
#    matrix, we can guarantee that tiny roundoff errors will not cause
#    such problems.  On the other hand, as the elimination process proceeds,
#    we may instead calculate integer matrix entries of increasingly
#    large, and then ultimately meaningless magnitude.  I imagine this is 
#    likely to happen for moderate size matrices of order 50x50, say, but
#    this is a huge improvement over the unreliability of the real
#    arithmetic case.
#
#
#    Thus, we define "integer row reduced echelon form" (IRREF):
#
#
#    A matrix is in integer row reduced echelon form if:
#
#    * The leading nonzero in each row is positive.
#
#    * Each row has no common factor greater than 1.
#
#    * The leading nonzero in each row occurs in a column to
#      the right of the leading nonzero in the previous row.
#
#    * Rows which are entirely zero occur last.
#
#    * When a row contains a leading nonzero in column J, then column J
#      is otherwise entirely zero.
#
#  Example:
#
#    Input matrix:
#
#     1    3    0    2    6    3    1
#    -2   -6    0   -2   -8    3    1
#     3    9    0    0    6    6    2
#    -1   -3    0    1    0    9    3
#
#    Output matrix:
#
#     1    3    0    0    2    0    0
#     0    0    0    1    2    0    0
#     0    0    0    0    0    3    1
#     0    0    0    0    0    0    0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer A(M,N), the matrix to be analyzed. 
#
#    Output, integer A(M,N), the IRREF of the matrix.
#
#    Output, integer DET, the pseudo-determinant.
#
  from sys import exit
  from i4mat_is_integer import i4mat_is_integer
  from i4mat_row_swap import i4mat_row_swap
  from i4vec_red import i4vec_red

  if ( not i4mat_is_integer ( m, n, a ) ):
    print ( '' )
    print ( 'I4MAT_REF - Fatal error!' )
    print ( '  Input matrix A is not integral.' )
    exit ( 'I4MAT_REF - Fatal error!' )

  lead = 0
  det = 1
 
  for r in range ( 0, m ):

    if ( n <= lead ):
      break
#
#  Start I at row R, and search for nonzero pivot entry A(I,LEAD).
#
    i = r

    while ( a[i,lead] == 0.0 ):

      i = i + 1
#
#  If reach last row, reset I to R, and increment LEAD.
#
      if ( m <= i ):
        i = r
        lead = lead + 1
#
#  If reach last column, we can find no more pivots.
#
        if ( n <= lead ):
          lead = -1
          break

    if ( lead < 0 ):
      break
#
#  Move pivot I into row R.
#
    if ( i != r ):
      i4mat_row_swap ( m, n, a, i, r )
#
#  Ensure pivot is positive.
#
    if ( a[r,lead] < 0 ):
      a[r,0:n] = - a[r,0:n]
      det = - det
#
#  Update the pseudo-determinant.
#
    det = det * a[r,lead]
#
#  Remove any common factor from row R.
#
    a[r,0:n], ifact = i4vec_red ( n, a[r,0:n], 1 )
#
#  Use a multiple of A(R,LEAD) to eliminate A(R+1:M,LEAD).
#
    for i in range ( 0, m ):

      if ( i != r ):

        a[i,0:n] = a[r,lead] * a[i,0:n] - a[i,lead] * a[r,0:n]

        a[i,0:n], ifact = i4vec_red ( n, a[i,0:n], 1 )

    lead = lead + 1

  return a, det

def i4mat_rref_test ( ):

#*****************************************************************************80
#
## I4MAT_RREF_TEST tests I4MAT_RREF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  m = 4
  n = 7

  a = np.array ( [ \
    [  1,  3,  0,  2,  6,  3,  1 ], \
    [ -2, -6,  0, -2, -8,  3,  1 ], \
    [  3,  9,  0,  0,  6,  6,  2 ], \
    [ -1, -3,  0,  1,  0,  9,  3 ] ] )

  print ( '' )
  print ( 'I4MAT_RREF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_RREF computes the integer reduced row echelon form (IREF)' )
  print ( '  of an I4MAT.' )

  i4mat_print ( m, n, a, '  Input A:' )

  a, det = i4mat_rref ( m, n, a )

  print ( '' )
  print ( '  The pseudo-determinant = %d' % ( det ) )

  i4mat_print ( m, n, a, '  IRREF form:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_RREF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_rref_test ( )
  timestamp ( )

