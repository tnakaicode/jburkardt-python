#! /usr/bin/env python
#
def i4rows_to_i4mat ( m, n, i4rows ):

#*****************************************************************************80
#
## I4ROWS_TO_I4MAT converts a row-major vector to an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an MxN array of I4's, in column major order.
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
#    09 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer I4ROWS(M*N), the data. stored rowwise
#    in a vector.
#
#    Output, integer I4MAT(M,N), a copy of the data, stored
#    columnwise in an array.
#
  import numpy as np

  k = 0
  i4mat = np.zeros ( [ m, n ] )
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      i4mat[i,j] = i4rows[k]
      k = k + 1

  return i4mat

def i4rows_to_i4mat_test ( ):

#*****************************************************************************80
#
## I4ROWS_TO_I4MAT_TEST tests I4ROWS_TO_I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print
  from i4vec_print import i4vec_print

  m = 3
  n = 4
  i4rows = np.array ( [ \
    11, 12, 13, 14, \
    21, 22, 23, 24, \
    31, 32, 33, 34 ] )

  print ( '' )
  print ( 'I4ROWS_TO_I4MAT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4ROWS_TO_I4MAT allows an I4MAT to be initialized' )
  print ( '  by data stored ROW-WISE in a vector.' )

  i4vec_print ( m * n, i4rows, '  The data vector:' )

  i4mat = i4rows_to_i4mat ( m, n, i4rows )

  i4mat_print ( m, n, i4mat, '  The data copied into an array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4ROWS_TO_I4MAT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4rows_to_i4mat_test ( )
  timestamp ( )

