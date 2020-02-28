#! /usr/bin/env python
#
def r8vec_is_integer ( n, x ):

#*****************************************************************************80
#
## R8VEC_IS_INTEGER is true if every entry is an integer.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, real X(N), the vector to be compared against.
#
#    Output, real VALUE, is true if all entries are integers.
#
  import numpy as np

  value = np.all ( x[0:n] == np.round ( x[0:n] ) )

  return value

def r8vec_is_integer_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_INTEGER_TEST tests R8VEC_IS_INTEGER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_transpose_print import r8vec_transpose_print

  print ( '' )
  print ( 'R8VEC_IS_INTEGER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_INTEGER is TRUE if an R8VEC contains' )
  print ( '  only integer entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 100.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_integer ( n, x ) ):
    print ( '  X contains only integer entries.' )
  else:
    print ( '  X contains at least one noninteger entry.' )

  x = np.array ( [ 1.0, 2.5, 3.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_integer ( n, x ) ):
    print ( '  X contains only integer entries.' )
  else:
    print ( '  X contains at least one noninteger entry.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_integer ( n, x ) ):
    print ( '  X contains only integer entries.' )
  else:
    print ( '  X contains at least one noninteger entry.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_INTEGER_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_integer_test ( )
  timestamp ( )
