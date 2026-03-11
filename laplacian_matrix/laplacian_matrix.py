#! /usr/bin/env python3
#
def laplacian_matrix_test ( ):

#*****************************************************************************80
#
## laplacian_matrix_test() tests laplacian_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'laplacian_matrix_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test laplacian_matrix()' )

  laplacian_matrix_test01 ( )
  laplacian_matrix_test02 ( )
  laplacian_matrix_test03 ( )
  laplacian_matrix_test04 ( )
  laplacian_matrix_test05 ( )
  laplacian_matrix_test06 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'laplacian_matrix_test():' )
  print ( '  Normal end of execution.' )

  return

def laplacian_matrix_test01 ( ):

#*****************************************************************************80
#
## laplacian_matrix_test01() tests l1dd() and similar routines.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laplacian_matrix_test01():' )
  print ( '  A full-storage matrix is returned by:' )
  print ( '  L1DD: Dirichlet/Dirichlet BC' )
  print ( '  L1DN: Dirichlet/Neumann BC' )
  print ( '  L1ND: Neumann/Dirichlet BC' )
  print ( '  L1NN: Neumann/Neumann BC' )
  print ( '  L1PP: Periodic BC' )

  n = 5

  for test in range ( 1, 3 ):

    if ( test == 1 ):
      h = 1.0
    else:
      h = 1.0 / ( n + 1 )

    print ( '' )
    print ( '  Using spacing H = ', h )

    l = l1dd ( n, h )
    print ( '' )
    print ( 'L1DD:' )
    print ( l )

    l = l1dn ( n, h )
    print ( '' )
    print ( 'L1DN:' )
    print ( l )

    l = l1nd ( n, h )
    print ( '' )
    print ( 'L1ND:' )
    print ( l )

    l = l1nn ( n, h )
    print ( '' )
    print ( 'L1NN:' )
    print ( l )

    l = l1pp ( n, h )
    print ( '' )
    print ( 'L1PP:' )
    print ( l )

  return

def laplacian_matrix_test02 ( ):

#*****************************************************************************80
#
## laplacian_matrix_test02() tests l1dd_apply() and similar functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'laplacian_matrix_test02():' )
  print ( '  The Laplacian L is applied to data U by:' )
  print ( '  L1DD_APPLY for Dirichlet/Dirichlet BC' )
  print ( '  L1DN_APPLY for Dirichlet/Neumann BC' )
  print ( '  L1ND_APPLY for Neumann/Dirichlet BC' )
  print ( '  L1NN_APPLY for Neumann/Neumann BC' )
  print ( '  L1PP_APPLY for Periodic BC' )

  n = 9

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = ( i + 1 ) / ( n + 1 )

  h = 1.0 / ( n + 1 )

  print ( '' )
  print ( '  Using spacing H = ', h )

  u = x * ( 1.0 - x )

  print ( '' )
  print ( '  Vector U:' )
  print ( u )

  lu = l1dd_apply ( n, h, u )
  print ( '' )
  print ( '  L1DD(U):' )
  print ( lu )

  lu = l1dn_apply ( n, h, u )
  print ( '' )
  print ( '  L1DN(U):' )
  print ( lu )

  lu = l1nd_apply ( n, h, u )
  print ( '' )
  print ( '  L1ND(U):' )
  print ( lu )

  lu = l1nn_apply ( n, h, u )
  print ( '' )
  print ( '  L1NN(U):' )
  print ( lu )

  lu = l1pp_apply ( n, h, u )
  print ( '' )
  print ( '  L1PP(U):' )
  print ( lu )
  
  return

def laplacian_matrix_test03 ( ):

