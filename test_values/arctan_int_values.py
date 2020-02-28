#! /usr/bin/env python
#
def arctan_int_values ( n_data ):

#*****************************************************************************80
#
## ARCTAN_INT_VALUES returns some values of the inverse tangent integral.
#
#  Discussion:
#
#    The function is defined by:
#
#      ARCTAN_INT(x) = Integral ( 0 <= t <= x ) arctan ( t ) / t dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
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

  n_max = 20

  fx_vec = np.array ( ( \
      0.19531241721588483191E-02, \
     -0.39062433772980711281E-02, \
      0.78124470192576499535E-02, \
      0.15624576181996527280E-01, \
     -0.31246610349485401551E-01, \
      0.62472911335014397321E-01, \
      0.12478419717389654039E+00, \
     -0.24830175098230686908E+00, \
      0.48722235829452235711E+00, \
      0.91596559417721901505E+00, \
      0.12749694484943800618E+01, \
     -0.15760154034463234224E+01, \
      0.24258878412859089996E+01, \
      0.33911633326292997361E+01, \
      0.44176450919422186583E+01, \
     -0.47556713749547247774E+01, \
      0.50961912150934111303E+01, \
      0.53759175735714876256E+01, \
     -0.61649904785027487422E+01, \
      0.72437843013083534973E+01 ) )

  x_vec = np.array ( ( \
       0.0019531250E+00, \
      -0.0039062500E+00, \
       0.0078125000E+00, \
       0.0156250000E+00, \
      -0.0312500000E+00, \
       0.0625000000E+00, \
       0.1250000000E+00, \
      -0.2500000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       1.5000000000E+00, \
      -2.0000000000E+00, \
       4.0000000000E+00, \
       8.0000000000E+00, \
      16.0000000000E+00, \
     -20.0000000000E+00, \
      25.0000000000E+00, \
      30.0000000000E+00, \
     -50.0000000000E+00, \
     100.0000000000E+00 ) )

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

def arctan_int_values_test ( ):

#*****************************************************************************80
#
## ARCTAN_INT_VALUES_TEST tests ARCTAN_INT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ARCTAN_INT_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCTAN_INT_VALUES stores values of' )
  print ( '  the arc tangent integral.' )
  print ( '' )
  print ( '        X               F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = arctan_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCTAN_INT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  arctan_int_values_test ( )
  timestamp ( )

