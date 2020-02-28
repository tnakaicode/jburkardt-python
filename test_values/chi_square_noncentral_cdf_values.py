#! /usr/bin/env python
#
def chi_square_noncentral_cdf_values ( n_data ):

#*****************************************************************************80
#
## CHI_SQUARE_NONCENTRAL_CDF_VALUES returns values of the noncentral chi CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NoncentralChiSquareDistribution [ df, lambda ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
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
#    Output, integer DF, the number of degrees of freedom.
#
#    Output, real LAMBDA, the noncentrality parameter.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the noncentral chi CDF.
#
  import numpy as np

  n_max = 28

  df_vec = np.array ( ( \
      1,   2,   3, \
      1,   2,   3, \
      1,   2,   3, \
      1,   2,   3, \
     60,  80, 100, \
      1,   2,   3, \
     10,  10,  10, \
     10,  10,  10, \
     10,  10,  10, \
      8 ) )

  f_vec = np.array ( ( \
     0.8399444269398261E+00, \
     0.6959060300435139E+00, \
     0.5350879697078847E+00, \
     0.7647841496310313E+00, \
     0.6206436532195436E+00, \
     0.4691667375373180E+00, \
     0.3070884345937569E+00, \
     0.2203818092990903E+00, \
     0.1500251895581519E+00, \
     0.3071163194335791E-02, \
     0.1763982670131894E-02, \
     0.9816792594625022E-03, \
     0.1651753140866208E-01, \
     0.2023419573950451E-03, \
     0.4984476352854074E-06, \
     0.1513252400654827E-01, \
     0.2090414910614367E-02, \
     0.2465021206048452E-03, \
     0.2636835050342939E-01, \
     0.1857983220079215E-01, \
     0.1305736595486640E-01, \
     0.5838039534819351E-01, \
     0.4249784402463712E-01, \
     0.3082137716021596E-01, \
     0.1057878223400849E+00, \
     0.7940842984598509E-01, \
     0.5932010895599639E-01, \
     0.2110395656918684E+00 ) )

  lam_vec = np.array ( ( \
       0.5E+00, \
       0.5E+00, \
       0.5E+00, \
       1.0E+00, \
       1.0E+00, \
       1.0E+00, \
       5.0E+00, \
       5.0E+00, \
       5.0E+00, \
      20.0E+00, \
      20.0E+00, \
      20.0E+00, \
      30.0E+00, \
      30.0E+00, \
      30.0E+00, \
       5.0E+00, \
       5.0E+00, \
       5.0E+00, \
       2.0E+00, \
       3.0E+00, \
       4.0E+00, \
       2.0E+00, \
       3.0E+00, \
       4.0E+00, \
       2.0E+00, \
       3.0E+00, \
       4.0E+00, \
       0.5E+00 ) )

  x_vec = np.array ( ( \
      3.000E+00, \
      3.000E+00, \
      3.000E+00, \
      3.000E+00, \
      3.000E+00, \
      3.000E+00, \
      3.000E+00, \
      3.000E+00, \
      3.000E+00, \
      3.000E+00, \
      3.000E+00, \
      3.000E+00, \
     60.000E+00, \
     60.000E+00, \
     60.000E+00, \
      0.050E+00, \
      0.050E+00, \
      0.050E+00, \
      4.000E+00, \
      4.000E+00, \
      4.000E+00, \
      5.000E+00, \
      5.000E+00, \
      5.000E+00, \
      6.000E+00, \
      6.000E+00, \
      6.000E+00, \
      5.000E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    df = 0
    lam = 0.0
    x = 0.0
    f = 0.0
  else:
    df = df_vec[n_data]
    lam = lam_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, df, lam, x, f

def chi_square_noncentral_cdf_values_test ( ):

#*****************************************************************************80
#
## CHI_SQUARE_NONCENTRAL_CDF_VALUES_TEST tests CHI_SQUARE_NONCENTRAL_CDF_VALUES.
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
  print ( 'CHI_SQUARE_NONCENTRAL_CDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHI_SQUARE_NONCENTRAL_CDF_VALUES: values of the noncentral Chi Square CDF.' )
  print ( '' )
  print ( '      DF      LAM      X        CHI_SQUARE_NONCENTRAL_CDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, df, lam, x, f = chi_square_noncentral_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12f  %12f  %24.16g' % ( df, lam, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHI_SQUARE_NONCENTRAL_CDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chi_square_noncentral_cdf_values_test ( )
  timestamp ( )

