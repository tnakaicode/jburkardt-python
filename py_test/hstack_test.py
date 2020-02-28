#! /usr/bin/env python3
#
def hstack_test ( ):

#*****************************************************************************80
#
## HSTACK_TEST tests np.hstack().
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from i4mat_print import i4mat_print
  import platform

  print ( '' )
  print ( 'HSTACK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  np.hstack() horizontally stacks arrays of same column dimension.' )

  m = 4
  n1 = 3
  a = np.array ( [ \
    [ 11, 12, 13 ], \
    [ 21, 22, 23 ], \
    [ 31, 32, 33 ], \
    [ 41, 42, 43 ] ] )

  i4mat_print ( m, n1, a, '  Matrix A:' )

  n2 = 2
  b = np.array ( [ \
    [ 104, 105 ], \
    [ 204, 205 ], \
    [ 304, 305 ], \
    [ 404, 405 ] ] )

  i4mat_print ( m, n2, b, '  Matrix B:' )

  c = np.hstack ( ( a, b ) )

  i4mat_print ( m, n1+n2, c, '  Matrix hstack(A,B)' )

  d = np.hstack ( ( a[:,0:1], b, a[:,1:3] ) )

  i4mat_print ( m, n1+n2, d, '  Matrix hstack(A[:,0:1], B, A[:,1:3])' )
#
#  Terminate.
#
  print ( '' )
  print ( 'HSTACK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hstack_test ( )
  timestamp ( )

