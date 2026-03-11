#! /usr/bin/env python3
#
def laguerre_integrands_test ( ):

#*****************************************************************************80
#
## laguerre_integrands_test() tests laguerre_integrands().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'laguerre_integrands_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test laguerre_integrands().' )

  laguerre_integrands_test01 ( )
  laguerre_integrands_test02 ( )
  laguerre_integrands_test03 ( )
  laguerre_integrands_test04 ( )
  laguerre_integrands_test05 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'laguerre_integrands_test():' )
  print ( '  Normal end of execution.' )

  return

def laguerre_compute ( norder, alpha ):

#*****************************************************************************80
#
## laguerre_compute() computes a Gauss-Laguerre quadrature rule.
#
#  Discussion:
#
#    In the simplest case, ALPHA is 0, and we are approximating the
#    integral from 0 to +oo of EXP(-X) * F(X).  When this is so,
#    it is easy to modify the rule to approximate the integral from
#    A to +oo as well.
#
#    If ALPHA is nonzero, then there is no simple way to extend the
#    rule to approximate the integral from A to +oo.  The simplest
#    procedures would be to approximate the integral from 0 to A.
#
#    The integration interval is [ A, +oo ) or [ 0, +oo ).
#
#    The weight function w(x) = EXP ( - X ) or EXP ( - X ) * X^ALPHA.
#
#
#    If the integral to approximate is:
#
#        Integral ( A <= X < +oo ) EXP ( - X ) * F(X) dX
#      or
#        Integral ( 0 <= X < +oo ) EXP ( - X ) * X^ALPHA * F(X) dX
#
#    then the quadrature rule is:
#
#      EXP ( - A ) * Sum ( 1 <= I <= ORDER ) WEIGHT(I) * F ( A+XTAB(I) )
#    or
#      sum ( 1 <= I <= ORDER ) WEIGHT(I) * F ( XTAB(I) )
#
#
#    If the integral to approximate is:
#
#        Integral ( A <= X < +oo ) F(X) dX
#      or
#        Integral ( 0 <= X < +oo ) X^ALPHA * F(X) dX
#
#    then the quadrature rule is:
#
#      EXP ( - A ) * sum ( 1 <= I <= ORDER ) 
#        WEIGHT(I) * EXP(A+XTAB(I)) * F ( A+XTAB(I) )
#    or
#      sum ( 1 <= I <= ORDER ) WEIGHT(I) * EXP(XTAB(I)) * F ( XTAB(I) )
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
#    integer NORDER, the order of the quadrature rule to be computed.
#    NORDER must be at least 1.
#
#    real ALPHA, the exponent of the X factor.
#    Set ALPHA = 0.0 for the simplest rule.
#    ALPHA must be nonnegative.
#
#  Output:
#
#    real XTAB(NORDER), the Gauss-Laguerre abscissas.
#
#    real WEIGHT(NORDER), the Gauss-Laguerre weights.
#
  from scipy.special import gamma
  import numpy as np
#
#  Set the recursion coefficients.
#
  b = np.zeros ( norder )
  for i in range ( 0, norder ):
    b[i] = ( alpha + 2 * i + 1 )

  c = np.zeros ( norder )
  for i in range ( 0, norder ):
    c[i] = i * ( alpha + i )

  cc = gamma ( alpha + 1.0 ) * np.prod ( c[1:norder] )

  xtab = np.zeros ( norder )
  weight = np.zeros ( norder )

  for i in range ( 0, norder ):
#
#  Compute an estimate for the root.
#
    if ( i == 0 ):

      x = ( 1.0 + alpha ) * ( 3.0 + 0.92 * alpha ) \
        / ( 1.0 + 2.4 * norder + 1.8 * alpha )

    elif ( i == 1 ):

      x = x + ( 15.0 + 6.25 * alpha ) \
        / ( 1.0 + 0.9 * alpha + 2.5 * norder )

    else:

      r1 = ( 1.0 + 2.55 * ( i - 1 ) ) / ( 1.9 * ( i - 1 ) )

      r2 = 1.26 * ( i - 1 ) * alpha / ( 1.0 + 3.5 * ( i - 1 ) )

      ratio = ( r1 + r2 ) / ( 1.0 + 0.3 * alpha )

      x = x + ratio * ( x - xtab[i-2] )
#
#  Use iteration to find the root.
#
    x, dp2, p1 = laguerre_root ( x, norder, alpha, b, c )
#
#  Set the abscissa and weight.
#
    xtab[i] = x
    weight[i] = ( cc / dp2 ) / p1

  return xtab, weight

def laguerre_integrands_test01 ( ):

#*****************************************************************************80
#
## laguerre_integrands_test01() tests p00_problem_num() and p00_title().
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
  print ( '' )
  print ( 'laguerre_integrands_test01():' )
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

def laguerre_integrands_test02 ( ):

#*****************************************************************************80
#
## laguerre_integrands_test02() tests p00_alpha() and p00_exact().
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
  print ( '' )
  print ( 'laguerre_integrands_test02():' )
  print ( '  p00_alpha() returns the lower limit of integration.' )
  print ( '  p00_exact() returns the "exact" integral.' )

  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '   Problem       ALPHA           EXACT' )
  print ( '' )

  for problem in range ( 1, problem_num + 1 ):

    alpha = p00_alpha ( problem )

    exact = p00_exact ( problem )

    print ( '  %8d  %14f  %24.16f' % ( problem, alpha, exact ) )

  return

def laguerre_integrands_test03 ( ):

