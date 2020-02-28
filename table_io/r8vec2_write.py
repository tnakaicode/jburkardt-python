#! /usr/bin/env python
#
def r8vec2_write ( filename, n, a, b ):

#*****************************************************************************80
#
## R8VEC2_WRITE writes an R8VEC2 to a file.
#
#  Discussion:
#
#    An R8VEC2 is a pair of vectors of R8's.
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
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), B(N), the vectors.
#
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g  %g\n' % ( a[i], b[i] )
    output.write ( s )

  output.close ( )

  return

def r8vec2_write_test ( ):

#*****************************************************************************80
#
## R8VEC2_WRITE_TEST tests R8VEC2_WRITE.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC2_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test R8VEC2_WRITE, which writes an R8VEC2 to a file.' )

  filename = 'r8vec2_write_test.txt'
  n = 5
  a = np.array ( [ 1.1, 1.2, 1.3, 1.4, 1.5 ] )
  b = np.array ( [ 1.2, 2.2, 3.2, 4.2, 5.2 ] )
  r8vec2_write ( filename, n, a, b )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec2_write_test ( )
  timestamp ( )

