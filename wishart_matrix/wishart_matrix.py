#! /usr/bin/env python3
#
def wishart_matrix_test ( ):

#*****************************************************************************80
#
## wishart_matrix_test() tests wishart_matrix().
#
#  Discussion:
#
#    A special experience in programming this code was figuring out how to
#    define a random number generator, initialized with a given seed, which
#    will be used by all functions in a given programming sequence.  I had
#    to struggle to see that this is done by defining a generator "rng()"
#    and then passing and using it everywhere it is needed.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 December 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'wishart_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test wishart_matrix().' )

  wishart_unit_sample_test ( )
  bartlett_unit_sample_test ( )
  wishart_test03 ( )
  wishart_test04 ( )
  wishart_test05 ( )
  wishart_test06 ( )
  wishart_test07 ( )
  wishart_test08 ( )
  wishart_test09 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'wishart_matrix_test():' )
  print ( '  Normal end of execution.' )
 
  return

def bartlett_sample ( m, df, sigma, rng ):

#*****************************************************************************80
#
## bartlett_sample() samples the Bartlett distribution.
#
#  Discussion:
#
#    If the matrix T is sampled from the Bartlett distribution, then 
#    the matrix W = T' * T is a sample from the Wishart distribution.
# 
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Patrick Odell, Alan Feiveson,
#    A numerical procedure to generate a sample covariance matrix,
#    Journal of the American Statistical Association,
#    Volume 61, Number 313, March 1966, pages 199-203.
#
#    Stanley Sawyer,
#    Wishart Distributions and Inverse-Wishart Sampling,
#    Washington University,
#    30 April 2007, 12 pages.
#
#  Input:
#
#    integer M, the order of the matrix.
#
#    integer DF, the number of degrees of freedom.
#    M <= DF.
#
#    real SIGMA(M,M), the covariance matrix, which should be 
#    a symmetric positive definite matrix.
#
#  Output:
#
#    real T(M,M), the sample matrix from the Bartlett distribution.
#
  from scipy.linalg import cholesky
  import numpy as np

  if ( df < m ):
    print ( '' )
    print ( 'bartlett_sample(): Fatal error!' )
    print ( '  DF = ', df, ' < M = ', m )
    raise Exception ( 'bartlett_sample(): Fatal error!' )
#
#  Get the upper triangular Cholesky factor of SIGMA.
#
  r = cholesky ( sigma, lower = False )
#
#  Sample the unit Bartlett distribution.
#
  tu = bartlett_unit_sample ( m, df, rng )
#
#  Construct the matrix.
#
  t = np.matmul ( tu, r )

  return t

def bartlett_unit_sample ( m, df, rng ):

#*****************************************************************************80
#
## bartlett_unit_sample() samples the unit Bartlett distribution.
#
#  Discussion:
#
#    If the matrix T is sampled from the unit Bartlett distribution, then 
#    the matrix W = T' * T is a sample from the unit Wishart distribution.
# 
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Patrick Odell, Alan Feiveson,
#    A numerical procedure to generate a sample covariance matrix,
#    Journal of the American Statistical Association,
#    Volume 61, Number 313, March 1966, pages 199-203.
#
#    Stanley Sawyer,
#    Wishart Distributions and Inverse-Wishart Sampling,
#    Washington University,
#    30 April 2007, 12 pages.
#
#  Input:
#
#    integer M, the order of the matrix.
#
#    integer DF, the number of degrees of freedom.
#    M <= DF.
#
#  Output:
#
#    real T(M,M), the sample matrix from the unit Bartlett distribution.
#
  import numpy as np

  if ( df < m ):
    print ( '' )
    print ( 'bartlett_unit_sample(): Fatal error!' )
    print ( '  DF = ', df, ' < M = ', m )
    raise Exception ( 'bartlett_unit_sample(): Fatal error!' )

  t = np.zeros ( [ m, m ] )
  
  for i in range ( 0, m ):
    df_chi = df - i
    t[i,i] = np.sqrt ( r8_chi_sample ( df_chi, rng ) )
    for j in range ( i + 1, m ):
      t[i,j] = r8_normal_01_sample ( rng )

  return t

def bartlett_unit_sample_test ( ):

