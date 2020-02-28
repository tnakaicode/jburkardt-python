#! /usr/bin/env python
#
def rotation_mat2axis ( a ):

#*****************************************************************************80
#
## ROTATION_MAT2AXIS converts a rotation from matrix to axis format in 3D.
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
#    Output, real AXIS(3), the axis vector which remains
#    unchanged by the rotation.
#
#    Output, real ANGLE, the angular measurement of the
#    rotation about the axis, in radians.
#
  import numpy as np
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
    print ( 'ROTATION_MAT2AXIS - Fatal error!' )
    print ( '  A is not a rotation matrix,' )
    print ( '  or there are multiple axes of rotation.' )
    exit ( 'ROTATION_MAT2AXIS - Fatal error!' )

  axis = axis / axis_norm
#
#  Find the angle.
#
  angle = np.arccos ( 0.5 * ( a[0,0] + a[1,1] + a[2,2] - 1.0 ) )

  return axis, angle

def rotation_mat2axis_test ( ):

#*****************************************************************************80
#
## ROTATION_MAT2AXIS_TEST tests ROTATION_MAT2AXIS.
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
  from rotation_axis2mat import rotation_axis2mat

  a = np.array ( [ \
   [  0.43301269,  0.25,       -0.86602539 ], \
   [ -0.5,         0.86602539,  0.0 ], \
   [  0.75,        0.43301269,  0.5 ] ])

  print ( '' )
  print ( 'ROTATION_MAT2AXIS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROTATION_MAT2AXIS computes a rotation axis' )
  print ( '  and angle from a rotation matrix.' )
  print ( '  ROTATION_AXIS2MAT computes a rotation matrix' )
  print ( '  from a rotation axis and angle.' )

  r8mat_print ( 3, 3, a, '  The rotation matrix:' )

  axis, angle = rotation_mat2axis ( a )

  r8vec_print ( 3, axis, '  The rotation axis:' )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  a = rotation_axis2mat ( axis, angle )

  r8mat_print ( 3, 3, a, '  The recovered rotation matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROTATION_MAT2AXIS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rotation_mat2axis_test ( )
  timestamp ( )

