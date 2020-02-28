#! /usr/bin/env python
#
def i4_is_power_of_10 ( n ):

#*****************************************************************************80
#
## I4_IS_POWER_OF_10 reports whether an integer is a power of 10.
#
#  Discussion:
#
#    The powers of 10 are 1, 10, 100, 1000, 10000, and so on.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the integer to be tested.
#
#    Output, logical VALUE, is TRUE if N is a power of 10.
#
  value = False

  if ( n <= 0 ):
    return value

  while ( 1 < n ):

    if ( ( n % 10 ) != 0 ):
      return value

    n = n // 10

  value = True

  return value

def i4_is_power_of_10_test ( ):

#*****************************************************************************80
#
## I4_IS_POWER_OF_10_TEST tests I4_IS_POWER_OF_10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_IS_POWER_OF_10_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_IS_POWER_OF_10 reports whether an I4 is a power of 10.' )
  print ( '' )
  print ( '  I     I4_IS_POWER_OF_10(I)' )
  print ( '' )

  for i in range ( 97, 104 ):
    print ( '  %6d  %s' % ( i, i4_is_power_of_10 ( i ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_IS_POWER_OF_10_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_is_power_of_10_test ( )
  timestamp ( )

