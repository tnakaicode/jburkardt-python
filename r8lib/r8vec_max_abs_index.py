#! /usr/bin/env python
#
def r8vec_max_abs_index ( n, a ):

#*****************************************************************************80
#
## R8VEC_MAX_ABS_INDEX: index of entry of maximum absolute value in an R8VEC.
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
#    Input, integer N, the number of entries in the array.
#
#    Input, real A(N), the array.
#
#    Output, integer MAX_ABS_INDEX, the index of the entry of maximum
#    absolute value.
#
  if ( n <= 0 ):

    max_abs_index = -1

  else:

    max_abs_index = 0

    for i in range ( 1, n ):
      if ( abs ( a[max_abs_index] ) < abs ( a[i] ) ):
        max_abs_index = i

  return max_abs_index

def r8vec_max_abs_index_test ( ):

#*****************************************************************************80
#
## R8VEC_MAX_ABS_INDEX_TEST tests R8VEC_MAX_ABS_INDEX.
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
  from r8vec_uniform_ab import r8vec_uniform_ab

  n = 10
 
  print ( '' )
  print ( 'R8VEC_MAX_ABS_INDEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MAX_ABS_INDEX: index of entry of maximum absolute value' )
 
  r8_lo = - 10.0
  r8_hi = + 10.0

  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
 
  r8vec_print ( n, a, '  Input vector:' )

  ival = r8vec_max_abs_index ( n, a )

  print ( '' )
  print ( '  Maximum index: %d' % ( ival ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MAX_ABS_INDEX_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_max_abs_index_test ( )
  timestamp ( )

