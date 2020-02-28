#! /usr/bin/env python3
#
def jacobi_eigenvalue ( n, a, it_max ):

#*****************************************************************************80
#
## JACOBI_EIGENVALUE carries out the Jacobi eigenvalue iteration.
#
#  Discussion:
#
#    This function computes the eigenvalues and eigenvectors of a
#    real symmetric matrix, using Rutishauser's modfications of the classical
#    Jacobi rotation method with threshold pivoting. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real A(N,N), the matrix, which must be square, real,
#    and symmetric.
#
#    Input, integer IT_MAX, the maximum number of iterations.
#
#    Output, real V(N,N), the matrix of eigenvectors.
#
#    Output, real D(N), the eigenvalues, in descending order.
#
#    Output, integer IT_NUM, the total number of iterations.
#
#    Output, integer ROT_NUM, the total number of rotations.
#
  import numpy as np

  v = np.zeros ( [ n, n ] )
  d = np.zeros ( n )
  
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      v[i,j] = 0.0
    v[j,j] = 1.0

  for i in range ( 0, n ):
    d[i] = a[i,i]

  bw = np.zeros ( n )
  zw = np.zeros ( n )
  w = np.zeros ( n )

  for i in range ( 0, n ):
    bw[i] = d[i]

  it_num = 0
  rot_num = 0

  while ( it_num < it_max ):

    it_num = it_num + 1
#
#  The convergence threshold is based on the size of the elements in
#  the strict upper triangle of the matrix.
#
    thresh = 0.0
    for j in range ( 0, n ):
      for i in range ( 0, j ):
        thresh = thresh + a[i,j] ** 2

    thresh = np.sqrt ( thresh ) / float ( 4 * n )

    if ( thresh == 0.0 ):
      break

    for p in range ( 0, n ):
      for q in range ( p + 1, n ):

        gapq = 10.0 * abs ( a[p,q] )
        termp = gapq + abs ( d[p] )
        termq = gapq + abs ( d[q] )
#
#  Annihilate tiny offdiagonal elements.
#
        if ( 4 < it_num and termp == abs ( d[p] ) and termq == abs ( d[q] ) ):

          a[p,q] = 0.0
#
#  Otherwise, apply a rotation.
#
        elif ( thresh <= abs ( a[p,q] ) ):

          h = d[q] - d[p]
          term = abs ( h ) + gapq

          if ( term == abs ( h ) ):
            t = a[p,q] / h
          else:
            theta = 0.5 * h / a[p,q]
            t = 1.0 / ( abs ( theta ) + np.sqrt ( 1.0 + theta * theta ) )
            if ( theta < 0.0 ):
              t = - t

          c = 1.0 / np.sqrt ( 1.0 + t * t )
          s = t * c
          tau = s / ( 1.0 + c )
          h = t * a[p,q]
#
#  Accumulate corrections to diagonal elements.
#
          zw[p] = zw[p] - h                  
          zw[q] = zw[q] + h
          d[p] = d[p] - h
          d[q] = d[q] + h

          a[p,q] = 0.0
#
#  Rotate, using information from the upper triangle of A only.
#
          for j in range ( 0, p ):
            g = a[j,p]
            h = a[j,q]
            a[j,p] = g - s * ( h + g * tau )
            a[j,q] = h + s * ( g - h * tau )

          for j in range ( p + 1, q ):
            g = a[p,j]
            h = a[j,q]
            a[p,j] = g - s * ( h + g * tau )
            a[j,q] = h + s * ( g - h * tau )

          for j in range ( q + 1, n ):
            g = a[p,j]
            h = a[q,j]
            a[p,j] = g - s * ( h + g * tau )
            a[q,j] = h + s * ( g - h * tau )
#
#  Accumulate information in the eigenvector matrix.
#
          for j in range ( 0, n ):
            g = v[j,p]
            h = v[j,q]
            v[j,p] = g - s * ( h + g * tau )
            v[j,q] = h + s * ( g - h * tau )

          rot_num = rot_num + 1

    for i in range ( 0, n ):
      bw[i] = bw[i] + zw[i]
      d[i] = bw[i]
      zw[i] = 0.0
#
#  Restore upper triangle of input matrix.
#
  for j in range ( 0, n ):
    for i in range ( 0, j ):
      a[i,j] = a[j,i]
