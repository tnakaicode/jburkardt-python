#! /usr/bin/env python3
#
def abwe1 ( n, m, tol, coef2, even, b, x ) :

#*****************************************************************************80
#
## ABWE1 calculates a Kronrod abscissa and weight.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    Original FORTRAN77 version by Robert Piessens, Maria Branders.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Robert Piessens, Maria Branders,
#    A Note on the Optimal Addition of Abscissas to Quadrature Formulas
#    of Gauss and Lobatto,
#    Mathematics of Computation,
#    Volume 28, Number 125, January 1974, pages 135-139.
#
#  Parameters:
#
#    Input, integer N, the order of the Gauss rule.
#
#    Input, integer M, the value of ( N + 1 ) / 2.
#
#    Input, real TOL, the requested absolute accuracy of the
#    abscissas.
#
#    Input, real COEF2, a value needed to compute weights.
#
#    Input, logical EVEN, is TRUE if N is even.
#
#    Input, real B(M+1), the Chebyshev coefficients.
#
#    Input, real X, an estimate for the abscissa.
#
#    Output, real X, the abscissa.
#
#    Output, real W, the weight.
#
  from sys import exit

  if ( x == 0.0 ):
    ka = 1
  else:
    ka = 0
#
#  Iterative process for the computation of a Kronrod abscissa.
#
  for iter in range ( 1, 51 ):

    b1 = 0.0
    b2 = b[m+1-1]
    yy = 4.0 * x * x - 2.0
    d1 = 0.0

    if ( even ):
      ai = m + m + 1
      d2 = ai * b[m+1-1]
      dif = 2.0
    else:
      ai = m + 1
      d2 = 0.0
      dif = 1.0

    for k in range ( 1, m + 1 ):
      ai = ai - dif
      i = m - k + 1
      b0 = b1
      b1 = b2
      d0 = d1
      d1 = d2
      b2 = yy * b1 - b0 + b[i-1]
      if ( not even ):
        i = i + 1
      d2 = yy * d1 - d0 + ai * b[i-1]

    if ( even ):
      f = x * ( b2 - b1 )
      fd = d2 + d1
    else:
      f = 0.5 * ( b2 - b0 )
      fd = 4.0 * x * d2
#
#  Newton correction.
#
    delta = f / fd
    x = x - delta

    if ( ka == 1 ):
      break

    if ( abs ( delta ) <= tol ):
      ka = 1
#
#  Catch non-convergence.
#
  if ( ka != 1 ):
    print ( '' )
    print ( 'ABWE1 - Fatal error!' )
    print ( '  Iteration limit reached.' )
    print ( '  Last DELTA was %e' % ( delta ) )
    exit ( 'ABWE1 - Fatal error!' )
#
#  Computation of the weight.
#
  d0 = 1.0
  d1 = x
  ai = 0.0
  for k in range ( 2, n + 1 ):
    ai = ai + 1.0
    d2 = ( ( ai + ai + 1.0 ) * x * d1 - ai * d0 ) / ( ai + 1.0 )
    d0 = d1
    d1 = d2

  w = coef2 / ( fd * d2 )

  return x, w

def abwe2 ( n, m, tol, coef2, even, b, x ):

#*****************************************************************************80
#
## ABWE2 calculates a Gaussian abscissa and two weights.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    Original FORTRAN77 version by Robert Piessens, Maria Branders.
#    PYTHON version by John Burkardt.
#
#  Reference:
#
#    Robert Piessens, Maria Branders,
#    A Note on the Optimal Addition of Abscissas to Quadrature Formulas
#    of Gauss and Lobatto,
#    Mathematics of Computation,
#    Volume 28, Number 125, January 1974, pages 135-139.
#
#  Parameters:
#
#    Input, integer N, the order of the Gauss rule.
#
#    Input, integer M, the value of ( N + 1 ) / 2.
#
#    Input, real TOL, the requested absolute accuracy of the
#    abscissas.
#
#    Input, real COEF2, a value needed to compute weights.
#
#    Input, logical EVEN, is TRUE if N is even.
#
#    Input, real B(M+1), the Chebyshev coefficients.
#
#    Input, real X, an estimate for the abscissa.
#
#    Output, real X, the abscissa.
#
#    Output, real W1, the Gauss-Kronrod weight.
#
#    Output, real W2, the Gauss weight.
#
  from sys import exit

  if ( x == 0.0 ):
    ka = 1
  else:
    ka = 0
