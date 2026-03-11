#! /usr/bin/env python3
#
def test_uni_test ( ):

#*****************************************************************************80
#
## test_uni_test() tests test_uni().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( 'test_uni_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test test_uni().' )

  print ( '' )
  print ( '  The number of unimodal test functions is', p00_test_num ( ) )

  p00_title_test ( )
  p00_interval_test ( )
  p00_f_test ( )
  p00_plot_test ( )
  p00_sol_test ( )
#
#  Solvers.
#
  nf = 1001
  p00_exhaust_test ( nf )

  x_tol = 1.0E-12
  p00_bisection_test ( x_tol )

  x_tol = 1.0E-12
  p00_golden_section_test ( x_tol )

# p00_optisection_test ( )

  p00_brent_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_uni_test():' )
  print ( '  Normal end of execution.' )
  return

def golden_section ( f, a, b, n, x_tol ):

#*****************************************************************************80
#
## golden_section() seeks a minimizer of a unimodal function in [a,b].
#
#  Discussion:
#
#    A unimodal function f(x) in [a,b] has a minimizer a <= c <= b such that
#    f(x) strictly decreases between a and c, and strictly increases between
#    c and b.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 August 2019
#
#  Author:
#
#    Original MATLAB code by J Nathan Kutz.
#    This version by John Burkardt.
#
#  Reference:
#
#    J Nathan Kutz,
#    Data Driven Modeling and Scientific Computation,
#    Oxford University Press, 2013,
#    ISBN: 978-0-19-966034-6.
#
#  Input:
#
#    function handle f: the function to be minimized.
#
#    real a, b: the left and right endpoints.
#
#    integer n: the maximum number of iterations allowed.
#    n must be at least 1.
#
#    real x_tol: a tolerance for the width of the x interval.
#
#  Output:
#
#    real a, b: the current interval containing the minimizer.
#
#    integer it: the number of steps taken.
#
#    integer nf: the number of function evaluations.
#
  import numpy as np

  nf = 0

  for it in range ( 0, n + 1 ):

    if ( it == 0 ):

      g = ( - 1.0 + np.sqrt ( 5.0 ) ) / 2.0
      x1 =         g   * a + ( 1.0 - g ) * b
      x2 = ( 1.0 - g ) * a +         g   * b
      f1 = f ( x1 )
      f2 = f ( x2 )
      nf = nf + 2

    else:

      if ( f1 < f2 ):

        b = x2
        x2 = x1
        f2 = f1
        x1 = g * a + ( 1.0 - g ) * b
        f1 = f ( x1 )
        nf = nf + 1

      else:

        a = x1
        x1 = x2
        f1 = f2
        x2 = ( 1.0 - g ) * a + g * b
        f2 = f ( x2 )
        nf = nf + 1

    if ( np.abs ( b - a ) <= x_tol ):
      break

  return a, b, it, nf

def p00_bisection_test ( x_tol ):

#*****************************************************************************80
#
## p00_bisection_test() tests p00_bisection().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x_tol: bisection stops when the interval is smaller than x_tol.
#
  print ( '' )
  print ( 'p00_bisection_test()' )
  print ( '  Minimize using the bisection method.' )
  print ( '  Bisection is halted when the interval is no more than ', x_tol )
#
#  Get the number of tests.
#
  test_num = p00_test_num ( )

  for test in range ( 1, test_num + 1 ):

    title = p00_title ( test )

    print ( '' )
    print ( '  test', test )
    print ( '  "' + title + '"' )

    it = 0

    while ( True ):

      if ( it == 0 ):

        a, c = p00_interval ( test )
        b = 0.5 * ( a + c )
        fa = p00_f ( test, a )
        fb = p00_f ( test, b )
        fc = p00_f ( test, c )
        nf = 3

      else:

        d = 0.5 * ( a + b )
        fd = p00_f ( test, d )

        e = 0.5 * ( b + c )
        fe = p00_f ( test, e )

        nf = nf + 2

        if ( fd <= fb ):
          c = b
          fc = fb
          b = d
          fb = fd
        elif ( fe <= fb ):
          a = b
          fa = fb
          b = e
          fb = fe
        else:
          a = d
          fa = fd
          c = e
          fc = fe

      if ( abs ( c - a ) < x_tol ):
        break

      it = it + 1
#
#  Print final (a,b,c) and (fa,fb,fc) results.
#
    print ( '  Number of iterations:', it )
    print ( '  Function evaluations:', nf )
    print ( '  X:  %16.12e  %16.12e  %16.12e' % ( a,   b,  c ) )
    print ( '  F:  %16.12e  %16.12e  %16.12e' % ( fa, fb, fc ) )

  return

def p00_brent ( a, b, test, tol ):

#*****************************************************************************80
#
## p00_brent() seeks a minimizer of a scalar function of a scalar variable.
#
#  Discussion:
#
#    The code seeks an approximation to the point where F attains a minimum on
#    the interval (A,B).
#
#    The method used is a combination of golden section search and
#    successive parabolic interpolation.  Convergence is never much
#    slower than that for a Fibonacci search.  If F has a continuous
#    second derivative which is positive at the minimum (which is not
#    at A or B), then convergence is superlinear, and usually of the
#    order of about 1.324\.
#
#    The function F is never evaluated at two points closer together
#    than EPS * ABS ( XMIN ) + (TOL/3), where EPS is approximately the
#    square root of the relative machine precision.  If F is a unimodal
#    function and the computed values of F are always unimodal when
#    separated by at least EPS * ABS ( XSTAR ) + (TOL/3), then XMIN
#    approximates the abcissa of the global minimum of F on the
#    interval [A, B] with an error less than 3 * EPS * ABS ( XMIN ) + TOL.
#    If F is not unimodal, then XMIN may approximate a local, but
#    perhaps non-global, minimum to the same accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 March 2026
#
#  Author:
#
#    This version by John Burkardt
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization without Derivatives,
#    Prentice Hall, 1973.
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1988.
#
#  Input:
#
#    real A, B, the left and right endpoints of the initial interval.  
#
#    integer test, the index of a test.
#
#    real TOL, the desired length of the interval of
#    uncertainty of the final result.  TOL must not be negative.
#
#  Output:
#
#    real xmin: the abcissa approximating the minimizer of f.
#
#    real A, B: the lower and upper bounds for the minimizer.
#
#    integer it: the number of iterations.
#
#    integer nf: the number of function evaluations.
#
  import numpy as np

  it = 0
  nf = 0

  c = 0.5 * ( 3.0 - np.sqrt ( 5.0 ) )
#
#  C is the squared inverse of the golden ratio.
#
#  EPSILON is the relative machine precision.
#
  epsilon = np.finfo(float).eps
#
#  Initialization.
#
  v = a + c * ( b - a )
  w = v
  x = v
  e = 0.0
  fx = p00_f ( test, x )
  nf = nf + 1
  nf 
  fv = fx
  fw = fx
