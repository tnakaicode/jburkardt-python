#! /usr/bin/env python
#
def rotation_mat2quat ( a ):

#*****************************************************************************80
#
## ROTATION_MAT2QUAT converts a rotation from matrix to quaternion format in 3D.
#
#  Discussion:
#
#    The computation is based on the fact that a rotation matrix must
#    have an eigenvector corresponding to the eigenvalue of 1, hence:
#
#      ( A - I ) * v = 0.
#
#    The eigenvector V is the axis of rotation.
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
#    Jack Kuipers,
#    Quaternions and Rotation Sequences,
#    Princeton, 1998.
#
#  Parameters:
#
#    Input, real A(3,3), the rotation matrix.
#
#    Output, real Q(4), the quaternion representing the rotation.
#
  import numpy as np
  from sys import exit
#
#  Compute the normalized axis of rotation.
#
  axis = np.zeros ( 3 )
  axis[0] = a[2,1] - a[1,2]
  axis[1] = a[0,2] - a[2,0]
  axis[2] = a[1,0] - a[0,1]

  axis_norm = np.linalg.norm ( axis )

  if ( axis_norm == 0.0 ):
    print ( '' )
    print ( 'ROTATION_MAT2QUAT - Fatal error!' )
    print ( '  A is not a rotation matrix,' )
    print ( '  or there are multiple axes of rotation.' )
    exit ( 'ROTATION_MAT2QUAT - Fatal error!' )

  axis = axis / axis_norm
#
#  Compute the angle.
#
  angle = np.arccos ( 0.5 * ( a[0,0] + a[1,1] + a[2,2] - 1.0 ) )
#
#  Compute the quaternion.
#
  cos_phi = np.cos ( 0.5 * angle )

  sin_phi = np.sqrt ( 1.0 - cos_phi * cos_phi )

  q = np.zeros ( 4 )
  q[0]   = cos_phi
  q[1:4] = sin_phi * axis[0:3]

  return q

def rotation_mat2quat_test ( ):

#*****************************************************************************80
#
## ROTATION_MAT2QUAT_TEST tests ROTATION_MAT2QUAT.
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
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print
  from rotation_quat2mat import rotation_quat2mat

  a = np.array ( [ \
   [  0.43301269,  0.25,       -0.86602539 ], \
   [ -0.5,         0.86602539,  0.0 ], \
   [  0.75,        0.43301269,  0.5 ] ] )

  print ( '' )
  print ( 'ROTATION_MAT2QUAT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROTATION_MAT2QUAT computes a quaternion' )
  print ( '  from a rotation matrix.' )
  print ( '  ROTATION_QUAT2MAT computes a rotation matrix' )
  print ( '  from a quaternion.' )

  r8mat_print ( 3, 3, a, '  The rotation matrix:' )

  q = rotation_mat2quat ( a )

  r8vec_print ( 4, q, '  The rotation quaternion Q:' )

  a = rotation_quat2mat ( q )

  r8mat_print ( 3, 3, a, '  The recovered rotation matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROTATION_MAT2QUAT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rotation_mat2quat_test ( )
  timestamp ( )

