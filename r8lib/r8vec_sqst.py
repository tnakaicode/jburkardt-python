#! /usr/bin/env python
#
def r8vec_sqstb ( n, x ):

#*****************************************************************************80
#
## R8VEC_SQSTB computes a "slow" quarter sine transform backward of an R8VEC.
#
#  Discussion:
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 0 <= I <= N-1,
#
#      Y(I) = -2 Sum ( 1 <= J <= N-1 ) X(J) * sin ( PI * J * (I+1/2) / N )
#             - X(N) * cos ( pi * I )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Briggs, Van Emden Henson,
#    The Discrete Fourier Transform,
#    SIAM, 1995,
#    QA403.5 B75
#
#  Parameters:
#
#    Input, integer N, the number of data values.
#
#    Input, real X(N), the data sequence.
#
#    Output, real Y(N), the transformed data.
#
  import numpy as np

  y = np.zeros ( n )

  for i in range ( 0, n ):

    for j in range ( 0, n - 1 ):
      theta = 0.5 * np.pi * float ( j + 1 ) * float ( 2 * i + 1 ) / float ( n )
      y[i] = y[i] - 2.0 * x[j] * np.sin ( theta  )

    theta = np.pi * float ( i )
    y[i] = y[i] - x[n-1] * np.cos ( theta )

  return y

def r8vec_sqstf ( n, x ):

#*****************************************************************************80
#
## R8VEC_SQSTF computes a "slow" quarter sine transform forward of an R8VEC.
#
#  Discussion:
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 1 <= I <= N,
#
#      Y(I) = -(1/N) Sum ( 0 <= J <= N-1 ) X(J) * sin ( PI * I * (J+1/2) / N )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Briggs, Van Emden Henson,
#    The Discrete Fourier Transform,
#    SIAM, 1995,
#    QA403.5 B75
#
#  Parameters:
#
#    Input, integer N, the number of data values.
#
#    Input, real X(N), the data sequence.
#
#    Output, real Y(N), the transformed data.
#
  import numpy as np

  y = np.zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      theta = 0.5 * np.pi * float ( i + 1 ) * float ( 2 * j + 1 ) / float ( n )
      y[i] = y[i] + x[j] * np.sin ( theta  )

  for i in range ( 0, n ):
    y[i] = - y[i] / float ( n )

  return y

def r8vec_sqst_test ( ):

#*****************************************************************************80
#
## R8VEC_SQST_TEST tests R8VEC_SQSTB and R8VEC_SQSTF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2010
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print_part import r8vec_print_part
  from r8vec_uniform_ab import r8vec_uniform_ab

  n = 256
  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'R8VEC_SQST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_SQSTF does a forward slow quarter wave sine transform' )
  print ( '  R8VEC_SQSTB does a backward slow quarter wave sine transform.' )
  print ( '' )
  print ( '  The number of data items is N = %d' % ( n ) )
#
#  Set the data values.
#
  seed = 123456789

  x, seed = r8vec_uniform_ab ( n, alo, ahi, seed )

  r8vec_print_part ( n, x, 1, 10, '  The original data:' )
#
#  Compute the coefficients.
#
  y = r8vec_sqstf ( n, x )

  r8vec_print_part ( n, y, 1, 10, '  The sine coefficients:' )
#
#  Now compute inverse transform of coefficients.  Should get back the
#  original data.

  x = r8vec_sqstb ( n, y )

  r8vec_print_part ( n, x, 1, 10, '  The retrieved data:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_SQST_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_sqst_test ( )
  timestamp ( )
 