#*****************************************************************************80
#
## bartlett_unit_sample_test() tests bartlett_unit_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 September 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy import linalg as LA
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'bartlett_unit_sample_test():' )
  print ( '  bartlett_unit_sample() samples unit Bartlett matrices by:' )
  print ( '  T = bartlett_unit_sample ( n, df )' )
#
#  Initialize the random number generator.
#
  seed = 123456789
  rng = default_rng ( seed )
#
#  Set the parameters and call.
#
  n = 5
  df = 8
  t = bartlett_unit_sample ( n, df, rng )
  r8mat_print ( n, n, t, '  bartlett_unit_sample ( 5, 8 ):' )
#
#  Calling again yields a new matrix.
#
  t = bartlett_unit_sample ( n, df, rng )
  r8mat_print ( n, n, t, '  bartlett_unit_sample ( 5, 8 ):' )
#
#  Reduce DF.
#
  n = 5
  df = 5
  t = bartlett_unit_sample ( n, df, rng )
  r8mat_print ( n, n, t, '  bartlett_unit_sample ( 5, 5 ):' )
#
#  Try a smaller matrix.
#
  n = 3
  df = 5
  t = bartlett_unit_sample ( n, df, rng )
  r8mat_print ( n, n, t, '  bartlett_unit_sample ( 3, 5 ):' )
#
#  What is the eigendecomposition of the matrix T' * T?
#
  w = np.matmul ( np.transpose ( t ), t )
  eigval, eigvec = LA.eig ( w )
  r8mat_print ( n, n, eigvec, '  Eigenvectors of W = T\' * T:' )
  r8vec_print ( n, eigval, '  Eigenvalues of W = T\' * T:' )

  return

def r8_chi_sample ( df, rng ):

#*****************************************************************************80
#
## r8_chi_sample() generates a Chi-Square random deviate.
#
#  Discussion:
#
#    This procedure generates a random deviate from the chi square distribution
#    with DF degrees of freedom random variable.
#
#    The algorithm exploits the relation between chisquare and gamma.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real DF, the degrees of freedom.
#    0.0 < DF.
#
#  Output:
#
#    real VALUE, a random deviate  from the distribution.
#
  if ( df <= 0.0 ):
    print ( '' )
    print ( 'r8_chi_sample(): Fatal error!' )
    print ( '  DF <= 0.' )
    print ( '  Value of DF:', df )
    raise Exception ( 'r8_chi_sample(): Fatal error!' )

  arg1 = 1.0
  arg2 = df / 2.0

  value = 2.0 * r8_gamma_sample ( arg1, arg2, rng )

  return value

def r8_gamma_sample ( r, a, rng ):

#*****************************************************************************80
#
## r8_gamma_sample() generates a Gamma random deviate.
#
#  Discussion:
#
#    This procedure generates random deviates from the gamma distribution whose
#    density is (R^A)/Gamma(A) * X^(A-1) * Exp(-R*X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Generating Gamma Variates by a Modified Rejection Technique,
#    Communications of the ACM,
#    Volume 25, Number 1, January 1982, pages 47-54.
#
#    Joachim Ahrens, Ulrich Dieter,
#    Computer Methods for Sampling from Gamma, Beta, Poisson and
#    Binomial Distributions,
#    Computing,
#    Volume 12, Number 3, September 1974, pages 223-246.
#
#  Input:
#
#    real R, the rate parameter.
#    A nonzero.
#
#    real A, the shape parameter.
#    0 < A.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  value = r8_gamma_01_sample ( a, rng ) / r

  return value

def r8_gamma_01_sample ( a, rng ):

#*****************************************************************************80
#
## r8_gamma_01_sample() samples the standard Gamma distribution.
#
#  Discussion:
#
#    This procedure corresponds to algorithm GD in the reference.
#
#    pdf ( a x ) = 1/gamma(a) * x^(a-1) * exp ( - x )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joachim Ahrens, Ulrich Dieter,
#    Generating Gamma Variates by a Modified Rejection Technique,
#    Communications of the ACM,
#    Volume 25, Number 1, January 1982, pages 47-54.
#
#  Input:
#
#    real A, the shape parameter.
#    0.0 < A.
#
#  Output:
#
#    real VALUE, a random deviate from the distribution.
#
  import numpy as np

  a1 =  0.3333333
  a2 = -0.2500030
  a3 =  0.2000062
  a4 = -0.1662921
  a5 =  0.1423657
  a6 = -0.1367177
  a7 =  0.1233795

  e1 = 1.0
  e2 = 0.4999897
  e3 = 0.1668290
  e4 = 0.0407753
  e5 = 0.0102930

  q1 =  0.04166669
  q2 =  0.02083148
  q3 =  0.00801191
  q4 =  0.00144121
  q5 = -0.00007388
  q6 =  0.00024511
  q7 =  0.00024240

  sqrt32 = 5.656854

  if ( 1.0 <= a ):

    s2 = a - 0.5
    s = np.sqrt ( s2 )
    d = sqrt32 - 12.0 * s
