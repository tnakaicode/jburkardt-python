#! /usr/bin/env python
#
def hermite_poly_prob_values ( n_data ):

#*****************************************************************************80
#
## HERMITE_POLY_PROB_VALUES: values of the probabilist's Hermite polynomial.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      He(n,x) = HermiteH[n,x/Sqrt[2]] / Sqrt [ 2^n ] 
#
#  First terms:
#
#   1
#   X
#   X^2  -  1
#   X^3  -  3 X
#   X^4  -  6 X^2 +   3
#   X^5  - 10 X^3 +  15 X
#   X^6  - 15 X^4 +  45 X^2 -   15
#   X^7  - 21 X^5 + 105 X^3 -  105 X
#   X^8  - 28 X^6 + 210 X^4 -  420 X^2 +  105
#   X^9  - 36 X^7 + 378 X^5 - 1260 X^3 +  945 X
#   X^10 - 45 X^8 + 630 X^6 - 3150 X^4 + 4725 X^2 - 945
#
#  Recursion:
#
#    He(0,X) = 1,
#    He(1,X) = X,
#    He(N,X) = X * He(N-1,X) - (N-1) * He(N-2,X)
#
#  Norm:
#
#    Integral ( -oo < X < +oo ) exp ( - 0.5 * X^2 ) * He(M,X) He(N,X) dX 
#    = sqrt ( 2 * pi ) * N! * delta ( N, M )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#    Input/output, integer N_DATA.  The user sets N_DATA to 0
#    before the first call.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the order of the polynomial.
#
#    Output, real X, the point where the polynomial is evaluated.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 18

  f_vec = np.array ((\
    1.000000000000000E+00, \
    5.000000000000000E+00, \
    24.00000000000000E+00, \
    110.0000000000000E+00, \
    478.0000000000000E+00, \
    1950.000000000000E+00, \
    7360.000000000000E+00, \
    25100.00000000000E+00, \
    73980.00000000000E+00, \
    169100.0000000000E+00, \
    179680.0000000000E+00, \
   -792600.0000000000E+00, \
   -5939480.000000000E+00, \
    0.000000000000000E+00, \
    6.281250000000000E+00, \
    6.000000000000000E+00, \
    18.00000000000000E+00, \
    90150.00000000000E+00 ))

  n_vec = np.array ((\
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  5,  5, \
     5,  5,  5 ))

  x_vec = np.array ((\
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    5.0E+00, \
    0.0E+00, \
    0.5E+00, \
    1.0E+00, \
    3.0E+00, \
    1.0E+01 ))

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

def hermite_poly_prob_values_test ( ):

#*****************************************************************************80
#
## HERMITE_POLY_PROB_VALUES_TEST demonstrates the use of HERMITE_POLY_PROB_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'HERMITE_POLY_PROB_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HERMITE_POLY_PROB_VALUES stores values of the Hermite probabilist polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = hermite_poly_prob_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HERMITE_POLY_PROB_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hermite_poly_prob_values_test ( )
  timestamp ( )
