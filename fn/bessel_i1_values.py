#! /usr/bin/env python
#
def bessel_i1_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_I1_VALUES returns some values of the I1 Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselI[1,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
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

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.1005008340281251E+00, \
     0.2040267557335706E+00, \
     0.3137040256049221E+00, \
     0.4328648026206398E+00, \
     0.5651591039924850E+00, \
     0.7146779415526431E+00, \
     0.8860919814143274E+00, \
     0.1084810635129880E+01, \
     0.1317167230391899E+01, \
     0.1590636854637329E+01, \
     0.2516716245288698E+01, \
     0.3953370217402609E+01, \
     0.6205834922258365E+01, \
     0.9759465153704450E+01, \
     0.1538922275373592E+02, \
     0.2433564214245053E+02, \
     0.6134193677764024E+02, \
     0.3998731367825601E+03, \
     0.2670988303701255E+04 ) )

  x_vec = np.array ( ( \
     0.00E+00, \
     0.20E+00, \
     0.40E+00, \
     0.60E+00, \
     0.80E+00, \
     0.10E+01, \
     0.12E+01, \
     0.14E+01, \
     0.16E+01, \
     0.18E+01, \
     0.20E+01, \
     0.25E+01, \
     0.30E+01, \
     0.35E+01, \
     0.40E+01, \
     0.45E+01, \
     0.50E+01, \
     0.60E+01, \
     0.80E+01, \
     0.10E+02  ) )

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

def bessel_i1_values_test ( ):

#*****************************************************************************80
#
## BESSEL_I1_VALUES_TEST demonstrates the use of BESSEL_I1_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BESSEL_I1_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BESSEL_I1_VALUES stores values of the Bessel I function. of order 1.' )
  print ( '' )
  print ( '      X           I(1,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_i1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_I1_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_i1_values_test ( )
  timestamp ( )
