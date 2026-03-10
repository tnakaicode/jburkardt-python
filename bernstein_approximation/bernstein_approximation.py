#! /usr/bin/env python3
#
def bernstein_approximation_test ( ):

#*****************************************************************************80
#
## bernstein_approximation_test() tests bernstein_approximation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'bernstein_approximation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test bernstein_approximation().' )

  bernstein_poly_ab_approx_test ( )
  bernstein_poly_ab_approx_display ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'bernstein_approximation_test():' )
  print ( '  Normal end of execution.' )

  return

def bernstein_poly_ab_approx_display ( ):

#*****************************************************************************80
#
## bernstein_poly_ab_approx_display() displays Bernstein approximants.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'bernstein_poly_ab_approx_display():' )
  print ( '  bernstein_poly_ab_approx() evaluates the Bernstein polynomial' )
  print ( '  approximant to a function F(X).' )
#
#  Sin(x)
#
  print ( '' )
  print ( '  This program displays the sequence of approximants' )
  print ( '  to y=sin(x) over the interval [1,3]' )

  a = 1.0
  b = 3.0

  for n in range ( 0, 11 ):
#
#  Generate data values.
#
    xdata = np.linspace ( a, b, n + 1 )
    ydata = np.sin ( xdata )
#
#  Compare the true function and the approximant.
#
    nval = 501
    xval = np.linspace ( a, b, nval )
    yval = bernstein_poly_ab_approx ( n, a, b, ydata, nval, xval )
    ytrue = np.sin ( xval )

    plt.clf ( )
    plt.plot ( xval, yval, 'b-' )
    plt.plot ( xval, ytrue, 'r-' )
    plt.plot ( xdata, ydata, 'r.', markersize = 30 )
    plt.grid ( True )
    plt.xlabel ( '<---X--->' )
    plt.ylabel ( '<---Y--->' )
    s = 'Bernstein Approximant to sine(), n =' + str ( n )
    plt.title ( s )
    filename = 'bernstein_sine_' + str ( n ).zfill(2)
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )
#
#  Heaviside.
#
  a = -1.0
  b = +1.0

  for n in range ( 1, 20, 2 ):
#
#  Generate data values.
#
    xdata = np.linspace ( a, b, n + 1 )
    ydata = np.heaviside ( xdata, 0.5 )
#
#  Compare the true function and the approximant.
#
    nval = 501
    xval = np.linspace ( a, b, nval )
    yval = bernstein_poly_ab_approx ( n, a, b, ydata, nval, xval )
    ytrue = np.heaviside ( xval, 0.5 )

    plt.clf ( )
    plt.plot ( xval, yval, 'b-' )
    plt.plot ( xval, ytrue, 'r-' )
    plt.plot ( xdata, ydata, 'r.', markersize = 30 )
    plt.grid ( True )
    plt.xlabel ( '<---X--->' )
    plt.ylabel ( '<---Y--->' )
    s = 'Bernstein Approximant to heaviside(), n =' + str ( n )
    plt.title ( s )
    filename = 'bernstein_heaviside_' + str ( n ).zfill(2)
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )

  return

def bernstein_poly_ab_approx ( n, a, b, ydata, nval, xval ):

#*****************************************************************************80
#
## bernstein_poly_ab_approx(): Bernstein polynomial approximant to F(X) on [A,B].
#
#  Formula:
#
#    BPAB(F)(X) = sum ( 0 <= I <= N ) F(X(I)) * B_BASE(I,X)
#
#    where
#
#      X(I) = ( ( N - I ) * A + I * B ) / N
#      B_BASE(I,X) is the value of the I-th Bernstein basis polynomial at X.
#
#  Discussion:
#
#    The Bernstein polynomial BPAB(F) for F(X) over [A,B] is an approximant, 
#    not an interpolant; in other words, its value is not guaranteed to equal
#    that of F at any particular point.  However, for a fixed interval
#    [A,B], if we let N increase, the Bernstein polynomial converges
#    uniformly to F everywhere in [A,B], provided only that F is continuous.
#    Even if F is not continuous, but is bounded, the polynomial converges
#    pointwise to F(X) at all points of continuity.  On the other hand,
#    the convergence is quite slow compared to other interpolation
#    and approximation schemes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    integer N, the degree of the Bernstein polynomial
#    to be used.  N must be at least 0.
#
#    real A, B, the endpoints of the interval on which the
#    approximant is based.  A and B should not be equal.
#
#    real YDATA(N+1), the data values at N+1 equally
#    spaced points in [A,B].  If N = 0, then the evaluation point should
#    be 0.5 * ( A + B).  Otherwise, evaluation point I should be
#    ( (N-I)*A + I*B ) / N ).
#
#    integer NVAL, the number of points at which the
#    approximant is to be evaluated.
#
#    real XVAL(NVAL), the point at which the Bernstein 
#    polynomial approximant is to be evaluated.  The entries of XVAL do not 
#    have to lie in the interval [A,B].
#
#  Output:
#
#    real YVAL(NVAL), the values of the Bernstein 
#    polynomial approximant for F, based in [A,B], evaluated at XVAL.
#
  import numpy as np

  yval = np.zeros ( nval )

  for i in range ( 0, nval ):
#
#  Evaluate the Bernstein basis polynomials at XVAL.
#
    bvec = bernstein_poly_ab ( n, a, b, xval[i] )
#
#  Now compute the sum of YDATA(I) * BVEC(I).
#
    yval[i] = np.dot ( ydata, bvec )

  return yval

