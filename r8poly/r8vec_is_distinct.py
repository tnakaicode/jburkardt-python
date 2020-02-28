#! /usr/bin/env python3
#
def r8vec_is_distinct ( n, a ):

#*****************************************************************************80
#
## R8VEC_IS_DISTINCT is true if the entries in an R8VEC are distinct.
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
#    Input, real A(N), the vector to be checked.
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

def r8vec_is_distinct_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_DISTINCT_TEST tests R8VEC_IS_DISTINCT.
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
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8VEC_IS_DISTINCT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_DISTINCT computes the maximum entry in an R8VEC.' )

  n = 5
  a = np.array ( [ 1.0, 2.0, 5.0, 3.0, 4.0 ] )
  r8vec_print ( n, a, '  Input vector:' )
  if ( r8vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )

  n = 5
  a = np.array ( [ 1.0, 2.0, 5.0, 2.0, 4.0 ] )
  r8vec_print ( n, a, '  Input vector:' )
  if ( r8vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_DISTINCT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_distinct_test ( )
  timestamp ( )