#
#  The main loop starts here.
#
  while ( True ):

    it = it + 1
    midpoint = 0.5 * ( a + b )
    tol1 = np.sqrt ( epsilon ) * np.abs ( x ) + tol / 3.0
    tol2 = 2.0 * tol1
#
#  Check the stopping criterion.
#
    if ( abs ( x - midpoint ) <= ( tol2 - 0.5 * ( b - a ) ) ):
      break
#
#  Is golden-section necessary?
#
    if ( abs ( e ) <= tol1 ):
      if ( midpoint <= x ):
        e = a - x
      else:
        e = b - x

      d = c * e
#
#  Consider fitting a parabola.
#
    else:

      r = ( x - w ) * ( fx - fv )
      q = ( x - v ) * ( fx - fw )
      p = ( x - v ) * q - ( x - w ) * r
      q = 2.0 * ( q - r )
      if ( 0.0 < q ):
        p = -p
      q = abs ( q )
      r = e
      e = d
#
#  Choose a golden-section step if the parabola is not advised.
#
      if ( \
        ( abs ( 0.5 * q * r ) <= abs ( p ) ) or \
        ( p <= q * ( a - x ) ) or \
        ( q * ( b - x ) <= p ) ):

        if ( midpoint <= x ):
          e = a - x
        else:
          e = b - x

        d = c * e
#
#  Choose a parabolic interpolation step.
#
      else:

        d = p / q
        u = x + d

        if ( ( u - a ) < tol2 ):
          d = abs ( tol1 ) * np.sign ( midpoint - x )

        if ( ( b - u ) < tol2 ):
          d = abs ( tol1 ) * np.sign ( midpoint - x )
#
#  F must not be evaluated too close to X.
#
    if ( tol1 <= abs ( d ) ):
      u = x + d

    if ( abs ( d ) < tol1 ):
      u = x + abs ( tol1 ) * np.sign ( d )

    fu = p00_f ( test, u )
    nf = nf + 1
#
#  Update the data.
#
    if ( fu <= fx ):

      if ( x <= u ):
        a = x
      else:
        b = x

      v = w
      fv = fw
      w = x
      fw = fx
      x = u
      fx = fu
      continue

    if ( u < x ):
      a = u
    else:
      b = u

    if ( fu <= fw or w == x ):
      v = w
      fv = fw
      w = u
      fw = fu
    elif ( fu <= fv or v == x or v == w ):
      v = u
      fv = fu

  fmin = x

  return fmin, a, b, it, nf

def p00_brent_test ( ):

#*****************************************************************************80
#
## p00_brent_test() carries out a version of Brent's derivative-free minimizer.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 March 2026
#
#  Author:
#
#    John Burkardt
#
  tol = 0.00000001

  print ( '' )
  print ( 'p00_brent_test():' )
  print ( '  p00_brent() use Brent\'s method to seek a minimizer.' )
#
#  Get the number of tests.
#
  test_num = p00_test_num ( )

  for test in range ( 1, test_num + 1 ):

    title = p00_title ( test )

    print ( '' )
    print ( '  test', test )
    print ( '  "' + title + '"' )

    a, b = p00_interval ( test )

    fa = p00_f ( test, a )
    fb = p00_f ( test, b )

    print ( '  Initial interval [A,B]:' )
    print ( '   A,       B:  %24.16e            %24.16e' % ( a,     b ) )
    print ( '  FA,      FB:  %24.16e            %24.16e' % ( fa,     fb ) )

    x, a, b, it, nf = p00_brent ( a, b, test, tol )

    fa = p00_f ( test, a )
    fb = p00_f ( test, b )
    fx = p00_f ( test, x )

    print ( '  Number of iterations:', it )
    print ( '  Function evaluations:', nf )
    print ( '  Final interval [A,X*,B]:' )
    print ( '   A,  X*,  B:  %24.16e  %24.16e  %24.16e' % ( a, x, b ) )
    print ( '  FA, FX*, FB:  %24.16e  %24.16e  %24.16e' % ( fa, fx, fb ) )

  return

def p00_exhaust_test ( nf ):

#*****************************************************************************80
#
## p00_exhaust_test() seeks a minimizer by exhaustion.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer nf: the number of function evaluations.
#
  import numpy as np

  print ( '' )
  print ( 'p00_exhaustion_test()' )
  print ( '  Minimize using exhaustion.' )
  print ( '  Compare function values at equally spaced values.' )
#
#  Get the number of tests.
#
  test_num = p00_test_num ( )

  for test in range ( 1, test_num + 1 ):

    title = p00_title ( test )

    print ( '' )
    print ( '  test', test )
    print ( '  "' + title + '"' )

    a, b = p00_interval ( test )
    x = np.linspace ( a, b, nf )
    f = p00_f ( test, x )

    fmin = np.min ( f )
    imin = np.argmin ( f )
    xmin = x[imin]

    print ( '  Function evaluations:', nf )
    print ( '  f(', xmin, ') = ', fmin )

  return

def p00_f ( test, x ):

#*****************************************************************************80
#
## p00_f() evaluates the function for any test.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer test, the test number.
#
#    real x, the argument of the objective function.
#
#  Output:
#
#    real f, the value of the objective function.
#
  if ( test == 1 ):
    f = p01_f ( x )
  elif ( test == 2 ):
    f = p02_f ( x )
  elif ( test == 3 ):
    f = p03_f ( x )
  elif ( test == 4 ):
    f = p04_f ( x )
  elif ( test == 5 ):
    f = p05_f ( x )
  elif ( test == 6 ):
    f = p06_f ( x )
  elif ( test == 7 ):
    f = p07_f ( x )
  elif ( test == 8 ):
    f = p08_f ( x )
  elif ( test == 9 ):
    f = p09_f ( x )
  elif ( test == 10 ):
    f = p10_f ( x )
  elif ( test == 11 ):
    f = p11_f ( x )
  elif ( test == 12 ):
    f = p12_f ( x )
  elif ( test == 13 ):
    f = p13_f ( x )
  elif ( test == 14 ):
    f = p14_f ( x )
  elif ( test == 15 ):
    f = p15_f ( x )
  elif ( test == 16 ):
    f = p16_f ( x )
  elif ( test == 17 ):
    f = p17_f ( x )
  elif ( test == 18 ):
    f = p18_f ( x )
  elif ( test == 19 ):
    f = p19_f ( x )
  elif ( test == 20 ):
    f = p20_f ( x )
  elif ( test == 21 ):
    f = p21_f ( x )
  elif ( test == 22 ):
    f = p22_f ( x )
  elif ( test == 23 ):
    f = p23_f ( x )
  elif ( test == 24 ):
    f = p24_f ( x )
  elif ( test == 25 ):
    f = p25_f ( x )
  elif ( test == 26 ):
    f = p26_f ( x )
  elif ( test == 27 ):
    f = p27_f ( x )
  elif ( test == 28 ):
    f = p28_f ( x )
  elif ( test == 29 ):
    f = p29_f ( x )
  elif ( test == 30 ):
    f = p30_f ( x )
  elif ( test == 31 ):
    f = p31_f ( x )
  elif ( test == 32 ):
    f = p32_f ( x )
  elif ( test == 33 ):
    f = p33_f ( x )
  elif ( test == 34 ):
    f = p34_f ( x )
  elif ( test == 35 ):
    f = p35_f ( x )
  elif ( test == 36 ):
    f = p36_f ( x )
  elif ( test == 37 ):
    f = p37_f ( x )
  elif ( test == 38 ):
    f = p38_f ( x )
  elif ( test == 39 ):
    f = p39_f ( x )
  elif ( test == 40 ):
    f = p40_f ( x )
  else:
    print ( '' )
    print ( 'p00_f(): Fatal error!' )
    print ( '  Illegal test number = ', test )
    raise Exception ( 'p00_f(): Fatal error!' )

  return f