#*****************************************************************************80
#
## laguerre_integrands_test03() tests p00_gauss_laguerre().
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
  import numpy as np

  print ( '' )
  print ( 'laguerre_integrands_test03():' )
  print ( '  p00_gauss_laguerre() applies a Gauss-Laguerre rule' )
  print ( '  to estimate an integral on [ALPHA,+oo).' )

  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '                           Exact' )
  print ( '   Problem     Order       Estimate    Error' )

  for problem in range ( 1, problem_num + 1 ):

    exact = p00_exact ( problem )

    order = 1

    print ( '' )
    print ( '  %8d            %14.6f' % ( problem, exact ) )

    for order_log in range ( 0, 7 ):

      estimate = p00_gauss_laguerre ( problem, order )

      err = np.abs ( exact - estimate )

      print ( '            %8d  %14.6f  %14.6e' % ( order, estimate, err ) )

      order = order * 2

  return

def laguerre_integrands_test04 ( ):

#*****************************************************************************80
#
## laguerre_integrands_test04() tests p00_exp_transform().
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
  import numpy as np

  print ( '' )
  print ( 'laguerre_integrands_test04():' )
  print ( '  p00_exp_transform() applies an exponential tranform' )
  print ( '  to estimate an integral on [ALPHA,+oo)' )
  print ( '  as a transformed integral on (0,exp(-ALPHA)]' )
  print ( '  and applying a Gauss-Legendre rule.' )

  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '                           Exact' )
  print ( '   Problem     Order       Estimate    Error' )

  for problem in range ( 1, problem_num + 1 ):

    exact = p00_exact ( problem )

    order = 1

    print ( '' )
    print ( '  %8d            %14.6f' % ( problem, exact ) )

    for order_log in range ( 0, 7 ):

      estimate = p00_exp_transform ( problem, order )

      err = np.abs ( exact - estimate )

      print ( '            %8d  %14.6f  %14.6e' % ( order, estimate, err ) )

      order = order * 2

  return

def laguerre_integrands_test05 ( ):

#*****************************************************************************80
#
## laguerre_integrands_test05() tests p00_rat_transform().
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
  import numpy as np

  print ( '' )
  print ( 'laguerre_integrands_test05():' )
  print ( '  p00_rat_transform() applies a rational tranform' )
  print ( '  to estimate an integral on [ALPHA,+oo)' )
  print ( '  as a transformed integral on (0,1/(1+ALPHA)]' )
  print ( '  and applying a Gauss-Legendre rule.' )

  problem_num = p00_problem_num ( )

  print ( '' )
  print ( '                           Exact' )
  print ( '   Problem     Order       Estimate    Error' )

  for problem in range ( 1, problem_num + 1 ):

    exact = p00_exact ( problem )

    order = 1

    print ( '' )
    print ( '  %8d            %14.6f' % ( problem, exact ) )

    for order_log in range ( 0, 7 ):

      estimate = p00_rat_transform ( problem, order )

      err = np.abs ( exact - estimate )

      print ( '            %8d  %14.6f  %14.6e' % ( order, estimate, err ) )

      order = order * 2

  return

def laguerre_recur ( x, norder, alpha, b, c ):

#*****************************************************************************80
#
## laguerre_recur() finds the value and derivative of a Laguerre polynomial.
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
#    real X, the point at which polynomials are evaluated.
#
#    integer NORDER, the order of the polynomial to be computed.
#
#    real ALPHA, the exponent of the X factor in the
#    integrand.
#
#    real B(NORDER), C(NORDER), the recursion coefficients.
#
#  Output:
#
#    real P2, the value of L(NORDER)(X).
#
#    real DP2, the value of L'(NORDER)(X).
#
#    real P1, the value of L(NORDER-1)(X).
#
  p1 = 1.0
  dp1 = 0.0

  p2 = x - alpha - 1.0
  dp2 = 1.0

  for i in range ( 1, norder ):

    p0 = p1
    dp0 = dp1

    p1 = p2
    dp1 = dp2

    p2  = ( x - b[i] ) * p1       - c[i] * p0
    dp2 = ( x - b[i] ) * dp1 + p1 - c[i] * dp0

  return p2, dp2, p1

def laguerre_root ( x, norder, alpha, b, c ):

#*****************************************************************************80
#
## laguerre_root() improves an approximate root of a Laguerre polynomial.
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
#    real X, the approximate root, which
#    should be improved on output.
#
#    integer NORDER, the order of the polynomial to be computed.
#
#    real ALPHA, the exponent of the X factor.
#
#    real B(NORDER), C(NORDER), the recursion coefficients.
#
#  Output:
#
#    real X, the approximate root, which
#    should be improved on output.
#
#    real DP2, the value of L'(NORDER)(X).
#
#    real P1, the value of L(NORDER-1)(X).
#
  import numpy as np

  maxstep = 10

  for i in range ( 0, maxstep ):

    p2, dp2, p1 = laguerre_recur ( x, norder, alpha, b, c )

    d = p2 / dp2
    x = x - d

    eps = 1.0e-10
    if ( np.abs ( d ) <= eps * ( np.abs ( x ) + 1.0 ) ):
      break

  return x, dp2, p1

def legendre_compute ( n ):

