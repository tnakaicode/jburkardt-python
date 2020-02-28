#! /usr/bin/env python
#
def i4vec_search_binary_d ( n, a, b ):

#*****************************************************************************80
#
#% I4VEC_SEARCH_BINARY_D searches a descending sorted I4VEC.
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
#    be sorted in descending order.
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
    elif ( b < a[mid] ):
      low = mid + 1
    elif ( a[mid] < b ):
      high = mid - 1

  return indx

def i4vec_search_binary_d_test ( ):

#*****************************************************************************80
#
## I4VEC_SEARCH_BINARY_D_TEST tests I4VEC_SEARCH_BINARY_D.
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
  print ( 'I4VEC_SEARCH_BINARY_D_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_SEARCH_BINARY_D searches a descending sorted vector.' )

  a = np.array ( [ 8, 7, 6, 5, 4, 3, 2, 1, 1, 0 ] )

  i4vec_print ( n, a, '  Descending sorted array:' )

  b = 5

  print ( '' )
  print ( '  Now search for an instance of the value %d' % ( b ) )

  index = i4vec_search_binary_d ( n, a, b )

  print ( '' )
  if ( index == -1 ):
    print ( '  The value does not occur.' )
  else:
    print ( '  The value occurs at index = %d' % ( index ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_SEARCH_BINARY_D_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_search_binary_d_test ( )
  timestamp ( )