def p00_f_test ( ):

#*****************************************************************************80
#
## p00_f()_test tests p00_f()
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'p00_f_test():' )
  print ( '  p00_f() evaluates the optimization function f(x)' )
  print ( '  at any point x, and for any test.' )
  print ( '' )
  print ( '  test               X            F(X)' )
  print ( '' )

  test_num = p00_test_num ( )

  for test in range ( 1, test_num + 1 ):

    a, b = p00_interval ( test )

    x_mid = 0.5 * ( a + b )

    f_mid = p00_f ( test, x_mid )

    print ( '  %7d  %14.6g  %14.6g' % ( test, x_mid, f_mid ) )

  return

def p00_golden_section_test ( x_tol ):

#*****************************************************************************80
#
## p00_golden_section_test() tests p00_golden_section().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x_tol: execution stops when the interval is smaller than x_tol.
#
  print ( '' )
  print ( 'p00_golden_section_test()' )
  print ( '  Minimize using the golden section method.' )
  print ( '  Execution is halted when the interval is no more than ', x_tol )
#
#  Get the number of tests.
#
  test_num = p00_test_num ( )

  for test in range ( 1, test_num + 1 ):

    title = p00_title ( test )

    print ( '' )
    print ( '  test', test )
    print ( '  "' + title + '"' )

    a, b = p00_interval ( test )
    n = 100
 
    a, b, it, nf = golden_section ( lambda x: p00_f ( test, x ), a, b, n, x_tol )
#
#  Print results.
#
    fa = p00_f ( test, a )
    fb = p00_f ( test, b )

    print ( '  Number of iterations:', it )
    print ( '  Function evaluations:', nf )
    print ( '  X:  %16.12e  %16.12e' % ( a,   b ) )
    print ( '  F:  %16.12e  %16.12e' % ( fa, fb ) )

  return

def p00_interval ( test ):

#*****************************************************************************80
#
## p00_interval() returns a bracketing interval for any test.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer test: the test index.
#
#  Output:
#
#    real a, b, two points, between which a local minimizer should be sought.
#
  if ( test == 1 ):
    a, b = p01_interval ( )
  elif ( test == 2 ):
    a, b = p02_interval ( )
  elif ( test == 3 ):
    a, b = p03_interval ( )
  elif ( test == 4 ):
    a, b = p04_interval ( )
  elif ( test == 5 ):
    a, b = p05_interval ( )
  elif ( test == 6 ):
    a, b = p06_interval ( )
  elif ( test == 7 ):
    a, b = p07_interval ( )
  elif ( test == 8 ):
    a, b = p08_interval ( )
  elif ( test == 9 ):
    a, b = p09_interval ( )
  elif ( test == 10 ):
    a, b = p10_interval ( )
  elif ( test == 11 ):
    a, b = p11_interval ( )
  elif ( test == 12 ):
    a, b = p12_interval ( )
  elif ( test == 13 ):
    a, b = p13_interval ( )
  elif ( test == 14 ):
    a, b = p14_interval ( )
  elif ( test == 15 ):
    a, b = p15_interval ( )
  elif ( test == 16 ):
    a, b = p16_interval ( )
  elif ( test == 17 ):
    a, b = p17_interval ( )
  elif ( test == 18 ):
    a, b = p18_interval ( )
  elif ( test == 19 ):
    a, b = p19_interval ( )
  elif ( test == 20 ):
    a, b = p20_interval ( )
  elif ( test == 21 ):
    a, b = p21_interval ( )
  elif ( test == 22 ):
    a, b = p22_interval ( )
  elif ( test == 23 ):
    a, b = p23_interval ( )
  elif ( test == 24 ):
    a, b = p24_interval ( )
  elif ( test == 25 ):
    a, b = p25_interval ( )
  elif ( test == 26 ):
    a, b = p26_interval ( )
  elif ( test == 27 ):
    a, b = p27_interval ( )
  elif ( test == 28 ):
    a, b = p28_interval ( )
  elif ( test == 29 ):
    a, b = p29_interval ( )
  elif ( test == 30 ):
    a, b = p30_interval ( )
  elif ( test == 31 ):
    a, b = p31_interval ( )
  elif ( test == 32 ):
    a, b = p32_interval ( )
  elif ( test == 33 ):
    a, b = p33_interval ( )
  elif ( test == 34 ):
    a, b = p34_interval ( )
  elif ( test == 35 ):
    a, b = p35_interval ( )
  elif ( test == 36 ):
    a, b = p36_interval ( )
  elif ( test == 37 ):
    a, b = p37_interval ( )
  elif ( test == 38 ):
    a, b = p38_interval ( )
  elif ( test == 39 ):
    a, b = p39_interval ( )
  elif ( test == 40 ):
    a, b = p40_interval ( )
  else:
    print ( '' )
    print ( 'p00_interval(): Fatal error!' )
    print ( '  Illegal test number = ', test )
    raise Exception ( 'p00_interval(): Fatal error!' )

  return a, b

def p00_interval_test ( ):

#*****************************************************************************80
#
## p00_interval_test() tests p00_interval().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'p00_interval_test():' )
  print ( '  p00_interval() returns the finite interval [A,B] over which' )
  print ( '  the optimization procedure is to be carried out.' )
  print ( '' )
  print ( '  test               A            F(A)               B            F(B)' )
  print ( '' )

  test_num = p00_test_num ( )

  for test in range ( 1, test_num + 1 ):

    a, b = p00_interval ( test )

    fa = p00_f ( test, a )
    fb = p00_f ( test, b )

    print ( '  %7d  %14.6g  %14.6g  %14.6g  %14.6g' % ( test, a, fa, b, fb ) )

  return

def p00_plot_test ( ):