#*****************************************************************************80
#
## legendre_compute(): Gauss-Legendre quadrature by Davis-Rabinowitz method.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the order.
#    N must be greater than 0.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n < 1 ):
    print ( '' )
    print ( 'legendre_compute(): Fatal error!' )
    print ( '  Illegal value of N = ', n )
    raise Exception ( 'legendre_compute(): Fatal error!' )

  e1 = n * ( n + 1 )

  m = ( ( n + 1 ) // 2 )

  for i in range ( 1, m + 1 ):

    mp1mi = m + 1 - i

    t = float ( 4 * i - 1 ) * np.pi / float ( 4 * n + 2 )

    x0 = np.cos ( t ) \
      * ( 1.0 - ( 1.0 - 1.0 / float ( n ) ) / float ( 8 * n * n ) )

    pkm1 = 1.0
    pk = x0

    for k in range ( 2, n + 1 ):
      pkp1 = 2.0 * x0 * pk - pkm1 - ( x0 * pk - pkm1 ) / float ( k )
      pkm1 = pk
      pk = pkp1

    d1 = float ( n ) * ( pkm1 - x0 * pk )

    dpn = d1 / ( 1.0 - x0 * x0 )

    d2pn = ( 2.0 * x0 * dpn - e1 * pk ) / ( 1.0 - x0 * x0 )

    d3pn = ( 4.0 * x0 * d2pn + ( 2.0 - e1 ) * dpn ) / ( 1.0 - x0 * x0 )

    d4pn = ( 6.0 * x0 * d3pn + ( 6.0 - e1 ) * d2pn ) / ( 1.0 - x0 * x0 )

    u = pk / dpn
    v = d2pn / dpn
#
#  Initial approximation H:
#
    h = - u * ( 1.0 + 0.5 * u * ( v + u * ( v * v - d3pn / ( 3.0 * dpn ) ) ) )
#
#  Refine H using one step of Newton's method:
#
    p = pk + h * ( dpn + 0.5 * h * ( d2pn + h / 3.0 \
      * ( d3pn + 0.25 * h * d4pn ) ) )

    dp = dpn + h * ( d2pn + 0.5 * h * ( d3pn + h * d4pn / 3.0 ) )

    h = h - p / dp

    xtemp = x0 + h

    x[mp1mi-1] = xtemp

    fx = d1 - h * e1 * ( pk + 0.5 * h * ( dpn + h / 3.0 \
      * ( d2pn + 0.25 * h * ( d3pn + 0.2 * h * d4pn ) ) ) )

    w[mp1mi-1] = 2.0 * ( 1.0 - xtemp * xtemp ) / fx / fx

  if ( ( n % 2 ) == 1 ):
    x[0] = 0.0
#
#  Shift the data up.
#
  nmove = ( ( n + 1 ) // 2 )
  ncopy = n - nmove

  for i in range ( 1, nmove + 1 ):
    iback = n + 1 - i
    x[iback-1] = x[iback-ncopy-1]
    w[iback-1] = w[iback-ncopy-1]
#
#  Reflect values for the negative abscissas.
#
  for i in range ( 1, n - nmove + 1 ):
    x[i-1] = - x[n-i]
    w[i-1] =   w[n-i]

  return x, w

def p00_alpha ( problem ):

#*****************************************************************************80
#
## p00_alpha() returns the value of ALPHA for any problem.
#
#  Discussion:
#
#    ALPHA is the lower, finite limit of integration in the integral.
#
#    The typical or default value is 0.0.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  if ( problem == 1 ):
    alpha = p01_alpha ( )
  elif ( problem == 2 ):
    alpha = p02_alpha ( )
  elif ( problem == 3 ):
    alpha = p03_alpha ( )
  elif ( problem == 4 ):
    alpha = p04_alpha ( )
  elif ( problem == 5 ):
    alpha = p05_alpha ( )
  elif ( problem == 6 ):
    alpha = p06_alpha ( )
  elif ( problem == 7 ):
    alpha = p07_alpha ( )
  elif ( problem == 8 ):
    alpha = p08_alpha ( )
  elif ( problem == 9 ):
    alpha = p09_alpha ( )
  elif ( problem == 10 ):
    alpha = p10_alpha ( )
  elif ( problem == 11 ):
    alpha = p11_alpha ( )
  elif ( problem == 12 ):
    alpha = p12_alpha ( )
  elif ( problem == 13 ):
    alpha = p13_alpha ( )
  elif ( problem == 14 ):
    alpha = p14_alpha ( )
  elif ( problem == 15 ):
    alpha = p15_alpha ( )
  elif ( problem == 16 ):
    alpha = p16_alpha ( )
  elif ( problem == 17 ):
    alpha = p17_alpha ( )
  elif ( problem == 18 ):
    alpha = p18_alpha ( )
  elif ( problem == 19 ):
    alpha = p19_alpha ( )
  elif ( problem == 20 ):
    alpha = p20_alpha ( )
  else:
    print ( '' )
    print ( 'P00_ALPHA(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'P00_ALPHA(): Fatal error!' )
 
  return alpha

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
  elif ( problem == 9 ):
    exact = p09_exact ( )
  elif ( problem == 10 ):
    exact = p10_exact ( )
  elif ( problem == 11 ):
    exact = p11_exact ( )
  elif ( problem == 12 ):
    exact = p12_exact ( )
  elif ( problem == 13 ):
    exact = p13_exact ( )
  elif ( problem == 14 ):
    exact = p14_exact ( )
  elif ( problem == 15 ):
    exact = p15_exact ( )
  elif ( problem == 16 ):
    exact = p16_exact ( )
  elif ( problem == 17 ):
    exact = p17_exact ( )
  elif ( problem == 18 ):
    exact = p18_exact ( )
  elif ( problem == 19 ):
    exact = p19_exact ( )
  elif ( problem == 20 ):
    exact = p20_exact ( )
  else:
    print ( '' )
    print ( 'P00_EXACT(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'P00_EXACT(): Fatal error!' )

  return exact

def p00_exp_transform ( problem, order ):

#*****************************************************************************80
#
## p00_exp_transform() applies an exponential transform and Gauss-Legendre rule.
#
#  Discussion:
#
#    To approximate:
#
#      Integral ( alpha <= x < Infinity ) f(x) dx
#
#    Transform:
#
#      u = exp ( -x )
#      du = - exp ( -x ) dx
#
#      x = - log ( u )
#      dx = - du / u
#
#      x = alpha    => u = exp ( -alpha )
#      x = Infinity => u = 0
#
#    Transformed integral:
#
#      Integral ( 0 <= u <= exp ( -alpha ) ) f ( -log(u) ) du / u
#
#    We apply a Gauss-Legendre rule here, but we could easily use any rule
#    that avoids evaluation at U = 0.
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
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    integer PROBLEM, the index of the problem.
#
#    integer ORDER, the order of the Gauss-Legendre rule
#    to apply.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  import numpy as np

  alpha = p00_alpha ( problem )
#
#  Get the abscissas and weights for Gauss-Legendre quadrature.
#
  u, weight = legendre_compute ( order )
#
#  Modify the weights from [-1,1] to [0,exp(-alpha)].
#
  weight = np.exp ( - alpha ) * weight / 2.0
#
#  Linear transform of abscissas from [-1,1] to [0,exp(-alpha)].
#
  u = ( ( 1.0 + u ) * np.exp ( - alpha ) \
      + ( 1.0 - u ) * 0.0 )           \
      / ( 2.0              )
#
#  Define U_LOG = - log ( U )
#
  u_log = - np.log ( u )
#
#  Evaluate F ( -LOG(U) ).
#
  f_vec = p00_fun ( problem, order, u_log )
#
#  The integrand is F ( -LOG(U) ) / U
#
  f_vec = f_vec / u
#
#  Sum.
#
  result = np.dot ( weight, f_vec )

  return result

def p00_fun ( problem, n, x ):

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
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  if ( problem == 1 ):
    fx = p01_fun ( n, x )
  elif ( problem == 2 ):
    fx = p02_fun ( n, x )
  elif ( problem == 3 ):
    fx = p03_fun ( n, x )
  elif ( problem == 4 ):
    fx = p04_fun ( n, x )
  elif ( problem == 5 ):
    fx = p05_fun ( n, x )
  elif ( problem == 6 ):
    fx = p06_fun ( n, x )
  elif ( problem == 7 ):
    fx = p07_fun ( n, x )
  elif ( problem == 8 ):
    fx = p08_fun ( n, x )
  elif ( problem == 9 ):
    fx = p09_fun ( n, x )
  elif ( problem == 10 ):
    fx = p10_fun ( n, x )
  elif ( problem == 11 ):
    fx = p11_fun ( n, x )
  elif ( problem == 12 ):
    fx = p12_fun ( n, x )
  elif ( problem == 13 ):
    fx = p13_fun ( n, x )
  elif ( problem == 14 ):
    fx = p14_fun ( n, x )
  elif ( problem == 15 ):
    fx = p15_fun ( n, x )
  elif ( problem == 16 ):
    fx = p16_fun ( n, x )
  elif ( problem == 17 ):
    fx = p17_fun ( n, x )
  elif ( problem == 18 ):
    fx = p18_fun ( n, x )
  elif ( problem == 19 ):
    fx = p19_fun ( n, x )
  elif ( problem == 20 ):
    fx = p20_fun ( n, x )
  else:
    print ( '' )
    print ( 'P00_FUN(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'P00_FUN(): Fatal error!' )

  return fx

def p00_gauss_laguerre ( problem, order ):

#*****************************************************************************80
#
## p00_gauss_laguerre() applies a Gauss-Laguerre rule.
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

  alpha = p00_alpha ( problem )

  alpha2 = 0.0
  xtab, weight = laguerre_compute ( order, alpha2 )

  xtab = xtab + alpha

  f_vec = p00_fun ( problem, order, xtab )
#
#  The Gauss-Laguerre rule assumes a weight of EXP(-X).
#
#  We need to multiply each F(X) by EXP(X) to implicitly 
#  adjust for this weight.
#
  f_vec = f_vec * np.exp ( xtab )

  result = np.exp ( - alpha ) * np.dot ( weight, f_vec )

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer PROBLEM_NUM, the number of test problems.
#
  problem_num = 20

  return problem_num

def p00_rat_transform ( problem, order ):

#*****************************************************************************80
#
## p00_rat_transform() applies a rational transform and Gauss-Legendre rule.
#
#  Discussion:
#
#    To approximate:
#
#      Integral ( alpha <= x < Infinity ) f(x) dx
#
#    Transform:
#
#      u = 1 / ( 1 + x )
#      du = - dx / ( 1 + x )^2
#
#      x = ( 1 - u ) / u
#      dx = - du / u^2
#
#      x = alpha    => u = 1 / ( 1 + alpha )
#      x = Infinity => u = 0
#
#    Transformed integral:
#
#      Integral ( 0 < u <= 1 / ( 1 + alpha ) ) f ( ( 1 - u ) / u ) du / u^2
#
#    We apply a Gauss-Legendre rule here, but we could easily use any rule
#    that avoids evaluation at U = 0.
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
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    integer PROBLEM, the index of the problem.
#
#    integer ORDER, the order of the Gauss-Legendre rule
#    to apply.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  import numpy as np

  alpha = p00_alpha ( problem )
#
#  Get the abscissas and weights for Gauss-Legendre quadrature.
#
  u, weight = legendre_compute ( order )
#
#  Modify the weights from [-1,1] to [0,1/(1+alpha)].
#
  weight = weight / 2.0 / ( 1.0 + alpha )
#
#  Linear transform of abscissas from [-1,1] to [0,1/(1+alpha)].
#
  u = ( ( 1.0 + u ) / ( 1.0 + alpha ) \
      + ( 1.0 - u ) * 0.0 )           \
      / ( 2.0              )
#
#  Define U_RAT = ( 1 - U ) / U.
#
  u_rat = ( 1.0 - u ) / u
#
#  Evaluate F ( (1-U)/U ).
#
  f_vec = p00_fun ( problem, order, u_rat )
#
#  The integrand is F ( (1-U)/U ) / U^2
#
  f_vec = f_vec / u**2
#
#  Sum.
#
  result = np.dot ( weight, f_vec )

  return result

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
  elif ( problem == 9 ):
    title = p09_title ( )
  elif ( problem == 10 ):
    title = p10_title ( )
  elif ( problem == 11 ):
    title = p11_title ( )
  elif ( problem == 12 ):
    title = p12_title ( )
  elif ( problem == 13 ):
    title = p13_title ( )
  elif ( problem == 14 ):
    title = p14_title ( )
  elif ( problem == 15 ):
    title = p15_title ( )
  elif ( problem == 16 ):
    title = p16_title ( )
  elif ( problem == 17 ):
    title = p17_title ( )
  elif ( problem == 18 ):
    title = p18_title ( )
  elif ( problem == 19 ):
    title = p19_title ( )
  elif ( problem == 20 ):
    title = p20_title ( )
  else:
    print ( '' )
    print ( 'P00_TITLE(): Fatal error!' )
    print ( '  Illegal problem number = ', problem )
    raise Exception ( 'P00_TITLE(): Fatal error!' )

  return title

def p01_alpha ( ):

#*****************************************************************************80
#
## p01_alpha() returns ALPHA for problem 1.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 2.0

  return alpha

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 0.19524754198276439152

  return exact

def p01_fun ( n, x ):

#*****************************************************************************80
#
## p01_fun() evaluates the integrand for problem 1.
#
#  Discussion:
#
#    D&R gives "exact" value as 0.19524753...
#    Mathematica returns        0.19524754198276439152...
#    D&R gives Laguerre(16) as  0.16623627...
#
#  Integral:
#
#    exp ( -2 ) Integral ( 2 <= x < +oo ) 1 / ( x * log(x)^2 ) dx
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
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.exp ( -2.0 ) / ( x * np.log ( x )**2 )

  return fx

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = '1 / ( x * log(x)^2 )'

  return title

def p02_alpha ( ):

#*****************************************************************************80
#
## p02_alpha() returns ALPHA for problem 2.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 2.0

  return alpha

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 0.32510848278991335198

  return exact

def p02_fun ( n, x ):

#*****************************************************************************80
#
## p02_fun() evaluates the integrand for problem 2.
#
#  Discussion:
#
#    D&R gives "exact" value as 0.32510855...
#    Mathematica returns        0.32510848278991335198...
#    D&R gives Laguerre(16) as  0.19142399...
#
#  Integral:
#
#    exp ( -2 ) Integral ( 2 <= x < +oo ) 1 / ( x * log(x)^(3/2) ) dx
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
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.exp ( - 2.0 ) / ( x * np.sqrt ( np.log ( x )**3 ) )

  return fx

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = '1 / ( x * log(x)^(3/2) )'

  return title

def p03_alpha ( ):

#*****************************************************************************80
#
## p03_alpha() returns ALPHA for problem 3.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 2.0

  return alpha

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 13.628

  return exact

def p03_fun ( n, x ):

#*****************************************************************************80
#
## p03_fun() evaluates the integrand for problem 3.
#
#  Discussion:
#
#    D&R gives "exact" value as 13.628...
#    Mathematica returns        13.440045415012575106...
#    D&R gives Laguerre(16) as   0.44996932...
#
#  Integral:
#
#    exp ( -2 ) Integral ( 2 <= x < +oo ) 1 / ( x^1.01 ) dx
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
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.exp ( - 2.0 ) * 1.0 / x**1.01

  return fx

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = '1 / ( x^1.01 )'

  return title

def p04_alpha ( ):

#*****************************************************************************80
#
## p04_alpha() returns ALPHA for problem 4.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 2.0

  return alpha

def p04_exact ( ):

#*****************************************************************************80
#
## p04_exact() returns the estimated integral for problem 4.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = -0.0046848541335080643181

  return exact

def p04_fun ( n, x ):

#*****************************************************************************80
#
## p04_fun() evaluates the integrand for problem 4.
#
#  Discussion:
#
#    D&R gives "exact" value as -0.0046984...
#    Mathematica returns        -0.0046848541335080643181...
#    D&R gives Laguerre(16) as  -0.039258696...
#
#  Integral:
#
#    exp ( -2 ) Integral ( 2 <= x < +oo ) sin ( x ) / x dx
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
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.zeros_like ( x )

  nzer = np.where ( x != 0.0 )
  fx[nzer] = np.exp ( -2.0 ) * np.sin ( x[nzer] ) / x[nzer]
  zero = np.where ( x == 0.0 )
  fx[zero] = np.exp ( -2.0 )

  return fx

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Sine integral'

  return title

def p05_alpha ( ):

#*****************************************************************************80
#
## p05_alpha() returns ALPHA for problem 5.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 2.0

  return alpha

def p05_exact ( ):

#*****************************************************************************80
#
## p05_exact() returns the estimated integral for problem 5.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.0015897286158592328774

  return exact

def p05_fun ( n, x ):

#*****************************************************************************80
#
## p05_fun() evaluates the integrand for problem 5.
#
#  Discussion:
#
#    D&R gives "exact" value as  0.00158973
#    Mathematica returns         0.0015897286158592328774...
#    D&R gives Laguerre(16) as  -0.067859545...
#
#  Integral:
#
#    exp ( -2 ) Integral ( 2 <= x < +oo ) cos ( pi * x^2 / 2 ) dx
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
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.exp ( - 2.0 ) * np.cos ( 0.5 * np.pi * x**2 )

  return fx

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Fresnel integral'

  return title

def p06_alpha ( ):

#*****************************************************************************80
#
## p06_alpha() returns ALPHA for problem 6.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 2.0

  return alpha

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.00056103711148387120640

  return exact

def p06_fun ( n, x ):

#*****************************************************************************80
#
## p06_fun() evaluates the integrand for problem 6.
#
#  Discussion:
#
#    D&R gives "exact" value as 0.0005610371...
#    Mathematica returns        0.00056103711148387120640...
#    D&R gives Laguerre(16) as  0.00056100775...
#
#  Integral:
#
#    exp ( -2 ) Integral ( 2 <= x < +oo ) exp ( -x^2 ) dx
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
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.exp ( - 2.0 ) * np.exp ( - x**2 )

  return fx

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Complementary error function'

  return title

def p07_alpha ( ):

#*****************************************************************************80
#
## p07_alpha() returns ALPHA for problem 7.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 2.0

  return alpha

def p07_exact ( ):

#*****************************************************************************80
#
## p07_exact() returns the exact integral for problem 7.
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
#  Output:
#
#    real EXACT, the value of the integral.
#
  exact = 0.16266891

  return exact

def p07_fun ( n, x ):

#*****************************************************************************80
#
## p07_fun() evaluates the integrand for problem 7.
#
#  Discussion:
#
#    D&R gives "exact" value as 0.16266891...
#    Mathematica does not return a value.
#    D&R gives Laguerre(16) as  0.097083064...
#
#  Integral:
#
#    exp ( -2 ) Integral ( 2 <= x < +oo ) sin ( x - 1 ) dx
#      / sqrt ( x * ( x - 2 ) )
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
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.zeros_like ( x )

  ntwo = np.where ( ( x == 2.0 ) | ( x == 0.0 ) )
  fx[ntwo] = 0.0

  not2 = np.where ( ( x != 2.0 ) & ( x != 0.0 ) )
  fx[not2] = np.exp ( -2.0 ) \
        * np.sin ( x[not2] - 1.0 ) / np.sqrt ( x[not2] * ( x[not2] - 2.0 ) )

  return fx

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Bessel function'

  return title

def p08_alpha ( ):

#*****************************************************************************80
#
## p08_alpha() returns ALPHA for problem 8.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p08_exact ( ):

#*****************************************************************************80
#
## p08_exact() returns the estimated integral for problem 8.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  import numpy as np

  exact = np.pi * np.pi / 6.0

  return exact

def p08_fun ( n, x ):

#*****************************************************************************80
#
## p08_fun() evaluates the integrand for problem 8.
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) x / ( exp ( x ) - 1 ) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.zeros_like ( x )

  zero = np.where ( x == 0.0 )
  fx[zero] = 1.0
  nzer = np.where ( x != 0.0 )
  fx[nzer] = x[nzer] / ( np.exp ( x[nzer] ) - 1.0 )

  return fx

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
#    21 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Debye function'

  return title

def p09_alpha ( ):

#*****************************************************************************80
#
## p09_alpha() returns ALPHA for problem 9.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p09_exact ( ):

#*****************************************************************************80
#
## p09_exact() returns the estimated integral for problem 9.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 24.0

  return exact

def p09_fun ( n, x ):

#*****************************************************************************80
#
## p09_fun() evaluates the integrand for problem 9.
#
#  Discussion:
#
#    The integral is the definition of the Gamma function for
#    Z = 5, with exact value (Z-1)! = 24.
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) x^4 exp ( -x ) dx
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
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = x**4 * np.exp ( - x )

  return fx

def p09_title ( ):

#*****************************************************************************80
#
## p09_title() returns the title for problem 9.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'Gamma(Z=5) function'

  return title

def p10_alpha ( ):

#*****************************************************************************80
#
## p10_alpha() returns ALPHA for problem 10.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p10_exact ( ):

#*****************************************************************************80
#
## p10_exact() returns the estimated integral for problem 10.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  import numpy as np

  exact = np.pi / 2.0

  return exact

def p10_fun ( n, x ):

#*****************************************************************************80
#
## p10_fun() evaluates the integrand for problem 10.
#
#  Discussion:
#
#    S&S gives exact value as pi/2 = 1.5707963267948966192...
#    S&S gives Laguerre(16) as       1.5537377347...
#    S&S gives EXP_TRANSFORM(16) as  1.4293043007...
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) 1/(1+x*x) dx
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
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = 1.0 / ( 1.0 + x**2 )

  return fx

def p10_title ( ):

#*****************************************************************************80
#
## p10_title() returns the title for problem 10.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = '1/(1+x*x)'

  return title

def p11_alpha ( ):

#*****************************************************************************80
#
## p11_alpha() returns ALPHA for problem 11.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p11_exact ( ):

#*****************************************************************************80
#
## p11_exact() returns the estimated integral for problem 11.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  import numpy as np

  exact = np.pi

  return exact

def p11_fun ( n, x ):

#*****************************************************************************80
#
## p11_fun() evaluates the integrand for problem 11.
#
#  Discussion:
#
#    S&S gives exact value as pi =  3.1415926535897932385...
#    S&S gives Laguerre(16) as      2.6652685196...
#    S&S gives EXP_TRANSFORM(16) as 2.3629036166... 
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) 1/((1+x)*sqrt(x)) dx
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
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.zeros_like ( x )

  zero = np.where ( x == 0.0 )
  fx[zero] = 0.0

  nzer = np.where ( x != 0.0 )
  fx[nzer] = 1.0 / ( ( 1.0 + x[nzer] ) * np.sqrt ( x[nzer] ) )

  return fx

def p11_title ( ):

#*****************************************************************************80
#
## p11_title() returns the title for problem 11.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = '1 / ( (1+x) * sqrt(x) )'

  return title

def p12_alpha ( ):

#*****************************************************************************80
#
## p12_alpha() returns ALPHA for problem 12.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p12_exact ( ):

#*****************************************************************************80
#
## p12_exact() returns the estimated integral for problem 12.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 0.5

  return exact

def p12_fun ( n, x ):

#*****************************************************************************80
#
## p12_fun() evaluates the integrand for problem 12.
#
#  Discussion:
#
#    S&S gives exact value as pi =  0.5
#    S&S gives Laguerre(16) as      0.5000000000...
#    S&S gives EXP_TRANSFORM(16) as 0.5019065783... 
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) exp ( -x ) * cos ( x ) dx
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
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    Input, integer N, the number of points.
#
#    Input, real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.exp ( -x ) * np.cos ( x )

  return fx

