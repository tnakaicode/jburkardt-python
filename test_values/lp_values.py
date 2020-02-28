#! /usr/bin/env python
#
def lp_values ( n_data ):

#*****************************************************************************80
#
## LP_VALUES returns values of the Legendre polynomials P(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Parameters:
#
#    Input, int N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, int N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, int N, the order of the function.
#
#    Output, double X, the point where the function is evaluated.
#
#    Output, double FX, the value of the function.
#
  import numpy as np

  n_max = 22

  fx_vec = np.array ( [
      0.1000000000000000E+01,
      0.2500000000000000E+00,
     -0.4062500000000000E+00,
     -0.3359375000000000E+00,
      0.1577148437500000E+00,
      0.3397216796875000E+00,
      0.2427673339843750E-01,
     -0.2799186706542969E+00,
     -0.1524540185928345E+00,
      0.1768244206905365E+00,
      0.2212002165615559E+00,
      0.0000000000000000E+00,
     -0.1475000000000000E+00,
     -0.2800000000000000E+00,
     -0.3825000000000000E+00,
     -0.4400000000000000E+00,
     -0.4375000000000000E+00,
     -0.3600000000000000E+00,
     -0.1925000000000000E+00,
      0.8000000000000000E-01,
      0.4725000000000000E+00,
      0.1000000000000000E+01 ], dtype = np.float64 )

  n_vec = np.array ( [
     0,  1,  2,
     3,  4,  5,
     6,  7,  8,
     9, 10,  3,
     3,  3,  3,
     3,  3,  3,
     3,  3,  3,
     3 ], dtype = np.int32 )

  x_vec = np.array ( [
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.25E+00,
     0.00E+00,
     0.10E+00,
     0.20E+00,
     0.30E+00,
     0.40E+00,
     0.50E+00,
     0.60E+00,
     0.70E+00,
     0.80E+00,
     0.90E+00,
     1.00E+00 ], dtype = np.float64 )

  if ( n_data < 0 ):
    n_data = 0

  n_data = n_data + 1

  if ( n_max < n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data-1]
    x = x_vec[n_data-1]
    fx = fx_vec[n_data-1]

  return n_data, n, x, fx

def lp_values_test ( ):

#*****************************************************************************80
#
## LP_VALUES_TEST tests LP_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LP_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LP_VALUES stores values of' )
  print ( '  the Legendre polynomial P(o,x).' )
  print ( '' )
  print ( '                        Tabulated' )
  print ( '     O        X           L(O,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, o, x, fx = lp_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %12.8f  %24.16g' % ( o, x, fx ) )
#
#  Terminate.
#-
  print ( '' )
  print ( 'LP_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lp_values_test ( )
  timestamp ( )