#*****************************************************************************80
#
## p00_plot_test() plots the functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'p00_plot_test():' )
  print ( '  plot the optimization functions.' )
  print ( '' )

  test_num = p00_test_num ( )

  for test in range ( 1, test_num + 1 ):

    a, b = p00_interval ( test )
    x = np.linspace ( a, b, 101 )
    fx = p00_f ( test, x )
    xm = p00_sol ( test )
    fxm = p00_f ( test, xm )

    plt.clf ( )
    plt.plot ( [a,b], [0.0,0.0], color = 'k' )
    plt.grid ( True )
    plt.plot ( x, fx, linewidth = 3, color = 'b' )
    plt.plot ( xm, fxm, 'o', markersize = 10, color = 'r' )
    plt.title ( 'p%02d' % test )
    filename = ( 'p%02d.png' % test )
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )

  return

def p00_sol ( test ):

#*****************************************************************************80
#
## p00_sol() returns the solution for any test.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer test: the test number.
#
#  Output:
#
#    real x: the (approximate) minimizer.
#
  if ( test == 1 ):
    x = p01_sol ( )
  elif ( test == 2 ):
    x = p02_sol ( )
  elif ( test == 3 ):
    x = p03_sol ( )
  elif ( test == 4 ):
    x = p04_sol ( )
  elif ( test == 5 ):
    x = p05_sol ( )
  elif ( test == 6 ):
    x = p06_sol ( )
  elif ( test == 7 ):
    x = p07_sol ( )
  elif ( test == 8 ):
    x = p08_sol ( )
  elif ( test == 9 ):
    x = p09_sol ( )
  elif ( test == 10 ):
    x = p10_sol ( )
  elif ( test == 11 ):
    x = p11_sol ( )
  elif ( test == 12 ):
    x = p12_sol ( )
  elif ( test == 13 ):
    x = p13_sol ( )
  elif ( test == 14 ):
    x = p14_sol ( )
  elif ( test == 15 ):
    x = p15_sol ( )
  elif ( test == 16 ):
    x = p16_sol ( )
  elif ( test == 17 ):
    x = p17_sol ( )
  elif ( test == 18 ):
    x = p18_sol ( )
  elif ( test == 19 ):
    x = p19_sol ( )
  elif ( test == 20 ):
    x = p20_sol ( )
  elif ( test == 21 ):
    x = p21_sol ( )
  elif ( test == 22 ):
    x = p22_sol ( )
  elif ( test == 23 ):
    x = p23_sol ( )
  elif ( test == 24 ):
    x = p24_sol ( )
  elif ( test == 25 ):
    x = p25_sol ( )
  elif ( test == 26 ):
    x = p26_sol ( )
  elif ( test == 27 ):
    x = p27_sol ( )
  elif ( test == 28 ):
    x = p28_sol ( )
  elif ( test == 29 ):
    x = p29_sol ( )
  elif ( test == 30 ):
    x = p30_sol ( )
  elif ( test == 31 ):
    x = p31_sol ( )
  elif ( test == 32 ):
    x = p32_sol ( )
  elif ( test == 33 ):
    x = p33_sol ( )
  elif ( test == 34 ):
    x = p34_sol ( )
  elif ( test == 35 ):
    x = p35_sol ( )
  elif ( test == 36 ):
    x = p36_sol ( )
  elif ( test == 37 ):
    x = p37_sol ( )
  elif ( test == 38 ):
    x = p38_sol ( )
  elif ( test == 39 ):
    x = p39_sol ( )
  elif ( test == 40 ):
    x = p40_sol ( )
  else:
    print ( '' )
    print ( 'p00_sol(): Fatal error!' )
    print ( '  Illegal test number = ', test )
    raise Exception ( 'p00_sol(): Fatal error!' )

  return x

def p00_sol_test ( ):

#*****************************************************************************80
#
## p00_sol_test() tests p00_sol().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'p00_sol_test():' )
  print ( '  p00_sol() returns a minimizer for any test function f(x)' )
  print ( '' )
  print ( '  test               X            F(X)' )
  print ( '' )

  test_num = p00_test_num ( )

  for test in range ( 1, test_num + 1 ):

    x_sol = p00_sol ( test )

    f_sol = p00_f ( test, x_sol )

    print ( '  %7d  %14.6g  %14.6g' % ( test, x_sol, f_sol ) )

  return

def p00_test_num ( ):

#*****************************************************************************80
#
## p00_test_num() returns the number of unimodal test functions available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer test_num: the number of unimodal test functions available.
#
  test_num = 40

  return test_num

def p00_title ( test ):

#*****************************************************************************80
#
## p00_title() returns a title for any test.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer test: the test index.
#
#  Output:
#
#    string title: the title for the test.
#
  if ( test == 1 ):
    title = p01_title ( )
  elif ( test == 2 ):
    title = p02_title ( )
  elif ( test == 3 ):
    title = p03_title ( )
  elif ( test == 4 ):
    title = p04_title ( )
  elif ( test == 5 ):
    title = p05_title ( )
  elif ( test == 6 ):
    title = p06_title ( )
  elif ( test == 7 ):
    title = p07_title ( )
  elif ( test == 8 ):
    title = p08_title ( )
  elif ( test == 9 ):
    title = p09_title ( )
  elif ( test == 10 ):
    title = p10_title ( )
  elif ( test == 11 ):
    title = p11_title ( )
  elif ( test == 12 ):
    title = p12_title ( )
  elif ( test == 13 ):
    title = p13_title ( )
  elif ( test == 14 ):
    title = p14_title ( )
  elif ( test == 15 ):
    title = p15_title ( )
  elif ( test == 16 ):
    title = p16_title ( )
  elif ( test == 17 ):
    title = p17_title ( )
  elif ( test == 18 ):
    title = p18_title ( )
  elif ( test == 19 ):
    title = p19_title ( )
  elif ( test == 20 ):
    title = p20_title ( )
  elif ( test == 21 ):
    title = p21_title ( )
  elif ( test == 22 ):
    title = p22_title ( )
  elif ( test == 23 ):
    title = p23_title ( )
  elif ( test == 24 ):
    title = p24_title ( )
  elif ( test == 25 ):
    title = p25_title ( )
  elif ( test == 26 ):
    title = p26_title ( )
  elif ( test == 27 ):
    title = p27_title ( )
  elif ( test == 28 ):
    title = p28_title ( )
  elif ( test == 29 ):
    title = p29_title ( )
  elif ( test == 30 ):
    title = p30_title ( )
  elif ( test == 31 ):
    title = p31_title ( )
  elif ( test == 32 ):
    title = p32_title ( )
  elif ( test == 33 ):
    title = p33_title ( )
  elif ( test == 34 ):
    title = p34_title ( )
  elif ( test == 35 ):
    title = p35_title ( )
  elif ( test == 36 ):
    title = p36_title ( )
  elif ( test == 37 ):
    title = p37_title ( )
  elif ( test == 38 ):
    title = p38_title ( )
  elif ( test == 39 ):
    title = p39_title ( )
  elif ( test == 40 ):
    title = p40_title ( )
  else:
    print ( '' )
    print ( 'p00_title(): Fatal error!' )
    print ( '  Illegal test number = ', test )
    raise Exception ( 'p00_title(): Fatal error!' )

  return title