#
#  Immediate acceptance.
#
    t = r8_normal_01_sample ( rng )
    x = s + 0.5 * t
    value = x * x

    if ( 0.0 <= t ):
      return value
#
#  Squeeze acceptance.
#
    u = rng.random ( )

    if ( d * u <= t * t * t ):
      return value

    r = 1.0 / a
    q0 = (((((( q7 \
      * r + q6 ) \
      * r + q5 ) \
      * r + q4 ) \
      * r + q3 ) \
      * r + q2 ) \
      * r + q1 ) \
      * r
#
#  Approximation depending on size of parameter A.
#
    if ( 13.022 < a ):
      b = 1.77
      si = 0.75
      c = 0.1515 / s
    elif ( 3.686 < a ):
      b = 1.654 + 0.0076 * s2
      si = 1.68 / s + 0.275
      c = 0.062 / s + 0.024
    else:
      b = 0.463 + s + 0.178 * s2
      si = 1.235
      c = 0.195 / s - 0.079 + 0.16 * s
#
#  Quotient test.
#
    if ( 0.0 < x ):

      v = 0.5 * t / s

      if ( 0.25 < abs ( v ) ):
        q = q0 - s * t + 0.25 * t * t + 2.0 * s2 * np.log ( 1.0 + v )
      else:
        q = q0 + 0.5 * t * t * (((((( a7 \
          * v + a6 ) \
          * v + a5 ) \
          * v + a4 ) \
          * v + a3 ) \
          * v + a2 ) \
          * v + a1 ) \
          * v

      if ( np.log ( 1.0 - u ) <= q ):
        return value

    while ( True ):

      e = r8_exponential_01_sample ( rng )
      u = 2.0 * rng.random ( ) - 1.0

      if ( 0.0 <= u ):
        t = b + abs ( si * e )
      else:
        t = b - abs ( si * e )
#
#  Possible rejection.
#
      if ( t < -0.7187449 ):
        continue
#
#  Calculate V and quotient Q.
#
      v = 0.5 * t / s

      if ( 0.25 < abs ( v ) ):
        q = q0 - s * t + 0.25 * t * t + 2.0 * s2 * np.log ( 1.0 + v )
      else:
        q = q0 + 0.5 * t * t * (((((( a7 \
          * v + a6 ) \
          * v + a5 ) \
          * v + a4 ) \
          * v + a3 ) \
          * v + a2 ) \
          * v + a1 ) \
          * v
#
#  Hat acceptance.
#
      if ( q <= 0.0 ):
        continue

      if ( 0.5 < q ):
        w = np.exp ( q ) - 1.0
      else:
        w = (((( e5 * q + e4 ) * q + e3 ) * q + e2 ) * q + e1 ) * q
#
#  May have to sample again.
#
      if ( c * abs ( u ) <= w * np.exp ( e - 0.5 * t * t ) ):
        break

    x = s + 0.5 * t
    value = x * x

    return value
#
#  Method for A < 1.
#
  else:

    b = 1.0 + 0.3678794 * a

    while ( True ):

      p = b * rng.random ( )

      if ( p < 1.0 ):

        value = np.exp ( np.log ( p ) / a )

        if ( value <= r8_exponential_01_sample ( rng ) ):
          return value

        continue

      value = - np.log ( ( b - p ) / a )

      if ( ( 1.0 - a ) * np.log ( value ) <= r8_exponential_01_sample ( rng ) ):
        break

  return value

def r8_normal_01_sample ( rng ):

