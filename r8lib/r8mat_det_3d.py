#! /usr/bin/env python
#
def r8mat_det_3d ( a ):

#*****************************************************************************80
#
## R8MAT_DET_3D computes the determinant of a 3 by 3 matrix.
#
#  Discussion:
#
#    The determinant is the volume of the shape spanned by the vectors
#    making up the rows or columns of the matrix.
#
#    det = a11 * a22 * a33 - a11 * a23 * a32
#        + a12 * a23 * a31 - a12 * a21 * a33
#        + a13 * a21 * a32 - a13 * a22 * a31
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real a[3,3), the matrix whose determinant is desired.
#
#    Output, real DET, the determinant of the matrix.
#
  det  =   a[0,0] * ( a[1,1] * a[2,2] - a[1,2] * a[2,1] ) \
         + a[0,1] * ( a[1,2] * a[2,0] - a[1,0] * a[2,2] ) \
         + a[0,2] * ( a[1,0] * a[2,1] - a[1,1] * a[2,0] )

  return det

def r8mat_det_3d_test ( ):

#*****************************************************************************80
#
## R8MAT_DET_3D_TEST tests R8MAT_DET_3D;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8mat_vand2 import r8mat_vand2

  n = 3

  x = np.array ( [ 1.0, 10.0, 4.0 ] )

  print ( '' )
  print ( 'R8MAT_DET_3D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_DET_3D: determinant of a 3 by 3 matrix' )

  a = r8mat_vand2 ( n, n, x )
  det = r8mat_det_3d ( a )

  r8mat_print ( n, n, a, '  Matrix:' )

  print ( '' )
  print ( '  R8MAT_DET_3D computes determinant: %g' % ( det ) )
#
#  Special formula for the determinant of a Vandermonde matrix:
#
  det = 1.0
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      det = det * ( x[i] - x[j] )

  print ( '  Exact determinant is %g' % ( det ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_DET_3D_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_det_3d_test ( )
  timestamp ( )
 
