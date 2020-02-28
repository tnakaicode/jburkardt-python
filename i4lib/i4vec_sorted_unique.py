#! /usr/bin/env python
#
def i4vec_sorted_unique ( n, a ):

#*****************************************************************************80
#
## I4VEC_SORTED_UNIQUE finds the unique elements in a sorted I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements in A.
#
#    Input, integer A(N), the sorted integer array.
#
#    Output, integer N_UNIQUE, the number of unique elements in A.
#
#    Output, integer A_UNIQUE[N_UNIQUE], the unique elements.
#
  import numpy as np
  from i4vec_sorted_unique_count import i4vec_sorted_unique_count

  if ( n <= 0 ):
    n_unique = 0
    a_unique = np.zeros ( 0 )
    return n_unique, a_unique

  n_unique = i4vec_sorted_unique_count ( n, a )

  a_unique = np.zeros ( n_unique, dtype = np.int32 )

  k = 0
  a_unique[0] = a[0];

  for i in range ( 1, n ):

    if ( a[i] != a_unique[k] ):
      k = k + 1
      a_unique[k] = a[i]

  return n_unique, a_unique

def i4vec_sorted_unique_test (  ):

#*****************************************************************************80
#
## I4VEC_SORTED_UNIQUE_TEST tests I4VEC_SORTED_UNIQUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print
  from i4vec_sort_heap_a import i4vec_sort_heap_a
  from i4vec_uniform_ab import i4vec_uniform_ab

  n = 20
  b = 0
  c = n

  print ( '' )
  print ( 'I4VEC_SORTED_UNIQUE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_SORTED_UNIQUE finds unique entries in a sorted array.' )

  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  a = i4vec_sort_heap_a ( n, a )

  i4vec_print ( n, a, '  Input vector:' )

  unique_num, a_unique = i4vec_sorted_unique ( n, a )

  i4vec_print ( unique_num, a_unique, '  Unique entries:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_SORTED_UNIQUE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_sorted_unique_test ( )
  timestamp ( )
 
