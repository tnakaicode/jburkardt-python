#! /usr/bin/env python
#
def bessel_i1_spherical_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_I1_SPHERICAL_VALUES returns some values of the Spherical Bessel function i1.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Sqrt[Pi/(2*x)] * BesselI[3/2,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
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
#    LC: QA47.A34,
#    ISBN: 0-486-61272-4.
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

  n_max = 21

  fx_vec = np.array ( ( \
    0.03336667857363341E+00, \
    0.06693371456802954E+00, \
    0.1354788933285401E+00, \
    0.2072931911031093E+00, \
    0.2841280857128948E+00, \
    0.3678794411714423E+00, \
    0.4606425870674146E+00, \
    0.5647736480096238E+00, \
    0.6829590627779635E+00, \
    0.8182955028627777E+00, \
    0.9743827435800610E+00, \
    1.155432469636406E+00, \
    1.366396525527973E+00, \
    1.613118767572064E+00, \
    1.902515460838681E+00, \
    2.242790117769266E+00, \
    2.643689828630357E+00, \
    3.116811526884873E+00, \
    3.675968313148932E+00, \
    4.337627987747642E+00, \
    5.121438384183637E+00 ) )

  x_vec = np.array ( ( \
     0.1E+00, \
     0.2E+00, \
     0.4E+00, \
     0.6E+00, \
     0.8E+00, \
     1.0E+00, \
     1.2E+00, \
     1.4E+00, \
     1.6E+00, \
     1.8E+00, \
     2.0E+00, \
     2.2E+00, \
     2.4E+00, \
     2.6E+00, \
     2.8E+00, \
     3.0E+00, \
     3.2E+00, \
     3.4E+00, \
     3.6E+00, \
     3.8E+00, \
     4.0E+00  ) )

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

def bessel_i1_spherical_values_test ( ):

#*****************************************************************************80
#
## BESSEL_I1_SPHERICAL_VALUES_TEST tests BESSEL_I1_SPHERICAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_I1_SPHERICAL_VALUES_TEST:' )
  print ( '  BESSEL_I1_SPHERICAL_VALUES stores values of the spherical Bessel I function. of order 1.' )
  print ( '' )
  print ( '      X        Spherical I(1,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_i1_spherical_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_I1_SPHERICAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_i1_spherical_values_test ( )
  timestamp ( )
