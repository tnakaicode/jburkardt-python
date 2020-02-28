#! /usr/bin/env python
#
def vstack_test ( ):

#*****************************************************************************80
#
## VSTACK_TEST tests np.vstack().
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
  print ( 'VSTACK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  np.vstack() vertically stacks arrays of same column dimension.' )

  m1 = 4
  n = 3
  a = np.array ( [ \
    [ 11, 12, 13 ], \
    [ 21, 22, 23 ], \
    [ 31, 32, 33 ], \
    [ 41, 42, 43 ] ] )

  i4mat_print ( m1, n, a, '  Matrix A:' )

  m2 = 2
  b = np.array ( [ \
    [ 501, 502, 503 ],\
    [ 601, 602, 603 ] ] )

  i4mat_print ( m2, n, b, '  Matrix B:' )

  c = np.vstack ( ( a, b ) )

  i4mat_print ( m1+m2, n, c, '  Matrix vstack(A,B)' )

  d = np.vstack ( ( a[0:2,:], b, a[2:4,:] ) )

  i4mat_print ( m1+m2, n, d, '  Matrix vstack(A[0:2,:],B,A{2:4,:])' )
#
#  Terminate.
#
  print ( '' )
  print ( 'VSTACK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  vstack_test ( )
  timestamp ( )

