#! /usr/bin/env python
#
def r8vec_sftb ( n, azero, a, b ):

#*****************************************************************************80
#
## R8VEC_SFTB computes a "slow" backward Fourier transform of an R8VEC.
#
#  Discussion:
#
#    SFTB and SFTF are inverses of each other.  If we begin with data
#    AZERO, A, and B, and apply SFTB to it, and then apply SFTF to the
#    resulting R vector, we should get back the original AZERO, A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of data values.
#
#    Input, real AZERO, the constant Fourier coefficient.
#
#    Input, real A(N/2), B(N/2), the Fourier coefficients.
#
#    Output, real R(N), the reconstructed data sequence.
#
  import numpy as np

  r = np.zeros ( n )
  for i in range ( 0, n ):
    r[i] = azero

  for i in range ( 0, n ):
    for k in range ( 0, ( n // 2 ) ):
      theta = float ( ( k + 1 ) * i * 2 ) * np.pi / float ( n )
      r[i] = r[i] + a[k] * np.cos ( theta ) + b[k] * np.sin ( theta )

  return r

def r8vec_sftf ( n, r ):

#*****************************************************************************80
#
## R8VEC_SFTF computes a "slow" forward Fourier transform of an R8VEC.
#
#  Discussion:
#
#    SFTF and SFTB are inverses of each other.  If we begin with data
#    R and apply SFTB to it, and then apply SFTB to the resulting AZERO, 
#    A, and B, we should get back the original R.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of data values.
#
#    Input, real R(N), the data to be transformed.
#
#    Output, real AZERO, = sum ( 1 <= I <= N ) R(I) / N.
#
#    Output, real A(N/2), B(N/2), the Fourier coefficients.
#
  import numpy as np

  a = np.zeros ( ( n // 2 ) )
  b = np.zeros ( ( n // 2 ) )

  azero = np.sum ( r ) / float ( n )

  for i in range ( 0, (  n // 2 ) ):

    a[i] = 0.0
    b[i] = 0.0

    for j in range ( 0, n ):
      theta = float ( 2 * ( i + 1 ) * j ) * np.pi / float ( n )
      a[i] = a[i] + r[j] * np.cos ( theta )
      b[i] = b[i] + r[j] * np.sin ( theta )

    a[i] = a[i] / float ( n )
    b[i] = b[i] / float ( n )

    if ( ( n % 2 ) == 1 or i + 1 != ( n // 2 ) ):
      a[i] = 2.0 * a[i]
      b[i] = 2.0 * b[i]
 
  return azero, a, b

def r8vec_sft_n_test ( n ):

#*****************************************************************************80
#
## R8VEC_SFT_N_TEST tests R8VEC_SFTB and R8VEC_SFTF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print_some import r8vec_print_some
  from r8vec_uniform_ab import r8vec_uniform_ab

  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'R8VEC_SFT_N_TEST' )
  print ( '  R8VEC_SFTF computes the forward slow Fourier transform.' )
  print ( '  R8VEC_SFTB computes the backward slow Fourier transform.' )
  print ( '' )
  print ( '  The number of data values, N = %d' % ( n ) )

  seed = 123456789

  x, seed = r8vec_uniform_ab ( n, alo, ahi, seed )

  r8vec_print_some ( n, x, 10, '  The original data:' )
#
#  Compute the slow Fourier transform of the data.
#
  azero, a, b = r8vec_sftf ( n, x )

  print ( '' )
  print ( '  A (cosine) coefficients:' )
  print ( '' )

  print ( '  %4d  %g' % ( 0, azero ) )

  for i in range ( 0, ( n // 2 ) ):
    print ( '  %4d  %g' % ( i, a[i] ) )

  print ( '' )
  print ( '  B (sine) coefficients:' )
  print ( '' )

  for i in range ( 0, ( n // 2 ) ):
    print ( '  %4d  %g' % ( i, b[i] ) )
#
#  Now try to retrieve the data from the coefficients.
#
  x = r8vec_sftb ( n, azero, a, b )

  r8vec_print_some ( n, x, 10, '  The retrieved data:' )

  return

def r8vec_sft_test ( ):

#*****************************************************************************80
#
## R8VEC_SFT_TEST tests R8VEC_SFTB and R8VEC_SFTF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'R8VEC_SFT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )

  r8vec_sft_n_test ( 35 )
  r8vec_sft_n_test ( 36 )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_SFT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_sft_test ( )
  timestamp ( )

