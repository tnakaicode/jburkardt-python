#! /usr/bin/env python3
#
def gram_schmidt_test ( ):

#*****************************************************************************80
#
## gram_schmidt_test() tests gram_schmidt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'gram_schmidt_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test gram_schmidt().' )

  rng = default_rng ( seed = 123456789 )
  cgs1_test ( rng )

  rng = default_rng ( seed = 123456789 )
  cgs2_test ( rng )

  rng = default_rng ( seed = 123456789 )
  cgs3_test ( rng )

  rng = default_rng ( seed = 123456789 )
  cgs4_test ( rng )

  rng = default_rng ( seed = 123456789 )
  gram_schmidt_naive_test ( rng )

  rng = default_rng ( seed = 123456789 )
  gram_schmidt_tolerance_test ( rng )

  rng = default_rng ( seed = 123456789 )
  mgs1_test ( rng )

  rng = default_rng ( seed = 123456789 )
  mgs2_test ( rng )

  rng = default_rng ( seed = 123456789 )
  mgs3_test ( rng )

  rng = default_rng ( seed = 123456789 )
  mgs4_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'gram_schmidt_test():' )
  print ( '  Normal end of execution.' )

  return

def cgs1 ( A ):

#*****************************************************************************80
#
## cgs1() applies the classical Gram-Schmidt algorithm with no normalization.
#
#  Discussion:
#
#    The output of this function will be a set of orthogonal vectors,
#    such that U(:,i) dot U(:,j) is zero if i is not equal to j.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), a matrix of N vectors.
#
#  Output:
#
#    real U(M,N), a matrix with orthogonal columns.
#
  import numpy as np

  m, n = A.shape

  U = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    v = A[:,j]

    for j2 in range ( 0, j ):
      v2 = U[:,j2]
      p = np.dot ( v, v2 ) / np.dot ( v2, v2 )
      v = v - p * v2

    U[:,j] = v
 
  return U

def cgs1_test ( rng ):

#*****************************************************************************80
#
## cgs1_test() tests cgs1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'cgs1_test():' )
  print ( '  Test cgs1().' )
