#! /usr/bin/env python
#
def r8vec_rotate ( n, a, m ):

#*****************************************************************************80
#
## R8VEC_ROTATE "rotates" the entries of an R8VEC in place.
#
#  Discussion:
#
#    This routine rotates an array of real "objects", but the same
#    logic can be used to permute an array of objects of any arithmetic
#    type, or an array of objects of any complexity.  The only temporary
#    storage required is enough to store a single object.  The number
#    of data movements made is N + the number of cycles of order 2 or more,
#    which is never more than N + N/2.
#
#  Example:
#
#    Input:
#
#      N = 5, M = 2
#      A    = ( 1.0, 2.0, 3.0, 4.0, 5.0 )
#
#    Output:
#
#      A    = ( 4.0, 5.0, 1.0, 2.0, 3.0 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects.
#
#    Input, integer M, the number of positions to the right that
#    each element should be moved.  Elements that shift pass position
#    N "wrap around" to the beginning of the array.
#
#    Input, real A(N), the array to be rotated.
#
#    Output, real A(N), the rotated array.
#
  from i4_modp import i4_modp
#
#  Force M to be positive, between 0 and N-1.
#
  m = i4_modp ( m, n )

  if ( m == 0 ):
    return a

  istart = 0
  nset = 0

  while ( True ):

    istart = istart + 1

    if ( n < istart ):
      break

    temp = a[istart-1]
    iget = istart
#
#  Copy the new value into the vacated entry.
#
    while ( True ):

      iput = iget

      iget = iget - m
      if ( iget < 1 ):
        iget = iget + n

      if ( iget == istart ):
        break

      a[iput-1] = a[iget-1]
      nset = nset + 1

    a[iput-1] = temp
    nset = nset + 1

    if ( n <= nset ):
      break

  return a

def r8vec_rotate_test ( ):

#*****************************************************************************80
#
## R8VEC_ROTATE_TEST tests R8VEC_ROTATE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  n = 5

  a = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )

  m = 2

  print ( '' )
  print ( 'R8VEC_ROTATE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_ROTATE rotates an R8VEC in place.' )
  print ( '' )
  print ( '  Rotate entries %d places to the right' % ( m ) )

  r8vec_print ( n, a, '  Original array:' )

  a = r8vec_rotate ( n, a, m )

  r8vec_print ( n, a, '  Rotated array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_ROTATE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_rotate_test ( )
  timestamp ( )
