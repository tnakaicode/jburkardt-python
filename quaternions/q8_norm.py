#! /usr/bin/env python3
#
def q8_norm ( q ):

#*****************************************************************************80
#
## Q8_NORM computes the norm of a quaternion.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#
#    The norm of Q is
#
#      norm(Q) = sqrt ( A^2 + B^2 + C^2 + D^2 ).
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
#    Input, real Q(4), the quaternion.
#
#    Output, real VALUE, the norm of the quaternion.
#
  import numpy as np

  value = np.sqrt ( np.sum ( q[0:4] ** 2 ) )

  return value

def q8_norm_test ( ):

#*****************************************************************************80
#
## Q8_NORM_TEST tests Q8_NORM.
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
  from q8_normal_01 import q8_normal_01
  from q8_transpose_print import q8_transpose_print

  seed = 123456789

  print ( '' )
  print ( 'Q8_NORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Q8_NORM computes the norm of a quaternion.' )

  for i in range ( 0, 5 ):
    print ( '' )
    q, seed = q8_normal_01 ( seed )
    label = '  q = q8_normal_01(seed):'
    q8_transpose_print ( q, label )
    value = q8_norm ( q )
    print ( '  q8_norm(q) = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'Q8_NORM_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  q8_norm_test ( )
  timestamp ( )