def p12_title ( ):

#*****************************************************************************80
#
## p12_title() returns the title for problem 12.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'exp ( - x ) * cos ( x )'

  return title

def p13_alpha ( ):

#*****************************************************************************80
#
## p13_alpha() returns ALPHA for problem 13.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p13_exact ( ):

#*****************************************************************************80
#
## p13_exact() returns the estimated integral for problem 13.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  import numpy as np

  exact = np.pi / 2.0

  return exact

def p13_fun ( n, x ):

#*****************************************************************************80
#
## p13_fun() evaluates the integrand for problem 13.
#
#  Discussion:
#
#    S&S gives exact value as pi/2 = 1.5707963267948966192...
#    S&S gives Laguerre(16) as       1.4399523793...
#    S&S gives EXP_TRANSFORM(16) as  1.3045186595...
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) sin ( x ) dx / x
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
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.zeros_like ( x )

  zero = np.where ( x == 0.0 )
  fx[zero] = 0.0

  nzer = np.where ( x != 0.0 )
  fx[nzer] = np.sin ( x[nzer] ) / x[nzer]

  return fx

def p13_title ( ):

#*****************************************************************************80
#
## p13_title() returns the title for problem 13.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'sin(x) / x'

  return title

def p14_alpha ( ):

#*****************************************************************************80
#
## p14_alpha() returns ALPHA for problem 14.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p14_exact ( ):

