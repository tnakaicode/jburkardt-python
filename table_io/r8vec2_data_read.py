#! /usr/bin/env python
#
def r8vec2_data_read ( filename, m ):

#*****************************************************************************80
#
## R8VEC2_DATA_READ reads the data from an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is an pair of R8VEC's.
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
#    Input, integer M, the number of rows in the file.
#
#    Output, real X(M), Y(M), the data.
#
  import numpy as np

  input = open ( filename, 'r' )

  x = np.zeros ( m )
  y = np.zeros ( m )

  i = 0
  for line in input:

    if ( line[0] == '#' ):
      continue
    else:
      data = line.split ( )
      x[i] = data[0]
      y[i] = data[1]
      i = i + 1

  input.close ( )

  return x, y

def r8vec2_data_read_test ( ):

#*****************************************************************************80
#
## R8VEC2_DATA_READ_TEST tests R8VEC2_DATA_READ.
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
  import platform
  from r8vec2_print import r8vec2_print

  print ( '' )
  print ( 'R8VEC2_DATA_READ_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_DATA_READ reads data from an R8VEC2.' )

  m = 5
  filename = 'r8vec2_write_test.txt'
  x, y = r8vec2_data_read ( filename, m )
  r8vec2_print ( m, x, y, '  Data read from file:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_DATA_READ_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec2_data_read_test ( )
  timestamp ( )
