#! /usr/bin/env python
#
def i4vec_width ( n, a ):

#*****************************************************************************80
#
## I4VEC_WIDTH returns the "width" of an I4VEC.
#
#  Discussion:
#
#    The width of an integer vector is simply the maximum of the widths of
#    its entries.
#
#    The width of a single integer is the number of characters 
#    necessary to print it.
#
#    The width of an integer vector can be useful when the vector is 
#    to be printed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A(N), the vector.
#
#    Output, integer VALUE, the width of the vector.
#
  from i4_width import i4_width

  value = -1

  for i in range ( 0, n ):
    value = max ( value, i4_width ( a[i] ) )

  return value

def i4vec_width_test ( ):

#*****************************************************************************80
#
## I4VEC_WIDTH_TEST tests I4VEC_WIDTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_print import i4vec_print

  n = 13
  i4vec = np.array ( [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ] )

  print ( '' )
  print ( 'I4VEC_WIDTH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_WIDTH determines the printing "width" of an I4VEC.' )

  i4vec_print ( n, i4vec, '  The vector' )

  w = i4vec_width ( n, i4vec )

  print ( '' )
  print ( '  The printing width is %d' % ( w ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_WIDTH_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_width_test ( )
  timestamp ( )

