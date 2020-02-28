#! /usr/bin/env python
#
def r8vec_is_one ( n, x ):

#*****************************************************************************80
#
## R8VEC_IS_ONE is true if every entry is one.
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
#    Output, real VALUE, is true if all entries are one.
#
  import numpy as np

  value = np.all ( x[0:n] == 1.0 )

  return value

def r8vec_is_one_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_ONE_TEST tests R8VEC_IS_ONE.
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
  print ( 'R8VEC_IS_ONE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_ONE is TRUE if an R8VEC contains' )
  print ( '  only one entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_one ( n, x ) ):
    print ( '  X contains only one entries.' )
  else:
    print ( '  X contains at least one nonone entry.' )

  x = np.array ( [ 1.0, 1.0, 1.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_one ( n, x ) ):
    print ( '  X contains only one entries.' )
  else:
    print ( '  X contains at least one nonone entry.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_one ( n, x ) ):
    print ( '  X contains only one entries.' )
  else:
    print ( '  X contains at least one nonone entry.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_ONE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_one_test ( )
  timestamp ( )
