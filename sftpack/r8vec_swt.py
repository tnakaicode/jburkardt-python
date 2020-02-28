#! /usr/bin/env python
#
def r8vec_swtb ( n, s, d ):

#*****************************************************************************80
#
## R8VEC_SWTB computes a "slow" backward wavelet transform of an R8VEC.
#
#  Discussion:
#
#    This function inverts the D4 Daubechies wavelet.
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
#    Input, real S((N+1)/2), D((N+1)/2), the transformed data.
#
#    Output, real X(N), the original data sequence.
#
  import numpy as np
  from i4_wrap import i4_wrap

  if ( ( n % 2 ) == 1 ):
    n2 = n + 1
  else:
    n2 = n

  np1h = ( ( n + 1 ) // 2 )
  nh = ( n // 2 )

  for i in range ( 0, np1h ):
    d[i] = d[i] / ( ( np.sqrt ( 3.0 ) + 1.0 ) / np.sqrt ( 2.0 ) )
    s[i] = s[i] / ( ( np.sqrt ( 3.0 ) - 1.0 ) / np.sqrt ( 2.0 ) )

  for i in range ( 0, np1h ):
    ip1 = i4_wrap ( i + 1, 0, np1h - 1 )
    s[i] = s[i] + d[ip1]

  y = np.zeros ( n2 )

  for i in range ( 0, np1h ):
    im1 = i4_wrap ( i - 1, 0, np1h - 1 )
    y[2*i+1] = d[i] + np.sqrt ( 3.0 ) / 4.0 * s[i] \
      + ( np.sqrt ( 3.0 ) - 2.0 ) / 4.0 * s[im1]

  for i in range ( 0, np1h ):
    y[2*i] = s[i] - np.sqrt ( 3.0 ) * y[2*i+1]

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = y[i]

  return x

def r8vec_swtf ( n, x ):

#*****************************************************************************80
#
## R8VEC_SWTF computes a "slow" forward wavelet transform of an R8VEC.
#
#  Discussion:
#
#    This function applies the D4 Daubechies wavelet.
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
#    Input, real X(N), the data sequence.
#
#    Output, real S((N+1)/2), D((N+1)/2), the transformed data.
#
  import numpy as np
  from i4_wrap import i4_wrap

  if ( ( n % 2 ) == 1 ):
    n2 = n + 1
  else:
    n2 = n

  y = np.zeros ( n2 )

  for i in range ( 0, n ):
    y[i] = x[i]

  if ( n < n2 ):
    y[n] = 0.0

  np1h = ( ( n + 1 ) // 2 )

  d = np.zeros ( np1h )
  s = np.zeros ( np1h )

  for i in range ( 0, np1h ):
    s[i] = y[2*i] + np.sqrt ( 3.0 ) * y[2*i+1]

  for i in range ( 0, np1h ):
    im1 = i4_wrap ( i - 1, 0, np1h - 1 )
    d[i] = y[2*i+1] - np.sqrt ( 3.0 ) / 4.0 * s[i] \
      - ( np.sqrt ( 3.0 ) - 2.0 ) / 4.0 * s[im1]

  for i in range ( 0, np1h ):
    ip1 = i4_wrap ( i + 1, 0, np1h - 1 )
    s[i] = s[i] - d[ip1]

  for i in range ( 0, np1h ):
    s[i] = ( np.sqrt ( 3.0 ) - 1.0 ) / np.sqrt ( 2.0 ) * s[i]
    d[i] = ( np.sqrt ( 3.0 ) + 1.0 ) / np.sqrt ( 2.0 ) * d[i]

  return s, d

def r8vec_swt_test ( ):

#*****************************************************************************80
#
## R8VEC_SWT_TEST tests R8VEC_SWTB and R8VEC_SWTF.
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
  from r8vec_print_part import r8vec_print_part
  from r8vec_uniform_ab import r8vec_uniform_ab

  n = 36
  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'R8VEC_SWT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_SWTF computes the forward slow wavelet transform.' )
  print ( '  R8VEC_SWTB computes the backward slow wavelet transform.' )
  print ( '' )
  print ( '  The number of data values, N = %d' % ( n ) )

  seed = 123456789

  x, seed = r8vec_uniform_ab ( n, alo, ahi, seed )

  r8vec_print_part ( n, x, 1, 10, '  The original data:' )
#
#  Compute the slow wavelet transform of the data.
#
  s, d = r8vec_swtf ( n, x )

  print ( '' )
  print ( '     I          S(I)            D(I)' )
  print ( '' )
  for i in range ( 0, ( ( n + 1 ) // 2 ) ):
    print ( '  %4d  %14f  %14f' % ( i, s[i], d[i] ) )
#
#  Now try to retrieve the data from the coefficients.
#
  x = r8vec_swtb ( n, s, d )

  r8vec_print_part ( n, x, 1, 10, '  The retrieved data:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_SWT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_swt_test ( )
  timestamp ( )
 
