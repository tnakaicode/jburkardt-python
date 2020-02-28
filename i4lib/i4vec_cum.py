#! /usr/bin/env python
#
def i4vec_cum ( n, a ):

#*****************************************************************************80
#
## I4VEC_CUM computes the cumulative sum of the entries of an I4VEC.
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
#      A_CUM = (/ 1, 3, 6, 10 /)
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
#    Output, integer A_CUM(0:N-1), the cumulative sum of the entries of A.
#
  import numpy as np

  a_cum = np.zeros ( n, dtype = np.int32 )

  a_cum[0] = a[0]

  for i in range ( 1, n ):
    a_cum[i] = a_cum[i-1] + a[i]

  return a_cum

def i4vec_cum_test ( ):

#*****************************************************************************80
#
## I4VEC_CUM_TEST tests I4VEC_CUM.
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
  print ( 'I4VEC_CUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_CUM:  cumulative sum of I4VEC entries;' )

  seed = 123456789
  b = 0
  c = n

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  Input vector:' )

  a_cum = i4vec_cum ( n, a )

  i4vec_print ( n, a_cum, '  Cumulative sums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_CUM_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_cum_test ( )
  timestamp ( )
 
