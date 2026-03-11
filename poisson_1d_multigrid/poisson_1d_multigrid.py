#! /usr/bin/env python3
#
def poisson_1d_multigrid_test ( ):

#*****************************************************************************80
#
## poisson_1d_multigrid_test() tests poisson_1d_multigrid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'poisson_1d_multigrid_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test poisson_1d_multigrid().' )

  poisson_1d_multigrid_test01_mono ( )
  poisson_1d_multigrid_test01_multi ( )
  poisson_1d_multigrid_test02_mono ( )
  poisson_1d_multigrid_test02_multi ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'poisson_1d_multigrid_test():' )
  print ( '  Normal end of execution.' )

  return

def ctof ( nc, uc, nf, uf ):

#*****************************************************************************80
#                                                    
## ctof() transfers data from a coarse to a finer grid.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Hager,
#    Applied Numerical Linear Algebra,
#    Prentice-Hall, 1988,
#    ISBN13: 978-0130412942,
#    LC: QA184.H33.
#
#  Input:
#
#    integer NC, the number of coarse nodes.
#
#    real UC(NC), the coarse correction data.
#
#    integer NF, the number of fine nodes.
#
#    real UF(NF), the fine grid data.
#
#  Output:
#
#    real UF(NF), the updated fine grid data.
# 
  uf[0:2*nc-1:2] = uf[0:2*nc-1:2] + uc[0:nc]
  uf[1:2*nc-2:2] = uf[1:2*nc-2:2] + 0.5 * ( uc[0:nc-1] + uc[1:nc] )

  return uf

def exact1 ( x ):

#*****************************************************************************80
#                                                    
## exact1() evaluates the exact solution for test case #1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Hager,
#    Applied Numerical Linear Algebra,
#    Prentice-Hall, 1988,
#    ISBN13: 978-0130412942,
#    LC: QA184.H33.
#
#  Input:
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the value of the exact solution at X.
#
  value = 0.5 * ( - x * x + x )

  return value

def exact2 ( x ):

#*****************************************************************************80
#                                                    
## exact2() evaluates the exact solution for test case #2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Hager,
#    Applied Numerical Linear Algebra,
#    Prentice-Hall, 1988,
#    ISBN13: 978-0130412942,
#    LC: QA184.H33.
#
#  Input:
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the value of the exact solution at X.
#
  import numpy as np

  value = x * ( x - 1.0 ) * np.exp ( x )

  return value

def force1 ( x ):

#*****************************************************************************80
#                                                    
## force1() evaluates the forcing function for test case #1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Hager,
#    Applied Numerical Linear Algebra,
#    Prentice-Hall, 1988,
#    ISBN13: 978-0130412942,
#    LC: QA184.H33.
#
#  Input:
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the value of the forcing function at X.
#
  value = 1.0

  return value

def force2 ( x ):

#*****************************************************************************80
#                                                    
## force2() evaluates the forcing function for test case #2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Hager,
#    Applied Numerical Linear Algebra,
#    Prentice-Hall, 1988,
#    ISBN13: 978-0130412942,
#    LC: QA184.H33.
#
#  Input:
#
#    real X, the evaluation point.
#
#  Output:
#
#    real FORCE2, the value of the forcing function at X.
#
  import numpy as np

  value = - x * ( x + 3.0 ) * np.exp ( x )

  return value

def ftoc ( nf, uf, rf, nc ):

#*****************************************************************************80
#                                                    
## ftoc() transfers data from a fine grid to a coarser grid.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Hager,
#    Applied Numerical Linear Algebra,
#    Prentice-Hall, 1988,
#    ISBN13: 978-0130412942,
#    LC: QA184.H33.
#
#  Input:
#
#    integer NF, the number of fine nodes.
#
#    real UF(NF), the fine data.
#
#    real RF(NF), the right hand side for the fine grid.
#
#    integer NC, the number of coarse nodes.
#
#  Output:
#
#    real UC[NC], the coarse grid data, set to zero.
#
#    real RC[NC], the right hand side for the coarse grid.
#
  import numpy as np

  uc = np.zeros ( nc )

  rc = np.zeros ( nc )

  rc[1:nc-1] = 4.0 * ( rf[2:2*nc-3:2] \
    + uf[1:2*nc-4:2] - 2.0 * uf[2:2*nc-3:2] + uf[3:2*nc-2:2] )

  return uc, rc

def gauss_seidel ( n, r, u ):