def p00_title_test ( ):

#*****************************************************************************80
#
## p00_title_test() prints the title of each test.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'p00_title_test():' )
  print ( '  p00_title() prints the title for each test.' )
#
#  Get the number of tests.
#
  test_num = p00_test_num ( )

  print ( '' )
  print ( '  Test case title' )
  print ( '' )

  for test in range ( 1, test_num + 1 ):

    title = p00_title ( test )
    print ( '  ', test, ':  "' + title + '"' )

  return

def p01_f ( x ):

#*****************************************************************************80
#
## p01_f() evaluates the objective function for test 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = np.ones_like ( x )

  return f

def p01_interval ( ):

#*****************************************************************************80
#
## p01_interval() returns a starting interval for optimization for test 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 1.9
  b = 3.1

  return a, b

def p01_sol ( ):

#*****************************************************************************80
#
## p01_sol() returns an approximate minimizer for test 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 1.9

  return x

def p01_title ( ):

#*****************************************************************************80
#
## p01_title() returns a title for test 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.'

  return title

def p02_f ( x ):

#*****************************************************************************80
#
## p02_f() evaluates the objective function for test 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  f = 20.0 + 16.0 / x

  return f

def p02_interval ( ):

#*****************************************************************************80
#
## p02_interval() returns a starting interval for optimization for test 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 1.5
  b = 4.5

  return a, b

def p02_sol ( ):

#*****************************************************************************80
#
## p02_sol() returns an approximate minimizer for test 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 4.5

  return x

def p02_title ( ):

#*****************************************************************************80
#
## p02_title() returns a title for test 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 20 + 16 / x.'

  return title

def p03_f ( x ):

#*****************************************************************************80
#
## p03_f() evaluates the objective function for test 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.5 + np.exp ( x )

  return f

def p03_interval ( ):

#*****************************************************************************80
#
## p03_interval() returns a starting interval for optimization for test 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 0.5
  b = 4.0

  return a, b

def p03_sol ( ):

#*****************************************************************************80
#
## p03_sol() returns an approximate minimizer for test 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 0.5

  return x

def p03_title ( ):

#*****************************************************************************80
#
## p03_title() returns a title for test 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.5 + exp(x).'

  return title

def p04_f ( x ):

#*****************************************************************************80
#
## p04_f() evaluates the objective function for test 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 3.0 + np.maximum ( 4.0 * np.cos ( x ), -3.0 )

  return f

def p04_interval ( ):

#*****************************************************************************80
#
## p04_interval() returns a starting interval for optimization for test 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 0.1
  b = 4.9

  return a, b

def p04_sol ( ):

#*****************************************************************************80
#
## p04_sol() returns an approximate minimizer for test 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 2.5

  return x

def p04_title ( ):

#*****************************************************************************80
#
## p04_title() returns a title for test 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 3 + max ( 4 * cos ( x ), -3 ).'

  return title

def p05_f ( x ):

#*****************************************************************************80
#
## p05_f() evaluates the objective function for test 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + np.maximum ( 5.0 * np.exp ( x ) - 1.0, 1.0 )

  return f

def p05_interval ( ):

#*****************************************************************************80
#
## p05_interval() returns a starting interval for optimization for test 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -1.6
  b =  1.1

  return a, b

def p05_sol ( ):

#*****************************************************************************80
#
## p05_sol() returns an approximate minimizer for test 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = -1.6

  return x

def p05_title ( ):

#*****************************************************************************80
#
## p05_title() returns a title for test 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + max ( 5 * exp ( x ) - 1, 1 ).'

  return title

def p06_f ( x ):

#*****************************************************************************80
#
## p06_f() evaluates the objective function for test 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.5 + np.maximum ( np.cos ( 4.0 - x**2 ), 0.5 )

  return f

def p06_interval ( ):

#*****************************************************************************80
#
## p06_interval() returns a starting interval for optimization for test 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 2.9
  b = 3.2

  return a, b

def p06_sol ( ):

#*****************************************************************************80
#
## p06_sol() returns an approximate minimizer for test 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 2.9

  return x

def p06_title ( ):

#*****************************************************************************80
#
## p06_title() returns a title for test 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.5 + max ( cos ( 4 - x^2 ), 0.5 ).'

  return title

def p07_f ( x ):

#*****************************************************************************80
#
## p07_f() evaluates the objective function for test 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + np.maximum ( np.exp ( - x ), \
            np.maximum ( np.cos ( x ), \
            np.maximum ( x**4, x**2 ) ) )

  return f

def p07_interval ( ):

#*****************************************************************************80
#
## p07_interval() returns a starting interval for optimization for test 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -0.6
  b =  1.1

  return a, b

def p07_sol ( ):

#*****************************************************************************80
#
## p07_sol() returns an approximate minimizer for test 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 0.8241323123025

  return x

def p07_title ( ):

#*****************************************************************************80
#
## p07_title() returns a title for test 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + max ( exp ( - x ), cos ( x ), x^4, x^2 ).'

  return title

def p08_f ( x ):

#*****************************************************************************80
#
## p08_f() evaluates the objective function for test 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 0.2 + np.maximum ( 3.0 * ( x - 2.0 )**2, 20.0 * ( x - 1.0 ) )

  return f

def p08_interval ( ):

#*****************************************************************************80
#
## p08_interval() returns a starting interval for optimization for test 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -6.0
  b = 11.5

  return a, b

def p08_sol ( ):

#*****************************************************************************80
#
## p08_sol() returns an approximate minimizer for test 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 1.116963119775

  return x

def p08_title ( ):

#*****************************************************************************80
#
## p08_title() returns a title for test 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 0.2 + max ( 3 * ( x - 2 )^2, 20 * ( x - 1 ) ).'

  return title

def p09_f ( x ):

#*****************************************************************************80
#
## p09_f() evaluates the objective function for test 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + np.abs ( x - 1.0 )

  return f

def p09_interval ( ):

#*****************************************************************************80
#
## p09_interval() returns a starting interval for optimization for test 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -0.2
  b =  4.0

  return a, b

def p09_sol ( ):

#*****************************************************************************80
#
## p09_sol() returns an approximate minimizer for test 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 1.0

  return x

def p09_title ( ):

#*****************************************************************************80
#
## p09_title() returns a title for test 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + abs ( x - 1 ).'

  return title

def p10_f ( x ):

#*****************************************************************************80
#
## p10_f() evaluates the objective function for test 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 12.0 + 1000.0 * ( np.abs ( x - 2.8 ) )**8.4

  return f

def p10_interval ( ):

#*****************************************************************************80
#
## p10_interval() returns a starting interval for optimization for test 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -0.4
  b =  5.1

  return a, b

def p10_sol ( ):

#*****************************************************************************80
#
## p10_sol() returns an approximate minimizer for test 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 2.793115234375

  return x

