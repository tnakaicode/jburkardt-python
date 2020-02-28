#! /usr/bin/env python
#
def r8rows_to_r8mat ( m, n, r8rows ):

#*****************************************************************************80
#
## R8ROWS_TO_R8MAT converts a row-major vector to an R8MAT.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, in column major order.
#
#    I am frustrated that the FORTRAN standard for initializing an array
#    forces me to enter a table of data by columns, so that I have to
#    transpose the information, which is confusing to me and any reader.
#
#    This function allows me to declare a vector of the right type and length,
#    fill it with data that I can display row-wise, and then have the
#    data copied into a column-major doubly-indexed array.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real R8ROWS(M*N), the data. stored rowwise
#    in a vector.
#
#    Output, real R8MAT(M,N), a copy of the data, stored
#    columnwise in an array.
#
  import numpy as np

  k = 0
  r8mat = np.zeros ( [ m, n ] )
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      r8mat[i,j] = r8rows[k]
      k = k + 1

  return r8mat

def r8rows_to_r8mat_test ( ):

#*****************************************************************************80
#
## R8ROWS_TO_R8MAT_TEST tests R8ROWS_TO_R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  m = 3
  n = 4
  r8rows = np.array ( [ \
    11.0, 12.0, 13.0, 14.0, \
    21.0, 22.0, 23.0, 24.0, \
    31.0, 32.0, 33.0, 34.0 ] )

  print ( '' )
  print ( 'R8ROWS_TO_R8MAT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8ROWS_TO_R8MAT allows an R8MAT to be initialized' )
  print ( '  by data stored ROW-WISE in a vector.' )

  r8vec_print ( m * n, r8rows, '  The data vector:' )

  r8mat = r8rows_to_r8mat ( m, n, r8rows )

  r8mat_print ( m, n, r8mat, '  The data copied into an array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROWS_TO_R8MAT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8rows_to_r8mat_test ( )
  timestamp ( )