#*****************************************************************************80
#
## laplacian_matrix_test03() tests l1dd_eigen() and similar routines.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laplacian_matrix_test03():' )
  print ( '  Compute eigen information for the Laplacian:' )
  print ( '  L1DD_EIGEN for Dirichlet/Dirichlet BC' )
  print ( '  L1DN_EIGEN for Dirichlet/Neumann BC' )
  print ( '  L1ND_EIGEN for Neumann/Dirichlet BC' )
  print ( '  L1NN_EIGEN for Neumann/Neumann BC' )
  print ( '  L1PP_EIGEN for Periodic BC' )

  n = 5

  for test in range ( 1, 3 ):

    if ( test == 1 ):
      h = 1.0
    else:
      h = 1.0 / ( n + 1 )

    print ( '' )
    print ( '  Using spacing H = ', h )

    a = l1dd ( n, h )
    v, lamda = l1dd_eigen ( n, h )
    print ( '' )
    print ( '  L1DD Eigenvalues:' )
    print ( lamda )
    print ( '  L1DD Eigenvectors:' )
    print ( v )
    err = eigen_error ( n, n, a, v, lamda )
    print ( '' )
    print ( '  L1DD eigenerror = ', err )

    a = l1dn ( n, h )
    v, lamda = l1dn_eigen ( n, h )
    print ( '' )
    print ( '  L1DN Eigenvalues:' )
    print ( lamda )
    print ( '  L1DN Eigenvectors:' )
    print ( v )
    err = eigen_error ( n, n, a, v, lamda )
    print ( '' )
    print ( '  L1DN eigenerror = ', err )

    a = l1nd ( n, h )
    v, lamda = l1nd_eigen ( n, h )
    print ( '' )
    print ( '  L1ND Eigenvalues:' )
    print ( lamda )
    print ( '  L1ND Eigenvectors:' )
    print ( v )
    err = eigen_error ( n, n, a, v, lamda )
    print ( '' )
    print ( '  L1ND eigenerror = ', err )

    a = l1nn ( n, h )
    v, lamda = l1nn_eigen ( n, h )
    print ( '' )
    print ( '  L1NN Eigenvalues:' )
    print ( lamda )
    print ( '  L1NN Eigenvectors:' )
    print ( v )
    err = eigen_error ( n, n, a, v, lamda )
    print ( '' )
    print ( '  L1NN eigenerror = ', err )

    a = l1pp ( n, h )
    v, lamda = l1pp_eigen ( n, h )
    print ( '' )
    print ( '  L1PP Eigenvalues:' )
    print ( lamda )
    print ( '  L1PP Eigenvectors:' )
    print ( v )
    err = eigen_error ( n, n, a, v, lamda )
    print ( '' )
    print ( '  L1PP eigenerror = ', err )

  return

def laplacian_matrix_test04 ( ):

#*****************************************************************************80
#
## laplacian_matrix_test04() tests l1dd_inverse() and similar routines.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laplacian_matrix_test04():' )
  print ( '  The inverse of a full-storage matrix is returned by:' )
  print ( '  L1DD_INVERSE: Dirichlet/Dirichlet BC' )
  print ( '  L1DN_INVERSE: Dirichlet/Neumann BC' )
  print ( '  L1ND_INVERSE: Neumann/Dirichlet BC' )

  n = 5

  for test in range ( 1, 3 ):

    if ( test == 1 ):
      h = 1.0
    else:
      h = 1.0 / ( n + 1 )

    print ( '' )
    print ( '  Using spacing H = ', h )

    l = l1dd ( n, h )
    print ( '' )
    print ( '  L1DD:' )
    print ( l )
    linv = l1dd_inverse ( n, h )
    print ( '' )
    print ( '  L1DD_INVERSE:' )
    print ( linv )
    err = inverse_error ( n, l, linv )
    print ( '' )
    print ( '  L1DD inverse error = ', err )

    l = l1dn ( n, h )
    print ( '' )
    print ( '  L1DN:' )
    print ( l )
    linv = l1dn_inverse ( n, h )
    print ( '' )
    print ( '  L1DN_INVERSE:' )
    print ( linv )
    err = inverse_error ( n, l, linv )
    print ( '' )
    print ( '  L1DN inverse error = ', err )

    l = l1nd ( n, h )
    print ( '' )
    print ( '  L1ND:' )
    print ( l )
    linv = l1nd_inverse ( n, h )
    print ( '' )
    print ( '  L1ND_INVERSE:' )
    print ( linv )
    err = inverse_error ( n, l, linv )
    print ( '' )
    print ( '  L1ND inverse error = ', err )

  return

def laplacian_matrix_test05 ( ):

#*****************************************************************************80
#
## laplacian_matrix_test05() tests l1dd_cholesky() and similar routines.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laplacian_matrix_test05():' )
  print ( '  Compute upper Cholesky factors for the Laplacian:' )
  print ( '  L1DD_CHOLESKY for Dirichlet/Dirichlet BC' )
  print ( '  L1DN_CHOLESKY for Dirichlet/Neumann BC' )
  print ( '  L1ND_CHOLESKY for Neumann/Dirichlet BC' )
  print ( '  L1NN_CHOLESKY for Neumann/Neumann BC' )
  print ( '  L1PP_CHOLESKY for Periodic BC' )

  n = 5

  for test in range ( 1, 3 ):

    if ( test == 1 ):
      h = 1.0
    else:
      h = 1.0 / ( n + 1 )

    print ( '' )
    print ( '  Using spacing H = ', h )

    a = l1dd ( n, h )
    c = l1dd_cholesky ( n, h )
    print ( '' )
    print ( '  L1DD Cholesky factor:' )
    print ( c )
    err = cholesky_upper_error ( n, a, c )
    print ( '' )
    print ( '  L1DD Cholesky error = ', err )

    a = l1dn ( n, h )
    c = l1dn_cholesky ( n, h )
    print ( '' )
    print ( '  L1DN Cholesky factor:' )
    print ( c )
    err = cholesky_upper_error ( n, a, c )
    print ( '' )
    print ( '  L1DN Cholesky error = ', err )

    a = l1nd ( n, h )
    c = l1nd_cholesky ( n, h )
    print ( '' )
    print ( '  L1ND Cholesky factor:' )
    print ( c )
    err = cholesky_upper_error ( n, a, c )
    print ( '' )
    print ( '  L1ND Cholesky error = ', err )

    a = l1nn ( n, h )
    c = l1nn_cholesky ( n, h )
    print ( '' )
    print ( '  L1NN Cholesky factor:' )
    print ( c )
    err = cholesky_upper_error ( n, a, c )
    print ( '' )
    print ( '  L1NN Cholesky error = ', err )

    a = l1pp ( n, h )
    c = l1pp_cholesky ( n, h )
    print ( '' )
    print ( '  L1PP Cholesky factor:' )
    print ( c )
    err = cholesky_upper_error ( n, a, c )
    print ( '' )
    print ( '  L1PP Cholesky error = ', err )

  return

