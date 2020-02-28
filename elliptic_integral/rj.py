#! /usr/bin/env python
#
def rj ( x, y, z, p, errtol ):

#*****************************************************************************80
#
## RJ computes an incomplete elliptic integral of the third kind, RJ(X,Y,Z,P).
#
#  Discussion:
#
#    This function computes an incomplete elliptic integral of the third kind.
#
#    RJ(X,Y,Z,P) = Integral ( 0 <= T < oo )
#
#                  -1/2     -1/2     -1/2     -1
#        (3/2)(T+X)    (T+Y)    (T+Z)    (T+P)  DT,
#
#    where X, Y, and Z are nonnegative, at most one of them is
#    zero, and P is positive.
#
#    If X or Y or Z is zero, then the integral is complete.
#
#    The duplication theorem is iterated until the variables are nearly equal,
#    and the function is then expanded in Taylor series to fifth order.
#
#    Check by addition theorem:
#
#      RJ(X,X+Z,X+W,X+P)
#      + RJ(Y,Y+Z,Y+W,Y+P) + (A-B) * RJ(A,B,B,A) + 3 / sqrt ( A)
#      = RJ(0,Z,W,P), where X,Y,Z,W,P are positive and X * Y
#      = Z * W,  A = P * P * (X+Y+Z+W),  B = P * (P+X) * (P+Y),
#      and B - A = P * (P-Z) * (P-W).
#
#    The sum of the third and fourth terms on the left side is 3 * RC(A,B).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 June 2018
#
#  Author:
#
#    Original FORTRAN77 version by Bille Carlson, Elaine Notis.
#    This Python version by John Burkardt.
#
#  Reference:
#
#    Bille Carlson,
#    Computing Elliptic Integrals by Duplication,
#    Numerische Mathematik,
#    Volume 33, 1979, pages 1-16.
#
#    Bille Carlson, Elaine Notis,
#    Algorithm 577, Algorithms for Incomplete Elliptic Integrals,
#    ACM Transactions on Mathematical Software,
#    Volume 7, Number 3, pages 398-403, September 1981.
#
#  Parameters:
#
#    Input, real X, Y, Z, P, the arguments in the integral.
#
#    Input, real ERRTOL, the error tolerance.
#    Relative error due to truncation of the series for rj
#    is less than 3 * ERRTOL ^ 6 / (1 - ERRTOL) ^ 3/2.
#    An error tolerance (ETOLRC) will be passed to the subroutine
#    for RC to make the truncation error for RC less than for RJ.
#    Sample choices:
#      ERRTOL   Relative truncation error less than
#      1.E-3    4.E-18
#      3.E-3    3.E-15
#      1.E-2    4.E-12
#      3.E-2    3.E-9
#      1.E-1    4.E-6
#
#    Output, real VALUE, the value of the function.
#
#    Output, integer IERR, the error flag.
#    0, no error occurred.
#    1, abnormal termination.
#
#  Local Parameters:
#
#    LOLIM AND UPLIM DETERMINE THE RANGE OF VALID ARGUMENTS.
#    LOLIM IS NOT LESS THAN THE CUBE ROOT OF THE VALUE
#    OF LOLIM USED IN THE SUBROUTINE FOR RC.
#    UPLIM IS NOT GREATER THAN 0.3 TIMES THE CUBE ROOT OF
#    THE VALUE OF UPLIM USED IN THE SUBROUTINE FOR RC.
#
  import numpy as np
  from rc import rc

  lolim = 2.E-26
  uplim = 3.E+24

  if ( \
    x < 0.0E+00 or \
    y < 0.0E+00 or \
    z < 0.0E+00 or \
    x + y < lolim or \
    x + z < lolim or \
    y + z < lolim or \
    p < lolim or \
    uplim < x or \
    uplim < y or \
    uplim < z or \
    uplim < p ):
    print ( '' )
    print ( 'RJ - Error!' )
    print ( '  Invalid input arguments.' )
    print ( '  X = %g' % ( x ) )
    print ( '  Y = %g' % ( y ) )
    print ( '  Z = %g' % ( z ) )
    print ( '  P = %g' % ( p ) )
    print ( '' )
    ierr = 1
    value = 0.0
    return value, ierr

  ierr = 0
  xn = x
  yn = y
  zn = z
  pn = p
  sigma = 0.0
  power4 = 1.0
  etolrc = 0.5 * errtol

  while ( True ):

    mu = ( xn + yn + zn + pn + pn ) * 0.2
    xndev = ( mu - xn ) / mu
    yndev = ( mu - yn ) / mu
    zndev = ( mu - zn ) / mu
    pndev = ( mu - pn ) / mu
    epslon = max ( abs ( xndev ), \
      max ( abs ( yndev ), \
      max ( abs ( zndev ), abs ( pndev ) ) ) )

    if ( epslon < errtol ):
      c1 = 3.0 / 14.0
      c2 = 1.0 / 3.0
      c3 = 3.0 / 22.0
      c4 = 3.0 / 26.0
      ea = xndev * ( yndev + zndev ) + yndev * zndev
      eb = xndev * yndev * zndev
      ec = pndev * pndev
      e2 = ea - 3.0 * ec
      e3 = eb + 2.0 * pndev * ( ea - ec )
      s1 = 1.0 + e2 * ( - c1 + 0.75 * c3 * e2 - 1.5 * c4 * e3 )
      s2 = eb * ( 0.5 * c2 + pndev * ( - c3 - c3 + pndev * c4 ) )
      s3 = pndev * ea * ( c2 - pndev * c3 ) - c2 * pndev * ec
      value = 3.0 * sigma + power4 * ( s1 + s2 + s3 ) / ( mu * np.sqrt ( mu ) )
      return value, ierr

    xnroot = np.sqrt ( xn )
    ynroot = np.sqrt ( yn )
    znroot = np.sqrt ( zn )
    lamda = xnroot * ( ynroot + znroot ) + ynroot * znroot
    alfa = pn * ( xnroot + ynroot + znroot ) + xnroot * ynroot * znroot
    alfa = alfa * alfa
    beta = pn * ( pn + lamda ) * ( pn + lamda )
    [ value, ierr ] = rc ( alfa, beta, etolrc )
    sigma = sigma + power4 * value

    if ( ierr != 0 ):
      value = 0.0
      return value, ierr

    power4 = power4 * 0.25
    xn = ( xn + lamda ) * 0.25
    yn = ( yn + lamda ) * 0.25
    zn = ( zn + lamda ) * 0.25
    pn = ( pn + lamda ) * 0.25

