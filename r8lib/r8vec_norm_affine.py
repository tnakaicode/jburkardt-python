#! /usr/bin/env python
#
def r8vec_norm_affine ( n, v0, v1 ):

#*****************************************************************************80
#
## R8VEC_NORM_AFFINE returns the affine norm of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    The affine vector L2 norm is defined as:
#
#      R8VEC_NORM_AFFINE(V0,V1) 
#        = sqrt ( sum ( 1 <= I <= N ) ( V1(I) - V0(I) )^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 July 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the vector dimnension.
#
#    Input, real V0(N), the base vector.
#
#    Input, real V1(N), the vector.
#
#    Output, real VALUE, the affine L2 norm.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ): 
    value = value + ( v0[i] - v1[i] ) ** 2
  value =  np.sqrt ( value )

  return value

def r8vec_norm_affine_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_AFFINE_TEST tests R8VEC_NORM_AFFINE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_norm import r8vec_norm
  from r8vec_uniform_01 import r8vec_uniform_01

  n = 10

  print ( '' )
  print ( 'R8VEC_NORM_AFFINE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM_AFFINE computes the L2 norm of' )
  print ( '  the difference of two R8VECs.' )

  seed = 123456789;

  x, seed = r8vec_uniform_01 ( n, seed )
  y, seed = r8vec_uniform_01 ( n, seed )
  z = np.zeros ( n )
  for i in range ( 0, n ):
    z[i] = x[i] - y[i]

  print ( '' )
  print ( '  R8VEC_NORM_AFFINE(X,Y) = %g' % ( r8vec_norm_affine ( n, x, y ) ) )
  print ( '  R8VEC_NORM (X-Y):        %g' % ( r8vec_norm ( n, z ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_AFFINE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_norm_affine_test ( )
  timestamp ( )
 
