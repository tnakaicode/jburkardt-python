#! /usr/bin/env python3
#
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
#    Unfortunately, the natural MATLAB function to use, polyval(),
#    assumes that the polynomial coefficients are given in the
#    opposite order, so that c1 multiplies x^(m-1).
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
#    real C(M+1,1), the polynomial coefficients.  
#    C(I+1) is the coefficient of X^I.
#
#    integer N, the number of evaluation points.
#
#    real X(N,1), the evaluation points.
#
#  Output:
#
#    real P(N,1), the polynomial values.
#
  import numpy as np

  p = np.zeros ( n )

  for j in range ( 0, n ):
    p[j] = c[m]
    for i in range ( m - 1, -1, -1 ):
      p[j] = p[j] * x[j] + c[i]

  return p

def vandermonde_approx_1d_coef ( n, m, x, y ):

#*****************************************************************************80
#
## vandermonde_approx_1d_coef() computes a 1D polynomial approximant.
#
#  Discussion:
#
#    We assume the approximating function has the form
#
#      p(x) = c1 + c2 * x + c3 * x^2 + ... + cm+1 * x^m.
#
#    We have n data values (x(i),y(i)) which must be approximated:
#
#      p(x(i)) = c1 + c2 * x(i) + c3 * x(i)^2 + ... + cm+1 * x(i)^m = y(i)
#
#    This can be cast as an Nx(M+1) linear system for the polynomial
#    coefficients:
#
#      [ 1 x1 x1^2 ... x1^m ] [  c1   ] = [  y1 ]
#      [ 1 x2 x2^2 ... x2^m ] [  c2   ] = [  y2 ]
#      [ .................. ] [ ...   ] = [ ... ]
#      [ 1 xn xn^2 ... xn^m ] [  cm+1 ] = [  yn ]
#
#    In the typical case, N is greater than M+1 (we have more data and equations
#    than degrees of freedom) and so a least squares solution is appropriate,
#    in which case the computed polynomial will be a least squares approximant
#    to the data.
#
#    The polynomial could be evaluated at the n-vector x by the command
#
#      pval = polyval ( c, x )
#
#    ...except that MATLAB assumes that c(1) multiplies x^m.
#
#    so instead, you might use
#
#      pval = poly_value ( m, c, n, x )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data points.
#
#    integer M, the degree of the polynomial.
#
#    real X(N,1), Y(N,1), the data values.
#
#  Output:
#
#    real C(M+1), the coefficients of the approximating
#    polynomial.  C(0) is the constant term, and C(M) multiplies X^M.
#
  import numpy as np

  A = vandermonde_approx_1d_matrix ( n, m, x )

  c = np.linalg.solve ( A, y )

  return c

def vandermonde_approx_1d_matrix ( n, m, x ):

#*****************************************************************************80
#
## vandermonde_approx_1d_matrix() computes a Vandermonde 1D approximation matrix.
#
#  Discussion:
#
#    We assume the approximant has the form
#
#      p(x) = c1 + c2 * x + c3 * x^2 + ... + cm+1 * x^m.
#
#    We have n data values (x(i),y(i)) which must be approximated:
#
#      p(x(i)) = c1 + c2 * x(i) + c3 * x(i)^2 + ... + cm+1 * x(i)^m = y(i)
#
#    This can be cast as an Nx(M+1) linear system for the polynomial
#    coefficients:
#
#      [ 1 x1 x1^2 ... x1^m ] [  c1   ] = [  y1 ]
#      [ 1 x2 x2^2 ... x2^m ] [  c2   ] = [  y2 ]
#      [ .................. ] [ ...   ] = [ ... ]
#      [ 1 xn xn^2 ... xn^m ] [  cm+1 ] = [  yn ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 September 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data points.
#
#    integer M, the degree of the polynomial.
#
#    real X(N,1), the data values.
#
#  Output:
#
#    real A(N,M+1), the Vandermonde matrix for X.
#
  import numpy as np

  A = np.zeros ( [ n, m + 1 ] )

  for i in range ( 0, n ):
    A[i,0] = 1.0

  for j in range ( 1, m + 1 ):
    for i in range ( 0, n ):
      A[i,j] = A[i,j-1] * x[i]

  return A

def vandermonde_approx_1d_test01 ( m, nd ):

