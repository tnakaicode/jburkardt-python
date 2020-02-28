#! /usr/bin/env python
#
def i4vec_search_binary_a ( n, a, b ):

#*****************************************************************************80
#
#% I4VEC_SEARCH_BINARY_A searches an ascending sorted I4VEC.
#
#  Discussion:
#
#    Binary search is used.
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
#    CRC Press, 1998, page 26.
#
#  Parameters:
#
#    Input, integer N, the number of elements in the vector.
#
#    Input, integer A(N), the array to be searched.  A must
#    be sorted in ascending order.
#
#    Input, integer B, the value to be searched for.
#
#    Output, integer INDX, the result of the search.
#    -1, B does not occur in A.
#    I, A(I) = B.
#
  indx = -1

  low = 0
  high = n - 1

  while ( low <= high ):

    mid = ( ( low + high ) // 2 )

    if ( a[mid] == b ):
      indx = mid;
      break
    elif ( a[mid] < b ):
      low = mid + 1
    elif ( b < a[mid] ):
      high = mid - 1

  return indx

def i4vec_search_binary_a_test ( ):

#*****************************************************************************80
#
## I4VEC_SEARCH_BINARY_A_TEST tests I4VEC_SEARCH_BINARY_A.
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
  import numpy as np
  import platform
  from i4vec_print import i4vec_print

  n = 10

  print ( '' )
  print ( 'I4VEC_SEARCH_BINARY_A_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_SEARCH_BINARY_A searches a ascending sorted vector.' )

  a = np.array ( [ 0, 1, 1, 2, 3, 4, 5, 6, 7, 8 ] )

  i4vec_print ( n, a, '  Ascending sorted array:' )

  b = 5

  print ( '' )
  print ( '  Now search for an instance of the value %d' % ( b ) )

  index = i4vec_search_binary_a ( n, a, b )

  print ( '' )
  if ( index == -1 ):
    print ( '  The value does not occur.' )
  else:
    print ( '  The value occurs at index = %d' % ( index ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_SEARCH_BINARY_A_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_search_binary_a_test ( )
  timestamp ( )

