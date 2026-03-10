#! /usr/bin/env python3
#
def asa111_test ( ):

#*****************************************************************************80
#
## asa111_test() tests asa111().
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
  print ( 'asa111_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa111().' )

  asa111_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa111_test():' )
  print ( '  Normal end of execution.' )

  return

def asa111_test01 ( ):

#*****************************************************************************80
#
## asa111_test01() tests ppnd().
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
  print ( 'asa111_test01():' )
  print ( '  ppnd() computes percentage points of the normal distribution.' )
  print ( '  Compare to tabulated values.' )
  print ( '' )
  print ( '         CDF      X                         X  ', end = '' )
  print ( '                    DIFF' )
  print ( '               (tabulated)                 (PPND)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    x2, ifault = ppnd ( fx )
    
    print ( '  %10.4e  %24.16e  %24.16e  %10.4e' \
      % ( fx, x, x2, np.abs ( x - x2 ) ) )

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
  asa111_test ( )
  timestamp ( )


