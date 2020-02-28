#! /usr/bin/env python
#
def i4vec2_print ( n, a, b, title ):

#*****************************************************************************80
#
## I4VEC2_PRINT prints an I4VEC2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, integer A(N), B(N), the vectors to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d  %6d' % ( i, a[i], b[i] ) )

  return

def i4vec2_print_test ( ):

#*****************************************************************************80
#
## I4VEC2_PRINT_TEST tests I4VEC2_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10

  print ( '' )
  print ( 'I4VEC2_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC2_PRINT prints a pair of I4VECs' )

  a = np.zeros ( n + 1, dtype = np.int32 )
  b = np.zeros ( n + 1, dtype = np.int32 )

  for i in range ( 0, n + 1 ):
    a[i] = ( i * ( i + 1 ) ) / 2
    b[i] = ( i * ( i + 1 ) * ( 2 * i + 1 ) ) / 6

  i4vec2_print ( n + 1, a, b, '  I, sum of I, sum of I^2:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC2_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec2_print_test ( )
  timestamp ( )

