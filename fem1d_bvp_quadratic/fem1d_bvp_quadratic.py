#! /usr/bin/env python3
#
def fem1d_bvp_quadratic ( n, a, c, f, x ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC solves a two point boundary value problem.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic.py
#
#  Discussion:
#
#    The program uses the finite element method, with piecewise quadratic basis
#    functions to solve a boundary value problem in one dimension.
#
#    The problem is defined on the region 0 <= x <= 1.
#
#    The following differential equation is imposed between 0 and 1:
#
#      - d/dx a(x) du/dx + c(x) * u(x) = f(x)
#
#    where a(x), c(x), and f(x) are given functions.
#
#    At the boundaries, the following conditions are applied:
#
#      u(0.0) = 0.0
#      u(1.0) = 0.0
#
#    A set of N equally spaced nodes is defined on this
#    interval, with 0 = X(1) < X(2) < ... < X(N) = 1.0.
#
#    At each node I, we associate a piecewise quadratic basis function V(I,X),
#    which is 0 at all nodes except node I.
#
#    We now assume that the solution U(X) can be written as a quadratic
#    sum of these basis functions:
#
#      U(X) = sum ( 1 <= J <= N ) U(J) * V(J,X)
#
#    where U(X) on the left is the function of X, but on the right,
#    is meant to indicate the coefficients of the basis functions.
#
#    To determine the coefficient U(J), we multiply the original
#    differential equation by the basis function V(J,X), and use
#    integration by parts, to arrive at the I-th finite element equation:
#
#        Integral A(X) * U'(X) * V'(I,X) + C(X) * U(X) * V(I,X) dx 
#      = Integral F(X) * V(I,X) dx
#
#    By writing this equation for basis functions I = 2 through N - 1,
#    and using the boundary conditions, we have N linear equations
#    for the N unknown coefficients U(1) through U(N), which can
#    be easily solved.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of nodes.
#
#    Input, function A ( X ), evaluates a(x);
#
#    Input, function C ( X ), evaluates c(x);
#
#    Input, function F ( X ), evaluates f(x);
#
#    Input, real X(N), the mesh points.
#
#    Output, real U(N), the finite element coefficients, which are also
#    the value of the computed solution at the mesh points.
#
  import numpy as np
  import scipy.linalg as la
#
#  Define a 2 point Gauss-Legendre quadrature rule on [-1,+1].
#
  quad_num = 3
  abscissa = np.array ( [ \
    -0.774596669241483377035853079956, \
     0.000000000000000000000000000000, \
     0.774596669241483377035853079956 ] )
  weight = np.array ( [ \
    0.555555555555555555555555555556, \
    0.888888888888888888888888888889, \
    0.555555555555555555555555555556 ] )
#
#  Make room for the matrix A and right hand side b.
#
  A = np.zeros ( [ n, n ] )
  b = np.zeros ( n )
#
#  Integrate over element E.
#
  e_num = ( n - 1 ) // 2

  for e in range ( 0, e_num ):

    l = 2 * e
    xl = x[l]

    m = 2 * e + 1
    xm = x[m]

    r = 2 * e + 2
    xr = x[r]

    for q in range ( 0, quad_num ):

      xq = ( ( 1.0 - abscissa[q] ) * xl   \
           + ( 1.0 + abscissa[q] ) * xr ) \
           / 2.0

      wq = weight[q] * ( xr - xl ) / 2.0

      axq = a ( xq )
      cxq = c ( xq )
      fxq = f ( xq )

      vl = ( ( xq - xm ) / ( xl - xm ) ) \
         * ( ( xq - xr ) / ( xl - xr ) )

      vm = ( ( xq - xl ) / ( xm - xl ) ) \
         * ( ( xq - xr ) / ( xm - xr ) )

      vr = ( ( xq - xl ) / ( xr - xl ) ) \
         * ( ( xq - xm ) / ( xr - xm ) )

      vlp = (         1.0 / ( xl - xm ) ) \
          * ( ( xq - xr ) / ( xl - xr ) ) \
          + ( ( xq - xm ) / ( xl - xm ) ) \
          * (         1.0 / ( xl - xr ) )

      vmp = (         1.0 / ( xm - xl ) ) \
          * ( ( xq - xr ) / ( xm - xr ) ) \
          + ( ( xq - xl ) / ( xm - xl ) ) \
          * (         1.0 / ( xm - xr ) )

      vrp = (         1.0 / ( xr - xl ) ) \
          * ( ( xq - xm ) / ( xr - xm ) ) \
          + ( ( xq - xl ) / ( xr - xl ) ) \
          * (         1.0 / ( xr - xm ) )

      A[l,l] = A[l,l] + wq * ( vlp * axq * vlp + vl * cxq * vl )
      A[l,m] = A[l,m] + wq * ( vlp * axq * vmp + vl * cxq * vm )
      A[l,r] = A[l,r] + wq * ( vlp * axq * vrp + vl * cxq * vr )
      b[l]   = b[l]   + wq * ( vl * fxq )

      A[m,l] = A[m,l] + wq * ( vmp * axq * vlp + vm * cxq * vl )
      A[m,m] = A[m,m] + wq * ( vmp * axq * vmp + vm * cxq * vm )
      A[m,r] = A[m,r] + wq * ( vmp * axq * vrp + vm * cxq * vr )
      b[m] =   b[m]   + wq * ( vm * fxq )

      A[r,l] = A[r,l] + wq * ( vrp * axq * vlp + vr * cxq * vl )
      A[r,m] = A[r,m] + wq * ( vrp * axq * vmp + vr * cxq * vm )
      A[r,r] = A[r,r] + wq * ( vrp * axq * vrp + vr * cxq * vr )
      b[r] =   b[r]   + wq * ( vr * fxq )
#
#  Equation 0 is the left boundary condition, U(0) = 0.0;
#
  for j in range ( 0, n ):
    A[0,j] = 0.0
  A[0,0] = 1.0
  b[0] = 0.0
#
#  We can keep the matrix symmetric by using the boundary condition
#  to eliminate U(0) from all equations but #0.
#
  for i in range ( 1, n ):
    b[i] = b[i] - A[i,0] * b[0]
    A[i,0] = 0.0
#
#  Equation N-1 is the right boundary condition, U(N-1) = 0.0;
#
  for j in range ( 0, n ):
    A[n-1,j] = 0.0
  A[n-1,n-1] = 1.0
  b[n-1] = 0.0
#
#  We can keep the matrix symmetric by using the boundary condition
#  to eliminate U(N-1) from all equations but #N-1.
#
  for i in range ( 0, n - 1 ):
    b[i] = b[i] - A[i,n-1] * b[n-1]
    A[i,n-1] = 0.0
#
#  Solve the linear system for the finite element coefficients U.
#
  u = la.solve ( A, b )

  return u

def fem1d_bvp_quadratic_test00 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST00 tests FEM1D_BVP_QUADRATIC.
#
#  Discussion:
#
#    - uxx + u = x  for 0 < x < 1
#    u(0) = u(1) = 0
#
#    exact  = x - sinh(x) / sinh(1)
#    exact' = 1 - cosh(x) / sinh(1)
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/m_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test00.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  n = 11

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST00' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '  A(X)  = 1.0' )
  print ( '  C(X)  = 1.0' )
  print ( '  F(X)  = X' )
  print ( '  U(X)  = X - SINH(X) / SINH(1)' )
  print ( '' )
  print ( '  Number of nodes = %d' % ( n ) )
#
#  Geometry definitions.
#
  x_lo = 0.0
  x_hi = 1.0
  x = np.linspace ( x_lo, x_hi, n )

  u = fem1d_bvp_quadratic ( n, a00, c00, f00, x )

  g = np.zeros ( n )
  for i in range ( 0, n ):
    g[i] = exact00 ( x[i] )
#
#  Print a table.
#
  print ( '' )
  print ( '     I    X         U         Uexact    Error' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %4d  %8f  %8f  %8f  %8e' \
      % ( i, x[i], u[i], g[i], abs ( u[i] - g[i] ) ) )
#
#  Compute error norms.
#
  e1 = l1_error ( n, x, u, exact00 )
  e2 = l2_error_quadratic ( n, x, u, exact00 )
  h1s = h1s_error_quadratic ( n, x, u, exactp00 )
  mx = max_error_quadratic ( n, x, u, exact00 )

  print ( '' )
  print ( '  l1 norm of error  = %g' % ( e1 ) )
  print ( '  L2 norm of error  = %g' % ( e2 ) )
  print ( '  Seminorm of error = %g' % ( h1s ) )
  print ( '  Max norm of error = %g' % ( mx ) )
#
#  Plot the computed solution.
#
  fig = plt.figure ( )
  plt.plot ( x, u, 'bo-' )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---U(X)--->' )
  plt.title ( 'FEM1D_BVP_QUADRATIC_TEST00 Solution' )
  plt.savefig ( 'fem1d_bvp_quadratic_test00.png' )
  plt.show ( block = False )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST00' )
  print ( '  Normal end of execution.' )
  return

def a00 ( x ):
  value = 1.0
  return value

def c00 ( x ):
  value = 1.0
  return value

def exact00 ( x ):
  import numpy as np
  value = x - np.sinh ( x ) / np.sinh ( 1.0 )
  return value

def exactp00 ( x ):
  from math import cosh
  from math import sinh
  value = 1.0 - cosh ( x ) / sinh ( 1.0 )
  return value

def f00 ( x ):
  value = x
  return value

def fem1d_bvp_quadratic_test01 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST01 carries out test case #1.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test01.py
#
#  Discussion:
#
#    Use A1, C1, F1, EXACT1, EXACT_UX1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
  import numpy as np
  import platform

  n = 11

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST01' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '  A1(X)  = 1.0' )
  print ( '  C1(X)  = 0.0' )
  print ( '  F1(X)  = X * ( X + 3 ) * exp ( X )' )
  print ( '  U1(X)  = X * ( 1 - X ) * exp ( X )' )
  print ( '' )
  print ( '  Number of nodes = %d' % ( n ) )
#
#  Geometry definitions.
#
  x_first = 0.0
  x_last = 1.0
  x = np.linspace ( x_first, x_last, n )

  u = fem1d_bvp_quadratic ( n, a1, c1, f1, x )

  g = np.zeros ( n )
  for i in range ( 0, n ):
    g[i] = exact1 ( x[i] )

  print ( '' )
  print ( '     I    X         U         Uexact    Error' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %4d  %8f  %8f  %8f  %8e' \
      % ( i, x[i], u[i], g[i], abs ( u[i] - g[i] ) ) )

  e1 = l1_error ( n, x, u, exact1 )
  e2 = l2_error_quadratic ( n, x, u, exact1 )
  h1s = h1s_error_quadratic ( n, x, u, exactp1 )
  mx = max_error_quadratic ( n, x, u, exact1 )

  print ( '' )
  print ( '  l1 norm of error  = %g' % ( e1 ) )
  print ( '  L2 norm of error  = %g' % ( e2 ) )
  print ( '  Seminorm of error = %g' % ( h1s ) )
  print ( '  Max norm of error = %g' % ( mx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST01' )
  print ( '  Normal end of execution.' )
  return

def a1 ( x ):
  value = 1.0
  return value

def c1 ( x ):
  value = 0.0
  return value

def exact1 ( x ):
  import numpy as np
  value = x * ( 1.0 - x ) * np.exp ( x )
  return value

def exactp1 ( x ):
  import numpy as np
  value = ( 1.0 - x - x * x ) * np.exp ( x )
  return value

def f1 ( x ):
  import numpy as np
  value = x * ( x + 3.0 ) * np.exp ( x )
  return value

def fem1d_bvp_quadratic_test02 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST02 carries out test case #2.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test02.py
#
#  Discussion:
#
#    Use A2, C2, F2, EXACT2, EXACT_UX2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
  import numpy as np
  import platform

  n = 11

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST02' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '  A2(X)  = 1.0' )
  print ( '  C2(X)  = 2.0' )
  print ( '  F2(X)  = X * ( 5 - X ) * exp ( X )' )
  print ( '  U2(X)  = X * ( 1 - X ) * exp ( X )' )
  print ( '' )
  print ( '  Number of nodes = %d' % ( n ) )
#
#  Geometry definitions.
#
  x_first = 0.0
  x_last = 1.0
  x = np.linspace ( x_first, x_last, n )

  u = fem1d_bvp_quadratic ( n, a2, c2, f2, x )

  g = np.zeros ( n )
  for i in range ( 0, n ):
    g[i] = exact2 ( x[i] )

  print ( '' )
  print ( '     I    X         U         Uexact    Error' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %4d  %8f  %8f  %8f  %8e' \
      % ( i, x[i], u[i], g[i], abs ( u[i] - g[i] ) ) )

  e1 = l1_error ( n, x, u, exact2 )
  e2 = l2_error_quadratic ( n, x, u, exact2 )
  h1s = h1s_error_quadratic ( n, x, u, exactp2 )
  mx = max_error_quadratic ( n, x, u, exact2 )

  print ( '' )
  print ( '  l1 norm of error  = %g' % ( e1 ) )
  print ( '  L2 norm of error  = %g' % ( e2 ) )
  print ( '  Seminorm of error = %g' % ( h1s ) )
  print ( '  Max norm of error = %g' % ( mx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST02' )
  print ( '  Normal end of execution.' )
  return

def a2 ( x ):
  value = 1.0
  return value

def c2 ( x ):
  value = 2.0
  return value

def exact2 ( x ):
  import numpy as np
  value = x * ( 1.0 - x ) * np.exp ( x )
  return value

def exactp2 ( x ):
  import numpy as np
  value = ( 1.0 - x - x * x ) * np.exp ( x )
  return value

def f2 ( x ):
  import numpy as np
  value = x * ( 5.0 - x ) * np.exp ( x )
  return value

def fem1d_bvp_quadratic_test03 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST03 carries out test case #3.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test03.py
#
#  Discussion:
#
#    Use A3, C3, F3, EXACT3, EXACT_UX3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
  import numpy as np
  import platform

  n = 11

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST03' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '  A3(X)  = 1.0' )
  print ( '  C3(X)  = 2.0 * X' )
  print ( '  F3(X)  = - X * ( 2 * X * X - 3 * X - 3 ) * exp ( X )' )
  print ( '  U3(X)  = X * ( 1 - X ) * exp ( X )' )
  print ( '' )
  print ( '  Number of nodes = %d' % ( n ) )
#
#  Geometry definitions.
#
  x_first = 0.0
  x_last = 1.0
  x = np.linspace ( x_first, x_last, n )

  u = fem1d_bvp_quadratic ( n, a3, c3, f3, x )

  g = np.zeros ( n )
  for i in range ( 0, n ):
    g[i] = exact3 ( x[i] )

  print ( '' )
  print ( '     I    X         U         Uexact    Error' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %4d  %8f  %8f  %8f  %8e' \
      % ( i, x[i], u[i], g[i], abs ( u[i] - g[i] ) ) )

  e1 = l1_error ( n, x, u, exact3 )
  e2 = l2_error_quadratic ( n, x, u, exact3 )
  h1s = h1s_error_quadratic ( n, x, u, exactp3 )
  mx = max_error_quadratic ( n, x, u, exact3 )

  print ( '' )
  print ( '  l1 norm of error  = %g' % ( e1 ) )
  print ( '  L2 norm of error  = %g' % ( e2 ) )
  print ( '  Seminorm of error = %g' % ( h1s ) )
  print ( '  Max norm of error = %g' % ( mx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST03' )
  print ( '  Normal end of execution.' )
  return

def a3 ( x ):
  value = 1.0
  return value

def c3 ( x ):
  value = 2.0 * x
  return value

def exact3( x ):
  import numpy as np
  value = x * ( 1.0 - x ) * np.exp ( x )
  return value

def exactp3 ( x ):
  import numpy as np
  value = ( 1.0 - x - x * x ) * np.exp ( x )
  return value

def f3 ( x ):
  import numpy as np
  value = - x * ( 2.0 * x * x - 3.0 * x - 3.0 ) * np.exp ( x )
  return value

def fem1d_bvp_quadratic_test04 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST04 carries out test case #4.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test04.py
#
#  Discussion:
#
#    Use A4, C4, F4, EXACT4, EXACT_UX4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
  import numpy as np
  import platform

  n = 11

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST04' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '  A4(X)  = 1.0 + X * X' )
  print ( '  C4(X)  = 0.0' )
  print ( '  F4(X)  = ( X + 3 X^2 + 5 X^3 + X^4 ) * exp ( X )' )
  print ( '  U4(X)  = X * ( 1 - X ) * exp ( X )' )
  print ( '' )
  print ( '  Number of nodes = %d' % ( n ) )
#
#  Geometry definitions.
#
  x_first = 0.0
  x_last = 1.0
  x = np.linspace ( x_first, x_last, n )

  u = fem1d_bvp_quadratic ( n, a4, c4, f4, x )

  g = np.zeros ( n )
  for i in range ( 0, n ):
    g[i] = exact4 ( x[i] )

  print ( '' )
  print ( '     I    X         U         Uexact    Error' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %4d  %8f  %8f  %8f  %8e' \
      % ( i, x[i], u[i], g[i], abs ( u[i] - g[i] ) ) )

  e1 = l1_error ( n, x, u, exact4 )
  e2 = l2_error_quadratic ( n, x, u, exact4 )
  h1s = h1s_error_quadratic ( n, x, u, exactp4 )
  mx = max_error_quadratic ( n, x, u, exact4 )

  print ( '' )
  print ( '  l1 norm of error  = %g' % ( e1 ) )
  print ( '  L2 norm of error  = %g' % ( e2 ) )
  print ( '  Seminorm of error = %g' % ( h1s ) )
  print ( '  Max norm of error = %g' % ( mx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST04' )
  print ( '  Normal end of execution.' )
  return

def a4 ( x ):
  value = 1.0 + x * x
  return value

def c4 ( x ):
  value = 0.0
  return value

def exact4 ( x ):
  import numpy as np
  value = x * ( 1.0 - x ) * np.exp ( x )
  return value

def exactp4 ( x ):
  import numpy as np
  value = ( 1.0 - x - x * x ) * np.exp ( x )
  return value

def f4 ( x ):
  import numpy as np
  value = ( x + 3.0 * x * x + 5.0 * x ** 3 + x ** 4 ) * np.exp ( x )
  return value

def fem1d_bvp_quadratic_test05 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST05 carries out test case #5.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test05.py
#
#  Discussion:
#
#    Use A5, C5, F5, EXACT5, EXACT_UX5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
  import numpy as np
  import platform

  n = 11

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST05' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '  A5(X)  = 1.0 + X * X for X <= 1/3' )
  print ( '         = 7/9 + X     for      1/3 < X' )
  print ( '  C5(X)  = 0.0' )
  print ( '  F5(X)  = ( X + 3 X^2 + 5 X^3 + X^4 ) * exp ( X )' )
  print ( '                       for X <= 1/3' )
  print ( '         = ( - 1 + 10/3 X + 43/9 X^2 + X^3 ) .* exp ( X )' )
  print ( '                       for      1/3 <= X' )
  print ( '  U5(X)  = X * ( 1 - X ) * exp ( X )' )
  print ( '' )
#
#  Geometry definitions.
#
  x_first = 0.0
  x_last = 1.0
  x = np.linspace ( x_first, x_last, n )

  u = fem1d_bvp_quadratic ( n, a5, c5, f5, x )

  g = np.zeros ( n )
  for i in range ( 0, n ):
    g[i] = exact5 ( x[i] )

  print ( '' )
  print ( '     I    X         U         Uexact    Error' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %4d  %8f  %8f  %8f  %8e' \
      % ( i, x[i], u[i], g[i], abs ( u[i] - g[i] ) ) )

  e1 = l1_error ( n, x, u, exact5 )
  e2 = l2_error_quadratic ( n, x, u, exact5 )
  h1s = h1s_error_quadratic ( n, x, u, exactp5 )
  mx = max_error_quadratic ( n, x, u, exact5 )

  print ( '' )
  print ( '  l1 norm of error  = %g' % ( e1 ) )
  print ( '  L2 norm of error  = %g' % ( e2 ) )
  print ( '  Seminorm of error = %g' % ( h1s ) )
  print ( '  Max norm of error = %g' % ( mx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST05' )
  print ( '  Normal end of execution.' )
  return

def a5 ( x ):
  if ( x <= 1.0 / 3.0 ):
    value = 1.0 + x * x
  else:
    value = x + 7.0 / 9.0

  return value

def c5 ( x ):
  value = 0.0
  return value

def exact5 ( x ):
  import numpy as np
  value = x * ( 1.0 - x ) * np.exp ( x )
  return value

def exactp5 ( x ):
  import numpy as np
  value = ( 1.0 - x - x * x ) * np.exp ( x )
  return value

def f5 ( x ):
  import numpy as np
  if ( x <= 1.0 / 3.0 ):
    value = ( x + 3.0 * x ** 2 + 5.0 * x ** 3 + x ** 4 ) * np.exp ( x )
  else:
    value = ( - 1.0 + ( 10.0 / 3.0 ) * x \
    + ( 43.0 / 9.0 ) * x ** 2 + x ** 3 ) * np.exp ( x )

  return value

def fem1d_bvp_quadratic_test06 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST06 does an error analysis.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test06.py
#
#  Discussion:
#
#    Use A6, C6, F6, EXACT6, EXACT_UX6.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST06' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '  A6(X)  = 1.0' )
  print ( '  C6(X)  = 0.0' )
  print ( '  F6(X)  = pi*pi*sin(pi*X)' )
  print ( '  U6(X)  = sin(pi*x)' )
  print ( '' )
  print ( '  Compute L2 norm and seminorm of error for various N.' )
  print ( '' )
  print ( '     N        L1 error        L2 error      Seminorm error  Maxnorm error' )
  print ( '' )

  n = 11

  for i in range ( 0, 5 ):
#
#  Geometry definitions.
#
    x_first = 0.0
    x_last = 1.0
    x = np.linspace ( x_first, x_last, n )

    u = fem1d_bvp_quadratic ( n, a6, c6, f6, x )

    e1 = l1_error ( n, x, u, exact6 )
    e2 = l2_error_quadratic ( n, x, u, exact6 )
    h1s = h1s_error_quadratic ( n, x, u, exactp6 )
    mx = max_error_quadratic ( n, x, u, exact6 )

    print ( '  %4d  %14g  %14g  %14g  %14g' % ( n, e1, e2, h1s, mx ) )

    n = 2 * ( n - 1 ) + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST06' )
  print ( '  Normal end of execution.' )
  return

def a6 ( x ):
  value = 1.0
  return value

def c6 ( x ):
  value = 0.0
  return value

def exact6 ( x ):
  import numpy as np
  value = np.sin ( np.pi * x )
  return value

def exactp6 ( x ):
  import numpy as np
  value = np.pi * np.cos ( np.pi * x )
  return value

def f6 ( x ):
  import numpy as np
  value = np.pi ** 2 * np.sin ( np.pi * x )
  return value

def fem1d_bvp_quadratic_test07 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST07 does an error analysis.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test07.py
#
#  Discussion:
#
#    Use A7, C7, F7, EXACT7, EXACT_UX7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Eric Becker, Graham Carey, John Oden,
#    Finite Elements, An Introduction, Volume I,
#    Prentice-Hall, 1981, page 123-124,
#    ISBN: 0133170578,
#    LC: TA347.F5.B4.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST07' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Becker/Carey/Oden example.' )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '' )
  print ( '  Compute L2 norm and seminorm of error for various N.' )
  print ( '' )
  print ( '     N        L1 error        L2 error      Seminorm error  Maxnorm error' )
  print ( '' )

  n = 11

  for i in range ( 0, 5 ):
#
#  Geometry definitions.
#
    x_first = 0.0
    x_last = 1.0
    x = np.linspace ( x_first, x_last, n )

    u = fem1d_bvp_quadratic ( n, a7, c7, f7, x )

    e1 = l1_error ( n, x, u, exact7 )
    e2 = l2_error_quadratic ( n, x, u, exact7 )
    h1s = h1s_error_quadratic ( n, x, u, exactp7 )
    mx = max_error_quadratic ( n, x, u, exact7 )

    print ( '  %4d  %14g  %14g  %14g  %14g' % ( n, e1, e2, h1s, mx ) )

    n = 2 * ( n - 1 ) + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST07' )
  print ( '  Normal end of execution.' )
  return

def a7 ( x ):
  alpha = 30.0
  x0 = 1.0 / 3.0
  value = 1.0 / alpha + alpha * ( x - x0 ) ** 2
  return value

def c7 ( x ):
  value = 0.0
  return value

def exact7 ( x ):
  import numpy as np
  alpha = 30.0
  x0 = 1.0 / 3.0
  value = ( 1.0 - x ) * ( np.arctan ( alpha * ( x - x0 ) ) + np.arctan ( alpha * x0 ) )
  return value

def exactp7 ( x ):
  import numpy as np
  alpha = 30.0
  x0 = 1.0 / 3.0
  value = - np.arctan ( alpha * ( x - x0 ) ) - np.arctan ( alpha * x0 ) \
    + ( 1.0 - x ) * alpha / ( 1.0 + alpha * alpha * ( x - x0 ) ** 2 )
  return value

def f7 ( x ):
  import numpy as np
  alpha = 30.0
  x0 = 1.0 / 3.0
  value = 2.0 * ( 1.0 + alpha * ( x - x0 ) * \
    ( np.arctan ( alpha * ( x - x0 ) ) + np.arctan ( alpha * x0 ) ) )
  return value

def fem1d_bvp_quadratic_test08 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST08 carries out test case #8.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test08.py
#
#  Discussion:
#
#    Use A8, C8, F8, EXACT8, EXACT_UX8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
  import numpy as np
  import platform

  n = 11

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST08' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '  A8(X)  = 1.0' )
  print ( '  C8(X)  = 0.0' )
  print ( '  F8(X)  = X * ( X + 3 ) * exp ( X ),   X <= 2/3' )
  print ( '         = 2 * exp ( 2/3),                   2/3 < X' )
  print ( '  U8(X)  = X * ( 1 - X ) * exp ( X ),   X <= 2/3' )
  print ( '         = X * ( 1 - X ) * exp ( 2/3 ),      2/3 < X' )
  print ( '' )
  print ( '  Number of nodes = %d' % ( n ) )
#
#  Geometry definitions.
#
  x_first = 0.0
  x_last = 1.0
  x = np.linspace ( x_first, x_last, n )

  u = fem1d_bvp_quadratic ( n, a8, c8, f8, x )

  g = np.zeros ( n )
  for i in range ( 0, n ):
    g[i] = exact8 ( x[i] )

  print ( '' )
  print ( '     I    X         U         Uexact    Error' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %4d  %8f  %8f  %8f  %8e' \
      % ( i, x[i], u[i], g[i], abs ( u[i] - g[i] ) ) )

  e1 = l1_error ( n, x, u, exact8 )
  e2 = l2_error_quadratic ( n, x, u, exact8 )
  h1s = h1s_error_quadratic ( n, x, u, exactp8 )
  mx = max_error_quadratic ( n, x, u, exact8 )

  print ( '' )
  print ( '  l1 norm of error  = %g' % ( e1 ) )
  print ( '  L2 norm of error  = %g' % ( e2 ) )
  print ( '  Seminorm of error = %g' % ( h1s ) )
  print ( '  Max norm of error = %g' % ( mx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST08' )
  print ( '  Normal end of execution.' )
  return

def a8 ( x ):
  value = 1.0
  return value

def c8 ( x ):
  value = 0.0
  return value

def exact8 ( x ):
  import numpy as np
  if ( x <= 2.0 / 3.0 ):
    value = x * ( 1.0 - x ) * np.exp ( x )
  else:
    value = x * ( 1.0 - x ) * np.exp ( 2.0 / 3.0 )
  return value

def exactp8 ( x ):
  import numpy as np
  if ( x <= 2.0 / 3.0 ):
    value = ( 1.0 - x - x * x ) * np.exp ( x )
  else:
    value = ( 1.0 - 2.0 * x ) * np.exp ( 2.0 / 3.0 )
  return value

def f8 ( x ):
  import numpy as np
  if ( x <= 2.0 / 3.0 ):
    value = x * ( x + 3.0 ) * np.exp ( x )
  else:
    value = 2.0 * np.exp ( 2.0 / 3.0 )
  return value

def fem1d_bvp_quadratic_test09 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST09 carries out test case #9.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test09.py
#
#  Discussion:
#
#    Use A9, C9, F9, EXACT9, EXACT_UX9.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
  import numpy as np
  import platform

  n = 11

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST09' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '  A9(X)  = 1.0' )
  print ( '  C9(X)  = 0.0' )
  print ( '  F9(X)  = X * ( X + 3 ) * exp ( X ),   X <= 2/3' )
  print ( '         = 2 * exp ( 2/3),                   2/3 < X' )
  print ( '  U9(X)  = X * ( 1 - X ) * exp ( X ),   X <= 2/3' )
  print ( '         = X * ( 1 - X ),                    2/3 < X' )
  print ( '' )
  print ( '  Number of nodes = %d' % ( n ) )
#
#  Geometry definitions.
#
  x_first = 0.0
  x_last = 1.0
  x = np.linspace ( x_first, x_last, n )

  u = fem1d_bvp_quadratic ( n, a9, c9, f9, x )

  g = np.zeros ( n )
  for i in range ( 0, n ):
    g[i] = exact9 ( x[i] )

  print ( '' )
  print ( '     I    X         U         Uexact    Error' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %4d  %8f  %8f  %8f  %8e' \
      % ( i, x[i], u[i], g[i], abs ( u[i] - g[i] ) ) )

  e1 = l1_error ( n, x, u, exact9 )
  e2 = l2_error_quadratic ( n, x, u, exact9 )
  h1s = h1s_error_quadratic ( n, x, u, exactp9 )
  mx = max_error_quadratic ( n, x, u, exact9 )

  print ( '' )
  print ( '  l1 norm of error  = %g' % ( e1 ) )
  print ( '  L2 norm of error  = %g' % ( e2 ) )
  print ( '  Seminorm of error = %g' % ( h1s ) )
  print ( '  Max norm of error = %g' % ( mx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST09' )
  print ( '  Normal end of execution.' )
  return

def a9 ( x ):
  value = 1.0
  return value

def c9 ( x ):
  value = 0.0
  return value

def exact9 ( x ):
  import numpy as np
  if ( x <= 2.0 / 3.0 ):
    value = x * ( 1.0 - x ) * np.exp ( x )
  else:
    value = x * ( 1.0 - x )
  return value

def exactp9 ( x ):
  import numpy as np
  if ( x <= 2.0 / 3.0 ):
    value = ( 1.0 - x - x * x ) * np.exp ( x )
  else:
    value = ( 1.0 - 2.0 * x )
  return value

def f9 ( x ):
  import numpy as np
  if ( x <= 2.0 / 3.0 ):
    value = x * ( x + 3.0 ) * np.exp ( x )
  else:
    value = 2.0
  return value

def fem1d_bvp_quadratic_test10 ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST10 tests FEM1D_BVP_QUADRATIC.
#
#  Discussion:
#
#    We want to compute errors and do convergence rates for the 
#    following problem:
#
#    - uxx + u = x  for 0 < x < 1
#    u(0) = u(1) = 0
#
#    exact  = x - sinh(x) / sinh(1)
#    exact' = 1 - cosh(x) / sinh(1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dianne O'Leary,
#    Scientific Computing with Case Studies,
#    SIAM, 2008,
#    ISBN13: 978-0-898716-66-5,
#    LC: QA401.O44.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST10' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve -( A(x) U\'(x) )\' + C(x) U(x) = F(x)' )
  print ( '  for 0 < x < 1, with U(0) = U(1) = 0.' )
  print ( '  A(X)  = 1.0' )
  print ( '  C(X)  = 1.0' )
  print ( '  F(X)  = X' )
  print ( '  U(X)  = X - SINH(X) / SINH(1)' )
  print ( '' )
  print ( ' log(E)    E         L2error         H1error        Maxerror' )
  print ( '' )

  e_log_max = 6

  ne_plot = np.zeros ( e_log_max + 1 )
  h_plot = np.zeros ( e_log_max + 1 )
  l2_plot = np.zeros ( e_log_max + 1 )
  h1_plot = np.zeros ( e_log_max + 1 )
  mx_plot = np.zeros ( e_log_max + 1 )

  for e_log in range ( 0, e_log_max + 1 ):

    ne = 2 ** ( e_log + 1 )
    n = ne + 1

    x_lo = 0.0
    x_hi = 1.0
    x = np.linspace ( x_lo, x_hi, n )

    u = fem1d_bvp_quadratic ( n, a10, c10, f10, x )

    ne_plot[e_log] = ne

    h_plot[e_log] = ( x_hi - x_lo ) / float ( ne )

    l2_plot[e_log] = l2_error_quadratic ( n, x, u, exact10 )

    h1_plot[e_log] = h1s_error_quadratic ( n, x, u, exactp10 )

    mx_plot[e_log] = max_error_quadratic ( n, x, u, exact10 )

    print ( '  %4d  %4d  %14g  %14g  %14g' \
    % ( e_log + 1, ne, l2_plot[e_log], h1_plot[e_log], mx_plot[e_log] ) )

  print ( '' )
  print ( ' log(E1)  E1 / E2          L2rate          H1rate         Maxrate' )
  print ( '' )

  for e_log in range ( 0, e_log_max ):
    ne1 = 2 ** ( e_log + 1 )
    ne2 = 2 * ne1
    ne_plot[e_log] = ne1
    l2 = l2_plot[e_log] / l2_plot[e_log+1]
    l2 = np.log ( l2 ) / np.log ( 2.0 )
    h1 = h1_plot[e_log] / h1_plot[e_log+1]
    h1 = np.log ( h1 ) / np.log ( 2.0 )
    mx = mx_plot[e_log] / mx_plot[e_log+1]
    mx = np.log ( mx ) / np.log ( 2.0 )
    print ( '  %4d  %4d/%4d  %14g  %14g  %14g' \
      % ( e_log + 1, ne1, ne2, l2, h1, mx ) )
#
#  Plot the L2 error as a function of NE.
#
  fig = plt.figure ( )
  plt.plot ( ne_plot, l2_plot, 'bo-' )
  plt.xlabel ( '<---NE--->' )
  plt.ylabel ( '<---L2(error)--->' )
  plt.title ( 'L2 error as function of number of elements' )
  plt.xscale ( 'log' )
  plt.yscale ( 'log' )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.savefig ( 'l2error_test10.png' )
  plt.show ( block = False )
#
#  Plot the max error as a function of NE.
#
  fig = plt.figure ( )
  plt.plot ( ne_plot, mx_plot, 'bo-' )
  plt.xlabel ( '<---NE--->' )
  plt.ylabel ( '<---Max(error)--->' )
  plt.title ( 'Max error as function of number of elements' )
  plt.xscale ( 'log' )
  plt.yscale ( 'log' )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.savefig ( 'maxerror_test10.png' )
  plt.show ( block = False )
#
#  Plot the H1 error as a function of NE.
#
  fig = plt.figure ( )
  plt.plot ( ne_plot, h1_plot, 'bo-' )
  plt.xlabel ( '<---NE--->' )
  plt.ylabel ( '<---H1(error)--->' )
  plt.title ( 'H1 error as function of number of elements' )
  plt.xscale ( 'log' )
  plt.yscale ( 'log' )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.savefig ( 'h1error_test10.png' )
  plt.show ( block = False )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST10' )
  print ( '  Normal end of execution.' )
  return

def a10 ( x ):
  value = 1.0
  return value

def c10 ( x ):
  value = 1.0
  return value

def exact10 ( x ):
  import numpy as np
  value = x - np.sinh ( x ) / np.sinh ( 1.0 )
  return value

def exactp10 ( x ):
  import numpy as np
  value = 1.0 - np.cosh ( x ) / np.sinh ( 1.0 )
  return value

def f10 ( x ):
  value = x
  return value

def fem1d_bvp_quadratic_test ( ):

#*****************************************************************************80
#
## FEM1D_BVP_QUADRATIC_TEST tests the FEM1D_BVP_QUADRATIC library.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/fem1d_bvp_quadratic_test.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the FEM1D_BVP_QUADRATIC library.' )
#
#  Utility functions.
#
  h1s_error_quadratic_test ( )
  l1_error_test ( )
  l2_error_quadratic_test ( )
  max_error_quadratic_test ( )
#
#  Library functions.
#
  fem1d_bvp_quadratic_test00 ( )
  fem1d_bvp_quadratic_test01 ( )
  fem1d_bvp_quadratic_test02 ( )
  fem1d_bvp_quadratic_test03 ( )
  fem1d_bvp_quadratic_test04 ( )
  fem1d_bvp_quadratic_test05 ( )
  fem1d_bvp_quadratic_test06 ( )
  fem1d_bvp_quadratic_test07 ( )
  fem1d_bvp_quadratic_test08 ( )
  fem1d_bvp_quadratic_test09 ( )
  fem1d_bvp_quadratic_test10 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEM1D_BVP_QUADRATIC_TEST:' )
  print ( '  Normal end of execution.' )

def h1s_error_quadratic ( n, x, u, exact_ux ):

#*****************************************************************************80
#
## H1S_ERROR_QUADRATIC: seminorm error of a finite element solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/h1s_error_quadratic.py
#
#  Discussion:
#
#    We assume the finite element method has been used, over an interval [A,B]
#    involving N nodes, with piecewise quadratic elements used for the basis.
#    The finite element solution U(x) has been computed, and a formula for the
#    exact derivative V'(x) is known.
#
#    This function estimates the H1 seminorm of the error:
#
#      H1S = sqrt ( integral ( A <= x <= B ) ( U'(x) - V'(x) )^2 dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of nodes.
#
#    Input, real X(N), the mesh points.
#
#    Input, real U(N), the finite element coefficients.
#
#    Input, function EQ = EXACT_UX ( X ), returns the value of the exact
#    derivative at the point X.
#
#    Output, real H1S, the estimated seminorm of the error.
#
  import numpy as np

  h1s = 0.0
#
#  Define a 2 point Gauss-Legendre quadrature rule on [-1,+1].
#
  quad_num = 2
  abscissa = np.array ( [ -0.577350269189625764509148780502, \
                          +0.577350269189625764509148780502 ] )
  weight = np.array ( [ 1.0, 1.0 ] )
#
#  Integrate over each interval.
#
  e_num = ( n - 1 ) // 2

  for e in range ( 0, e_num ):

    l = 2 * e
    xl = x[l]
    ul = u[l]

    m = 2 * e + 1
    xm = x[m]
    um = u[m]

    r = 2 * e + 2
    xr = x[r]
    ur = u[r]

    for q in range ( 0, quad_num ):

      xq = ( ( 1.0 - abscissa[q] ) * xl   \
           + ( 1.0 + abscissa[q] ) * xr ) \
           /   2.0

      wq = weight[q] * ( xr - xl ) / 2.0

      vxl = (         1.0 / ( xl - xm ) ) \
          * ( ( xq - xr ) / ( xl - xr ) ) \
          + ( ( xq - xm ) / ( xl - xm ) ) \
          * (         1.0 / ( xl - xr ) )

      vxm = (         1.0 / ( xm - xl ) ) \
          * ( ( xq - xr ) / ( xm - xr ) ) \
          + ( ( xq - xl ) / ( xm - xl ) ) \
          * (         1.0 / ( xm - xr ) )

      vxr = (         1.0 / ( xr - xl ) ) \
          * ( ( xq - xm ) / ( xr - xm ) ) \
          + ( ( xq - xl ) / ( xr - xl ) ) \
          * (         1.0 / ( xr - xm ) )

      uxq = u[l] * vxl + u[m] * vxm + u[r] * vxr
#
#  The piecewise quadratic derivative is a constant in the interval.
#
      uxq = ( ur - ul ) / ( xr - xl )

      exq = exact_ux ( xq )

      h1s = h1s + wq * ( uxq - exq ) ** 2

  h1s = np.sqrt ( h1s )

  return h1s

def h1s_error_quadratic_test ( ):

#*****************************************************************************80
#
## H1S_ERROR_QUADRATIC_TEST tests H1S_ERROR_QUADRATIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'H1S_ERROR_QUADRATIC_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  H1S_ERROR_QUADRATIC computes the H1 seminorm approximation error' )
  print ( '  between the exact derivative of a function and the derivative' )
  print ( '  of a piecewise quadratic approximation to the function,' )
  print ( '  associated with n mesh points x().' )
  print ( '' )
  print ( '   N    H1S_Error' )
  print ( '' )

  x_n = 3

  for test in range ( 0, 8 ):
    x_lo = 0.0
    x_hi = np.pi
    x = np.linspace ( x_lo, x_hi, x_n )
#
#  U is an approximation to sin(x).
#
    u = np.zeros ( x_n )
    for i in range ( 0, x_n ):
      u[i] = np.sin ( x[i] )
#
#  Compare the derivative of the piecewise interpolant of U
#  to the actual derivative, cos(x).
#
    e1 = h1s_error_quadratic ( x_n, x, u, np.cos )

    print ( '  %2d  %g' % ( x_n, e1 ) )

    x_n = 2 * ( x_n - 1 ) + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'H1S_ERROR_QUADRATIC_TEST:' )
  print ( '  Normal end of execution.' )
  return

def l1_error ( n, x, u, exact ):

#*****************************************************************************80
#
## L1_ERROR estimates the l1 error norm of a finite element solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/l1_error.py
#
#  Discussion:
#
#    We assume the finite element method has been used, over an interval [A,B]
#    involving N nodes.
#
#    The coefficients U(1:N) have been computed, and a formula for the
#    exact solution is known.
#
#    This function estimates the little l1 norm of the error:
#      L1_NORM = sum ( 1 <= I <= N ) abs ( U(i) - EXACT(X(i)) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of nodes.
#
#    Input, real X(N), the mesh points.
#
#    Input, real U(N), the finite element coefficients.
#
#    Input, function EQ = EXACT ( X ), returns the value of the exact
#    solution at the point X.
#
#    Output, real E1, the little l1 norm of the error.
#
  e1 = 0.0
  for i in range ( 0, n ):
    e1 = e1 + abs ( u[i] - exact ( x[i] ) )

  e1 = e1 / n

  return e1

def l1_error_test ( ):

#*****************************************************************************80
#
## L1_ERROR_TEST tests L1_ERROR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'L1_ERROR_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  L1_ERROR computes the little l1 approximation error between' )
  print ( '  a function exact(x) and a vector of n values u() at points x().'  )
  print ( '' )
  print ( '   N    L1_Error' )
  print ( '' )

  x_n = 3

  for test in range ( 0, 6 ):
    x_lo = 0.0
    x_hi = np.pi
    x = np.linspace ( x_lo, x_hi, x_n )
#
#  U is an approximation to sin(x).
#
    u = np.zeros ( x_n )
    for i in range ( 0, x_n ):
      u[i] = x[i] - x[i] ** 3 / 6.0

    e1 = l1_error ( x_n, x, u, np.sin )

    print ( '  %2d  %g' % ( x_n, e1 ) )

    x_n = 2 * ( x_n - 1 ) + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'L1_ERROR_TEST:' )
  print ( '  Normal end of execution.' )
  return

def l2_error_quadratic ( n, x, u, exact ):

#*****************************************************************************80
#
## L2_ERROR_QUADRATIC estimates the L2 error norm of a finite element solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/l2_error_quadratic.py
#
#  Discussion:
#
#    We assume the finite element method has been used, over an interval [A,B]
#    involving N nodes, with piecewise quadratic elements used for the basis.
#    The coefficients U(1:N) have been computed, and a formula for the
#    exact solution is known.
#
#    This function estimates the L2 norm of the error:
#
#      L2_NORM = Integral ( A <= X <= B ) ( U(X) - EXACT(X) )^2 dX
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of nodes.
#
#    Input, real X(N), the mesh points.
#
#    Input, real U(N), the finite element coefficients.
#
#    Input, function EQ = EXACT ( X ), returns the value of the exact
#    solution at the point X.
#
#    Output, real E2, the estimated L2 norm of the error.
#
  import numpy as np

  e2 = 0.0
#
#  Define a 2 point Gauss-Legendre quadrature rule on [-1,+1].
#
  quad_num = 2
  abscissa = np.array ( [ -0.577350269189625764509148780502, \
                          +0.577350269189625764509148780502 ] )
  weight = np.array ( [ 1.0, 1.0 ] )
#
#  Integrate over each interval.
#
  e_num = ( n - 1 ) // 2

  for e in range ( 0, e_num ):

    l = 2 * e
    xl = x[l]
    ul = u[l]

    m = 2 * e + 1
    xm = x[m]
    um = u[m]

    r = 2 * e + 2
    xr = x[r]
    ur = u[r]

    for q in range ( 0, quad_num ):

      xq = ( ( 1.0 - abscissa[q] ) * xl   \
           + ( 1.0 + abscissa[q] ) * xr ) \
           /   2.0

      wq = weight[q] * ( xr - xl ) / 2.0

      vl = ( ( xq - xm ) / ( xl - xm ) ) \
         * ( ( xq - xr ) / ( xl - xr ) )

      vm = ( ( xq - xl ) / ( xm - xl ) ) \
         * ( ( xq - xr ) / ( xm - xr ) )

      vr = ( ( xq - xl ) / ( xr - xl ) ) \
         * ( ( xq - xm ) / ( xr - xm ) )

      uq = u[l] * vl + u[m] * vm + u[r] * vr

      eq = exact ( xq )

      e2 = e2 + wq * ( uq - eq ) ** 2

  e2 = np.sqrt ( e2 )

  return e2

def l2_error_quadratic_test ( ):

#*****************************************************************************80
#
## L2_ERROR_QUADRATIC_TEST tests L2_ERROR_QUADRATIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'L2_ERROR_QUADRATIC_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  L2_ERROR_QUADRATIC computes the L2 approximation error between' )
  print ( '  a function exact(x) and a piecewise quadratic function u()' )
  print ( '  associated with n mesh points x().' )
  print ( '' )
  print ( '   N    L2_Error' )
  print ( '' )

  x_n = 3

  for test in range ( 0, 6 ):
    x_lo = 0.0
    x_hi = np.pi
    x = np.linspace ( x_lo, x_hi, x_n )
#
#  U is an approximation to sin(x).
#
    u = np.zeros ( x_n )
    for i in range ( 0, x_n ):
      u[i] = np.sin ( x[i] )

    e1 = l2_error_quadratic ( x_n, x, u, np.sin )

    print ( '  %2d  %g' % ( x_n, e1 ) )

    x_n = 2 * ( x_n - 1 ) + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'L2_ERROR_QUADRATIC_TEST:' )
  print ( '  Normal end of execution.' )
  return

def max_error_quadratic ( n, x, u, exact ):

#*****************************************************************************80
#
## MAX_ERROR_QUADRATIC estimates the max error norm of a finite element solution.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/fem1d_bvp_quadratic/max_error_quadratic.py
#
#  Discussion:
#
#    We assume the finite element method has been used, over an interval [A,B]
#    involving N nodes, with piecewise quadratic elements used for the basis.
#    The coefficients U(1:N) have been computed, and a formula for the
#    exact solution is known.
#
#    This function estimates the max norm of the error:
#
#      MAX_NORM = Integral ( A <= X <= B ) max ( abs ( U(X) - EXACT(X) ) ) dX
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of nodes.
#
#    Input, real X(N), the mesh points.
#
#    Input, real U(N), the finite element coefficients.
#
#    Input, function EQ = EXACT ( X ), returns the value of the exact
#    solution at the point X.
#
#    Output, real VALUE, the estimated max norm of the error.
#
  import numpy as np

  quad_num = 8
  value = 0.0
#
#  Examine QUAD_NUM points in each element, including left node but not right.
#
  e_num = ( n - 1 ) // 2

  for e in range ( 0, e_num ):

    l = 2 * e
    xl = x[l]
    ul = u[l]

    m = 2 * e + 1
    xm = x[m]
    um = u[m]

    r = 2 * e + 2
    xr = x[r]
    ur = u[r]

    for q in range ( 0, quad_num ):

      xq = ( float ( quad_num - q ) * xl   \
           + float (            q ) * xr ) \
         /   float ( quad_num     )

      vl = ( ( xq - xm ) / ( xl - xm ) ) \
         * ( ( xq - xr ) / ( xl - xr ) )

      vm = ( ( xq - xl ) / ( xm - xl ) ) \
         * ( ( xq - xr ) / ( xm - xr ) )

      vr = ( ( xq - xl ) / ( xr - xl ) ) \
         * ( ( xq - xm ) / ( xr - xm ) )

      uq = u[l] * vl + u[m] * vm + u[r] * vr

      eq = exact ( xq )

      value = max ( value, abs ( uq - eq ) )
#
#  For completeness, check last node.
#
  xq = x[n-1]
  uq = u[n-1]
  eq = exact ( xq )

  value = max ( value, abs ( uq - eq ) )
#
#  Integral approximation requires multiplication by interval length.
#
  value = value * ( x[n-1] - x[0] )

  return value

def max_error_quadratic_test ( ):

#*****************************************************************************80
#
## MAX_ERROR_QUADRATIC_TEST tests MAX_ERROR_QUADRATIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'MAX_ERROR_QUADRATIC_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MAX_ERROR_QUADRATIC computes the maximum absolute approximation error' )
  print ( '  between a function exact(x) and a piecewise quadratic function u()' )
  print ( '  associated with n mesh points x().' )
  print ( '' )
  print ( '   N    Max_Error' )
  print ( '' )

  n = 3

  for test in range ( 0, 5 ):

    x_lo = 0.0
    x_hi = np.pi
    x = np.linspace ( x_lo, x_hi, n )
#
#  U is an approximation to sin(x).
#
    u = np.zeros ( n )
    for i in range ( 0, n ):
      u[i] = np.sin ( x[i] )

    e1 = max_error_quadratic ( n, x, u, np.sin )

    print ( '  %2d    %g' % ( n, e1 ) )

    n = 2 * ( n - 1 ) + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'MAX_ERROR_QUADRATIC_TEST:' )
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
  fem1d_bvp_quadratic_test ( )
  timestamp ( )

