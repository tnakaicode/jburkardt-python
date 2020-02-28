#! /usr/bin/env python3
#
def quaternions_test ( ):

#*****************************************************************************80
#
## QUATERNIONS_TEST tests the QUATERNIONS library.
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

  from degrees_to_radians import degrees_to_radians_test

  from q8_conjugate import q8_conjugate_test
  from q8_exponentiate import q8_exponentiate_test
  from q8_inverse import q8_inverse_test
  from q8_multiply import q8_multiply_test
  from q8_multiply2 import q8_multiply2_test
  from q8_norm import q8_norm_test
  from q8_normal_01 import q8_normal_01_test
  from q8_transpose_print import q8_transpose_print_test

  from r8_acos import r8_acos_test

  from r8vec_uniform_01 import r8vec_uniform_01_test

  from radians_to_degrees import radians_to_degrees_test

  from rotation_axis_vector import rotation_axis_vector_test
  from rotation_axis2mat import rotation_axis2mat_test
  from rotation_axis2quat import rotation_axis2quat_test

  from rotation_mat_vector import rotation_mat_vector_test
  from rotation_mat2axis import rotation_mat2axis_test
  from rotation_mat2quat import rotation_mat2quat_test

  from rotation_quat_vector import rotation_quat_vector_test
  from rotation_quat2axis import rotation_quat2axis_test
  from rotation_quat2mat import rotation_quat2mat_test

  print ( '' )
  print ( 'QUATERNIONS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the QUATERNIONS library.' )

  degrees_to_radians_test ( )

  q8_conjugate_test ( )
  q8_exponentiate_test ( )
  q8_inverse_test ( )
  q8_multiply_test ( )
  q8_multiply2_test ( )
  q8_norm_test ( )
  q8_normal_01_test ( )
  q8_transpose_print_test ( )

  r8_acos_test ( )

  r8vec_uniform_01_test ( )

  radians_to_degrees_test ( )

  rotation_axis_vector_test ( )
  rotation_axis2mat_test ( )
  rotation_axis2quat_test ( )

  rotation_mat_vector_test ( )
  rotation_mat2axis_test ( )
  rotation_mat2quat_test ( )

  rotation_quat_vector_test ( )
  rotation_quat2axis_test ( )
  rotation_quat2mat_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'QUATERNIONS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  quaternions_test ( )
  timestamp ( )

