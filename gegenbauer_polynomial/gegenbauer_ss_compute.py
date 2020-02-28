#! /usr/bin/env python3
#
def gegenbauer_ss_compute ( n, alpha ):

#*****************************************************************************80
#
## GEGENBAUER_SS_COMPUTE computes a Gauss-Gegenbauer quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) (1-X^2)^ALPHA * F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    Thanks to Janiki Raman for pointing out a problem in an earlier
#    version of the code that occurred when ALPHA was -0.5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    Original FORTRAN77 version by Arthur Stroud, Don Secrest.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Parameters:
#
#    Input, integer N, the order.
#
#    Input, real ALPHA, the exponent of (1-X^2) in the weight.  
#    -1.0 < ALPHA is required.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np
  from r8_gamma import r8_gamma
  from r8vec_reverse import r8vec_reverse
  from sys import exit
#
#  Check N.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'GEGENBAUER_SS_COMPUTE - Fatal error!' )
    print ( '  1 <= N is required.' )
    exit ( 'GEGENBAUER_SS_COMPUTE - Fatal error!' )
#
#  Check ALPHA.
#
  if ( alpha <= -1.0 ):
    print ( '' )
    print ( 'GEGENBAUER_SS_COMPUTE - Fatal error!' )
    print ( '  -1.0 < ALPHA is required.' )
    exit ( 'GEGENBAUER_SS_COMPUTE - Fatal error!' )

  x = np.zeros ( n )
  w = np.zeros ( n )
#
#  Set the recursion coefficients.
#
  c = np.zeros ( n )

  c[0] = 0.0;
  if ( 2 <= n ):
    c[1] = 1.0 / ( 2.0 * alpha + 3.0 )

  for i in range ( 2, n ):

    c[i] = float ( i ) \
      * ( alpha + alpha + i ) / \
      ( ( alpha + alpha + 2 * i + 1 ) \
      * ( alpha + alpha + 2 * i - 1 ) )

  delta = r8_gamma ( alpha         + 1.0 ) \
        * r8_gamma (         alpha + 1.0 ) \
        / r8_gamma ( alpha + alpha + 2.0 )

  c_product = 1.0
  for i in range ( 1, n ):
    c_product = c_product * c[i]

  cc = delta * 2.0 ** ( 2.0 * alpha + 1.0 ) * c_product

  for i in range ( 0, n ):

    if ( i == 0 ):

      an = alpha / float ( n )

      r1 = ( 1.0 + alpha ) * ( 2.78 / ( 4.0 + n * n ) + 0.768 * an / n )

      r2 = 1.0 + 2.44 * an + 1.281 * an ** 2

      xval = ( r2 - r1 ) / r2

    elif ( i == 1 ):

      r1 = ( 4.1 + alpha ) / ( ( 1.0 + alpha ) * ( 1.0 + 0.156 * alpha ) )

      r2 = 1.0 + 0.06 * ( n - 8.0 ) * ( 1.0 + 0.12 * alpha ) / n

      r3 = 1.0 + 0.012 * alpha * ( 1.0 + 0.25 * abs ( alpha ) ) / n

      xval = xval - r1 * r2 * r3 * ( 1.0 - xval )

    elif ( i == 2 ):

      r1 = ( 1.67 + 0.28 * alpha ) / ( 1.0 + 0.37 * alpha )

      r2 = 1.0 + 0.22 * ( n - 8.0 ) / n

      r3 = 1.0 + 8.0 * alpha / ( ( 6.28 + alpha ) * n * n )

      xval = xval - r1 * r2 * r3 * ( x[0] - xval )

    elif ( i < n - 2 ):

      xval = 3.0 * x[i-1] - 3.0 * x[i-2] + x[i-3]

    elif ( i == n - 2 ):

      r1 = ( 1.0 + 0.235 * alpha ) / ( 0.766 + 0.119 * alpha )

      r2 = 1.0 / ( 1.0 + 0.639 * ( n - 4.0 ) / ( 1.0 + 0.71 * ( n - 4.0 ) ) )

      r3 = 1.0 / ( 1.0 + 20.0 * alpha / ( ( 7.5 + alpha ) * n * n ) )

      xval = xval + r1 * r2 * r3 * ( xval - x[i-2] )

    elif ( i == n - 1 ):

      r1 = ( 1.0 + 0.37 * alpha ) / ( 1.67 + 0.28 * alpha )

      r2 = 1.0 / ( 1.0 + 0.22 * ( n - 8.0 ) / n )

      r3 = 1.0 / ( 1.0 + 8.0 * alpha / ( ( 6.28 + alpha ) * n * n ) )

      xval = xval + r1 * r2 * r3 * ( xval - x[i-2] )

    xval, dp2, p1 = gegenbauer_ss_root ( xval, n, alpha, c )
 
    x[i] = xval
    w[i] = cc / ( dp2 * p1 )
