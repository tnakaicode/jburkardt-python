#! /usr/bin/env python
#
def r8vec_is_in_01 ( n, x ):

#*****************************************************************************80
#
## R8VEC_IS_IN_01 is true if all entries are in [0,1].
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
#    Output, real VALUE, is true if all entries are in [0,1].
#
  import numpy as np

  value = ( np.all ( 0.0 <= x[0:n] ) and np.all ( x[0:n] <= 1.0 ) )

  return value

def r8vec_is_in_01_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_IN_01_TEST tests R8VEC_IS_IN_01.
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
  print ( 'R8VEC_IS_IN_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_IN_01 is TRUE if an R8VEC only contains' )
  print ( '  entries in [0,1].' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 2.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_01 ( n, x ) ):
    print ( '  All entries are in [0,1].' )
  else:
    print ( '  At least one entry is NOT in [0,1].' )

  x = np.array ( [ 0.5, 0.1, 0.9 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_01 ( n, x ) ):
    print ( '  All entries are in [0,1].' )
  else:
    print ( '  At least one entry is NOT in [0,1].' )

  x = np.array ( [ -0.5, 0.5, 0.4 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_01 ( n, x ) ):
    print ( '  All entries are in [0,1].' )
  else:
    print ( '  At least one entry is NOT in [0,1].' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_IN_01_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_in_01_test ( )
  timestamp ( )
