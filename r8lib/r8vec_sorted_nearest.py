#! /usr/bin/env python
#
def r8vec_sorted_nearest ( n, a, value ):

#*****************************************************************************80
#
## R8VEC_SORTED_NEAREST returns the nearest element in a sorted R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements of A.
#
#    Input, real A(N), a sorted vector.
#
#    Input, real VALUE, the value whose nearest vector entry is sought.
#
#    Output, integer INDEX, the index of the nearest
#    entry in the vector.
#
  import numpy as np

  if ( n < 1 ):
    index = -1
    return index

  if ( n == 1 ):
    index = 0
    return index

  if ( a[0] < a[n-1] ):

    if ( value < a[0] ):
      index = 0
      return index
    elif ( a[n-1] < value ):
      index = n - 1
      return index
#
#  Seek an interval containing the value.
#
    lo = 0
    hi = n - 1

    while ( lo < hi - 1 ):

      mid = int ( np.floor ( ( lo + hi ) / 2 ) )

      if ( value == a[mid] ):
        index = mid
        return
      elif ( value < a[mid] ):
        hi = mid
      else:
        lo = mid
#
#  Take the nearest.
#
    if ( abs ( value - a[lo] ) < abs ( value - a[hi] ) ):
      index = lo
    else:
      index = hi

    return index
#
#  A descending sorted vector A.
#
  else:

    if ( value < a[n-1] ):
      index = n - 1
      return index
    elif ( a[0] < value ):
      index = 0
      return index
#
#  Seek an interval containing the value.
#
    lo = n - 1
    hi = 0

    while ( lo < hi - 1 ):

      mid = np.floor ( ( lo + hi ) / 2 )

      if ( value == a[mid] ):
        index = mid
        return index
      elif ( value < a[mid] ):
        hi = mid
      else:
        lo = mid
#
#  Take the nearest.
#
    if ( abs ( value - a(lo) ) < abs ( value - a(hi) ) ):
      index = lo
    else:
      index = hi

    return index

  return index

def r8vec_sorted_nearest_test ( ):

#*****************************************************************************80
#
## R8VEC_SORTED_NEAREST_TEST tests R8VEC_SORTED_NEAREST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print
  from r8_uniform_ab import r8_uniform_ab

  n = 11
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_SORTED_NEAREST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_SORTED_NEAREST finds, for a given value R,' )
  print ( '  the nearest element in a sorted R8VEC.' )

  s = np.linspace ( 0.0, 10.0, n );
  r8vec_print ( n, s, '  Sorted R8VEC:' )

  print ( '' )
  for i in range ( 0, 15 ):
    r, seed = r8_uniform_ab ( -1.0, 11.0, seed )
    index = r8vec_sorted_nearest ( n, s, r )
    print ( '  R = %g is nearest S[%d] = %g' % ( r, index, s[index] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_SORTED_NEAREST_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_sorted_nearest_test ( )
  timestamp ( )


