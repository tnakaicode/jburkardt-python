#! /usr/bin/env python
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
  print ( '              X                          Y                         RC(X,Y)' )
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

if ( __name__ == '__main__' ):
  from timestamp import timestamp 
  timestamp ( )
  rc_test ( )
  rc_test2 ( )
  timestamp ( )