#
#  Reverse the order of the values.
#
  x = r8vec_reverse ( n, x );
  w = r8vec_reverse ( n, w );

  return x, w

def gegenbauer_ss_recur ( x, n, alpha, c ):

#*****************************************************************************80
#
## GEGENBAUER_SS_RECUR: value and derivative of a Gegenbauer polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    Original FORTRAN77 version by Arthur Stroud, Don Secrest,
#    Python version by John Burkardt,
#
#  Reference:
#
#    Arthur Stroud, Don Secrest,
#    Gaussian Quadrature Formulas,
#    Prentice Hall, 1966,
#    LC: QA299.4G3S7.
#
#  Parameters:
#
#    Input, real X, the point at which polynomials are evaluated.
#
#    Input, integer N, the order of the polynomial to be computed.
#
#    Input, real ALPHA, the exponent of (1-X^2) in the quadrature rule.
#
#    Input, real C(N), the recursion coefficients.
#
#    Output, real P2, the value of J(N)(X).
#
#    Output, real DP2, the value of J'(N)(X).
#
#    Output, real P1, the value of J(N-1)(X).
#
  p1 = 1.0
  dp1 = 0.0

  p2 = x
  dp2 = 1.0

  for i in range ( 1, n ):

    p0 = p1
    dp0 = dp1

    p1 = p2
    dp1 = dp2

    p2 = x * p1 - c[i] * p0
    dp2 = x * dp1 + p1 - c[i] * dp0

  return p2, dp2, p1

def gegenbauer_ss_root ( x, n, alpha, c ):

#*****************************************************************************80
#
## GEGENBAUER_SS_ROOT improves an approximate root of a Gegenbauer polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
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
#  Parameters:
#
#    Input, real X, the approximate root.
#
#    Input, integer N, the order of the polynomial to be computed.
#
#    Input, real ALPHA, the exponent of (1-X^2) in the quadrature rule.
#
#    Input, real C(N), the recursion coefficients.
#
#    Output, real X, the improved approximate root.
#
#    Output, real DP2, the value of J'(N)(X).
#
#    Output, real P1, the value of J(N-1)(X).
#
  maxstep = 10
  eps = 2.220446049250313E-016

  for i in range ( 0, maxstep ):

    p2, dp2, p1 = gegenbauer_ss_recur ( x, n, alpha, c )

    d = p2 / dp2
    x = x - d

    if ( abs ( d ) <= eps * ( abs ( x ) + 1.0 ) ):
      break

  return x, dp2, p1

def gegenbauer_ss_compute_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_SS_COMPUTE_TEST compares GEGENBAUER_SS_COMPUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  alpha = 0.5

  print ( '' )
  print ( 'GEGENBAUER_SS_COMPUTE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEGENBAUER_SS_COMPUTE computes Gauss-Gegenbauer rules;' )
  print ( '' )
  print ( '  Abscissas and weights for a generalized Gauss Gegenbauer rule' )
  print ( '  with ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '   #                         W                         X' )
  print ( '' )

  for n in range ( 1, 11 ):

    x, w = gegenbauer_ss_compute ( n, alpha );

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, w[i], x[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_SS_COMPUTE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gegenbauer_ss_compute_test ( )
  timestamp ( )

