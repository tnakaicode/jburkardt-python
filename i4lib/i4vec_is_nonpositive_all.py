#! /usr/bin/env python
#
def i4vec_is_nonpositive_all ( n, x ):

#*****************************************************************************80
#
## I4VEC_IS_NONPOSITIVE_ALL is true if all entries of an I4VEC are nonpositive.
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
#    Input, integer N, the dimension of the vectors.
#
#    Input, integer X(N), the vector to be compared against.
#
#    Output, logical VALUE, is true if all entries of X are <= 0.
#
  value = all ( x[0:n] <= 0 )

  return value

def i4vec_is_nonpositive_all_test ( ):

#*****************************************************************************80
#
## I4VEC_IS_NONPOSITIVE_ALL_TEST tests I4VEC_IS_NONPOSITIVE_ALL.
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
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'I4VEC_IS_NONPOSITIVE_ALL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_IS_NONPOSITIVE_ALL is TRUE if an I4VEC only contains' )
  print ( '  nonpositive entries.' )

  n = 3

  x = np.array ( [ -1, -2, 0 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonpositive_all ( n, x ) ):
    print ( '  X is only nonpositives.' )
  else:
    print ( '  X is NOT only nonpositives.' )

  x = np.array ( [ -1, 0, 1 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonpositive_all ( n, x ) ):
    print ( '  X is only nonpositives.' )
  else:
    print ( '  X is NOT only nonpositives.' )

  x = np.array ( [ -1, -3, -99 ] )
  print ( '' )
  i4vec_transpose_print ( n, x, '  X:' )
  if ( i4vec_is_nonpositive_all ( n, x ) ):
    print ( '  X is only nonpositives.' )
  else:
    print ( '  X is NOT only nonpositives.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_IS_NONPOSITIVE_ALL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_is_nonpositive_all_test ( )
  timestamp ( )


