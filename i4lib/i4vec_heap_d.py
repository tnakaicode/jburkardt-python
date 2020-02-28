#! /usr/bin/env python
#
def i4vec_heap_d ( n, a ):

#*****************************************************************************80
#
## I4VEC_HEAP_D reorders an I4VEC into an descending heap.
#
#  Definition:
#
#    A descending heap is an array A with the property that, for every index J,
#    A(J) >= A(2*J) and A(J) >= A(2*J+1), (as long as the indices
#    2*J and 2*J+1 are legal).
#
#  Diagram:
#
#                  A(1)
#                /      \
#            A(2)         A(3)
#          /     \        /  \
#      A(4)       A(5)  A(6) A(7)
#      /  \       /   \
#    A(8) A(9) A(10) A(11)
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
#    Input, integer N, the size of the input array.
#
#    Input, integer A(N), an unsorted array.
#
#    Output, integer A_OUT(N), the array has been reordered into a heap.
#
  import numpy as np

  a_out = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    a_out[i] = a[i]
#
#  Only nodes N/2-1 down to 0 can be "parent" nodes.
#
  i_hi = ( n // 2 )

  for i in range ( i_hi - 1, -1, -1 ):
#
#  Copy the value out of the parent node.
#  Position IFREE is now "open".
#
    key = a_out[i]
    ifree = i

    while ( True ):
#
#  Positions 2*IFREE and 2*IFREE + 1 are the descendants of position
#  IFREE.  (One or both may not exist because they exceed N.)
#
      m = 2 * ifree + 1
#
#  Does the first position exist?
#
      if ( n - 1 < m ):
        break
#
#  Does the second position exist?
#
      if ( m + 1 < n ):
#
#  If both positions exist, take the larger of the two values,
#  and update M if necessary.
#
        if ( a_out[m] < a_out[m+1] ):
          m = m + 1
#
#  If the large descendant is larger than KEY, move it up,
#  and update IFREE, the location of the free position, and
#  consider the descendants of THIS position.
#
      if ( a_out[m] <= key ):
        break

      a_out[ifree] = a_out[m]
      ifree = m
#
#  Once there is no more shifting to do, KEY moves into the free spot IFREE.
#
    a_out[ifree] = key

  return a_out

def i4vec_heap_d_test ( ):

#*****************************************************************************80
#
## I4VEC_HEAP_D_TEST tests I4VEC_HEAP_D.
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

  n = 10
  b = 0
  c = n
  seed = 123456789

  print ( '' )
  print ( 'I4VEC_HEAP_D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_HEAP_D puts an I4VEC into descending heap form.' )

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  Unsorted array:' )
 
  a = i4vec_heap_d ( n, a )
 
  i4vec_print ( n, a, '  Descending heap form:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_HEAP_D_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_heap_d_test ( )
  timestamp ( )

