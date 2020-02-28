#! /usr/bin/env python
#
def r8vec_is_in_ab ( n, x, a, b ):

#*****************************************************************************80
#
## R8VEC_IS_IN_AB is true if all entries are in [A,B].
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
#    Input, real A, B, the limits, with A <= B.
#
#    Output, real VALUE, is true if all entries are in [A,B].
#
  import numpy as np

  value = ( np.all ( a <= x[0:n] ) and np.all ( x[0:n] <= b ) )

  return value

def r8vec_is_in_ab_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_IN_AB_TEST tests R8VEC_IS_IN_AB.
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
  print ( 'R8VEC_IS_IN_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_IN_AB is TRUE if an R8VEC only contains' )
  print ( '  entries in [A,B].' )

  n = 3
  a = 0.5
  b = 2.0

  x = np.array ( [ 0.0, 1.0, 2.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_ab ( n, x, a, b ) ):
    print ( '  All entries are in [%f,%f].' % ( a, b ) )
  else:
    print ( '  At least one entry is NOT in [%f,%f].' % ( a, b ) )

  x = np.array ( [ 0.5, 1.1, 0.9 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_ab ( n, x, a, b ) ):
    print ( '  All entries are in [%f,%f].' % ( a, b ) )
  else:
    print ( '  At least one entry is NOT in [%f,%f].' % ( a, b ) )

  x = np.array ( [ -0.5, 0.5, 0.4 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_in_ab ( n, x, a, b ) ):
    print ( '  All entries are in [%f,%f].' % ( a, b ) )
  else:
    print ( '  At least one entry is NOT in [%f,%f].' % ( a, b ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_IN_AB_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_in_ab_test ( )
  timestamp ( )
