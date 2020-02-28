#! /usr/bin/env python
#
def i4mat_width ( m, n, a ):

#*****************************************************************************80
#
## I4MAT_WIDTH returns the printing width of an I4MAT.
#
#  Discussion:
#
#    The width of an I4MAT is simply the maximum of the widths of
#    its entries.
#
#    The width of a single integer is the number of characters 
#    necessary to print it.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the dimensions of the array.
#
#    Input, integer A[M,N], the array.
#
#    Output, integer VALUE, the width of the array.
#
  from i4_width import i4_width

  value = 0

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      value = max ( value, i4_width ( a[i,j] ) )

  return value

def i4mat_width_test ( ):

#*****************************************************************************80
#
## I4MAT_WIDTH_TEST tests I4MAT_WIDTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  print ( '' )
  print ( 'I4MAT_WIDTH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_WIDTH determines the printing width of an I4MAT.' )

  m1 = 3
  n1 = 3
  a1 = np.array ( [ \
    [ 11, 211, 3111 ], \
    [ 12, 222, 3222 ], \
    [ 13, 233, 3333 ] ] )

  i4mat_print ( m1, n1, a1, '  A1:' )

  w = i4mat_width ( m1, n1, a1 )

  print ( '' )
  print ( '  The printing width of A1 is %d' % ( w ) )

  m2 = 3
  n2 = 3
  a2 = np.array ( [ \
    [ 10,    23, 45 ], \
    [ 42, -1000, 63 ], \
    [ 77,    63, 90 ] ] )

  i4mat_print ( m2, n2, a2, '  A2:' )

  w = i4mat_width ( m2, n2, a2 )

  print ( '' )
  print ( '  The printing width of A2 is %d' % ( w ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_WIDTH_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_width_test ( )
  timestamp ( )