#*****************************************************************************80
#
## p14_exact() returns the estimated integral for problem 14.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 1.0634618101722400407

  return exact

def p14_fun ( n, x ):

#*****************************************************************************80
#
## p14_fun() evaluates the integrand for problem 14.
#
#  Discussion:
#
#    S&S gives "exact" value as     1.0634618101...
#    Mathematica returns            1.0634618101722400407...
#    S&S gives Laguerre(16) as      1.0634713425...
#    S&S gives EXP_TRANSFORM(16) as 1.0634618101...
#
#    The FORTRAN version of this routine, compiled with G95, was getting 
#    a floating point exception when evaluating the integrand
#    and using a Laguerre rule of order 64.  So I have had to truncate
#    the evaluation of the exponential.
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) sin ( exp ( - x ) + exp ( - 4 x ) ) dx
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
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.sin ( np.exp ( - x ) + np.exp ( - 4.0 * x ) )

  return fx

def p14_title ( ):

#*****************************************************************************80
#
## p14_title() returns the title for problem 14.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'sin ( exp(-x) + exp(-4x) )'

  return title

def p15_alpha ( ):

#*****************************************************************************80
#
## p15_alpha() returns ALPHA for problem 15.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p15_exact ( ):

#*****************************************************************************80
#
## p15_exact() returns the estimated integral for problem 15.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  import numpy as np

  exact = - np.pi * np.log ( 10.0 ) / 20.0

  return exact

