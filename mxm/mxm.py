#! /usr/bin/env python3
#
def mxm_test ( ):

#*****************************************************************************80
#
## mxm_test() tests mxm().
#
#  Discussion:
#
#    While other versions of this example run in a reasonable time using
#    n1 = n2 = n3 = 1000, the Python version seems to bog down with either
#    memory or speed issues.  So we cut it down to a smaller size instead.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'mxm_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test mxm().' )

  n1 = 300
  n2 = 300
  n3 = 300
  mxm ( n1, n2, n3 )
#
#  Terminate.
#
  print ( '' )
  print ( 'mxm_test():' )
  print ( '  Normal end of execution.' )

  return

def mxm ( n1, n2, n3 ):

#*****************************************************************************80
#
## mxm() computes a matrix-matrix product reports the elapsed CPU time.
#
#  Discussion:
#
#    The multiplication carried out is
#
#      A(1:N1,1:N3) = B(1:N1,1:N2) * C(1:N2,1:N3)
#
#    where B and C are real matrices whose entries
#    are assigned randomly.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, defines the number of
#    rows and columns in the two matrices.
#
  print ( ''  )
  print ( 'mxm():' )
  print ( '  Compute matrix-matrix product A = B * C' )
#
#  Record the amount of work.
#  Each of the N1 * N3 entries of A requires N2 multiplies and N2 adds.
#
  flop_count = 2 * n1 * n2 * n3

  print ( '' )
  print ( '  Matrix B is ', n1, ' by ', n2 )
  print ( '  Matrix C is ', n2, ' by ', n3 )
  print ( '  Matrix A is ', n1, ' by ', n3 )
  print ( '' )
  print ( '  Number of floating point operations = ', flop_count )
  time_estimate = flop_count / 2.6E+09
  print ( '  Estimated CPU time is ', time_estimate, ' seconds' )
#
#  Set B and C.
#
  key = 1325
  b, key = matgen ( n1, n2, key )
  c, key = matgen ( n2, n3, key )
  print ( '' )
  print ( '  Method     Cpu Seconds       MegaFlopS' )
  print ( '  ------  --------------  --------------' )
#
#  IJK
#
  cpu_seconds, a = mxm_ijk ( n1, n2, n3, b, c )

  if ( 0.0 < cpu_seconds ):
    mflops = flop_count / cpu_seconds / 1000000.0
  else:
    mflops = -1.0

  print ( '  IJK     %14f  %14f' % ( cpu_seconds, mflops ) )
#
#  IKJ
#
  cpu_seconds, a = mxm_ikj ( n1, n2, n3, b, c )

  if ( 0.0 < cpu_seconds ):
    mflops = flop_count / cpu_seconds / 1000000.0
  else:
    mflops = -1.0

  print ( '  IKJ     %14f  %14f' % ( cpu_seconds, mflops ) )
#
#  JIK
#
  cpu_seconds, a = mxm_jik ( n1, n2, n3, b, c )

  if ( 0.0 < cpu_seconds ):
    mflops = flop_count / cpu_seconds / 1000000.0
  else:
    mflops = -1.0

  print ( '  JIK     %14f  %14f' % ( cpu_seconds, mflops ) )
#
#  JKI
#
  cpu_seconds, a = mxm_jki ( n1, n2, n3, b, c )

  if ( 0.0 < cpu_seconds ):
    mflops = flop_count / cpu_seconds / 1000000.0
  else:
    mflops = -1.0

  print ( '  JKI     %14f  %14f' % ( cpu_seconds, mflops ) )
#
#  KIJ
#
  cpu_seconds, a = mxm_kij ( n1, n2, n3, b, c )

  if ( 0.0 < cpu_seconds ):
    mflops = flop_count / cpu_seconds / 1000000.0
  else:
    mflops = -1.0

  print ( '  KIJ     %14f  %14f' % ( cpu_seconds, mflops ) )
#
#  KJI
#
  cpu_seconds, a = mxm_kji ( n1, n2, n3, b, c )

  if ( 0.0 < cpu_seconds ):
    mflops = flop_count / cpu_seconds / 1000000.0
  else:
    mflops = -1.0

  print ( '  KJI     %14f  %14f' % ( cpu_seconds, mflops ) )
#
#  matmul
#
  cpu_seconds, a = mxm_matmul ( n1, n2, n3, b, c )

  if ( 0.0 < cpu_seconds ):
    mflops = flop_count / cpu_seconds / 1000000.0
  else:
    mflops = -1.0

  print ( '  matmul()%14f  %14f' % ( cpu_seconds, mflops ) )

  return

def matgen ( m, n, key ):

#*****************************************************************************80
#
## matgen() generates a random matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns
#    of the matrix.
#
#    integer key, a key for the random number generator.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )
#
#  Set the matrix A.
#
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      key = ( ( 3125 * key ) % 65536 )
      a[i,j] = ( key - 32768.0 ) / 16384.0

  return a, key

def mxm_ijk ( n1, n2, n3, b, c ):

