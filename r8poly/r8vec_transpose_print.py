#! /usr/bin/env python3
#
def r8vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_TRANSPOSE_PRINT prints an R8VEC "transposed".
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Example:
#
#    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
#    TITLE = 'My vector:  '
#
#    My vector:   1.0    2.1    3.2    4.3    5.4
#                 6.5    7.6    8.7    9.8   10.9
#                11.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  title_length = len ( title )

  for ilo in range ( 0, n, 5 ):

    if ( ilo == 0 ):
      print ( title ),
    else:
      blanks = ''
      for i in range ( 0, title_length ):
        blanks = blanks + ' '
      print ( blanks ),

    print ( '  ' ),

    ihi = min ( ilo + 5 - 1, n - 1 )

    for i in range ( ilo, ihi + 1 ):
      print ( '  %12g' % ( a[i] ) ),
    print ( '' )

  return

def r8vec_transpose_print_test ( ):

#*****************************************************************************80
#
## R8VEC_TRANSPOSE_PRINT_TEST tests R8VEC_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_uniform_01 import r8vec_uniform_01

  n = 12
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_TRANSPOSE_PRINT prints an R8VEC "tranposed",' )
  print ( '  that is, placing multiple entries on a line.' )

  x, seed = r8vec_uniform_01 ( n, seed )

  r8vec_transpose_print ( n, x, '  The vector X:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_TRANSPOSE_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_transpose_print_test ( )
  timestamp ( )
 
