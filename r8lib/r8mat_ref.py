#! /usr/bin/env python
#
def r8mat_ref ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_REF computes the row echelon form of a matrix.
#
#  Discussion:
#
#    A matrix is in row echelon form if:
#
#    * The first nonzero entry in each row is 1.
#
#    * The leading 1 in a given row occurs in a column to
#      the right of the leading 1 in the previous row.
#
#    * Rows which are entirely zero must occur last.
#
#  Example:
#
#    Input matrix:
#
#     1.0  3.0  0.0  2.0  6.0  3.0  1.0
#    -2.0 -6.0  0.0 -2.0 -8.0  3.0  1.0
#     3.0  9.0  0.0  0.0  6.0  6.0  2.0
#    -1.0 -3.0  0.0  1.0  0.0  9.0  3.0
#
#    Output matrix:
#
#     1.0  3.0  0.0  2.0  6.0  3.0  1.0
#     0.0  0.0  0.0  1.0  2.0  4.5  1.5
#     0.0  0.0  0.0  0.0  0.0  1.0  0.3
#     0.0  0.0  0.0  0.0  0.0  0.0  0.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 April 2018
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
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of
#    the matrix A.
#
#    Input, real A(M,N), the matrix to be analyzed.
#
#    Output, real A(M,N), the REF form of the matrix.
#
#    Output, real DET, the pseudo-determinant.
#
  from r8_epsilon import r8_epsilon

  det = 1.0
  asum = 0.0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      asum = asum + abs ( a[i,j] )
  tol = r8_epsilon ( ) * asum
  lead = 0

  for r in range ( 0, m ):

    if ( n < lead ):
      break

    i = r

    while ( abs ( a[i,lead] ) <= 0.0 ):

      i = i + 1

      if ( m <= i ):
        i = r
        lead = lead + 1
        if ( n <= lead ):
          lead = -1
          break

    if ( lead < 0 ):
      break

    temp     = a[i,0:n]
    a[i,0:n] = a[r,0:n]
    a[r,0:n] = temp

    det = det * a[r,lead]
    a[r,0:n] = a[r,0:n] / a[r,lead]

    for i in range ( r + 1, m ):
      a[i,0:n] = a[i,0:n] - a[i,lead] * a[r,0:n]

    lead = lead + 1

  return a, det

def r8mat_ref_test ( ):

#*****************************************************************************80
#
## R8MAT_REF_TEST tests R8MAT_REF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print

  m = 4
  n = 7

  a = np.array( [ \
    [  1.0,  3.0,  0.0,  2.0,  6.0,  3.0,  1.0 ], \
    [ -2.0, -6.0,  0.0, -2.0, -8.0,  3.0,  1.0 ], \
    [  3.0,  9.0,  0.0,  0.0,  6.0,  6.0,  2.0 ], \
    [ -1.0, -3.0,  0.0,  1.0,  0.0,  9.0,  3.0 ] ] )

  print ( '' )
  print ( 'R8MAT_REF_TEST' )
  print ( '  R8MAT_REF computes the row echelon form of a matrix.' )

  r8mat_print ( m, n, a, '  Input A:' )

  a, det = r8mat_ref ( m, n, a )

  print ( '' )
  print ( '  Pseudo-determinat = %g' % ( det ) )

  r8mat_print ( m, n, a, '  REF form:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_REF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_ref_test ( )
  timestamp ( )

