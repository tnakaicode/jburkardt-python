#! /usr/bin/env python
#
def cheby_v01_poly_values ( n_data ):

#*****************************************************************************80
#
## CHEBY_V01_POLY_VALUES: values of shifted Chebyshev polynomials V01(n,x).
#
#  Discussion:
#
#    V01(n,x) = V(n,2*x-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2015
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
#    Output, integer N, the order of the function.
#
#    Output, real X, the point where the function is evaluated.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 25

  fx_vec = np.array ( ( \
     0.0000000000000000, \
     1.0000000000000000, \
     0.4000000000000000, \
    -0.4400000000000000, \
    -1.0160000000000000, \
    -0.9824000000000000, \
    -0.3593600000000000, \
     0.4792960000000000, \
     1.0303744000000000, \
     0.9632281600000000, \
     0.3181450240000000, \
    -0.5178251264000000, \
    -1.0431002009600000, \
    -0.9425151549440000, \
    -15.000000000000000, \
     3.1417984000000000, \
    -1.3912448000000000, \
    -1.2177792000000000, \
     1.1837056000000000, \
     1.0000000000000000, \
    -0.8558976000000000, \
    -0.8905088000000000, \
     0.8752768000000000, \
     0.1197696000000000, \
     1.0000000000000000 ) )

  n_vec = np.array ( ( \
    -1, \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  7,  7, \
     7,  7,  7, \
     7,  7,  7, \
     7,  7,  7 ))

  x_vec = np.array ( ( \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.00, \
    0.10, \
    0.20, \
    0.30, \
    0.40, \
    0.50, \
    0.60, \
    0.70, \
    0.80, \
    0.90, \
    1.00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def cheby_v01_poly_values_test ( ):

#*****************************************************************************80
#
## CHEBY_V01_POLY_VALUES_TEST demonstrates the use of CHEBY_V01_POLY_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHEBY_V01_POLY_VALUES_TEST:' )
  print ( '  CHEBY_V01_POLY_VALUES: values of the shifted Chebyshev V polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = cheby_v01_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBY_V01_POLY_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cheby_v01_poly_values_test ( )
  timestamp ( )

