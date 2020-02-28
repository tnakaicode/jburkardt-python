#! /usr/bin/env python
#
def mittag_leffler_eab_values ( n_data ):

#*****************************************************************************80
#
## MITTAG_LEFFLER_EAB_VALUES: values of two-parameter Mittag Leffler function.
#
#  Discussion:
#
#    E(alpha,beta;z) = sum ( 0 <= k < oo ) z^k / Gamma ( alpha * k + beta )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2017
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
#    Output, real A, B, the parameters.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 18

  a_vec = np.array ( ( \
    1.0, \
    1.0, \
    1.0, \
    1.5, \
    1.5, \
    1.5, \
    3.0, \
    3.0, \
    3.0, \
    1.5, \
    1.5, \
    1.5, \
    1.5, \
    2.0, \
    2.5, \
    2.0, \
    2.0, \
    2.0 ))

  b_vec = np.array ( (\
    0.0, \
    2.5, \
    5.0, \
    0.0, \
    5.0, \
   10.0, \
    1.0, \
    1.1, \
    1.2, \
    5.0, \
   10.0, \
   15.0, \
    5.0, \
    5.0, \
    5.0, \
    1.0, \
    2.0, \
    3.0 ))

  fx_vec = np.array ( ( \
    -0.1947001957678512, \
     0.6821152851737027, \
     0.3966713294631294E-01, \
    -0.7783327874361643, \
     0.376189576668972E-01, \
     0.2653864659692168E-05, \
     0.5521129475536116, \
     0.6561318862220054, \
     0.7417555514147703, \
     0.283627999653323E-01, \
     0.2382766080122566E-05, \
     0.1057337628882522E-10, \
     0.6524069073077504E-01, \
     0.4926693884523065E-01, \
     0.4440848516337653E-01, \
     0.217818355660857E+01, \
     0.1368298872008591E+01, \
     0.5890917783042855 ))

  x_vec = np.array ( ( \
      -0.25, \
      -0.25, \
      -0.25, \
      -1.25, \
      -1.25, \
      -1.25, \
      -2.75, \
      -2.75, \
      -2.75, \
      -5.0, \
      -5.0, \
      -5.0, \
       5.0, \
       5.0, \
       5.0, \
       2.0, \
       2.0, \
       2.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    x = 0.0
    fx = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, x, fx

def mittag_leffler_eab_values_test ( ):

#*****************************************************************************80
#
## MITTAG_LEFFLER_EAB_VALUES_TEST demonstrates MITTAG_LEFFLER_EAB_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'MITTAG_LEFFLER_EAB_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MITTAG_LEFFLER_EAB_VALUES stores values of' )
  print ( '  the Mittag-Leffler three parameter function E(A;X).' )
  print ( '' )
  print ( '        A             B             X               E(A,B;X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, x, fx = mittag_leffler_eab_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %12f  %24.16g' % ( a, b, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'MITTAG_LEFFLER_EAB_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  mittag_leffler_eab_values_test ( )
  timestamp ( )

