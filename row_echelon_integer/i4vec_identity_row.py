#! /usr/bin/env python
#
def i4vec_identity_row ( n, i ):

#*****************************************************************************80
#
## I4VEC_IDENTITY_ROW returns a row of the identity matrix as an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 August 2018
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
#    0 <= I < N.
#
#    Output, integer A(N), the vector.
#
  import numpy as np

  a = np.zeros ( n )

  if ( 0 <= i and i < n ):
    a[i] = 1

  return a

def i4vec_identity_row_test ( ):

#*****************************************************************************80
#
## I4VEC_IDENTITY_ROW_TEST tests I4VEC_IDENTITY_ROW.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4VEC_IDENTITY_ROW_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_IDENTITY_ROW returns a row of the identity matrix.' )
  print ( '' )

  n = 5
  for i in range ( -1, 6 ):
    a = i4vec_identity_row ( n, i )
    print ( '%2d: ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( ' %d' % ( a[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_IDENTITY_ROW_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_identity_row_test ( )
  timestamp ( )


