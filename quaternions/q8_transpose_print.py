#! /usr/bin/env python3
#
def q8_transpose_print ( q, title ):

#*****************************************************************************80
#
## Q8_TRANSPOSE_PRINT prints a Q8 "transposed".
#
#  Discussion:
#
#    A Q8 is a quaternion using R8 arithmetic.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real Q(4), the quaternion to be printed.
#
#    Input, string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( title, end = '' )

  print ( '%12g  %12g  %12g  %12g' % ( q[0], q[1], q[2], q[3] ) )
 
  return

def q8_transpose_print_test ( ):

#*****************************************************************************80
#
## Q8_TRANSPOSE_PRINT_TEST tests Q8_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform
  from q8_normal_01 import q8_normal_01

  seed = 123456789

  print ( '' )
  print ( 'Q8_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Q8_TRANSPOSE_PRINT prints a quaternion "transposed",' )
  print ( '  that is, writing it as a row vector.' )
  print ( '' )

  q, seed = q8_normal_01 ( seed )
  q8_transpose_print ( q, '  The quaternion:' )

  print ( '' )
  print ( '  Now print without a label:' )
  print ( '' )

  q8_transpose_print ( q, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'Q8_TRANSPOSE_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  q8_transpose_print_test ( )
  timestamp ( )