#*****************************************************************************80
#
## mxm_ijk() computes A = B * C using DO I, DO J, DO K loops.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, define the orders of the
#    matrices.
#
#    real B(N1,N2), C(N2,N3), the factor matrices.
#
#  Output:
#
#    real CPU_SECONDS, the elapsed CPU time.
#
#    real A(N1,N3), the result matrix.
#
  from time import perf_counter
  import numpy as np

  a = np.zeros ( [ n1, n3 ] )

  cpu_seconds = perf_counter ( )

  for i in range ( 0, n1 ):
    for j in range ( 0, n3 ):
      for k in range ( 0, n2 ):
        a[i,j] = a[i,j] + b[i,k] * c[k,j]

  cpu_seconds = perf_counter ( ) - cpu_seconds

  return cpu_seconds, a

def mxm_ikj ( n1, n2, n3, b, c ):

#*****************************************************************************80
#
## mxm_ikj() computes A = B * C using DO I, DO K, DO J loops.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, define the orders of the matrices.
#
#    real B(N1,N2), C(N2,N3), the factor matrices.
#
#  Output:
#
#    real CPU_SECONDS, the elapsed CPU time.
#
#    real A(N1,N3), the result matrix.
#
  from time import perf_counter
  import numpy as np

  a = np.zeros ( [ n1, n3 ] )

  cpu_seconds = perf_counter ( )

  for i in range ( 0, n1 ):
    for k in range ( 0, n2 ):
      for j in range ( 0, n3 ):
        a[i,j] = a[i,j] + b[i,k] * c[k,j]

  cpu_seconds = perf_counter ( ) - cpu_seconds

  return cpu_seconds, a

def mxm_jik ( n1, n2, n3, b, c ):

#*****************************************************************************80
#
## mxm_jik() computes A = B * C using DO J, DO I, DO K loops.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, define the orders of the matrices.
#
#    real B(N1,N2), C(N2,N3), the factor matrices.
#
#  Output:
#
#    real CPU_SECONDS, the elapsed CPU time.
#
#    real A(N1,N3), the result matrix.
#
  from time import perf_counter
  import numpy as np

  a = np.zeros ( [ n1, n3 ] )

  cpu_seconds = perf_counter ( )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        a[i,j] = a[i,j] + b[i,k] * c[k,j]

  cpu_seconds = perf_counter ( ) - cpu_seconds

  return cpu_seconds, a

def mxm_jki ( n1, n2, n3, b, c ):

#*****************************************************************************80
#
## mxm_jki() computes A = B * C using DO J, DO K, DO I loops.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, define the orders of the
#    matrices.
#
#    real B(N1,N2), C(N2,N3), the factor matrices.
#
#  Output:
#
#    real CPU_SECONDS, the elapsed CPU time.
#
#    real A(N1,N3), the result matrix.
#
  from time import perf_counter
  import numpy as np

  a = np.zeros ( [ n1, n3 ] )

  cpu_seconds = perf_counter ( )

  for j in range ( 0, n3 ):
    for k in range ( 0, n2 ):
      for i in range ( 0, n1 ):
        a[i,j] = a[i,j] + b[i,k] * c[k,j]

  cpu_seconds = perf_counter ( ) - cpu_seconds

  return cpu_seconds, a

def mxm_kij ( n1, n2, n3, b, c ):

#*****************************************************************************80
#
## mxm_kij() computes A = B * C using DO K, DO I, DO J loops.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, define the orders of the matrices.
#
#    real B(N1,N2), C(N2,N3), the factor matrices.
#
#  Output:
#
#    real CPU_SECONDS, the elapsed CPU time.
#
#    real A(N1,N3), the result matrix.
#
  from time import perf_counter
  import numpy as np

  a = np.zeros ( [ n1, n3 ] )

  cpu_seconds = perf_counter ( )

  for k in range ( 0, n2 ):
    for i in range ( 0, n1 ):
      for j in range ( 0, n3 ):
        a[i,j] = a[i,j] + b[i,k] * c[k,j]

  cpu_seconds = perf_counter ( ) - cpu_seconds

  return cpu_seconds, a

def mxm_kji ( n1, n2, n3, b, c ):

#*****************************************************************************80
#
## mxm_kji() computes A = B * C using DO K, DO J, DO I loops.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, define the orders of the
#    matrices.
#
#    real B(N1,N2), C(N2,N3), the factor matrices.
#
#  Output:
#
#    real CPU_SECONDS, the elapsed CPU time.
#
#    real A(N1,N3), the result matrix.
#
  from time import perf_counter
  import numpy as np

  a = np.zeros ( [ n1, n3 ] )

  cpu_seconds = perf_counter ( )

  for k in range ( 0, n2 ):
    for j in range ( 0, n3 ):
      for i in range ( 0, n1 ):
        a[i,j] = a[i,j] + b[i,k] * c[k,j]

  cpu_seconds = perf_counter ( ) - cpu_seconds

  return cpu_seconds, a

  return

def mxm_matmul ( n1, n2, n3, b, c ):

#*****************************************************************************80
#
## mxm_matmul() computes A = B * C using the numpy matmul() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, N3, define the orders of the
#    matrices.
#
#    real B(N1,N2), C(N2,N3), the factor matrices.
#
#  Output:
#
#    real CPU_SECONDS, the elapsed CPU time.
#
#    real A(N1,N3), the result matrix.
#
  from time import perf_counter
  import numpy as np

  cpu_seconds = perf_counter ( )

  a = np.matmul ( b, c )

  cpu_seconds = perf_counter ( ) - cpu_seconds

  return cpu_seconds, a

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
  mxm_test ( )
  timestamp ( )

