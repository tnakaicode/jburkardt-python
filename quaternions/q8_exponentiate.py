#! /usr/bin/env python3
#
def q8_exponentiate ( q1 ):

#*****************************************************************************80
#
## Q8_EXPONENTIATE exponentiates a quaternion.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#    
#    The exponential of Q can be set by
#      V = sqrt ( B^2 + C^2 + D^2 )
#      e^Q = e^A * ( cos ( ||V|| ) + V/||V|| sin ||V|| )
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
#    Input, real Q1(4), the quaternions to exponentiate.
#
#    Output, real Q2(4), the exponential of the quaternion.
#
  import numpy as np

  vnorm = np.sqrt ( np.sum ( q1[1:4] ** 2 ) )

  q2 = np.zeros ( 4 )

  q2[0] = np.cos ( vnorm )
  if ( vnorm != 0.0 ):
    q2[1:4] = np.sin ( vnorm ) * q1[1:4] / vnorm

  q2[0:4] = np.exp ( q1[0] ) * q2[0:4]

  return q2

def q8_exponentiate_test ( ):

#*****************************************************************************80
#
## Q8_EXPONENTIATE_TEST tests Q8_EXPONENTIATE.
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
  print ( 'Q8_EXPONENTIATE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Q8_EXPONENTIATE exponentiates a quaternion' )

  for i in range ( 0, 5 ):

    q1, seed = q8_normal_01 ( seed )
    q2 = q8_exponentiate ( q1 )

    print ( '' )
    q8_transpose_print ( q1, '  q1 = q8_normal_01 ( seed ):' )
    q8_transpose_print ( q2, '  q2 = q8_exponentiate ( q1 ):' )  
#
#  Terminate.
#
  print ( '' )
  print ( 'Q8_EXPONENTIATE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  q8_exponentiate_test ( )
  timestamp ( )

