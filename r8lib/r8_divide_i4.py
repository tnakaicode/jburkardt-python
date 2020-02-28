#! /usr/bin/env python3
#
def r8_divide_i4 ( i, j ):

#*****************************************************************************80
#
## R8_DIVIDE_I4 returns an I4 fraction as an R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the numerator and denominator.
#
#    Output, real VALUE, the value of (I/J).
#
  value = float ( i ) / float ( j )

  return value

def r8_divide_i4_test ( ):

#*****************************************************************************80
#
## R8_DIVIDE_I4_TEST tests R8_DIVIDE_I4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 12

  print ( '' )
  print ( 'R8_DIVIDE_I4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_DIVIDE_I4 computes an integer ratio as a real number.' )
  print ( '' )
  print ( '     I     J    I/J  I//J  R8_DIVIDE_I4(I,J)' )
  print ( '' )
  for i in range ( - 3, 8 ):
    for j in range ( -2, 5 ):
      if ( j != 0 ):
        k = i / j
        l = i // j
        m = r8_divide_i4 ( i, j )
        print ( '  %4d  %4d  %4d  %4d  %g' % ( i, j, k, l, m ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_DIVIDE_I4_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_divide_i4_test ( )
  timestamp ( )
 