def laplacian_matrix_test06 ( ):

#*****************************************************************************80
#
## laplacian_matrix_test06() tests l1dd_lu() and similar routines.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'laplacian_matrix_test06():' )
  print ( '  Compute LU factors for the Laplacian:' )
  print ( '  L1DD_LU for Dirichlet/Dirichlet BC' )
  print ( '  L1DN_LU for Dirichlet/Neumann BC' )
  print ( '  L1ND_LU for Neumann/Dirichlet BC' )
  print ( '  L1NN_LU for Neumann/Neumann BC' )
  print ( '  L1PP_LU for Periodic BC' )

  n = 5

  for test in range ( 1, 3 ):

    if ( test == 1 ):
      h = 1.0
    else:
      h = 1.0 / ( n + 1 )

    print ( '' )
    print ( '  Using spacing H = ', h )

    a = l1dd ( n, h )
    l, u = l1dd_lu ( n, h )
    print ( '' )
    print ( '  L1DD L factor:' )
    print ( l )
    print ( '  L1DD U factor:' )
    print ( u )
    err = lu_error ( n, a, l, u )
    print ( '' )
    print ( '  L1DD LU error = ', err )

    a = l1dn ( n, h )
    l, u = l1dn_lu ( n, h )
    print ( '' )
    print ( '  L1DN L factor:' )
    print ( l )
    print ( '  L1DN U factor:' )
    print ( u )
    err = lu_error ( n, a, l, u )
    print ( '' )
    print ( '  L1DN LU error = ', err )

    a = l1nd ( n, h )
    l, u = l1nd_lu ( n, h )
    print ( '' )
    print ( '  L1ND L factor:' )
    print ( l )
    print ( '  L1ND U factor:' )
    print ( u )
    err = lu_error ( n, a, l, u )
    print ( '' )
    print ( '  L1ND LU error = ', err )

    a = l1nn ( n, h )
    l, u = l1nn_lu ( n, h )
    print ( '' )
    print ( '  L1NN L factor:' )
    print ( l )
    print ( '  L1NN U factor:' )
    print ( u )
    err = lu_error ( n, a, l, u )
    print ( '' )
    print ( '  L1NN LU error = ', err )

    a = l1pp ( n, h )
    l, u = l1pp_lu ( n, h )
    print ( '' )
    print ( '  L1PP L factor:' )
    print ( l )
    print ( '  L1PP U factor:' )
    print ( u )
    err = lu_error ( n, a, l, u )
    print ( '' )
    print ( '  L1PP LU error = ', err )

  return

def cholesky_upper_error ( n, a, c ):

#*****************************************************************************80
#
## cholesky_upper_error() determines the error in an upper Cholesky factor.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
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
#    real C(N,N), the upper triangular Cholesky factor.
#
#  Output:
#
#    real ERROR_FROBENIUS, the Frobenius norm
#    of the difference matrix A - C' * C.
#
  import numpy as np

  ctc = np.matmul ( c.transpose ( ), c )

  error_frobenius = np.linalg.norm ( a - ctc, 'fro' )

  return error_frobenius

def eigen_error ( n, k, a, x, lamda ):

#*****************************************************************************80
#
## eigen_error() determines the error in a (right) eigensystem.
#
#  Discussion:
#
#    An R8MAT is a matrix of real ( kind = 8 ) values.
#
#    This routine computes the Frobenius norm of
#
#      A * X - X * LAMDA
#
#    where
#
#      A is an N by N matrix,
#      X is an N by K matrix (each of K columns is an eigenvector)
#      LAMDA is a K by K diagonal matrix of eigenvalues.
#
#    This routine assumes that A, X and LAMDA are all real.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer K, the number of eigenvectors.
#    K is usually 1 or N.
#
#    real A(N,N), the matrix.
#
#    real X(N,K), the K eigenvectors.
#
#    real LAMDA(K,1), the K eigenvalues.
#
#  Output:
#
#    real ERROR_FROBENIUS, the Frobenius norm
#    of the difference matrix A * X - X * LAMDA, which would be exactly zero
#    if X and LAMDA were exact eigenvectors and eigenvalues of A.
#
  import numpy as np

  c = np.matmul ( a, x )

  for j in range ( 0, k ):
    c[:,j] = c[:,j] - x[:,j] * lamda[j]

  error_frobenius = np.linalg.norm ( c, 'fro' )

  return error_frobenius

