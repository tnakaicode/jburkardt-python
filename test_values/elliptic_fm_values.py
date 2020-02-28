#! /usr/bin/env python
#
def elliptic_fm_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_FM_VALUES returns values of the complete elliptic integral F(M).
#
#  Discussion:
#
#    This is one form of what is sometimes called the complete elliptic 
#    integral of the first kind.
#
#    The function is defined by the formula:
#
#      F(M) = integral ( 0 <= T <= PI/2 ) 
#        dT / sqrt ( 1 - M * sin ( T )^2 )
#
#    In Mathematica, the function can be evaluated by:
#
#      EllipticK[m]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
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

  fx_vec = np.array ( (
     1.570796326794897E+00, \
     1.591003453790792E+00, \
     1.612441348720219E+00, \
     1.635256732264580E+00, \
     1.659623598610528E+00, \
     1.685750354812596E+00, \
     1.713889448178791E+00, \
     1.744350597225613E+00, \
     1.777519371491253E+00, \
     1.813883936816983E+00, \
     1.854074677301372E+00, \
     1.898924910271554E+00, \
     1.949567749806026E+00, \
     2.007598398424376E+00, \
     2.075363135292469E+00, \
     2.156515647499643E+00, \
     2.257205326820854E+00, \
     2.389016486325580E+00, \
     2.578092113348173E+00, \
     2.908337248444552E+00 ))

  x_vec = np.array ( (
      0.00E+00, \
      0.05E+00, \
      0.10E+00, \
      0.15E+00, \
      0.20E+00, \
      0.25E+00, \
      0.30E+00, \
      0.35E+00, \
      0.40E+00, \
      0.45E+00, \
      0.50E+00, \
      0.55E+00, \
      0.60E+00, \
      0.65E+00, \
      0.70E+00, \
      0.75E+00, \
      0.80E+00, \
      0.85E+00, \
      0.90E+00, \
      0.95E+00 ))

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

def elliptic_fm_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_FM_VALUES_TEST demonstrates the use of ELLIPTIC_FM_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ELLIPTIC_FM_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPTIC_FM_VALUES stores values of the complete elliptic' )
  print ( '  integral of the first kind, with parameter modulus M.' )
  print ( '' )
  print ( '      M         F(M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = elliptic_fm_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPTIC_FM_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_fm_values_test ( )
  timestamp ( )

