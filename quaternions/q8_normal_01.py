#! /usr/bin/env python3
#
def q8_normal_01 ( seed ):

#*****************************************************************************80
#
## Q8_NORMAL_01 returns a normally distributed quaternion.
#
#  Discussion:
#
#    The normal distribution with mean 0 and variance 1 is used.
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
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real Q(4), the sampled quaternion.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8vec_uniform_01 import r8vec_uniform_01

  q = np.zeros ( 4 )

  r, seed = r8vec_uniform_01 ( 4, seed )

  q[0:3:2] = \
    np.sqrt ( -2.0 * np.log ( r[0:3:2] ) ) * np.cos ( 2.0 * np.pi * r[1:4:2] )

  q[1:4:2] = \
    np.sqrt ( -2.0 * np.log ( r[0:3:2] ) ) * np.sin ( 2.0 * np.pi * r[1:4:2] )

  return q, seed

def q8_normal_01_test ( ):

#*****************************************************************************80
#
## Q8_NORMAL_01_TEST tests Q8_NORMAL_01.
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
  from q8_transpose_print import q8_transpose_print

  seed = 123456789

  print ( '' )
  print ( 'Q8_NORMAL_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Q8_NORMAL_01 computes a normally distributed quaternion.' )
  print ( '' )

  for i in range ( 0, 5 ):
    q, seed = q8_normal_01 ( seed )
    label = ( '  Sample #%d' % ( i ) )
    q8_transpose_print ( q, label )
#
#  Terminate.
#
  print ( '' )
  print ( 'Q8_NORMAL_01_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  q8_normal_01_test ( )
  timestamp ( )