def p10_title ( ):

#*****************************************************************************80
#
## p10_title() returns a title for test 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 12 + 1000 * abs ( x - 2.8 )^8.4.'

  return title

def p11_f ( x ):

#*****************************************************************************80
#
## p11_f() evaluates the objective function for test 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 0.3 + np.cos ( x**2 + 2.0 * x - 3.0 )

  return f

def p11_interval ( ):

#*****************************************************************************80
#
## p11_interval() returns a starting interval for optimization for test 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -0.9
  b =  0.5

  return a, b

def p11_sol ( ):

#*****************************************************************************80
#
## p11_sol() returns an approximate minimizer for test 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = -0.07349725067584

  return x

def p11_title ( ):

#*****************************************************************************80
#
## p11_title() returns a title for test 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 0.3 + cos ( x^2 + 2 * x - 3.0 )'

  return title

def p12_f ( x ):

#*****************************************************************************80
#
## p12_f() evaluates the objective function for test 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 0.2 + ( x - 1.5 )**2

  return f

def p12_interval ( ):

#*****************************************************************************80
#
## p12_interval() returns a starting interval for optimization for test 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 1.0
  b = 3.0

  return a, b

def p12_sol ( ):

#*****************************************************************************80
#
## p12_sol() returns an approximate minimizer for test 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 1.5

  return x

def p12_title ( ):

#*****************************************************************************80
#
## p12_title() returns a title for test 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 0.2 + ( x - 1.5 )^2'

  return title

def p13_f ( x ):

#*****************************************************************************80
#
## p13_f() evaluates the objective function for test 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 100.0 + ( 1.0 - np.exp ( x ) * np.sin ( x ) )**2

  return f

def p13_interval ( ):

#*****************************************************************************80
#
## p13_interval() returns a starting interval for optimization for test 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a =  0.1
  b =  1.0

  return a, b

def p13_sol ( ):

#*****************************************************************************80
#
## p13_sol() returns an approximate minimizer for test 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 0.5885327219967

  return x

def p13_title ( ):

#*****************************************************************************80
#
## p13_title() returns a title for test 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 100 + ( 1 - exp ( x ) * sin ( x ) )^2.'

  return title

def p14_f ( x ):

#*****************************************************************************80
#
## p14_f() evaluates the objective function for test 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 - np.cos ( x**2 )

  return f

def p14_interval ( ):

#*****************************************************************************80
#
## p14_interval() returns a starting interval for optimization for test 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -1.2
  b =  1.5

  return a, b

def p14_sol ( ):

#*****************************************************************************80
#
## p14_sol() returns an approximate minimizer for test 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 0.0

  return x

def p14_title ( ):

#*****************************************************************************80
#
## p14_title() returns a title for test 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 - cos ( x^2 )'

  return title

def p15_f ( x ):

#*****************************************************************************80
#
## p15_f() evaluates the objective function for test 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + 5.0 * np.exp ( - x**2 ) + x

  return f

def p15_interval ( ):

#*****************************************************************************80
#
## p15_interval() returns a starting interval for optimization for test 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a =  0.2
  b =  5.7

  return a, b

def p15_sol ( ):

#*****************************************************************************80
#
## p15_sol() returns an approximate minimizer for test 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 1.679630604507

  return x

def p15_title ( ):

#*****************************************************************************80
#
## p15_title() returns a title for test 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + exp ( - x^2 ) + x'

  return title

def p16_f ( x ):

#*****************************************************************************80
#
## p16_f() evaluates the objective function for test 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + np.exp ( - x ) + 3.5 * np.sin ( x )

  return f

def p16_interval ( ):

#*****************************************************************************80
#
## p16_interval() returns a starting interval for optimization for test 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 2.0
  b = 6.2

  return a, b

def p16_sol ( ):

#*****************************************************************************80
#
## p16_sol() returns an approximate minimizer for test 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 4.714949074049

  return x

def p16_title ( ):

#*****************************************************************************80
#
## p16_title() returns a title for test 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + exp ( - x ) + 3.5 * sin ( x ).'

  return title

def p17_f ( x ):

#*****************************************************************************80
#
## p17_f() evaluates the objective function for test 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 2.3 + 3.0 * np.exp ( x ) - x**2 + 5.0 * x

  return f

def p17_interval ( ):

#*****************************************************************************80
#
## p17_interval() returns a starting interval for optimization for test 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -3.9
  b =  2.5

  return a, b

def p17_sol ( ):

#*****************************************************************************80
#
## p17_sol() returns an approximate minimizer for test 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = -3.9

  return x

def p17_title ( ):

#*****************************************************************************80
#
## p17_title() returns a title for test 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 2.3 + 3 * exp ( x ) - x^2 + 5 * x'

  return title

def p18_f ( x ):

#*****************************************************************************80
#
## p18_f() evaluates the objective function for test 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + 3.0 * np.cosh ( x - 2.0 ) - 2.0 * np.sinh ( x - 3.0 )

  return f

def p18_interval ( ):

#*****************************************************************************80
#
## p18_interval() returns a starting interval for optimization for test 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 1.0
  b = 4.9

  return a, b

def p18_sol ( ):

#*****************************************************************************80
#
## p18_sol() returns an approximate minimizer for test 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 2.657667706908

  return x

def p18_title ( ):

#*****************************************************************************80
#
## p18_title() returns a title for test 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + 3 * cosh ( x - 2 ) - 2 * sinh ( x - 3 )'

  return title

def p19_f ( x ):

#*****************************************************************************80
#
## p19_f() evaluates the objective function for test 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 2.3 + ( np.exp ( 3.0 - x ) + 4.0 * ( x - 2.0 ) )**2

  return f

def p19_interval ( ):

#*****************************************************************************80
#
## p19_interval() returns a starting interval for optimization for test 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 1.0
  b = 2.9

  return a, b

def p19_sol ( ):

#*****************************************************************************80
#
## p19_sol() returns an approximate minimizer for test 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 1.613705632091

  return x

def p19_title ( ):

#*****************************************************************************80
#
## p19_title() returns a title for test 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 2.3 + ( exp ( 3 - x ) + 4 * ( x - 2 ) )^2'

  return title

def p20_f ( x ):

#*****************************************************************************80
#
## p20_f() evaluates the objective function for test 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = x**3 - 3.0 * x**2 - 5.0 * x + 8.0

  return f

def p20_interval ( ):

#*****************************************************************************80
#
## p20_interval() returns a starting interval for optimization for test 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 1.0
  b = 5.0

  return a, b

def p20_sol ( ):

#*****************************************************************************80
#
## p20_sol() returns an approximate minimizer for test 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 2.632993164465

  return x

def p20_title ( ):

#*****************************************************************************80
#
## p20_title() returns a title for test 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = x^3 - 3 * x^2 - 5 * x - 8'

  return title

def p21_f ( x ):