#*****************************************************************************80
#                                                    
## gauss_seidel() carries out one step of a Gauss-Seidel iteration.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Hager,
#    Applied Numerical Linear Algebra,
#    Prentice-Hall, 1988,
#    ISBN13: 978-0130412942,
#    LC: QA184.H33.
#
#  Input:
#
#    integer N, the number of unknowns.
#
#    real R(N), the right hand side.
#
#    real U(N), the estimated solution.
#
#  Output:
#
#    real U(N), the estimated solution.
#
#    real DIF_L1, the L1 norm of the difference between the
#    input and output solution estimates.
#
  import numpy as np

  u_old = u.copy()

  for i in range ( 1, n - 1 ):
    u[i] = 0.5 * ( u[i-1] + u_old[i+1] + r[i] )

  dif_l1 = np.sum ( np.abs ( u[1:n-1] - u_old[1:n-1] ) )

  return u, dif_l1

def i4_log_2 ( i ):

#*****************************************************************************80
#
## i4_log_2() returns the integer part of the logarithm base 2 of |I|.
#
#  Discussion:
#
#    For positive i4_log_2(I), it should be true that
#      2^i4_log_2(X) <= |I| < 2^(i4_log_2(I)+1).
#    The special case of i4_log_2(0) returns -HUGE().
#
#  Example:
#
#     I  Value
#
#     0  -1
#     1,  0
#     2,  1
#     3,  1
#     4,  2
#     5,  2
#     6,  2
#     7,  2
#     8,  3
#     9,  3
#    10,  3
#   127,  6
#   128,  7
#   129,  7
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose logarithm base 2 is desired.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm base 2 of
#    the absolute value of I.
#
  import numpy as np

  i = np.floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0

    i = abs ( i )

    while ( 2 <= i ):
      i = np.floor ( i / 2 )
      value = value + 1

  return value

def poisson_1d_monogrid ( n, a, b, ua, ub, force, exact ):

#*****************************************************************************80
#                                                    
## poisson_1d_monogrid() solves a 1D PDE, using the Gauss-Seidel method.
#
#  Discussion:
#
#    This routine solves a 1D boundary value problem of the form
#
#      - U''(X) = F(X) for A < X < B,
#
#    with boundary conditions U(A) = UA, U(B) = UB.
#
#    The Gauss-Seidel method is used. 
#
#    This routine is provided primarily for comparison with the
#    multigrid solver.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Hager,
#    Applied Numerical Linear Algebra,
#    Prentice-Hall, 1988,
#    ISBN13: 978-0130412942,
#    LC: QA184.H33.
#
#  Input:
#
#    integer N, the number of intervals.
#
#    real A, B, the left and right endpoints of the region.
#
#    real UA, UB, the left and right boundary values.
#
#    def FORCE ( x ), the function which evaluates the right hand side.
#
#    def EXACT ( x ), the function which evaluates the exact solution.
#
#  Output:
#
#    integer IT_NUM: the number of iterations.
#
#    real U[N+1]: the computed solution.
#
  import numpy as np
#
#  Initialization.
#
  tol = 0.0001
#
#  Set the nodes.
#
  x = np.linspace ( a, b, n + 1 )
#
#  Set the right hand side.
#
  r = np.zeros ( n + 1 )

  r[0] = ua
  r[1:n] = force ( x[1:n] ) / n / n
  r[n] = ub

  u = np.zeros ( n + 1 )

  it_num = 0
#
#  Gauss-Seidel iteration.
#
  while ( True ):

    it_num = it_num + 1

    u, d1 = gauss_seidel ( n + 1, r, u )

    if ( d1 <= tol ):
      break

  return u, it_num

def poisson_1d_multigrid ( n, a, b, ua, ub, force, exact ):

#*****************************************************************************80
#                                                    
## poisson_1d_multigrid() solves a 1D PDE using the multigrid method.
#
#  Discussion:
#
#    This routine solves a 1D boundary value problem of the form
#
#      - U''(X) = F(X) for A < X < B,
#
#    with boundary conditions U(A) = UA, U(B) = UB.
#
#    The multigrid method is used. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    Original FORTRAN77 version by William Hager.
#    This version by John Burkardt.
#
#  Reference:
#
#    William Hager,
#    Applied Numerical Linear Algebra,
#    Prentice-Hall, 1988,
#    ISBN13: 978-0130412942,
#    LC: QA184.H33.
#
#  Input:
#
#    integer N, the number of intervals.
#    N must be a power of 2.
#
#    real A, B, the left and right endpoints of the region.
#
#    real UA, UB, the left and right boundary values.
#
#    function value = FORCE ( x ), the name of the function 
#    which evaluates the right hand side.
#
#    function value = EXACT ( x ), the name of the function 
#    which evaluates the exact solution.
#
#  Output:
#
#    integer IT_NUM, the number of iterations.
#
#    real U(N+1), the computed solution.
#
  import numpy as np
