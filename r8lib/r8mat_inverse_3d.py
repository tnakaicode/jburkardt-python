#! /usr/bin/env python
#
def r8mat_inverse_3d ( a ):

#*****************************************************************************80
#
## R8MAT_INVERSE_3D inverts a 3 by 3 R8MAT using Cramer's rule.
#
#  Discussion:
#
#    If DET is zero, then A is singular, and does not have an
#    inverse.  In that case, B is simply set to zero, and a
#    message is printed.
#
#    If DET is nonzero, then its value is roughly an estimate
#    of how nonsingular the matrix A is.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A(3,3), the matrix to be inverted.
#
#    Output, real B(3,3), the inverse of the matrix.
#
#    Output, real DET, the determinant of the matrix.
#
  import numpy as np
#
#  Compute the determinant of A
#
  det =   a[0,0] * ( a[1,1] * a[2,2] - a[1,2] * a[2,1] ) \
        + a[0,1] * ( a[1,2] * a[2,0] - a[1,0] * a[2,2] ) \
        + a[0,2] * ( a[1,0] * a[2,1] - a[1,1] * a[2,0] )
#
#  If the determinant is zero, bail out.
#
  if ( det == 0.0 ):
    b = np.zeros ( [ 3, 3 ] )
    return b, det
#
#  Compute the entries of the inverse matrix using an explicit
#  formula.
#
  b = np.zeros ( [ 3, 3 ] )

  b[0,0] = + ( a[1,1] * a[2,2] - a[1,2] * a[2,1] ) / det
  b[0,1] = - ( a[0,1] * a[2,2] - a[0,2] * a[2,1] ) / det
  b[0,2] = + ( a[0,1] * a[1,2] - a[0,2] * a[1,1] ) / det

  b[1,0] = - ( a[1,0] * a[2,2] - a[1,2] * a[2,0] ) / det
  b[1,1] = + ( a[0,0] * a[2,2] - a[0,2] * a[2,0] ) / det
  b[1,2] = - ( a[0,0] * a[1,2] - a[0,2] * a[1,0] ) / det

  b[2,0] = + ( a[1,0] * a[2,1] - a[1,1] * a[2,0] ) / det
  b[2,1] = - ( a[0,0] * a[2,1] - a[0,1] * a[2,0] ) / det
  b[2,2] = + ( a[0,0] * a[1,1] - a[0,1] * a[1,0] ) / det

  return b, det

def r8mat_inverse_3d_test ( ):

#*****************************************************************************80
#
## R8MAT_INVERSE_3D_TEST tests R8MAT_INVERSE_3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print

  n = 3
#
#  Each ROW of this definion is a COLUMN of the matrix.
#
  a = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ], \
    [ 7.0, 8.0, 0.0 ] ] )

  print ( '' )
  print ( 'R8MAT_INVERSE_3D_TEST' )
  print ( '  R8MAT_INVERSE_3D inverts a 3 by 3 matrix.' )

  r8mat_print ( n, n, a, '  Matrix A to be inverted:' )
#
#  Compute the inverse matrix.
#
  b, det = r8mat_inverse_3d ( a )
 
  if ( det == 0.0 ):
    print ( '' )
    print ( '  The input matrix was singular, no inverse' )
    print ( '  could be computed.' )
    return

  r8mat_print ( n, n, b, '  Inverse matrix B:' )

  c = np.dot ( a, b )

  r8mat_print ( n, n, c, '  Product C = A * B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_INVERSE_3D_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_inverse_3d_test ( )
  timestamp ( )

