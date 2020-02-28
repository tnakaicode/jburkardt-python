#! /usr/bin/env python
#
def i4vec_choose ( m, n, k ):

#*****************************************************************************80
#
## I4VEC_CHOOSE computes the generalized binomial coefficient C(M,N,K).
#
#  Discussion:
#
#    C(M,N,K) = product ( 1 <= I <= M ) C(N,K)
#
#    where:
#
#      C(N,K) = N! / ( K! * (N-K)! )
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
#    Input, integer M, the spatial dimension.
#
#    Input, integer N(M), K(M), the parameters for each dimension.
#
#    Output, integer I4VEC_CHOOSE, the generalized binomial coefficient.
#
  from i4_choose import i4_choose

  value = 1
  for i in range ( 0, m ):
    value = value * i4_choose ( n[i], k[i] )

  return value

def i4vec_choose_test ( ):

#*****************************************************************************80
#
## I4VEC_CHOOSE_TEST tests I4VEC_CHOOSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_choose import i4_choose
  from i4vec_sum_vec import i4vec_sum_vec
  from i4vec_transpose_print import i4vec_transpose_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ( '' )
  print ( 'I4VEC_CHOOSE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_CHOOSE computes the generalized binomial coefficient.' )

  m = 5
  seed = 12345678

  j, seed = i4vec_uniform_ab ( m, 0, 6, seed )
  k, seed = i4vec_uniform_ab ( m, 0, 6, seed )
  n = i4vec_sum_vec ( m, j, k )

  i4vec_transpose_print ( m, n, '  N:' )
  i4vec_transpose_print ( m, k, '  K:' )

  print ( '' )
  print ( '   M        V1        V2' )
  print ( '' )
  v1 = 1
  for mm in range ( 0, m + 1 ):
 
    if ( mm == 0 ):
      v1 = 1
    else:
      v1 = v1 * i4_choose ( n[mm-1], k[mm-1] )
    v2 = i4vec_choose ( mm, n, k )
    print ( '  %2d  %8d  %8d' % ( mm, v1, v2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_CHOOSE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_choose_test ( )
  timestamp ( )

