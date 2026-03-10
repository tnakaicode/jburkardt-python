#! /usr/bin/env python3
#
def asa121_test ( ):

#*****************************************************************************80
#
## asa121_test() tests asa121().
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
  print ( 'asa121_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa121().' )

  asa121_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa121_test():' )
  print ( '  Normal end of execution.' )

  return

def asa121_test01 ( ):

#*****************************************************************************80
#
## asa121_test01() tests trigamma().
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

  print ( '' )
  print ( 'asa121_test01():' )
  print ( '  trigamma() computes the trigamma function.' )
  print ( '  Compare the result to tabulated values.' )
  print ( '' )
  print ( '          X         ' )
  print ( 'FX                        FX2' )
  print ( '                    ' )
  print ( '(Tabulated)               (TRIGAMMA)              DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = trigamma_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, ifault = trigamma ( x )

    print ( '  %12.4f  %24.16e  %24.16e  %10.4e' \
      % ( x, fx, fx2, np.abs ( fx - fx2 ) ) )

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

def trigamma ( x ):

#*****************************************************************************80
#
## trigamma() calculates trigamma(x) = d^2 log(gamma(x)) / dx^2
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
#    Original FORTRAN77 version by BE Schneider.
#    This version by John Burkardt.
#
#  Reference:
#
#    BE Schneider,
#    Algorithm AS 121:
#    Trigamma Function,
#    Applied Statistics,
#    Volume 27, Number 1, pages 97-99, 1978.
#
#  Input:
#
#    real X, the argument of the trigamma function.
#    0 < X.
#
#  Output:
#
#    real VALUE, the value of the trigamma function at X.
#
#    integer IFAULT, error flag.
#    0, no error.
#    1, X <= 0.
#
  a = 0.0001
  b = 5.0
  b2 =  0.1666666667
  b4 = -0.03333333333
  b6 =  0.02380952381
  b8 = -0.03333333333
#
#  Check the input.
#
  if ( x <= 0.0 ):
    ifault = 1
    value = 0.0
    return value, ifault

  ifault = 0
  z = x
#
#  Use small value approximation if X <= A.
#
  if ( x <= a ):
    value = 1.0 / x / x
    return value, ifault
#
#  Increase argument to ( X + I ) >= B.
#
  value = 0.0

  while ( z < b ):
    value = value + 1.0 / z / z
    z = z + 1.0
#
#  Apply asymptotic formula if argument is B or greater.
#
  y = 1.0 / z / z

  value = value + 0.5 * \
      y + ( 1.0 \
    + y * ( b2  \
    + y * ( b4  \
    + y * ( b6  \
    + y *   b8 )))) / z

  return value, ifault

def trigamma_values ( n_data ):

#*****************************************************************************80
#
## trigamma_values() returns some values of the trigamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyGamma[1,x]
#
#    trigamma(X) = d^2 ln ( Gamma ( X ) ) / d X^2
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
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 11

  f_vec = np.array ( ( \
     0.1644934066848226E+01, \
     0.1433299150792759E+01, \
     0.1267377205423779E+01, \
     0.1134253434996619E+01, \
     0.1025356590529597E+01, \
     0.9348022005446793E+00, \
     0.8584318931245799E+00, \
     0.7932328301639984E+00, \
     0.7369741375017002E+00, \
     0.6879720582426356E+00, \
     0.6449340668482264E+00 ))

  x_vec = np.array ( ( \
    1.0E+00, \
    1.1E+00, \
    1.2E+00, \
    1.3E+00, \
    1.4E+00, \
    1.5E+00, \
    1.6E+00, \
    1.7E+00, \
    1.8E+00, \
    1.9E+00, \
    2.0E+00 ))

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

if ( __name__ == '__main__' ):
  timestamp ( )
  asa121_test ( )
  timestamp ( )