#*****************************************************************************80
#
## p21_f() evaluates the objective function for test 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + np.cos ( x ) + 0.1 * x

  return f

def p21_interval ( ):

#*****************************************************************************80
#
## p21_interval() returns a starting interval for optimization for test 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -0.9
  b =  6.2

  return a, b

def p21_sol ( ):

#*****************************************************************************80
#
## p21_sol() returns an approximate minimizer for test 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 3.041425240905

  return x

def p21_title ( ):

#*****************************************************************************80
#
## p21_title() returns a title for test 21.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + cos ( x ) + 0.1 * x'

  return title

def p22_f ( x ):

#*****************************************************************************80
#
## p22_f() evaluates the objective function for test 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 10.2 + ( np.abs ( x - 5 ) )**3

  return f

def p22_interval ( ):

#*****************************************************************************80
#
## p22_interval() returns a starting interval for optimization for test 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 3.0
  b = 7.8

  return a, b

def p22_sol ( ):

#*****************************************************************************80
#
## p22_sol() returns an approximate minimizer for test 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 5.0

  return x

def p22_title ( ):

#*****************************************************************************80
#
## p22_title() returns a title for test 22.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 10.2 + abs ( ( x - 5 )^3 )'

  return title

def p23_f ( x ):

#*****************************************************************************80
#
## p23_f() evaluates the objective function for test 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + np.log ( x ) * np.cos ( 2.0 * ( 4.0 - x ) )

  return f

def p23_interval ( ):

#*****************************************************************************80
#
## p23_interval() returns a starting interval for optimization for test 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 2.7
  b = 3.1

  return a, b

def p23_sol ( ):

#*****************************************************************************80
#
## p23_sol() returns an approximate minimizer for test 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 2.7

  return x

def p23_title ( ):

#*****************************************************************************80
#
## p23_title() returns a title for test 23.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + log ( x ) * cos ( 2 * ( 4 - x ) )'

  return title

def p24_f ( x ):

#*****************************************************************************80
#
## p24_f() evaluates the objective function for test 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + ( x - 7.4 )**2

  return f

def p24_interval ( ):

#*****************************************************************************80
#
## p24_interval() returns a starting interval for optimization for test 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a =  1.0
  b = 17.0

  return a, b

def p24_sol ( ):

#*****************************************************************************80
#
## p24_sol() returns an approximate minimizer for test 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 7.4

  return x

def p24_title ( ):

#*****************************************************************************80
#
## p24_title() returns a title for test 24.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + ( x - 7.4 )^2'

  return title

def p25_f ( x ):

#*****************************************************************************80
#
## p25_f() evaluates the objective function for test 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + np.exp ( 3.0 - x ) + 2.0 * ( x - 2.0 )

  return f

def p25_interval ( ):

#*****************************************************************************80
#
## p25_interval() returns a starting interval for optimization for test 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 1.0
  b = 4.0

  return a, b

def p25_sol ( ):

#*****************************************************************************80
#
## p25_sol() returns an approximate minimizer for test 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 2.306852798909

  return x

def p25_title ( ):

#*****************************************************************************80
#
## p25_title() returns a title for test 25.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + exp ( 3 - x ) + 4 * ( x - 2 )'

  return title

def p26_f ( x ):

#*****************************************************************************80
#
## p26_f() evaluates the objective function for test 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.5 + np.exp ( - 2.0 * ( x + 6.0 ) ) + 13.0 * np.sin ( x )

  return f

def p26_interval ( ):

#*****************************************************************************80
#
## p26_interval() returns a starting interval for optimization for test 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 2.0
  b = 6.5

  return a, b

def p26_sol ( ):

#*****************************************************************************80
#
## p26_sol() returns an approximate minimizer for test 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 4.712388970889

  return x

def p26_title ( ):

#*****************************************************************************80
#
## p26_title() returns a title for test 26.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.5 + exp ( - 2 * ( x + 6 ) ) + 13 * sin ( x )'

  return title

def p27_f ( x ):

#*****************************************************************************80
#
## p27_f() evaluates the objective function for test 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + np.sinh ( x ) - 2.0 * x

  return f

def p27_interval ( ):

#*****************************************************************************80
#
## p27_interval() returns a starting interval for optimization for test 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 0.6
  b = 2.7

  return a, b

def p27_sol ( ):

#*****************************************************************************80
#
## p27_sol() returns an approximate minimizer for test 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 1.316957893968

  return x

def p27_title ( ):

#*****************************************************************************80
#
## p27_title() returns a title for test 27.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + sinh ( x ) - 2 * x'

  return title

def p28_f ( x ):

#*****************************************************************************80
#
## p28_f() evaluates the objective function for test 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 12.2 + 10.0 * np.sin ( 19.0 * x - 2.0 )

  return f

def p28_interval ( ):

#*****************************************************************************80
#
## p28_interval() returns a starting interval for optimization for test 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 1.9
  b = 2.1

  return a, b

def p28_sol ( ):

#*****************************************************************************80
#
## p28_sol() returns an approximate minimizer for test 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 2.006753447676

  return x

def p28_title ( ):

#*****************************************************************************80
#
## p28_title() returns a title for test 28.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 12.2 + 10 * sin ( 19 * x - 2 )'

  return title

def p29_f ( x ):

#*****************************************************************************80
#
## p29_f() evaluates the objective function for test 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 2.2 + np.abs ( x - 8.0 )

  return f

def p29_interval ( ):

#*****************************************************************************80
#
## p29_interval() returns a starting interval for optimization for test 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -12.3
  b =   5.5

  return a, b

def p29_sol ( ):

#*****************************************************************************80
#
## p29_sol() returns an approximate minimizer for test 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 5.5

  return x

def p29_title ( ):

#*****************************************************************************80
#
## p29_title() returns a title for test 29.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 2.2 + abs ( x - 8 )'

  return title

def p30_f ( x ):

#*****************************************************************************80
#
## p30_f() evaluates the objective function for test 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + x - 5.0 * np.sin ( 2.0 * x )

  return f

def p30_interval ( ):

#*****************************************************************************80
#
## p30_interval() returns a starting interval for optimization for test 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -0.5
  b =  2.2

  return a, b

def p30_sol ( ):

#*****************************************************************************80
#
## p30_sol() returns an approximate minimizer for test 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 0.7353144479144

  return x

def p30_title ( ):

#*****************************************************************************80
#
## p30_title() returns a title for test 30.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + x - 5 * sin ( 2 * x )'

  return title

def p31_f ( x ):

#*****************************************************************************80
#
## p31_f() evaluates the objective function for test 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + np.sin ( 2.5 * np.sqrt ( np.abs ( x ) + x ) )

  return f

def p31_interval ( ):

#*****************************************************************************80
#
## p31_interval() returns a starting interval for optimization for test 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 1.4
  b = 3.0

  return a, b

def p31_sol ( ):

#*****************************************************************************80
#
## p31_sol() returns an approximate minimizer for test 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 1.776528787613

  return x

