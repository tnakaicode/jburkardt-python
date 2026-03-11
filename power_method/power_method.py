#! /usr/bin/env python3
#
def power_method_test ( ):

#*****************************************************************************80
#
## power_method_test() tests power_method().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 September 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'power_method_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test power_method().' )

  rng = default_rng ( )

  power_method_test01 ( rng )
  power_method_test02 ( rng )
  power_method_test03 ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'power_method_test():' )
  print ( '  Normal end of execution.' )

  return

def power_method_test01 ( rng ):

#*****************************************************************************80
#
## power_method_test01() tests power_method() on the Fibonacci2 matrix.
#
#  Discussion:
#
#    This matrix, despite having a single dominant eigenvalue, will generally
#    converge only very slowly under the power method.  This has to do with
#    the fact that the matrix has only 3 eigenvectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  from time import time
  import numpy as np

  n = 50

  a = fibonacci2_matrix ( n )

  x = rng.standard_normal ( size = n )

  it_max = 300
  tol = 0.000001

  phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0

  print ( '' )
  print ( 'power_method_test01():' )
  print ( '  Use the power method on the Fibonacci2 matrix.' )
  print ( '' )
  print ( '  Matrix order N       = ', n )
  print ( '  Maximum iterations   = ', it_max )
  print ( '  Error tolerance      = ', tol )

  ctime1 = time ( )

  x, lam, it_num = power_method ( n, a, x, it_max, tol )

  ctime2 = time ( )
  ctime = ctime2 - ctime1

  print ( '' )
  print ( '  Number of iterations = ', it_num )
  print ( '  CPU time             = ', ctime )
  print ( '  Estimated eigenvalue = ', lam )
  print ( '  Correct value        = ', phi )
  print ( '  Error                = ', np.abs ( lam - phi ) )
#
#  X2 is the exact eigenvector.
#
  x2 = np.ones ( n )
  for i in range ( 1, n ):
    x2[i] = phi * x2[i-1]
  x2 = x2 / np.linalg.norm ( x2 )
#
#  The sine of the angle between X and X2 is a measure of error.
#
  cos_x1x2 = np.dot ( x, x2 )
  sin_x1x2 = np.sqrt ( ( 1.0 - cos_x1x2 ) * ( 1.0 + cos_x1x2 ) )

  print ( '' )
  print ( '  Sine of angle between true and estimated vectors = ', sin_x1x2 )

  return

def power_method_test02 ( rng ):

#*****************************************************************************80
#
## power_method_test02() tests power_method2() on the Fibonacci2 matrix.
#
#  Discussion:
#
#    This matrix, despite having a single dominant eigenvalue, will generally
#    converge only very slowly under the power method.  This has to do with
#    the fact that the matrix has only 3 eigenvectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  from time import time
  import numpy as np

  n = 50

  a = fibonacci2_matrix ( n )

  x = rng.random ( size = n )

  it_max = 300
  tol = 0.000001

  phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0

  print ( '' )
  print ( 'power_method_test02():' )
  print ( '  power_method2() is applied to the Fibonacci2 matrix.' )
  print ( '' )
  print ( '  Matrix order N       = ', n )
  print ( '  Maximum iterations   = ', it_max )
  print ( '  Error tolerance      = ', tol )

  ctime1 = time ( )

  lam, v, it_num = power_method2 ( n, a, x, it_max, tol )

  ctime2 = time ( )
  ctime = ctime2 - ctime1

  print ( '' )
  print ( '  Number of iterations = ', it_num )
  print ( '  CPU time             = ', ctime )
  print ( '  Estimated eigenvalue = ', lam.real, lam.imag )
  print ( '  Correct value        = ', phi )
  print ( '  Error                = ', np.abs ( lam - phi ) )

  return

def power_method_test03 ( rng ):

