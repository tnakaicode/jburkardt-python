#! /usr/bin/env python
#
def r8vec_diff_norm ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_DIFF_NORM returns the L2 norm of the difference of R8VEC's.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), B(N), the vectors.
#
#    Output, real VALUE, the L2 norm of A - B.
#
  import numpy as np

  value = np.sqrt ( np.sum ( ( a[0:n] - b[0:n] ) ** 2 ) )

  return value

def r8vec_diff_norm_test ( ):

#*****************************************************************************80
#
## R8VEC_DIFF_NORM_TEST tests R8VEC_DIFF_NORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_DIFF_NORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_DIFF_NORM: L2 norm of the difference of two R8VECs.' )

  n = 6
  v = np.array ( [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0 ], dtype = np.float64 )
  w = np.array ( [ 1.0, 2.0, 3.0, 5.0, 5.0, 6.0 ], dtype = np.float64 )
  
  print ( '' )
  print ( '  I    V[I]  W[I]' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '%2d  %f  %f' % ( i, v[i], w[i] ) )

  d = r8vec_diff_norm ( n, v, w )

  print ( '' )
  print ( '  L2 norm of vector difference ||V-W|| is %g' % ( d ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_DIFF_NORM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_diff_norm_test ( )
  timestamp ( )