def inverse_error ( n, a, b ):

#*****************************************************************************80
#
## inverse_error() determines the error in an inverse matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
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
#    real B(N,N), the inverse.
#
#  Output:
#
#    real ERROR_FROBENIUS, the Frobenius norm of (A*B-I) + (B*A-I).
#
  import numpy as np

  error_frobenius = \
    np.linalg.norm ( np.matmul ( a, b ) - np.identity ( n ), 'fro' ) + \
    np.linalg.norm ( np.matmul ( b, a ) - np.identity ( n ), 'fro' )

  return error_frobenius

def l1dd ( n, h ):

#*****************************************************************************80
#
## l1dd() stores the 1D DD Laplacian as a full matrix.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with Dirichlet boundary conditions
#    at both ends of [0,6] has the matrix form L:
#
#       2 -1  0  0  0
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#       0  0  0 -1  2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), the Laplacian matrix.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'l1dd(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'l1dd(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  i = 0
  l[i,0] =  2.0 / h / h
  l[i,1] = -1.0 / h / h

  for i in range ( 1, n - 1 ):
    l[i,i-1] = -1.0 / h / h
    l[i,i] =    2.0 / h / h
    l[i,i+1] = -1.0 / h / h

  i = n - 1
  l[i,n-2] =   -1.0 / h / h
  l[i,n-1] =    2.0 / h / h

  return l

def l1dd_apply ( n, h, u ):

#*****************************************************************************80
#
## l1dd_apply() applies the 1D DD Laplacian to a vector.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with Dirichlet boundary conditions
#    at both ends of [0,6] is applied to a vector of 7 values, with a spacing
#    of H = 6/(N+1) = 1 at the points X:
#
#      0  1  2  3  4  5  6
#
#    and has the matrix form L:
#
#       2 -1  0  0  0
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#       0  0  0 -1  2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#    real U(N,1), the value at each point.
#
#  Output:
#
#    real LU(N), the Laplacian evaluated at each point.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1DD_APPLY(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1DD_APPLY(): Fatal error!' )

  lu = np.zeros ( n )

  i = 0
  lu[i] = ( 2.0 * u[i] - u[i+1] ) / h / h

  for i in range ( 1, n - 1 ):
    lu[i] = ( - u[i-1] + 2.0 * u[i] - u[i+1] ) / h / h

  i = n - 1
  lu[i] = ( - u[i-1] + 2.0 * u[i] ) / h / h

  return lu

def l1dd_cholesky ( n, h ):

#*****************************************************************************80
#
## l1dd_cholesky() computes the Cholesky factor of the 1D DD Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real C(N,N), the Cholesky factor.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1DD_CHOLESKY(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1DD_CHOLESKY(): Fatal error!' )

  c = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    c[i,i] = np.sqrt ( i + 2 ) / np.sqrt ( i + 1 )

  for i in range ( 0, n - 1 ):
    c[i,i+1] = - np.sqrt ( i + 1 ) / np.sqrt ( i + 2 )

  c = c / h

  return c

def l1dd_eigen ( n, h ):

#*****************************************************************************80
#
## l1dd_eigen() returns eigeninformation for the 1D DD Laplacian.
#
#  Discussion:
#
#    The grid points are assumed to be evenly spaced by H.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real V(N,N), the eigenvectors.
#
#    real LAMDA(N), the eigenvalues.
#
  import numpy as np

  lamda = np.zeros ( n )
  v = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    theta = 0.5 * np.pi * ( j + 1 ) / ( n + 1.0 )
    lamda[j] = 4.0 * ( np.sin ( theta ) / h ) ** 2
    for i in range ( 0, n ):
      theta = np.pi * ( i + 1 ) * ( j + 1 ) / ( n + 1.0 )
      v[i,j] = np.sqrt ( 2.0 / ( n + 1.0 ) ) * np.sin ( theta )

  return v, lamda

def l1dd_inverse ( n, h ):

#*****************************************************************************80
#
## l1dd_inverse() stores the inverse of the 1D DD Laplacian.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with Dirichlet boundary conditions
#    at both ends of [0,6] has the matrix form L:
#
#       2 -1  0  0  0
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#       0  0  0 -1  2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), the inverse of the Laplacian matrix.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1DD_INVERSE(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1DD_INVERSE(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      l[i,j] = min ( i + 1, j + 1 ) * ( n - max ( i, j ) ) * h * h / ( n + 1 )

  return l