#
#  Determine if we have enough storage.
#
  k = i4_log_2 ( n )

  if ( n != 2**k ):
    print ( '' )
    print ( 'poisson_1d_multigrid(): Fatal error!' )
    print ( '  N is not a power of 2.' )
    raise Exception ( 'poisson_1d_multigrid(): Fatal error!' )

  nl = n + n + k - 2

  uu = np.zeros ( nl )
  r = np.zeros ( nl )
#
#  Initialization.
#
  it = 4
  it_num = 0
  tol = 0.0001
  utol = 0.7
  m = n
# 
#  Set the nodes.
#
  x = ( np.linspace ( a, b, n + 1 ) )
#
#  Set the right hand side.
#
  r[0] = ua
  r[1:n] = force ( x[1:n] ) / n / n
  r[n] = ub
#
#  LN points to first entry of solution.
#  RN points to last entry.
#  NN counts the number of intervals (nodes - 1 ).
#
  ln = 0
  rn = n
  nn = n
# 
#  Gauss-Seidel iteration
#
  d1 = 0.0
  j = 0

  while ( True ):

    d0 = d1
    j = j + 1
    uu[ln:rn+1], d1 = gauss_seidel ( nn + 1, r[ln:rn+1], uu[ln:rn+1] )
    it_num = it_num + 1
#
#  Do at least 4 iterations at each level.
#
    if ( j < it ):

      continue
#
#  Enough iterations, satisfactory decrease, already on finest grid, exit.
#
    elif ( d1 < tol and nn == m ):

      break
#
#  Enough iterations, satisfactory convergence, go finer, start an iteration.
#
    elif ( d1 < tol ):

      nf = 2 * nn
      lf = ln - 2 * nn - 1
      rf = ln - 1

      uu[lf:rf+1] = ctof ( nn + 1, uu[ln:rn+1], nf + 1, uu[lf:rf+1] )

      nn = nf
      ln = lf
      rn = rf
      j = 0
