#! /usr/bin/env python3
#
def asa091_test ( ):

#*****************************************************************************80
#
## asa091_test() tests asa091().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa091_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa091().' )

  asa091_test01 ( )
  asa091_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa091_test():' )
  print ( '  Normal end of execution.' )

  return

def asa091_test01 ( ):

#*****************************************************************************80
#
## asa091_test01() tests ppchi2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import gammaln

  value_correct = 0.4
  p = 0.017523
  v = 4.0

  print ( '' )
  print ( 'asa091_test01():' )
  print ( '  Perform a simple sample calculation using' )
  print ( '  ppchi2() to invert the Chi-Squared CDF.' )

  g = gammaln ( v / 2.0 )

  print ( '' )
  print ( '  P =                  ', p )
  print ( '  V =                  ', v )
  print ( '  G Log(Gamma(V/2)) =  ', g )

  value, ifault = ppchi2 ( p, v, g )

  print ( '  VALUE =              ', value )
  print ( '  VALUE (correct) =    ', value_correct )

  print ( '' )
  print ( '  Error flag IFAULT = ', ifault )

  return

def asa091_test02 ( ):

#*****************************************************************************80
#
## asa091_test02() tests ppchi2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import gammaln
  import numpy as np

  print ( '' )
  print ( 'asa091_test02():' )
  print ( '  Compare tabulated values of the Chi-Squared ' )
  print ( '  Cumulative Density Function against values' )
  print ( '  computed by ppchi2().' )
  print ( '' )
  print ( '         N        CDF           X                        ', end = '' )
  print ( ' X2                  DIFF' )
  print ( '                               (tabulated)               ', end = '' )
  print ( '(PPCHI2)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, fx = chi_square_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    v = a

    g = gammaln ( v / 2.0 )

    x2, ifault = ppchi2 ( fx, v, g )

    print ( '  %8d  %10.4f  %24.16f  %24.16f  %10.4e' \
      % ( a, fx, x, x2, np.abs ( x - x2 ) ) )

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

def chi_square_cdf_values ( n_data ):

#*****************************************************************************80
#
## chi_square_cdf_values() returns some values of the Chi-Square CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = ChiSquareDistribution [ df ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2015
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
#    integer A, the parameter of the function.
#
#    real X, the argument of the function.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  a_vec = np.array ( ( \
     1,  2,  1,  2, \
     1,  2,  3,  4, \
     1,  2,  3,  4, \
     5,  3,  3,  3, \
     3,  3, 10, 10, \
    10  ) )

  f_vec = np.array ( ( \
     0.7965567455405796E-01, \
     0.4987520807317687E-02, \
     0.1124629160182849E+00, \
     0.9950166250831946E-02, \
     0.4729107431344619E+00, \
     0.1812692469220181E+00, \
     0.5975750516063926E-01, \
     0.1752309630642177E-01, \
     0.6826894921370859E+00, \
     0.3934693402873666E+00, \
     0.1987480430987992E+00, \
     0.9020401043104986E-01, \
     0.3743422675270363E-01, \
     0.4275932955291202E+00, \
     0.6083748237289110E+00, \
     0.7385358700508894E+00, \
     0.8282028557032669E+00, \
     0.8883897749052874E+00, \
     0.1721156299558408E-03, \
     0.3659846827343712E-02, \
     0.1857593622214067E-01 ) )

  x_vec = np.array ( ( \
     0.01E+00, \
     0.01E+00, \
     0.02E+00, \
     0.02E+00, \
     0.40E+00, \
     0.40E+00, \
     0.40E+00, \
     0.40E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     2.00E+00, \
     3.00E+00, \
     4.00E+00, \
     5.00E+00, \
     6.00E+00, \
     1.00E+00, \
     2.00E+00, \
     3.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, x, f

def gammad ( x, p ):

#*****************************************************************************80
#
## gammad() computes the incomplete Gamma integral.
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
#    Original FORTRAN77 version by B Shea.
#    This version by John Burkardt.
#
#  Reference:
#
#    B Shea,
#    Algorithm AS 239:
#    Chi-squared and Incomplete Gamma Integral,
#    Applied Statistics,
#    Volume 37, Number 3, 1988, pages 466-473.
#
#  Input:
#
#    real X, P, the parameters of the incomplete
#    gamma ratio.  0 <= X, and 0 < P.
#
#  Output:
#
#    real GAMMAD, the value of the incomplete Gamma integral.
#
#    integer IFAULT, error flag.
#    0, no error.
#    1, X < 0 or P <= 0.
#
  from scipy.special import gammaln
  import numpy as np

  elimit = - 88.0
  oflo = 1.0E+37
  plimit = 1000.0
  tol = 1.0E-14
  xbig = 1.0E+08

  value = 0.0
#
#  Check the input.
#
  if ( x < 0.0 ):
    ifault = 1
    return value, ifault

  if ( p <= 0.0 ):
    ifault = 1
    return value, ifault

  ifault = 0

  if ( x == 0.0 ):
    value = 0.0
    return value, ifault
#
#  If P is large, use a normal approximation.
#
  if ( plimit < p ):

    pn1 = 3.0 * np.sqrt ( p ) * ( ( x / p )**( 1.0 / 3.0 ) \
      + 1.0 / ( 9.0 * p ) - 1.0 )

    upper = 0
    value = alnorm ( pn1, upper )
    return value, ifault
#
#  If X is large set GAMMAD = 1.
#
  if ( xbig < x ):
    value = 1.0
    return value, ifault
#
#  Use Pearson's series expansion.
#  (Note that P is not large enough to force overflow in ALOGAM).
#  No need to test IFAULT on exit since P > 0.
#
  if ( x <= 1.0 or x < p ):

    arg = p * np.log ( x ) - x - gammaln ( p + 1.0 )
    c = 1.0
    value = 1.0
    a = p

    while ( True ):

      a = a + 1.0
      c = c * x / a
      value = value + c

      if ( c <= tol ):
        break

    arg = arg + np.log ( value )

    if ( elimit <= arg ):
      value = np.exp ( arg )
    else:
      value = 0.0
#
#  Use a continued fraction expansion.
#
  else:

    arg = p * np.log ( x ) - x - gammaln ( p )
    a = 1.0 - p
    b = a + x + 1.0
    c = 0.0
    pn1 = 1.0
    pn2 = x
    pn3 = x + 1.0
    pn4 = x * b
    value = pn3 / pn4

    while ( True ):

      a = a + 1.0
      b = b + 2.0
      c = c + 1.0
      an = a * c
      pn5 = b * pn3 - an * pn1
      pn6 = b * pn4 - an * pn2

      if ( pn6 != 0.0 ):

        rn = pn5 / pn6

        if ( np.abs ( value - rn ) <= min ( tol, tol * rn ) ):
          break

        value = rn

      pn1 = pn3
      pn2 = pn4
      pn3 = pn5
      pn4 = pn6
#
#  Re-scale terms in continued fraction if terms are large.
#
      if ( oflo <= np.abs ( pn5 ) ):
        pn1 = pn1 / oflo
        pn2 = pn2 / oflo
        pn3 = pn3 / oflo
        pn4 = pn4 / oflo

    arg = arg + np.log ( value )

    if ( elimit <= arg ):
      value = 1.0 - np.exp ( arg )
    else:
      value = 1.0

  return value, ifault

def ppchi2 ( p, v, g ):

#*****************************************************************************80
#
## ppchi2() evaluates the percentage points of the Chi-squared PDF.
#
#  Discussion
#
#    Incorporates the suggested changes in AS R85 (vol.40(1),
#    pages 233-5, 1991) which should eliminate the need for the limited
#    range for P, though these limits have not been removed
#    from the routine.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2008
#
#  Author:
#
#    Original FORTRAN77 version by Donald Best, DE Roberts.
#    This version by John Burkardt.
#
#  Reference:
#
#    Donald Best, DE Roberts,
#    Algorithm AS 91:
#    The Percentage Points of the Chi-Squared Distribution,
#    Applied Statistics,
#    Volume 24, Number 3, 1975, pages 385-390.
#
#  Input:
#
#    real P,  value of the chi-squared cumulative
#    probability density function.
#    0.000002 <= P <= 0.999998.
#
#    real V, the parameter of the chi-squared probability
#    density function.
#    0 < V.
#
#    real G, the value of log ( Gamma ( V / 2 ) ).
#
#  Output:
#
#    real VALUE, the value of the chi-squared random
#    deviate with the property that the probability that a chi-squared random
#    deviate with parameter V is less than or equal to PPCHI2 is P.
#
#    integer IFAULT, is nonzero if an error occurred.
#    0, no error.
#    1, P is outside the legal range.
#    2, V is not positive.
#    3, an error occurred in GAMMAD.
#    4, the result is probably as accurate as the machine will allow.
#
  import numpy as np

  aa = 0.6931471806
  c1 = 0.01
  c2 = 0.222222
  c3 = 0.32
  c4 = 0.4
  c5 = 1.24
  c6 = 2.2
  c7 = 4.67
  c8 = 6.66
  c9 = 6.73
  c10 = 13.32
  c11 = 60.0
  c12 = 70.0
  c13 = 84.0
  c14 = 105.0
  c15 = 120.0
  c16 = 127.0
  c17 = 140.0
  c18 = 175.0
  c19 = 210.0
  c20 = 252.0
  c21 = 264.0
  c22 = 294.0
  c23 = 346.0
  c24 = 420.0
  c25 = 462.0
  c26 = 606.0
  c27 = 672.0
  c28 = 707.0
  c29 = 735.0
  c30 = 889.0
  c31 = 932.0
  c32 = 966.0
  c33 = 1141.0
  c34 = 1182.0
  c35 = 1278.0
  c36 = 1740.0
  c37 = 2520.0
  c38 = 5040.0
  e = 0.5E-06
  maxit = 20
  pmax = 0.999998
  pmin = 0.000002
#
#  Test arguments and initialize.
#
  value = - 1.0

  if ( p < pmin or pmax < p ):
    ifault = 1
    return value, ifault

  if ( v <= 0.0 ):
    ifault = 2
    return value, ifault

  ifault = 0
  xx = 0.5 * v
  c = xx - 1.0
#
#  Starting approximation for small chi-squared
#
  if ( v < - c5 * np.log ( p ) ):

    ch = ( p * xx * np.exp ( g + xx * aa ) )**( 1.0 / xx )

    if ( ch < e ):
      value = ch
      return value, ifault
#
#  Starting approximation for V less than or equal to 0.32
#
  elif ( v <= c3 ):

    ch = c4
    a = np.log ( 1.0 - p )

    while ( True ):

      q = ch
      p1 = 1.0 + ch * ( c7 + ch )
      p2 = ch * ( c9 + ch * ( c8 + ch ) )

      t = - 0.5 + (c7 + 2.0 * ch ) / p1 \
        - ( c9 + ch * ( c10 + 3.0 * ch ) ) / p2

      ch = ch - ( 1.0 - np.exp ( a + g + 0.5 * ch + c * aa ) * p2 / p1) / t

      if ( np.abs ( q / ch - 1.0 ) <= c1 ):
        break

  else:
#
#  Call to algorithm AS 111 - note that P has been tested above.
#  AS 241 could be used as an alternative.
#
    x, ifault = ppnd ( p )
#
#  Starting approximation using Wilson and Hilferty estimate
#
    p1 = c2 / v
    ch = v * ( x * np.sqrt ( p1 ) + 1.0 - p1)**3
#
#  Starting approximation for P tending to 1.
#
    if ( c6 * v + 6.0 < ch ):
       ch = - 2.0 * ( np.log ( 1.0 - p ) - c * np.log ( 0.5 * ch ) + g )
#
#  Call to algorithm AS 239 and calculation of seven term Taylor series
#
  for i in range ( 0, maxit ):

    q = ch
    p1 = 0.5 * ch
    temp, if1 = gammad ( p1, xx )
    p2 = p - temp

    if ( if1 != 0 ):
      ifault = 3
      return value, ifault

    t = p2 * np.exp ( xx * aa + g + p1 - c * np.log ( ch ) )
    b = t / ch
    a = 0.5 * t - b * c
    s1 = ( c19 + a * ( c17 + a * ( c14 + a * ( c13 + a * ( c12 + \
      c11 * a ))))) / c24
    s2 = ( c24 + a * ( c29 + a * ( c32 + a * ( c33 + c35 * a )))) / c37
    s3 = ( c19 + a * ( c25 + a * ( c28 + c31 * a ))) / c37
    s4 = ( c20 + a * ( c27 + c34 * a) + c * ( c22 + a * ( c30 + c36 * a ))) \
      / c38
    s5 = ( c13 + c21 * a + c * ( c18 + c26 * a )) / c37
    s6 = ( c15 + c * ( c23 + c16 * c )) / c38
    ch = ch + t * ( 1.0 + 0.5 * t * s1 - b * c * ( s1 - b * \
      ( s2 - b * ( s3 - b * ( s4 - b * ( s5 - b * s6 ))))))

    if ( e < np.abs ( q / ch - 1.0 ) ):
       value = ch
       return value, ifault

  ifault = 4
  value = ch

  return value, ifault

def ppnd ( p ):

#*****************************************************************************80
#
## ppnd() produces the normal deviate value corresponding to lower tail area = P.
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
#    Original FORTRAN77 version by J Beasley, S Springer.
#    This version by John Burkardt.
#
#  Reference:
#
#    J Beasley, S Springer,
#    Algorithm AS 111:
#    The Percentage Points of the Normal Distribution,
#    Applied Statistics,
#    Volume 26, Number 1, 1977, pages 118-121.
#
#  Input:
#
#    real P, the value of the cumulative probability
#    densitity function.  0 < P < 1.
#
#  Output:
#
#    real VALUE, the normal deviate value with the property that
#    the probability of a standard normal deviate being less than or
#    equal to PPND is P.
#
#    integer IFAULT, error flag.
#    0, no error.
#    1, P <= 0 or P >= 1.  PPND is returned as 0.
#
  import numpy as np

  a0 = 2.50662823884
  a1 = -18.61500062529
  a2 = 41.39119773534
  a3 = -25.44106049637
  b1 = -8.47351093090
  b2 = 23.08336743743
  b3 = -21.06224101826
  b4 = 3.13082909833
  c0 = -2.78718931138
  c1 = -2.29796479134
  c2 = 4.85014127135
  c3 = 2.32121276858
  d1 = 3.54388924762
  d2 = 1.63706781897
  split = 0.42

  ifault = 0
#
#  0.08 < P < 0.92
#
  if ( abs ( p - 0.5 ) <= split ):

    r = ( p - 0.5 ) * ( p - 0.5 )

    value = ( p - 0.5 ) * ( ( ( \
        a3   * r \
      + a2 ) * r \
      + a1 ) * r \
      + a0 ) / ( ( ( ( \
        b4   * r \
      + b3 ) * r \
      + b2 ) * r \
      + b1 ) * r \
      + 1.0 )
#
#  P < 0.08 or P > 0.92,
#  R = min ( P, 1-P )
#
  elif ( 0.0 < p and p < 1.0 ):

    if ( 0.5 < p ):
      r = np.sqrt ( - np.log ( 1.0 - p ) )
    else:
      r = np.sqrt ( - np.log ( p ) )

    value = ( ( ( \
        c3   * r \
      + c2 ) * r \
      + c1 ) * r \
      + c0 ) / ( ( \
        d2   * r \
      + d1 ) * r \
      + 1.0 )

    if ( p < 0.5 ):
      value = - value
#
#  P <= 0.0 or 1.0 <= P
#
  else:

    ifault = 1
    value = 0.0


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
  asa091_test ( )
  timestamp ( )