def l1dd_lu ( n, h ):

#*****************************************************************************80
#
## l1dd_lu() computes the LU factors of the 1D DD Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), U(N,n), the LU factors.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1DD_LU(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1DD_LU(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    l[i,i] = 1.0

  for i in range ( 1, n ):
    l[i,i-1] = - i / ( i + 1 )

  u = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    u[i,i] = ( i + 2 ) / ( i + 1 )

  for i in range ( 0, n - 1 ):
    u[i,i+1] = - 1.0

  u = u / h / h

  return l, u

def l1dn ( n, h ):

#*****************************************************************************80
#
## l1dn() stores the 1D DN Laplacian as a full matrix.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with left Dirichlet and right
#    Neumann condition on [0,6] has the matrix form L:
#
#       2 -1  0  0  0
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#       0  0  0 -1  1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), the Laplacian matrix.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1DN(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1DN(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  i = 0
  l[i,0] =  2.0 / h / h
  l[i,1] = -1.0 / h / h

  for i in range ( 1, n - 1 ):
    l[i,i-1] = -1.0 / h / h
    l[i,i] =    2.0 / h / h
    l[i,i+1] = -1.0 / h / h

  i = n - 1
  l[i,n-2] = -1.0 / h / h
  l[i,n-1] =  1.0 / h / h

  return l

def l1dn_apply ( n, h, u ):

#*****************************************************************************80
#
## l1dn_apply() applies the 1D DN Laplacian to a vector.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with left Dirichlet and right
#    Neumann condition on [0,6] has the matrix form L:
#
#       2 -1  0  0  0
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#       0  0  0 -1  1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 October 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#    real U(N), the value at each point.
#
#  Output:
#
#    real LU(N), the Laplacian evaluated at each point.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1DN_APPLY(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1DN_APPLY(): Fatal error!' )

  lu = np.zeros ( n )

  i = 0
  lu[i] = ( 2.0 * u[i] - u[i+1] ) / h / h

  for i in range ( 1, n - 1 ):
    lu[i] = ( - u[i-1] + 2.0 * u[i] - u[i+1] ) / h / h

  i = n - 1
  lu[i] = ( - u[i-1] + u[i] ) / h / h

  return lu

def l1dn_cholesky ( n, h ):

#*****************************************************************************80
#
## l1dn_cholesky() computes the Cholesky factor of the 1D DN Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real C(N,N), the Cholesky factor.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1DN_CHOLESKY(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1DN_CHOLESKY(): Fatal error!' )

  c = np.zeros ( [ n, n ] )

  for i in range ( 0, n - 1 ):
    c[i,i]   =   np.sqrt ( i + 2 ) / np.sqrt ( i + 1 )
    c[i,i+1] = - np.sqrt ( i + 1 ) / np.sqrt ( i + 2 )

  i = n - 1
  c[i,i] = 1.0 / np.sqrt ( n )

  c = c / h

  return c

def l1dn_eigen ( n, h ):

#*****************************************************************************80
#
## l1dn_eigen() returns eigeninformation for the 1D DN Laplacian.
#
#  Discussion:
#
#    The grid points are assumed to be evenly spaced by H.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 Januaryu 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real V(N,N), the eigenvectors.
#
#    real LAMDA(N), the eigenvalues.
#
  import numpy as np

  v = np.zeros ( [ n, n ] )
  lamda = np.zeros ( n )

  for j in range ( 2, n ):
    theta = np.pi * ( j + 0.5 ) / ( 2.0 * n + 1.0 )
    lamda[j] = ( 2.0 * np.sin ( theta ) / h ) ** 2
    for i in range ( 0, n ):
      theta = np.pi * ( i + 1 ) * ( 2.0 * j + 1.0 ) / ( 2.0 * n + 1.0 )
      v[i,j] = np.sqrt ( 2.0 / ( n + 0.5 ) ) * np.sin ( theta )

  return v, lamda

def l1dn_inverse ( n, h ):

#*****************************************************************************80
#
## l1dn_inverse() stores the inverse of the 1D DN Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), the inverse of the Laplacian matrix.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1DN_INVERSE(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1DN_INVERSE(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      l[i,j] = min ( i + 1, j + 1 ) * h * h

  return l

def l1dn_lu ( n, h ):

#*****************************************************************************80
#
## l1dn_lu() computes the LU factors of the 1D DN Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), U(N,n), the LU factors.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1DN_LU(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1DN_LU(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    l[i,i] = 1.0

  for i in range ( 1, n ):
    l[i,i-1] = - i / ( i + 1 )

  u = np.zeros ( [ n, n ] )

  for i in range ( 0, n - 1 ):
    u[i,i] = ( i + 2 ) / ( i + 1 )

  i = n - 1
  u[i,i] = 1.0 / ( i + 1 )

  for i in range ( 0, n - 1 ):
    u[i,i+1] = - 1.0

  u = u / h / h

  return l, u

