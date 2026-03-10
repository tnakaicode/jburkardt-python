#! /usr/bin/env python3
#
def asa226_test ( ):

#*****************************************************************************80
#
## asa226_test() tests asa226().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa226_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa226().' )

  asa226_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa226_test():' )
  print ( '  Normal end of execution.' )

  return

def asa226_test01 ( ):

#*****************************************************************************80
#
## asa226_test01() tests betanc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'asa226_test01():' )
  print ( '  betanc() computes the noncentral incomplete beta function.' )
  print ( '  Compare to tabulated values.' )
  print ( '' )
  print ( '      A       B   LAMBDA      X       ', end = '' )
  print ( 'FX                        FX2' )
  print ( '                                      ', end = '' )
  print ( '(Tabulated)              (BETANC)                DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, lam, x, fx = beta_noncentral_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, ifault = betanc ( x, a, b, lam )

    print ( '  %6.2f  %6.2f  %6.2f  %6.2f  %24.16e  %24.16e  %10.4e' \
      % ( a, b, lam, x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

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
#    23 December 2015
#
#  Author:
#
#    Original FORTRAN77 versionby KL Majumder, GP Bhattacharjee.
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
#    real P, Q, the parameters, which
#    must be positive.
#
#    real BETA, the logarithm of the complete
#    beta function.
#
#  Output:
#
#    real VALUE, the value of the incomplete Beta function ratio.
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

def betanc ( x, a, b, lam ):

#*****************************************************************************80
#
## betanc() computes the tail of the noncentral Beta distribution.
#
#  Discussion:
#
#    This routine returns the cumulative probability of X for the non-central
#    Beta distribution with parameters A, B and non-centrality LAM.
#
#    Note that if LAM = 0, the standard Beta distribution is defined.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 August 2022
#
#  Author:
#
#    Original FORTRAN77 version by Russell Lenth.
#    This version by John Burkardt.
#
#  Reference:
#
#    Russell Lenth,
#    Algorithm AS 226:
#    Computing Noncentral Beta Probabilities,
#    Applied Statistics,
#    Volume 36, Number 2, 1987, pages 241-244.
#
#    H Frick,
#    Algorithm AS R84:
#    A Remark on Algorithm AS 226:
#    Computing Noncentral Beta Probabilities,
#    Applied Statistics,
#    Volume 39, Number 2, 1990, pages 311-312.
#
#  Input:
#
#    real X, the value defining the cumulative
#    probability lower tail.  Normally, 0 <= X <= 1, but any value
#    is allowed.
#
#    real A, B, the parameters of the distribution.
#    0 < A, 0 < B.
#
#    real LAM, the noncentrality parameter
#    of the distribution.  0 <= LAM.  The program can produce reasonably
#    accurate results for values of LAM up to about 100.
#
#  Output:
#
#    real VALUE, the cumulative probability of X.
#
#    integer IFAULT, error flag.
#    0, no error occurred.
#    nonzero, an error occurred.
#
  from scipy.special import gammaln
  import numpy as np

  errmax = 1.0E-07
  itrmax = 150
  ualpha = 5.0

  ifault = 0

  if ( lam < 0.0 or a <= 0.0 or b <= 0.0 ):
    ifault = 2
    value = -1.0
    return value, ifault

  if ( x <= 0.0 ):
    value = 0.0
    return value, ifault

  if ( 1.0 <= x ):
    value = 1.0
    return value, ifault

  c = 0.5 * lam
#
#  Initialize the series.
#
  beta = gammaln ( a ) \
       + gammaln ( b ) \
       - gammaln ( a + b )

  temp, ifault = betain ( x, a, b, beta )

  gx = np.exp ( a * np.log ( x ) + b * np.log ( 1.0 - x ) \
                - beta - np.log ( a ) )

  q = np.exp ( - c )

  xj = 0.0
  ax = q * temp
  sumq = 1.0 - q
  value = ax
#
#  Recur over subsequent terms until convergence is achieved.
#
  ifault = 1

  while ( True ):

    xj = xj + 1.0
    temp = temp - gx
    gx = x * ( a + b + xj - 1.0 ) * gx / ( a + xj )
    q = q * c / xj
    sumq = sumq - q
    ax = temp * q
    value = value + ax
#
#  Check for convergence and act accordingly.
#
    errbd = np.abs ( ( temp - gx ) * sumq )

    if ( errbd <= errmax ):
      ifault = 0
      break

    if (  itrmax < xj ):
      break

  return value, ifault

def beta_noncentral_cdf_values ( n_data ):

#*****************************************************************************80
#
## beta_noncentral_cdf_values() returns some values of the noncentral Beta CDF.
#
#  Discussion:
#
#    The values presented here are taken from the reference, where they
#    were given to a limited number of decimal places.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#    R Chattamvelli, R Shanmugam,
#    Algorithm AS 310:
#    Computing the Non-central Beta Distribution Function,
#    Applied Statistics,
#    Volume 46, Number 1, 1997, pages 146-156.
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
#    rea A, B, the shape parameters.
#
#    real LAMDA, the noncentrality parameter.
#    It is necessary to misspell LAMBDA since Python uses it as a keyword.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 25

  a_vec = np.array ( ( \
        5.0, \
        5.0, \
        5.0, \
       10.0, \
       10.0, \
       10.0, \
       20.0, \
       20.0, \
       20.0, \
       10.0, \
       10.0, \
       15.0, \
       20.0, \
       20.0, \
       20.0, \
       30.0, \
       30.0, \
       10.0, \
       10.0, \
       10.0, \
       15.0, \
       10.0, \
       12.0, \
       30.0, \
       35.0  ))

  b_vec = np.array ( ( \
        5.0, \
        5.0, \
        5.0, \
       10.0, \
       10.0, \
       10.0, \
       20.0, \
       20.0, \
       20.0, \
       20.0, \
       10.0, \
        5.0, \
       10.0, \
       30.0, \
       50.0, \
       20.0, \
       40.0, \
        5.0, \
       10.0, \
       30.0, \
       20.0, \
        5.0, \
       17.0, \
       30.0, \
       30.0 ))

  f_vec = np.array ( ( \
       0.4563021, \
       0.1041337, \
       0.6022353, \
       0.9187770, \
       0.6008106, \
       0.0902850, \
       0.9998655, \
       0.9925997, \
       0.9641112, \
       0.9376626573, \
       0.7306817858, \
       0.1604256918, \
       0.1867485313, \
       0.6559386874, \
       0.9796881486, \
       0.1162386423, \
       0.9930430054, \
       0.0506899273, \
       0.1030959706, \
       0.9978417832, \
       0.2555552369, \
       0.0668307064, \
       0.0113601067, \
       0.7813366615, \
       0.8867126477 ) )

  lamda_vec = np.array ( ( \
        54.0, \
       140.0, \
       170.0, \
        54.0, \
       140.0, \
       250.0, \
        54.0, \
       140.0, \
       250.0, \
       150.0, \
       120.0, \
        80.0, \
       110.0, \
        65.0, \
       130.0, \
        80.0, \
       130.0, \
        20.0, \
        54.0, \
        80.0, \
       120.0, \
        55.0, \
        64.0, \
       140.0, \
        20.0 ))

  x_vec = np.array ( ( \
       0.8640, \
       0.9000, \
       0.9560, \
       0.8686, \
       0.9000, \
       0.9000, \
       0.8787, \
       0.9000, \
       0.9220, \
       0.868, \
       0.900, \
       0.880, \
       0.850, \
       0.660, \
       0.720, \
       0.720, \
       0.800, \
       0.644, \
       0.700, \
       0.780, \
       0.760, \
       0.795, \
       0.560, \
       0.800, \
       0.670   ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    lamda = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    lamda = lamda_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, lamda, x, f

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
  asa226_test ( )
  timestamp ( )


