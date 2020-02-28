#! /usr/bin/env python
#
def rotation_axis_vector ( axis, angle, v ):

#*****************************************************************************80
#
## ROTATION_AXIS_VECTOR rotates a vector around an axis vector in 3D.
#
#  Discussion:
#
#    Thanks to Cody Farnell for correcting some mistakes in an earlier
#    version of this routine.
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
#    Input, real AXIS(3), the axis vector for the rotation.
#
#    Input, real ANGLE, the angle, in radians, of the rotation.
#
#    Input, real V(3), the vector to be rotated.
#
#    Output, real W(3), the rotated vector.
#
  import numpy as np
#
#  Compute the length of the rotation axis.
#
  u = axis.copy ( )
  axis_norm = np.linalg.norm ( u )

  if ( axis_norm == 0.0 ):
    w = np.zeros ( 3 )
    return w

  u = u / axis_norm
#
#  Compute the dot product of the vector and the rotation axis.
#
  udotv = np.dot ( u, v )
#
#  Compute the parallel component of the vector.
#
  parallel = udotv * u
#
#  Compute the normal component of the vector.
#
  normal = v - parallel

  normal_norm = np.linalg.norm ( normal )

  if ( normal_norm == 0.0 ):
    w = parallel.copy ( )
    return w

  normal = normal / normal_norm
#
#  Compute a second vector, lying in the plane, perpendicular
#  to V, and forming a right-handed system, as the cross product
#  of the first two vectors.
#
  normal2 = np.zeros ( 3 )

  normal2[0] = u[1] * normal[2] - u[2] * normal[1]
  normal2[1] = u[2] * normal[0] - u[0] * normal[2]
  normal2[2] = u[0] * normal[1] - u[1] * normal[0]

  normal2_norm = np.linalg.norm ( normal2 )

  normal2 = normal2 / normal2_norm
#
#  Rotate the normal component by the angle.
#
  rot = normal_norm * ( \
      np.cos ( angle ) * normal \
    + np.sin ( angle ) * normal2 )
#
#  The rotated vector is the parallel component plus the rotated component.
#
  w = parallel + rot

  return w

def rotation_axis_vector_test ( ):

#*****************************************************************************80
#
## ROTATION_AXIS_VECTOR_TEST tests ROTATION_AXIS_VECTOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 July 2019=8
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from degrees_to_radians import degrees_to_radians
  from r8vec_print import r8vec_print

  angle = 1.159804
  axis = np.array ( [ 0.2361737, -0.8814124, -0.4090649 ] )
  v = np.array ( [ 1.0, 4.0, 10.0 ] )

  print ( '' )
  print ( 'ROTATION_AXIS_VECTOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROTATION_AXIS_VECTOR applies an axis' )
  print ( '  rotation to a vector' )

  r8vec_print ( 3, v, '  The vector:' )

  r8vec_print ( 3, axis, '  The rotation axis:' )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  w = rotation_axis_vector ( axis, angle, v )

  r8vec_print ( 3, w, '  The rotated vector:' )
#
#  Another test of ROTATION_AXIS_VECTOR with an axis vector
#  that does not have unit length.
#
  v = np.array ( [ 1.0, 1.0, 1.0 ] )

  r8vec_print ( 3, v, '  The vector:' )

  axis = np.array ( [ 0.0, 0.0, 2.0 ] )

  r8vec_print ( 3, axis, '  The rotation axis:' )

  angle = 90.0
  angle = degrees_to_radians ( angle )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  w = rotation_axis_vector ( axis, angle, v )

  r8vec_print ( 3, w, '  The rotated vector:' )

#
#  Terminate.
#
  print ( '' )
  print ( 'ROTATION_AXIS_VECTOR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rotation_axis_vector_test ( )
  timestamp ( )


