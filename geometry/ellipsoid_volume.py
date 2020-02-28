#! /usr/bin/env python
#
def ellipsoid_volume ( m, a, v, r ):

#*****************************************************************************80
#
## ELLIPSOID_VOLUME returns the volume of an ellipsoid.
#
#  Discussion:
#
#    The points X in the ellipsoid are described by an M by M
#    positive definite symmetric matrix A, an M-dimensional point V,
#    and a "radius" R, such that
#      (X-V)' * A * (X-V) <= R * R
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, real A(M,M), the matrix that describes
#    the ellipsoid.  A must be symmetric and positive definite.
#
#    Input, real V(M), the "center" of the ellipse.
#    The value of V is not actually needed by this function.
#
#    Input, real R, the "radius" of the ellipse.
#
#    Output, real VOLUME, the volume of the ellipsoid.
#
  from hyperball01_volume import hyperball01_volume
  from r8po import r8po_fa

  u = r8po_fa ( m, a )
 
  sqrt_det = 1.0
  for i in range ( 0, m ):
    sqrt_det = sqrt_det * u[i,i]

  volume = r ** m * hyperball01_volume ( m ) / sqrt_det

  return volume

def ellipsoid_volume_test ( ):

#*****************************************************************************80
#
## ELLIPSOID_VOLUME_TEST tests ELLIPSOID_VOLUME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'ELLIPSOID_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPSOID_VOLUME computes the volume of the ellipsoid' )
  print ( '    (X-V)\' * A * (X-V) <= R * R.' )

  m = 3;
  a = np.array ( [ \
    [ 9.0, 3.0, 3.0 ], \
    [ 3.0, 5.0, 3.0 ], \
    [ 3.0, 3.0, 3.0 ] ] )
  v = np.array ( [ 2.0, 3.0, 1.0 ] )
  r = 1.0

  print ( '' )
  print ( '  M = %d' % ( m ) )
  r8mat_print ( m, m, a, '  A:' )
  r8vec_print ( m, v, '  V:' )

  volume = ellipsoid_volume ( m, a, v, r )

  print ( '' )
  print ( '  Volume = %14.6g' % ( volume ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPSOID_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  ellipsoid_volume_test ( )
  timestamp ( )