#*****************************************************************************80
#
## r8_normal_01_sample() returns a unit pseudonormal R8.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#    The Box-Muller method is used, which is efficient, but
#    generates two values at a time.  
#
#    Typically, we would use one value and save the other for the next call.
#    However, the fact that this function has saved memory makes it difficult
#    to correctly handle cases where we want to re-initialize the code,
#    or to run in parallel.  Therefore, we will instead use the first value
#    and DISCARD the second.
#
#    EFFICIENCY must defer to SIMPLICITY.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, a sample of the standard normal PDF.
#
  import numpy as np

  r1 = rng.random ( )
  r2 = rng.random ( )

  x = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  value = x

  return value

def r8_exponential_01_sample ( rng ):

#*****************************************************************************80
#
## r8_exponential_01_sample() samples the standard exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, a sample of the PDF.
#
  import numpy as np

  r = rng.random ( )

  value = - np.log ( r )

  return value

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8ut_inverse ( n, a ):

#*****************************************************************************80
#
## r8ut_inverse() computes the inverse of a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix to be inverted.
#
#  Output:
#
#    real A_INV(N,N), the inverse matrix.
#
  import numpy as np
#
#  Check.
#
  for i in range ( 0, n ):
    if ( a[i,i] == 0.0 ):
      print ( '' )
      print ( 'r8ut_inverse(): Fatal error!' )
      print ( '  Zero diagonal element.' )
      raise Exception ( 'r8ut_inverse(): Fatal error!' )

  a_inv = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a_inv[i,j] = a[i,j]

  for j in range ( n - 1, -1, -1 ):

    for i in range ( n - 1, -1, -1 ):

      if ( j < i ):

        a_inv[i,j] = 0.0

      elif ( i == j ):

        a_inv[i,j] = 1.0 / a_inv[i,j]

      elif ( i < j ):

        t = 0.0
        for k in range ( i + 1, j + 1 ):
          t = t + a_inv[i,k] * a_inv[k,j]
        a_inv[i,j] = - t / a_inv[i,i]

  return a_inv

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def wishart_sample_inverse ( m, df, sigma, rng ):

#*****************************************************************************80
#
## wishart_sample_inverse() returns the inverse of a sample Wishart matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Patrick Odell, Alan Feiveson,
#    A numerical procedure to generate a sample covariance matrix,
#    Journal of the American Statistical Association,
#    Volume 61, Number 313, March 1966, pages 199-203.
#
#    Stanley Sawyer,
#    Wishart Distributions and Inverse-Wishart Sampling,
#    Washington University,
#    30 April 2007, 12 pages.
#
#  Input:
#
#    integer M, the order of the matrix.
#
#    integer DF, the number of degrees of freedom.
#    M <= DF.
#
#    real SIGMA(M,M), the covariance matrix, which should be 
#    a symmetric positive definite matrix.
#
#  Output:
#
#    real A(M,M), the inverse of a sample matrix from the Wishart 
#    distribution.
#
  from scipy.linalg import cholesky
  import numpy as np

  if ( df < m ):
    print ( '' )
    print ( 'wishart_sample_inverse(): Fatal error!' )
    print ( '  DF = ', df, ' < M = ', m )
    raise Exception ( 'wishart_sample_inverse(): Fatal error!' )
#
#  Get R, the upper triangular Cholesky factor of SIGMA.
#
  r = cholesky ( sigma, lower = False )
#
#  Get S, the inverse of R.
#
  s = r8ut_inverse ( m, r )
#
#  Get UA, the inverse of a sample from the unit Wishart distribution.
#
  ua = wishart_unit_sample_inverse ( m, df, rng )
#
#  Construct the matrix A = S * UA * S'.
#
  a = np.matmul ( s, \
    np.matmul ( ua, np.transpose ( s ) ) )

  return a

def wishart_sample ( m, df, sigma, rng ):

#*****************************************************************************80
#
## wishart_sample() samples the Wishart distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Patrick Odell, Alan Feiveson,
#    A numerical procedure to generate a sample covariance matrix,
#    Journal of the American Statistical Association,
#    Volume 61, Number 313, March 1966, pages 199-203.
#
#    Stanley Sawyer,
#    Wishart Distributions and Inverse-Wishart Sampling,
#    Washington University,
#    30 April 2007, 12 pages.
#
#  Input:
#
#    integer M, the order of the matrix.
#
#    integer DF, the number of degrees of freedom.
#    M <= DF.
#
#    real SIGMA(M,M), the covariance matrix, which should be 
#    a symmetric positive definite matrix.
#
#  Output:
#
#    real A(M,M), the sample matrix from the Wishart distribution.
#
  from scipy.linalg import cholesky
  import numpy as np

  if ( df < m ):
    print ( '' )
    print ( 'wishart_sample(): Fatal error!' )
    print ( '  DF = ', df, ' < M = ', m )
    raise Exception ( 'wishart_sample(): Fatal error!' )