#
#  Iterative process for the computation of a Gaussian abscissa.
#
  for iter in range ( 1, 51 ):

    p0 = 1.0
    p1 = x
    pd0 = 0.0
    pd1 = 1.0
#
#  When N is 1, we need to initialize P2 and PD2 to avoid problems with DELTA.
#
    if ( n <= 1 ):
      if ( x != 0.0 ):
        p2 = ( 3.0 * x * x - 1.0 ) / 2.0
        pd2 = 3.0 * x
      else:
        p2 = 3.0 * x
        pd2 = 3.0

    ai = 0.0
    for k in range ( 2, n + 1 ):
      ai = ai + 1.0
      p2 = ( ( ai + ai + 1.0 ) * x * p1 - ai * p0 ) / ( ai + 1.0 )
      pd2 = ( ( ai + ai + 1.0 ) * ( p1 + x * pd1 ) - ai * pd0 ) / ( ai + 1.0 )
      p0 = p1
      p1 = p2
      pd0 = pd1
      pd1 = pd2
#
#  Newton correction.
#
    delta = p2 / pd2
    x = x - delta

    if ( ka == 1 ):
      break

    if ( abs ( delta ) <= tol ):
      ka = 1
#
#  Catch non-convergence.
#
  if ( ka != 1 ):
    print ( '' )
    print ( 'ABWE2 - Fatal error!' )
    print ( '  Iteration limit reached.' )
    print ( '  Last DELTA was %e' % ( delta ) )
    exit ( 'ABWE2 - Fatal error!' )
#
#  Computation of the weight.
#
  an = n

  w2 = 2.0 / ( an * pd2 * p0 )

  p1 = 0.0
  p2 = b[m+1-1]
  yy = 4.0 * x * x - 2.0
  for k in range ( 1, m + 1 ):
    i = m - k + 1
    p0 = p1
    p1 = p2
    p2 = yy * p1 - p0 + b[i-1]

  if ( even ):
    w1 = w2 + coef2 / ( pd2 * x * ( p2 - p1 ) )
  else:
    w1 = w2 + 2.0 * coef2 / ( pd2 * ( p2 - p0 ) )

  return x, w1, w2

def f ( x ):

#*****************************************************************************80
#
## F is a function whose integral from -1 to +1 is to be estimated.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, double X, the argument.
#
#    Output, double F, the value.
#
  value = 1.0 / ( x * x + 1.005 )

  return value

def kronrod ( n, tol ):