def rj_test ( ):

#*****************************************************************************80
#
## RJ_TEST tests RJ.
#
#  Discussion:
#
#    This driver tests the real ( kind = 8 ) function subroutine for the
#    integral Rj(X,Y,Z,P), which is symmetric in X, Y, Z.  The first
#    twenty sets of values of X, Y, Z, P are extreme points of the region
#    of valid arguments defined by the machine-dependent constants
#    LOLIM and UPLIM.  The values of LOLIM, UPLIM, X, Y, Z, P, and
#    ERRTOL (see comments in subroutine) may be used on most machines
#    but provide a severe test of robustness only on the ibm 360/370
#    series.  The twenty-first set tests the failure exit.  The twenty-
#    second set is a check value:
#      RJ(2,3,4,5) = 0.1429757966715675383323308.
#    The remaining sets show the dependence on Z and P
#    when Y = 1 (no loss of generality because of homogeneity) and
#    X = 0.5 (midway between the complete case x = 0 and the degenerate
#    case X = Y).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 June 2018
#
#  Author:
#
#    Original FORTRAN77 version by Bille Carlson, Elaine Notis.
#    This Python version by John Burkardt.
#
  import numpy as np

  p = np.array ( [ \
   2.01E-26, \
   2.01E-26, \
   2.01E-26, \
   2.01E-26, \
   2.01E-26, \
   2.01E-26, \
   2.01E-26, \
   2.01E-26, \
   2.01E-26, \
   2.01E-26, \
   2.99E+24, \
   2.99E+24, \
   2.99E+24, \
   2.99E+24, \
   2.99E+24, \
   2.99E+24, \
   2.99E+24, \
   2.99E+24, \
   2.99E+24, \
   2.99E+24, \
   1.00E+00, \
   5.00E+00, \
   0.25E+00, \
   0.75E+00, \
   1.00E+00, \
   2.00E+00, \
   0.25E+00, \
   0.75E+00, \
   1.50E+00, \
   4.00E+00, \
   0.25E+00, \
   0.75E+00, \
   3.00E+00, \
   1.00E+01, \
   0.25E+00, \
   0.75E+00, \
   5.00E+00, \
   2.00E+01, \
   0.25E+00, \
   0.75E+00, \
   5.00E+01, \
   2.00E+02 ] )

  x = np.array ( [ \
   1.01E-26, \
   1.01E-26, \
   0.00E+00, \
   0.00E+00, \
   0.00E+00, \
   2.99E+24, \
   0.55E-78, \
   0.55E-78, \
   0.55E-78, \
   2.01E-26, \
   1.01E-26, \
   1.01E-26, \
   0.00E+00, \
   0.00E+00, \
   0.00E+00, \
   2.99E+24, \
   0.55E-78, \
   0.55E-78, \
   0.55E-78, \
   2.01E-26, \
   0.00E+00, \
   2.00E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00 ] )

  y = np.array ( [ \
   1.01E-26, \
   1.01E-26, \
   2.01E-26, \
   2.01E-26, \
   2.99E+24, \
   2.99E+24, \
   2.01E-26, \
   2.01E-26, \
   2.99E+24, \
   2.01E-26, \
   1.01E-26, \
   1.01E-26, \
   2.01E-26, \
   2.01E-26, \
   2.99E+24, \
   2.99E+24, \
   2.01E-26, \
   2.01E-26, \
   2.99E+24, \
   2.01E-26, \
   1.90E-26, \
   3.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00 ] )

  z = np.array ( [ \
   1.01E-26, \
   2.99E+24, \
   2.01E-26, \
   2.99E+24, \
   2.99E+24, \
   2.99E+24, \
   2.01E-26, \
   2.99E+24, \
   2.99E+24, \
   2.01E-26, \
   1.01E-26, \
   2.99E+24, \
   2.01E-26, \
   2.99E+24, \
   2.99E+24, \
   2.99E+24, \
   2.01E-26, \
   2.99E+24, \
   2.99E+24, \
   2.01E-26, \
   1.90E-26, \
   4.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   2.00E+00, \
   2.00E+00, \
   2.00E+00, \
   2.00E+00, \
   5.00E+00, \
   5.00E+00, \
   5.00E+00, \
   5.00E+00, \
   1.00E+01, \
   1.00E+01, \
   1.00E+01, \
   1.00E+01, \
   1.00E+02, \
   1.00E+02, \
   1.00E+02, \
   1.00E+02 ] )

  print ( '' )
  print ( 'RJ_TEST' )
  print ( '  RJ evaluates the Carlson elliptic integral' )
  print ( '  of the third kind, RJ(X,Y,Z,P)' )
  print ( '' )
  print ( '               X                          Y                           Z                         P                 RJ(X,Y,Z,P)' )
  print ( '' )

  errtol = 1.0E-3

  for i in range ( 0, 42 ):
    eliptc, ierr = rj ( x[i], y[i], z[i], p[i], errtol )
    if ( ierr == 0 ):
      print ( '%27.16g%27.16g%27.16g%27.16g%27.16g' % ( x[i], y[i], z[i], p[i], eliptc ) )
    else:
      print ( '%27.16g%27.16g%27.16g%27.16g  ***Error***' % ( x[i], y[i], z[i], p[i] ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp 
  timestamp ( )
  rj_test ( )
  timestamp ( )