#
#  Use columns of the same matrix for all tests.
#
  A = rng.uniform ( low = -10.0, high = +10.0, size = [ 3, 4 ] )
  A = np.round ( A )
  A = np.array ( [[ 1, 2, 3, 4 ], [4,5,6,7], [7,8,9,10]], dtype = float)

  m = 3
  na = 2
  A1 = A[0:m,0:na]
  print ( '  A1:' )
  print ( A1 )
  U = cgs1 ( A1 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 3
  A2 = A[0:m,0:na]
  print ( '  A2:' )
  print ( A2 )
  U = cgs1 ( A2 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 4
  A3 = A[0:m,0:na]
  print ( '  A3:' )
  print ( A3 )
  U = cgs1 ( A3 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  return

def cgs2 ( A ):

#*****************************************************************************80
#
## cgs2() applies the classical Gram-Schmidt algorithm with normalization.
#
#  Discussion:
#
#    The output of this function will be a set of orthonormal vectors,
#    such that U(:,i) dot U(:,j) = delta(i,j).
#
#    Some vectors might be exactly zero, in which case othonormality
#    does not apply to them.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), a matrix of N vectors.
#
#  Output:
#
#    real U(M,N), a matrix with orthonormal columns.
#
  import numpy as np

  m, n = A.shape

  U = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    v = A[:,j]

    for j2 in range ( 0, j ):
      v2 = U[:,j2]
      p = np.dot ( v, v2 ) / np.linalg.norm ( v2 )
      v = v - p * v2

    vnorm = np.linalg.norm ( v )
    if ( 0.0 < vnorm ):
      v = v / vnorm

    U[:,j] = v

  return U

def cgs2_test ( rng ):

#*****************************************************************************80
#
## cgs2_test() tests cgs2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'cgs2_test():' )
  print ( '  Test cgs2().' )
#
#  Use columns of the same matrix for all tests.
#
  A = rng.uniform ( low = -10.0, high = +10.0, size = [ 3, 4 ] )
  A = np.round ( A )

  m = 3
  na = 2
  A1 = A[0:m,0:na]
  print ( '  A1:' )
  print ( A1 )
  U = cgs2 ( A1 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 3
  A2 = A[0:m,0:na]
  print ( '  A2:' )
  print ( A2 )
  U = cgs2 ( A2 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 4
  A3 = A[0:m,0:na]
  print ( '  A3:' )
  print ( A3 )
  U = cgs2 ( A3 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  return

def cgs3 ( A ):

#*****************************************************************************80
#
## cgs3() applies the classical Gram-Schmidt algorithm with normalization.
#
#  Discussion:
#
#    The output of this function will be a set of orthonormal vectors,
#    such that U(:,i) dot U(:,j) = delta(i,j).
#
#    Zero vectors will not be included in the output.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), a matrix of N vectors.
#
#  Output:
#
#    Output, real U(M,K), a matrix with orthonormal columns.
#
  import numpy as np

  m, n = A.shape

  k = 0
  U = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    v = A[:,j]

    for j2 in range ( 0, k ):
      v2 = U[:,j2]
      p = np.dot ( v, v2 ) / np.linalg.norm ( v2 )
      v = v - p * v2

    vnorm = np.linalg.norm ( v )
    if ( 0.0 < vnorm ):
      v = v / vnorm
      U[:,k] = v
      k = k + 1

  return U

def cgs3_test ( rng ):

#*****************************************************************************80
#
## cgs3_test() tests cgs3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'cgs3_test():' )
  print ( '  Test cgs3().' )
#
#  Use columns of the same matrix for all tests.
#
  A = rng.uniform ( low = -10.0, high = +10.0, size = [ 3, 4 ] )
  A = np.round ( A )

  m = 3
  na = 2
  A1 = A[0:m,0:na]
  print ( '  A1:' )
  print ( A1 )
  U = cgs3 ( A1 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 3
  A2 = A[0:m,0:na]
  print ( '  A2:' )
  print ( A2 )
  U = cgs3 ( A2 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 4
  A3 = A[0:m,0:na]
  print ( '  A3:' )
  print ( A3 )
  U = cgs3 ( A3 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  return

def cgs4 ( A, tol ):

#*****************************************************************************80
#
## cgs4() applies the classical Gram-Schmidt algorithm with normalization.
#
#  Discussion:
#
#    The output of this function will be a set of orthonormal vectors,
#    such that U(:,i) dot U(:,j) = delta(i,j).
#
#    The process will reject zero vectors, as well as vectors with very
#    small remainder after the subtraction of projections of previously 
#    accepted vectors.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), a matrix of N vectors.
#
#    real TOL, the acceptance tolerance.
#
#  Output:
#
#    real U(M,K), a matrix with orthonormal columns.
#
  import numpy as np

  m, n = A.shape

  k = 0
  U = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    v = A[:,j]

    for j2 in range ( 0, k ):
      v2 = U[:,j2]
      p = np.dot ( v, v2 )
      v = v - p * v2

    vnorm = np.linalg.norm ( v )
    if ( tol < vnorm ):
      v = v / vnorm
      U[:,k] = v
      k = k + 1

  return U

def cgs4_test ( rng ):

#*****************************************************************************80
#
## cgs4_test() tests cgs4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'cgs4_test():' )
  print ( '  Test cgs4().' )

  tol = 1000.0 * np.finfo ( float ).eps
#
#  Use columns of the same matrix for all tests.
#
  A = rng.uniform ( low = -10.0, high = +10.0, size = [ 3, 4 ] )
  A = np.round ( A )

  m = 3
  na = 2
  A1 = A[0:m,0:na]
  print ( '  A1:' )
  print ( A1 )
  U = cgs4 ( A1, tol )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 3
  A2 = A[0:m,0:na]
  print ( '  A2:' )
  print ( A2 )
  U = cgs4 ( A2, tol )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 4
  A3 = A[0:m,0:na]
  print ( '  A3:' )
  print ( A3 )
  U = cgs4 ( A3, tol )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  return

def gram_schmidt_naive ( A ):

#*****************************************************************************80
#
## gram_schmidt_naive() applies the naive Gram-Schmidt orthonormalization process.
#
#  Discussion:
#
#    Because of roundoff, the orthonormalization process may have
#    significant errors.
#
#    In fact, given a matrix with M < N, the process is unlikely to notice
#    that no more than M columns can be linearly independent.
#
#    In exact arithmetic, linearly dependent columns would be returned
#    as 0 columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), a matrix whose columns are to be orthonormalized.
#
#  Output:
#
#    real U(M,N), the matrix with orthonormalized columns.
#
  import numpy as np

  m, n = A.shape

  U = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    v = A[:,j]

    for j2 in range ( 0, j ):
      vu = np.dot ( v, U[:,j2] )
      v = v - vu * U[:,j2]

    v_norm = np.linalg.norm ( v )
    if ( 0.0 < v_norm ):
      U[:,j] = v / v_norm

  return U

def gram_schmidt_naive_test ( rng ):

#*****************************************************************************80
#
## gram_schmidt_naive_test() tests gram_schmidt_naive().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'gram_schmidt_naive_test():' )
  print ( '  Test gram_schmidt_naive().' )
#
#  Use columns of the same matrix for all tests.
#
  A = rng.uniform ( low = -10.0, high = +10.0, size = [ 3, 4 ] )
  A = np.round ( A )
  A = np.array ( [[ 1, 2, 3, 4 ], [4,5,6,7], [7,8,9,10]], dtype = float)

  m = 3
  na = 2
  A1 = A[0:m,0:na]
  print ( '  A1:' )
  print ( A1 )
  U = gram_schmidt_naive ( A1 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 3
  A2 = A[0:m,0:na]
  print ( '  A2:' )
  print ( A2 )
  U = gram_schmidt_naive ( A2 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 4
  A3 = A[0:m,0:na]
  print ( '  A3:' )
  print ( A3 )
  U = gram_schmidt_naive ( A3 )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  return

def gram_schmidt_tolerance ( A, tol ):

#*****************************************************************************80
#
## gram_schmidt_tolerance() implements Gram-Schmidt orthonormalization.
#
#  Discussion:
#
#    A tolerance is used to discard vectors whose orthogonal component
#    is very small.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,NA), a matrix whose columns are to be orthonormalized.
#
#    real TOL, the tolerance.
#
#  Output:
#
#    real U(M,NU), the matrix with orthonormalized columns.
#    Note that 0 <= NU <= NA, because some columns of A may be rejected.
#
  import numpy as np

  m, na = A.shape

  nu = 0
  U = np.zeros ( [ m, nu ] )

  for j in range ( 0, na ):

    v = A[:,j]

    for j2 in range ( 0, nu ):
      vu = np.dot ( v, U[:,j2] )
      v = v - vu * U[:,j2]
#
#  Appending a column vector to a matrix is absurdly badly implemented
#  and documented.  IT SHOULD BE EASY!
#
    v_norm = np.linalg.norm ( v )
    if ( tol < v_norm ):
      v = v.reshape ( m, 1 ) / v_norm
      nu = nu + 1
      U = np.hstack ( ( U, v ) )

  return U

def gram_schmidt_tolerance_test ( rng ):

#*****************************************************************************80
#
## gram_schmidt_tolerance_test() tests gram_schmidt_tolerance().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'gram_schmidt_tolerance_test():' )
  print ( '  Test gram_schmidt_tolerance().' )
#
#  Use columns of the same matrix for all tests.
#
  A = rng.uniform ( low = -10.0, high = +10.0, size = [ 3, 4 ] )
  A = np.round ( A )
  A = np.array ( [[ 1, 2, 3, 4 ], [4,5,6,7], [7,8,9,10]], dtype = float)

  tol = 0.00001

  m = 3
  na = 2
  A1 = A[0:m,0:na]
  print ( '  A1:' )
  print ( A1 )
  U = gram_schmidt_tolerance ( A1, tol )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( np.transpose ( U ), U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 3
  A2 = A[0:m,0:na]
  print ( '  A2:' )
  print ( A2 )
  U = gram_schmidt_tolerance ( A2, tol )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( np.transpose ( U ), U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 4
  A3 = A[0:m,0:na]
  print ( '  A3:' )
  print ( A3 )
  U = gram_schmidt_tolerance ( A3, tol )
  print ( '  U:' )
  print ( U )
  UTU = np.matmul ( np.transpose ( U ), U )
  print ( "  U' * U:" )
  print ( UTU )

  return

def mgs1 ( A ):

#*****************************************************************************80
#
## mgs1() applies the modified Gram-Schmidt algorithm with no normalization.
#
#  Discussion:
#
#    The output of this function will be a set of orthogonal vectors,
#    such that U(:,i) dot U(:,j) is zero if i is not equal to j.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), a matrix of N vectors.
#
#  Output:
#
#    real U(M,N), a matrix with orthogonal columns.
#
  import numpy as np

  m, n = A.shape

  U = A.copy ( )

  for j in range ( 0, n ):

    v = U[:,j]

    for j2 in range ( j + 1, n ):
      v2 = U[:,j2]
      p = np.dot ( v, v2 ) / np.dot ( v, v )
      v2 = v2 - p * v
      U[:,j2] = v2

  return U

def mgs1_test ( rng ):

#*****************************************************************************80
#
## mgs1_test() tests mgs1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'mgs1_test():' )
  print ( '  Test mgs1().' )
#
#  Use columns of the same matrix for all tests.
#
  A = rng.uniform ( low = -10.0, high = +10.0, size = [ 3, 4 ] )
  A = np.round ( A )
  A = np.array ( [[ 1, 2, 3, 4 ], [4,5,6,7], [7,8,9,10]], dtype = float)

  m = 3
  na = 2
  A1 = A[0:m,0:na]
  print ( '  A1:' )
  print ( A1 )
  U = mgs1 ( A1 )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 3
  A2 = A[0:m,0:na]
  print ( '  A2:' )
  print ( A2 )
  U = mgs1 ( A2 )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 4
  A3 = A[0:m,0:na]
  print ( '  A3:' )
  print ( A3 )
  U = mgs1 ( A3 )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  return

def mgs2 ( A ):

#*****************************************************************************80
#
## mgs2() applies the modified Gram-Schmidt algorithm with normalization.
#
#  Discussion:
#
#    The output of this function will be a set of orthonormal vectors,
#    such that U(:,i) dot U(:,j) = delta(i,j).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), a matrix of N vectors.
#
#  Output:
#
#    real U(M,N), a matrix with orthonormal columns.
#
  import numpy as np

  m, n = A.shape

  U = A.copy ( )

  for j in range ( 0, n ):

    v = U[:,j]
    v = v / np.linalg.norm ( v )
    U[:,j] = v

    for j2 in range ( j + 1, n ):
      v2 = U[:,j2]
      p = np.dot ( v, v2 )
      v2 = v2 - p * v
      U[:,j2] = v2

  return U

def mgs2_test ( rng ):

#*****************************************************************************80
#
## mgs2_test() tests mgs2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'mgs2_test():' )
  print ( '  Test mgs2().' )
#
#  Use columns of the same matrix for all tests.
#
  A = rng.uniform ( low = -10.0, high = +10.0, size = [ 3, 4 ] )
  A = np.round ( A )

  m = 3
  na = 2
  A1 = A[0:m,0:na]
  print ( '  A1:' )
  print ( A1 )
  U = mgs2 ( A1 )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 3
  A2 = A[0:m,0:na]
  print ( '  A2:' )
  print ( A2 )
  U = mgs2 ( A2 )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 4
  A3 = A[0:m,0:na]
  print ( '  A3:' )
  print ( A3 )
  U = mgs2 ( A3 )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  return

def mgs3 ( A ):

#*****************************************************************************80
#
## mgs3() applies the modified Gram-Schmidt algorithm with normalization.
#
#  Discussion:
#
#    The output of this function will be a set of orthonormal vectors,
#    such that U(:,i) dot U(:,j) = delta(i,j).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), a matrix of N vectors.
#
#  Output:
#
#    real U(M,K), a matrix with orthonormal columns.
#
  import numpy as np

  m, n = A.shape

  k = 0
  U = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    v = A[:,j]
    vnorm = np.linalg.norm ( v )

    if ( 0.0 < vnorm ):

      v = v / vnorm
      U[:,k] = v
      k = k + 1

      for j2 in range ( j + 1, n ):
        v2 = A[:,j2]
        p = np.dot ( v, v2 )
        v2 = v2 - p * v
        A[:,j2] = v2

  return U

def mgs3_test ( rng ):

#*****************************************************************************80
#
## mgs3_test() tests mgs3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'mgs3_test():' )
  print ( '  Test mgs3().' )
#
#  Use columns of the same matrix for all tests.
#
  A = rng.uniform ( low = -10.0, high = +10.0, size = [ 3, 4 ] )
  A = np.round ( A )

  m = 3
  na = 2
  A1 = A[0:m,0:na]
  print ( '  A1:' )
  print ( A1 )
  U = mgs3 ( A1 )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 3
  A2 = A[0:m,0:na]
  print ( '  A2:' )
  print ( A2 )
  U = mgs3 ( A2 )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 4
  A3 = A[0:m,0:na]
  print ( '  A3:' )
  print ( A3 )
  U = mgs3 ( A3 )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  return

def mgs4 ( A, tol ):

#*****************************************************************************80
#
## mgs4() applies the modified Gram-Schmidt algorithm with normalization.
#
#  Discussion:
#
#    The output of this function will be a set of orthonormal vectors,
#    such that U(:,i) dot U(:,j) = delta(i,j).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), a matrix of N vectors.
#
#  Output:
#
#    real U(M,K), a matrix with orthonormal columns.
#
  import numpy as np

  m, n = A.shape

  k = 0
  U = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    v = A[:,j]
    vnorm = np.linalg.norm ( v )

    if ( tol < vnorm ):

      v = v / vnorm
      U[:,k] = v
      k = k + 1

      for j2 in range ( j + 1, n ):
        v2 = A[:,j2]
        p = np.dot ( v, v2 )
        v2 = v2 - p * v
        A[:,j2] = v2

  return U

def mgs4_test ( rng ):

#*****************************************************************************80
#
## mgs4_test() tests mgs4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'mgs4_test():' )
  print ( '  Test mgs4().' )

  tol = 1000.0 * np.finfo ( float ).eps
#
#  Use columns of the same matrix for all tests.
#
  A = rng.uniform ( low = -10.0, high = +10.0, size = [ 3, 4 ] )
  A = np.round ( A )

  m = 3
  na = 2
  A1 = A[0:m,0:na]
  print ( '  A1:' )
  print ( A1 )
  U = mgs4 ( A1, tol )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 3
  A2 = A[0:m,0:na]
  print ( '  A2:' )
  print ( A2 )
  U = mgs4 ( A2, tol )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

  m = 3
  na = 4
  A3 = A[0:m,0:na]
  print ( '  A3:' )
  print ( A3 )
  U = mgs4 ( A3, tol )
  print ( "  U:" )
  UTU = np.matmul ( U.T, U )
  print ( "  U' * U:" )
  print ( UTU )

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
  gram_schmidt_test ( )
  timestamp ( )

