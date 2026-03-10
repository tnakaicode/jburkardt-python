#! /usr/bin/env python3
#
def asa109_test ( ):

#*****************************************************************************80
#
## asa109_test() tests asa109().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa109_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa109().' )

  asa109_test01 ( )
  asa109_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa109_test()' )
  print ( '  Normal end of execution.' )

  return

def asa109_test01 ( ):

#*****************************************************************************80
#
## asa109_test01() tests xinbta().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import gammaln
  import numpy as np

  print ( '' )
  print ( 'asa109_test01():' )
  print ( '  xinbta() inverts the incomplete beta function.' )
  print ( '' )
  print ( '      A        B         CDF     ', end = '' )
  print ( ' X                         X' )
  print ( '                                 ', end = '' )
  print ( '(Tabulated)               (XINBTA)                DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, fx = beta_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    beta_log = gammaln ( a ) \
             + gammaln ( b ) \
             - gammaln ( a + b )

    x2, ifault = xinbta ( a, b, beta_log, fx )

    print ( '  %6.2f  %6.2f  %10.4f  %24.16e  %24.16e  %10.4e' \
      % ( a, b, fx, x, x2, np.abs ( x - x2 ) ) )

  return

def asa109_test02 ( ):

#*****************************************************************************80
#
## asa109_test02() tests beta_inc_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import gammaln
  import numpy as np

  print ( '' )
  print ( 'asa109_test02():' )
  print ( '  beta_inc_values() stores values of' )
  print ( '  the incomplete Beta function.' )
  print ( '' )
  print ( '      A            B            X            BETA_INC(A,B)(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, fx = beta_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    beta_log = gammaln ( a ) \
             + gammaln ( b ) \
             - gammaln ( a + b )

    fx2, ifault = betain ( x, a, b, beta_log )

    print ( '  %6.2f  %6.2f  %10.4f  %24.16e  %24.16e  %10.4e' \
      % ( a, b, x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

def beta_inc_values ( n_data ):

#*****************************************************************************80
#
## beta_inc_values() returns some values of the incomplete Beta function.
#
#  Discussion:
#
#    The incomplete Beta function may be written
#
#      beta_inc(A,B,X) = Integral (0 to X) T^(A-1) * (1-T)^(B-1) dT
#                      / Integral (0 to 1) T^(A-1) * (1-T)^(B-1) dT
#
#    Thus,
#
#      beta_inc(A,B,0.0) = 0.0;
#      beta_inc(A,B,1.0) = 1.0
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
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
#  Input:
#
#    integer N_data.  The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer N_data.  On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    real A, B, the parameters of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
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

def betain ( x, p, q, beta ):

#*****************************************************************************80
#
## betain() computes the incomplete Beta function ratio.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    Original FORTRAN77 version by KL Majumder, GP Bhattacharjee.
#    This version by John Burkardt.
#
#  Reference:
#
#    KL Majumder, GP Bhattacharjee,
#    Algorithm AS 63:
#    The incomplete Beta Integral,
#    Applied Statistics,
#    Volume 22, Number 3, 1973, pages 409-411.
#
#  Input:
#
#    real X, the argument, between 0 and 1.
#
#    real P, Q, the parameters, which must be positive.
#
#    real BETA, the logarithm of the complete beta function.
#
#  Output:
#
#    real BETAIN, the value of the incomplete Beta function ratio.
#
#    integer IFAULT, error flag.
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
    temp = np.abs ( term )

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

def xinbta ( p, q, beta, alpha ):

#*****************************************************************************80
#
## xinbta() computes inverse of the incomplete Beta function.
#
#  Discussion:
#
#    The accuracy exponent SAE was loosened from -37 to -30, because
#    the code would not otherwise accept the results of an iteration
#    with p = 0.3, q = 3.0, alpha = 0.2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    Original FORTRAN77 version by GW Cran, KJ Martin, GE Thomas.
#    This version by John Burkardt.
#
#  Reference:
#
#    GW Cran, KJ Martin, GE Thomas,
#    Remark AS R19 and Algorithm AS 109:
#    A Remark on Algorithms AS 63: The Incomplete Beta Integral
#    and AS 64: Inverse of the Incomplete Beta Integeral,
#    Applied Statistics,
#    Volume 26, Number 1, 1977, pages 111-114.
#
#  Input:
#
#    real P, Q, the parameters of the incomplete Beta function.
#
#    real BETA, the logarithm of the value of
#    the complete Beta function.
#
#    real ALPHA, the value of the incomplete Beta
#    function.  0 <= ALPHA <= 1.
#
#  Output:
#
#    real VALUE, the argument of the incomplete
#    Beta function which produces the value ALPHA.
#
#    integer IFAULT, error flag.
#    0, no error occurred.
#    nonzero, an error occurred.
#
#  Local:
#
#    integer SAE, requests an accuracy of about 10^SAE.
#
  import numpy as np

  sae = -30

  fpu = 10.0 ** sae

  ifault = 0
  value = alpha
#
#  Test for admissibility of parameters.
#
  if ( p <= 0.0 ):
    print ( '' )
    print ( 'xinbta(): Fatal error!' )
    print ( '  P <= 0.0' )
    ifault = 1
    raise Exception ( 'xinbta(): Fatal error!' )

  if ( q <= 0.0 ):
    print ( '' )
    print ( 'xinbta(): Fatal error!' )
    print ( '  Q <= 0.0' )
    ifault = 1
    raise Exception ( 'xinbta(): Fatal error!' )

  if ( alpha < 0.0 or 1.0 < alpha ):
    print ( '' )
    print ( 'xinbta(): Fatal error!' )
    print ( '  ALPHA not between 0 and 1.' )
    ifault = 2
    raise Exception ( 'xinbta(): Fatal error!' )
#
#  If the answer is easy to determine, return immediately.
#
  if ( alpha == 0.0 ):
    value = 0.0
    return value, ifault

  if ( alpha == 1.0 ):
    value = 1.0
    return value, ifault
#
#  Change tail if necessary.
#
  if ( 0.5 < alpha ):
    a = 1.0 - alpha
    pp = q
    qq = p
    indx = 1
  else:
    a = alpha
    pp = p
    qq = q
    indx = 0
#
#  Calculate the initial approximation.
#
  r = np.sqrt ( - np.log ( a * a ) )

  y = r - ( 2.30753 + 0.27061 * r ) \
    / ( 1.0 + ( 0.99229 + 0.04481 * r ) * r )

  if ( 1.0 < pp and 1.0 < qq ):

    r = ( y * y - 3.0 ) / 6.0
    s = 1.0 / ( pp + pp - 1.0 )
    t = 1.0 / ( qq + qq - 1.0 )
    h = 2.0 / ( s + t )
    w = y * np.sqrt ( h + r ) / h - ( t - s ) \
      * ( r + 5.0 / 6.0 - 2.0 / ( 3.0 * h ) )
    value = pp / ( pp + qq * np.exp ( w + w ) )

  else:

    r = qq + qq
    t = 1.0 / ( 9.0 * qq )
    t = r * ( 1.0 - t + y * np.sqrt ( t ) ) ** 3

    if ( t <= 0.0 ):
      value = 1.0 - np.exp ( ( np.log ( ( 1.0 - a ) * qq ) + beta ) / qq )
    else:

      t = ( 4.0 * pp + r - 2.0 ) / t

      if ( t <= 1.0 ):
        value = np.exp ( ( np.log ( a * pp ) + beta ) / pp )
      else:
        value = 1.0 - 2.0 / ( t + 1.0 )
#
#  Solve for X by a modified Newton-Raphson method,
#  using the function BETAIN.
#
  r = 1.0 - pp
  t = 1.0 - qq
  yprev = 0.0
  sq = 1.0
  prev = 1.0

  if ( value < 0.0001 ):
    value = 0.0001

  if ( 0.9999 < value ):
    value = 0.9999

  iex = int ( max ( - 5.0 / pp / pp - 1.0 / a ** 0.2 - 13.0, sae ) )

  acu = 10.0 ** iex
#
#  Iteration loop.
#
  while ( True ):

    y, ifault = betain ( value, pp, qq, beta )

    if ( ifault != 0 ):
      print ( '' )
      print ( 'xinbta(): Fatal error!' )
      print ( '  betain() returns IFAULT =', ifault )
      ifault = 3
      raise Exception ( 'xinbta(): Fatal error!' )

    xin = value
    y = ( y - a ) * np.exp ( beta + r * np.log ( xin ) \
      + t * np.log ( 1.0 - xin ) )

    if ( y * yprev <= 0.0 ):
      prev = max ( sq, fpu )

    g = 1.0

    while ( True ):

      while ( True ):

        adj = g * y
        sq = adj * adj

        if ( sq < prev ):

          tx = value - adj

          if ( 0.0 <= tx and tx <= 1.0 ):
            break

        g = g / 3.0
#
#  Check whether current estimate is acceptable.
#  The change "VALUE = TX" was suggested by Ivan Ukhov.
#
      if ( prev <= acu and y * y <= acu ):
        value = tx
        if ( indx ):
          value = 1.0 - value
        return value, ifault

      if ( tx != 0.0 and tx != 1.0 ):
        break

      g = g / 3.0

    if ( tx == value ):
      break

    value = tx
    yprev = y

  if ( indx ):
    value = 1.0 - value

  return value, ifault

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == "__main__" ):
  timestamp ( )
  asa109_test ( )
  timestamp ( )