def l1nd ( n, h ):

#*****************************************************************************80
#
## l1nd() stores the 1D ND Laplacian as a full matrix.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with left Neumann and right Dirichlet
#    boundary conditions on [0,6] has the matrix form L:
#
#       1 -1  0  0  0
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#       0  0  0 -1  2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), the Laplacian matrix.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1ND(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1ND(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  i = 0
  l[i,0] =  1.0 / h / h
  l[i,1] = -1.0 / h / h

  for i in range ( 1, n - 1 ):
    l[i,i-1] = -1.0 / h / h
    l[i,i] =    2.0 / h / h
    l[i,i+1] = -1.0 / h / h

  i = n - 1
  l[i,n-2] = -1.0 / h / h
  l[i,n-1] =  2.0 / h / h

  return l

def l1nd_apply ( n, h, u ):

#*****************************************************************************80
#
## l1nd_apply() applies the 1D ND Laplacian to a vector.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with left Neumann and right Dirichlet
#    boundary conditions on [0,6] has the matrix form L:
#
#       1 -1  0  0  0
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#       0  0  0 -1  2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#    real U(N), the value at each point.
#
#  Output:
#
#    real LU(N), the Laplacian evaluated at each point.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1ND_APPLY(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1ND_APPLY(): Fatal error!' )

  lu = np.zeros ( n )

  i = 0
  lu[i] = ( u[i] - u[i+1] ) / h / h

  for i in range ( 1, n - 1 ):
    lu[i] = ( - u[i-1] + 2.0 * u[i] - u[i+1] ) / h / h

  i = n - 1
  lu[i] = ( - u[i-1] + 2.0 * u[i] ) / h / h

  return lu

def l1nd_cholesky ( n, h ):

#*****************************************************************************80
#
## l1nd_cholesky() computes the Cholesky factor of the 1D ND Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real C(N,N), the Cholesky factor.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1ND_CHOLESKY(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1ND_CHOLESKY(): Fatal error!' )

  c = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    c[i,i] = 1.0

  for i in range ( 0, n - 1 ):
    c[i,i+1] = - 1.0

  c = c / h

  return c

def l1nd_eigen ( n, h ):

#*****************************************************************************80
#
## l1nd_eigen() returns eigeninformation for the 1D ND Laplacian.
#
#  Discussion:
#
#    The grid points are assumed to be evenly spaced by H.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real V(N,N), the eigenvectors.
#
#    real LAMDA(N), the eigenvalues.
#
  import numpy as np

  v = np.zeros ( [ n, n ] )
  lamda = np.zeros ( n )

  for j in range ( 0, n ):
    theta = np.pi * ( j + 0.5 ) / ( 2.0 * n + 1.0 )
    lamda[j] = 4.0 * ( np.sin ( theta ) / h ) ** 2
    for i in range ( 0, n ):
      theta = np.pi * ( i + 0.5 ) * ( 2.0 * j + 1.0 ) / ( 2.0 * n + 1.0 )
      v[i,j] = np.sqrt ( 2.0 / ( n + 0.5 ) ) * np.cos ( theta )

  return v, lamda

def l1nd_inverse ( n, h ):

#*****************************************************************************80
#
## l1nd_inverse() stores the inverse of the 1D ND Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), the inverse of the Laplacian matrix.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1ND_INVERSE(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1ND_INVERSE(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      l[i,j] = ( n - max ( i, j ) ) * h * h

  return l

def l1nd_lu ( n, h ):

#*****************************************************************************80
#
## l1nd_lu() computes the LU factors of the 1D ND Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), U(N,n), the LU factors.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1ND_LU(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1ND_LU(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    l[i,i] = 1.0

  for i in range ( 1, n ):
    l[i,i-1] = - 1.0

  u = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    u[i,i] = 1.0

  for i in range ( 0, n - 1 ):
    u[i,i+1] = - 1.0

  u = u / h / h

  return l, u

def l1nn ( n, h ):

#*****************************************************************************80
#
## l1nn() computes the 1D NN Laplacian as a full matrix.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with Neumann boundary conditions
#    at both ends of [0,6] has the matrix form L:
#
#       1 -1  0  0  0
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#       0  0  0 -1  1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), the Laplacian matrix.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1NN(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1NN(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  i = 0
  l[i,0] =  1.0 / h / h
  l[i,1] = -1.0 / h / h

  for i in range ( 1, n - 1 ):
    l[i,i-1] = -1.0 / h / h
    l[i,i] =    2.0 / h / h
    l[i,i+1] = -1.0 / h / h

  i = n - 1
  l[i,n-2] = -1.0 / h / h
  l[i,n-1] =  1.0 / h / h

  return l