#
#  Get R, the upper triangular Cholesky factor of SIGMA.
#
  r = cholesky ( sigma, lower = False )
#
#  Get AU, a sample from the unit Wishart distribution.
#
  au = wishart_unit_sample ( m, df, rng )
#
#  Construct the matrix A = R' * AU * R.
#
  a = np.matmul ( np.transpose ( r ), \
    np.matmul ( au, r ) )

  return a

def wishart_test03 ( ):

#*****************************************************************************80
#
## wishart_test03() compares the unit Wishart and Bartlett sample matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2013
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'wishart_test03():' )
  print ( '  Verify that, if using the same set of random numbers,' )
  print ( '    W = T\' * T,' )
  print ( '  where' )
  print ( '    W = wishart_unit_sample ( n, df )' )
  print ( '    T = bartlett_unit_sample ( n, df )' )
#
#  Set the parameters.
#
  n = 5
  df = 8
#
#  Compute W.
#
  seed = 123456789
  rng = default_rng ( seed )
  w = wishart_unit_sample ( n, df, rng )
  r8mat_print ( n, n, w, '  W:' )
#
#  Compute T.
#
  seed = 123456789
  rng = default_rng ( seed )
  t = bartlett_unit_sample ( n, df, rng )
  r8mat_print ( n, n, t, '  T:' )
#
#  Compute T' * T.
#
  tt = np.matmul ( np.transpose ( t ), t )
#
#  Compare T'T to W.
#
  dif = np.linalg.norm ( w - tt, ord = 'fro' )
  print ( '' )
  print ( '  Frobenius norm of W-T\'T:', dif )

  return

def wishart_test04 ( ):

#*****************************************************************************80
#
## wishart_test04() demonstrates the Wishart sampling function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 September 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy import linalg as LA
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'wishart_test04():' )
  print ( '  We can compute sample Wishart matrices by:' )
  print ( '    W = wishart_sample ( n, df, sigma )' )
#
#  Initialize the random number generator.
#
  seed = 123456789
  rng = default_rng ( seed )
#
#  Set the parameters and call.
#
  n = 5
  df = 8
  sigma = np.eye ( 5, 5 )
  w = wishart_sample ( n, df, sigma, rng )
  r8mat_print ( n, n, w, '  wishart_sample ( 5, 8, Identity ):' )
#
#  Calling again yields a new matrix.
#
  w = wishart_sample ( n, df, sigma, rng )
  r8mat_print ( n, n, w, '  wishart_sample ( 5, 8, Identity ):' )
#
#  Try a diagonal matrix.
#
  sigma = np.diag ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ], k = 0 )
  w = wishart_sample ( n, df, sigma, rng )
  r8mat_print ( n, n, w, '  wishart_sample ( 5, 8, diag(1,2,3,4,5) ):' )
#
#  Try a smaller matrix.  Sigma must be positive definite symmetric.
#
  n = 3
  df = 3
  r = np.array ( [ \
    [ 5.0, 1.0, 3.0 ], \
    [ 0.0, 4.0, 2.0 ], \
    [ 0.0, 0.0, 6.0 ] ] )
  sigma = np.matmul ( np.transpose ( r ), r )
  r8mat_print ( n, n, sigma, '  Set covariance SIGMA:' )
  w = wishart_sample ( n, df, sigma, rng )
  r8mat_print ( n, n, w, '  wishart_sample ( 3, 3, sigma ):' )
#
#  What is the eigendecomposition of this matrix?
#
  eigval, eigvec = LA.eig ( w )
  r8mat_print ( n, n, eigvec, '  Eigenvectors of previous matrix:' )
  r8vec_print ( n, eigval, '  Eigenvalues of previous matrix:' )

  return

def wishart_test05 ( ):

#*****************************************************************************80
#
## wishart_test05() demonstrates the Bartlett sampling function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 September 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy import linalg as LA
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'wishart_test05():' )
  print ( '  We can compute sample Bartlett matrices by:' )
  print ( '    T = bartlett_sample ( n, df, sigma )' )
