#! /usr/bin/env python3
#
def jacobi_poisson_1d_test ( ):

#*****************************************************************************80
#
## jacobi_poisson_1d_test() tests jacobi_poisson_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'jacobi_poisson_1d_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test jacobi_poisson_1d().' )

  k = 5
  jacobi_poisson_1d ( k )
#
#  Terminate.
#
  print ( '' )
  print ( 'jacobi_poisson_1d_test():' )
  print ( '  Normal end of execution.' )

  return

def jacobi_poisson_1d ( k ):

#*****************************************************************************80
#
## jacobi_poisson_1d() uses Jacobi iteration for the 1D Poisson equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 November 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer K, the grid index.
#    K specifies the number of nodes, by the formula NK = 2^K + 1.
#    K must be at least 0.
#
  import numpy as np

  print ( '' )
  print ( 'jacobi_poisson_1d():' )
  print ( '  Use Jacobi iteration for the 1D Poisson equation.' )
#
#  Set boundaries.
#
  a = 0.0
  b = 1.0
#
#  Set boundary conditions.
#
  ua = 0.0
  ub = 0.0
#
#  Get NK.
#
  nk = 2**k + 1
#
#  Set XK.
#
  xk = np.linspace ( a, b, nk )
#
#  Get HK.
#
  hk = ( b - a ) / ( nk - 1 )
#
#  Set FK.
#
  fk = force ( xk )
  fk[0] = ua
  fk[nk-1] = ub
#
#  Set the -1/2/-1 entries of Ak.
#
#  In order that the operator Ak approximation the Poisson operator,
#  and in order that we can compare linear systems for successive grids,
#  we should NOT multiply through by hk^2.
#
  Ak = np.zeros ( [ nk, nk ] )
  Ak[0,0] = 1.0
  for i in range ( 1, nk - 2 ):
    Ak[i,i+1] = -1.0 / hk**2
  for i in range ( 1, nk - 1 ):
    Ak[i,i] = 2.0 / hk**2
  for i in range ( 2, nk - 1 ):
    Ak[i,i-1] = -1.0 / hk**2
  Ak[nk-1,nk-1] = 1.0
#
#  Just because we can, ask MATLAB to get the exact solution of the linear system
#  directly.
#
  udk = np.linalg.solve ( Ak, fk )
#
#  Sample the solution to the continuous problem.
#
  uek = exact ( xk )
#
#  Use Jacobi iteration to solve the linear system to the given tolerance.
#
  ujk = np.zeros ( nk )
  it_max = 10000000
  res_max = 0.000001

  ujk, it_num, res_norm = jacobi ( nk, Ak, fk, ujk, it_max, res_max )
#
#  Examine errors:
#
  print ( '' )
  print ( '  Using grid index K = ', k )
  print ( '  System size NK was ', nk )
  print ( '  Tolerance for linear residual ', res_max )
  print ( '  RMS of linear residual ', res_norm )
  print ( '  Number of Jacobi iterations taken was ', it_num )
  print ( '  RMS Jacobi error in solution of linear system = ' \
    % ( np.linalg.norm ( udk - ujk ) / np.sqrt ( nk ) ) )
  print ( '  RMS discretization error in Poisson solution = ' \
    % ( np.linalg.norm ( uek - ujk ) / np.sqrt ( nk ) ) )

  print ( '' )
  print ( '     I        X        U_Exact    U_Direct    U_Jacobi' )
  print ( '' )
  for i in range ( 0, nk ):
    print ( '  %4d  %10.4f  %10.4g  %10.4g  %10.4g' \
      % ( i, xk[i], uek[i], udk[i], ujk[i] ) )

  return

def exact ( x ):

#*****************************************************************************80
#
## exact() evaluates the solution of the continuous problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the evaluation points.
#
#  Output:
#
#    real UEX(*), the solution of the continuous problem 
#    at the evaluation points.
#
  import numpy as np

  uex = x * ( x - 1.0 ) * np.exp ( x )

  return uex

def force ( x ):

#*****************************************************************************80
#
## force() evaluates the forcing term.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(*), the evaluation points.
#
#  Output:
#
#    real F(*), the forcing term at the evaluation points.
#
  import numpy as np

  f = - x * ( x + 3.0 ) * np.exp ( x )

  return f

def jacobi ( n, A, f, u, it_max, res_max ):

#*****************************************************************************80
#
## jacobi() carries out the Jacobi iteration.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2011
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N,N), the matrix.
#
#    real F(N), the right hand side.
#
#    real U(N), the estimated solution.
#
#    integer IT_MAX, the maximum number of iterations.
#
#    real RES_MAX, a convergence tolerance on the residual.
#
#  Output:
#
#    real U(N), the improved estimate of the solution.
#
#    integer IT_NUM, the number of iterations taken.
#
#    real RES_NORM, the RMS norm of the residual.
#
  import numpy as np

  print ( '' )
  print ( '    Step    Residual      Change' )
  print ( '' )

  it_num = it_max

  for it in range ( 1, it_max + 1 ):

    u_old = u.copy()
    u = ( f - np.matmul ( A, u_old ) + ( np.diag ( A ) * u_old ) ) / np.diag ( A )
    r = np.matmul ( A, u ) - f
    res_norm = np.linalg.norm ( r ) / np.sqrt ( n )

    print ( '  %6d  %10.4g  %10.4g' \
      % ( it, res_norm, np.linalg.norm ( u - u_old ) / np.sqrt ( n ) ) )

    if ( res_norm <= res_max ):
      it_num = it
      break

  return u, it_num, res_norm

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

if ( __name__ == "__main__" ):
  timestamp ( )
  jacobi_poisson_1d_test ( )
  timestamp ( )

