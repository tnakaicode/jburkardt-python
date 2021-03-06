#! /usr/bin/env python
#
def chi_square_cdf_values ( n_data ):

#*****************************************************************************80
#
## CHI_SQUARE_CDF_VALUES returns some values of the Chi-Square CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = ChiSquareDistribution [ df ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
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
#    Output, integer A, the parameter of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  a_vec = np.array ( ( \
     1,  2,  1,  2, \
     1,  2,  3,  4, \
     1,  2,  3,  4, \
     5,  3,  3,  3, \
     3,  3, 10, 10, \
    10  ) )

  f_vec = np.array ( ( \
     0.7965567455405796E-01, \
     0.4987520807317687E-02, \
     0.1124629160182849E+00, \
     0.9950166250831946E-02, \
     0.4729107431344619E+00, \
     0.1812692469220181E+00, \
     0.5975750516063926E-01, \
     0.1752309630642177E-01, \
     0.6826894921370859E+00, \
     0.3934693402873666E+00, \
     0.1987480430987992E+00, \
     0.9020401043104986E-01, \
     0.3743422675270363E-01, \
     0.4275932955291202E+00, \
     0.6083748237289110E+00, \
     0.7385358700508894E+00, \
     0.8282028557032669E+00, \
     0.8883897749052874E+00, \
     0.1721156299558408E-03, \
     0.3659846827343712E-02, \
     0.1857593622214067E-01 ) )

  x_vec = np.array ( ( \
     0.01E+00, \
     0.01E+00, \
     0.02E+00, \
     0.02E+00, \
     0.40E+00, \
     0.40E+00, \
     0.40E+00, \
     0.40E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     2.00E+00, \
     3.00E+00, \
     4.00E+00, \
     5.00E+00, \
     6.00E+00, \
     1.00E+00, \
     2.00E+00, \
     3.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, x, f

def chi_square_cdf_values_test ( ):

#*****************************************************************************80
#
## CHI_SQUARE_CDF_VALUES_TEST tests CHI_SQUARE_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHI_SQUARE_CDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHI_SQUARE_CDF_VALUES stores values of the Chi Square CDF.' )
  print ( '' )
  print ( '      A       X        CHI_SQUARE_CDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, f = chi_square_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12f  %24.16g' % ( a, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHI_SQUARE_CDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chi_square_cdf_values_test ( )
  timestamp ( )