def p15_fun ( n, x ):

#*****************************************************************************80
#
## p15_fun() evaluates the integrand for problem 15.
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) log(x) / (1+100*x*x) dx
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
#  Reference:
#
#    Robert Piessens, Elise deDoncker-Kapenga, 
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983,
#    ISBN: 3540125531,
#    LC: QA299.3.Q36.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.log ( x ) / ( 1.0 + 100.0 * x**2 )

  return fx

def p15_title ( ):

#*****************************************************************************80
#
## p15_title() returns the title for problem 15.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'log(x) / ( 1 + 100 x^2 )'

  return title

def p16_alpha ( ):

#*****************************************************************************80
#
## p16_alpha() returns ALPHA for problem 16.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p16_exact ( ):

#*****************************************************************************80
#
## p16_exact() returns the estimated integral for problem 16.
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
#  Output:
#
#    real EXACT, the estimated value of the integral.
#
  exact = 1.0

  return exact

def p16_fun ( n, x ):

#*****************************************************************************80
#
## p16_fun() evaluates the integrand for problem 16.
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) cos ( pi * x / 2 ) / sqrt ( x ) dx
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
#  Reference:
#
#    Robert Piessens, Elise deDoncker-Kapenga, 
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983,
#    ISBN: 3540125531,
#    LC: QA299.3.Q36.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real FX(N), the function values.
#
  import numpy as np

  fx = np.cos ( np.pi * x / 2.0 ) / np.sqrt ( x )

  return fx

