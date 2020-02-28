#! /usr/bin/env python
#
def r8mat_det_4d ( a ):

#*****************************************************************************80
#
## R8MAT_DET_4D computes the determinant of a 4 by 4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A(4,4), the matrix whose determinant is desired.
#
#    Output, real VALUE, the determinant of the matrix.
#
  value = \
      a[0,0] * ( \
        a[1,1] * ( a[2,2] * a[3,3] - a[2,3] * a[3,2] ) \
      - a[1,2] * ( a[2,1] * a[3,3] - a[2,3] * a[3,1] ) \
      + a[1,3] * ( a[2,1] * a[3,2] - a[2,2] * a[3,1] ) ) \
    - a[0,1] * ( \
        a[1,0] * ( a[2,2] * a[3,3] - a[2,3] * a[3,2] ) \
      - a[1,2] * ( a[2,0] * a[3,3] - a[2,3] * a[3,0] ) \
      + a[1,3] * ( a[2,0] * a[3,2] - a[2,2] * a[3,0] ) ) \
    + a[0,2] * ( \
        a[1,0] * ( a[2,1] * a[3,3] - a[2,3] * a[3,1] ) \
      - a[1,1] * ( a[2,0] * a[3,3] - a[2,3] * a[3,0] ) \
      + a[1,3] * ( a[2,0] * a[3,1] - a[2,1] * a[3,0] ) ) \
    - a[0,3] * ( \
        a[1,0] * ( a[2,1] * a[3,2] - a[2,2] * a[3,1] ) \
      - a[1,1] * ( a[2,0] * a[3,2] - a[2,2] * a[3,0] ) \
      + a[1,2] * ( a[2,0] * a[3,1] - a[2,1] * a[3,0] ) )

  return value

def r8mat_det_4d_test ( ):

#*****************************************************************************80
#
## R8MAT_DET_4D_TEST tests R8MAT_DET_4D
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8mat_vand2 import r8mat_vand2

  n = 4

  x = np.array ( [ 1.0, 10.0, 4.0, 2.0 ] )

  print ( '' )
  print ( 'R8MAT_DET_4D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_DET_4D determinant of a 4 by 4 matrix' )

  a = r8mat_vand2 ( n, n, x )
  det = r8mat_det_4d ( a )

  r8mat_print ( n, n, a, '  Matrix:' )

  print ( '' )
  print ( '  R8MAT_DET_4D computes determinant: %g' % ( det ) )
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
  print ( 'R8MAT_DET_4D_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_det_4d_test ( )
  timestamp ( )
 
