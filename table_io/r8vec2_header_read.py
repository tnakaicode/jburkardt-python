#! /usr/bin/env python
#
def r8vec2_header_read ( filename ):

#*****************************************************************************80
#
## R8VEC2_HEADER_READ reads the header from an R8VEC2 file.
#
#  Discussion:
#
#    An R8VEC2 is a pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the input file.
#
#    Output, integer M, the number of rows in the file.
#
  from file_column_count import file_column_count
  from file_row_count import file_row_count

  n = file_column_count ( filename )

  if ( n != 2 ):
    print ( '' )
    print ( 'R8VEC2_HEADER_READ - Fatal error!' )
    print ( '  The number of columns is not 2, but %d.' % ( n ) )
    exit ( 'R8VEC2_HEADER_READ - Fatal error!' )

  m = file_row_count ( filename )

  return m

def r8vec2_header_read_test ( ):

#*****************************************************************************80
#
## R8VEC2_HEADER_READ_TEST tests R8VEC2_HEADER_READ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC2_HEADER_READ_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_HEADER_READ counts rows in a file containing an R8VEC2.' )

  filename = 'r8vec2_write_test.txt'
  m = r8vec2_header_read ( filename )

  print ( '' )
  print ( '  File "%s" contains %d rows.' % ( filename, m ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_HEADER_READ_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec2_header_read_test ( )
  timestamp ( )