#*****************************************************************************80
#
## vandermonde_approx_1d_test01() tests vandermonde_approx_1d_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the polynomial degree.
#
#    integer N, the number of sample points.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'vandermonde_approx_1d_test01():' )
  print ( '  Number of data points = ', nd )

  a = 0.0;
  b = 1.0;
  xd = np.linspace ( a, b, nd );
  yd =          np.cos (  7.0 * xd ) \
        + 5.0 * np.cos ( 11.2 * xd ) \
        - 2.0 * np.cos ( 14.0 * xd ) \
        + 5.0 * np.cos ( 31.5 * xd ) \
        + 7.0 * np.cos ( 63.0 * xd )

  print ( '' )
  print ( '  Data array:' )
  print ( np.vstack ( [ xd, yd ]  ).T )
#
#  Compute the Vandermonde matrix.
#
  print ( '  Using polynomial approximant of degree', m )

  A = vandermonde_approx_1d_matrix ( nd, m, xd )
#
#  Solve the linear system for the polynomial coefficients.
#
  c, _, _, _ = np.linalg.lstsq ( A, yd, rcond = None )
#
#  #1:  Does approximant match function at data points?
#
  ni = nd
  xi = xd
  yi = r8poly_values_horner ( m, c, ni, xi )

  app_error = np.linalg.norm ( yi - yd ) / ni

  print ( '' )
  print ( '  L2 data interpolation error = ', app_error )
#
#  #2: Compare estimated curve length to piecewise linear (minimal) curve length.
#  Assume data is sorted, and normalize X and Y dimensions by (XMAX-XMIN) and
#  (YMAX-YMIN).
#
  xmin = np.min ( xd )
  xmax = np.max ( xd )
  ymin = np.min ( yd )
  ymax = np.max ( yd )

  ni = 501
  xi = np.linspace ( xmin, xmax, ni )
  yi = r8poly_values_horner ( m, c, ni, xi )

  ld = np.sum ( np.sqrt ( ( ( xd[1:nd] - xd[0:nd-1] ) / ( xmax - xmin ) )**2 \
                        + ( ( yd[1:nd] - yd[0:nd-1] ) / ( ymax - ymin ) )**2 ) )

  li = np.sum ( np.sqrt ( ( ( xi[1:ni] - xi[0:ni-1] ) / ( xmax - xmin ) )**2 \
                        + ( ( yi[1:ni] - yi[0:ni-1] ) / ( ymax - ymin ) )**2 ) )

  print ( '' )
  print ( '  Normalized length of piecewise linear interpolant = ', ld )
  print ( '  Normalized length of polynomial approximant       = ', li )
#
#  #3: Plot the piecewise linear interpolant.
#
  if ( m == 1 ):
    plt.clf ( )
    plt.plot ( xd, yd, 'b-', linewidth = 3 )
    plt.plot ( xd, yd, 'k.', markersize = 20 )
    plt.xlabel ( '<--- X --->' )
    plt.ylabel ( '<--- Y --->' )
    plt.title ( 'Piecewise Linear Interpolant' )
    plt.grid ( True )
    filename = 'data.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )
#
#  #4: Plot the exact function and polynomial approximant.
#
  plt.clf ( )
  ni = 101
  xmin = np.min ( xd )
  xmax = np.max ( xd )
  xi = np.linspace ( xmin, xmax, ni )
  yi = r8poly_values_horner ( m, c, ni, xi )
  ne = 501
  xe = np.linspace ( xmin, xmax, ne )
  ye =          np.cos (  7.0 * xe ) \
        + 5.0 * np.cos ( 11.2 * xe ) \
        - 2.0 * np.cos ( 14.0 * xe ) \
        + 5.0 * np.cos ( 31.5 * xe ) \
        + 7.0 * np.cos ( 63.0 * xe )
  plt.plot ( xi, yi, 'r-', linewidth = 3 )
  plt.plot ( xe, ye, 'b-', linewidth = 3 )
  plt.plot ( xd, yd, 'k.', markersize = 20 )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'Vandermonde Polynomial Approximant of degree ' + str ( m ) )
  plt.grid ( True )
  filename = 'poly_' + str ( m ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def vandermonde_approx_1d_test ( ):

#*****************************************************************************80
#
## vandermonde_approx_1d_test() tests vandermonde_approx_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'vandermonde_approx_1d_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test vandermonde_approx_1d().' )

  n = 25
  for m in [ 0, 1, 2, 3, 4, 5, 9, 12, 15, 18 ]:
    vandermonde_approx_1d_test01 ( m, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'vandermonde_approx_1d_test():' )
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
  vandermonde_approx_1d_test ( )
  timestamp ( )


