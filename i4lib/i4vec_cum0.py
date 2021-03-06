#! /usr/bin/env python
#
def i4vec_cum0 ( n, a ):

#*****************************************************************************80
#
## I4VEC_CUM0 computes the zero-based cumulative sum of the entries of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Example:
#
#    Input:
#
#      A = (/ 1, 2, 3, 4 /)
#
#    Output:
#
#      A_CUM0 = (/ 0, 1, 3, 6, 10 /)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2010
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A(N), the vector to be summed.
#
#    Output, integer A_CUM(0:N), the cumulative sum of the entries of A.
#
  import numpy as np

  a_cum = np.zeros ( n + 1, dtype = np.int32 )

  a_cum[0] = 0.0

  for i in range ( 0, n ):
    a_cum[i+1] = a_cum[i] + a[i]

  return a_cum

def i4vec_cum0_test ( ):

#*****************************************************************************80
#
## I4VEC_CUM0_TEST tests I4VEC_CUM0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 November 2014
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 10

  print ( '' )
  print ( 'I4VEC_CUM0_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_CUM0:  zero-based cumulative sum of I4VEC entries;' )

  seed = 123456789
  b = 0
  c = n

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  Input vector:' )

  a_cum = i4vec_cum0 ( n, a )

  i4vec_print ( n + 1, a_cum, '  Cumulative sums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_CUM0_TEST' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_cum0_test ( )
  timestamp ( )
