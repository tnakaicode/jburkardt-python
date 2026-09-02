#! /usr/bin/env python3
#
def collocation_test ( ):

#*****************************************************************************80
#
## collocation_test() tests collocation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'collocation_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  Test collocation().' )
 
  collocation_test01 ( )
  collocation_test02 ( )
  collocation_test03 ( )
  collocation_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'collocation_test():' )
  print ( '  Normal end of execution.' )

  return

def collocation_test01 ( ):

#*****************************************************************************80
#
## collocation_test01() collocates Y(X)=SIN(X) using a polynomial.
#
#  Discussion:
#
#    Given the functional equation:
#
#      f(x) = sin(x)
#
#    we use collocation to construct a function g(x) such that
#
#      g(x(i)) = sin(x(i))
#
#    exactly, at a set of N collocation points.
#
#    N = number of collocation points X.
#    X(I) evenly spaced points in interval [0,2*PI].
#    G(X) = polynomial of degree N-1 in X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'collocation_test01():' )
  print ( '  Collocate the equation F(X)=SIN(X)' )
  print ( '  Let N be the number of collocation points.' )
  print ( '  Choose N points X in [0,2Pi].' )
  print ( '  Let G(X) be a polynomial of degree N-1.' )
  print ( '    G(X(1:N)) = SIN(X(1:N))' )
  print ( '  is N equations for the N unknown coefficients in G.' )
#
#  Set the collocation points.
#
  n1 = 11
  xl = 0.0
  xr = 2.0 * np.pi
  d = n1 - 1
  x1 = np.linspace ( xl, xr, n1 )
#
#  Set up the linear system for the coefficients.
#
  A = np.zeros ( [ n1, n1 ] )
  A[:,0] = 1.0
  for j in range ( 1, n1 ):
    A[:,j] = A[:,j-1] * x1

  y1 = np.sin ( x1 ) 
#
#  Solve the system.
#
  c = np.linalg.solve ( A, y1 )
#
#  Plot the collocation function versus the exact solution.
#
  n2 = 101
  x2 = np.linspace ( xl, xr, n2 )
  y2 = r8poly_values_horner ( d, c, n2, x2 )

  y3 = np.sin ( x2 )

  plt.clf ( )
  plt.plot ( x2, y3, 'r-', linewidth = 8 )
  plt.plot ( x2, y2, 'b-', linewidth = 2 )
  plt.plot ( x1, y1, 'k.', markersize = 30 )
  plt.grid ( True )
  plt.title ( 'Collocate F(X)=SIN(X) using a polyonomial.' )
  filename = 'test01.png'
  plt.savefig ( filename );
  print ( '  Graphics saved as "' + filename + '".' )
  plt.close ( )

  return

def collocation_test02 ( ):

#*****************************************************************************80
#
## collocation_test02() collocates a two point boundary value problem.
#
#  Discussion:
#
#    A function y(x) is assumed to exist, and to be twice continuously
#    differentiable, over [0.0,2.0], satisfying the following conditions:
#
#      y(0.0) = 1.0
#      y''(x) = y(x) for 0 < x < 2.0
#      y(2.0) = e^2 
#
#    We use collocation to construct a function g(x) such that
#
#      g(x(1)=0.0) = 1.0
#      g''(x(i)) = g(x(i)) for x(2) through x(n-1)
#      g(x(n)=2.0) = e^2
#
#    exactly, at a set of N collocation points between 0.0 and 2.0,
#    with X(1) = 0.0 and X(N) = 2.0, and assuming G(X) is a polynomial
#    of degree N-1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'collocation_test02():' )
  print ( '  Collocate a two point boundary value problem.' )
  print ( '  Let N be the number of collocation points.' )
  print ( '  Choose N points X in [0,2].' )
  print ( '  Let G(X) be a polynomial of degree N-1.' )
  print ( '    G(X(1)=0.0) = 1.0' )
  print ( '    G"(X(2:N-1)) = G(X(2:N-1))' )
  print ( '    G(X(N)=2.0) = exp(2.0)' )
  print ( '  is N equations for the N unknown coefficients in G.' )
