#! /usr/bin/env python
#
def i4mat_sum ( m, n, a ):

#*****************************************************************************80
#
## I4MAT_SUM returns the sum of the entries in an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an M by N array of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer A(M,N), the matrix.
#
#    Output, integer VALUE, the sum of the entries.
#
  value = 0

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      value = value + a[i,j]

  return value

def i4mat_sum_test ( ):

#*****************************************************************************80
#
## I4MAT_SUM_TEST tests I4MAT_SUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 May 2018
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4mat_print import i4mat_print
  from i4mat_uniform_ab import i4mat_uniform_ab

  print ( '' )
  print ( 'I4MAT_SUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_SUM sums the entries in an I4MAT.' )

  m = 4
  n = 3
  a = 0
  b = 5
  seed = 123456789
  x, seed = i4mat_uniform_ab ( m, n, a, b, seed )

  i4mat_print ( m, n, x, '  The matrix:' )
  
  x_sum = i4mat_sum ( m, n, x )

  print ( '' )
  print ( '  Sum of entries = %d' % ( x_sum ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_SUM_TEST' )
  print ( '  Normal_end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_sum_test ( )
  timestamp ( )
