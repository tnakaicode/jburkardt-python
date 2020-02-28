#! /usr/bin/env python
#
def i4vec_print_mask ( n, a, mask, title ):

#*****************************************************************************80
#
## I4VEC_PRINT_MASK prints masked elements of an I4VEC.
#
#  Discussion:
#
#    Vector elements with a nonzero mask will be printed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, integer MASK(N), the mask.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    if ( mask[i] != 0 ):
      print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_mask_test ( ):

#*****************************************************************************80
#
## I4VEC_PRINT_MASK_TEST tests I4VEC_PRINT_MASK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_print import i4vec_print

  print ( '' )
  print ( 'I4VEC_PRINT_MASK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_PRINT_MASK prints the masked elements of an I4VEC.' )

  n = 10
  v = np.array (    [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], dtype = np.int32 )
  mask = np.array ( [ 0, 1, 1, 0, 1, 0, 1, 0, 0,  0 ], dtype = np.int32 )

  i4vec_print ( n, v, '  Here is the full vector:' )
  i4vec_print ( n, mask, '  Here is the vector mask:' )
  i4vec_print_mask ( n, v, mask, '  Here is the masked vector I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_PRINT_MASK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_print_mask_test ( )
  timestamp ( )