#
#  Initialize the random number generator.
#
  seed = 123456789
  rng = default_rng ( seed )
#
#  Set the parameters and call.
#
  n = 5
  df = 8
  sigma = np.eye ( 5, 5 )
  t = bartlett_sample ( n, df, sigma, rng )
  r8mat_print ( n, n, t, '  bartlett_sample ( 5, 8, Identity ):' )
#
#  Calling again yields a new matrix.
#
  t = bartlett_sample ( n, df, sigma, rng )
  r8mat_print ( n, n, t, '  bartlett_sample ( 5, 8, Identity ):' )
#
#  Try a diagonal matrix.
#
  sigma = np.diag ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ], k = 0 )
  t = bartlett_sample ( n, df, sigma, rng )
  r8mat_print ( n, n, t, '  bartlett_sample ( 5, 8, diag(1,2,3,4,5) ):' )
#
#  Try a smaller matrix.
#
  n = 3
  df = 3
  r = np.array ( [ \
    [ 5.0, 1.0, 3.0 ], \
    [ 0.0, 4.0, 2.0 ], \
    [ 0.0, 0.0, 6.0 ] ] )
  sigma = np.matmul ( np.transpose ( r ), r )
  r8mat_print ( n, n, sigma, '  Set covariance SIGMA:' )
  t = bartlett_sample ( n, df, sigma, rng )
  r8mat_print ( n, n, t, '  bartlett_sample ( 3, 3, sigma ):' )
#
#  What is the eigendecomposition of the matrix T' * T?
#
  w = np.matmul ( np.transpose ( t ), t )
  eigval, eigvec = LA.eig ( w )
  r8mat_print ( n, n, eigvec, '  Eigenvectors of W = T'' * T:' )
  r8vec_print ( n, eigval, '  Eigenvalues of W = T'' * T:' )

  return

def wishart_test06 ( ):

#*****************************************************************************80
#
## wishart_test06() compares the Wishart and Bartlett sample matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2013
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'wishart_test06():' )
  print ( '  Verify that, if using the same set of random numbers,' )
  print ( '    W = T\' * T,' )
  print ( '  where' )
  print ( '    W = wishart_sample ( n, df, sigma )' )
  print ( '    T = bartlett_sample ( n, df, sigma )' )
#
#  Set the parameters.
#
  n = 3
  df = 5
  r = np.array ( [ \
    [ 5.0, 1.0, 3.0 ], \
    [ 0.0, 4.0, 2.0 ], \
    [ 0.0, 0.0, 6.0 ] ] )
  sigma = np.matmul ( np.transpose ( r ), r )
  r8mat_print ( n, n, sigma, '  Covariance SIGMA:' )
#
#  Initialize the random number package and compute W.
#
  seed = 123456789
  rng = default_rng ( seed )
  w = wishart_sample ( n, df, sigma, rng )
#
#  Initialize the random number package again, and compute T.
#
  seed = 123456789
  rng = default_rng ( seed )
  t = bartlett_sample ( n, df, sigma, rng )
#
#  Compute T' * T and compare it to W.
#
  tt = np.matmul ( np.transpose ( t ), t )

  dif = np.linalg.norm ( w - tt, ord = 'fro' )
  print ( '' )
  print ( '  Frobenius norm of W-T\'*T is ', dif )

  return

def wishart_test07 ( ):

#*****************************************************************************80
#
## wishart_test07() demonstrates a property of the Wishart distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2013
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'wishart_test07():' )
  print ( '  For given values of N, DF, SIGMA, the random' )
  print ( '  matrices from the Wishart distribution:' )
  print ( '    W = wishart_sample ( n, df, sigma )' )
  print ( '  should have mean DF * SIGMA.' )
#
#  Initialize the random number generator.
#
  seed = 123456789
  rng = default_rng ( seed )
#
#  Set the parameters.
#
  n = 3
  print ( '  Fix N =', n )
  df = 5
  print ( '  Fix DF =', df )
  r = np.array ( [ \
    [ 5.0, 1.0, 3.0 ], \
    [ 0.0, 4.0, 2.0 ], \
    [ 0.0, 0.0, 6.0 ] ] )
  sigma = np.matmul ( np.transpose ( r ), r )
  r8mat_print ( n, n, sigma, '  Covariance matrix SIGMA:' )
