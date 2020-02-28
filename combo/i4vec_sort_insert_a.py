#! /usr/bin/env python
#
def i4vec_sort_insert_a ( n, a ):

#*****************************************************************************80
#
## I4VEC_SORT_INSERT_A uses an ascending insertion sort on an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher and Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998, page 11.
#
#  Parameters:
#
#    Input, integer N, the number of items in the vector.
#    N must be positive.
#
#    Input, integer A(N), the array to be sorted.
#
#    Output, integer A(N), the sorted array.
#
  for i in range ( 1, n ):

    x = a[i]

    j = i - 1

    while ( 0 <= j ):

      if ( a[j] <= x ):
        break

      a[j+1] = a[j]
      j = j - 1

    a[j+1] = x

  return a

def i4vec_sort_insert_a_test (  ):

#*****************************************************************************80
#
## I4VEC_SORT_INSERT_A_TEST tests I4VEC_SORT_INSERT_A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 November 2015
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
  print ( 'I4VEC_SORT_INSERT_A_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_SORT_INSERT_A sorts an integer array.' )

  seed = 123456789
  b = 0
  c = n

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  Unsorted array:' )

  a = i4vec_sort_insert_a ( n, a )

  i4vec_print ( n, a, '  Sorted array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_SORT_INSERT_A_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_sort_insert_a_test ( )
  timestamp ( )

