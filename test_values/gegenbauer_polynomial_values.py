#! /usr/bin/env python
#
def gegenbauer_polynomial_values ( n_data ):

#*****************************************************************************80
#
## GEGENBAUER_POLYNOMIAL_VALUES returns some values of the Gegenbauer polynomials.
#
#  Discussion:
#
#    The Gegenbauer polynomials are also known as the "spherical
#    polynomials" or "ultraspherical polynomials".
#
#    In Mathematica, the function can be evaluated by:
#
#      GegenbauerC[n,m,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
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
#    Output, integer N, the order parameter of the function.
#
#    Output, real A, the real parameter of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 38

  a_vec = np.array ( ( \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.5E+00, \
      0.0E+00, \
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
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00, \
      3.0E+00 ))

  f_vec = np.array ( ( \
       1.0000000000E+00, \
       0.2000000000E+00, \
      -0.4400000000E+00, \
      -0.2800000000E+00, \
       0.2320000000E+00, \
       0.3075200000E+00, \
      -0.0805760000E+00, \
      -0.2935168000E+00, \
      -0.0395648000E+00, \
       0.2459712000E+00, \
       0.1290720256E+00, \
       0.0000000000E+00, \
      -0.3600000000E+00, \
      -0.0800000000E+00, \
       0.8400000000E+00, \
       2.4000000000E+00, \
       4.6000000000E+00, \
       7.4400000000E+00, \
      10.9200000000E+00, \
      15.0400000000E+00, \
      19.8000000000E+00, \
      25.2000000000E+00, \
      -9.0000000000E+00, \
      -0.1612800000E+00, \
      -6.6729600000E+00, \
      -8.3750400000E+00, \
      -5.5267200000E+00, \
       0.0000000000E+00, \
       5.5267200000E+00, \
       8.3750400000E+00, \
       6.6729600000E+00, \
       0.1612800000E+00, \
      -9.0000000000E+00, \
     -15.4252800000E+00, \
      -9.6969600000E+00, \
      22.4409600000E+00, \
     100.8892800000E+00, \
     252.0000000000E+00 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  2, \
     2,  2,  2, \
     2,  2,  2, \
     2,  2,  2, \
     2,  5,  5, \
     5,  5,  5, \
     5,  5,  5, \
     5,  5,  5, \
     5,  5,  5, \
     5,  5 ))

  x_vec = np.array ( ( \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.20E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
      0.40E+00, \
     -0.50E+00, \
     -0.40E+00, \
     -0.30E+00, \
     -0.20E+00, \
     -0.10E+00, \
      0.00E+00, \
      0.10E+00, \
      0.20E+00, \
      0.30E+00, \
      0.40E+00, \
      0.50E+00, \
      0.60E+00, \
      0.70E+00, \
      0.80E+00, \
      0.90E+00, \
      1.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, a, x, f

def gegenbauer_polynomial_values_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_POLYNOMIAL_VALUES_TEST tests GEGENBAUER_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GEGENBAUER_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEGENBAUER_POLYNOMIAL_VALUES stores values of the Gegenbauer polynomials.' )
  print ( '' )
  print ( '      N            A         X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, a, x, fx = gegenbauer_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %12f  %24.16g' % ( n, a, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gegenbauer_polynomial_values_test ( )
  timestamp ( )

