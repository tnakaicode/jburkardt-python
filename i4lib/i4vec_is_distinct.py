#! /usr/bin/env python
#
def i4vec_is_distinct ( n, a ):

#*****************************************************************************80
#
## I4VEC_IS_DISTINCT is true if the entries in an I4VEC are distinct.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A(N), the vector to be checked.
#
#    Output, logical VALUE is true if the elements of A are distinct.
#
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      if ( a[i] == a[j] ):
        value = False;
        return value

  value = True

  return value

def i4vec_is_distinct_test ( ):

#*****************************************************************************80
#
## I4VEC_IS_DISTINCT_TEST tests I4VEC_IS_DISTINCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_print import i4vec_print

  print ( '' )
  print ( 'I4VEC_IS_DISTINCT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_IS_DISTINCT computes the maximum entry in an I4VEC.' )

  n = 5
  a = np.array ( [ 1, 2, 5, 3, 4 ] )
  i4vec_print ( n, a, '  Input vector:' )
  if ( i4vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )

  n = 5
  a = np.array ( [ 1, 2, 5, 2, 4 ] )
  i4vec_print ( n, a, '  Input vector:' )
  if ( i4vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_IS_DISTINCT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_is_distinct_test ( )
  timestamp ( )