def p16_title ( ):

#*****************************************************************************80
#
## p16_title() returns the title for problem 16.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'cos(pi x / 2 ) / sqrt(x)'

  return title

def p17_alpha ( ):

#*****************************************************************************80
#
## p17_alpha() returns ALPHA for problem 17.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p17_exact ( ):

#*****************************************************************************80
#
## p17_exact() returns the exact integral for problem 17.
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
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  beta = 2.0

  exact = np.sqrt ( np.pi ) * np.cos ( 0.5 * np.arctan ( 2.0**beta ) ) \
    / np.sqrt ( np.sqrt ( 1.0 + 0.25**beta ) )

  return exact

def p17_fun ( n, x ):

#*****************************************************************************80
#
## p17_fun() evaluates the integrand for problem 17.
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) exp ( - x / 2^beta ) * cos ( x ) / sqrt ( x ) dx
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
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 84.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the point at which the integrand
#    is to be evaluated.
#
#  Output:
#
#    real FX(N), the value of the integrand at X.
#
  import numpy as np

  beta = 2.0

  fx = np.zeros_like ( x )

  zero = np.where ( x == 0.0 )
  fx[zero] = 0.0

  nzer = np.where ( x != 0.0 )
  fx[nzer] = np.exp ( - x[nzer] / 2.0**beta ) * np.cos ( x[nzer] ) \
    / np.sqrt ( x[nzer] )

  return fx

