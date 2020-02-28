#! /usr/bin/env python
#
def i4vec_max_index_last ( n, a ):

#*****************************************************************************80
#
## I4VEC_MAX_INDEX returns the index of the last largest entry in an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of integer values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A(N), the vector to be searched.
#
#    Output, integer MAX_INDEX_LAST, the index of the last largest entry.
#
  if ( n <= 0 ):

    max_index_last = -1

  else:

    amax = a[0]
    max_index_last = 0

    for i in range ( 1, n ):

      if ( amax <= a[i] ):
        amax = a[i]
        max_index_last = i

  return max_index_last

def i4vec_max_index_last_test ( ):

#*****************************************************************************80
#
## I4VEC_MAX_INDEX_LAST_TEST tests I4VEC_MAX_INDEX_LAST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 15

  print ( '' )
  print ( 'I4VEC_MAX_INDEX_LAST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_MAX_INDEX_LAST:     last maximal index' )

  seed = 123456789
  i4_lo = 0
  i4_hi = + ( n // 4 )

  a, seed = i4vec_uniform_ab ( n, i4_lo, i4_hi, seed )

  i4vec_print ( n, a, '  Input vector:' )

  print ( '' )

  ival = i4vec_max_index_last ( n, a )
  print ( '  Last maximum index: %d' % ( ival ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_MAX_INDEX_LAST_TEST:' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_max_index_last_test ( )
  timestamp ( )

