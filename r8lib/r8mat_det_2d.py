#! /usr/bin/env python
#
def r8mat_det_2d ( a ):

#*****************************************************************************80
#
## R8MAT_DET_2D computes the determinant of a 2 by 2 matrix.
#
#  Discussion:
#
#    The determinant is the area spanned by the vectors making up the rows
#    or columns of the matrix.
#
#    value = A(1,1) * A(2,2) - A(1,2) * A(2,1).
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
#    Input, real A(2,2), the matrix whose determinant is desired.
#
#    Output, real DET, the determinant of the matrix.
#
  det = a[0,0] * a[1,1] - a[0,1] * a[1,0]

  return det

def r8mat_det_2d_test ( ):

#*****************************************************************************80
#
## R8MAT_DET_2D_TEST tests R8MAT_DET_2D;
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

  n = 2

  x = np.array ( [ 1.0, 10.0 ] )

  print ( '' )
  print ( 'R8MAT_DET_2D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_DET_2D: determinant of a 2 by 2 matrix;' )

  a = r8mat_vand2 ( n, n, x )

  det = r8mat_det_2d ( a )

  r8mat_print ( n, n, a, '  Matrix:' );

  print ( '' )
  print ( '  R8MAT_DET_2D computes determinant: %g' % ( det ) )
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
  print ( 'R8MAT_DET_2D_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_det_2d_test ( )
  timestamp ( )
 