#
#  Sample many times and average.
#
  sample_num = 1000
  w_average = np.zeros ( [ n, n ] )
  for i in range ( 0, sample_num ):
    w = wishart_sample ( n, df, sigma, rng )
    w_average = w_average + w
  w_average = w_average / sample_num
#
#  Compare SIGMA and W_SAMPLE / DF.
#
  w_average = w_average / df

  r8mat_print ( n, n, w_average, '  W_Average / DF: ' )

  dif = np.linalg.norm ( sigma - w_average, ord = 'fro' )
  print ( '' )
  print ( '  Frobenius norm of SIGMA-W_average/DF =', dif )

  return

def wishart_test08 ( ):

#*****************************************************************************80
#
## wishart_test08() samples the unit Wishart and unit Wishart inverse matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2013
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'wishart_test08():' )
  print ( '  Verify that, if using the same set of random numbers,' )
  print ( '    inverse(W) = M,' )
  print ( '  where' )
  print ( '    W = wishart_unit_sample ( n, df )' )
  print ( '    M = wishart_unit_sample_inverse ( n, df )' )
#
#  Set the parameters.
#
  n = 5
  df = 8
#
#  Initialize the random number package and compute W.
#
  seed = 123456789
  rng = default_rng ( seed )
  w = wishart_unit_sample ( n, df, rng )
#
#  Initialize the random number package again, and compute M.
#
  seed = 123456789
  rng = default_rng ( seed )
  m = wishart_unit_sample_inverse ( n, df, rng )
#
#  Compute W * M
#
  wm = np.matmul ( w, m )
#
#  Compare W*M to I
#
  ident = np.eye ( n, n )
  dif = np.linalg.norm ( wm - ident, ord = 'fro' )
  print ( '' )
  print ( '  Frobenius norm of error M*W-I is', dif )

  return

def wishart_test09 ( ):

#*****************************************************************************80
#
## wishart_test09() samples the Wishart and Wishart inverse matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2013
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'wishart_test09():' )
  print ( '  Verify that, if using the same set of random numbers,' )
  print ( '    inverse(W) = M,' )
  print ( '  where' )
  print ( '    W = wishart_sample ( n, df, sigma )' )
  print ( '    M = wishart_sample_inverse ( n, df, sigma )' )
#
#  Set the parameters.
#
  n = 5
  df = 8
  r = np.array ( [ \
    [ 3.0, 1.0, 1.0, 1.0, 1.0 ], \
    [ 0.0, 7.0, 1.0, 2.0, 3.0 ], \
    [ 0.0, 0.0, 5.0, 1.0, 3.0 ], \
    [ 0.0, 0.0, 0.0, 4.0, 2.0 ], \
    [ 0.0, 0.0, 0.0, 0.0, 6.0 ] ] )
  sigma = np.matmul ( np.transpose ( r ), r )
#
#  Initialize the random number package and compute W.
#
  seed = 123456789
  rng = default_rng ( seed )
  w = wishart_sample ( n, df, sigma, rng )
#
#  Initialize the random number package again, and compute T.
#
  seed = 123456789
  rng = default_rng ( seed )
  m = wishart_sample_inverse ( n, df, sigma, rng )
#
#  Compute W * M
#
  wm = np.matmul ( w, m )
#
#  Compare W*M to I
#
  ident = np.eye ( n, n )
  dif = np.linalg.norm ( wm - ident, ord = 'fro' )
  print ( '' )
  print ( '  Frobenius norm of error M*W-I is ', dif )

  return

def wishart_unit_sample_inverse ( m, df, rng ):

#*****************************************************************************80
#
## wishart_unit_sample_inverse() inverts a unit Wishart sample matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Patrick Odell, Alan Feiveson,
#    A numerical procedure to generate a sample covariance matrix,
#    Journal of the American Statistical Association,
#    Volume 61, Number 313, March 1966, pages 199-203.
#
#    Stanley Sawyer,
#    Wishart Distributions and Inverse-Wishart Sampling,
#    Washington University,
#    30 April 2007, 12 pages.
#
#  Input:
#
#    integer M, the order of the matrix.
#
#    integer DF, the number of degrees of freedom.
#    M <= DF.
#
#  Output:
#
#    real A(M,M), the inverse of a sample matrix from the unit 
#    Wishart distribution.
#
  import numpy as np

  if ( df < m ):
    print ( '' )
    print ( 'wishart_unit_sample_inverse(): Fatal error!' )
    print ( '  DF = ', df, ' < M = ', m )
    raise Exception ( 'wishart_unit_sample_inverse(): Fatal error!' )
