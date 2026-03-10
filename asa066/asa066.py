#! /usr/bin/env python3
#
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

def alnorm_test ( ):

#*****************************************************************************80
#
## alnorm_test() tests alnorm().
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
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'alnorm_test():' )
  print ( '  Compare tabulated values of the normal' )
  print ( '  Cumulative Density Function against values' )
  print ( '  computed by alnorm()' )
  print ( '' )
  print ( '         X        CDF                       CDF' )
  print ( '                    DIFF' )
  print ( '               (tabulated)                 (ALNORM)' )
  print ( '' )

  upper = 0
  n_data = 0

  while ( True ):

    n_data, x, fx = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = alnorm ( x, upper )
    
    print ( '  %10.4e  %24.16e  %24.16e  %10.4e' % \
      ( x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

def asa066_test ( ):

#*****************************************************************************80
#
## asa066_test() tests asa066().
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
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa066_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa066().' )

  alnorm_test ( )
  normp_test ( )
  nprob_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa066_test():' )
  print ( '  Normal end of execution.' )

  return

def normal_01_cdf_values ( n_data ):

#*****************************************************************************80
#
## normal_01_cdf_values() returns some values of the Normal 01 CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NormalDistribution [ 0, 1 ]
#      CDF [ dist, x ]
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
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( (\
     0.5000000000000000E+00, \
     0.5398278372770290E+00, \
     0.5792597094391030E+00, \
     0.6179114221889526E+00, \
     0.6554217416103242E+00, \
     0.6914624612740131E+00, \
     0.7257468822499270E+00, \
     0.7580363477769270E+00, \
     0.7881446014166033E+00, \
     0.8159398746532405E+00, \
     0.8413447460685429E+00, \
     0.9331927987311419E+00, \
     0.9772498680518208E+00, \
     0.9937903346742239E+00, \
     0.9986501019683699E+00, \
     0.9997673709209645E+00, \
     0.9999683287581669E+00 ))

  x_vec = np.array ((\
     0.0000000000000000E+00, \
     0.1000000000000000E+00, \
     0.2000000000000000E+00, \
     0.3000000000000000E+00, \
     0.4000000000000000E+00, \
     0.5000000000000000E+00, \
     0.6000000000000000E+00, \
     0.7000000000000000E+00, \
     0.8000000000000000E+00, \
     0.9000000000000000E+00, \
     0.1000000000000000E+01, \
     0.1500000000000000E+01, \
     0.2000000000000000E+01, \
     0.2500000000000000E+01, \
     0.3000000000000000E+01, \
     0.3500000000000000E+01, \
     0.4000000000000000E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def normp ( z ):

#*****************************************************************************80
#
## normp() computes the cumulative density of the standard normal distribution.
#
#  Discussion:
#
#    This is algorithm 5666 from Hart, et al.
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
#    Original FORTRAN77 version by Alan Miller.
#    This version by John Burkardt.
#
#  Reference:
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly,
#    Charles Mesztenyi, John Rice, Henry Thacher,
#    Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968,
#    LC: QA297.C64.
#
#  Input:
#
#    real Z, divides the real ( kind = 8 ) line into two
#    semi-infinite intervals, over each of which the standard normal
#    distribution is to be integrated.
#
#  Output:
#
#    real P, Q, the integrals of the standard normal
#    distribution over the intervals ( - Infinity, Z] and
#    [Z, + Infinity ), respectively.
#
#    real PDF, the value of the standard normal distribution at Z.
#
  import numpy as np

  cutoff = 7.071
  p0 = 220.2068679123761
  p1 = 221.2135961699311
  p2 = 112.0792914978709
  p3 = 33.91286607838300
  p4 = 6.373962203531650
  p5 = 0.7003830644436881
  p6 = 0.03526249659989109 
  q0 = 440.4137358247522
  q1 = 793.8265125199484
  q2 = 637.3336333788311
  q3 = 296.5642487796737
  q4 = 86.78073220294608
  q5 = 16.06417757920695
  q6 = 1.755667163182642
  q7 = 0.08838834764831844
  root2pi = 2.506628274631001

  zabs = np.abs ( z )
#
#  37 < |Z|.
#
  if ( 37.0  < zabs ):

    pdf = 0.0
    p = 0.0
#
#  |Z| <= 37.
#
  else:

    expntl = np.exp ( - 0.5  * zabs * zabs )
    pdf = expntl / root2pi
#
#  |Z| < CUTOFF = 10 / sqrt(2).
#
    if ( zabs < cutoff ):

      p = expntl * (((((( \
          p6   * zabs \
        + p5 ) * zabs \
        + p4 ) * zabs \
        + p3 ) * zabs \
        + p2 ) * zabs \
        + p1 ) * zabs \
        + p0 ) / ((((((( \
          q7   * zabs \
        + q6 ) * zabs \
        + q5 ) * zabs \
        + q4 ) * zabs \
        + q3 ) * zabs \
        + q2 ) * zabs \
        + q1 ) * zabs \
        + q0 )
#
#  CUTOFF <= |Z|.
#
    else:

      p = pdf / ( \
        zabs + 1.0  / ( \
        zabs + 2.0  / ( \
        zabs + 3.0  / ( \
        zabs + 4.0  / ( \
        zabs + 0.65  )))))

  if ( z < 0.0  ):
    q = 1.0  - p
  else:
    q = p
    p = 1.0  - q

  return p, q, pdf

def normp_test ( ):

#*****************************************************************************80
#
## normp_test() tests normp().
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
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'normp_test():' )
  print ( '  Compare tabulated values of the normal' )
  print ( '  Cumulative Density Function against values' )
  print ( '  computed by normp().' )
  print ( '' )
  print ( '         X        CDF                       CDF' )
  print ( '                    DIFF' )
  print ( '               (tabulated)                 (NORMP)' )
  print ( '' )

  upper = 0
  n_data = 0

  while ( True ):

    n_data, x, fx = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    p, q, pdf = normp ( x )
    fx2 = p

    print ( '  %10.4e  %24.16e  %24.16e  %10.4e' % \
      ( x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

def nprob ( z ):

#*****************************************************************************80
#
## nprob() computes the cumulative density of the standard normal distribution.
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
#    Original FORTRAN77 version by AG Adams.
#    This version by John Burkardt.
#
#  Reference:
#
#    AG Adams,
#    Algorithm 39:
#    Areas Under the Normal Curve,
#    Computer Journal,
#    Volume 12, Number 2, May 1969, pages 197-198.
#
#  Input:
#
#    real Z, divides the real line into
#    two semi-infinite intervals, over each of which the standard normal
#    distribution is to be integrated.
#
#  Output:
#
#    real P, Q, the integrals of the standard normal
#    distribution over the intervals ( - Infinity, Z] and
#    [Z, + Infinity ), respectively.
#
#    real PDF, the value of the standard normal distribution at Z.
#
  import numpy as np

  a0 = 0.5
  a1 = 0.398942280444
  a2 = 0.399903438504
  a3 = 5.75885480458
  a4 = 29.8213557808
  a5 = 2.62433121679
  a6 = 48.6959930692
  a7 = 5.92885724438
  b0 = 0.398942280385
  b1 = 0.000000038052
  b2 = 1.00000615302
  b3 = 0.000398064794
  b4 = 1.98615381364
  b5 = 0.151679116635
  b6 = 5.29330324926
  b7 = 4.8385912808
  b8 = 15.1508972451
  b9 = 0.742380924027
  b10 = 30.789933034
  b11 = 3.99019417011

  zabs = np.abs ( z )
#
#  |Z| between 0 and 1.28
#
  if ( np.abs ( z ) <= 1.28 ):

    y = a0 * z * z
    pdf = np.exp ( - y ) * b0

    q = a0 - zabs * ( a1 - a2 * y \
      / ( y + a3 - a4 \
      / ( y + a5 + a6 \
      / ( y + a7 ))))
#
#  |Z| between 1.28 and 12.7
#
  elif ( abs ( z ) <= 12.7 ):

    y = a0 * z * z
    pdf = np.exp ( - y ) * b0

    q = pdf \
      / ( zabs - b1 + b2 \
      / ( zabs + b3 + b4 \
      / ( zabs - b5 + b6 \
      / ( zabs + b7 - b8 \
      / ( zabs + b9 + b10 \
      / ( zabs + b11 ))))))
#
#  Z far out in tail.
#
  else:

    q = 0.0
    pdf = 0.0

  if ( z < 0.0 ):
    p = q
    q = 1.0 - p
  else:
    p = 1.0 - q

  return p, q, pdf

def nprob_test ( ):

#*****************************************************************************80
#
## nprob_test() tests nprob().
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
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'nprob_test():' )
  print ( '  Compare tabulated values of the normal' )
  print ( '  Cumulative Density Function against values' )
  print ( '  computed by nprob().' )
  print ( '' )
  print ( '         X        CDF                       CDF' )
  print ( '                    DIFF' )
  print ( '               (tabulated)                 (NPROB)' )
  print ( '' )

  upper = 0
  n_data = 0

  while ( True ):

    n_data, x, fx = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    p, q, pdf = nprob ( x )
    fx2 = p

    print ( '  %10.4e  %24.16e  %24.16e  %10.4e' % \
      ( x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

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

if ( __name__ == "__main__" ):
  timestamp ( )
  asa066_test ( )
  timestamp ( )

