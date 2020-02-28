#! /usr/bin/env python
#
def r8vec2_print_some ( n, x1, x2, max_print, title ):

#*****************************************************************************80
#
#% R8VEC2_PRINT_SOME prints "some" of an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is two R8VEC's.
#
#    An R8VEC is a vector of R8 values.
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vectors, is no more than MAX_PRINT, then
#    the entire vectors are printed, one entry of each per line.
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
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vectors.
#
#    Input, real X1(N), X2(N), the vector to be printed.
#
#    Input, integer MAX_PRINT, the maximum number of lines to print.
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
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    print ( '......  ..............  ..............' )
    i = n - 1
    print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    i = max_print - 1
    print ( '%6d: %14g  %14g  ...more entries...' % ( i, x1[i], x2[i] ) )

  return

def r8vec2_print_some_test ( ):

#*****************************************************************************80
#
## R8VEC2_PRINT_SOME_TEST tests R8VEC2_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 100
  a = np.zeros ( n )
  b = np.zeros ( n )

  for i in range ( 0, n ):
    x = float ( i + 1 )
    a[i] = x * x
    b[i] = np.sqrt ( x )

  print ( '' )
  print ( 'R8VEC2_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_PRINT_SOME prints some of a pair of R8VEC\'s.' )

  r8vec2_print_some ( n, a, b, 10, '  Square and square root:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec2_print_some_test ( )
  timestamp ( )