def p17_title ( ):

#*****************************************************************************80
#
## p17_title() returns the title for problem 17.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'exp ( - x / 2^beta ) * cos ( x ) / sqrt ( x )'

  return title

def p18_alpha ( ):

#*****************************************************************************80
#
## p18_alpha() returns ALPHA for problem 18.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p18_exact ( ):

#*****************************************************************************80
#
## p18_exact() returns the exact integral for problem 18.
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
#  Output:
#
#    real EXACT, the value of the integral.
#
  beta = 1.0

  exact = 2.0**( 3.0 * beta + 1.0 )

  return exact

def p18_fun ( n, x ):

#*****************************************************************************80
#
## p18_fun() evaluates the integrand for problem 18.
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) x^2 * exp ( - x / 2^beta ) dx
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
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 84.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the point at which the integrand
#    is to be evaluated.
#
#  Output:
#
#    real FX(N), the value of the integrand at X.
#
  import numpy as np

  beta = 1.0

  fx = x**2 * np.exp ( - x / 2**beta )

  return fx

def p18_title ( ):

#*****************************************************************************80
#
## p18_title() returns the title for problem 18.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'x^2 * exp ( - x / 2^beta )'

  return title

def p19_alpha ( ):

#*****************************************************************************80
#
## p19_alpha() returns ALPHA for problem 19.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p19_exact ( ):

#*****************************************************************************80
#
## p19_exact() returns the exact integral for problem 19.
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
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  beta = 0.5

  exact = ( 1.0 - beta ) * np.pi / ( 10.0**beta * np.sin ( np.pi * beta ) )

  return exact

def p19_fun ( n, x ):

#*****************************************************************************80
#
## p19_fun() evaluates the integrand for problem 19.
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) x^(beta-1) / ( 1 + 10 x )^2 dx
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
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 84.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the point at which the integrand
#    is to be evaluated.
#
#  Output:
#
#    real FX(N), the value of the integrand at X.
#
  import numpy as np

  beta = 0.5

  if ( 1.0 <= beta ):
    fx = x**( beta - 1.0 ) / ( 1.0 + 10.0 * x )**2
  else:
    fx = np.zeros_like ( x )
    zero = np.where ( x == 0.0 )
    fx[zero] = 0.0
    nzer = np.where ( x != 0.0 )
    fx[nzer] = x[nzer]**( beta - 1.0 ) / ( 1.0 + 10.0 * x[nzer] )**2

  return fx

def p19_title ( ):

#*****************************************************************************80
#
## p19_title() returns the title for problem 19.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = 'x^(beta-1) / ( 1 + 10 x )^2'

  return title

def p20_alpha ( ):

#*****************************************************************************80
#
## p20_alpha() returns ALPHA for problem 20.
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
#  Output:
#
#    real ALPHA, the value of ALPHA.
#
  alpha = 0.0

  return alpha

def p20_exact ( ):

#*****************************************************************************80
#
## p20_exact() returns the exact integral for problem 20.
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
#  Output:
#
#    real EXACT, the value of the integral.
#
  import numpy as np

  beta = 1.0

  exact = \
    ( \
      np.log ( 1.5 ) / 2.0**beta \
      - 1.0 / 2.0**( beta + 1.0 ) * \
      np.log ( ( 16.0 + 0.25**beta ) / ( 1.0 + 0.25**beta ) ) \
      - np.arctan ( 2.0**( beta + 2.0 ) ) - np.arctan ( 2.0**beta ) \
    ) / ( 1.0 + 0.25**beta )

  return exact

def p20_fun ( n, x ):

#*****************************************************************************80
#
## p20_fun() evaluates the integrand for problem 20.
#
#  Integral:
#
#    Integral ( 0 <= x < +oo ) 
#      1 / ( 2^beta * ( ( x - 1 )^2 + (1/4)^beta ) * ( x - 2 ) ) dx
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
#  Reference:
#
#    Robert Piessens, Elise de Doncker-Kapenga,
#    Christian Ueberhuber, David Kahaner,
#    QUADPACK: A Subroutine Package for Automatic Integration,
#    Springer, 1983, page 84.
#
#  Input:
#
#    integer N, the number of points.
#
#    real X(N), the point at which the integrand
#    is to be evaluated.
#
#  Output:
#
#    real FX(N), the value of the integrand at X.
#
  import numpy as np

  beta = 1.0

  fx = ( 2.0**beta * ( ( x - 1.0 )**2 + 0.25**beta ) * ( x - 2.0 ) )

  nzer = np.where ( fx != 0.0 )
  fx[nzer] = 1.0 / fx[nzer]

  return fx

def p20_title ( ):

#*****************************************************************************80
#
## p20_title() returns the title for problem 20.
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
#  Output:
#
#    string TITLE, the title of the problem.
#
  title = '1 / ( 2^beta * ( ( x - 1 )^2 + (1/4)^beta ) * ( x - 2 ) )'

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
  laguerre_integrands_test ( )
  timestamp ( )

