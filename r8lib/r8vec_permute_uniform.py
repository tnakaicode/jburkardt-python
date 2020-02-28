#! /usr/bin/env python
#
def r8vec_permute_uniform ( n, a, seed ):

#*****************************************************************************80
#
## R8VEC_PERMUTE_UNIFORM randomly permutes an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects.
#
#    Input, real A(N), the array to be permuted.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real A(N), the permuted array.
#
#    Output, integer SEED, a seed for the random number generator.
#
  from r8vec_permute import r8vec_permute
  from perm0_uniform import perm0_uniform

  p, seed = perm0_uniform ( n, seed )

  a = r8vec_permute ( n, p, a )

  return a, seed

def r8vec_permute_uniform_test ( ):

#*****************************************************************************80
#
## R8VEC_PERMUTE_UNIFORM_TEST tests R8VEC_PERMUTE_UNIFORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  n = 12
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_PERMUTE_UNIFORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PERMUTE_UNIFORM randomly reorders an R8VEC.' )

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = 101 + i

  r8vec_print ( n, a, '  A, before rearrangement:' )

  a, seed = r8vec_permute_uniform ( n, a, seed )

  r8vec_print ( n, a, '  A, after rearrangement:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PERMUTE_UNIFORM_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_permute_uniform_test ( )
  timestamp ( )
