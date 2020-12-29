#! /usr/bin/env python3
#
def alogam ( x ):

#*****************************************************************************80
#
## ALOGAM computes the logarithm of the Gamma function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    Original FORTRAN77 version by Malcolm Pike, David Hill.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Malcolm Pike, David Hill,
#    Algorithm 291:
#    Logarithm of Gamma Function,
#    Communications of the ACM,
#    Volume 9, Number 9, September 1966, page 684.
#
#  Parameters:
#
#    Input, real X, the argument of the Gamma function.
#    X should be greater than 0.
#
#    Output, real ALOGAM, the logarithm of the Gamma
#    function of X.
#
  import numpy as np

  if ( x <= 0.0 ):
    value = 0.0
    return value

  y = x

  if ( x < 7.0 ):

    f = 1.0
    z = y

    while ( z < 7.0 ):
      f = f * z
      z = z + 1.0

    y = z
    f = - np.log ( f )

  else:

    f = 0.0

  z = 1.0 / y / y

  value = f + ( y - 0.5 ) * np.log ( y ) - y \
    + 0.918938533204673 + \
    ((( \
    - 0.000595238095238   * z \
    + 0.000793650793651 ) * z \
    - 0.002777777777778 ) * z \
    + 0.083333333333333 ) / y

  return value

def alogam_test ( ):

