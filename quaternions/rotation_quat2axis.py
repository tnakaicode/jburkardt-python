#! /usr/bin/env python
#
def rotation_quat2axis ( q ):

#*****************************************************************************80
#
## ROTATION_QUAT2AXIS converts a rotation from quaternion to axis format in 3D.
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
#    vector pointing in the direction of the axis of rotation.
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
#    Input, real Q(4), the quaternion representing the rotation.
#
#    Output, real AXIS(3), the axis vector which remains 
#    unchanged by the rotation.
#
#    Output, real ANGLE, the angular measurement of the 
#    rotation about the axis, in radians.
#
  import numpy as np

  cos_phi = q[0]
  sin_phi = np.linalg.norm ( q[1:4] )

  angle = 2.0 * np.arctan2 ( sin_phi, cos_phi )

  if ( sin_phi == 0.0 ):
    axis = np.array ( [ 1.0, 0.0, 0.0 ] )
  else:
    axis = q[1:4] / sin_phi

  return axis, angle

def rotation_quat2axis_test ( ):

#*****************************************************************************80
#
## ROTATION_QUAT2AXIS_TEST tests ROTATION_QUAT2AXIS.
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
  from r8vec_print import r8vec_print
  from rotation_axis2quat import rotation_axis2quat

  q = np.array ( [ 0.836516, 0.12941, -0.482963, -0.224144 ] )

  print ( '' )
  print ( 'ROTATION_QUAT2AXIS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROTATION_QUAT2AXIS computes a rotation axis' )
  print ( '  and angle from a rotation quaternion.' )
  print ( '  ROTATION_AXIS2QUAT computes a rotation' )
  print ( '  quaternion from a rotation axis and angle.' )

  q8_transpose_print ( q, '  The rotation quaternion:' )

  axis, angle = rotation_quat2axis ( q )

  r8vec_print ( 3, axis, '  The rotation axis:' )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  q = rotation_axis2quat ( axis, angle )

  q8_transpose_print ( q, '  The recoverd rotation quaternion:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROTATION_QUAT2AXIS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rotation_quat2axis_test ( )
  timestamp ( )

