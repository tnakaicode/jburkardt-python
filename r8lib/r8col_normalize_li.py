#! /usr/bin/env python
#
def r8col_normalize_li ( m, n, a ):

#*****************************************************************************80
#
## R8COL_NORMALIZE_LI normalizes an R8COL with the column infinity norm.
#
#  Discussion:
#
#    Each column is scaled so that the entry of maximum norm has the value 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the array to be examined.
#
#    Output, real B(M,N), the normalize array.
#
  import numpy as np

  b = a.copy ( )

  for j in range ( 0, n ):

    c = a[0,j]
    for i in range ( 1, m ):
      if ( abs ( c ) < abs ( a[i,j] ) ):
        c = a[i,j]

    if ( c != 0.0 ):
      b[0:m,j] = b[0:m,j] / c

  return b

def r8col_normalize_li_test ( ):

#*****************************************************************************80
#
## R8COL_NORMALIZE_LI_TEST tests R8COL_NORMALIZE_LI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8COL_NORMALIZE_LI_TEST:' )
  print ( '  R8COL_NORMALIZE_LI normalizes an array A, dividing each' )
  print ( '  column by its maximum element.' )

  m = 5
  n = 4
  a = np.random.random ( [ m, n ] )

  r8mat_print ( m, n, a, '  Matrix A:' )

  b = r8col_normalize_li ( m, n, a )

  r8mat_print ( m, n, b, '  Matrix after column LI normalization:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8COL_NORMALIZE_LI_TEST:' )
  print ( '  Normale end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8col_normalize_li_test ( )
  timestamp ( )

