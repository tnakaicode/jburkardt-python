#! /usr/bin/env python
#
def i4vec_sum_vec ( n, a, b ):

#*****************************************************************************80
#
## I4VEC_SUM_VEC does a pairwise sum of two I4VEC's.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Example:
#
#    Input:
#
#      A = ( 1, 2, 3, 4 )
#      B = ( 5, 6, 7, 8 )
#
#    Output:
#
#      C = ( 6, 8, 10, 12 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A(N), B(N), the vectors to be summed.
#
#    Output, integer C(N), the pairwise sum of A and B.
#
  import numpy as np

  c = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    c[i] = a[i] + b[i]

  return c

def i4vec_sum_vec_test ( ):

#*****************************************************************************80
#
## I4VEC_SUM_VEC_TEST tests I4VEC_SUM_VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_transpose_print import i4vec_transpose_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ( '' )
  print ( 'I4VEC_SUM_VEC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_SUM_VEC sums the entries in an I4VEC.' )

  n = 5
  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, 0, 10, seed )
  i4vec_transpose_print ( n, a, '  A:' );

  b, seed = i4vec_uniform_ab ( n, 0, 10, seed )
  i4vec_transpose_print ( n, b, '  B:' )

  c = i4vec_sum_vec ( n, a, b )
  i4vec_transpose_print ( n, c, '  C = A + B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_SUM_VEC_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_sum_vec_test ( )
  timestamp ( )

