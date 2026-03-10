#! /usr/bin/env python3
#
def asa243_test ( ):

#*****************************************************************************80
#
## asa243_test() tests asa243().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa243_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa243().' )

  asa243_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa243_test():' )
  print ( '  Normal end of execution.' )

  return

def asa243_test01 ( ):

#*****************************************************************************80
#
## asa243_test01() tests tnc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'asa243_test01():' )
  print ( '  tnc() computes the noncentral Student T ' )
  print ( '  Cumulative Density Function.' )
  print ( '  Compare with tabulated values.' )
  print ( '' )
  print ( '        X         LAMBDA        DF     ', end = '' )
  print ( ' CDF             CDF           DIFF' )
  print ( '                                       ', end = '' )
  print ( ' Tabulated       PRNCST' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, df, delta, x, fx = student_noncentral_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, ifault = tnc ( x, df, delta )

    print ( '  %10.4f  %10.4f  %8d  %14.6e  %14.6e  %10.4e' \
      % ( x, delta, df, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

def alnorm ( x, upper ):

#*****************************************************************************80
#
## alnorm() computes the cumulative density of the standard normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2022
#
#  Author:
#
#    Original FORTRAN77 version by David Hill.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Hill,
#    Algorithm AS 66:
#    The Normal Integral,
#    Applied Statistics,
#    Volume 22, Number 3, 1973, pages 424-427.
#
#  Input:
#
#    real X, is one endpoint of the semi-infinite interval
#    over which the integration takes place.
#
#    logical UPPER, determines whether the upper or lower
#    interval is to be integrated:
#    1 => integrate from X to + Infinity
#    0 => integrate from - Infinity to X.
#
#  Output:
#
#    real VALUE, the integral of the standard normal
#    distribution over the desired interval.
#
  import numpy as np

  a1 = 5.75885480458 
  a2 = 2.62433121679 
  a3 = 5.92885724438 
  b1 = -29.8213557807 
  b2 = 48.6959930692 
  c1 = -0.000000038052 
  c2 = 0.000398064794 
  c3 = -0.151679116635 
  c4 = 4.8385912808 
  c5 = 0.742380924027 
  c6 = 3.99019417011
  con = 1.28
  d1 = 1.00000615302
  d2 = 1.98615381364
  d3 = 5.29330324926
  d4 = -15.1508972451
  d5 = 30.789933034
  ltone = 7.0
  p = 0.39894228044 
  q = 0.39990348504
  r = 0.398942280385
  utzero = 18.66

  up = upper
  z = x

  if ( z < 0.0 ):
    if ( up ):
      up = 0
    else:
      up = 1
    z = - z

  if ( ltone < z and ( ( not up ) or utzero < z ) ):

    if ( up ):
      value = 0.0
    else:
      value = 1.0
 
    return value

  y = 0.5 * z * z

  if ( z <= con ):

    value = 0.5  - z * ( p - q * y \
      / ( y + a1 + b1 \
      / ( y + a2 + b2 \
      / ( y + a3 ))))

  else:

    value = r * np.exp ( - y ) \
      / ( z + c1 + d1 \
      / ( z + c2 + d2 \
      / ( z + c3 + d3 \
      / ( z + c4 + d4 \
      / ( z + c5 + d5 \
      / ( z + c6 ))))))

  if ( not up ):
    value = 1.0  - value

  return value

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

def student_noncentral_cdf_values ( n_data ):

#*****************************************************************************80
#
## student_noncentral_cdf_values() returns values of the noncentral Student CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NoncentralStudentTDistribution [ df, lambda ]
#      CDF [ dist, x ]
#
#    Mathematica seems to have some difficulty computing this function
#    to the desired number of digits.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2015
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
#    integer DF, real LAM, the parameters of the
#    function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 30

  df_vec = np.array ( ( \
     1,  2,  3, \
     1,  2,  3, \
     1,  2,  3, \
     1,  2,  3, \
     1,  2,  3, \
    15, 20, 25, \
     1,  2,  3, \
    10, 10, 10, \
    10, 10, 10, \
    10, 10, 10 ))

  f_vec = np.array ( ( \
     0.8975836176504333E+00, \
     0.9522670169E+00, \
     0.9711655571887813E+00, \
     0.8231218864E+00, \
     0.9049021510E+00, \
     0.9363471834E+00, \
     0.7301025986E+00, \
     0.8335594263E+00, \
     0.8774010255E+00, \
     0.5248571617E+00, \
     0.6293856597E+00, \
     0.6800271741E+00, \
     0.20590131975E+00, \
     0.2112148916E+00, \
     0.2074730718E+00, \
     0.9981130072E+00, \
     0.9994873850E+00, \
     0.9998391562E+00, \
     0.168610566972E+00, \
     0.16967950985E+00, \
     0.1701041003E+00, \
     0.9247683363E+00, \
     0.7483139269E+00, \
     0.4659802096E+00, \
     0.9761872541E+00, \
     0.8979689357E+00, \
     0.7181904627E+00, \
     0.9923658945E+00, \
     0.9610341649E+00, \
     0.8688007350E+00 ))

  lam_vec = np.array ( ( \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     2.0E+00, \
     2.0E+00, \
     2.0E+00, \
     4.0E+00, \
     4.0E+00, \
     4.0E+00, \
     7.0E+00, \
     7.0E+00, \
     7.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00, \
     2.0E+00, \
     3.0E+00, \
     4.0E+00 ))

  x_vec = np.array ( ( \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
      3.00E+00, \
     15.00E+00, \
     15.00E+00, \
     15.00E+00, \
      0.05E+00, \
      0.05E+00, \
      0.05E+00, \
      4.00E+00, \
      4.00E+00, \
      4.00E+00, \
      5.00E+00, \
      5.00E+00, \
      5.00E+00, \
      6.00E+00, \
      6.00E+00, \
      6.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    df = 0
    lam = 0.0
    x = 0.0
    f = 0.0
  else:
    df = df_vec[n_data]
    lam = lam_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, df, lam, x, f

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

def tnc ( t, df, delta ):

#*****************************************************************************80
#
## tnc() computes the tail of the noncentral T distribution.
#
#  Discussion:
#
#    This routine computes the cumulative probability at T of the
#    non-central T-distribution with DF degrees of freedom (which may
#    be fractional) and non-centrality parameter DELTA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    Original FORTRAN77 version by Russell Lenth.
#    This version by John Burkardt.
#
#  Reference:
#
#    Russell Lenth,
#    Algorithm AS 243:
#    Cumulative Distribution Function of the Non-Central T Distribution,
#    Applied Statistics,
#    Volume 38, Number 1, 1989, pages 185-189.
#
#    William Guenther,
#    Evaluation of probabilities for the noncentral distributions and
#    difference of two T-variables with a desk calculator,
#    Journal of Statistical Computation and Simulation,
#    Volume 6, Number 3-4, 1978, pages 199-206.
#
#  Input:
#
#    real T, the point whose cumulative probability is desired.
#
#    real DF, the number of degrees of freedom.
#
#    real DELTA, the noncentrality parameter.
#
#  Output:
#
#    real VALUE, the tail of the noncentral T distribution.
#
#    integer IFAULT, error flag.
#    0, no error.
#    nonzero, an error occcurred.
#
  from scipy.special import gammaln
  import numpy as np

  alnrpi = 0.57236494292470008707
  errmax = 1.0E-10
  itrmax = 100
  r2pi = 0.79788456080286535588

  value = 0.0

  if ( df <= 0.0 ):
    ifault = 2
    return value, ifault

  ifault = 0

  tt = t
  delt = delta
  negdel = 0

  if ( t < 0.0 ):
    negdel = 1
    tt = - tt
    delt = - delt
#
#  Initialize twin series.
#
  en = 1.0
  x = t * t / ( t * t + df )

  if ( x <= 0.0 ):

    ifault = 0
    value = value + alnorm ( delt, 1 )

    if ( negdel ):
      value = 1.0 - value

    return value, ifault

  lam = delt * delt
  p = 0.5 * np.exp ( - 0.5 * lam )
  q = r2pi * p * delt
  s = 0.5 - p
  a = 0.5
  b = 0.5 * df
  rxb = ( 1.0 - x ) ** b
  albeta = alnrpi + gammaln ( b ) - gammaln ( a + b )
  xodd, ifault = betain ( x, a, b, albeta )
  godd = 2.0 * rxb * np.exp ( a * np.log ( x ) - albeta )
  xeven = 1.0 - rxb
  geven = b * x * rxb
  value = p * xodd + q * xeven
#
#  Repeat until convergence.
#
  while ( True ):

    a = a + 1.0
    xodd = xodd - godd
    xeven = xeven - geven
    godd = godd * x * ( a + b - 1.0 ) / a
    geven = geven * x * ( a + b - 0.5 ) / ( a + 0.5 )
    p = p * lam / ( 2.0 * en )
    q = q * lam / ( 2.0 * en + 1.0 )
    s = s - p
    en = en + 1.0
    value = value + p * xodd + q * xeven
    errbd = 2.0 * s * ( xodd - godd )

    if ( errbd <= errmax ):
      ifault = 0
      break

    if ( itrmax < en ):
      ifault = 1
      break

  value = value + alnorm ( delt, 1 )

  if ( negdel ):
    value = 1.0 - value

  return value, ifault

if ( __name__ == '__main__' ):
  timestamp ( )
  asa243_test ( )
  timestamp ( )


