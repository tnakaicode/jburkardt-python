#! /usr/bin/env python
#
def c8vec_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## C8VEC_PRINT_PART prints "part" of an C8VEC.
#
#  Discussion:
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_PRINT, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vector.
#
#    Input, complex A(N), the vector to be printed.
#
#    Input, integer MAX_PRINT, the maximum number of lines
#    to print.
#
#    Input, string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )
    print ( '  ......  ..............  ..............' )
    i = n - 1
    print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )
    i = max_print - 1
    print ( '  %6d  %14g  %14g  ...more entries...' % ( i, a.real[i], a.imag[i] ) )

  return

def c8vec_print_part_test ( ):

#*****************************************************************************80
#
## C8VEC_PRINT_PART_TEST tests C8VEC_PRINT_PART.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from c8vec_indicator import c8vec_indicator

  print ( '' )
  print ( 'C8VEC_PRINT_PART_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8VEC_PRINT_PART prints part of a C8VEC.' )

  n = 100
  a = c8vec_indicator ( n )

  max_print = 10

  c8vec_print_part ( n, a, max_print, '  Part of the C8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8VEC_PRINT_PART_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_print_part_test ( )
  timestamp ( )

