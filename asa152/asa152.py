#! /usr/bin/env python3
#
def asa152_test ( ):

#*****************************************************************************80
#
## asa152_test() tests asa152().
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
  print ( 'asa152_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa152().' )

  asa152_test01 ( )
  asa152_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa152_test():' )
  print ( '  Normal end of execution.' )

  return

def asa152_test01 ( ):

#*****************************************************************************80
#
## asa152_test01() tests chyper() for cumulative probabilities.
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
  print ( 'asa152_test01():' )
  print ( '  chyper() computes cumulative probabilities' )
  print ( '  of the hypergeometric PDF.' )
  print ( '  Compare to tabulated values.' )
  print ( '' )
  print ( '   SAM   SUC   POP     X    ', end = '' )
  print ( '  CDF                       CDF                     DIFF' )
  print ( '                            ', end = '' )
  print ( ' (tabulated)               (CHYPER)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, sam, suc, pop, x, fx = hypergeometric_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    point = False

    fx2, ifault = chyper ( point, sam, x, pop, suc )

    print ( '  %4d  %4d  %4d  %4d  %24.16e  %24.16e  %10.4e' \
      % ( sam, suc, pop, x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

def asa152_test02 ( ):

#*****************************************************************************80
#
## asa152_test02() tests chyper() for point probabilities.
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
  print ( 'asa152_test02():' )
  print ( '  chyper() computes point probabilities' )
  print ( '  of the hypergeometric PDF.' )
  print ( '  Compare to tabulated values.' )
  print ( '' )
  print ( '   SAM   SUC   POP     X    ', end = '' )
  print ( '  PDF                       PDF                     DIFF' )
  print ( '                            ', end = '' )
  print ( ' (tabulated)               (CHYPER)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, sam, suc, pop, x, fx = hypergeometric_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    point = True

    fx2, ifault = chyper ( point, sam, x, pop, suc )

    print ( '  %4d  %4d  %4d  %4d  %24.16e  %24.16e  %10.4e' \
      % ( sam, suc, pop, x, fx, fx2, np.abs ( fx - fx2 ) ) )

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

def chyper ( point, kk, ll, mm, nn ):

#*****************************************************************************80
#
## chyper() computes point or cumulative hypergeometric probabilities.
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
#    Original FORTRAN77 version by Richard Lund.
#    This version by John Burkardt.
#
#  Reference:
#
#    PR Freeman,
#    Algorithm AS 59:
#    Hypergeometric Probabilities,
#    Applied Statistics,
#    Volume 22, Number 1, 1973, pages 130-133.
#
#    Richard Lund,
#    Algorithm AS 152:
#    Cumulative hypergeometric probabilities,
#    Applied Statistics,
#    Volume 29, Number 2, 1980, pages 221-223.
#
#    BL Shea,
#    Remark AS R77:
#    A Remark on Algorithm AS 152: Cumulative hypergeometric probabilities,
#    Applied Statistics,
#    Volume 38, Number 1, 1989, pages 199-204.
#
#  Input:
#
#    logical POINT, is TRUE if the point probability is desired,
#    and FALSE if the cumulative probability is desired.
#
#    integer KK, the sample size.
#    0 <= KK <= MM.
#
#    integer LL, the number of successes in the sample.
#    0 <= LL <= KK.
#
#    integer MM, the population size that was sampled.
#    0 <= MM.
#
#    integer NN, the number of "successes" in the population.
#    0 <= NN <= MM.
#
#  Output:
#
#    real VALUE, the PDF (point probability) of
#    exactly LL successes out of KK samples, or the CDF (cumulative
#    probability) of up to LL successes out of KK samples.
#
#    integer IFAULT, error flag.
#    0, no error occurred.
#    nonzero, an error occurred.
#
  from scipy.special import gammaln
  import numpy as np

  elimit = - 88.0
  mbig = 600
  mvbig = 1000
  rootpi = 2.506628274631001
  scale = 1.0E+35

  ifault = 0

  k = kk + 1
  l = ll + 1
  m = mm + 1
  n = nn + 1

  direction = True
#
#  Check arguments are within permitted limits.
#
  value = 0.0

  if ( n < 1 or m < n or k < 1 or m < k ):
    ifault = 1
    return value, ifault

  if ( l < 1 or m - n < k - l ):
    ifault = 2
    return value, ifault

  if ( not point ):
    value = 1.0

  if ( n < l or k < l ):
    ifault = 2
    return value, ifault

  ifault = 0
  value = 1.0

  if ( k == 1 or k == m or n == 1 or n == m ):
    return value, ifault

  if ( not point and ll == min ( kk, nn ) ):
    return value, ifault

  p = nn / ( mm - nn )

  if ( 16.0 * max ( p, 1.0 / p ) < min ( kk, mm - kk ) and \
    mvbig < mm and - 100.0 < elimit ):
#
#  Use a normal approximation.
#
    mean = kk * nn / mm

    sig = np.sqrt ( mean * ( ( mm - nn ) / mm ) \
    * ( ( mm - kk ) / ( mm - 1 ) ) )

    if ( point ):

      arg = - 0.5 * ( ( ( ll - mean ) / sig )**2 )
      if ( elimit <= arg ):
        value = np.exp ( arg ) / ( sig * rootpi )
      else:
        value = 0.0
 
    else:

      value = alnorm ( ( ll + 0.5 - mean ) / sig, 0 )

  else:
#
#  Calculate exact hypergeometric probabilities.
#  Interchange K and N if this saves calculations.
#
    if ( min ( n - 1, m - n ) < min ( k - 1, m - k ) ):
      i = k
      k = n
      n = i
 
    if ( m - k < k - 1 ):
      direction = not direction
      l = n - l + 1
      k = m - k + 1

    if ( mbig < mm ):
#
#  Take logarithms of factorials.
#
      p = gammaln ( nn + 1 ) \
        - gammaln ( mm + 1 ) \
        + gammaln ( mm - kk + 1 ) \
        + gammaln ( kk + 1 ) \
        + gammaln ( mm - nn + 1 ) \
        - gammaln ( ll + 1 ) \
        - gammaln ( nn - ll + 1 ) \
        - gammaln ( kk - ll + 1 ) \
        - gammaln ( mm - nn - kk + ll + 1 )

      if ( elimit <= p ):
        value = np.exp ( p )
      else:
        value = 0.0

    else:
#
#  Use Freeman/Lund algorithm.
#
      for i in range ( 1, l ):
        value = value * ( k - i ) * ( n - i ) / ( l - i ) / ( m - i )

      if ( l != k ):
        j = m - n + l
        for i in range ( l, k ):
          value = value * ( j - i ) / ( m - i )

    if ( point ):
      return value, ifault

    if ( value == 0.0 ):
#
#  We must recompute the point probability since it has underflowed.
#
      if ( mm <= mbig ):
        p = gammaln ( nn + 1 ) \
          - gammaln ( mm + 1 ) \
          + gammaln ( kk + 1 ) \
          + gammaln ( mm - nn + 1 ) \
          - gammaln ( ll + 1 ) \
          - gammaln ( nn - ll + 1 ) \
          - gammaln ( kk - ll + 1 ) \
          - gammaln ( mm - nn - kk + ll + 1 ) \
          + gammaln ( mm - kk + 1 )

      p = p + np.log ( scale )

      if ( p < elimit ):
        ifault = 3
        if ( ( nn * kk + nn + kk + 1 ) / ( mm + 2 ) < ll ):
          value = 1.0
        return value, ifault
      else:
        p = np.exp ( p )

    else:
#
#  Scale up at this point.
#
      p = value * scale

    pt = 0.0
    nl = n - l
    kl = k - l
    mnkl = m - n - kl + 1

    if ( l <= kl ):

      for i in range ( 1, l ):
        p = p * ( l - i ) * ( mnkl - i ) / ( nl + i ) / ( kl + i )
        pt = pt + p

    else:

      direction = not direction

      for j in range ( 0, kl ):
        p = p * ( nl - j ) * ( kl - j ) / ( l + j ) / ( mnkl + j )
        pt = pt + p

    if ( p == 0.0 ):
      ifault = 3

    if ( direction ):
      value = value + ( pt / scale )
    else:
      value = 1.0 - ( pt / scale )

  return value, ifault

def hypergeometric_cdf_values ( n_data ):

#*****************************************************************************80
#
## hypergeometric_cdf_values() returns some values of the hypergeometric CDF.
#
#  Discussion:
#
#    CDF(X)(A,B) is the probability of at most X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`DiscreteDistributions`]
#      dist = HypergeometricDistribution [ sam, suc, pop ]
#      CDF [ dist, n ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
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
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition, CRC Press, 1996, pages 651-652.
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
#    integer SAM, integer SUC, integer POP, the sample size, 
#    success size, and population parameters of the function.
#
#    integer N, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 16

  f_vec = np.array ( (\
     0.6001858177500578E-01, \
     0.2615284665839845E+00, \
     0.6695237889132748E+00, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.5332595856827856E+00, \
     0.1819495964117640E+00, \
     0.4448047017527730E-01, \
     0.9999991751316731E+00, \
     0.9926860896560750E+00, \
     0.8410799901444538E+00, \
     0.3459800113391901E+00, \
     0.0000000000000000E+00, \
     0.2088888139634505E-02, \
     0.3876752992448843E+00, \
     0.9135215248834896E+00 ))

  n_vec = np.array ( (\
     7,  8,  9, 10, \
     6,  6,  6,  6, \
     6,  6,  6,  6, \
     0,  0,  0,  0 ))

  pop_vec = np.array ( (\
    100, 100, 100, 100, \
    100, 100, 100, 100, \
    100, 100, 100, 100, \
    90,  200, 1000, 10000 ))

  sam_vec = np.array ( (\
    10, 10, 10, 10, \
     6,  7,  8,  9, \
    10, 10, 10, 10, \
    10, 10, 10, 10 ))

  suc_vec = np.array ( (\
    90, 90, 90, 90, \
    90, 90, 90, 90, \
    10, 30, 50, 70, \
    90, 90, 90, 90 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    sam = 0
    suc = 0
    pop = 0
    n = 0
    f = 0.0
  else:
    sam = sam_vec[n_data]
    suc = suc_vec[n_data]
    pop = pop_vec[n_data]
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, sam, suc, pop, n, f

def hypergeometric_pdf_values ( n_data ):

#*****************************************************************************80
#
## hypergeometric_pdf_values() returns some values of the hypergeometric PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) is the probability of X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    In Mathematica, the function can be evaluated by:
#
#      dist = HypergeometricDistribution [ sam, suc, pop ]
#      PDF [ dist, n ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 February 2015
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
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition, CRC Press, 1996, pages 651-652.
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
#    integer SAM, integer SUC, integer POP, the sample size, 
#    success size, and population parameters of the function.
#
#    integer N, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 16

  f_vec = np.array ( (\
    0.05179370533242827E+00, \
    0.2015098848089788E+00, \
    0.4079953223292903E+00, \
    0.3304762110867252E+00, \
    0.5223047493549780E+00, \
    0.3889503452643453E+00, \
    0.1505614239732950E+00, \
    0.03927689321042477E+00, \
    0.00003099828465518108E+00, \
    0.03145116093938197E+00, \
    0.2114132170316862E+00, \
    0.2075776621999210E+00, \
    0.0000000000000000E+00, \
    0.002088888139634505E+00, \
    0.3876752992448843E+00, \
    0.9135215248834896E+00 ))

  n_vec = np.array ( (\
     7,  8,  9, 10, \
     6,  6,  6,  6, \
     6,  6,  6,  6, \
     0,  0,  0,  0 ))

  pop_vec = np.array ( (\
    100, 100, 100, 100, \
    100, 100, 100, 100, \
    100, 100, 100, 100, \
    90,  200, 1000, 10000 ))

  sam_vec = np.array ( (\
    10, 10, 10, 10, \
     6,  7,  8,  9, \
    10, 10, 10, 10, \
    10, 10, 10, 10 ))

  suc_vec = np.array ( (\
    90, 90, 90, 90, \
    90, 90, 90, 90, \
    10, 30, 50, 70, \
    90, 90, 90, 90 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    sam = 0
    suc = 0
    pop = 0
    n = 0
    f = 0.0
  else:
    sam = sam_vec[n_data]
    suc = suc_vec[n_data]
    pop = pop_vec[n_data]
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, sam, suc, pop, n, f

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
  asa152_test ( )
  timestamp ( )


