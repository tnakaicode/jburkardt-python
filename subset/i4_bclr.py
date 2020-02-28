#! /usr/bin/env python
#
def i4_bclr ( i4, pos ):

#*****************************************************************************80
#
## I4_BCLR returns a copy of an I4 in which the POS-th bit is set to 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 June 20145
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Military Standard 1753,
#    FORTRAN, DoD Supplement To American National Standard X3.9-1978,
#    9 November 1978.
#
#  Parameters:
#
#    Input, integer I4, the integer to be tested.
#
#    Input, integer POS, the bit position, between 0 and 31.
#
#    Output, integer VALUE, a copy of I4, but with the POS-th bit
#    set to 0.
#
  i4_huge = 2147483647

  value = i4

  if ( pos < 0 ):
    pass
  elif ( pos < 31 ):

    sub = 1

    if ( 0 <= i4 ):
      j = i4
    else:
      j = ( i4_huge + i4 ) + 1

    for k in range ( 0, pos ):
      j = ( j // 2 )
      sub = sub * 2

    if ( ( j % 2 ) == 1 ):
      value = i4 - sub

  elif ( pos == 31 ):

    if ( i4 < 0 ):
      value = ( i4_huge + i4 ) + 1

  elif ( 31 < pos ):

    value = i4

  return value

def i4_bclr_test ( ):

#*****************************************************************************80
#
## I4_BCLR_TEST tests I4_BCLR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 2

  i4_test = np.array ( [ 101, -31 ], dtype = np.int32 )

  print ( '' )
  print ( 'I4_BCLR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_BCLR sets a given bit to 0.' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Working on I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     I4_BCLR(I4,Pos)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_bclr ( i4, pos )

      print ( '  %8d  %12d' % ( pos, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_BCLR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_bclr_test ( )
  timestamp ( )

