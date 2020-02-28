#! /usr/bin/env python
#
def rayleigh_cdf_values ( n_data ):

#*****************************************************************************80
#
## RAYLEIGH_CDF_VALUES returns some values of the Rayleigh CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = RayleighDistribution [ sigma ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
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
#    Output, real SIGMA, the shape parameter of the distribution.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 9

  f_vec = np.array ( ( \
     0.8646647167633873E+00, \
     0.9996645373720975E+00, \
     0.9999999847700203E+00, \
     0.999999999999987E+00, \
     0.8646647167633873E+00, \
     0.3934693402873666E+00, \
     0.1992625970831920E+00, \
     0.1175030974154046E+00, \
     0.7688365361336422E-01 ))

  sigma_vec = np.array ( ( \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.5000000000000000E+00, \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.4000000000000000E+01, \
     0.5000000000000000E+01 ))

  x_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.3000000000000000E+01, \
     0.4000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01, \
     0.2000000000000000E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    sigma = 0.0
    x = 0.0
    f = 0.0
  else:
    sigma = sigma_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, sigma, x, f

def rayleigh_cdf_values_test ( ):

#*****************************************************************************80
#
## RAYLEIGH_CDF_VALUES_TEST tests RAYLEIGH_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'RAYLEIGH_CDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RAYLEIGH_CDF_VALUES stores values of the Rayleigh CDF.' )
  print ( '' )
  print ( '      SIGMA       X        RAYLEIGH_CDF(SIGMA,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, sigma, x, f = rayleigh_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( sigma, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RAYLEIGH_CDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rayleigh_cdf_values_test ( )
  timestamp ( )

