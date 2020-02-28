#! /usr/bin/env python
#
def rotation_mat_vector ( a, v ):

#*****************************************************************************80
#
## ROTATION_MAT_VECTOR applies a marix rotation to a vector in 3d.
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
#    Input, real A(3,3), the matrix defining the rotation.
#
#    Input, real V(3,1), the vector to be rotated.
#
#    Output, real W(3), the rotated vector.
#  
  import numpy as np

  w = np.dot ( a, v )

  return w

def rotation_mat_vector_test ( ):

#*****************************************************************************80
#
## ROTATION_MAT_VECTOR_TEST tests ROTATION_MAT_VECTOR.
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

  print ( '' )
  print ( 'ROTATION_MAT_VECTOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROTATION_MAT_VECTOR applies a matrix' )
  print ( '  rotation to a vector.' )
 
  a = np.array ( [ \
  [  0.43301269,  0.25,       -0.86602539 ], \
  [ -0.5,         0.86602539,  0.0 ], \
  [  0.75,        0.43301269,  0.5 ] ] )

  r8mat_print ( 3, 3, a, '  The rotation matrix:' )

  v = np.array ( [ 1.0, 4.0, 10.0 ] )
  r8vec_print ( 3, v, '  The vector V:' )

  w = rotation_mat_vector ( a, v )
  r8vec_print ( 3, w, '  The rotated vector W = A * V:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROTATION_MAT_VECTOR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rotation_mat_vector_test ( )
  timestamp ( )