#*****************************************************************************80
#
## power_method_test03() tests power_method2() on the TRIS matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  from time import time
  import numpy as np

  n = 50

  alpha = -1.0
  beta = 10.0
  gamma = 8.0

  a = tris_matrix ( n, n, alpha, beta, gamma )

  x = rng.random ( size = n )

  it_max = 4000
  tol = 0.000001

  print ( '' )
  print ( 'power_method_test03():' )
  print ( '  power method2() is applied to the tris() matrix.' )
  print ( '' )
  print ( '  Matrix order N       = ', n )
  print ( '  Maximum iterations   = ', it_max )
  print ( '  Error tolerance      = ', tol )

  ctime1 = time ( )

  lam, v, it_num = power_method2 ( n, a, x, it_max, tol )

  ctime2 = time ( )
  ctime = ctime2 - ctime1

  print ( '' )
  print ( '  Number of iterations = ', it_num )
  print ( '  CPU time             = ', ctime )
  print ( '  Estimated eigenvalue = ', lam.real, lam.imag )

  lam_vec = tris_eigenvalues ( n, alpha, beta, gamma )

  lam_max = lam_vec[0]
  for i in range ( 1, n ):
    if ( np.abs ( lam_max ) < np.abs ( lam_vec[i] ) ):
      lam_max = lam_vec[i]

  print ( '  Correct value        = ', lam_max.real, lam_max.imag )
  print ( '  Error                = ', np.abs ( lam - lam_max ) )

  return

def fibonacci2_matrix ( n ):

#*****************************************************************************80
#
## fibonacci2_matrix() returns the FIBONACCI2 matrix.
#
#  Example:
#
#    N = 5
#
#    0 1 0 0 0
#    1 1 0 0 0
#    0 1 1 0 0
#    0 0 1 1 0
#    0 0 0 1 1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is integral: int ( A ) = A.
#
#    A is a zero/one matrix.
#
#    If N = 1 then
#      det ( A ) = 0
#    else
#      det ( A ) = (-1)^(N-1)
#
#    If 1 < N, then A is unimodular.
#
#    For 2 <= N, A has the eigenvalues:
#
#      PHI   (once),
#      1     (N-2) times,
#      1-PHI (once).
#
#    When applied to a Fibonacci1 matrix B, the Fibonacci2 matrix
#    A produces the "next" Fibonacci1 matrix C = A*B.
#
#    Let PHI be the golden ratio (1+sqrt(5))/2.
#
#    For 2 <= N, the eigenvalues and eigenvectors are:
#
#    LAMBDA(1)     = PHI,     vector = (1,PHI,PHI^2,...PHI^(N-1));
#    LAMBDA(2:N-1) = 1        vector = (0,0,0,...,0,1);
#    LAMBDA(N)     = 1 - PHI. vector = (1,1-PHI,(1-PHI)^2,...(1-PHI)^(N-1))
#
#    Note that there is only one eigenvector corresponding to 1.
#    Hence, for 3 < N, the matrix is defective.  This fact means, 
#    for instance, that the convergence of the eigenvector in the power 
#    method will be very slow.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):

        if ( j == 1 ):
          a[i,j] = 1.0

      else:

        if ( j == i - 1 or j == i ):
          a[i,j] = 1.0

  return a

def power_method ( n, A, y, it_max, tol ):

