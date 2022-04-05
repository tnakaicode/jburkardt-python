#! /usr/bin/env python
#
def r8vec_multinormal_pdf ( n, mu, r, c_det, x ):

#*****************************************************************************80
#
## R8VEC_MULTINORMAL_PDF evaluates a multivariate normal PDF.
#
#  Discussion:
#
#    PDF ( MU(1:N), C(1:N,1:N); X(1:N) ) = 
#      1 / ( 2 * pi ) ^ ( N / 2 ) * 1 / det ( C )
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
#    03 August 2015
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
#    Input, real C_DET, the determinant of the
#    covariance matrix C.
#
#    Input, real X(N), a sample of the distribution.
#
#    Output, real VALUe, the PDF evaluated
#    at X.
#
  import numpy as np
  from r8ut import r8ut_slt
#
#  Compute:
#    inverse(R')*(x-mu) = y
#  by solving:
#    R'*y = x-mu
#
  b = x - mu
  y = r8ut_slt ( n, r, b )
#
#  Compute:
#    (x-mu)' * inv(C)          * (x-mu)
#  = (x-mu)' * inv(R'*R)       * (x-mu)
#  = (x-mu)' * inv(R) * inv(R) * (x-mu)
#  = y' * y.
#
  xcx = np.dot ( y, y )

  value = 1.0 / np.sqrt ( ( 2.0 * np.pi ) ** n ) \
  * 1.0 / np.sqrt ( c_det ) \
  * np.exp ( - 0.5 * xcx )

  return value

def r8vec_multinormal_pdf_test ( ):

#*****************************************************************************80
#
## R8VEC_MULTINORMAL_PDF_TEST tests R8VEC_MULTINORMAL_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from initialize import initialize
  from r8_normal_01_sample import r8_normal_01_sample
  from r8_uniform_01_sample import r8_uniform_01_sample
  from r8ge import r8ge_to_r8po
  from r8ge import r8ge_print
  from r8po import r8po_det
  from r8po import r8po_fa
  from r8po import r8po_inverse
  from r8po import r8po_mv
  from r8po import r8po_print
  from r8ut import r8ut_print
  from r8ut import r8ut_zeros
  from r8vec_print import r8vec_print

  initialize ( )

  n = 5

  print ( '' )
  print ( 'R8VEC_MULTINORMAL_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MULTINORMAL_PDF evaluates the PDF for the' )
  print ( '  multinormal distribution.' )
  print ( '' )
  print ( '  The covariance matrix is C.' )
  print ( '  The definition uses the inverse of C;' )
  print ( '  R8VEC_MULTINORMAL_PDF uses the Cholesky factor R' )
  print ( '  Verify that the algorithms are equivalent.' )
#
#  Generate a random upper triangular matrix with positive diagonal.
#
  r1 = r8ut_zeros ( n, n )

  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      r1[i,j] = r8_uniform_01_sample ( )

  r8ut_print ( n, n, r1, '  R1:' );
#
#  Compute a positive definite symmetric covariance matrix C.
#
  c_ge = np.dot ( np.transpose ( r1 ), r1 )

  r8ge_print ( n, n, c_ge, '  C:' )
#
#  Convert to R8PO format.
#
  c = r8ge_to_r8po ( n, c_ge )
#
#  Compute the Cholesky factor R.
#
  r2 = r8po_fa ( n, c )

  r8ut_print ( n, n, r2, '  R2:' );
#
#  Compute the determinant of C.
#
  c_det = r8po_det ( n, r2 )
  print ( '' )
  print ( '  Determinant of C = %g' % ( c_det ) )
#
#  Compute the inverse of C.
#
  c_inv = r8po_inverse ( n, r2 )
  r8po_print ( n, c_inv, '  inverse(C):' )
#
#  Compute a random set of means.
#
  mu = np.zeros ( n )
  for i in range ( 0, n ):
    mu[i] = r8_normal_01_sample ( )
  r8vec_print ( n, mu, '  MU:' )
#
#  Compute X as small variations from MU.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    eps = 0.01 * r8_normal_01_sample ( )
    x[i] = ( 1.0 + eps ) * mu[i]
  r8vec_print ( n, x, '  X: ' );
#
#  Compute PDF1 from the function.
#
  pdf1 = r8vec_multinormal_pdf ( n, mu, r2, c_det, x )
#
#  Compute PDF2 from the definition.
#
  y = x - mu

  ciy = r8po_mv ( n, c_inv, y )

  xcx = np.dot ( y, ciy )

  pdf2 = 1.0 / np.sqrt ( ( 2.0 * np.pi ) ** n ) \
  * 1.0 / np.sqrt ( c_det ) * np.exp ( - 0.5 * xcx )

  print ( '' )
  print ( '  PDF1 = %g' % ( pdf1 ) )
  print ( '  PDF2 = %g' % ( pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MULTINORMAL_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_multinormal_pdf_test ( )
  timestamp ( )
 
