#! /usr/bin/env python3
#
def hermite_integrands_test ( ):

#*****************************************************************************80
#
## hermite_integrands_test() tests hermite_integrands().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hermite_integrands_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hermite_integrands().' )

  hermite_integrands_test01 ( )
  hermite_integrands_test02 ( )
  hermite_integrands_test03 ( )
  hermite_integrands_test04 ( )
  hermite_integrands_test05 ( )
  hermite_integrands_test06 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hermite_integrands_test():' )
  print ( '  Normal end of execution.' )

  return

def hermite_compute ( order ):

#*****************************************************************************80
#
## hermite_compute() computes a Gauss-Hermite quadrature rule.
#
#  Discussion:
#
#    The abscissas are the zeros of the N-th order Hermite polynomial.
#
#    The integration interval is ( -oo, +oo ).
#
#    The weight function is w(x) = exp ( - x^2 )
#
#    The integral to approximate:
#
#      Integral ( -oo < X < +oo ) exp ( - X^2 ) * F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= ORDER ) WEIGHT(I) * F ( XTAB(I) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2025
#
#  Author:
#
#    Original FORTRAN77 version by Arthur Stroud, Don Secrest.
#    This version by John Burkardt.
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    integer ORDER, the order of the formula to be computed.
#
#  Output:
#
#    real XTAB(ORDER), the Gauss-Hermite abscissas.
#
#    real WEIGHT(ORDER), the Gauss-Hermite weights.
#
  from scipy.special import gamma
  import numpy as np

  xtab = np.zeros ( order )
  weight = np.zeros ( order )

  cc = 1.7724538509 * gamma ( order ) / ( 2.0**( order - 1 ) )

  s = ( 2.0 * order + 1.0 )**( 1.0 / 6.0 )

  ihi = ( order + 1 ) // 2

  for i in range ( 0, ihi ):

    if ( i == 0 ):

      x = s**3 - 1.85575 / s

    elif ( i == 1 ):

      x = x - 1.14 * ( ( order )**0.426 ) / x

    elif ( i == 2 ):

      x = 1.86 * x - 0.86 * xtab[0]

    elif ( i == 3 ):

      x = 1.91 * x - 0.91 * xtab[1]

    else:

      x = 2.0 * x - xtab[i-2]

    x, dp2, p1 = hermite_root ( x, order )

    xtab[i] = x
    weight[i] = ( cc / dp2 ) / p1

#   xtab[order-i+1] = - x
#   weight[order-i+1] = weight[i]

    xtab[order-1-i] = - x
    weight[order-1-i] = weight[i]
#
#  Reverse the order of the XTAB values.
#
  xtab = np.flip ( xtab )

  return xtab, weight

def hermite_integral ( n ):

#*****************************************************************************80
#
## hermite_integral() returns the value of a Hermite polynomial integral.
#
#  Discussion:
#
#    H(n) = Integral ( -oo < x < +oo ) x^n exp(-x^2) dx
#
#    H(n) is 0 for n odd.
#
#    H(n) = (n-1)!! * sqrt(pi) / 2^(n/2) for n even.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the integral.
#    0 <= N.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np
  import scipy as sp
  from scipy.special import factorial2

  if ( n < 0 ):

    value = - np.inf

  elif ( ( n % 2 ) == 1 ):

    value = 0.0

  else:

    value = factorial2 ( n - 1 ) * np.sqrt ( np.pi ) / 2.0 ** ( n / 2 )

  return value

def hermite_integrands_test01 ( ):

#*****************************************************************************80
#
## hermite_integrands_test01() tests p00_problem_num() and p00_title().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_integrands_test01()' )
  print ( '  p00_problem_num() returns the number of problems.' )
  print ( '  p00_title() returns the title of a problem.' )

  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '  P00_PROBLEM_NUM: number of problems is ', problem_num )
  print ( '' )
  print ( '   Problem       Title' )
  print ( '' )

  for problem in range ( 1, problem_num + 1 ):

    title = p00_title ( problem )

    print ( '  %8d  "%s"' % ( problem, title ) )

  return

def hermite_integrands_test02 ( ):

