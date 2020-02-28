#! /usr/bin/env python
#
def bessel_y0_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_Y0_VALUES returns some values of the Y0 Bessel function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselY[0,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 December 2014
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

  n_max = 16

  fx_vec = np.array ( ( \
     -0.1534238651350367E+01, \
      0.8825696421567696E-01, \
      0.5103756726497451E+00, \
      0.3768500100127904E+00, \
     -0.1694073932506499E-01, \
     -0.3085176252490338E+00, \
     -0.2881946839815792E+00, \
     -0.2594974396720926E-01, \
      0.2235214893875662E+00, \
      0.2499366982850247E+00, \
      0.5567116728359939E-01, \
     -0.1688473238920795E+00, \
     -0.2252373126343614E+00, \
     -0.7820786452787591E-01, \
      0.1271925685821837E+00, \
      0.2054642960389183E+00 ) )

  x_vec = np.array ( ( \
      0.1E+00, \
      1.0E+00, \
      2.0E+00, \
      3.0E+00, \
      4.0E+00, \
      5.0E+00, \
      6.0E+00, \
      7.0E+00, \
      8.0E+00, \
      9.0E+00, \
     10.0E+00, \
     11.0E+00, \
     12.0E+00, \
     13.0E+00, \
     14.0E+00, \
     15.0E+00  ) )

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

def bessel_y0_values_test ( ):

#*****************************************************************************80
#
## BESSEL_Y0_VALUES_TEST demonstrates the use of BESSEL_Y0_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_Y0_VALUES_TEST:' )
  print ( '  BESSEL_Y0_VALUES stores values of the Bessel Y function. of order 0.' )
  print ( '' )
  print ( '      X           Y(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_y0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_Y0_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_y0_values_test ( )
  timestamp ( )
