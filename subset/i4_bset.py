#! /usr/bin/env python
#
def i4_bset ( i4, pos ):

#*****************************************************************************80
#
## I4_BSET returns a copy of an I4 in which the POS-th bit is set to 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 June 2015
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
#    set to 1.
#
  i4_huge = 2147483647

  value = i4

  if ( pos < 0 ):

    pass

  elif ( pos < 31 ):

    add = 1

    if ( 0 <= i4 ):
      j = i4
    else:
      j = ( i4_huge + i4 ) + 1

    for k in range ( 0, pos ):
      j = ( j // 2 )
      add = add * 2

    if ( ( j % 2 ) == 0 ):
      value = i4 + add

  elif ( pos == 31 ):

    if ( 0 < i4 ):
      value = - ( i4_huge - i4 ) - 1

  elif ( 31 < pos ):

    value = i4

  return value

def i4_bset_test ( ):

#*****************************************************************************80
#
## I4_BSET_TEST tests I4_BSET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 2

  i4_test = np.array ( [ 101, -31 ] )

  print ( '' )
  print ( 'I4_BSET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_BSET sets a given bit to 1.' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Working on I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     I4_BSET(I4,Pos)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_bset ( i4, pos )

      print ( '  %8d  %12d' % ( pos, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_BSET_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_bset_test ( )
  timestamp ( )

