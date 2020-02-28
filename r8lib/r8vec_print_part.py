#! /usr/bin/env python
#
def r8vec_print_part ( n, a, i_lo, i_hi, title ):

#*****************************************************************************80
#
## R8VEC_PRINT_PART prints "part" of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8 values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, integer MAX_PRINT, the maximum number of lines to print.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )

  for i in range ( max ( 0, i_lo ), min ( n, i_hi + 1 ) ):
    print ( '  %8d: %12g' % ( i, a[i] ) )

  return

def r8vec_print_part_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_PART_TEST tests R8VEC_PRINT_PART.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_indicator1 import r8vec_indicator1

  print ( '' )
  print ( 'R8VEC_PRINT_PART_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT_PART prints part of an R8VEC.' )

  n = 100
  a = r8vec_indicator1 ( n )

  r8vec_print_part ( n, a, 10, 20, '  Lines 10:20 of the vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_PART_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_print_part_test ( )
  timestamp ( )
