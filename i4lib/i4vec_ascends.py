#! /usr/bin/env python
#
def i4vec_ascends ( n, x ):

#*****************************************************************************80
#
## I4VEC_ASCENDS is TRUE if an I4VEC is increasing.
#
#  Example:
#
#    X = ( 9, 7, 7, 3, 2, 1, -8 )
#
#    I4VEC_ASCENDS = FALSE
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the array.
#
#    Input, integer X(N), the array to be examined.
#
#    Output, logical VALUE, is TRUE if the entries of X ascend.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( x[i] > x[i+1] ):
      value = False
      break

  return value

def i4vec_ascends_test ( ):

#*****************************************************************************80
#
## I4VEC_ASCENDS_TEST tests I4VEC_ASCENDS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 4
  test_num = 6

  x_test = np.array ( [ \
    [ 1, 3, 2, 4 ], \
    [ 2, 2, 2, 2 ], \
    [ 1, 2, 2, 4 ], \
    [ 1, 2, 3, 4 ], \
    [ 4, 4, 3, 1 ], \
    [ 9, 7, 3, 0 ] ] )

  print ( '' )
  print ( 'I4VEC_ASCENDS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_ASCENDS determines if an I4VEC ascends.' )

  for i in range ( 0, test_num ):

    x = np.zeros ( n )
    for j in range ( 0, n ):
      x[j] = x_test[i,j]

    i4vec_transpose_print ( n, x, '  Test vector:' )

    value = i4vec_ascends ( n, x )

    print ( '  I4VEC_ASCENDS = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_ASCENDS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_ascends_test ( )
  timestamp ( )
