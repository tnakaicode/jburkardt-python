

def sample_paths2_eigen ( n, n2, rhomin, rhomax, rho0, correlation2 ):

#*****************************************************************************80
#
## sample_paths2_eigen(): sample paths for nonstationary correlation functions.
#
#  Discussion:
#
#    This function does not assume that the correlation function
#    C(S,T) is actually a function of |S-T|.
#
#    This method uses the eigen-decomposition of the correlation matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points on each path.
#
#    integer N2, the number of paths.
#
#    real RHOMIN, RHOMAX, the minimum and maximum values of RHO.
#
#    real RHO0, the correlation length.
#
#    CORRELATION2, a handle for a correlation function, which has
#    the form c = correlation2 ( m, n, s, t, rho0 ).
#
#  Output:
#
#    real X(N,N2), the sample paths.
#
  import numpy as np
  from numpy.random import default_rng

  rng = default_rng ( )
#
#  Choose 2 equal N vectors of equally spaced sample points from RHOMIN to RHOMAX.
#
  s = np.linspace ( rhomin, rhomax, n )
#
#  Evaluate the correlation function.
#
  cor = correlation2 ( n, n, s, s, rho0 )
#
#  Get the eigendecomposition of COR:
#
#    COR = V * D * V'.
#
#  Because COR is symmetric, V is orthogonal.
#
  [ v, d ] = eig ( cor )
#
#  We assume COR is non-negative definite, and hence that there
#  are no negative eigenvalues.  If this is not the case,
#  warn the user, hope the numbers are only slightly negative,
#  and reset them to 0.
#
  dmin = min ( min ( d ) )

  if ( dmin < - np.sqrt ( eps ) ):
    print ( '' )
    print ( 'SAMPLE_PATHS2_EIGEN - Warning!' )
    print ( '  Negative eigenvalues observed as low as ', dmin )

  d = max ( d, 0.0 )
#
#  Compute the eigenvalues of the factor C.
#
  sqrt_d = np.sqrt ( d )
#
#  Compute C, such that C' * C = COR.
#
  c = v * np.sqrt_d * v.T
#
#  Compute N independent random normal values.
#
  r = rng.standard_normal ( size = [ n, n2 ] )
#
#  Get the variables X which have correlation COR.
#
  x = np.matmul ( c, r )

  return x



def sample_paths_eigen ( n, n2, rhomax, rho0, correlation ):

#*****************************************************************************80
#
## sample_paths_eigen(): sample paths for stationary correlation functions.
#
#  Discussion:
#
#    This method uses the eigen-decomposition of the correlation matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points on each path.
#
#    integer N2, the number of paths.
#
#    real RHOMAX, the maximum value of RHO.
#
#    real RHO0, the correlation length.
#
#    CORRELATION, a handle for a correlation function.
#
#  Output:
#
#    real X[N,N2], the sample paths.
#
  import numpy as np
  from numpy.random import default_rng

  rng = default_rng ( )
#
#  Choose N equally spaced sample points from 0 to RHOMAX.
#
  rho_vec = np.linspace ( 0.0, rhomax, n )
#
#  Evaluate the correlation function.
#
  cor_vec = correlation ( n, rho_vec, rho0 )

  cor = np.zeros ( [ n, n ] )
#
#  Construct the correlation matrix
#
#  From the vector 
#    [ C(0), C(1), C(2), ... C(N-1) ]
#  construct the vector
#    [ C(N-1), ..., C(2), C(1), C(0), C(1), C(2), ...  C(N-1) ]
#  Every row of the correlation matrix can be constructed by a subvector
#  of this vector.
#
  cor_vec = [ cor_vec(n:-1:2)', cor_vec(1:n)' ]
  for i = 1 : n
    cor(i,1:n) = cor_vec(n+1-i:2*n-i)
  end
#
#  Get the eigendecomposition of COR:
#
#    COR = V * D * V'.
#
#  Because COR is symmetric, V is orthogonal.
#
  [ v, d ] = eig ( cor )
#
#  We assume COR is non-negative definite, and hence that there
#  are no negative eigenvalues.  If this is not the case,
#  warn the user, hope the numbers are only slightly negative,
#  and reset them to 0.
#
  dmin = min ( min ( d ) )

  if ( dmin < - np.sqrt ( eps ) )
    print ( '' )
    print ( 'SAMPLE_PATHS_EIGEN(): Warning!' )
    print ( '  Negative eigenvalues observed as low as ', dmin )

  d = max ( d, 0.0 )