#*****************************************************************************80
#
## hermite_integrands_test02() tests p00_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hermite_integrands_test02()' )
  print ( '  p00_exact() returns the exact integral.' )

  problem_num = p00_problem_num ( )

  m = 4
  p06_parameters ( m )

  print ( '' )
  print ( '   Problem       EXACT' )
  print ( '' )

  for problem in range ( 1, problem_num + 1 ):

    exact = p00_exact ( problem )

    print ( '  %8d  %24.16f' % ( problem, exact ) )

  return

def hermite_integrands_test03 ( ):

#*****************************************************************************80
#
## hermite_integrands_test03() tests p00_gauss_hermite().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_integrands_test03():' )
  print ( '  p00_gauss_hermite() applies a Gauss-Hermite rule' )
  print ( '  to estimate an integral on (-oo,+oo).' )

  problem_num = p00_problem_num ( )

  m = 4
  p06_parameters ( m )

  print ( '' )
  print ( '   Problem     Order       Estimate    Exact    Error' )

  for problem in range ( 1, problem_num + 1 ):

    exact = p00_exact ( problem )

    order = 1

    print ( '' )

    for order_log in range ( 0, 7 ):

      estimate = p00_gauss_hermite ( problem, order )

      err = np.abs ( exact - estimate )

      print ( '  %8d  %8d  %14.6f  %14.6f  %14.6e'  \
        % ( problem, order, estimate, exact, err ) )

      order = order * 2

  return

def hermite_integrands_test04 ( ):

#*****************************************************************************80
#
## hermite_integrands_test04() tests p00_turing().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_integrands_test04():' )
  print ( '  p00_turing() applies a Turing procedure' )
  print ( '  to estimate an integral on (-oo,+oo).' )

  problem_num = p00_problem_num ( )

  m = 4
  p06_parameters ( m )

  for test in range ( 1, 3 ):

    if ( test == 1 ):
      tol = 1.0E-04
    elif ( test == 2 ):
      tol = 1.0E-07

    print ( '' )
    print ( '  Using a tolerance of TOL = ', tol )
    print ( '' )
    print ( '   Problem      H              N      Estimate    Exact    Error' )

    for problem in range ( 1, problem_num + 1 ):

      exact = p00_exact ( problem )

      h = 1.0

      print ( '' )

      for order_log in range ( 0, 7 ):

        n, estimate = p00_turing ( problem, h, tol )

        err = np.abs ( exact - estimate )

        print ( '  %8d  %10f  %8d  %14.6f  %14.6f  %14.6e' \
          % ( problem, h, 2*n+1, estimate, exact, err ) )

        h = h / 2.0

  return

def hermite_integrands_test05 ( ):

#*****************************************************************************80
#
## hermite_integrands_test05() tests p00_gauss_hermite() against the polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_integrands_test05():' )
  print ( '  p00_gauss_hermite() applies a Gauss-Hermite rule to' )
  print ( '  estimate the integral x^m exp(-x*x) over (-oo,+oo).' )

  problem = 6

  print ( '' )
  print ( '         M     Order      Estimate        Exact           Error' )

  for m in range ( 0, 7 ):

    p06_parameters ( m )

    exact = p00_exact ( problem )

    print ( '' )

    order_max = 3 + m // 2

    for order in range ( 1, order_max + 1 ):
 
      estimate = p00_gauss_hermite ( problem, order )

      error = np.abs ( exact - estimate )

      print ( '  %8d  %8d  %14f  %14f  %14f' \
        % ( m, order, estimate, exact, error ) )

  return

def hermite_integrands_test06 ( ):

#*****************************************************************************80
#
## hermite_integrands_test06() tests p00_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hermite_integrands_test06():' )
  print ( '  p00_monte_carlo() applies a weighted Monte Carlo rule' )
  print ( '  to estimate an integral on (-oo,+oo).' )

  problem_num = p00_problem_num ( )

  m = 4
  p06_parameters ( m )

  print ( '' )
  print ( '   Problem     Order       Estimate    Exact    Error' )

  for problem in range ( 1, problem_num + 1 ):

    exact = p00_exact ( problem )

    order = 128

    print ( '' )

    for order_log in range ( 0, 7 ):

      estimate = p00_monte_carlo ( problem, order )

      err = np.abs ( exact - estimate )

      print ( '  %8d  %8d  %14.6f  %14.6f  %14.6e' \
        % ( problem, order, estimate, exact, err ) )

      order = order * 4

  return