#
#  Compute C, an upper triangular matrix such that the
#  Wishart sample matrix is C' * C.
#
  c = np.zeros ( [ m, m ] )

  for i in range ( 0, m ):
    df_chi = df - i
    c[i,i] = np.sqrt ( r8_chi_sample ( df_chi, rng ) )
    for j in range ( i + 1, m ):
      c[i,j] = r8_normal_01_sample ( rng )
#
#  Compute B, the inverse of C.
#
  b = r8ut_inverse ( m, c )
#
#  The inverse of the Wishart sample matrix C'*C is inv(C) * C'.
#
  a = np.matmul ( b, np.transpose ( b ) )

  return a

def wishart_unit_sample ( m, df, rng ):

#*****************************************************************************80
#
## wishart_unit_sample() samples the unit Wishart distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 October 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Patrick Odell, Alan Feiveson,
#    A numerical procedure to generate a sample covariance matrix,
#    Journal of the American Statistical Association,
#    Volume 61, Number 313, March 1966, pages 199-203.
#
#    Stanley Sawyer,
#    Wishart Distributions and Inverse-Wishart Sampling,
#    Washington University,
#    30 April 2007, 12 pages.
#
#  Input:
#
#    integer M, the order of the matrix.
#
#    integer DF, the number of degrees of freedom.
#    M <= DF.
#
#  Output:
#
#    real A(M,M), the sample matrix from the unit Wishart distribution.
#
  import numpy as np

  if ( df < m ):
    print ( '' )
    print ( 'wishart_unit_sample(): Fatal error!' )
    print ( '  DF = ', df, ' < M = ', m )
    raise Exception ( 'wishart_unit_sample(): Fatal error!' )

  c = np.zeros ( [ m, m ] )

  for i in range ( 0, m ):
    df_chi = df - i
    c[i,i] = np.sqrt ( r8_chi_sample ( df_chi, rng ) )
    for j in range ( i + 1, m ):
      c[i,j] = r8_normal_01_sample ( rng )

  a = np.matmul ( np.transpose ( c ), c )

  return a

def wishart_unit_sample_test ( ):

#*****************************************************************************80
#
## wishart_unit_sample_test() tests wishart_unit_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 December 2023
#
#  Author:
#
#    John Burkardt
#
  from numpy import linalg as LA
  from numpy.random import default_rng

  print ( '' )
  print ( 'wishart_unit_sample_test():' )
  print ( '  wishart_unit_sample() samples unit Wishart matrices by:' )
  print ( '  W = wishart_unit_sample ( n, df )' )

  seed = 123456789
  rng = default_rng ( seed )
#
#  Set the parameters and call.
#
  n = 5
  df = 8
  w = wishart_unit_sample ( n, df, rng )
  r8mat_print ( n, n, w, '  wishart_unit_sample ( 5, 8 ):' )
#
#  Calling again yields a new matrix.
#
  w = wishart_unit_sample ( n, df, rng )
  r8mat_print ( n, n, w, '  wishart_unit_sample ( 5, 8 ):' )
#
#  Reduce DF
#
  n = 5
  df = 5
  w = wishart_unit_sample ( n, df, rng )
  r8mat_print ( n, n, w, '  wishart_unit_sample ( 5, 5 ):' )
#
#  Try a smaller matrix.
#
  n = 3
  df = 5
  w = wishart_unit_sample ( n, df, rng )
  r8mat_print ( n, n, w, '  wishart_unit_sample ( 3, 5 ):' )
#
#  What is the eigendecomposition of the matrix?
#
  eigval, eigvec = LA.eig ( w )
  r8mat_print ( n, n, eigvec, '  Eigenvectors of previous matrix:' )
  r8vec_print ( n, eigval, '  Eigenvalues of previous matrix:' )

  return

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

if ( __name__ == '__main__' ):
  timestamp ( )
  wishart_matrix_test ( )
  timestamp ( )