#
#  Set the collocation points.
#
  n1 = 11
  xl = 0.0
  xr = 2.0
  d = n1 - 1
  x1 = np.linspace ( xl, xr, n1 )
  x1 = x1
#
#  Set up the linear system for the coefficients.
#
  A = np.zeros ( [ n1, n1 ] )

  for i in range ( 0, n1 ):
    for j in range ( 0, n1 ):
      A[i,j] = x1[i]**j

  for i in range ( 1, n1 - 1 ):
    for j in range ( 2, n1 ):
      A[i,j] = A[i,j] - j * ( j - 1 ) * x1[i]**( j - 2 )

  y1 = np.zeros ( n1 )
  y1[0] = 1.0
  y1[n1-1] = np.exp ( 2.0 )
#
#  Solve the system.
#
  c = np.linalg.solve ( A, y1 )
#
#  Overwrite Y1 (RHS of linear system) with actual collocation values.
#
  y1 = r8poly_values_horner ( d, c, n1, x1 )
#
#  Plot the collocation function versus the exact solution.
#
  n2 = 101
  x2 = np.linspace ( xl, xr, n2 )
  y2 = r8poly_values_horner ( d, c, n2, x2 )

  y3 = np.exp ( x2 )

  plt.clf ( )
  plt.axis ( [ 0.0, 2.0, 0.0, 8.0 ] )
  plt.plot ( x2, y3, 'r-', linewidth = 8 )
  plt.plot ( x2, y2, 'b-', linewidth = 2 )
  plt.plot ( x1, y1, 'k.', markersize = 30 )
  plt.grid ( True )
  plt.title ( 'Collocate two point BVP using a polyonomial.' )
  filename = 'test02.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '".' )
  plt.close ( )

  return

def collocation_test03 ( ):

#*****************************************************************************80
#
## collocation_test03() collocates a two point boundary value problem.
#
#  Discussion:
#
#    A function y(x) is assumed to exist, and to be twice continuously
#    differentiable, over [0.0,2.0], satisfying the following conditions:
#
#      y(0.0) = 1.0
#      y''(x) = y(x) for 0 < x < 2.0
#      y(2.0) = e^2 
#
#    We use collocation to construct a function g(x) such that
#
#      g(x(1)=0.0) = 1.0
#      g''(x(i)) = g(x(i)) for x(2) through x(n-1)
#      g(x(n)=2.0) = e^2
#
#    exactly, at a set of N collocation points between 0.0 and 2.0,
#    with X(1) = 0.0 and X(N) = 2.0, and assuming G(X) is a sum of
#    sine functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'collocation_test03():' )
  print ( '  Collocate a two point boundary value problem.' )
  print ( '  Let N be the number of collocation points.' )
  print ( '  Choose N points X in [0,2].' )
  print ( '  Let G(X) be C1+C2*X+C(3:N)*SIN((1:N-2)*PI*X/(N-2)).' )
  print ( '    G(X(1)=0.0) = 1.0' )
  print ( '    G"(X(2:N-1)) = G(X(2:N-1))' )
  print ( '    G(X(N)=2.0) = exp(2.0)' )
  print ( '  is N equations for the N unknown coefficients in G.' )
#
#  Set the collocation points.
#
  n1 = 5
  xl = 0.0
  xr = 2.0
  d = n1 - 1
  x1 = np.linspace ( xl, xr, n1 )
