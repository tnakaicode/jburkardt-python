#! /usr/bin/env python
#
def r8mat_vand2 ( m, n, x ):

#*****************************************************************************80
#
## R8MAT_VAND2 returns the N by N row Vandermonde matrix A.
#
#  Discussion:
#
#    The row Vandermonde matrix returned by this routine reads "across"
#    rather than down.  In particular, each row begins with a 1, followed by
#    some value X, followed by successive powers of X.
#
#  Formula:
#
#    A(I,J) = X(I)^(J-1)
#
#  Properties:
#
#    A is nonsingular if, and only if, the X values are distinct.
#
#    The determinant of A is
#
#      det(A) = product ( 2 <= I <= N ) (
#        product ( 1 <= J <= I-1 ) ( ( X(I) - X(J) ) ) ).
#
#    The matrix A is generally ill-conditioned.
#
#  Example:
#
#    N = 5, X = (2, 3, 4, 5, 6)
#
#    1 2  4   8   16
#    1 3  9  27   81
#    1 4 16  64  256
#    1 5 25 125  625
#    1 6 36 216 1296
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix desired.
#
#    Input, real X(M), the values that define A.
#
#    Output, real A(M,N), the M by N row Vandermonde matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )
  
  for i in range ( 0, m ):
    a[i,0] = 1.0
    for j in range ( 1, n ):
      a[i,j] = a[i,j-1] * x[i]

  return a

def r8mat_vand2_test ( ):

#*****************************************************************************80
#
## R8MAT_VAND2_TEST tests R8MAT_VAND2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_print import r8mat_print
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  m = 5
  n = 4

  print ( '' )
  print ( 'R8MAT_VAND2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_VAND2 returns a row Vandermonde matrix.' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  The factor vector X:' )

  a = r8mat_vand2 ( m, n, x )
  r8mat_print ( m, n, a, '  The row Vandermonde matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_VAND2_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_vand2_test ( )
  timestamp ( )
 
