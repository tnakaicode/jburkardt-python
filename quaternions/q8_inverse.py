#! /usr/bin/env python3
#
def q8_inverse ( q ):

#*****************************************************************************80
#
## Q8_INVERSE returns the inverse of a quaternion.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#
#    The inverse of Q is
#
#      inverse ( Q ) = conjugate ( Q ) / ( norm ( Q ) )^2.
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
#    Input, real Q(4), the quaternion to be inverted.
#
#    Output, real Q2(4), the inverse of the input quaternion.
#
  import numpy as np

  q2 = q.copy ( );
  q_norm_sq = np.sum ( q[0:4] ** 2 )
  q2[0:4] = q2[0:4] / q_norm_sq
  q2[1:4] = - q2[1:4]

  return q2

def q8_inverse_test ( ):

#*****************************************************************************80
#
## Q8_INVERSE_TEST tests Q8_INVERSE.
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
  from q8_multiply import q8_multiply
  from q8_normal_01 import q8_normal_01
  from q8_transpose_print import q8_transpose_print

  seed = 123456789

  print ( '' )
  print ( 'Q8_INVERSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Q8_INVERSE inverts a quaternion' )

  for i in range ( 0, 5 ):

    q1, seed = q8_normal_01 ( seed )
    q2 = q8_inverse ( q1 )
    q3 = q8_multiply ( q1, q2 )

    print ( '' )
    q8_transpose_print ( q1, '  q1 = q8_normal_01 ( seed ):' )
    q8_transpose_print ( q2, '  q2 = q8_inverse ( q1 ):    ' ) 
    q8_transpose_print ( q3, '  q3 = q8_multiply ( q1, q2 ):    ' )
     
#
#  Terminate.
#
  print ( '' )
  print ( 'Q8_INVERSE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  q8_inverse_test ( )
  timestamp ( )