#*****************************************************************************80
#
## power_method() applies the power method for a real eigenvalue.
#
#  Discussion:
#
#    For a given NxN matrix A and an N vector Y, the power method produces
#    a series of estimates for lam, the largest eigenvalue, and Y,
#    the eigenvector corresponding to lam.
#
#    The iteration repeats the following steps
#
#      AY     = A * Y
#      lam = | AY |
#      Y      = AY / lam
#
#    If the matrix A has a single real eigenvalue of maximum modulus,
#    then this iteration will generally produce a good estimate for that
#    eigenvalue and its corresponding eigenvector.
#
#    If there are multiple distinct eigenvalues of the same modulus,
#    perhaps two values of opposite sign, or complex eigenvalues, then
#    the situation is more complicated.
#
#    Separate issues:
#
#    * when estimating the value of lam, we use the Rayleigh quotient,
#    lam = ( y' * A * y ) / ( y' * y ).  Since we normalize Y, the
#    bottom of the fraction is 1.  Using this estimate allows us to
#    easily capture the sign of LAMDBA.  Using the eucldean norm
#    instead, for instance, would always give a positive value.
#
#    * If the dominant eigenvalue is negative, then the iteration 
#    as given will produce eigenvector iterates that alternate in sign.  
#    
#    * It is worth knowing whether the successive eigenvector estimates
#    are tending to some value.  Since an eigenvector is really a direction,
#    we need to normalize the vectors, and we need to somehow treat both
#    a vector and its negative as holding the same information.  This
#    means that the proper way of measuring the difference between two
#    eigenvector estimates is to normalize them both, and then compute
#    the cosine between them as y1'y2, followed by the sine, which is
#    sqrt ( 1 - ( y1'y2)^2 ).  If this sine is small, the vectors y1 and y2
#    are "close" in the sense of direction.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix.
#
#    real Y(N,1), the current estimate for the eigenvector.
#
#    integer IT_MAX, the maximum number of iterations to take.
#    1 <= IT_MAX.
#
#    Input, real TOL, an error tolerance.
#
#  Output:
#
#    real Y(N,1), the updated estimate for the eigenvector.
#
#    real lam, the estimate for the eigenvalue.
#
#    integer IT_NUM, the number of iterations taken.
#
  import numpy as np

  debug = False

  if ( debug ):
    print ( '' )
    print ( '     IT      lam          Delta-lam    Delta-Y' )
    print ( '' )
#
#  Force Y to be a vector of unit norm.
#
# y = y / np.linalg.norm ( y )

  lam = 0.0

  for it_num in range ( 0, it_max ):

    lam_old = lam
    y_old = y.copy ( )
    ay = np.matmul ( A, y )
    lam = np.dot ( y, ay )
    y = ay / np.linalg.norm ( ay )
    if ( lam < 0.0 ):
      y = - y

    if ( 0 == it_num ):
      if ( debug ):
        print ( it_num, lam )
    else:
      val_dif = np.abs ( lam - lam_old )
      cos_y1y2 = np.dot ( y, y_old )
      arg = ( 1.0 - cos_y1y2 ) * ( 1.0 + cos_y1y2 )
      sin_y1y2 = np.sqrt ( ( 1.0 - cos_y1y2 ) * ( 1.0 + cos_y1y2 ) )
      if ( debug ):
        print ( it_num, lam, val_dif, sin_y1y2 )

      if ( val_dif <= tol ):  
        break

# y = ay / lam

  return y, lam, it_num

def power_method2 ( n, A, x_init, it_max, tol ):

#*****************************************************************************80
#
## power_method2() applies the power method for possibly complex eigenvalues.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric VanDeVelde,
#    Concurrent Scientific Programming,
#    Springer, 1994,
#    ISBN: 0-387-94195-9,
#    LC: QA76.58.V35.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix.
#
#    real X(N), the initial estimate for the eigenvector.
#
#    integer IT_MAX, the maximum number of iterations to take.
#    1 <= IT_MAX.
#
#    real TOL, an error tolerance.
#
#  Output:
#
#    complex lam, the estimate for the eigenvalue.
#
#    complex V(N), the estimate for the eigenvector.
#
#    integer IT_NUM, the number of iterations taken.
#
  import numpy as np

  it_num = 0
