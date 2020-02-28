#! /usr/bin/env python
#
def r8vec_covariance ( n, x, y ):

#*****************************************************************************80
#
## R8VEC_COVARIANCE computes the covariance of two vectors.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer N, the dimension of the two vectors.
#
#    Input, real X(N), Y(N), the two vectors.
#
#    Output, real VALUE, the covariance of the two vectors.
#
  import numpy as np

  x_average = np.mean ( x[0:n] )
  y_average = np.mean ( y[0:n] )
  
  value = 0.0
  for i in range ( 0, n ):
    value = value + ( x[i] - x_average ) * ( y[i] - y_average )

  value = value / float ( n - 1 )

  return value

def r8vec_covariance_test ( ):

#*****************************************************************************80
#
## R8VEC_COVARIANCE_TEST tests R8VEC_COVARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8_uni_01 import r8_uni_01

  print ( '' )
  print ( 'R8VEC_COVARIANCE_TEST:' )
  print ( '  R8VEC_COVARIANCE computes the covariance of two R8VECs.' )

  n = 2

  v1 = np.array ( [ 1.0, 0.0 ] )
  print ( '' )
  print ( '  Vector V1:' ),
  for i in range ( 0, n ):
    print ( '%g' % ( v1[i] ) ),
  print ( '' )

  for i in range ( 0, 12 ):
    angle = float ( 2 * i ) * np.pi / 12.0
    r = r8_uni_01 ( )
    v2 = r * np.array ( [ np.cos(angle), np.sin(angle) ] )
    print ( '' )
    print ( '  Vector V2:' ),
    for i in range ( 0, n ):
      print ( '%g' % ( v2[i] ) ),
    print ( '' )
    value = r8vec_covariance ( n, v1, v2 )
    print ( '  Covariance(V1,V2) = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_COVARIANCE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_covariance_test ( )
  timestamp ( )

