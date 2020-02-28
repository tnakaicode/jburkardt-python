#! /usr/bin/env python3
#
def rc ( x, y, errtol ):

#*****************************************************************************80
#
## RC computes the elementary integral RC(X,Y).
#
#  Discussion:
#
#    This function computes the elementary integral
#
#      RC(X,Y) = Integral ( 0 <= T < oo )
#
#                  -1/2     -1
#        (1/2)(T+X)    (T+Y)  DT,
#
#    where X is nonnegative and Y is positive.  The duplication
#    theorem is iterated until the variables are nearly equal,
#    and the function is then expanded in Taylor series to fifth
#    order.
#
#    Logarithmic, inverse circular, and inverse hyperbolic
#    functions can be expressed in terms of RC.
#
#    Check by addition theorem:
#
#      RC(X,X+Z) + RC(Y,Y+Z) = RC(0,Z),
#      where X, Y, and Z are positive and X * Y = Z * Z.
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
#    Input, real X, Y, the arguments in the integral.
#
#    Input, real ERRTOL, the error tolerance.
#    Relative error due to truncation is less than
#      16 * ERRTOL ^ 6 / (1 - 2 * ERRTOL).
#    Sample choices:
#      ERRTOL   Relative truncation error less than
#      1.0E-3    2.0E-17
#      3.0E-3    2.0E-14
#      1.0E-2    2.0E-11
#      3.0E-2    2.0E-8
#      1.0E-1    2.0E-5
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

  lolim = 3.E-78
  uplim = 1.0E+75

  if ( \
    x < 0.0 or \
    y <= 0.0 or \
    ( x + y ) < lolim or \
    uplim < x or \
    uplim < y ):
    print ( '' )
    print ( 'RC - Error!' )
    print ( '  Invalid input arguments.' )
    print ( '  X = %g' % ( x ) )
    print ( '  Y = %g' % ( y ) )
    print ( '' )
    ierr = 1
    value = 0.0
    return value, ierr

  ierr = 0
  xn = x
  yn = y

  while ( True ):

    mu = ( xn + yn + yn ) / 3.0
    sn = ( yn + mu ) / mu - 2.0

    if ( abs ( sn ) < errtol ):
      c1 = 1.0 / 7.0
      c2 = 9.0 / 22.0
      s = sn * sn * ( 0.3 + sn * ( c1 + sn * ( 0.375 + sn * c2 ) ) )
      value = ( 1.0 + s ) / np.sqrt ( mu )
      return value, ierr

    lamda = 2.0 * np.sqrt ( xn ) * np.sqrt ( yn ) + yn
    xn = ( xn + lamda ) * 0.25
    yn = ( yn + lamda ) * 0.25

def rc_test ( ):