#
#  Compute the eigenvalues of the factor C.
#
  sqrt_d = np.sqrt ( d )
#
#  Compute C, such that C' * C = COR.
#
  c = v * sqrt_d * v.T
#
#  Compute N independent random normal values.
#
  r = rng.standard_normal ( size = [ n, n2 ] )
#
#  Get the variables X which have correlation COR.
#
  x = np.matmul ( c, r )

  return x

def sample_paths_fft ( n, n2, rhomax, rho0, correlation ):

#*****************************************************************************80
#
## sample_paths_fft(): sample paths for stationary correlation functions.
#
#  Discussion:
#
#    This method embeds the symmetric Toeplitz correlation matrix
#    into a circulant matrix.  It then uses FFT techniques to quickly
#    factor the matrix and generate the samples.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Claude Dietrich, Garry Newsam,
#    Fast and exact simulation of stationary Gaussian processes through
#    the circulant embedding of the covariance matrix,
#    SIAM Journal on Scientific Computing,
#    Volume 18, Number 4, pages 1088-1107, July 1997.
#
#  Input:
#
#    integer N, the number of points on each path.
#
#    integer N2, the number of paths.
#
#    real RHOMAX, the maximum value of RHO.
#
#    real RHO0, the correlation length.
#
#    CORRELATION, a handle for a correlation function.
#
#  Output:
#
#    real X[N,N2], the sample paths.
#
  import numpy as np
  from numpy.random import default_rng

  rng = default_rng ( )
#
#  Choose N equally spaced sample points from 0 to RHOMAX.
#
  rho_vec = np.linspace ( 0.0, rhomax, n )
#
#  Evaluate the correlation function.
#
  cor_vec = correlation ( n, rho_vec, rho0 )
#
#  Formally, the correlation matrix is the following Toeplitz matrix R:
#
#        C0 C1 C2 C3 C4
#        C1 C0 C1 C2 C3
#    R = C2 C1 C0 C1 C2
#        C3 C2 C1 C0 C1
#        C4 C3 C2 C1 C0
#
#  Imagine this matrix embedded into a circulant matrix S:
#
#        C0 C1 C2 C3 C4 | C3 C2 C1
#        C1 C0 C1 C2 C3 | C4 C3 C2
#        C2 C1 C0 C1 C2 | C3 C4 C3
#        C3 C2 C1 C0 C1 | C2 C3 C4
#    S = C4 C3 C2 C1 C0 | C1 C2 C3
#        ---------------+---------
#        C3 C4 C3 C2 C1 | C0 C1 C2
#        C2 C3 C4 C3 C2 | C1 C0 C1
#        C1 C2 C3 C4 C3 | C2 C1 C0
#
#  This matrix is fully described by its first row:
#
#    s = C0 C1 C2 C3 C4 | C3 C2 C1
#
  s = np.zeros ( [ 2 * n - 2 ] )
  s(1:n) = cor_vec(1:n)
  s(n+1:2*n-2) = cor_vec(n-1:-1:2)
#
#  Compute sbar, the Fourier transform of s.
#
  sbar = fft ( s )
#
#  Form s2 = sqrt ( sbar / 2 / ( n - 1 ) )
#  Since SBAR may have negative elements, S2 may have imaginary elements.
#
  m = 2 * ( n - 1 )
  s2 = np.sqrt ( sbar / m )
#
#  We want N2 paths.  We can only compute paths in pairs.
#  So we want to compute N3 = floor ( ( N2 + 1 ) / 2 ) pairs.
#
  n3 = floor ( ( n2 + 1 ) / 2 )
#
#  Generate e = er + i * ei with er and ei normal.
#
  ervec = randn ( m, n3 )
  eivec = randn ( m, n3 )
  e(1:m,1:n3) = complex ( ervec(1:m,1:n3), eivec(1:m,1:n3) )
#
#  Pairwise multiply.
#
  ebar(1:m,1:n3) = diag ( s2 ) * e(1:m,1:n3)
#
#  Compute e2, the Fourier transform of ebar.
#  The FFT command will transform each column of E2.
#
  e2(1:m,1:n3) = fft ( ebar )
#
#  Each E2 contains a pair of real samples.  
#  Extract entries 1 to n of each pair to make two paths.
#  We may end up discarding one imaginary result.
#
  x(1:n,1:2:n2) = real ( e2(1:n,1:n3) )
  x(1:n,2:2:n2) = imag ( e2(1:n,1:n2-n3) )

  return x