#*****************************************************************************80
#
## KRONROD adds N+1 points to an N-point Gaussian rule.
#
#  Discussion:
#
#    This subroutine calculates the abscissas and weights of the 2N+1
#    point Gauss Kronrod quadrature formula which is obtained from the
#    N point Gauss quadrature formula by the optimal addition of N+1 points.
#
#    The optimally added points are called Kronrod abscissas.  The
#    abscissas and weights for both the Gauss and Gauss Kronrod rules
#    are calculated for integration over the interval [-1,+1].
#
#    Since the quadrature formula is symmetric with respect to the origin,
#    only the nonnegative abscissas are calculated.
#
#    Note that the code published in Mathematics of Computation
#    omitted the definition of the variable which is here called COEF2.
#
#  Storage:
#
#    Given N, let M = ( N + 1 ) / 2.
#
#    The Gauss-Kronrod rule will include 2*N+1 points.  However, by symmetry,
#    only N + 1 of them need to be listed.
#
#    The arrays X, W1 and W2 contain the nonnegative abscissas in decreasing
#    order, and the weights of each abscissa in the Gauss-Kronrod and
#    Gauss rules respectively.  This means that about half the entries
#    in W2 are zero.
#
#    For instance, if N = 3, the output is:
#
#    I      X               W1              W2
#
#    1    0.960491        0.104656         0.000000
#    2    0.774597        0.268488         0.555556
#    3    0.434244        0.401397         0.000000
#    4    0.000000        0.450917         0.888889
#
#    and if N = 4, (notice that 0 is now a Kronrod abscissa)
#    the output is
#
#    I      X               W1              W2
#
#    1    0.976560        0.062977        0.000000
#    2    0.861136        0.170054        0.347855
#    3    0.640286        0.266798        0.000000
#    4    0.339981        0.326949        0.652145
#    5    0.000000        0.346443        0.000000
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    Original FORTRAN77 version by Robert Piessens, Maria Branders.
#    PYTHON version by John Burkardt.
#
#  Reference:
#
#    Robert Piessens, Maria Branders,
#    A Note on the Optimal Addition of Abscissas to Quadrature Formulas
#    of Gauss and Lobatto,
#    Mathematics of Computation,
#    Volume 28, Number 125, January 1974, pages 135-139.
#
#  Parameters:
#
#    Input, integer N, the order of the Gauss rule.
#
#    Input, real TOL, the requested absolute accuracy of the
#    abscissas.
#
#    Output, real X(N+1), the abscissas.
#
#    Output, real W1(N+1), the weights for the Gauss-Kronrod rule.
#
#    Output, real W2(N+1), the weights for the Gauss rule.
#
  import numpy as np

  m = ( ( n + 1 ) // 2 )
  even = ( 2 * m == n )

  b = np.zeros ( m + 1 )
  tau = np.zeros ( m )
  w1 = np.zeros ( n + 1 )
  w2 = np.zeros ( n + 1 )
  x = np.zeros ( n + 1 )

  d = 2.0
  an = 0.0
  for k in range ( 1, n + 1 ):
    an = an + 1.0
    d = d * an / ( an + 0.5 )
#
#  Calculation of the Chebyshev coefficients of the orthogonal polynomial.
#  
  tau[1-1] = ( an + 2.0 ) / ( an + an + 3.0 )
  b[m-1] = tau[1-1] - 1.0
  ak = an

  for l in range ( 1, m ):
    ak = ak + 2.0
    tau[l+1-1] = ( ( ak - 1.0 ) * ak \
      - an * ( an + 1.0 ) ) * ( ak + 2.0 ) * tau[l-1] \
      / ( ak * ( ( ak + 3.0 ) * ( ak + 2.0 ) \
      - an * ( an + 1.0 ) ) )
    b[m-l-1] = tau[l+1-1]

    for ll in range ( 1, l + 1 ):
      b[m-l-1] = b[m-l-1] + tau[ll-1] * b[m-l+ll-1]

  b[m+1-1] = 1.0
#
#  Calculation of approximate values for the abscissas.
#
  bb = np.sin ( 0.5 * np.pi / ( an + an + 1.0 ) )
  x1 = np.sqrt ( 1.0 - bb * bb )
  s = 2.0 * bb * x1
  c = np.sqrt ( 1.0 - s * s )
  coef = 1.0 - ( 1.0 - 1.0 / an ) / ( 8.0 * an * an )
  xx = coef * x1
#
#  Coefficient needed for weights.
#
#  COEF2 = 2^(2*n+1) * n! * n! / (2n+1)!
#
  coef2 = 2.0 / ( 2 * n + 1 )
  for i in range ( 1, n + 1 ):
    coef2 = coef2 * 4.0 * i / ( n + i )
#
#  Calculation of the K-th abscissa (a Kronrod abscissa) and the
#  corresponding weight.
#
  for k in range ( 1, n + 1, 2 ):

    [ xx, w1[k-1] ] = abwe1 ( n, m, tol, coef2, even, b, xx )
    w2[k-1] = 0.0

    x[k-1] = xx
    y = x1
    x1 = y * c - bb * s
    bb = y * s + bb * c

    if ( k == n ):
      xx = 0.0
    else:
      xx = coef * x1
#
#  Calculation of the K+1 abscissa (a Gaussian abscissa) and the
#  corresponding weights.
#
    [ xx, w1[k+1-1], w2[k+1-1] ] = abwe2 ( n, m, tol, coef2, even, b, xx )

    x[k+1-1] = xx
    y = x1
    x1 = y * c - bb * s
    bb = y * s + bb * c
    xx = coef * x1
#
#  If N is even, we have one more Kronrod abscissa to compute,
#  namely the origin.
#
  if ( even ):
    xx = 0.0
    [ xx, w1[n+1-1] ] = abwe1 ( n, m, tol, coef2, even, b, xx )
    w2[n+1-1] = 0.0
    x[n+1-1] = xx

  return x, w1, w2

def kronrod_adjust ( a, b, n, x, w1, w2 ):

#*****************************************************************************80
#
## KRONROD_ADJUST adjusts a Gauss-Kronrod rule from [-1,+1] to [A,B].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the endpoints of the new interval.
#
#    Input, integer N, the order of the rule.
#
#    Input/output, real X(N+1), W1(N+1), W2(N+1), the abscissas
#    and weights.
#
  for i in range ( 0, n + 1 ):

    x[i] = ( ( 1.0 - x[i] ) * a   \
           + ( 1.0 + x[i] ) * b ) \
             / 2.0

    w1[i] = ( ( b - a ) / 2.0 ) * w1[i]
    w2[i] = ( ( b - a ) / 2.0 ) * w2[i]

  return x, w1, w2

def kronrod_test01 ( ):

#*****************************************************************************80
#
## KRONROD_TEST01 tests the code for the odd case N = 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 3

  wg = np.array ( [ \
    0.555555555555555555556, \
    0.888888888888888888889, \
    0.555555555555555555556 ] )

  wk = np.array ( [ \
    0.104656226026467265194, \
    0.268488089868333440729, \
    0.401397414775962222905, \
    0.450916538658474142345, \
    0.401397414775962222905, \
    0.268488089868333440729, \
    0.104656226026467265194 ] )

  xg = np.array ( [ \
   -0.77459666924148337704, \
    0.0, \
    0.77459666924148337704 ] )

  xk = np.array ( [ \
   -0.96049126870802028342, \
   -0.77459666924148337704, \
   -0.43424374934680255800, \
    0.0, \
    0.43424374934680255800, \
    0.77459666924148337704, \
    0.96049126870802028342 ] )

  print ( '' )
  print ( 'KRONROD_TEST01' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Request KRONROD to compute the Gauss rule' )
  print ( '  of order 3, and the Kronrod extension of' )
  print ( '  order 3+4=7.' )
  print ( '' )
  print ( '  Compare to exact data.' )

  tol = 0.000001

  x, w1, w2 = kronrod ( n, tol )

  print ( '' )
  print ( '  KRONROD returns 3 vectors of length %d' % ( n + 1 ) )
  print ( '' )
  print ( '     I      X               WK              WG' )
  print ( '' )
  for i in range ( 1, n + 2 ):
    print ( '  %4d  %14f  %14f  %14f' % ( i, x[i-1], w1[i-1], w2[i-1] ) )

  print ( '' )
  print ( '               Gauss Abscissas' )
  print ( '            Exact           Computed' )
  print ( '' )
  for i in range ( 1, n + 1 ):
    if ( 2 * i <= n + 1 ):
      i2 = 2 * i
      s = -1.0
    else:
      i2 = 2 * ( n + 1 ) - 2 * i
      s = +1.0
    print ( '  %4d  %14f  %14f' % ( i, xg[i-1], s * x[i2-1] ) )
  print ( '' )
  print ( '               Gauss Weights' )
  print ( '            Exact           Computed' )
  print ( '' )
  for i in range ( 1, n + 1 ):
    if ( 2 * i <= n + 1 ):
      i2 = 2 * i
    else:
      i2 = 2 * ( n + 1 ) - 2 * i
    print ( '  %4d  %14f  %14f' % ( i, wg[i-1], w2[i2-1] ) )

  print ( '' )
  print ( '             Gauss Kronrod Abscissas' )
  print ( '            Exact           Computed' )
  print ( '' )
  for i in range ( 1, 2 * n + 2 ):
    if ( i <= n + 1 ):
      i2 = i
      s = -1.0
    else:
      i2 = 2 * ( n + 1 ) - i
      s = +1.0
    print ( '  %4d  %14f  %14f' % ( i, xk[i-1], s * x[i2-1] ) )
  print ( '' )
  print ( '             Gauss Kronrod Weights' )
  print ( '            Exact           Computed' )
  print ( '' )
  for i in range ( 1, 2 * n + 2 ):
    if ( i <= n + 1 ):
      i2 = i
    else:
      i2 = 2 * ( n + 1 ) - i
    print ( '  %4d  %14f  %14f' % ( i, wk[i-1], w1[i2-1] ) )

  return

def kronrod_test02 ( ):

#*****************************************************************************80
#
## KRONROD_TEST02 tests the code for the even case N = 4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 4

  print ( '' )
  print ( 'KRONROD_TEST02' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Request KRONROD to compute the Gauss rule' )
  print ( '  of order 4, and the Kronrod extension of' )
  print ( '  order 4+5=9.' )

  tol = 0.000001

  x, w1, w2 = kronrod ( n, tol )

  print ( '' )
  print ( '  KRONROD returns 3 vectors of length %d' % ( n + 1 ) )
  print ( '' )
  print ( '     I      X               WK              WG' )
  print ( '' )
  for i in range ( 1, n + 2 ):
    print ( '  %4d  %14f  %14f  %14f' % ( i, x[i-1], w1[i-1], w2[i-1] ) )

  return

def kronrod_test03 ( ):

#*****************************************************************************80
#
## KRONROD_TEST03 uses the program to estimate an integral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 April 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  exact = 1.5643964440690497731

  print ( '' )
  print ( 'KRONROD_TEST03' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Call Kronrod to estimate the integral of a function.' )
  print ( '  Keep trying until the error is small.' )
#
#  TOL just tells KRONROD how carefully it must compute X, W1 and W2.
#  It is NOT a statement about the accuracy of your integral estimate!
#
  tol = 0.000001
#
#  Start the process with a 1 point rule.
#
  n = 1

  while ( 1 ):

    x, w1, w2 = kronrod ( n, tol )
#
#  Compute the estimates.
#  There are two complications here:
#
#  1) Both rules use all the points.  However, the lower order rule uses
#     a zero weight for the points it doesn't need.
#
#  2) The points X are all positive, and are listed in descending order.
#     this means that 0 is always in the list, and always occurs as the
#     last member.  Therefore, the integral estimates should use the
#     function value at 0 once, and the function values at the other
#     X values "twice", that is, once at X and once at -X.
#
    i1 = w1[n+1-1] * f ( x[n+1-1] )
    i2 = w2[n+1-1] * f ( x[n+1-1] )

    for i in range ( 1, n + 1 ):
      i1 = i1 + w1[i-1] * ( f ( - x[i-1] ) + f ( x[i-1] ) )
      i2 = i2 + w2[i-1] * ( f ( - x[i-1] ) + f ( x[i-1] ) )

    if ( abs ( i1 - i2 ) < 0.0001 ):
      print ( '' )
      print ( '  Error tolerance satisfied with N = %d' % ( n ) )
      print ( '  Coarse integral estimate = %14.6g' % ( i1 ) )
      print ( '  Fine   integral estimate = %14.6g' % ( i2 ) )
      print ( '  Error estimate = %g' % ( abs ( i2 - i1 ) ) )
      print ( '  Actual error =   %g' % ( abs ( exact - i2 ) ) )
      break

    if ( 25 < n ):
      print ( '' )
      print ( '  Error tolerance failed even for n = %d' % ( n ) )
      print ( '  Canceling iteration, and accepting bad estimates!' )
      print ( '  Coarse integral estimate = %14.6g' % ( i1 ) )
      print ( '  Fine   integral estimate = %14.6g' % ( i2 ) )
      print ( '  Error estimate = %g' % ( abs ( i2 - i1 ) ) )
      print ( '  Actual error =   %g' % ( abs ( exact - i2 ) ) )
      break

    n = 2 * n + 1

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
  kronrod_test01 ( )
  kronrod_test02 ( )
  kronrod_test03 ( )
  timestamp ( )

