#! /usr/bin/env python
#
def rf ( x, y, z, errtol ):

#*****************************************************************************80
#
## RF computes an incomplete elliptic integral of the first kind, RF(X,Y,Z).
#
#  Discussion:
#
#    This function computes the incomplete elliptic integral of the first kind.
#
#    RF(X,Y,Z) = Integral ( 0 <= T < oo )
#
#                    -1/2     -1/2     -1/2
#          (1/2)(T+X)    (T+Y)    (T+Z)    DT,
#
#    where X, Y, and Z are nonnegative and at most one of them is zero.
#
#    If X or Y or Z is zero, the integral is complete.
#
#    The duplication theorem is iterated until the variables are
#    nearly equal, and the function is then expanded in Taylor
#    series to fifth order.
#
#    Check by addition theorem:
#
#      RF(X,X+Z,X+W) + RF(Y,Y+Z,Y+W) = RF(0,Z,W),
#      where X, Y, Z, W are positive and X * Y = Z * W.
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
#    Input, real X, Y, Z, the arguments in the integral.
#
#    Input, real ERRTOL, the error tolerance.
#    Relative error due to truncation is less than
#      ERRTOL ^ 6 / (4 * (1 - ERRTOL)).
#    Sample choices:
#      ERRTOL   Relative truncation error less than
#      1.E-3    3.E-19
#      3.E-3    2.E-16
#      1.E-2    3.E-13
#      3.E-2    2.E-10
#      1.E-1    3.E-7
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
#    LOLIM IS NOT LESS THAN THE MACHINE MINIMUM MULTIPLIED BY 5.
#    UPLIM IS NOT GREATER THAN THE MACHINE MAXIMUM DIVIDED BY 5.
#
  import numpy as np

  lolim = 3.0E-78
  uplim = 1.0E+75

  if ( \
    x < 0.0E+00 or \
    y < 0.0E+00 or \
    z < 0.0E+00 or \
    x + y < lolim or \
    x + z < lolim or \
    y + z < lolim or \
    uplim <= x or \
    uplim <= y or \
    uplim <= z ):
    print ( '' )
    print ( 'RF - Error!' )
    print ( '  Invalid input arguments.')
    print ( '  X = %g' % ( x ) )
    print ( '  Y = %g' % ( y ) )
    print ( '  Z = %g' % ( z ) )
    print ( '' )
    ierr = 1
    value = 0.0
    return value, ierr

  ierr = 0
  xn = x
  yn = y
  zn = z

  while ( True ):

    mu = ( xn + yn + zn ) / 3.0
    xndev = 2.0 - ( mu + xn ) / mu
    yndev = 2.0 - ( mu + yn ) / mu
    zndev = 2.0 - ( mu + zn ) / mu
    epslon = max ( abs ( xndev ), \
      max ( abs ( yndev ), abs ( zndev ) ) )

    if ( epslon < errtol ):
      c1 = 1.0 / 24.0
      c2 = 3.0 / 44.0
      c3 = 1.0 / 14.0
      e2 = xndev * yndev - zndev * zndev
      e3 = xndev * yndev * zndev
      s = 1.0 + ( c1 * e2 - 0.1 - c2 * e3 ) * e2 + c3 * e3
      value = s / np.sqrt ( mu )
      return value, ierr

    xnroot = np.sqrt ( xn )
    ynroot = np.sqrt ( yn )
    znroot = np.sqrt ( zn )
    lamda = xnroot * ( ynroot + znroot ) + ynroot * znroot
    xn = ( xn + lamda ) * 0.25
    yn = ( yn + lamda ) * 0.25
    zn = ( zn + lamda ) * 0.25

def rf_test ( ):

#*****************************************************************************80
#
#c RF_TEST tests RF.
#
#  Discussion:
#
#    This driver tests the real ( kind = 8 ) function subroutine for the
#    integral RF(X,Y,Z), which is symmetric in X, Y, Z.  The first nine
#    sets of values of X, Y, Z are extreme points of the region of valid
#    arguments defined by the machine-dependent constants LOLIM and
#    UPLIM.  The values of LOLIM, UPLIM, X, Y, Z, and ERRTOL (see
#    comments in subroutine) may be used on most machines but provide a
#    severe test of robustness only on the ibm 360/370 series.  The
#    tenth set tests the failure exit.  The eleventh set is a check
#    value: RF(0,1,2) = A, where A is the first lemniscate constant.
#    The remaining sets show the dependence on Z when Y = 1 (no loss of
#    generality because of homogeneity) and X = 0.5 (midway between the
#    complete case X = 0 and the degenerate case X = Y).
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

  x = np.array ( [ \
   1.51E-78, \
   1.51E-78, \
   0.00E+00, \
   0.00E+00, \
   0.00E+00, \
   0.99E+75, \
   0.55E-78, \
   0.55E-78, \
   0.55E-78, \
   0.00E+00, \
   0.00E+00, \
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
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00, \
   0.50E+00 ] )

  y = np.array ( [ \
   1.51E-78, \
   1.51E-78, \
   3.01E-78, \
   3.01E-78, \
   0.99E+75, \
   0.99E+75, \
   3.01E-78, \
   3.01E-78, \
   0.99E+75, \
   2.00E-78, \
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
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00, \
   1.00E+00 ] )

  z = np.array ( [ \
   1.51E-78, \
   0.99E+75, \
   3.01E-78, \
   0.99E+75, \
   0.99E+75, \
   0.99E+75, \
   3.01E-78, \
   0.99E+75, \
   0.99E+75, \
   1.00E+00, \
   2.00E+00, \
   1.00E+00, \
   1.10E+00, \
   1.20E+00, \
   1.30E+00, \
   1.40E+00, \
   1.50E+00, \
   1.60E+00, \
   1.70E+00, \
   1.80E+00, \
   1.90E+00, \
   2.00E+00, \
   2.20E+00, \
   2.40E+00, \
   2.60E+00, \
   2.80E+00, \
   3.00E+00, \
   3.50E+00, \
   4.00E+00, \
   4.50E+00, \
   5.00E+00, \
   6.00E+00, \
   7.00E+00, \
   8.00E+00, \
   9.00E+00, \
   1.00E+01, \
   2.00E+01, \
   3.00E+01, \
   4.00E+01, \
   5.00E+01, \
   1.00E+02, \
   2.00E+02, \
   5.00E+02, \
   1.00E+03, \
   1.00E+04, \
   1.00E+05, \
   1.00E+06, \
   1.00E+08, \
   1.00E+10, \
   1.00E+12, \
   1.00E+15, \
   1.00E+20, \
   1.00E+30, \
   1.00E+40, \
   1.00E+50 ] )

  print ( '' )
  print ( 'RF_TEST' )
  print ( '  RF evaluates the Carlson elliptic integral' )
  print ( '  of the first kind, RF(X,Y,Z)' )
  print ( '' )
  print ( '               X                          Y                          Z                         RF(X,Y,Z)' )
  print ( '' )

  errtol = 1.0E-3

  for i in range ( 0, 55 ):
    eliptc, ierr = rf ( x[i], y[i], z[i], errtol )
    if ( ierr == 0 ):
      print ( '%27.16g%27.16g%27.16g%27.16g' % ( x[i], y[i], z[i], eliptc ) )
    else:
      print ( '%27.16g%27.16g%27.16g  ***Error***' % ( x[i], y[i], z[i] ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp 
  timestamp ( )
  rf_test ( )
  timestamp ( )

