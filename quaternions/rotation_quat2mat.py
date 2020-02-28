#! /usr/bin/env python
#
def rotation_quat2mat ( q ):

#*****************************************************************************80
#
## ROTATION_QUAT2MAT converts a rotation from quaternion to matrix format in 3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Foley, van Dam, Feiner, Hughes,
#    Computer Graphics, Principles and Practice,
#    Addison Wesley, Second Edition, 1990.
#
#  Parameters:
#
#    Input, real Q(4), the quaternion representing the rotation.
#
#    Output, real A(3,3), the rotation matrix.
#
  import numpy as np

  cos_phi = q[0]
  sin_phi = np.linalg.norm ( q[1:4] )

  angle = 2.0 * np.arctan2 ( sin_phi, cos_phi )

  if ( sin_phi == 0.0 ):
    v1 = 1.0
    v2 = 0.0
    v3 = 0.0
  else:
    v1 = q[1] / sin_phi
    v2 = q[2] / sin_phi
    v3 = q[3] / sin_phi

  ca = np.cos ( angle )
  sa = np.sin ( angle )

  a = np.zeros ( [ 3, 3 ] )

  a[0,0] =                v1 * v1 + ca * ( 1.0 - v1 * v1 )
  a[0,1] = ( 1.0 - ca ) * v1 * v2 - sa * v3
  a[0,2] = ( 1.0 - ca ) * v1 * v3 + sa * v2

  a[1,0] = ( 1.0 - ca ) * v2 * v1 + sa * v3
  a[1,1] =                v2 * v2 + ca * ( 1.0 - v2 * v2 )
  a[1,2] = ( 1.0 - ca ) * v2 * v3 - sa * v1

  a[2,0] = ( 1.0 - ca ) * v3 * v1 - sa * v2
  a[2,1] = ( 1.0 - ca ) * v3 * v2 + sa * v1
  a[2,2] =                v3 * v3 + ca * ( 1.0 - v3 * v3 )

  return a

def rotation_quat2mat_test ( ):

#*****************************************************************************80
#
## ROTATION_QUAT2MAT_TEST tests ROTATION_QUAT2MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from q8_transpose_print import q8_transpose_print
  from r8mat_print import r8mat_print
  
  from rotation_mat2quat import rotation_mat2quat

  q = np.array ( [ 0.836516, 0.12941, -0.482963, -0.224144 ] )

  print ( '' )
  print ( 'ROTATION_QUAT2MAT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROTATION_QUAT2MAT computes a rotation axis' )
  print ( '  from a rotation quaternion.' )
  print ( '  ROTATION_MAT2QUAT computes a rotation' )
  print ( '  quaternion from a rotation matrix.' )

  print ( '' )
  q8_transpose_print ( q, '  The rotation quaternion:' )

  a = rotation_quat2mat ( q )

  r8mat_print ( 3, 3, a, '  The rotation matrix:' )

  q = rotation_mat2quat ( a )

  print ( '' );
  q8_transpose_print ( q, '  The recovered rotation quaternion:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROTATION_QUAT2MAT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rotation_quat2mat_test ( )
  timestamp ( )