def hermite_recur ( x, norder ):

#*****************************************************************************80
#
## hermite_recur() finds the value and derivative of a Hermite polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    Original FORTRAN77 version by Arthur Stroud, Don Secrest
#    This version by John Burkardt
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    real X, the point at which polynomials are evaluated.
#
#    integer NORDER, the order of the polynomial to be computed.
#
#  Output:
#
#    P2, the value of H(NORDER)(X).
#
#    DP2, the value of H'(NORDER)(X).
#
#    P1, the value of H(NORDER-1)(X).
#
  p1 = 1.0
  dp1 = 0.0

  p2 = x
  dp2 = 1.0

  for i in range ( 2, norder + 1 ):

    p0 = p1
    dp0 = dp1

    p1 = p2
    dp1 = dp2

    p2  = x * p1 - 0.5 * ( i - 1.0 ) * p0
    dp2 = x * dp1 + p1 - 0.5 * ( i - 1.0 ) * dp0

  return p2, dp2, p1

def hermite_root ( x, norder ):

#*****************************************************************************80
#
## hermite_root() improves an approximate root of a Hermite polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    Original FORTRAN77 version by Arthur Stroud, Don Secrest
#    This version by John Burkardt
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    real X, the approximate root.
#
#    integer NORDER, the order of the Hermite polynomial.
#
#  Output:
#
#    real X, an improved estimate of the approximate root.
#
#    real DP2, the value of H'(NORDER)(X).
#
#    real P1, the value of H(NORDER-1)(X).
#
  import numpy as np

  eps = 1.0E-12
  maxstep = 10

  for i in range ( 1, maxstep + 1 ):

    p2, dp2, p1 = hermite_recur ( x, norder )

    d = p2 / dp2
    x = x - d

    if ( np.abs ( d ) <= eps * ( np.abs ( x ) + 1.0 ) ):
      break

  return x, dp2, p1

def p00_exact ( problem ):

