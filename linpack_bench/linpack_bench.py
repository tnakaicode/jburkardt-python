#! /usr/bin/env python3
#
def linpack_bench ( n ):

#*****************************************************************************80
#
## linpack_bench() drives the LINPACK benchmark program.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2025
#
#  Author:
#
#    Original F77 version by Jack Dongarra, Jim Bunch, Cleve Moler, Pete Stewart.
#    This version by John Burkardt.
#
#  Input:
#
#    integer N, the order of the matrix.
#
  from time import perf_counter
  import numpy as np
  import platform

  print ( '' )
  print ( 'linpack_bench():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  The LINPACK benchmark.' )
  print ( '  Datatype: float64' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix A, a solution x, and a right hand side.
#
  A = 2.0 * np.random.random ( [ n, n ] ) - 1.0
  x_exact = np.ones ( n )
  b = np.matmul ( A, x_exact )
#
#  Factor the matrix.
#
  t = perf_counter ( )
  ALU, ipvt, info = dgefa ( A, n )
  t = perf_counter ( ) - t

  if ( info != 0 ):
    print ( '' )
    print ( 'linpack_bench(): Fatal error!' )
    print ( '  The matrix A is apparently singular.' )
    print ( '  Abnormal end of execution.' )
    raise Exception ( 'linpack_bench(): Fatal error!' )
#
#  Solve the linear system.
#
  t2 = perf_counter ( )
  x = dgesl ( ALU, n, ipvt, b )
  t2 = perf_counter ( ) - t2
  t = t + t2
#
#  Compute the residual.
#
  r = np.matmul ( A, x ) - b
#
#  Compute infinity norms.
#
  A_norm = np.linalg.norm ( A, np.inf )
  r_norm = np.linalg.norm ( r, np.inf )
  x_norm = np.linalg.norm ( x, np.inf )
#
#  Report.
#
  eps = np.finfo(float).eps
  ratio = r_norm / A_norm / x_norm / eps

  ops = ( 2 * n * n * n ) / 3.0 + 2.0 * ( n * n )
  mflops = ops / ( 1000000 * t )
  unit = 2.0 / mflops

  cray = 0.056
  cray_ratio = t / cray

  print ( "" )
  print ( "  Normalized residual = ", ratio )
  print ( "  Residual norm       = ", r_norm )
  print ( "  Machine epsilon     = ", eps )
  print ( "  First X[]           = ", x[0] )
  print ( "  Last X[]            = ", x[-1] )
  print ( "  Time in seconds     = ", t )
  print ( "  MegaFLOPS           = ", mflops )
  print ( "  Unit                = ", unit )
  print ( "  Cray ratio          = ", cray_ratio )
#
#  Terminate.
#
  print ( '' )
  print ( 'linpack_bench():' )
  print ( '  Normal end of execution.' )

  return

def dgefa ( A, n ):

#*****************************************************************************80
#
## dgefa() factors a real matrix in general storage format.
#
#  Discussion:
#
#    Gaussian elimination with partial pivoting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2024
#
#  Author:
#
#    Original F77 version by Jack Dongarra, Jim Bunch, Cleve Moler, Pete Stewart.
#    This version by John Burkardt
#
#  Reference:
#
#    Dongarra, Moler, Bunch and Stewart,
#    LINPACK User's Guide,
#    SIAM, (Society for Industrial and Applied Mathematics),
#    3600 University City Science Center,
#    Philadelphia, PA, 19104-2688.
#    ISBN 0-89871-172-X
#
#  Input:
#
#    real A(N,N), the matrix to be factored.
#
#    integer N, the order of the matrix A.
#
#  Output:
#
#    real ALU(N,N), an upper triangular matrix and the multipliers 
#    used to obtain it.  The factorization can be written A=L*U, where L is 
#    a product of permutation and unit lower triangular matrices, and U is 
#    upper triangular.
#
#    integer IPVT(N), the pivot indices.
#
#    integer INFO, singularity indicator.
#    0, normal value.
#    K, if U(K-1,K-1) == 0.  This is not an error condition for this subroutine,
#    but it does indicate that DGESL or DGEDI will divide by zero if called.
#    Use RCOND in DGECO for a reliable indication of singularity.
#
  import numpy as np

  ALU = A.copy ( )

  ipvt = np.zeros ( n, dtype = int )
  info = 0

  for k in range ( 0, n - 1 ):
#
#  Find L = pivot index,
#  K <= L < N,
#  index of largest entry in column K.
#
    l = -1
    amax = - np.inf
   
    for i in range ( k, n ):
      if ( amax < np.abs ( ALU[i,k] ) ):
        l = i
        amax = np.abs ( ALU[i,k] )

    ipvt[k] = l
#
#  Zero pivot implies this column already triangularized.
#
    if ( ALU[l,k] == 0.0 ):
      info = k + 1
      continue
#
#  Interchange row K and pivot row L if necessary.
#
    if ( l != k ):
      t        = ALU[l,k]
      ALU[l,k] = ALU[k,k]
      ALU[k,k] = t
#
#  Compute multipliers.
#
    ALU[k+1:n,k] = - ALU[k+1:n,k] / ALU[k,k]
#
#  Row elimination with column indexing.
#
    for j in range ( k + 1, n ):

      t = ALU[l,j]
      if ( l != k ):
        ALU[l,j] = ALU[k,j]
        ALU[k,j] = t

      ALU[k+1:n,j] = ALU[k+1:n,j] + t * ALU[k+1:n,k]

  ipvt[n-1] = n - 1

  if ( ALU[n-1,n-1] == 0.0 ):
    info = n

  return ALU, ipvt, info

def dgesl ( ALU, n, ipvt, b ):

#*****************************************************************************80
#
## dgesl() solves a real general linear system A * X = B.
#
#  Discussion:
#
#    The system matrix must have been factored by DGECO or DGEFA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2024
#
#  Author:
#
#    Original F77 version by Jack Dongarra, Jim Bunch, Cleve Moler, Pete Stewart.
#    This version by John Burkardt.
#
#  Reference:
#
#    Dongarra, Moler, Bunch and Stewart,
#    LINPACK User's Guide,
#    SIAM, (Society for Industrial and Applied Mathematics),
#    3600 University City Science Center,
#    Philadelphia, PA, 19104-2688.
#    ISBN 0-89871-172-X
#
#  Input:
#
#    real ALU(N,N), the LU factorization from DGECO or DGEFA.
#
#    integer N, the order of the matrix A.
#
#    integer IPVT(N), the pivot vector from DGECO or DGEFA.
#
#    real B(N), the right hand side vector.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = b.copy()

  for k in range ( 0, n - 1 ):

    l = ipvt[k]
    t = x[l]
    if ( l != k ):
      x[l] = x[k]
      x[k] = t

    x[k+1:n] = x[k+1:n] + t * ALU[k+1:n,k]

  for k in range ( n - 1, -1, -1 ):
    x[k] = x[k] / ALU[k,k]
    t = - x[k]
    x[0:k] = x[0:k] + t * ALU[0:k,k]

  return x

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
#    06 April 2013
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
  n = 1000
  linpack_bench ( n )
  timestamp ( )