def l1nn_apply ( n, h, u ):

#*****************************************************************************80
#
## l1nn_apply() applies the 1D NN Laplacian to a vector.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with left Neumann and right Neumann
#    boundary conditions on [0,6] has the matrix form L:
#
#       1 -1  0  0  0
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#       0  0  0 -1  1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#    real U(N), the value at each point.
#
#  Output:
#
#    real LU(N), the Laplacian evaluated at each point.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1NN_APPLY(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1NN_APPLY(): Fatal error!' )

  lu = np.zeros ( n )

  i = 0
  lu[i] = ( u[i] - u[i+1] ) / h / h

  for i in range ( 1, n - 1 ):
    lu[i] = ( - u[i-1] + 2.0 * u[i] - u[i+1] ) / h / h

  i = n - 1
  lu[i] = ( - u[i-1] +  u[i] ) / h / h

  return lu

def l1nn_cholesky ( n, h ):

#*****************************************************************************80
#
## l1nn_cholesky() computes the Cholesky factor of the 1D NN Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real C(N,N), the Cholesky factor.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1NN_CHOLESKY(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1NN_CHOLESKY(): Fatal error!' )

  c = np.zeros ( [ n, n ] )

  for i in range ( 0, n - 1 ):
    c[i,i]   = + 1.0
    c[i,i+1] = - 1.0

  c = c / h

  return c

def l1nn_eigen ( n, h ):

#*****************************************************************************80
#
## l1nn_eigen() returns eigeninformation for the 1D NN Laplacian.
#
#  Discussion:
#
#    The grid points are assumed to be evenly spaced by H.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real V(N,N), the eigenvectors.
#
#    real LAMDA(N), the eigenvalues.
#
  import numpy as np

  v = np.zeros ( [ n, n ] )
  lamda = np.zeros ( n )

  for j in range ( 0, n ):
    theta = np.pi * j / ( 2.0 * n )
    lamda[j] = 4.0 * ( np.sin ( theta ) / h ) ** 2
    if ( j == 0 ):
      for i in range ( 0, n ):
        v[i,j] = np.sqrt ( n )
    else:
      for i in range ( 0, n ):
        theta = np.pi * ( i + 0.5 ) * j / n
        v[i,j] = np.sqrt ( 2.0 / n ) * np.cos ( theta )

  return v, lamda

def l1nn_lu ( n, h ):

#*****************************************************************************80
#
## l1nn_lu() computes the LU factors of the 1D NN Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), U(N,n), the LU factors.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1NN_LU(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1NN_LU(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    l[i,i] = 1.0

  for i in range ( 1, n ):
    l[i,i-1] = - 1.0

  u = np.zeros ( [ n, n ] )

  for i in range ( 0, n - 1 ):
    u[i,i] = 1.0

  i = n - 1
  u[i,i] = 0.0

  for i in range ( 0, n - 1 ):
    u[i,i+1] = - 1.0

  u = u / h / h

  return l, u

def l1pp ( n, h ):

#*****************************************************************************80
#
## l1pp() stores the 1D PP Laplacian as a full matrix.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with periodic boundary conditions
#    has the matrix form L:
#
#       2 -1  0  0 -1
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#      -1  0  0 -1  2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), the Laplacian matrix.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1PP(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1PP(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  i = 0
  l[i,0]   =  2.0 / h / h
  l[i,1]   = -1.0 / h / h
  l[i,n-1] = -1.0 / h / h

  for i in range ( 1, n - 1 ):
    l[i,i-1] = -1.0 / h / h
    l[i,i] =    2.0 / h / h
    l[i,i+1] = -1.0 / h / h

  i = n - 1
  l[i,0] =   -1.0 / h / h
  l[i,n-2] = -1.0 / h / h
  l[i,n-1] =  2.0 / h / h

  return l

def l1pp_apply ( n, h, u ):

#*****************************************************************************80
#
## l1pp_apply() applies the 1D PP Laplacian to a vector.
#
#  Discussion:
#
#    The N grid points are assumed to be evenly spaced by H.
#
#    For N = 5, the discrete Laplacian with periodic boundary conditions
#    on [0,6] has the matrix form L:
#
#       2 -1  0  0 -1
#      -1  2 -1  0  0
#       0 -1  2 -1  0
#       0  0 -1  2 -1
#      -1  0  0 -1  2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#    real U(N), the value at each point.
#
#  Output:
#
#    real LU(N), the Laplacian evaluated at each point.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1PP_APPLY(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1PP_APPLY(): Fatal error!' )

  lu = np.zeros ( n )

  i = 0
  lu[i] = ( - u[n-1] + 2.0 * u[i] - u[i+1] ) / h / h

  for i in range ( 1, n - 1 ):
    lu[i] = ( - u[i-1] + 2.0 * u[i] - u[i+1] ) / h / h

  i = n - 1
  lu[i] = ( - u[i-1] + 2.0 * u[i] - u[0] ) / h / h

  return lu