#
#  Set up the linear system for the coefficients.
#
  A = np.zeros ( [ n1, n1 ] )

  for i in range ( 0, n1 ):
    A[i,0] = 1.0
    A[i,1] = x1[i]
    for j in range ( 2, n1 ):
      angle = ( j - 1 ) * np.pi * x1[i] / ( n1 - 2 )
      A[i,j] = np.sin ( angle )

  for i in range ( 1, n1 - 1 ):
    for j in range ( 2, n1 ):
      A[i,j] = A[i,j] + ( j - 1 )**2 * np.pi**2 * np.sin ( ( j - 1 ) \
        * np.pi * x1[i] / ( n1 - 2 ) ) / ( n1 - 2 )**2

  y1 = np.zeros ( n1 )
  y1[0] = 1.0
  y1[n1-1] = np.exp ( 2.0 )
#
#  Solve the system.
#
  c = np.linalg.solve ( A, y1 )
#
#  Overwrite Y1 (RHS of linear system) with actual collocation values.
#
  for i in range ( 0, n1 ):
    y1[i] = c[0] + c[1] * x1[i]
    for j in range ( 2, n1 ):
      y1[i] = y1[i] + c[j] * np.sin ( ( j - 1 ) * np.pi * x1[i] / ( n1 - 2 ) )
#
#  Plot the collocation function versus the exact solution.
#
  n2 = 101
  x2 = np.linspace ( xl, xr, n2 )
  y2 = np.zeros ( n2 )
  for i in range ( 0, n2 ):
    y2[i] = y2[i] + c[0] + c[1] * x2[i]
    for j in range ( 2, n1 ):
      y2[i] = y2[i] + c[j] * np.sin ( ( j - 1 ) * np.pi * x2[i] / ( n1 - 2 ) )

  y3 = np.exp ( x2 )

  plt.clf ( )
  plt.axis ( [ 0.0, 2.0, 0.0, 8.0 ] )
  plt.plot ( x2, y3, 'r-', linewidth = 8 )
  plt.plot ( x2, y2, 'b-', linewidth = 2 )
  plt.plot ( x1, y1, 'k.', markersize = 30 )
  plt.grid ( True )
  plt.title ( 'Collocate two point BVP using sines.' )
  filename = 'test03.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '".' )
  plt.close ( )

  return

def collocation_test04 ( ):

#*****************************************************************************80
#
## collocation_test04() collocates a second-order initial value problem.
#
#  Discussion:
#
#    A function y(x) is assumed to exist, and to be twice continuously
#    differentiable, over [-3.0,2.0], satisfying the following conditions:
#
#      y (-3.0) = a
#      y'(-3.0) = b
#      y''(x) - 6y'(x) + 13 y(x) = 0 for -3.0 < x < 2.0
#
#    We use collocation to construct a function g(x) such that
#
#      g(x(1)=-3.0) = a
#      g'(x(1)=-3.0) = b
#      g''(x(i)) - 6 g'(x(i))+13 g(x(i)) = 0 for x(2) through x(n-1)
#
#    exactly, at a set of N-1 collocation points between -3.0 and 2.0,
#    with X(1) = -3.0 and X(N) = 2.0, and assuming G(X) is a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'collocation_test04():' )
  print ( '  Collocate a second order initial value ODE.' )
  print ( '  Let N be the number of collocation points.' )
  print ( '  Choose N points X in [-3,2].' )
  print ( '  Let G(X) be a polynomial in X of degree N.' )
  print ( '    G(-3) = A' )
  print ( '    G''(-3) = B' )
  print ( '    G"(X(I)) - 6 G''(X(I) + 13 G(X(I)) = 0, I = 2...N' )
  print ( '  is N equations for the N unknown coefficients in G.' )
#
#  Set the collocation points.
#  For this case, we have 
#    N = 6 distinct collocation points
#    7 constraints
#    7 polynomial coefficients.
#
  n1 = 6
  xl = -3.0
  xr = 2.0
  d = n1
  x1 = np.linspace ( xl, xr, n1 )
#
#  Choose alpha and beta.
#  e(x) = exp ( 3 x ) * ( alpha * cos ( 2x ) + beta * sin ( 2x ) )
#
  alpha = 1.0
  beta = 2.0