#*****************************************************************************80
#
## p00_exact() returns the exact integral for any problem.
#
#  Discussion:
#
#    This routine provides a "generic" interface to the exact integral
#    routines for the various problems, and allows a problem to be called
#    by index (PROBLEM) rather than by name.
#
#    In most cases, the "exact" value of the integral is not given
#    instead a "respectable" approximation is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the index of the problem.
#
#  Output:
#
#    real EXACT, the exact value of the integral.
#
  if ( problem == 1 ):
    exact = p01_exact ( )
  elif ( problem == 2 ):
    exact = p02_exact ( )
  elif ( problem == 3 ):
    exact = p03_exact ( )
  elif ( problem == 4 ):
    exact = p04_exact ( )
  elif ( problem == 5 ):
    exact = p05_exact ( )
  elif ( problem == 6 ):
    exact = p06_exact ( )
  elif ( problem == 7 ):
    exact = p07_exact ( )
  elif ( problem == 8 ):
    exact = p08_exact ( )
  else:
    print ( '' )
    print ( 'p00_exact(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'p00_exact(): Fatal error!' )

  return exact

def p00_fun ( problem, option, n, x ):

#*****************************************************************************80
#
## p00_fun() evaluates the integrand for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the index of the problem.
#
#    integer OPTION:
#    0, integrand is f(x).
#    1, integrand is exp(-x*x) * f(x)
#    2, integrand is exp(-x*x/2) * f(x)
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  if ( problem == 1 ):
    f = p01_fun ( option, n, x )
  elif ( problem == 2 ):
    f = p02_fun ( option, n, x )
  elif ( problem == 3 ):
    f = p03_fun ( option, n, x )
  elif ( problem == 4 ):
    f = p04_fun ( option, n, x )
  elif ( problem == 5 ):
    f = p05_fun ( option, n, x )
  elif ( problem == 6 ):
    f = p06_fun ( option, n, x )
  elif ( problem == 7 ):
    f = p07_fun ( option, n, x )
  elif ( problem == 8 ):
    f = p08_fun ( option, n, x )
  else:
    print ( '' )
    print ( 'p00_fun(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'p00_fun(): Fatal error!' )

  return f

def p00_gauss_hermite ( problem, order ):

#*****************************************************************************80
#
## p00_gauss_hermite() applies a Gauss-Hermite quadrature rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the index of the problem.
#
#    integer ORDER, the order of the Gauss-Laguerre rule
#    to apply.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  import numpy as np

  xtab, weight = hermite_compute ( order )

  option = 1
  f_vec = p00_fun ( problem, option, order, xtab )

  result = np.dot ( weight, f_vec )

  return result

def p00_monte_carlo ( problem, order ):

#*****************************************************************************80
#
## p00_monte_carlo() applies a Monte Carlo procedure to Hermite integrals.
#
#  Discussion:
#
#    We wish to estimate the integral:
#
#      I(f) = integral ( -oo < x < +oo ) f(x) exp ( - x * x ) dx
#
#    We do this by a Monte Carlo sampling procedure, in which
#    we select N points X(1:N) from a standard normal distribution,
#    and estimate
#
#      Q(f) = sum ( 1 <= I <= N ) f(x(i)) / sqrt ( pi )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the index of the problem.
#
#    integer ORDER, the order of the Gauss-Laguerre rule
#    to apply.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  import numpy as np
  from numpy.random import default_rng

  rng = default_rng ( )

  x_vec = rng.standard_normal ( size = order )

  option = 2
  f_vec = p00_fun ( problem, option, order, x_vec )

  weight = order / np.sqrt ( 2.0 * np.pi )

  result = np.sum ( f_vec ) / weight

  return result

def p00_problem_num ( ):

#*****************************************************************************80
#
## p00_problem_num() returns the number of test integration problems.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer PROBLEM_NUM, the number of test problems.
#
  problem_num = 8

  return problem_num

def p00_title ( problem ):

#*****************************************************************************80
#
## p00_title() returns the title for any problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer PROBLEM, the index of the problem.
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  if ( problem == 1 ):
    title = p01_title ( )
  elif ( problem == 2 ):
    title = p02_title ( )
  elif ( problem == 3 ):
    title = p03_title ( )
  elif ( problem == 4 ):
    title = p04_title ( )
  elif ( problem == 5 ):
    title = p05_title ( )
  elif ( problem == 6 ):
    title = p06_title ( )
  elif ( problem == 7 ):
    title = p07_title ( )
  elif ( problem == 8 ):
    title = p08_title ( )
  else:
    print ( '' )
    print ( 'P00_TITLE(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'P00_TITLE(): Fatal error!' )

  return title

def p00_turing ( problem, h, tol ):

#*****************************************************************************80
#
## p00_turing() applies the Turing quadrature rule.
#
#  Discussion:
#
#    We consider the approximation:
#
#      Integral ( -oo < x < +oo ) f(x) dx
#
#      = h * Sum ( -oo < i < +oo ) f(nh) + error term
#
#    Given H and a tolerance TOL, we start summing at I = 0, and
#    adding one more term in the positive and negative I directions,
#    until the absolute value of the next two terms being added
#    is less than TOL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Turing,
#    A Method for the Calculation of the Zeta Function,
#    Proceedings of the London Mathematical Society,
#    Volume 48, 1943, pages 180-197.
#
#  Input:
#
#    integer PROBLEM, the index of the problem.
#
#    real H, the spacing to use.
#
#    real TOL, the tolerance.
#
#  Output:
#
#    integer N, the number of pairs of steps taken.
#    The actual number of function evaluations is 2*N+1.
#
#    real RESULT, the approximate integral.
#
  import numpy as np

  n_too_many = 100000

  option = 0
  n = 0

  result = 0.0
  order = 1
  xtab = np.zeros ( order )
  f_vec = p00_fun ( problem, option, order, xtab )
  result = result + h * f_vec[0]

  order = 2
  xtab = np.zeros ( order )

  while ( True ):

    n = n + 1

    xtab[0] =   n * h
    xtab[1] = - n * h

    f_vec = p00_fun ( problem, option, order, xtab )

    result = result + h * ( f_vec[0] + f_vec[1] )
#
#  Just do a simple-minded absolute error tolerance check to start with.
#
    if ( np.abs ( f_vec[0] ) + np.abs ( f_vec[1] ) <= tol ):
      break
#
#  Just in case things go crazy.
#
    if ( n_too_many <= n ):
      print ( '' )
      print ( 'P00_TURING(): Warning!' )
      print ( '  Number of steps exceeded N_TOO_MANY = ', n_too_many )
      break

  return n, result

def p01_exact ( ):

#*****************************************************************************80
#
## p01_exact() returns the exact integral for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  omega = 1.0

  exact = np.sqrt ( np.pi ) * np.exp ( - omega * omega )

  return exact

def p01_fun ( option, n, x ):

#*****************************************************************************80
#
## p01_fun() evaluates the integrand for problem 1.
#
#  Discussion:
#
#    Squire gives exact value as sqrt(pi) * exp(-w*w).
#
#    Integral ( -oo < x < oo ) exp(-x*x) cos(2*w*x) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Squire,
#    Comparison of Gauss-Hermite and Midpoint Quadrature with Application
#    to the Voigt Function,
#    in Numerical Integration:
#    Recent Developments, Software and Applications,
#    edited by Patrick Keast, Graeme Fairweather,
#    Reidel, 1987, pages 337-340,
#    ISBN: 9027725144,
#    LC: QA299.3.N38.
#
#  Input:
#
#    integer OPTION:
#    0, integrand is f(x).
#    1, integrand is exp(-x*x) * f(x)
#    2, integrand is exp(-x*x/2) * f(x)
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  omega = 1.0

  f = np.cos ( 2.0 * omega * x )

  if ( option == 0 ):
    f = f * np.exp ( - x**2 )
  elif ( option == 1 ):
    pass
  elif ( option == 2 ):
    f = f * np.exp ( - 0.5 * x**2 )

  return f

def p01_title ( ):

#*****************************************************************************80
#
## p01_title() returns the title for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'exp(-x*x) * cos(2*omega*x)'

  return title

def p02_exact ( ):

#*****************************************************************************80
#
## p02_exact() returns the exact integral for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = np.sqrt ( np.pi )

  return exact

def p02_fun ( option, n, x ):

#*****************************************************************************80
#
## p02_fun() evaluates the integrand for problem 2.
#
#  Discussion:
#
#    The exact value is sqrt(pi).
#
#    Integral ( -oo < x < +oo ) exp(-x*x) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer OPTION:
#    0, integrand is f(x).
#    1, integrand is exp(-x*x) * f(x)
#    2, integrand is exp(-x*x/2) * f(x)
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.ones ( n )

  if ( option == 0 ):
    f = f * np.exp ( - x**2 )
  elif ( option == 1 ):
    pass
  elif ( option == 2 ):
    f = f * np.exp ( - 0.5 * x**2 )

  return f

def p02_title ( ):

#*****************************************************************************80
#
## p02_title() returns the title for problem 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'exp(-x*x)'

  return title

def p03_exact ( ):

#*****************************************************************************80
#
## p03_exact() returns the exact integral for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  p = 1.0
  q = 3.0

  exact = np.pi / ( q * np.sin ( np.pi * p / q ) )

  return exact

def p03_fun ( option, n, x ):

#*****************************************************************************80
#
## p03_fun() evaluates the integrand for problem 3.
#
#  Discussion:
#
#    The exact value is pi / (q*sin(pi*p/q) ), assuming 0 < p < q.
#
#    Integral ( -oo < x < +oo ) exp(-px) / ( 1 + exp ( -qx) ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer OPTION:
#    0, integrand is f(x).
#    1, integrand is exp(-x*x) * f(x)
#    2, integrand is exp(-x*x/2) * f(x)
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  p = 1.0
  q = 3.0

  f = np.exp ( - p * x ) / ( 1.0 + np.exp ( - q * x ) )

  if ( option == 0 ):
    pass
  elif ( option == 1 ):
    f = f * np.exp ( x**2 )
  elif ( option == 2 ):
    f = f * np.exp ( 0.5 * x**2 )

  return f

def p03_title ( ):

#*****************************************************************************80
#
## p03_title() returns the title for problem 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'exp(-px) / ( 1 + exp(-qx) )'

  return title

def p04_exact ( ):

#*****************************************************************************80
#
## p04_exact() returns the exact integral for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = np.sqrt ( np.pi / 2.0 )

  return exact

def p04_fun ( option, n, x ):

#*****************************************************************************80
#
## p04_fun() evaluates the integrand for problem 4.
#
#  Discussion:
#
#    The exact value is sqrt ( pi / 2 )
#
#    Integral ( -oo < x < +oo ) sin ( x^2 ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer OPTION:
#    0, integrand is f(x).
#    1, integrand is exp(-x*x) * f(x)
#    2, integrand is exp(-x*x/2) * f(x)
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.sin ( x**2 )

  if ( option == 0 ):
    pass
  elif ( option == 1 ):
    f = f * np.exp ( x**2 )
  elif ( option == 2 ):
    f = f * np.exp ( 0.5 * x**2 )

  return f

def p04_title ( ):

#*****************************************************************************80
#
## p04_title() returns the title for problem 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'sin(x^2)'

  return title

def p05_exact ( ):

#*****************************************************************************80
#
## p05_exact() returns the exact integral for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = np.pi / 3.0

  return exact

def p05_fun ( option, n, x ):

#*****************************************************************************80
#
## p05_fun() evaluates the integrand for problem 5.
#
#  Discussion:
#
#    The exact value is pi / 3.
#
#    Integral ( -oo < x < +oo ) dx / ( (1+x^2) sqrt(4+3x^2) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer OPTION:
#    0, integrand is f(x).
#    1, integrand is exp(-x*x) * f(x)
#    2, integrand is exp(-x*x/2) * f(x)
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = 1.0 / ( ( 1.0 + x**2 ) * np.sqrt ( 4.0 + 3.0 * x**2 ) )

  if ( option == 0 ):
    pass
  elif ( option == 1 ):
    f = f * np.exp ( x**2 )
  elif ( option == 2 ):
    f = f * np.exp ( 0.5 * x**2 )

  return f

def p05_title ( ):

#*****************************************************************************80
#
## p05_title() returns the title for problem 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = '1/( (1+x^2) sqrt(4+3x^2) )'

  return title

def p06_exact ( ):

#*****************************************************************************80
#
## p06_exact() returns the exact integral for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np
  import scipy as sp
  from scipy.special import factorial2

  m = p06_parameters ( )

  if ( m <= -1 ):

    exact = - np.inf

  elif ( ( m % 2 ) == 1 ):

    exact = 0.0

  else:

    exact = factorial2 ( m - 1 ) * np.sqrt ( np.pi ) / 2.0 ** ( m / 2 )

  return exact

def p06_fun ( option, n, x ):

#*****************************************************************************80
#
## p06_fun() evaluates the integrand for problem 6.
#
#  Discussion:
#
#    The exact value is (m-1)!! * sqrt ( pi ) / sqrt ( 2^m ).
#
#    Integral ( -oo < x < +oo ) x^m exp (-x*x) dx
#
#    The parameter M is set by calling P06_PARAM.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer OPTION:
#    0, integrand is f(x).
#    1, integrand is exp(-x*x) * f(x)
#    2, integrand is exp(-x*x/2) * f(x)
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  m = p06_parameters ( )

  f = x**m

  if ( option == 0 ):
    f = f * np.exp ( - x**2 )
  elif ( option == 1 ):
    pass
  elif ( option == 2 ):
    f = f * np.exp ( - 0.5 * x**2 )

  return f

def p06_parameters ( m_user = None ):

#*****************************************************************************80
#
## p06_param() gets or sets parameters for problem 6.
#
#  Discussion:
#
#    The parameter is named "M", and it represents the value of the exponent
#    in the integrand function:
#
#    Integral ( -oo < x < +oo ) x^m exp (-x*x) dx
#
#    M must be greater than -1.
#
#    The default value is m = 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M_USER: if supplied, a new value for the parameter.
#
#  Output:
#
#    integer M: the current value of the parameter.
#
#
#  Initialize defaults.
#
  if not hasattr ( p06_parameters, "m_default" ):
    p06_parameters.m_default = 0
#
#  Update defaults if input was supplied.
#
  if ( m_user is not None ):
    p06_parameters.m_default = m_user
#
#  Return values.
#
  m = p06_parameters.m_default

  return m

def p06_title ( ):

#*****************************************************************************80
#
## p06_title() returns the title for problem 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'x^m exp(-x*x)'

  return title

def p07_exact ( ):

#*****************************************************************************80
#
## p07_exact() returns the exact integral for problem 7.
#
#  Discussion:
#
#    The 20 digit values of pi^(1/2) and e^(1/4) were computed by Mathematica.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  exact = 0.25 * np.sqrt ( np.pi ) / np.sqrt ( np.sqrt ( np.e ) )

  return exact

def p07_fun ( option, n, x ):

#*****************************************************************************80
#
## p07_fun() evaluates the integrand for problem 7.
#
#  Discussion:
#
#    The exact value is (1/4) sqrt(pi) / sqrt(sqrt(e)).
#
#    Integral ( -oo < x < +oo ) x^2 cos(x) e^(-x^2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Prem Kythe, Michael Schaeferkotter,
#    Handbook of Computational Methods for Integration,
#    Chapman and Hall, 2004,
#    ISBN: 1-58488-428-2,
#    LC: QA299.3.K98.
#
#  Input:
#
#    integer OPTION:
#    0, integrand is f(x).
#    1, integrand is exp(-x*x) * f(x)
#    2, integrand is exp(-x*x/2) * f(x)
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  if ( option == 0 ):
    f = x**2 * np.cos ( x ) * np.exp ( - x**2 )
  elif ( option == 1 ):
    f = x**2 * np.cos ( x )
  elif ( option == 2 ):
    f = x**2 * np.cos ( x ) * np.exp ( - x**2 / 2.0 )

  return f

def p07_title ( ):

#*****************************************************************************80
#
## p07_title() returns the title for problem 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'x^2 cos ( x ) exp(-x*x)'

  return title

def p08_exact ( ):

#*****************************************************************************80
#
## p08_exact() returns the exact integral for problem 8.
#
#  Discussion:
#
#    The 20 digit value of the answer was computed by Mathematica.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 3.0088235661136433510

  return exact

def p08_fun ( option, n, x ):

#*****************************************************************************80
#
## p08_fun() evaluates the integrand for problem 8.
#
#  Discussion:
#
#    The exact value is sqrt ( 2 pi ) * HypergeometricU ( -1/2, 0, 1 ).
#
#    Integral ( -oo < x < +oo ) sqrt(1+x*x/2) * exp(-x*x/2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Prem Kythe, Michael Schaeferkotter,
#    Handbook of Computational Methods for Integration,
#    Chapman and Hall, 2004,
#    ISBN: 1-58488-428-2,
#    LC: QA299.3.K98.
#
#  Input:
#
#    integer OPTION:
#    0, integrand is f(x).
#    1, integrand is exp(-x*x) * f(x)
#    2, integrand is exp(-x*x/2) * f(x)
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real F(N), the function values.
#
  import numpy as np

  f = np.sqrt ( 1.0 + 0.5 * x**2 )

  if ( option == 0 ):
    f = f * np.exp ( - 0.5 * x**2 )
  elif ( option == 1 ):
    f = f * np.exp ( + 0.5 * x**2 )
  elif ( option == 2 ):
    pass

  return f

def p08_title ( ):

#*****************************************************************************80
#
## p08_title() returns the title for problem 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'sqrt(1+x*x/2) * exp(-x*x/2)'

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
  hermite_integrands_test ( )
  timestamp ( )

