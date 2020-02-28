#! /usr/bin/env python
#
def i4vec_sort_heap_a ( n, a ):

#*****************************************************************************80
#
## I4VEC_SORT_HEAP_A ascending sorts an I4VEC using heap sort.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the array.
#
#    Input, integer A(N), the array to be sorted;
#
#    Output, integer A_SORTED(N), the sorted array.
#
  import numpy as np
  from i4vec_heap_d import i4vec_heap_d

  if ( n == 1 ):
    a_sorted = np.zeros ( n )
    a_sorted[0] = a[0]
    return a_sorted
#
#  1: Put A into descending heap form.
#
  a_sorted = i4vec_heap_d ( n, a )
#
#  2: Sort A.
#
#  The largest object in the heap is in A(0).
#  Move it to position A(N-1).
#
  temp = a_sorted[0]
  a_sorted[0] = a_sorted[n-1]
  a_sorted[n-1] = temp
#
#  Consider the diminished heap of size N1.
#
  for n1 in range ( n - 1, 0, -1 ):
#
#  Restore the heap structure of A(0) through A(N1-1).
#
    a_resorted = i4vec_heap_d ( n1, a_sorted )

    for i in range ( 0, n1 ):
      a_sorted[i] = a_resorted[i]
#
#  Take the largest object from A(1) and move it to A(N1).
#
    temp = a_sorted[0]
    a_sorted[0] = a_sorted[n1-1]
    a_sorted[n1-1] = temp

  return a_sorted

def i4vec_sort_heap_a_test ( ):

#*****************************************************************************80
#
## I4VEC_SORT_HEAP_A_TEST tests I4VEC_SORT_HEAP_A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 September 2015
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
  c = 3 * n

  print ( '' )
  print ( 'I4VEC_SORT_HEAP_A_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_SORT_HEAP_A ascending sorts an I4VEC.' )

  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  Unsorted:' )

  a = i4vec_sort_heap_a ( n, a )

  i4vec_print ( n, a, '  Ascending sorted:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_SORT_HEAP_A_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_sort_heap_a_test ( )
  timestamp ( )

