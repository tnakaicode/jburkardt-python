#! /usr/bin/env python3
#
def asa005_test ( ):

#*****************************************************************************80
#
## asa005_test() tests asa005().
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
  print ( 'asa005_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa005().' )

  asa005_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa005_test():' )
  print ( '  Normal end of execution.' )

  return

def asa005_test01 ( ):

#*****************************************************************************80
#
## asa005_test01() tests prncst().
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

  print ( '' )
  print ( 'asa005_test01():' )
  print ( '  prncst() computes the noncentral Student' )
  print ( '  Cumulative Density Function.' )
  print ( '  Compare to tabulated values.' )
  print ( '' )
  print ( '      X   LAMBDA  DF     ', end = '' )
  print ( ' CDF                       CDF                     DIFF' )
  print ( '                         ', end = '' )
  print ( ' Tabulated                 PRNCST' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, df, lamb, x, fx = student_noncentral_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, ifault = prncst ( x, df, lamb )

    print ( '  %6.2f  %6.2f  %2d  %24.16e  %24.16e  %10.4e' \
      % ( x, lamb, df, fx, fx2, np.abs ( fx - fx2 ) ) )

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
#    real X, one endpoint of the semi-infinite interval
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

def prncst ( st, idf, d ):

#*****************************************************************************80
#
## prncst() computes the lower tail of noncentral T distribution.
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
#    Original FORTRAN77 version by BE Cooper.
#    This version by John Burkardt.
#
#  Reference:
#
#    BE Cooper,
#    Algorithm AS 5:
#    The Integral of the Non-Central T-Distribution,
#    Applied Statistics,
#    Volume 17, Number 2, 1968, page 193.
#
#  Input:
#
#    real ST, the argument.
#
#    integer IDF, the number of degrees of freedom.
#
#    real D, the noncentrality parameter.
#
#  Output:
#
#    real PRNCST, the value of the lower tail of
#    the noncentral T distribution.
#
#    integer IFAULT, error flag.
#    0, no error occurred.
#    nonzero, an error occurred.
#
#  Local:
#
#    real G1, 1.0 / sqrt(2.0 * pi)
#
#    real G2, 1.0 / (2.0 * pi)
#
#    real G3, sqrt(2.0 * pi)
#
  from scipy.special import gammaln
  import numpy as np

  emin = 12.5
  g1 = 0.3989422804
  g2 = 0.1591549431
  g3 = 2.5066282746

  f = idf
#
#  For very large IDF, use the normal approximation.
#
  if ( 100 < idf ):

    ifault = 1

    a = np.sqrt ( 0.5 * f ) * np.exp ( gammaln ( 0.5 * ( f - 1.0 ) ) \
    - gammaln ( 0.5 * f ) ) * d

    value = alnorm ( ( st - a ) / np.sqrt ( f * ( 1.0 + d * d ) \
      / ( f - 2.0 ) - a * a ), 0 )

    return value, ifault

  ifault = 0
  ioe = ( idf % 2 )
  a = st / np.sqrt ( f )
  b = f / ( f + st * st )
  rb = np.sqrt ( b )
  da = d * a
  drb = d * rb

  if ( idf == 1 ):
    value = alnorm ( drb, 1 ) + 2.0 * tfn ( drb, a )
    return value, ifault

  if ( np.abs ( drb ) < emin ):
    fmkm2 = a * rb * np.exp ( - 0.5 * drb * drb ) * alnorm ( a * drb, 0 ) * g1
  else:
    fmkm2 = 0.0

  if ( np.abs ( d ) < emin ):
    fmkm1 = b * da * fmkm2 + b * a * g2 * np.exp ( - 0.5 * d * d )
  else:
    fmkm1 = b * da * fmkm2

  if ( ioe == 0 ):
    s = fmkm2
  else:
    s = fmkm1

  ak = 1.0
  fk = 2.0

  for k in range ( 2, idf - 1, 2 ):

    fkm1 = fk - 1.0
    fmkm2 = b * ( da * ak * fmkm1 + fmkm2 ) * fkm1 / fk
    ak = 1.0 / ( ak * fkm1 )
    fmkm1 = b * ( da * ak * fmkm2 + fmkm1 ) * fk / ( fk + 1.0 )

    if ( ioe == 0 ):
      s = s + fmkm2
    else:
      s = s + fmkm1

    ak = 1.0 / ( ak * fk )
    fk = fk + 2.0

  if ( ioe == 0 ):
    value = alnorm ( d, 1 ) + s * g3
  else:
    value = alnorm ( drb, 1 ) + 2.0 * ( s + tfn ( drb, a ) )

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
     0.8975836176504333, \
     0.9522670169, \
     0.9711655571887813, \
     0.8231218864, \
     0.9049021510, \
     0.9363471834, \
     0.7301025986, \
     0.8335594263, \
     0.8774010255, \
     0.5248571617, \
     0.6293856597, \
     0.6800271741, \
     0.20590131975, \
     0.2112148916, \
     0.2074730718, \
     0.9981130072, \
     0.9994873850, \
     0.9998391562, \
     0.168610566972, \
     0.16967950985, \
     0.1701041003, \
     0.9247683363, \
     0.7483139269, \
     0.4659802096, \
     0.9761872541, \
     0.8979689357, \
     0.7181904627, \
     0.9923658945, \
     0.9610341649, \
     0.8688007350 ))

  lam_vec = np.array ( ( \
     0.0, \
     0.0, \
     0.0, \
     0.5, \
     0.5, \
     0.5, \
     1.0, \
     1.0, \
     1.0, \
     2.0, \
     2.0, \
     2.0, \
     4.0, \
     4.0, \
     4.0, \
     7.0, \
     7.0, \
     7.0, \
     1.0, \
     1.0, \
     1.0, \
     2.0, \
     3.0, \
     4.0, \
     2.0, \
     3.0, \
     4.0, \
     2.0, \
     3.0, \
     4.0 ))

  x_vec = np.array ( ( \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
      3.00, \
     15.00, \
     15.00, \
     15.00, \
      0.05, \
      0.05, \
      0.05, \
      4.00, \
      4.00, \
      4.00, \
      5.00, \
      5.00, \
      5.00, \
      6.00, \
      6.00, \
      6.00 ))

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