def bernstein_poly_ab_approx_test ( ):

#*****************************************************************************80
#
## bernstein_poly_ab_approx_test() examines a sequence of approximants.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'bernstein_poly_ab_approx_test():' )
  print ( '  bernstein_poly_ab_approx() evaluates the Bernstein polynomial' )
  print ( '  approximant to a function F(X).' )
  print ( '  As N, the polynomial degree increases, the norm of the error' )
  print ( '  should decrease.' )

  a = 1.0
  b = 3.0

  print ( '' )
  print ( '  Approximate y=sin(x) over the interval [1,3]' )
  print ( '' )
  print ( '   N         |F-B| / |F|' )
  print ( '' )

  for n in range ( 0, 11 ):

    xdata = np.linspace ( a, b, n + 1 )
    ydata = np.sin ( xdata )
#
#  Compare the true function and the approximant.
#
    nval = 501
    xval = np.linspace ( a, b, nval )
    ytrue = np.sin ( xval )
    yapprox = bernstein_poly_ab_approx ( n, a, b, ydata, nval, xval )

    f_norm = np.sum ( np.abs ( ytrue ) ) / ( b - a )
    e_norm = np.sum ( np.abs ( ytrue - yapprox ) ) / ( b - a )
    print ( '  %2d  %14.6g' % ( n, e_norm / f_norm ) )

  a = -1.0
  b = +1.0

  print ( '' )
  print ( '  Approximate y=heaviside(x) over the interval [-1,+1]' )
  print ( '' )
  print ( '   N         |F-B| / |F|' )
  print ( '' )

  for n in range ( 1, 20, 2 ):

    xdata = np.linspace ( a, b, n + 1 )
    ydata = np.heaviside ( xdata, 0.5 )
#
#  Compare the true function and the approximant.
#
    nval = 501
    xval = np.linspace ( a, b, nval )
    ytrue = np.heaviside ( xval, 0.5 )
    yapprox = bernstein_poly_ab_approx ( n, a, b, ydata, nval, xval )

    f_norm = np.sum ( np.abs ( ytrue ) ) / ( b - a )
    e_norm = np.sum ( np.abs ( ytrue - yapprox ) ) / ( b - a )
    print ( '  %2d  %14.6g' % ( n, e_norm / f_norm ) )

  return

def bernstein_poly_ab ( n, a, b, x ):

#*****************************************************************************80
#
## bernstein_poly_ab() evaluates at X the Bernstein polynomials based in [A,B].
#
#  Formula:
#
#    BERN(N,I)(X) = [N!/(I!*(N-I)!)] * (B-X)^(N-I) * (X-A)^I / (B-A)^N
#
#  First values:
#
#    B(0,0)(X) =   1
#
#    B(1,0)(X) = (      B-X                ) / (B-A)
#    B(1,1)(X) = (                 X-A     ) / (B-A)
#
#    B(2,0)(X) = (     (B-X)^2             ) / (B-A)^2
#    B(2,1)(X) = ( 2 * (B-X)    * (X-A)    ) / (B-A)^2
#    B(2,2)(X) = (                (X-A)^2  ) / (B-A)^2
#
#    B(3,0)(X) = (     (B-X)^3             ) / (B-A)^3
#    B(3,1)(X) = ( 3 * (B-X)^2  * (X-A)    ) / (B-A)^3
#    B(3,2)(X) = ( 3 * (B-X)    * (X-A)^2  ) / (B-A)^3
#    B(3,3)(X) = (                (X-A)^3  ) / (B-A)^3
#
#    B(4,0)(X) = (     (B-X)^4             ) / (B-A)^4
#    B(4,1)(X) = ( 4 * (B-X)^3  * (X-A)    ) / (B-A)^4
#    B(4,2)(X) = ( 6 * (B-X)^2  * (X-A)^2  ) / (B-A)^4 
#    B(4,3)(X) = ( 4 * (B-X)    * (X-A)^3  ) / (B-A)^4 
#    B(4,4)(X) = (                (X-A)^4  ) / (B-A)^4 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the degree of the Bernstein polynomials to be used.
#    For any N, there is a set of N+1 Bernstein polynomials, each of
#    degree N, which form a basis for polynomials on [A,B].
#
#    real A, B, the endpoints of the interval on which the
#    polynomials are to be based.  A and B should not be equal.
#
#    real X, the point at which the polynomials are to be evaluated.
#
#  Output:
#
#    real P(N+1), the values of the N+1 Bernstein polynomials at X.
#
  import numpy as np

  if ( b == a ):
    print ( '' )
    print ( 'bernstein_poly_ab(): Fatal error!' )
    print ( '  A = B = %g' % ( a ) )
    raise Exception ( 'bernstein_poly_ab(): Fatal error!' )

  p = np.zeros ( n + 1 )

  if ( n == 0 ):
 
    p[0] = 1.0
 
  elif ( 0 < n ):
 
    p[0] = ( b - x ) / ( b - a )
    p[1] = ( x - a ) / ( b - a )
 
    for i in range ( 2, n + 1 ):
      p[i] = ( x - a ) * p[i-1] / ( b - a )
      for j in range ( i - 1, 0, -1 ):
        p[j] = ( ( b - x ) * p[j] + ( x - a ) * p[j-1] ) / ( b - a )
      p[0] = ( b - x ) * p[0] / ( b - a )
 
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
  bernstein_approximation_test ( )
  timestamp ( )