def p31_title ( ):

#*****************************************************************************80
#
## p31_title() returns a title for test 31.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + sin ( 2.5 * sqrt ( abs ( x ) + x ) )'

  return title

def p32_f ( x ):

#*****************************************************************************80
#
## p32_f() evaluates the objective function for test 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + np.maximum ( \
    20.0 * np.log ( x**2 + 3.0 ), \
    np.exp ( x - 2.5 ) + x - 1.0 )

  return f

def p32_interval ( ):

#*****************************************************************************80
#
## p32_interval() returns a starting interval for optimization for test 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -1.0
  b =  1.0

  return a, b

def p32_sol ( ):

#*****************************************************************************80
#
## p32_sol() returns an approximate minimizer for test 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 0.0

  return x

def p32_title ( ):

#*****************************************************************************80
#
## p32_title() returns a title for test 32.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + max ( 20 * log ( x^2 + 3 ), exp ( x - 2.5 ) + x - 1 )'

  return title

def p33_f ( x ):

#*****************************************************************************80
#
## p33_f() evaluates the objective function for test 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + 5.0 * x * ( x - 1.0 ) * np.exp ( x - 0.5 )

  return f

def p33_interval ( ):

#*****************************************************************************80
#
## p33_interval() returns a starting interval for optimization for test 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -1.2
  b =  1.2

  return a, b

def p33_sol ( ):

#*****************************************************************************80
#
## p33_sol() returns an approximate minimizer for test 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 0.6180339815403

  return x

def p33_title ( ):

#*****************************************************************************80
#
## p33_title() returns a title for test 33.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + 5 * x * ( x - 1 ) * exp ( x - 0.5 )'

  return title

def p34_f ( x ):

#*****************************************************************************80
#
## p34_f() evaluates the objective function for test 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 - 4.0 * x * np.sin ( x )

  return f

def p34_interval ( ):

#*****************************************************************************80
#
## p34_interval() returns a starting interval for optimization for test 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a =  0.3
  b =  4.5

  return a, b

def p34_sol ( ):

#*****************************************************************************80
#
## p34_sol() returns an approximate minimizer for test 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 2.028757837450

  return x

def p34_title ( ):

#*****************************************************************************80
#
## p34_title() returns a title for test 34.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 - 4 * x * sin ( x )'

  return title

def p35_f ( x ):

#*****************************************************************************80
#
## p35_f() evaluates the objective function for test 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + 3.0 * x**2 + ( x - 1.0 )**2

  return f

def p35_interval ( ):

#*****************************************************************************80
#
## p35_interval() returns a starting interval for optimization for test 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -13.5
  b =  15.0

  return a, b

def p35_sol ( ):

#*****************************************************************************80
#
## p35_sol() returns an approximate minimizer for test 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 0.25

  return x

def p35_title ( ):

#*****************************************************************************80
#
## p35_title() returns a title for test 35.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + 3 * x^4 + ( x - 1 )^2'

  return title

def p36_f ( x ):

#*****************************************************************************80
#
## p36_f() evaluates the objective function for test 36.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 1.2 + 3.0 * np.cos ( np.exp ( - 2.0 * x ) )

  return f

def p36_interval ( ):

#*****************************************************************************80
#
## p36_interval() returns a starting interval for optimization for test 36.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -0.8
  b =  2.1

  return a, b

def p36_sol ( ):

#*****************************************************************************80
#
## p36_sol() returns an approximate minimizer for test 36.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = -0.5723649442193

  return x

def p36_title ( ):

#*****************************************************************************80
#
## p36_title() returns a title for test 36.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 1.2 + 3 * cos ( exp ( - 2 * x ) ).'

  return title

def p37_f ( x ):

#*****************************************************************************80
#
## p37_f() evaluates the objective function for test 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 3.2 + 3.0 * np.cos ( x**3 + 2.4 )

  return f

def p37_interval ( ):

#*****************************************************************************80
#
## p37_interval() returns a starting interval for optimization for test 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 2.2
  b = 2.5

  return a, b

def p37_sol ( ):

#*****************************************************************************80
#
## p37_sol() returns an approximate minimizer for test 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 2.369757270627

  return x

def p37_title ( ):

#*****************************************************************************80
#
## p37_title() returns a title for test 37.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 3.2 + 3 * cos ( x^3 + 2.4 )'

  return title

def p38_f ( x ):

#*****************************************************************************80
#
## p38_f() evaluates the objective function for test 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = np.exp ( - x**2 ) + 2.0 * ( x**2 - x + 1.0 )**2

  return f

def p38_interval ( ):

#*****************************************************************************80
#
## p38_interval() returns a starting interval for optimization for test 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = -1.0
  b =  4.0

  return a, b

def p38_sol ( ):

#*****************************************************************************80
#
## p38_sol() returns an approximate minimizer for test 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 0.6380483150624

  return x

def p38_title ( ):

#*****************************************************************************80
#
## p38_title() returns a title for test 38.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = exp ( - x^2 ) + 2 * ( x^2 - x + 1 )^2'

  return title

def p39_f ( x ):

#*****************************************************************************80
#
## p39_f() evaluates the objective function for test 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = 25.0 * ( x - 1.0 ) \
    + np.maximum ( \
    - 2.0 * ( x - 1.0 ), \
      8.0 * ( x - 1.0 ) )

  return f

def p39_interval ( ):

#*****************************************************************************80
#
## p39_interval() returns a starting interval for optimization for test 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a =  0.0
  b =  2.5

  return a, b

def p39_sol ( ):

#*****************************************************************************80
#
## p39_sol() returns an approximate minimizer for test 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 0.0

  return x

def p39_title ( ):

#*****************************************************************************80
#
## p39_title() returns a title for test 39.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = 25 * ( x - 1 ) + max ( - 2 * ( x - 1 ), 8 * ( x - 1 ) )'

  return title

def p40_f ( x ):

#*****************************************************************************80
#
## p40_f() evaluates the objective function for test 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x: the argument.
#
#  Output:
#
#    real f: the function value.
#
  import numpy as np

  f = np.maximum ( \
    2.0 - x**2, \
    5.0 - ( x - 4.0 )**2 )

  return f

def p40_interval ( ):

#*****************************************************************************80
#
## p40_interval() returns a starting interval for optimization for test 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real A, B: the left and right endpoints of the interval.
#
  import numpy as np

  a = 1.0
  b = 3.8

  return a, b

def p40_sol ( ):

#*****************************************************************************80
#
## p40_sol() returns an approximate minimizer for test 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x: an approximate minimizer.
#
  x = 1.625

  return x

def p40_title ( ):

#*****************************************************************************80
#
## p40_title() returns a title for test 40.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string title: a title for the test.
#
  title = 'f(x) = max ( 2 - x^2, 5 - ( x - 4 )^2 )'

  return title

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
  test_uni_test ( )
  timestamp ( )