def tfn ( x, fx ):

#*****************************************************************************80
#
## tfn() calculates the T-function of Owen.
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
#    Original FORTRAN77 version by JC Young, Christoph Minder.
#    This version by John Burkardt.
#
#  Reference:
#
#    MA Porter, DJ Winstanley,
#    Remark AS R30:
#    A Remark on Algorithm AS76:
#    An Integral Useful in Calculating Noncentral T and Bivariate
#    Normal Probabilities,
#    Applied Statistics,
#    Volume 28, Number 1, 1979, page 113.
#
#    JC Young, Christoph Minder,
#    Algorithm AS 76:
#    An Algorithm Useful in Calculating Non-Central T and
#    Bivariate Normal Distributions,
#    Applied Statistics,
#    Volume 23, Number 3, 1974, pages 455-457.
#
#  Input:
#
#    real X, FX, the parameters of the function.
#
#  Output:
#
#    real VALUE, the value of the T-function.
#
  import numpy as np

  ng = 5

  r = np.array ( [ \
    0.1477621, \
    0.1346334, \
    0.1095432, \
    0.0747257, \
    0.0333357 ] )

  tp = 0.159155
  tv1 = 1.0E-35
  tv2 = 15.0
  tv3 = 15.0
  tv4 = 1.0E-05

  u = np.array ( [ \
    0.0744372, \
    0.2166977, \
    0.3397048, \
    0.4325317, \
    0.4869533 ] )
#
#  Test for X near zero.
#
  if ( np.abs ( x ) < tv1 ):
    value = tp * np.arctan ( fx )
    return value
#
#  Test for large values of abs(X).
#
  if ( tv2 < np.abs ( x ) ):
    value = 0.0
    return value
#
#  Test for FX near zero.
#
  if ( np.abs ( fx ) < tv1 ):
    value = 0.0
    return value
#
#  Test whether abs ( FX ) is so large that it must be truncated.
#
  xs = - 0.5 * x * x
  x2 = fx
  fxs = fx * fx
#
#  Computation of truncation point by Newton iteration.
#
  if ( tv3 <= np.log ( 1.0 + fxs ) - xs * fxs ):

    x1 = 0.5 * fx
    fxs = 0.25 * fxs

    while ( True ):

      rt = fxs + 1.0

      x2 = x1 + ( xs * fxs + tv3 - np.log ( rt ) ) \
        / ( 2.0 * x1 * ( 1.0 / rt - xs ) )

      fxs = x2 * x2

      if ( np.abs ( x2 - x1 ) < tv4 ):
        break

      x1 = x2
#
#  Gaussian quadrature.
#
  rt = 0.0

  for i in range ( 0, ng ):

    r1 = 1.0 + fxs * ( 0.5 + u[i] )**2
    r2 = 1.0 + fxs * ( 0.5 - u[i] )**2

    rt = rt + r[i] * ( np.exp ( xs * r1 ) / r1 + np.exp ( xs * r2 ) / r2 )

  value = rt * x2 * tp

  return value

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
  asa005_test ( )
  timestamp ( )
 
