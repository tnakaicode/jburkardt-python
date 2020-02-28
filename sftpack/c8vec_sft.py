#! /usr/bin/env python
#
def c8vec_sftb ( n, y ):

#*****************************************************************************80
#
## C8VEC_SFTB computes a "slow" backward Fourier transform of a C8VEC.
#
#  Discussion:
#
#    SFTF and SFTB are inverses of each other.  If we begin with data
#    X and apply SFTF to get Y, and then apply SFTB to Y,
#    we should get back the original X.
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 0 <= I <= N - 1
#
#      X(I) = 1/N * Sum ( 0 <= J <= N - 1 ) Y(J) * exp ( 2 pi i I J / N )
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
#  Parameters:
#
#    Input, integer N, the number of data values.
#
#    Input, complex Y(0:N-1), the Fourier coefficients.
#
#    Output, complex X(0:N-1), the data.
#
  import numpy as np

  x = np.zeros ( n, dtype = np.complex128 )

  for k in range ( 0, n ):
    for j in range ( 0, n ):
      theta = - 2.0 * np.pi * float ( k ) * float ( j ) / float ( n )
      x[k] = x[k] + y[j] * ( np.cos ( theta ) + 1j * np.sin ( theta ) )

  for i in range ( 0, n ):
    x[i] = x[i] / float ( n )

  return x

def c8vec_sftf ( n, x ):

#*****************************************************************************80
#
## C8VEC_SFTF computes a "slow" forward Fourier transform of a C8VEC.
#
#  Discussion:
#
#    SFTF and SFTB are inverses of each other.  If we begin with data
#    X and apply SFTF to get Y, and then apply SFTB to Y,
#    we should get back the original X.
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 0 <= I <= N - 1
#
#      Y(I) = Sum ( 0 <= J <= N - 1 ) X(J) * exp ( - 2 pi i I J / N )
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
#  Parameters:
#
#    Input, integer N, the number of data values.
#
#    Input, complex X(0:N-1), the data to be transformed.
#
#    Output, complex Y(0:N-1), the Fourier coefficients.
#
  import numpy as np

  y = np.zeros ( n, dtype = np.complex128 )

  for k in range ( 0, n ):
    for j in range ( 0, n ):
      theta = - 2.0 * np.pi * float ( k ) * float ( j ) / float ( n )
      y[k] = y[k] + x[j] * ( np.cos ( theta ) - 1j * np.sin ( theta ) )

  return y

def c8vec_sft_test ( ):

#*****************************************************************************80
#
## C8VEC_SFT_TEST tests C8VEC_SFTB and C8VEC_SFTF.
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
  import platform
  from c8vec_print_part import c8vec_print_part
  from c8vec_uniform_01 import c8vec_uniform_01

  n = 36

  print ( '' )
  print ( 'C8VEC_SFT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8VEC_SFTF computes the forward slow Fourier transform.' )
  print ( '  C8VEC_SFTB computes the backward slow Fourier transform.' )
  print ( '' )
  print ( '  The number of data values, N = %d' % ( n ) )

  seed = 123456789

  x, seed = c8vec_uniform_01 ( n, seed )

  c8vec_print_part ( n, x, 10, '  The original data:' )
#
#  Compute the slow Fourier transform of the data.
#
  y = c8vec_sftf ( n, x )

  c8vec_print_part ( n, y, 10, '  The Fourier coefficients:' )
#
#  Now try to retrieve the data from the coefficients.
#
  x2 = c8vec_sftb ( n, y )

  c8vec_print_part ( n, x2, 10, '  The retrieved data:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8VEC_SFT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_sft_test ( )
  timestamp ( )

