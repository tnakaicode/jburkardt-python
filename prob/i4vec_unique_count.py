#! /usr/bin/env python
#
def i4vec_unique_count ( n, a ):

#*****************************************************************************80
#
## I4VEC_UNIQUE_COUNT counts the unique elements in an I4VEC.
#
#  Discussion:
#
#    Because the array is sorted, this algorithm is O(N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 April 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements of A.
#
#    Input, integer A(N), the sorted array to examine.
#
#    Output, integer UNIQUE_NUM, the number of unique elements of A.
#
  unique_num = 0

  for i in range ( 0, n ):

    unique_num = unique_num + 1

    for j in range ( 0, i ):
      if ( a[i] == a[j] ):
        unique_num = unique_num - 1
        break

  return unique_num

def i4vec_unique_count_test (  ):

#*****************************************************************************80
#
## I4VEC_UNIQUE_COUNT_TEST tests I4VEC_UNIQUE_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 20
  b = 0
  c = n

  print ( '' )
  print ( 'I4VEC_UNIQUE_COUNT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_UNIQUE_COUNT counts unique entries in an I4VEC.' )

  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  Input vector:' )

  a_unique = i4vec_unique_count ( n, a )

  print ( '' )
  print ( '  Number of unique entries is %d' % ( a_unique ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_UNIQUE_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_unique_count_test ( )
  timestamp ( )

