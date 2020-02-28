#! /usr/bin/env python
#
def r8vec_mean_geometric ( n, a ):

#*****************************************************************************80
#
## R8VEC_MEAN_GEOMETRIC returns the geometric mean of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#    All entries should be nonnegative.
#
#    Output, real VALUE, the geometric mean of the vector.
#
  import numpy as np

  value = np.exp ( np.sum ( np.log ( a[0:n] ) ) / float ( n ) );

  return value

def r8vec_mean_geometric_test ( ):

#*****************************************************************************80
#
## R8VEC_MEAN_GEOMETRIC_TEST tests R8VEC_MEAN_GEOMETRIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 December 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'R8VEC_MEAN_GEOMETRIC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MEAN_GEOMETRIC computes the geometric mean of an R8VEC.' )

  n = 10
  r8_lo = 0.0
  r8_hi = 5.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_mean_geometric ( n, a )
  print ( '' )
  print ( '  Geometric mean = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MEAN_GEOMETRIC_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_mean_geometric_test ( )
  timestamp ( )