#*****************************************************************************80
#
## ALOGAM_TEST tests ALOGAM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ALOGAM_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ALOGAM evaluates the logarithm of the gamma function.' )
  print ( '' )
  print ( '      X            GAMMA_LOG(X)            GAMMA_LOG(X)' )
  print ( '      X            tabulated               computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = alogam ( x )

    print ( '  %12f  %24.16g  %24.16g' % ( x, fx1, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ALOGAM_TEST:' )
  print ( '  Normal end of execution.' )

  return

def asa063_test ( ):

#*****************************************************************************80
#
## ASA063_TEST tests the ASA063 library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ASA063_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the ASA063 library.' )

  alogam_test ( )
  beta_inc_values_test ( )
  betain_test ( )
  gamma_log_values_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ASA063_TEST:' )
  print ( '  Normal end of execution.' )
  return

def beta_inc_values ( n_data ):

#*****************************************************************************80
#
## BETA_INC_VALUES returns some values of the incomplete Beta function.
#
#  Discussion:
#
#    The incomplete Beta function may be written
#
#      BETA_INC(A,B,X) = Integral (0 to X) T^(A-1) * (1-T)^(B-1) dT
#                      / Integral (0 to 1) T^(A-1) * (1-T)^(B-1) dT
#
#    Thus,
#
#      BETA_INC(A,B,0.0) = 0.0;
#      BETA_INC(A,B,1.0) = 1.0
#
#    The incomplete Beta function is also sometimes called the
#    "modified" Beta function, or the "normalized" Beta function
#    or the Beta CDF (cumulative density function).
#
#    In Mathematica, the function can be evaluated by:
#
#      BETA[X,A,B] / BETA[A,B]
#
#    The function can also be evaluated by using the Statistics package:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = BetaDistribution [ a, b ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Karl Pearson,
#    Tables of the Incomplete Beta Function,
#    Cambridge University Press, 1968.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real A, B, the parameters of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 45

  a_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      1.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      5.5E+00, \
     10.0E+00, \
     10.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     20.0E+00, \
     30.0E+00, \
     30.0E+00, \
     40.0E+00, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.1E+01, \
      0.2E+01, \
      0.3E+01, \
      0.4E+01, \
      0.5E+01, \
      1.30625, \
      1.30625, \
      1.30625 ))

  b_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      2.0E+00, \
      5.0E+00, \
      0.5E+00, \
      5.0E+00, \
      5.0E+00, \
     10.0E+00, \
      5.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     20.0E+00, \
     10.0E+00, \
     10.0E+00, \
     20.0E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.2E+01, \
     0.3E+01, \
     0.4E+01, \
     0.5E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
     0.2E+01, \
    11.7562, \
    11.7562, \
    11.7562 ))

  f_vec = np.array ( ( \
     0.6376856085851985E-01, \
     0.2048327646991335E+00, \
     0.1000000000000000E+01, \
     0.0000000000000000E+00, \
     0.5012562893380045E-02, \
     0.5131670194948620E-01, \
     0.2928932188134525E+00, \
     0.5000000000000000E+00, \
     0.2800000000000000E-01, \
     0.1040000000000000E+00, \
     0.2160000000000000E+00, \
     0.3520000000000000E+00, \
     0.5000000000000000E+00, \
     0.6480000000000000E+00, \
     0.7840000000000000E+00, \
     0.8960000000000000E+00, \
     0.9720000000000000E+00, \
     0.4361908850559777E+00, \
     0.1516409096347099E+00, \
     0.8978271484375000E-01, \
     0.1000000000000000E+01, \
     0.5000000000000000E+00, \
     0.4598773297575791E+00, \
     0.2146816102371739E+00, \
     0.9507364826957875E+00, \
     0.5000000000000000E+00, \
     0.8979413687105918E+00, \
     0.2241297491808366E+00, \
     0.7586405487192086E+00, \
     0.7001783247477069E+00, \
     0.5131670194948620E-01, \
     0.1055728090000841E+00, \
     0.1633399734659245E+00, \
     0.2254033307585166E+00, \
     0.3600000000000000E+00, \
     0.4880000000000000E+00, \
     0.5904000000000000E+00, \
     0.6723200000000000E+00, \
     0.2160000000000000E+00, \
     0.8370000000000000E-01, \
     0.3078000000000000E-01, \
     0.1093500000000000E-01, \
     0.918884684620518, \
     0.21052977489419, \
     0.1824130512500673 ) )

  x_vec = np.array ( ( \
     0.01E+00, \
     0.10E+00, \
     1.00E+00, \
     0.00E+00, \
     0.01E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.90E+00, \
     0.50E+00, \
     0.90E+00, \
     0.50E+00, \
     1.00E+00, \
     0.50E+00, \
     0.80E+00, \
     0.60E+00, \
     0.80E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.70E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.30E+00, \
     0.30E+00, \
     0.30E+00, \
     0.30E+00, \
     0.225609, \
     0.0335568, \
     0.0295222  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, x, f

def beta_inc_values_test ( ):

#*****************************************************************************80
#
## BETA_INC_VALUES_TEST demonstrates the use of BETA_INC_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BETA_INC_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BETA_INC_VALUES stores values of the BETA function.' )
  print ( '' )
  print ( '      A         B         X        BETA_INC(A,B,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, f = beta_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %12g  %24.16g' % ( a, b, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BETA_INC_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def betain ( x, p, q, beta ):

#*****************************************************************************80
#
## BETAIN computes the incomplete Beta function ratio.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    Original FORTRAN77 versionby KL Majumder, GP Bhattacharjee.
#    Python version by John Burkardt.
#
#  Reference:
#
#    KL Majumder, GP Bhattacharjee,
#    Algorithm AS 63:
#    The incomplete Beta Integral,
#    Applied Statistics,
#    Volume 22, Number 3, 1973, pages 409-411.
#
#  Parameters:
#
#    Input, real X, the argument, between 0 and 1.
#
#    Input, real P, Q, the parameters, which
#    must be positive.
#
#    Input, real BETA, the logarithm of the complete
#    beta function.
#
#    Output, real BETAIN, the value of the incomplete
#    Beta function ratio.
#
#    Output, integer IFAULT, error flag.
#    0, no error.
#    nonzero, an error occurred.
#
  import numpy as np

  acu = 0.1E-14

  value = x
  ifault = 0
#
#  Check the input arguments.
#
  if ( p <= 0.0 or q <= 0.0 ):
    ifault = 1
    return value, ifault

  if ( x < 0.0 or 1.0 < x ):
    ifault = 2
    return value, ifault
#
#  Special cases.
#
  if ( x == 0.0 or x == 1.0 ):
    return value, ifault
#
#  Change tail if necessary and determine S.
#
  psq = p + q
  cx = 1.0 - x

  if ( p < psq * x ):
    xx = cx
    cx = x
    pp = q
    qq = p
    indx = 1
  else:
    xx = x
    pp = p
    qq = q
    indx = 0

  term = 1.0
  ai = 1.0
  value = 1.0
  ns = np.floor ( qq + cx * psq )
#
#  Use the Soper reduction formula.
#
  rx = xx / cx
  temp = qq - ai
  if ( ns == 0 ):
    rx = xx

  while ( True ):

    term = term * temp * rx / ( pp + ai )
    value = value + term
    temp = abs ( term )

    if ( temp <= acu and temp <= acu * value ):

      value = value * np.exp ( pp * np.log ( xx ) \
      + ( qq - 1.0 ) * np.log ( cx ) - beta ) / pp

      if ( indx ):
        value = 1.0 - value

      break

    ai = ai + 1.0
    ns = ns - 1

    if ( 0 <= ns ):
      temp = qq - ai
      if ( ns == 0 ):
        rx = xx
    else:
      temp = psq
      psq = psq + 1.0

  return value, ifault

def betain_test ( ):

#*****************************************************************************80
#
## ASA063_TEST01 demonstrates the use of BETAIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BETAIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BETAIN computes the incomplete beta function.' )
  print ( '  Compare to tabulated values.' )
  print ( '' )
  print ( '      A       B       X     FX                       FX2' )
  print ( '                            (Tabulated)              (BETAIN)                DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, fx = beta_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    beta_log = alogam ( a ) \
             + alogam ( b ) \
             - alogam ( a + b )

    fx2, ifault = betain ( x, a, b, beta_log )

    print ( '  %6.2f  %6.2f  %6.2f  %24.16e  %24.16e  %10.4e' \
      % ( a, b, x, fx, fx2, abs ( fx - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BETAIN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def gamma_log_values ( n_data ):

#*****************************************************************************80
#
## GAMMA_LOG_VALUES returns some values of the Log Gamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[Gamma[x]]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
      0.1524063822430784E+01, \
      0.7966778177017837E+00, \
      0.3982338580692348E+00, \
      0.1520596783998375E+00, \
      0.0000000000000000E+00, \
     -0.4987244125983972E-01, \
     -0.8537409000331584E-01, \
     -0.1081748095078604E+00, \
     -0.1196129141723712E+00, \
     -0.1207822376352452E+00, \
     -0.1125917656967557E+00, \
     -0.9580769740706586E-01, \
     -0.7108387291437216E-01, \
     -0.3898427592308333E-01, \
     0.00000000000000000E+00, \
     0.69314718055994530E+00, \
     0.17917594692280550E+01, \
     0.12801827480081469E+02, \
     0.39339884187199494E+02, \
     0.71257038967168009E+02 ) )

  x_vec = np.array ( ( \
      0.20E+00, \
      0.40E+00, \
      0.60E+00, \
      0.80E+00, \
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
      3.00E+00, \
      4.00E+00, \
     10.00E+00, \
     20.00E+00, \
     30.00E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def gamma_log_values_test ( ):

#*****************************************************************************80
#
## GAMMA_LOG_VALUE_TEST demonstrates the use of GAMMA_LOG_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 February 2009
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GAMMA_LOG_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GAMMA_LOG_VALUES stores values of' )
  print ( '  the logarithm of the Gamma function.' )
  print ( '' )
  print ( '      X            GAMMA_LOG(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, fx ) )

  print ( '' )
  print ( 'GAMMA_LOG_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
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
  asa063_test ( )
  timestamp ( )