#
#  Enough iterations, slow convergence, 2 < N, go coarser, start an iteration.
#
    elif ( utol * d0 <= d1 and 2 < n ):

      nc = nn // 2
      lc = rn + 1
      rc = rn + ( nn // 2 ) + 1

      uu[lc:rc+1], r[lc:rc+1] = ftoc ( nn + 1, uu[ln:rn+1], r[ln:rn+1], nc + 1 )

      nn = nc
      ln = lc
      rn = rc

      j = 0

  u = uu.copy()

  return u, it_num

def poisson_1d_multigrid_test01_mono ( ):

#*****************************************************************************80
#
## poisson_1d_multigrid_test01_mono() tests poisson_1d_monogrid() on test case #1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'poisson_1d_multigrid_test01_mono()' )
  print ( '  poisson_1d_monogrid() solves a 1D Poisson BVP' )
  print ( '  using the Gauss-Seidel method.' )

  a = 0.0
  b = 1.0
  ua = 0.0
  ub = 0.0

  print ( '' )
  print ( '  -u"(x) = 1, for ', a, ' < x < ', b )
  print ( '  u(', a, ') = ', ua, ' u(', b , ') = ', ub )
  print ( '  Solution is u(x) = ( -x^2 + x ) / 2' )

  for k in range ( 5, 6 ):

    n = 2**k

    x = np.linspace ( a, b, n + 1 )

    print ( '' )
    print ( '  Mesh index K = ', k )
    print ( '  Number of intervals N=2^K = ', n )
    print ( '  Number of nodes = 2^K+1 =   ', n + 1 )

    u, it_num = poisson_1d_monogrid ( n, a, b, ua, ub, force1, exact1 )

    print ( '' )
    print ( '     I        X(I)      U(I)         U Exact(X(I))' )
    print ( '' )
    for i in range ( 0, n + 1 ):
      print ( '  %4d  %10f  %14g  %14g' % ( i, x[i], u[i], exact1 ( x[i] ) ) )

    print ( '' )

    difmax = 0.0
    for i in range ( 0, n + 1 ):
      difmax = max ( difmax, np.abs ( u[i] - exact1 ( x[i] ) ) )

    print ( '  Maximum error = ', difmax )
    print ( '  Number of Gauss-Seidel iterations = ', it_num )

  return

def poisson_1d_multigrid_test01_multi ( ):

#*****************************************************************************80
#
## poisson_1d_multigrid_test01_multi() tests poisson_1d_multigrid() on test case #1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'poisson_1d_multigrid_test01_multi():' )
  print ( '  poisson_1d_multigrid() solves a 1D Poisson BVP' )
  print ( '  using the multigrid method.' )

  a = 0.0
  b = 1.0
  ua = 0.0
  ub = 0.0

  print ( '' )
  print ( '  -u"(x) = 1, for ', a, ' < x < ', b )
  print ( '  u(', a, ') = ', ua, ', u(', b, ') = ', ub )
  print ( '  Solution is u(x) = ( -x^2 + x ) / 2' )

  for k in range ( 5, 6 ):

    n = 2**k
    x = np.linspace ( a, b, n + 1 )

    print ( '' )
    print ( '  Mesh index K = ', k )
    print ( '  Number of intervals N=2^K = ', n )
    print ( '  Number of nodes = 2^K+1 =   ', n + 1 )

    u, it_num = poisson_1d_multigrid ( n, a, b, ua, ub, force1, exact1 )

    print ( '' )
    print ( '     I        X(I)      U(I)         U Exact(X(I))' )
    print ( '' )
    for i in range ( 0, n + 1 ):
      print ( '  %4d  %10f  %14g  %14g' % ( i, x[i], u[i], exact1 ( x[i] ) ) )

    print ( '' )

    difmax = 0.0
    for i in range ( 0, n + 1 ):
      difmax = max ( difmax, np.abs ( u[i] - exact1 ( x[i] ) ) )

    print ( '  Maximum error = ', difmax )
    print ( '  Number of iterations = ', it_num )

  return

def poisson_1d_multigrid_test02_mono ( ):

#*****************************************************************************80
#
## poisson_1d_multigrid_test02_mono() tests poisson_1d_monogrid() on test case 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'poisson_1d_multigrid_test02_mono():' )
  print ( '  poisson_1d_monogrid() solves a 1D Poisson BVP' )
  print ( '  using the Gauss-Seidel method.' )

  a = 0.0
  b = 1.0
  ua = 0.0
  ub = 0.0

  print ( '' )
  print ( '  -u"(x) = - x * (x+3) * exp(x), for ', a, ' < x < ', b )
  print ( '  u(', a, ') = ', ua, ', u(', b, ') = ', ub )
  print ( '  Solution is u(x) = x * (x-1) * exp(x)' )

  for k in range ( 5, 6 ):

    n = 2**k

    x = np.linspace ( a, b, n + 1 )

    print ( '' )
    print ( '  Mesh index K = ', k )
    print ( '  Number of intervals N=2^K = ', n )
    print ( '  Number of nodes = 2^K+1 =   ', n + 1 )

    u, it_num = poisson_1d_monogrid ( n, a, b, ua, ub, force2, exact2 )

    print ( '' )
    print ( '     I        X(I)      U(I)         U Exact(X(I))' )
    print ( '' )
    for i in range ( 0, n + 1 ):
      print ( '  %4d  %10f  %14g  %14g' % ( i, x[i], u[i], exact2 ( x[i] ) ) )

    print ( '' )

    difmax = 0.0
    for i in range ( 0, n + 1 ):
      difmax = max ( difmax, np.abs ( u[i] - exact2 ( x[i] ) ) )

    print ( '  Maximum error = ', difmax )
    print ( '  Number of Gauss-Seidel iterations = ', it_num )

  return

def poisson_1d_multigrid_test02_multi ( ):

#*****************************************************************************80
#
## poisson_1d_multigrid_test02_multi() tests poisson_1d_multigrid() on test case 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 November 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'poisson_1d_multigrid_test02_multi():' )
  print ( '  poisson_1d_multigrid() solves a 1D Poisson BVP' )
  print ( '  using the multigrid method.' )

  a = 0.0
  b = 1.0
  ua = 0.0
  ub = 0.0

  print ( '' )
  print ( '  -u"(x) = - x * (x+3) * exp(x), for ', a, ' < x < ', b )
  print ( '  u(', a, ') = ', ua, ', u(', b, ') = ', ub )
  print ( '  Solution is u(x) = x * (x-1) * exp(x)' )

  for k in range ( 5, 6 ):

    n = 2**k

    x = np.linspace ( a, b, n + 1 )

    print ( '' )
    print ( '  Mesh index K = ', k )
    print ( '  Number of intervals N=2^K = ', n )
    print ( '  Number of nodes = 2^K+1 =   ', n + 1 )

    u, it_num = poisson_1d_multigrid ( n, a, b, ua, ub, force2, exact2 )

    print ( '' )
    print ( '     I        X(I)      U(I)         U Exact(X(I))' )
    print ( '' )
    for i in range ( 0, n + 1 ):
      print ( '  %4d  %10f  %14g  %14g' % ( i, x[i], u[i], exact2 ( x[i] ) ) )

    print ( '' )

    difmax = 0.0
    for i in range ( 0, n + 1 ):
      difmax = max ( difmax, np.abs ( u[i] - exact2 ( x[i] ) ) )

    print ( '  Maximum error = ', difmax )
    print ( '  Number of iterations = ', it_num )

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
  poisson_1d_multigrid_test ( )
  timestamp ( )

