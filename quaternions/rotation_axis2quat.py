#! /usr/bin/env python
#
def rotation_axis2quat ( axis, angle ):

#*****************************************************************************80
#
## ROTATION_AXIS2QUAT converts a rotation from axis to quaternion format in 3D.
#
#  Discussion:
#
#    A rotation quaternion Q has the form:
#
#      Q = A + Bi + Cj + Dk
#
#    where A, B, C and D are real numbers, and i, j, and k are to be regarded
#    as symbolic constant basis vectors, similar to the role of the "i"
#    in the representation of imaginary numbers.
#
#    A is the cosine of half of the angle of rotation.  (B,C,D) is a
#    unit vector pointing in the direction of the axis of rotation.
#    Rotation multiplication and inversion can be carried out using
#    this format and the usual rules for quaternion multiplication
#    and inversion.
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
#  Parameters:
#
#    Input, real AXIS(3), the axis vector which remains 
#    unchanged by the rotation.
#
#    Input, real ANGLE, the angular measurement of the 
#    rotation about the axis, in radians.
#
#    Output, real Q(4), the quaternion representing the rotation.
#
  import numpy as np

  q = np.zeros ( 4 )

  axis_norm = np.linalg.norm ( axis )

  if ( axis_norm == 0.0 ):
    print ( '' )
    print ( 'ROTATION_AXIS2QUAT_3D - Fatal error!' )
    print ( '  The axis vector is null.' )

  q[0]   = np.cos ( 0.5 * angle )
  q[1:4] = np.sin ( 0.5 * angle ) * axis[0:3] / axis_norm

  return q

def rotation_axis2quat_test ( ):

#*****************************************************************************80
#
## ROTATION_AXIS2QUAT_TEST tests ROTATION_AXIS2QUAT.
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
  from degrees_to_radians import degrees_to_radians
  from r8vec_print import r8vec_print
  from rotation_quat_vector import rotation_quat_vector

  print ( '' )
  print ( 'ROTATION_AXIS2QUAT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROTATION_AXIS2QUAT converts a rotation axis to a quaternion.' )
 
  v = np.array ( [ 1.0, 4.0, 10.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  axis = np.array ( [ 0.2361737, -0.8814124, -0.4090649 ] )
  r8vec_print ( 3, axis, '  The rotation axis:' )

  angle = 1.159804
  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  q = rotation_axis2quat ( axis, angle )

  r8vec_print ( 4, q, '  The rotation quaternion Q:' )

  w = rotation_quat_vector ( q, v )

  r8vec_print ( 3, w, '  The rotated vector W:' )
#
#  Another test of ROTATION_AXIS_VECTOR with an axis vector
#  that does not have unit length.
#
  v = np.array ( [ 1.0, 1.0, 1.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  axis = np.array ( [ 0.0, 0.0, 2.0 ] )
  r8vec_print ( 3, axis, '  The rotation axis:' )

  angle = 90.0
  angle = degrees_to_radians ( angle )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )
  q = rotation_axis2quat ( axis, angle )

  r8vec_print ( 4, q, '  The rotation quaternion Q:' )

  w = rotation_quat_vector ( q, v )

  r8vec_print ( 3, w, '  The rotated vector W:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROTATION_AXIS2QUAT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rotation_axis2quat_test ( )
  timestamp ( )