#*****************************************************************************80
#
## RC_TEST tests RC.
#
#  Discussion:
#
#    This driver tests the real ( kind = 8 ) function subroutine for the
#    integral RC(X,Y).  The first six sets of values of X and Y are
#    extreme points of the region of valid arguments defined by the
#    machine-dependent constants LOLIM and UPLIM.  The values of LOLIM,
#    UPLIM, X, Y, and ERRTOL (see comments in subroutine) may be used on
#    most machines but provide a severe test of robustness only on the
#    ibm 360/370 series.  The seventh set tests the failure exit.  The
#    next three sets are check values: RC(0,0.25) = RC(0.0625,0.125) = PI
#    and RC(2.25,2) = LN(2).  The remaining sets show the dependence on X
#    when Y = 1.  Fixing Y entails no loss here because RC is homogeneous.
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
   3.01E-78, \
   0.00E+00, \
   0.99E+75, \
   0.00E+00, \
   0.99E+75, \
   0.00E+00, \
   0.00E+00, \
   6.25E-02, \
   2.25E+00, \
   0.01E+00, \
   0.02E+00, \
   0.05E+00, \
   0.10E+00, \
   0.20E+00, \
   0.40E+00, \
   0.60E+00, \
   0.80E+00, \
   1.00E+00, \
   1.20E+00, \
   1.50E+00, \
   2.00E+00, \
   3.00E+00, \
   4.00E+00, \
   5.00E+00, \
   1.00E+01, \
   2.00E+01, \
   5.00E+01, \
   1.00E+02, \
   1.00E+03, \
   1.00E+04, \
   1.00E+05, \
   1.00E+06, \
   1.00E+07, \
   1.00E+08, \
   1.00E+09, \
   1.00E+10, \
   1.00E+12, \
   1.00E+15, \
   1.00E+20, \
   1.00E+30, \
   1.00E+40, \
   1.00E+50 ] )

  y = np.array ( [ \
   1.51E-78, \
   0.55E-78, \
   3.01E-78, \
   0.55E-78, \
   0.99E+75, \
   0.99E+75, \
   2.00E-78, \
   2.50E-01, \
   1.25E-01, \
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

  print ( '' )
  print ( 'RC_TEST' )
  print ( '  RC evaluates the elementary integral RC(X,Y)' )

  print ( '' )
  print ( '              X                          Y' ),
  print ( '                         RC(X,Y)' )
  print ( '' )

  errtol = 1.0E-3

  for i in range ( 0, 43 ):
    eliptc, ierr = rc ( x[i], y[i], errtol )
    if ( ierr == 0 ):
      print ( '  %27.16g%27.16g%27.16g' % ( x[i], y[i], eliptc ) )
    else:
      print ( '  %27.16g%27.16g  **Error***' % ( x[i], y[i] ) )

  return

def rc_test2 ( ):

#*****************************************************************************80
#
## RC_TEST2 checks RC by examining special values.
#
#  Discussion:
#
#    This driver compares values of (LOG X)/(X-1) and ARCTAN(X)
#    calculated on one hand from the subroutine RC and on the other
#    from library LOG and ARCTAN routines.  to avoid over/underflows
#    for extreme values of X, we write (LOG X)/(X-1) = RC(Y,X/Y)/SQRT(Y),
#    where Y = (1+X)/2, and ARCTAN(X) = SQRT(X)*RC(Z,Z+X), where Z = 1/X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2018
#
#  Author:
#
#    Original FORTRAN77 version by Bille Carlson, Elaine Notis.
#    This Python version by John Burkardt.
#
  import numpy as np

  x_vec = np.array ( [ \
   1.0E-75, \
   1.0E-15, \
   1.0E-03, \
   1.0E-01, \
   2.0E-01, \
   5.0E-01, \
   1.0E+00, \
   2.0E+00, \
   5.0E+00, \
   1.0E+01, \
   1.0E+03, \
   1.0E+15, \
   1.0E+75 ] )

  print ( '' )
  print ( 'RC_TEST2' )
  print ( '  Compare LOG(X)/(X-1) and ARCTAN(X) with' )
  print ( '  values based on RC.' )

  print ( '' )
  print ( '     X               From LOG                   From RC' )
  print ( '' )

  errtol = 1.0E-3

  for j in range ( 1, 11 ):
    x = 0.2 * j
    y = ( 1.0 + x ) / 2.0
    v = x / y
    value, ierr = rc ( y, v, errtol )
    mylog = value / np.sqrt ( y )
    if ( j == 5 ):
      print ( '%9.1g     ***** ZERO DIVIDE *****%27.16g' % ( x, mylog ) )
    else:
      ibmlog = np.log ( x ) / ( x - 1.0 )
      print ( '%9.1g     %27.16g%27.16g' % ( x, ibmlog, mylog ) )

  print ( '' )
  print ( '  Extreme values of X' )
  print ( '' )
  print ( '     X               From LOG                   From RC' )
  print ( '' )

  for i in range ( 0, 16 ):
    ipower = - 75 + 10 * i
    x = 10.0 ** ipower
    y = ( 1.0 + x ) / 2.0
    v = x / y
    value, ierr = rc ( y, v, errtol )
    mylog = value / np.sqrt ( y )
    ibmlog = np.log ( x ) / ( x - 1.0 )
    print ( '%9.1g     %27.16g%27.16g'  % ( x, ibmlog, mylog ) )

  print ( '' )
  print ( '     X              From ARCTAN                 From RC' )
  print ( '' )

  for m in range ( 0, 13 ):
    x = x_vec[m]
    z = 1.0 / x
    w = z + x
    value, ierr = rc ( z, w, errtol )
    myarc = np.sqrt ( x ) * value
    ibmarc = np.arctan ( x )
    print ( '%9.1g     %27.16g%27.16g' % ( x, ibmarc, myarc ) )

  return

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
  print ( '               X                          Y          ' ),
  print ( '                Z                         RD(X,Y,Z)' )
  print ( '' )

  errtol = 1.0E-3

  for i in range ( 0, 27 ):
    eliptc, ierr = rd ( x[i], y[i], z[i], errtol )
    if (ierr == 0 ):
      print ( '%27.16g%27.16g%27.16g%27.16g' % ( x[i], y[i], z[i], eliptc ) )
    else:
      print ( '%27.16g%27.16g%27.16g  ***Error***' % ( x[i], y[i], z[i] ) )

  return

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
  print ( '               X                          Y          ' ),
  print ( '                Z                         RF(X,Y,Z)' )
  print ( '' )

  errtol = 1.0E-3

  for i in range ( 0, 55 ):
    eliptc, ierr = rf ( x[i], y[i], z[i], errtol )
    if (ierr == 0 ):
      print ( '%27.16g%27.16g%27.16g%27.16g' % ( x[i], y[i], z[i], eliptc ) )
    else:
      print ( '%27.16g%27.16g%27.16g  ***Error***' % ( x[i], y[i], z[i] ) )

  return

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
  print ( '               X                          Y          ' ),
  print ( '                Z                         P' ),
  print ( '                RJ(X,Y,Z,P)' )
  print ( '' )

  errtol = 1.0E-3

  for i in range ( 0, 42 ):
    eliptc, ierr = rj ( x[i], y[i], z[i], p[i], errtol )
    if ( ierr == 0 ):
      print ( '%27.16g%27.16g%27.16g%27.16g%27.16g' % ( x[i], y[i], z[i], p[i], eliptc ) )
    else:
      print ( '%27.16g%27.16g%27.16g%27.16g  ***Error***' % ( x[i], y[i], z[i], p[i] ) )

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

def toms577_test ( ):

#*****************************************************************************80
#
## TOMS577_TEST tests TOMS577.
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
  import platform

  print ( '' )
  print ( 'TOMS577_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TOMS577 evaluates Carlsons elliptic functions.' )

  rc_test ( )
  rc_test2 ( )
  rd_test ( )
  rf_test ( )
  rj_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TOMS577_TEST' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  toms577_test ( )
  timestamp ( )
