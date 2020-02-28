#! /usr/bin/env python
#
def r8vec_amin_index ( n, a ):

#*****************************************************************************80
#
## R8VEC_AMIN_INDEX returns the index of the minimum absolute value in an R8VEC.
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
#    13 August 2017
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
#
#    Output, integer VALUE_INDEX, the (0-based) index of the minimum absolute 
#    value in the vector.
#
  import numpy as np

  value_min = np.inf
  value_index = -1

  for i in range ( 0, n ):
    if ( abs ( a[i] ) < value_min ):
      value_min = abs ( a[i] )
      value_index = i

  return value_index

def r8vec_amin_index_test ( ):

#*****************************************************************************80
#
## R8VEC_AMIN_INDEX_TEST tests R8VEC_AMIN_INDEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'R8VEC_AMIN_INDEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_AMIN_INDEX computes the index of the entry of' )
  print ( '  minimum absolute value in an R8VEC.' )

  n = 10
  a_lo = - 10.0
  a_hi = + 10.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value_index = r8vec_amin_index ( n, a )
  value_min = a[value_index]

  print ( '' )
  print ( '  AMIN = A[%d] = %g' % ( value_index, value_min ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_AMIN_INDEX_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_amin_index_test ( )
  timestamp ( )

