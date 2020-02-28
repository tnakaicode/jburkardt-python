#! /usr/bin/env python
#
def i4_btest ( i4, pos ):

#*****************************************************************************80
#
## I4_BTEST returns TRUE if the POS-th bit of an I4 is 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
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
#    Output, logical VALUE, is TRUE if the POS-th bit of I4 is 1.
#
  from sys import exit

  i4_huge = 2147483647

  if ( pos < 0 ):

    print ( '' )
    print ( 'I4_BTEST - Fatal error!' )
    print ( '  POS < 0.' )
    exit ( 'I4_BTEST - Fatal error!' )

  elif ( pos < 31 ):

    if ( 0 <= i4 ):
      j = i4
    else:
      j = ( i4_huge + i4 ) + 1

    for k in range ( 0, pos ):
      j = ( j // 2 )

    if ( ( j % 2 ) == 0 ):
      value = False
    else:
      value = True

  elif ( pos == 31 ):

    if ( i4 < 0 ):
      value = True
    else:
      value = False

  elif ( 31 < pos ):

    print ( '' )
    print ( 'I4_BTEST - Fatal error!' )
    print ( '  31 < POS.' )
    exit ( 'I4_BTEST - Fatal error!' )

  return value

def i4_btest_test ( ):

#*****************************************************************************80
#
## I4_BTEST_TEST tests I4_BTEST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  i4_test = np.array ( [ 101, -31 ] )

  print ( '' )
  print ( 'I4_BTEST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_BTEST reports whether a given bit is 0 or 1.' )

  for test in range ( 0, 2 ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Analyze the integer I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     I4_BTEST(I4,POS)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_btest ( i4, pos )

      print ( '  %12d             %s' % ( pos, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_BTEST_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_btest_test ( )
  timestamp ( )

