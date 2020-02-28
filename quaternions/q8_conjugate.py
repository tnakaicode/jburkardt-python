#! /usr/bin/env python3
#
def q8_conjugate ( q ):

#*****************************************************************************80
#
## Q8_CONJUGATE conjugates a quaternion.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#
#    The conjugate of Q is
#
#      conj ( Q ) = A - Bi - Cj - Dk.
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
#    Input, real Q(4), the quaternion to be conjugated.
#
#    Output, real Q2(4), the conjugated quaternion.
#
  import numpy as np

  q2 = np.zeros ( 4 )

  q2[0]   =   q[0]
  q2[1:4] = - q[1:4]

  return q2

def q8_conjugate_test ( ):

#*****************************************************************************80
#
## Q8_CONJUGATE_TEST tests Q8_CONJUGATE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 July 2018
#
#  Author:
#
#    John Burkardt
#
  import platform
  from q8_normal_01 import q8_normal_01
  from q8_transpose_print import q8_transpose_print

  seed = 123456789

  print ( '' )
  print ( 'Q8_CONJUGATE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Q8_CONJUGATE conjugates a quaternion' )

  for i in range ( 0, 5 ):

    q1, seed = q8_normal_01 ( seed )
    q2 = q8_conjugate ( q1 )

    print ( '' )
    q8_transpose_print ( q1, '  q1 = q8_normal_01 ( seed ):' )
    q8_transpose_print ( q2, '  q2 = q8_conjugate ( q1 ):  ' )  
#
#  Terminate.
#
  print ( '' )
  print ( 'Q8_CONJUGATE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  q8_conjugate_test ( )
  timestamp ( )


