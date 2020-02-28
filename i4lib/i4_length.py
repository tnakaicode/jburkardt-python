#! /usr/bin/env python
#
def i4_length ( i4 ):

#*****************************************************************************80
#
## I4_LENGTH computes the number of characters needed to print an I4.
#
#  Example:
#
#        I4    I4_LENGTH
#
#         0       1
#         1       1
#        -1       2
#      1952       4
#    123456       6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the integer whose length is desired.
#
#    Output, integer VALUE, the number of characters required
#    to print the integer.
#

#
#  Ensure that I4 is an integer.
#
  i4 = int ( i4 )

  if ( i4 < 0 ):
    value = 1
    i4 = - i4
  elif ( i4 == 0 ):
    value = 1
    return value
  else:
    value = 0

  while ( i4 != 0 ):
    value = value + 1
    i4 = ( i4 // 10 )

  return value

def i4_length_test ( ):

#*****************************************************************************80
#
## I4_LENGTH_TEST tests I4_LENGTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 6

  i4_test = np.array ( [ 0, 1, -1, 140, -1952, 123456 ], dtype = np.int32 )

  print ( '' )
  print ( 'I4_LENGTH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_LENGTH computes an integer\'s "length".' )
  print ( '' )
  print ( '        I4    Length' )
  print ( '' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    j4 = i4_length ( i4 )

    print ( '  %8d  %8d' % ( i4, j4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_LENGTH_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_length_test ( )
  timestamp ( )