#
#  Set up the linear system for the coefficients.
#
  A = np.zeros ( [ n1+1, n1+1 ] )
  y1 = np.zeros ( n1 + 1 )
#
#  y(-3) = exact(-3.0).
#
  i = 0
  A[0,0] = 1.0
  for j in range ( 1, n1 + 1 ):
    A[0,j] = A[0,j-1] * x1[0]

  y1[i] = exact ( xl, alpha, beta )
#
#  y'(-3) = exact'(-3.0).
#
  i = 1
  A[1,0] = 0.0
  A[1,1] = 1.0
  for j in range ( 1, n1 + 1 ):
    A[1,j] = j * x1[0]**( j - 1 )

  y1[i] = exact1 ( xl, alpha, beta )
#
#  y''-6y'+13y = 0 at nodes 2 through N-1.
#
  for i in range ( 2, n1 + 1 ):
    xp0 = 1.0
    xp1 = 0.0
    xp2 = 0.0
    for j in range ( 0, n1 + 1 ):
      A[i,j] = xp2 - 6.0 * xp1 + 13.0 * xp0
      xp2 = ( j + 1 ) * xp1
      xp1 = ( j + 1 ) * xp0
      xp0 = xp0 * x1[i-1]
    y1[i] = 0.0
#
#  Solve the system.
#
  c = np.linalg.solve ( A, y1 )
#
#  Set up a table of the collocation function.
#
  n2 = 101
  x2 = np.linspace ( xl, xr, n2 )
  y2 = r8poly_values_horner ( d, c, n2, x2 )
#
#  Set up a table of the exact solution.
#
  n3 = 101
  x3 = np.linspace ( xl, xr, n2 )
  y3 = exact ( x3, alpha, beta )
#
#  Plot.
#
  plt.clf ( )
  plt.plot ( x2, y3, 'r-', linewidth = 8 )
  plt.plot ( x2, y2, 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.title ( 'Collocate second order ODE using polynomial.' )
  filename = 'test04.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '".' )
  plt.close ( )

  return

def exact ( x, alpha, beta ):

#*****************************************************************************80
#
## exact() returns the exact value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    double x: the evaluation point.
#
#    double alpha, beta: parameter values.
#
#  Output:
#
#    double value: the value of the function.
#
  import numpy as np

  value = np.exp ( 3.0 * x ) \
    * ( alpha * np.cos ( 2.0 * x ) + beta * np.sin ( 2.0 * x ) )

  return value

def exact1 ( x, alpha, beta ):

#*****************************************************************************80
#
## exact1() returns the exact value of the derivative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    double x: the evaluation point.
#
#    double alpha, beta: parameter values.
#
#  Output:
#
#    double value: the value of the derivative.
#
  import numpy as np

  value = 3.0 * np.exp ( 3.0 * x ) \
    * ( alpha * np.cos ( 2.0 * x ) + beta * np.sin ( 2.0 * x ) ) \
    + np.exp ( 3.0 * x ) \
    * ( - 2.0 * alpha * np.sin ( 2.0 * x ) + 2.0 * beta * np.cos ( 2.0 * x ) )

  return value

def r8poly_values_horner ( m, c, n, x ):

#*****************************************************************************80
#
## r8poly_values_horner() evaluates a polynomial using Horner's method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    can be evaluated at the vector x by the command
#
#      pval = r8poly_value ( m, c, n, x )
#
#    Note that C must actually be dimensioned of size M+1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the degree.
#
#    real C(M+1), the polynomial coefficients.  
#    C(I+1) is the coefficient of X^I.
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real P(N), the polynomial values.
#
  import numpy as np

  p = np.zeros ( n )

  for j in range ( 0, n ):
    p[j] = c[m]
    for i in range ( m - 1, -1, -1 ):
      p[j] = p[j] * x[j] + c[i]

  return p

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
  collocation_test ( )
  timestamp ( )

