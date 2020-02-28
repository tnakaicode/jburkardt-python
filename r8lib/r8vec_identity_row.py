#! /usr/bin/env python
#
def r8vec_identity_row ( n, i ):

#*****************************************************************************80
#
## R8VEC_IDENTITY_ROW returns a row of the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer I, the index of the entry to be set to 1.
#    0-based indexing is used.
#
#    Output, real A(N), the vector.
#
  import numpy as np

  a = np.zeros ( n );

  if ( 0 <= i and i < n ):
    a[i] = 1.0

  return a

def r8vec_identity_row_test ( ):

#*****************************************************************************80
#
## R8VEC_IDENTITY_ROW_TEST tests R8VEC_IDENTITY_ROW.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8VEC_IDENTITY_ROW_TEST' )
  print ( '  R8VEC_IDENTITY_ROW returns a row of the identity matrix.' )
  print ( '' )

  n = 5
  for i in range ( -1, 6 ):
    a = r8vec_identity_row ( n, i )
    print ( '%2d: ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( ' %d' % ( a[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IDENTITY_ROW_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_identity_row_test ( )
  timestamp ( )

