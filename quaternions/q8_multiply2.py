#! /usr/bin/env python3
#
def q8_multiply2 ( q1, q2 ):

#*****************************************************************************80
#
## Q8_MULTIPLY2 multiplies two quaternions using a matrix format.
#
#  Discussion:
#
#    A quaternion is a quadruplet (A,B,C,D) of real numbers, which
#    may be written as
#
#      Q = A + Bi + Cj + Dk.
#
#    To multiply two quaternions, use the relationships:
#
#      i * j = -j * i = k
#      j * k = -k * j = i
#      k * i = -i * k = j
#      i * i =  j * j = k * k = -1
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
#  Parameters:
#
#    Input, real Q1[3], Q2[3], the two quaternions to be multiplied.
#
#    Output, real Q3[3], the product of the two quaternions.
#
  import numpy as np

  qm = np.array ( [ \
    [ q1[0], -q1[1], -q1[2], -q1[3] ], \
    [ q1[1], +q1[0], -q1[3], +q1[2] ], \
    [ q1[2], +q1[3], +q1[0], -q1[1] ], \
    [ q1[3], -q1[2], +q1[1], +q1[0] ] ] )

  q3 = np.dot ( qm, q2 )
  
  return q3

def q8_multiply2_test ( ):

#*****************************************************************************80
#
## Q8_MULTIPLY2_TEST tests Q8_MULTIPLY2.
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
  print ( 'Q8_MULTIPLY2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Q8_MULTIPLY2 multiplies two quaternions using a matrix' )

  for i in range ( 0, 5 ):

    q1, seed = q8_normal_01 ( seed )
    q2, seed = q8_normal_01 ( seed )
    q3 = q8_multiply2 ( q1, q2 )

    print ( '' )
    q8_transpose_print ( q1, '  q1 = q8_normal_01 ( seed )  :' )
    q8_transpose_print ( q2, '  q2 = q8_normal_01 ( seed )  :' )
    q8_transpose_print ( q3, '  q3 = q8_multiply2 ( q1, q2 ):' )  
#
#  Terminate.
#
  print ( '' )
  print ( 'Q8_MULTIPLY2_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  q8_multiply2_test ( )
  timestamp ( )


