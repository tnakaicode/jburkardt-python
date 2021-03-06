#! /usr/bin/env python
#
def i4_not ( i, j ):

#*****************************************************************************80
#
## I4_NOT calculates the NOT of an I4 with respect to a maximum value.
#
#  Discussion:
#
#    An I4 is an integer value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the value whose NOT is needed.
#
#    Input, integer J, the maximum value.
#
#    Output, integer VALUE, the NOT of I with respect to J.
#
  i1 = i
  j1 = j
  value = 0
  l = 1

  while ( j1 != 0 ):

    i2 = i1 // 2

    if ( i1 == 2 * i2 ):
      value = value + l

    i1 = i2
    l = 2 * l

    j1 = j1 // 2

  return value

def i4_not_test ( ):

#*****************************************************************************80
#
## I4_NOT_TEST tests I4_NOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_uniform_ab import i4_uniform_ab

  i4_lo = 0
  i4_hi = 100
  test_num = 10
  seed = 123456789
  j = 255

  print ( '' )
  print ( 'I4_NOT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_NOT returns the NOT of an I4 with respect to a value J.' )
  print ( '' )
  print ( '         I         J    I4_NOT    ~I+J+1' )
  print ( '' )

  for test in range ( 0, test_num ):

    i, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )
    k = i4_not ( i, j )
    l = ~ i + j + 1
    print ( '  %8d  %8d  %8d  %8d' % ( i, j, k, l ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_NOT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_not_test ( )
  timestamp ( )