def l1pp_cholesky ( n, h ):

#*****************************************************************************80
#
## l1pp_cholesky() computes the Cholesky factor of the 1D PP Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real C(N,N), the Cholesky factor.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1PP_CHOLESKY(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1PP_CHOLESKY(): Fatal error!' )

  c = np.zeros ( [ n, n ] )

  for i in range ( 0, n - 1 ):
    c[i,i] = np.sqrt ( i + 2.0 ) / np.sqrt ( i + 1 )

  for i in range ( 0, n - 2 ):
    c[i,i+1] = - ( i + 1 ) / ( i + 2.0 ) * np.sqrt ( i + 2.0 ) / np.sqrt ( i + 1 )

  for i in range ( 0, n - 2 ):
    c[i,n-1] = - 1.0 / ( i + 2.0 ) * np.sqrt ( i + 2.0 ) / np.sqrt ( i + 1 )

  i = n - 2
  c[i,n-1] = - n / ( i + 2.0 ) * np.sqrt ( i + 2.0 ) / np.sqrt ( i + 1 )

  c = c / h

  return c

def l1pp_eigen ( n, h ):

#*****************************************************************************80
#
## l1pp_eigen() returns eigeninformation for the 1D PP Laplacian.
#
#  Discussion:
#
#    The grid points are assumed to be evenly spaced by H.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real V(N,N), the eigenvectors.
#
#    real LAMDA(N), the eigenvalues.
#
  import numpy as np

  v = np.zeros ( [ n, n ] )
  lamda = np.zeros ( n )

  for j in range ( 0, n ):

    if ( ( j % 2 ) == 0 ):
      theta = np.pi * j         / ( 2.0 * n )
    else:
      theta = np.pi * ( j + 1 ) / ( 2.0 * n )
  
    lamda[j] = 4.0 * ( np.sin ( theta ) / h ) ** 2

    if ( ( j % 2 ) == 0 ):
      if ( j == 0 ):
        for i in range ( 0, n ):
          v[i,j] = 1.0 / np.sqrt ( n )
      else:
        for i in range ( 0, n ):
          theta = np.pi * ( i + 0.5 ) * j /  n
          v[i,j] = np.sqrt ( 2.0 / n ) * np.cos ( theta )
    else:
      if ( j == n - 1 ):
        s = - 1.0 / np.sqrt ( n )
        for i in range ( 0, n ):
          v[i,j] = s
          s = - s
      else:
        for i in range ( 0, n ):
          theta = np.pi * ( i + 0.5 ) * ( j + 1 ) / n
          v[i,j] = np.sqrt ( 2.0 / n ) * np.sin ( theta )

  return v, lamda

def l1pp_lu ( n, h ):

#*****************************************************************************80
#
## l1pp_lu() computes the LU factors of the 1D PP Laplacian.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    N must be at least 3.
#
#    real H, the spacing between points.
#
#  Output:
#
#    real L(N,N), U(N,n), the LU factors.
#
  import numpy as np

  if ( n < 3 ):
    print ( '' )
    print ( 'L1PP_LU(): Fatal error!' )
    print ( '  N < 3.' )
    raise Exception ( 'L1PP_LU(): Fatal error!' )

  l = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    l[i,i] = 1.0

  for i in range ( 1, n - 1 ):
    l[i,i-1] =   - i / ( i + 1 )
    l[n-1,i-1] = - 1 / ( i + 1 )

  l[n-1,n-2] = - 1.0

  u = np.zeros ( [ n, n ] )

  for i in range ( 0, n - 2 ):
    u[i,i]   = ( i + 2 ) / ( i + 1 )
    u[i,i+1] = - 1
    u[i,n-1] = - 1       / ( i + 1 )

  i = n - 2
  u[i,i]   =   ( i + 2 ) / ( i + 1 )
  u[i,i+1] = - ( i + 2 ) / ( i + 1 )

  i = n - 1
  u[i,i] = 0.0

  u = u / h / h

  return l, u

def lu_error ( n, a, l, u ):

#*****************************************************************************80
#
## lu_error() determines the error in an LU factorization.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 January 2026
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
#    real L(N,N), U(N,N), the LU factors.
#
#  Output:
#
#    real ERROR_FROBENIUS, the Frobenius norm
#    of the difference matrix A - L * U.
#
  import numpy as np

  error_frobenius = np.linalg.norm ( a - np.matmul ( l, u ), 'fro' )

  return error_frobenius

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
  laplacian_matrix_test ( )
  timestamp ( )