#
#  Ascending sort the eigenvalues and eigenvectors.
#
  for k in range ( 0, n - 1 ):

    m = k
    for l in range ( k + 1, n ):
      if ( d[l] < d[m] ):
        m = l

    if ( k != m ):

      t    = d[m]
      d[m] = d[k]
      d[k] = t

      for i in range ( 0, n ):
        w[i]   = v[i,m]
        v[i,m] = v[i,k]
        v[i,k] = w[i]

  return v, d, it_num, rot_num

def jacobi_eigenvalue_test01 ( ):

#*****************************************************************************80
#
## JACOBI_EIGENVALUE_TEST01 uses a 4x4 test matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  a = np.array ( [ \
    [   4.0,  -30.0,    60.0,   -35.0, ], \
    [ -30.0,  300.0,  -675.0,   420.0, ], \
    [  60.0, -675.0,  1620.0, -1050.0, ], \
    [ -35.0,  420.0, -1050.0,   700.0  ] ] )

  print ( '' )
  print ( 'JACOBI_EIGENVALUE_TEST01' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JACOBI_EIGENVALUE computes the eigenvalues D' )
  print ( '  and eigenvectors V of a symmetric matrix A so that A * V = D * V.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  it_max = 100

  v, d, it_num, rot_num = jacobi_eigenvalue ( n, a, it_max )

  print ( '' )
  print ( '  Number of iterations = %d' % ( it_num ) )
  print ( '  Number of rotations  = %d' % ( rot_num ) )

  r8vec_print ( n, d, '  Eigenvalues D:' )

  r8mat_print ( n, n, v, '  Eigenvector matrix V:' )
#
#  Compute eigentest.
#
  error_frobenius = r8mat_is_eigen_right ( n, n, a, v, d )
  print ( '' )
  print ( '  Frobenius norm error in eigensystem A*V-D*V = %g' % ( error_frobenius ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JACOBI_EIGENVALUE_TEST01' )
  print ( '  Normal end of execution.' )
  return

def jacobi_eigenvalue_test02 ( ):

#*****************************************************************************80
#
## JACOBI_EIGENVALUE_TEST02 uses a 4x4 test matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  a = np.array ( [ \
    [ 4.0, 0.0, 0.0, 0.0 ], \
    [ 0.0, 1.0, 0.0, 0.0 ], \
    [ 0.0, 0.0, 3.0, 0.0 ], \
    [ 0.0, 0.0, 0.0, 2.0 ] ] )

  print ( '' )
  print ( 'JACOBI_EIGENVALUE_TEST02' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JACOBI_EIGENVALUE computes the eigenvalues D' )
  print ( '  and eigenvectors V of a symmetric matrix so that A * V = D * V.' )
  print ( '' )
  print ( '  As a sanity check, input a diagonal matrix.' )

  r8mat_print ( n, n, a, '  Input matrix A:' )

  it_max = 100

  [ v, d, it_num, rot_num ] = jacobi_eigenvalue ( n, a, it_max );

  print ( '' )
  print ( '  Number of iterations = %d' % ( it_num ) )
  print ( '  Number of rotations  = %d' % ( rot_num ) )

  r8vec_print ( n, d, '  Eigenvalues D:' )

  r8mat_print ( n, n, v, '  Eigenvector matrix V:' )
#
#  Compute eigentest.
#
  error_frobenius = r8mat_is_eigen_right ( n, n, a, v, d );
  print ( '' )
  print ( '  Frobenius norm error in eigensystem A*V-D*V = %g' % ( error_frobenius ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JACOBI_EIGENVALUE_TEST02' )
  print ( '  Normal end of execution.' )
  return

def jacobi_eigenvalue_test03 ( ):

#*****************************************************************************80
#
## JACOBI_EIGENVALUE_TEST03 uses a 5x5 test matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'JACOBI_EIGENVALUE_TEST03' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JACOBI_EIGENVALUE computes the eigenvalues D' )
  print ( '  and eigenvectors V of a symmetric matrix so that A * V = D * V.' )
  print ( '' )
  print ( '  Use the discretized second derivative matrix.' )

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == j ):
        a[i,j] = -2.0
      elif ( i == j + 1 or i == j - 1 ):
        a[i,j] = 1.0

  r8mat_print ( n, n, a, '  Input matrix A:' )

  it_max = 100

  [ v, d, it_num, rot_num ] = jacobi_eigenvalue ( n, a, it_max );

  print ( '' )
  print ( '  Number of iterations = %d' % ( it_num ) )
  print ( '  Number of rotations  = %d' % ( rot_num ) )

  r8vec_print ( n, d, '  Eigenvalues D:' )

  r8mat_print ( n, n, v, '  Eigenvector matrix V:' )
#
#  Compute eigentest.
#
  error_frobenius = r8mat_is_eigen_right ( n, n, a, v, d );
  print ( '' )
  print ( '  Frobenius norm error in eigensystem A*V-D*V = %g' % ( error_frobenius ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JACOBI_EIGENVALUE_TEST03' )
  print ( '  Normal end of execution.' )
  return

def jacobi_eigenvalue_test ( ):

#*****************************************************************************80
#
## JACOBI_EIGENVALUE_TEST tests the JACOBI_EIGENVALUE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'JACOBI_EIGENVALUE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the JACOBI_EIGENVALUE library.' )

  jacobi_eigenvalue_test01 ( )
  jacobi_eigenvalue_test02 ( )
  jacobi_eigenvalue_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'JACOBI_EIGENVALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_diag_get_vector ( n, a ):

#*****************************************************************************80
#
## R8MAT_DIAG_GET_VECTOR returns the diagonal of an R8MAT in a vector.
#
#  Discussion:
#
#    An R8MAT is an MxN array of R8's, stored by (I,J) -> [I+J*M].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns of
#    the matrix.
#
#    Input, real A(N,N), the N by N matrix.
#
#    Output, real V(N), the diagonal entries
#    of the matrix.
#
  import numpy as np

  v = np.zeros ( n )

  for i in range ( 0, n ):
    v[i] = a[i,i]
 
  return v

def r8mat_diag_get_vector_test ( ):

#*****************************************************************************80
#
## R8MAT_DIAG_GET_VECTOR_TEST tests R8MAT_DIAG_GET_VECTOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = m
  seed = 123456789

  print ( '' )
  print ( 'R8MAT_DIAG_GET_VECTOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_DIAG_GET_VECTOR retrieves the diagonal from an R8MAT.' )

  a, seed = r8mat_uniform_01 ( m, n, seed )

  r8mat_print ( m, n, a, '  Random R8MAT:' )

  v = r8mat_diag_get_vector ( n, a )
  r8vec_print ( n, v, '  Diagonal vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_DIAG_GET_VECTOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_identity ( n ):

#*****************************************************************************80
#
## R8MAT_IDENTITY sets up an NxN identity matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ), dtype = np.float64 )

  for i in range ( 0, n ):
    a[i,i] = 1.0

  return a

def r8mat_identity_test ( ):

#*****************************************************************************80
#
## R8MAT_IDENTITY_TEST tests R8MAT_IDENTITY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8MAT_IDENTITY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IDENTITY creates an identity matrix.' )

  m = 5
  n = m
  a = r8mat_identity ( n )
  r8mat_print ( m, n, a, '  The identity matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IDENTITY_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8mat_is_eigen_right ( n, k, a, x, lam ):

#*****************************************************************************80
#
## R8MAT_IS_EIGEN_RIGHT determines the error in a right eigensystem.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    This routine computes the Frobenius norm of
#
#      A * X - X * LAMBDA
#
#    where
#
#      A is an N by N matrix,
#      X is an N by K matrix (each of K columns is an eigenvector)
#      LAMBDA is a K by K diagonal matrix of eigenvalues.
#
#    This routine assumes that A, X and LAMBDA are all real.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, integer K, the number of eigenvectors.
#    K is usually 1 or N.
#
#    Input, real A(N,N), the matrix.
#
#    Input, real X(N,K), the K eigenvectors.
#
#    Input, real LAM(K), the K eigenvalues.
#
#    Output, real VALUE, the Frobenius norm
#    of the difference matrix A * X - X * LAM, which would be exactly zero
#    if X and LAM were exact eigenvectors and eigenvalues of A.
#
  c = r8mat_mm ( n, n, k, a, x )

  for j in range ( 0, k ):
    for i in range ( 0, n ):
      c[i,j] = c[i,j] - lam[j] * x[i,j]

  value = r8mat_norm_fro ( n, k, c )

  return value

def r8mat_is_eigen_right_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_EIGEN_RIGHT_TEST tests R8MAT_IS_EIGEN_RIGHT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
#
#  This is the CARRY ( 4.0, 4 ) matrix.
#
  m = 4
  n = m
  a = np.array ( [ \
   [ 0.13671875,   0.60546875,   0.25390625,   0.00390625 ], \
   [ 0.05859375,   0.52734375,   0.39453125,   0.01953125 ], \
   [ 0.01953125,   0.39453125,   0.52734375,   0.05859375 ], \
   [ 0.00390625,   0.25390625,   0.60546875,   0.13671875 ] ] )

  k = 4
  x = np.array ( [ \
    [ 1.0,     6.0,    11.0,     6.0 ], \
    [ 1.0,     2.0,    -1.0,    -2.0 ], \
    [ 1.0,    -2.0,    -1.0,     2.0 ], \
    [ 1.0,    -6.0,    11.0,    -6.0 ] ] )

  lam = np.array ( [ \
     1.000000000000000, \
     0.250000000000000, \
     0.062500000000000, \
     0.015625000000000 ] )

  print ( '' )
  print ( 'R8MAT_IS_EIGEN_RIGHT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_EIGEN_RIGHT tests the error in the right eigensystem' )
  print ( '    A * X - X * LAMBDA = 0' )

  r8mat_print ( n, n, a, '  Matrix A:' )
  r8mat_print ( n, k, x, '  Eigenmatrix X:' )
  r8vec_print ( n, lam, '  Eigenvalues LAM:' )

  value = r8mat_is_eigen_right ( n, k, a, x, lam )

  print ( '' )
  print ( '  Frobenius norm of A*X-X*LAMBDA is %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_EIGEN_RIGHT_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8mat_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## R8MAT_MM multiplies two R8MAT's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, N3, the order of the matrices.
#
#    Input, real A(N1,N2), B(N2,N3), the matrices to multiply.
#
#    Output, real  C(N1,N3), the product matrix C = A * B.
#
  import numpy as np

  c = np.zeros ( ( n1, n3 ) )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def r8mat_mm_test ( ):

#*****************************************************************************80
#
## R8MAT_MM_TEST tests R8MAT_MM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'R8MAT_MM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_MM computes a matrix-matrix product C = A * B;' )

  a = np.zeros ( ( n1, n2 ) )

  for i in range ( 0, n1 ): 
    for j in range ( 0, n2 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = np.transpose ( a )

  c = r8mat_mm ( n1, n2, n3, a, b )

  r8mat_print ( n1, n2, a, '  A:' )
  r8mat_print ( n2, n3, b, '  B:' )
  r8mat_print ( n1, n3, c, '  C = A*B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_MM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8mat_norm_fro ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_NORM_FRO returns the Frobenius norm of an R8MAT.
#
#  Discussion:
#
#    The Frobenius norm is defined as
#
#      value = sqrt ( sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J)^2 )
#
#    The matrix Frobenius norm is not derived from a vector norm, but
#    is compatible with the vector L2 norm, so that:
#
#      vec_norm_l2 ( A * x ) <= mat_norm_fro ( A ) * vec_norm_l2 ( x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix whose Frobenius
#    norm is desired.
#
#    Output, real VALUE, the Frobenius norm of A.
#
  import numpy as np
 
  value = np.sqrt ( sum ( sum ( a ** 2 ) ) )

  return value

def r8mat_norm_fro_test ( ):

#*****************************************************************************80
#
## R8MAT_NORM_FRO_TEST tests R8MAT_NORM_FRO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4

  a = np.zeros ( ( m, n ) )

  k = 0
  t1 = 0.0

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k
      t1 = t1 + k * k

  t1 = np.sqrt ( t1 )

  print ( '' )
  print ( 'R8MAT_NORM_FRO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_NORM_FRO computes the Frobenius norm of an R8MAT;' )

  t2 = r8mat_norm_fro ( m, n, a )

  r8mat_print ( m, n, a, '  A:' )
  print ( '' )
  print ( '  Expected Frobenius norm = %g' % ( t1 ) )
  print ( '  Computed Frobenius norm = %g' % ( t2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_NORM_FRO_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return


def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  jacobi_eigenvalue_test ( )
  timestamp ( )

