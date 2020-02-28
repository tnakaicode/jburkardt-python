#! /usr/bin/env python
#
def r8vec_uniform_unit ( m, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_UNIT generates a random unit vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the dimension of the space.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real W(M), a random direction vector,
#    with unit norm.
#
#    Output, integer SEED, a seed for the random number generator.
#
  from r8vec_norm import r8vec_norm
  from r8vec_normal_01 import r8vec_normal_01
#
#  Get N values from a standard normal distribution.
#
  w, seed = r8vec_normal_01 ( m, seed )
#
#  Compute the length of the vector.
#
  norm = r8vec_norm ( m, w )
#
#  Normalize the vector.
#
  for i in range ( 0, m ):
    w[i] = w[i] / norm

  return w, seed

def r8vec_uniform_unit_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_UNIT_TEST tests R8VEC_UNIFORM_UNIT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print

  m = 5

  print ( '' )
  print ( 'R8VEC_UNIFORM_UNIT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_UNIT returns a random R8VEC' )
  print ( '  on the surface of the unit M sphere.' )
  print ( '' )

  seed = 123456789

  for j in range ( 0, 5 ):

    x, seed = r8vec_uniform_unit ( m, seed )

    r8vec_print ( m, x, '  Vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_UNIT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_uniform_unit_test ( )
  timestamp ( )
