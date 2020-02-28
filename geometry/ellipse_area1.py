#! /usr/bin/env python
#
def ellipse_area1 ( a, r ):

#*****************************************************************************80
#
## ELLIPSE_AREA1 returns the area of an ellipse defined by a matrix.
#
#  Discussion:
#
#    The points X in the ellipse are described by a 2 by 2
#    positive definite symmetric matrix A, and a "radius" R, such that
#      X' * A * X <= R * R
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A(2,2), the matrix that describes
#    the ellipsoid.  A must be symmetric and positive definite.
#
#    Input, real R, the "radius" of the ellipse.
#
#    Output, real VALUE, the area of the ellipse.
#
  import numpy as np

  value = r * r * np.pi / np.sqrt ( a[0,0] * a[1,1] - a[1,0] * a[0,1] )

  return value

def ellipse_area1_test ( ):

#*****************************************************************************80
#
## ELLIPSE_AREA1_TEST tests ELLIPSE_AREA1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'ELLIPSE_AREA1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPSE_AREA1 computes the area of an ellipse.' )

  r = 10.0
  a = np.array ( [ [ 5.0, 1.0 ], [ 1.0, 2.0 ] ] )
  area = ellipse_area1 ( a, r )
  print ( '' )
  print ( '  R = %g' % ( r ) )
  r8mat_print ( 2, 2, a, '  Matrix A in ellipse definition x*A*x=r^2' )
  print ( '  Area = %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPSE_AREA1_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ellipse_area1_test ( )
  timestamp ( )
