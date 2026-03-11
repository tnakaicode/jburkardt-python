#! /usr/bin/env python3
#
def linalg_solve_bench ( n ):

#*****************************************************************************80
#
## linalg_solve_bench() uses scipy.linalg.solve() for the LINPACK benchmark.
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
#    This version by John Burkardt.
#
#  Input:
#
#    integer N, the order of the matrix.
#
  from numpy.random import default_rng
  from scipy.linalg import solve
  from time import perf_counter
  import numpy as np
  import platform

  rng = default_rng ( )


  print ( '' )
  print ( 'linalg_solve_bench():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test scipy.linalg.solve() on the LINPACK benchmark.' )
  print ( '  Datatype: float64' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix A, a solution x, and a right hand side.
#
  A = 2.0 * np.random.random ( [ n, n ] ) - 1.0
  x_exact = np.ones ( n )
  b = np.matmul ( A, x_exact )
#
#  Solve the system.
#
  t = perf_counter ( )
  x = solve ( A, b )
  t = perf_counter ( ) - t
#
#  How well does x satisfy the equation?
#
  r = np.matmul ( A, x ) - b
#
#  Take infinity norms.
#
  a_norm = np.linalg.norm ( A, np.inf )
  r_norm = np.linalg.norm ( r, np.inf )
  x_norm = np.linalg.norm ( x, np.inf )
#
#  Report.
#
  eps = np.finfo(float).eps
  ratio = r_norm / ( a_norm * x_norm * eps )

  ops = ( 2 * n * n * n ) / 3.0 + 2.0 * n * n
  mflops = ops / ( 1000000 * t )
  unit = 2.0 / mflops

  cray = 0.056
  cray_ratio = t / cray

  print ( '' )
  print ( '  Normalized residual = ', ratio )
  print ( '  Residual norm       = ', r_norm )
  print ( '  Machine epsilon     = ', eps )
  print ( '  First X[]           = ', x[0] )
  print ( '  Last X[]            = ', x[-1] )
  print ( '  Time in seconds     = ', t )
  print ( '  MegaFLOPS           = ', mflops )
  print ( '  Unit                = ', unit )
  print ( '  Cray ratio          = ', cray_ratio )
#
#  Terminate.
#
  print ( '' )
  print ( 'linalg_solve_bench():' )
  print ( '  Normal end of execution.' )

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
  linalg_solve_bench ( n )
  timestamp ( )
