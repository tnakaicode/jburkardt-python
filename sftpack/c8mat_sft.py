#! /usr/bin/env python
#
def c8mat_sftb ( n1, n2, y ):

#*****************************************************************************80
#
## C8MAT_SFTB computes a "slow" backward Fourier transform of a C8MAT.
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
#    For 0 <= I1 <= N1 - 1,
#        0 <= I2 <= N2 - 1,
#
#      X(I1,I2) = Sum ( 0 <= K2 <= N2 - 1 ) Sum ( 0 <= K1 <= N1 - 1 )
#        Y(K1,K2) * exp ( 2 pi i I1 K1 / N1 ) * exp ( 2 pi i I2 K2 / N2 )
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
#    Input, integer N1, N2, the number of rows and columns of data.
#
#    Input, complex Y(0:N1-1,0:N2-1), the Fourier coefficients.
#
#    Output, complex X(0:N1-1,0:N2-1), the data.
#
  import numpy as np

  x = np.zeros ( [ n1, n2 ], dtype = np.complex128 )

  for i2 in range ( 0, n2 ):
    for j2 in range ( 0, n2 ):
      theta2 = 2.0 * np.pi * float ( i2 ) * float ( j2 ) / float ( n2 )
      cs2 = np.cos ( theta2 ) - 1j * np.sin ( theta2 )
      for i1 in range ( 0, n1 ):
        for j1 in range ( 0, n1 ):
          theta1 = 2.0 * np.pi * float ( i1 ) * float ( j1 ) / float ( n1 )
          cs1 = np.cos ( theta1 ) - 1j * np.sin ( theta1 )
          x[i1,i2] = x[i1,i2] + y[j1,j2] * cs1 * cs2

  for i2 in range ( 0, n2 ):
    for i1 in range ( 0, n1 ):
      x[i1,i2] = x[i1,i2] / float ( n1 * n2 )

  return x

def c8mat_sftf ( n1, n2, x ):

#*****************************************************************************80
#
## C8MAT_SFTF computes a "slow" forward Fourier transform of a C8MAT.
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
#    For 0 <= I1 <= N1 - 1,
#        0 <= I2 <= N2 - 1,
#
#      Y(I1,I2) = Sum ( 0 <= K2 <= N2 - 1 ) Sum ( 0 <= K1 <= N1 - 1 )
#        X(K1,K2) * exp ( - 2 pi i I1 K1 / N1 ) * exp ( - 2 pi i I2 K2 / N2 )
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
#    Input, integer N1, N2, the number of rows and columns of data.
#
#    Input, complex X(0:N1-1,0:N2-1), the data to be transformed.
#
#    Output, complex Y(0:N1-1,0:N2-1), the Fourier coefficients.
#
  import numpy as  np

  y = np.zeros ( [ n1, n2 ], dtype = np.complex128 )

  for i2 in range ( 0, n2 ):
    for j2 in range ( 0, n2 ):
      theta2 = - 2.0 * np.pi * float ( i2 ) * float ( j2 ) / float ( n2 )
      cs2 = np.cos ( theta2 ) - 1j * np.sin ( theta2 )
      for i1 in range ( 0, n1 ):
        for j1 in range ( 0, n1 ):
          theta1 = - 2.0 * np.pi * float ( i1 ) * float ( j1 ) / float ( n1 )
          cs1 = np.cos ( theta1 ) - 1j * np.sin ( theta1 )
          y[i1,i2] = y[i1,i2] + x[j1,j2] * cs1 * cs2

  return y

def c8mat_sft_test ( ):

#*****************************************************************************80
#
## C8MAT_SFT_TEST tests C8MAT_SFTB and C8MAT_SFTF.
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
  from c8mat_print_some import c8mat_print_some
  from c8mat_uniform_01 import c8mat_uniform_01

  n1 = 10
  n2 = 4

  print ( '' )
  print ( 'C8MAT_SFT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8MAT_SFTF computes the forward slow Fourier transform.' )
  print ( '  C8MAT_SFTB computes the backward slow Fourier transform.' )
  print ( '' )
  print ( '  The data has dimension N1 = %d by N2 = %d' % ( n1, n2 ) )

  seed = 123456789

  x, seed = c8mat_uniform_01 ( n1, n2, seed )

  c8mat_print_some ( n1, n2, x, 1, 1, 10, 10, '  The data X:' )
#
#  Compute the slow Fourier transform of the data.
#
  y = c8mat_sftf ( n1, n2, x )

  c8mat_print_some ( n1, n2, y, 1, 1, 10, 10, '  The Fourier coefficients Y:' )

  x2 = c8mat_sftb ( n1, n2, y )

  c8mat_print_some ( n1, n2, x2, 1, 1, 10, 10, '  The recovered data:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8MAT_SFT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8mat_sft_test ( )
  timestamp ( )
 
