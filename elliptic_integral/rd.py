#! /usr/bin/env python
#
def rd ( x, y, z, errtol ):

#*****************************************************************************80
#
## RD computes an incomplete elliptic integral of the second kind, RD(X,Y,Z).
#
#  Discussion:
#
#    This function computes an incomplete elliptic integral of the second kind.
#
#    RD(X,Y,Z) = Integral ( 0 <= T < oo )
#
#                    -1/2     -1/2     -3/2
#          (3/2)(T+X)    (T+Y)    (T+Z)    DT,
#
#    where X and Y are nonnegative, X + Y is positive, and Z is positive.
#
#    If X or Y is zero, the integral is complete.
#
#    The duplication theorem is iterated until the variables are
#    nearly equal, and the function is then expanded in Taylor
#    series to fifth order.
#
#    Check:
#
#      RD(X,Y,Z) + RD(Y,Z,X) + RD(Z,X,Y) = 3 / sqrt ( X * Y * Z ),
#      where X, Y, and Z are positive.
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
#    The relative error due to truncation is less than
#      3 * ERRTOL ^ 6 / (1-ERRTOL) ^ 3/2.
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
#    LOLIM IS NOT LESS THAN 2 / (MACHINE MAXIMUM) ^ (2/3).
#    UPLIM IS NOT GREATER THAN (0.1 * ERRTOL / MACHINE
#    MINIMUM) ^ (2/3), WHERE ERRTOL IS DESCRIBED BELOW.
#    IN THE FOLLOWING TABLE IT IS ASSUMED THAT ERRTOL WILL
#    NEVER BE CHOSEN SMALLER THAN 1.E-5.
#
  import numpy as np

  lolim = 6.E-51
  uplim = 1.0E+48

  if ( \
    x < 0.0 or \
    y < 0.0 or \
    x + y < lolim or \
    z < lolim or \
    uplim < x or \
    uplim < y or \
    uplim < z ):
    print ( '' )
    print ( 'RD - Error!' )
    print ( '  Invalid input arguments.' )
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
  sigma = 0.0
  power4 = 1.0

  while ( True ):

    mu = ( xn + yn + 3.0 * zn ) * 0.2
    xndev = ( mu - xn ) / mu
    yndev = ( mu - yn ) / mu
    zndev = ( mu - zn ) / mu
    epslon = max ( abs ( xndev ), max ( abs ( yndev ), abs ( zndev ) ) )

    if ( epslon < errtol ):
      c1 = 3.0 / 14.0
      c2 = 1.0 / 6.0
      c3 = 9.0 / 22.0
      c4 = 3.0 / 26.0
      ea = xndev * yndev
      eb = zndev * zndev
      ec = ea - eb
      ed = ea - 6.0 * eb
      ef = ed + ec + ec
      s1 = ed * ( - c1 + 0.25 * c3 * ed - 1.5 * c4 * zndev * ef )
      s2 = zndev  * ( c2 * ef + zndev * ( - c3 * ec + zndev * c4 * ea ) )
      value = 3.0 * sigma  + power4 * ( 1.0 + s1 + s2 ) / ( mu * np.sqrt ( mu ) )

      return value, ierr

    xnroot = np.sqrt ( xn )
    ynroot = np.sqrt ( yn )
    znroot = np.sqrt ( zn )
    lamda = xnroot * ( ynroot + znroot ) + ynroot * znroot
    sigma = sigma + power4 / ( znroot * ( zn + lamda ) )
    power4 = power4 * 0.25
    xn = ( xn + lamda ) * 0.25
    yn = ( yn + lamda ) * 0.25
    zn = ( zn + lamda ) * 0.25

def rd_test ( ):

#*****************************************************************************80
#
## RD_TEST tests RD.
#
#  Discussion:
#
#    This driver tests the real ( kind = 8 ) function subroutine for the
#    integral RD(X,Y,Z), which is symmetric in X and Y.  The first
#    twelve sets of values of X, Y, Z are extreme points of the region of
#    valid arguments defined by the machine-dependent constants LOLIM
#    and UPLIM.  The values of LOLIM, UPLIM, X, Y, Z, and ERRTOL (see
#    comments in subroutine) may be used on most machines but provide a
#    severe test of robustness only on the ibm 360/370 series.  The
#    thirteenth set tests the failure exit.  The fourteenth set is a
#    check value: RD(0,2,1) = 3B = 3(PI)/4A, where A and B are the
#    lemniscate constants.  The remaining sets show the dependence
#    on Z when Y = 1 (no loss of generality because of homogeneity)
#    and X = 0.5 (midway between the complete case X = 0 and the
#    degenerate case X = Y).
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
   0.00E+00, \
   0.55E-78, \
   0.00E+00, \
   0.55E-78, \
   0.00E+00, \
   0.55E-78, \
   0.00E+00, \
   0.55E-78, \
   3.01E-51, \
   3.01E-51, \
   0.99E+48, \
   0.99E+48, \
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
   0.50E+00 ] )

  y = np.array ( [ \
   6.01E-51, \
   6.01E-51, \
   6.01E-51, \
   6.01E-51, \
   0.99E+48, \
   0.99E+48, \
   0.99E+48, \
   0.99E+48, \
   3.01E-51, \
   3.01E-51, \
   0.99E+48, \
   0.99E+48, \
   3.01E-51, \
   2.00E+00, \
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
   6.01E-51, \
   6.01E-51, \
   0.99E+48, \
   0.99E+48, \
   6.01E-51, \
   6.01E-51, \
   0.99E+48, \
   0.99E+48, \
   6.01E-51, \
   0.99E+48, \
   6.01E-51, \
   0.99E+48, \
   1.00E+00, \
   1.00E+00, \
   1.00E-10, \
   1.00E-05, \
   1.00E-02, \
   1.00E-01, \
   2.00E-01, \
   5.00E-01, \
   1.00E+00, \
   2.00E+00, \
   5.00E+00, \
   1.00E+01, \
   1.00E+02, \
   1.00E+05, \
   1.00E+10 ] )

  print ( '' )
  print ( 'RD_TEST' )
  print ( '  RD evaluates the Carlson elliptic integral' )
  print ( '  of the second kind, RD(X,Y,Z)' )
  print ( '' )
  print ( '               X                          Y                          Z                         RD(X,Y,Z)' )
  print ( '' )

  errtol = 1.0E-3

  for i in range ( 0, 27 ):
    eliptc, ierr = rd ( x[i], y[i], z[i], errtol )
    if (ierr == 0 ):
      print ( '%27.16g%27.16g%27.16g%27.16g' % ( x[i], y[i], z[i], eliptc ) )
    else:
      print ( '%27.16g%27.16g%27.16g  ***Error***' % ( x[i], y[i], z[i] ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp 
  timestamp ( )
  rd_test ( )
  timestamp ( )
