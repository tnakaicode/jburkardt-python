#! /usr/bin/env python3
#
def normal_dataset_test ( ):

#*****************************************************************************80
#
## normal_dataset_test() tests normal_dataset().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 May 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'normal_dataset_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test normal_dataset().' )
#
#  Select the default random number generator.
#  Vary the value of seed to get new results.
#
  seed = 123456789
  rng = default_rng ( seed = seed )

  m = 2
  n = 1000
  mu = np.array ( [ 1, 2 ] )
  A = np.array ( [
    [ 1.0, 1.0 ], \
    [ 1.0, 3.0 ]
  ] )

  r = normal_dataset ( m, n, rng, mu, A )
#
#  Make a quick plot of the data.
#
  import matplotlib.pyplot as plt
  plt.clf ( )
  plt.plot ( r[0,:], r[1,:], '.' )
  plt.grid ( 'True' )
  plt.axis ( 'equal' )
  filename = 'normal_' + str ( m ) + '_' + str ( n ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'normal_dataset_test():' )
  print ( '  Normal end of execution.' )

  return

def normal_dataset ( m, n, rng, mu, a ):

#*****************************************************************************80
#
## normal_dataset() generates a multivariate normal dataset and writes it to a file.
#
#  Usage:
#
#    x = normal_dataset ( m, n, rng, mu, a )
#
#    where
#
#    * M the spatial dimension
#    * N the number of points to generate
#    * RNG the current random number generator
#    * MU is the mean vector of dimension M
#    * A is the MxM positive definite symmetric variance-covariance matrix
#    * R is the M by N array created.
#
#    The command creates an M by N multivariate normal dataset and writes 
#    it to the file "normal_M_N.txt".
#
#  Licensing:
#
#    This information is distributed under the MIT license.
#
#  Modified:
#
#    15 May 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'normal_dataset():' )
  print ( '  Generate a multivariate normal random dataset.' )
  print ( '' )
  print ( '  The program requests input values from the user:' )
  print ( '' )
  print ( '  * M, the spatial dimension,' )
  print ( '  * N, the number of points to generate,' )
  print ( '  * RNG, the current random number generator.' )
  print ( '  * MU, the mean vector of length M.' )
  print ( '  * A, the MxM positive definite symmetric variance-covariance matrix.' )
  print ( '' )
  print ( '  The program generates the data and writes it to the file' )
  print ( '' )
  print ( '    normal_M_N.txt' )
  print ( '' )
  print ( '  where "M" and "N" are the numeric values.' )
#
#  Report the input.
#
  print ( '' )
  print ( '  Spatial dimension M = ', m )
  print ( '  Number of points N = ', n )
  r8vec_print ( m, mu, '  The mean vector MU:' )
  r8mat_print ( m, m, a, '  The variance-covariance matrix A:' )
#
#  Compute the data.
#
  r = multinormal_sample ( m, n, a, mu, rng )
#
#  Write it to a file.
#
  filename = 'normal_' + str ( m ) + '_' + str ( n ) + '.txt'
  r8mat_write ( filename, m, n, r )
  print ( '' )
  print ( '  The data was written to "' + filename + "'" )

  return r

def multinormal_sample ( m, n, a, mu, rng ):

#*****************************************************************************80
#
## multinormal_sample() samples a multivariate normal distribution.
#
#  Discussion:
#
#    The multivariate normal distribution for the M dimensional vector X
#    has the form:
#
#      pdf(X) = (2*pi*det(A))**(-M/2) * exp(-0.5*(X-MU)'*inverse(A)*(X-MU))
#
#    where MU is the mean vector, and A is a positive definite symmetric
#    matrix called the variance-covariance matrix.
#
#  Licensing:
#
#    This information is distributed under the MIT license. 
#
#  Modified:
#
#    15 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the dimension of the space.
#
#    integer N, the number of points.
#
#    real A(M,M), the variance-covariance 
#    matrix.  A must be symmetric positive definite.
#
#    real MU(M), the mean vector.
#
#    RNG: the current random number generator.
#
#  Output:
#
#    real X(M,N), the points.
#
  import numpy as np
#
#  Compute the upper triangular Cholesky factor R of the variance-covariance matrix.
#
  r = r8po_fa ( m, a )
#
#  Get an MxN matrix of samples of the 1D normal distribution with mean 0
#  and variance 1.  
#
  x = rng.normal ( loc = 0.0, scale = 1.0, size = [ m, n ] )
#
#  Compute X = MU + R' * X.
#
  for j in range ( 0, n ):
    x[:,j] = mu[:] + np.dot ( np.transpose ( r ), x[:,j] )

  return x

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

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## r8mat_write() writes an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8po_fa ( n, a ):

#*****************************************************************************80
#
## r8po_fa() factors a R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
#
#    The positive definite symmetric matrix A has a Cholesky factorization
#    of the form:
#
#      A = R' * R
#
#    where R is an upper triangular matrix with positive elements on
#    its diagonal.  This routine overwrites the matrix A with its
#    factor R.
#
#    This function failed miserably when I wrote "r = a", because of a
#    disastrously misconceived feature of Python, which does not copy
#    one matrix to another, but makes them both point to the same object.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 May 2024
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix in R8PO storage.
#
#  Output:
#
#    real R(N,N), the Cholesky factor R in R8GE storage.
#
#    integer INFO, error flag.
#    0, normal return.
#    K, error condition.  The principal minor of order K is not
#    positive definite, and the factorization was not completed.
#
  import numpy as np

  r = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      r[i,j] = a[i,j]

  for j in range ( 0, n ):

    for k in range ( 0, j ):
      t = 0.0
      for i in range ( 0, k ):
        t = t + r[i,k] * r[i,j]
      r[k,j] = ( r[k,j] - t ) / r[k,k]

    t = 0.0
    for i in range ( 0, j ):
      t = t + r[i,j] ** 2

    s = r[j,j] - t

    if ( s <= 0.0 ):
      print ( '' )
      print ( 'r8po_fa(): Fatal error!' )
      print ( '  Factorization fails on column', j )
      raise Exception ( 'r8po_fa(): Fatal error!' )

    r[j,j] = np.sqrt ( s )
#
#  Since the Cholesky factor is stored in R8GE format, be sure to
#  zero out the lower triangle.
#
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      r[i,j] = 0.0

  return r

def r8mat_normal_01 ( m, n, rng ):

#*****************************************************************************80
#
## r8mat_normal_01() returns an R8MAT of  normal random values.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N: the number of rows and columns.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real X(M,N), the random normal values.
#
  import numpy as np

  x = rng.normal ( loc = 0.0, scale = 1.0, size = [ m, n ] )

  return x

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
  normal_dataset_test ( )
  timestamp ( )

