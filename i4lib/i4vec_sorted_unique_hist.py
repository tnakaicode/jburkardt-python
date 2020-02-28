#! /usr/bin/env python
#
def i4vec_sorted_unique_hist ( n, a ):

#*****************************************************************************80
#
## I4VEC_SORTED_UNIQUE_HIST histograms unique elements of a sorted I4VEC.
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
#    Input, integer N, the number of elements of A.
#
#    Input, integer A(N), the array to examine.  The elements of A
#    should have been sorted.
#
#    Output, integer UNIQUE_NUM, the number of unique elements of A.
#
#    Output, integer AUNIQ(UNIQUE_NUM), the unique elements of A.
#
#    Output, integer ACOUNT(UNIQUE_NUM), the number of times each element
#    of AUNIQ occurs in A.
#
  import numpy as np
  from i4vec_sorted_unique_count import i4vec_sorted_unique_count

  unique_num = i4vec_sorted_unique_count ( n, a )

  auniq = np.zeros ( unique_num, dtype = np.int32 )
  acount = np.zeros ( unique_num, dtype = np.int32 )
#
#  Start taking statistics.
#
  k = 0
  auniq[k] = a[0]
  acount[k] = 1

  for i in range ( 1, n ):

    if ( a[i] == auniq[k] ):

      acount[k] = acount[k] + 1

    else:

      k = k + 1
      auniq[k] = a[i]
      acount[k] = 1

  return unique_num, auniq, acount

def i4vec_sorted_unique_hist_test ( ):

#*****************************************************************************80
#
## I4VEC_SORTED_UNIQUE_HIST_TEST tests I4VEC_SORTED_UNIQUE_HIST_TEST.
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
  import numpy as np
  import platform
  from i4vec_print import i4vec_print
  from i4vec_sort_heap_a import i4vec_sort_heap_a
  from i4vec_uniform_ab import i4vec_uniform_ab
  from i4vec2_print import i4vec2_print

  print ( '' )
  print ( 'I4VEC_SORTED_UNIQUE_HIST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_SORTED_UNIQUE_HIST_TEST is given a sorted array' )
  print ( '  of integers, and returns the number of unique values,' )
  print ( '  the unique values, and their frequency.' )

  n = 50
  a = 0
  b = 10
  seed = 123456789

  v1, seed = i4vec_uniform_ab ( n, a, b, seed )

  v2, seed = i4vec_uniform_ab ( n, a, b, seed )

  v3 = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    v3[i] = v1[i] * v2[i]

  v3 = i4vec_sort_heap_a ( n, v3 )

  i4vec_print ( n, v3, '  The sorted vector:' )

  [ unique_num, unique_value,  unique_freq ] = i4vec_sorted_unique_hist ( n, v3 )

  i4vec2_print ( unique_num, unique_value, unique_freq, \
    '  Unique values and frequencies:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_SORTED_UNIQUE_HIST_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_sorted_unique_hist_test ( )
  timestamp ( )

