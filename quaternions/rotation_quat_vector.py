#! /usr/bin/env python
#
def rotation_quat_vector ( q, v ):

#*****************************************************************************80
#
## ROTATION_QUAT_VECTOR applies a quaternion rotation to a vector in 3D.
#
#  Discussion:
#
#    If Q is a unit quaternion that encodes a rotation of ANGLE
#    radians about the vector AXIS, then for an arbitrary real
#    vector V, the result W of the rotation on V can be written as:
#
#      W = Q * V * Conj(Q)
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
#    Input, real Q[3], the quaternion defining the rotation.
#
#    Input, real V[2], the vector to be rotated.
#
#    Output, real W[2], the rotated vector.
#
  import numpy as np

  w = np.zeros ( 3 )

  w[0] = \
         ( 2.0 * ( q[0] * q[0] + q[1] * q[1] ) - 1.0 ) * v[0] \
       +   2.0 * ( q[1] * q[2] - q[0] * q[3] )         * v[1] \
       +   2.0 * ( q[1] * q[3] + q[0] * q[2] )         * v[2]

  w[1] = \
           2.0 * ( q[1] * q[2] + q[0] * q[3] )         * v[0] \
       + ( 2.0 * ( q[0] * q[0] + q[2] * q[2] ) - 1.0 ) * v[1] \
       +   2.0 * ( q[2] * q[3] - q[0] * q[1] )         * v[2]

  w[2] = \
           2.0 * ( q[1] * q[3] - q[0] * q[2] )         * v[0] \
       +   2.0 * ( q[2] * q[3] + q[0] * q[1] )         * v[1] \
       + ( 2.0 * ( q[0] * q[0] + q[3] * q[3] ) - 1.0 ) * v[2]

  return w

def rotation_quat_vector_test ( ):

#*****************************************************************************80
#
## ROTATION_QUAT_VECTOR_TEST tests ROTATION_QUAT_VECTOR.
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
  import platform
  import numpy as np
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'ROTATION_QUAT_VECTOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROTATION_QUAT_VECTOR applies a quaternion' )
  print ( '  rotation to a vector.' )

  q = np.array ( [ 0.836516, 0.12941, -0.482963, -0.224144 ] )
  r8vec_print ( 4, q, '  The rotation quaternion:' )

  v = np.array ( [ 1.0, 4.0, 10.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  w = rotation_quat_vector ( q, v )
  r8vec_print ( 3, w, '  The rotated vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROTATION_QUAT_VECTOR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rotation_quat_vector_test ( )
  timestamp ( )

