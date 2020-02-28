#! /usr/bin/env python
#
def r8vec_multinormal_sample ( n, mu, r ):

#*****************************************************************************80
#
## R8VEC_MULTINORMAL_SAMPLE samples a multivariate normal PDF.
#
#  Discussion:
#
#    PDF ( MU(1:N), C(1:N,1:N); X(1:N) ) = 
#      1 / ( 2 * pi ) ^ ( N / 2 ) * 1 / sqrt ( det ( C ) )
#      * exp ( - ( X - MU )' * inverse ( C ) * ( X - MU ) / 2 )
#
#    Here,
#
#      X is the argument vector of length N,
#      MU is the mean vector of length N,
#      C is an N by N positive definite symmetric covariance matrix.
#
#    The properties of C guarantee that it has an upper triangular
#    matrix R, the Cholesky factor, such that C = R' * R.  It is the
#    matrix R that is required by this routine.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the spatial dimension.
#
#    Input, real MU(N), the mean vector.
#
#    Input, real R(N,N), the upper triangular Cholesky
#    factor of the covariance matrix C.
#
#    Output, real X(N), a sample of the distribution.
#
  import numpy as np
  from r8_normal_01_sample import r8_normal_01_sample
#
#  Compute X = MU + R' * Z
#  where Z is a vector of standard normal variates.
#
  z = np.zeros ( n );
  for j in range ( 0, n ):
    z[j] = r8_normal_01_sample ( )

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = mu[i]
    for j in range ( 0, i + 1 ):
      x[i] = x[i] + r[j,i] * z[j]

  return x

def r8vec_multinormal_sample_test ( ):

#*****************************************************************************80
#
## R8VEC_MULTINORMAL_SAMPLE_TEST tests R8VEC_MULTINORMAL_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from initialize import initialize
  from r8_uniform_01_sample import r8_uniform_01_sample
  from r8po import r8po_dif2
  from r8vec_multinormal_pdf import r8vec_multinormal_pdf
  from r8vec_uniform_ab import r8vec_uniform_ab

  initialize ( )

  seed = 123456789

  n = 5
#
#  Set the covariance matrix C.
#
  c = r8po_dif2 ( n )
#
#  Set the determinant.
#
  c_det = float ( n + 1 )
#
#  Set the upper triangular Cholesky factor.
#
  r = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    r[i,i] = np.sqrt ( float ( i + 2 ) ) / np.sqrt ( float ( i + 1 ) )

  for i in range ( 1, n ):
    r[i-1,i] = - np.sqrt ( float ( i ) ) / np.sqrt ( float ( i + 1 ) )

  print ( '' )
  print ( 'R8VEC_MULTINORMAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MULTINORMAL_SAMPLE samples the multinormal distribution.' )
  print ( '' )
  print ( '     N     I      MU        X           PDF()' )

  for k in range ( 0, 10 ):
    mu, seed = r8vec_uniform_ab ( n, -5.0, +5.0, seed )
    x = r8vec_multinormal_sample ( n, mu, r )
    pdf = r8vec_multinormal_pdf ( n, mu, r, c_det, x )
    print ( '' )
    for i in range ( 0, n ):
      print ( '        %4d  %8.4f  %8.4f' % ( i, mu[i], x[i] ) )
    print ( '  %4d                            %14.6g' % ( n, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MULTINORMAL_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  timestamp ( )
  initialize ( )
  r8vec_multinormal_sample_test ( )
  timestamp ( )