#
#  Compute data necessary to start the iteration.
#
  x = x_init.copy ( )

  pi_xx = np.dot ( x, x )
  x = x / pi_xx
  y = np.matmul ( A, x )
  pi_xy = np.dot ( x, y )
  pi_yy = np.dot ( y, y )

  for it in range ( 1, it_max + 1 ):

    if ( pi_yy - pi_xy**2 < tol**2 * pi_yy ):
      lam = pi_xy
      v = y / np.sqrt ( pi_yy )
      return lam, v, it_num

    z = np.matmul ( A, y )

    pi_xz = np.dot ( x, z )
    pi_yz = np.dot ( y, z )
    pi_zz = np.dot ( z, z )

    alpha = - ( pi_yz - pi_xy * pi_xz ) / ( pi_yy - pi_xy * pi_xy )
    beta = ( pi_xy * pi_yz - pi_yy * pi_xz ) / ( pi_yy - pi_xy * pi_xy )
    gamma = pi_zz + alpha * alpha * pi_yy + beta * beta \
      + 2.0 * ( alpha * pi_yz + beta * pi_xz + alpha * beta * pi_xy )

    if ( gamma < tol**2 * pi_zz and alpha**2 < 4.0 * beta ):

      lam_real = - alpha / 2.0
      lam_imag = np.sqrt ( 4.0 * beta - alpha**2 ) / 2.0
      lam = complex ( lam_real, lam_imag )

      v = ( lam * y - z ) / np.sqrt ( beta * pi_yy + alpha * pi_yz + pi_zz )

      return lam, v, it_num

    x = y / np.sqrt ( pi_yy )
    y = z / np.sqrt ( pi_yy )

    pi_xy = pi_yz / pi_yy
    pi_yy = pi_zz / pi_yy

    it_num = it

  print ( '' )
  print ( 'power_method2(): Fatal error!' )
  print ( '  Convergence was not reached.' )
  raise Exception ( 'power_method2(): Fatal error!' )

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

def tris_matrix ( m, n, x, y, z ):

#*****************************************************************************80
#
## tris_matrix() returns the TRIS matrix.
#
#  Formula:
#
#    if ( J = I-1 )
#      A(I,J) = X
#    elseif ( J = I )
#      A(I,J) = Y
#    elseif ( J = I + 1 )
#      A(I,J) = Z
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 5, N = 5, X = 1, Y = 2, Z = 3
#
#    2 3 0 0 0
#    1 2 3 0 0
#    0 1 2 3 0
#    0 0 1 2 3
#    0 0 0 1 2
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is banded, with bandwidth 3.
#
#    A is Toeplitz: constant along diagonals.
#
#    If Y is not zero, then for A to be singular, it must be the case that
#
#      0.5 * Y / sqrt ( X * Z ) < 1
#
#    and
#
#      cos (K*PI/(N+1)) = - 0.5 * Y / sqrt ( X * Z ) for some 1 <= K <= N.
#
#    If Y is zero, then A is singular when N is odd, or if X or Z is zero.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A has eigenvalues
#
#      LAMBDA(I) = Y + 2 * sqrt(X*Z) * COS(I*PI/(N+1))
#
#    The eigenvalues will be complex if X * Z < 0.
#
#    If X = Z, the matrix is symmetric.
#
#    As long as X and Z are nonzero, the matrix is irreducible.
#
#    If X = Z = -1, and Y = 2, the matrix is a symmetric, positive
#    definite M matrix, the negative of the second difference matrix.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Todd,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Academic Press, 1978, page 155.
#
#  Input:
#
#    integer M, N, the order of A.
#
#    real X, Y, Z, the scalars that define A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( j == i - 1 ):
        a[i,j] = x
      elif ( j == i ):
        a[i,j] = y
      elif ( j == i + 1 ):
        a[i,j] = z

  return a

def tris_eigenvalues ( n, x, y, z ):

#*****************************************************************************80
#
## tris_eigenvalues() returns the eigenvalues of the tridiagonal scalar matrix.
#
#  Discussion:
#
#    The eigenvalues will be complex if X * Z < 0.
#
#  Modified:
#
#    23 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X, Y, Z, the scalars that define A.
#
#  Output:
#
#    complex lam(N), the eigenvalues.  The eigenvalues are
#    complex if X * Z < 0.
#
  import numpy as np

  lam = np.zeros ( n, dtype = complex )
#
#  np.emath.sqrt() correctly returns complex results for negative input.
#
  for i in range ( 0, n ):
    angle = ( i + 1 ) * np.pi / ( n + 1 )
    lam[i] = y + 2.0 * np.emath.sqrt ( x * z ) * np.cos ( angle )

  return lam

if ( __name__ == "__main__" ):
  timestamp ( )
  power_method_test ( )
  timestamp ( )

