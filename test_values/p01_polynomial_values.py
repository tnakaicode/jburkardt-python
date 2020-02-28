#! /usr/bin/env python
#
def p01_polynomial_values ( n_data ):

#*****************************************************************************80
#
## P01_POLYNOMIAL_VALUES returns values of the shifted Legendre polynomials.
#
#  Discussion:
#
#    If we denote the Legendre polynomial by P(n)(x), and the shifted 
#    Legendre polynomial by P01(n)(x), then
#
#      P01(n)(x) = P(n)(2*x-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the order of the function.
#
#    Output, real X, the point where the function is evaluated.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 22

  f_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.2500000000000000E+00, \
     -0.4062500000000000E+00, \
     -0.3359375000000000E+00, \
      0.1577148437500000E+00, \
      0.3397216796875000E+00, \
      0.2427673339843750E-01, \
     -0.2799186706542969E+00, \
     -0.1524540185928345E+00, \
      0.1768244206905365E+00, \
      0.2212002165615559E+00, \
      0.0000000000000000E+00, \
     -0.1475000000000000E+00, \
     -0.2800000000000000E+00, \
     -0.3825000000000000E+00, \
     -0.4400000000000000E+00, \
     -0.4375000000000000E+00, \
     -0.3600000000000000E+00, \
     -0.1925000000000000E+00, \
      0.8000000000000000E-01, \
      0.4725000000000000E+00, \
      0.1000000000000000E+01 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3 ))

  x_vec = np.array ( ( \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.625E+00, \
     0.50E+00, \
     0.55E+00, \
     0.60E+00, \
     0.65E+00, \
     0.70E+00, \
     0.75E+00, \
     0.80E+00, \
     0.85E+00, \
     0.90E+00, \
     0.95E+00, \
     1.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def p01_polynomial_values_test ( ):

#*****************************************************************************80
#
## P01_POLYNOMIAL_VALUES_TEST tests P01_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'P01_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P01_POLYNOMIAL_VALUES stores values of the shifted Legendre polynomials.' )
  print ( '' )
  print ( '      N            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = p01_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12g  %24.16g' % ( n, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P01_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  p01_polynomial_values_test ( )
  timestamp ( )

