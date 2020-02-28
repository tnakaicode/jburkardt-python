#! /usr/bin/env python
#
def r8mat_add ( m, n, alpha, a, beta, b ):

#*****************************************************************************80
#
## R8MAT_ADD computes C = alpha * A + beta * B for R8MAT's.
#
#  Discussion:
#
#    An R8MAT is an array of R8 values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real ALPHA, the multiplier for A.
#
#    Input, real A(M,N), the first matrix.
#
#    Input, real BETA, the multiplier for A.
#
#    Input, real B(M,N), the second matrix.
#
#    Output, real C(M,N), the sum of alpha*A+beta*B.
#
  import numpy as np

  c = np.zeros ( [ m, n ] )

  c = alpha * a + beta * b

# for i in range ( 0, m ):
#   for j in range ( 0, n ):
#     c[i.j] = alpha * a[i.j] + beta * b[i.j]

  return c

def r8mat_add_test ( ):

#*****************************************************************************80
#
## R8MAT_ADD_TEST tests R8MAT_ADD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_indicator import r8mat_indicator
  from r8mat_print import r8mat_print
  from r8mat_transpose import r8mat_transpose

  m = 4
  n = 4

  print ( '' )
  print ( 'R8MAT_ADD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_ADD computes C = alpha * A + beta * B for R8MATs.' )

  alpha = 3.0

  a = r8mat_indicator ( m, n )

  beta = 0.5

  b = r8mat_indicator ( n, m )
  b = r8mat_transpose ( n, m, b )

  c = r8mat_add ( m, n, alpha, a, beta, b )

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )

  print ( '' )
  print ( '  ALPHA = %g, BETA = %g' % ( alpha, beta ) )

  r8mat_print ( m, n, c, '  C = alpha * A + beta * B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_ADD_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_add_test ( )
  timestamp ( )

