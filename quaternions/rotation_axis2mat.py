#! /usr/bin/env python
#
def rotation_axis2mat ( axis, angle ):

#*****************************************************************************80
#
## ROTATION_AXIS2MAT converts a rotation from axis to matrix format in 3D.
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
#    Input, real AXIS[3], the axis vector which remains 
#    unchanged by the rotation.
#
#    Input, real ANGLE, the angular measurement of the
#    rotation about the axis, in radians.
#
#    Output, real A[3,3], the rotation matrix.
#
  import numpy as np

  a = np.zeros ( [ 3, 3 ] )

  axis_norm = np.linalg.norm ( axis )
  if ( axis_norm == 0.0 ):
    return a

  axis[0:3] = axis[0:3] / axis_norm

  ca = np.cos ( angle )
  sa = np.sin ( angle )

  a[0,0] =                axis[0] * axis[0] + ca * ( 1.0 - axis[0] * axis[0] )
  a[0,1] = ( 1.0 - ca ) * axis[0] * axis[1] - sa * axis[2]
  a[0,2] = ( 1.0 - ca ) * axis[0] * axis[2] + sa * axis[1]

  a[1,0] = ( 1.0 - ca ) * axis[1] * axis[0] + sa * axis[2]
  a[1,1] =                axis[1] * axis[1] + ca * ( 1.0 - axis[1] * axis[1] )
  a[1,2] = ( 1.0 - ca ) * axis[1] * axis[2] - sa * axis[0]

  a[2,0] = ( 1.0 - ca ) * axis[2] * axis[0] - sa * axis[1]
  a[2,1] = ( 1.0 - ca ) * axis[2] * axis[1] + sa * axis[0]
  a[2,2] =                axis[2] * axis[2] + ca * ( 1.0 - axis[2] * axis[2] )

  return a

def rotation_axis2mat_test ( ):

#*****************************************************************************80
#
## ROTATION_AXIS2MAT_TEST tests ROTATION_AXIS2MAT.
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
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'ROTATION_AXIS2MAT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROTATION_AXIS2MAT converts a rotation axis to a matrix.' )

  v = np.array ( [ 1.0, 4.0, 10.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  axis = np.array ( [ 0.2361737, -0.8814124, -0.4090649 ] )
  r8vec_print ( 3, axis, '  The rotation axis:' )

  angle = 1.159804
  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  a = rotation_axis2mat ( axis, angle )

  r8mat_print ( 3, 3, a, '  The rotation matrix A:' )

  w = np.dot ( a, v )

  r8vec_print ( 3, w, '  The rotated vector W = A * V:' )
#
#  Test an axis vector that does not have unit length.
#
  v = np.array ( [ 1.0, 1.0, 1.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  axis = np.array ( [ 0.0, 0.0, 2.0 ] )
  r8vec_print ( 3, axis, '  The rotation axis:' )

  angle = 90.0
  angle = degrees_to_radians ( angle )

  print ( '' )
  print ( '  The rotation angle is %f' % ( angle ) )

  a = rotation_axis2mat ( axis, angle )

  r8mat_print ( 3, 3, a, '  The rotation matrix A:' )

  w = np.dot ( a, v )

  r8vec_print ( 3, w, '  The rotated vector W = A * V:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROTATION_AXIS2MAT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rotation_axis2mat_test ( )
  timestamp ( )


