#! /usr/bin/env python
#
def prandtl_values ( n_data ):

#*****************************************************************************80
#
## PRANDTL_VALUES returns some values of the Prandtl number.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Lester Haar, John Gallagher and George Kell,
#    NBS/NRC Steam Tables:
#    Thermodynamic and Transport Properties and Computer Programs
#    for Vapor and Liquid States of Water in SI Units,
#    Hemisphere Publishing Corporation, Washington, 1984,
#    TJ270.H3, page 265.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real TC, the temperature, in degrees Celsius.
#
#    Output, real P, the pressure, in bar.
#
#    Output, real PR, the Prandtl number, dimensionless.
#
  import numpy as np

  n_max = 35

  pr_vec = np.array ( ( \
     13.50E+00, \
     13.48E+00, \
     13.46E+00, \
     13.39E+00, \
     13.27E+00, \
     13.15E+00, \
     13.04E+00, \
     12.93E+00, \
     12.83E+00, \
     12.73E+00, \
     12.63E+00, \
     12.53E+00, \
     12.43E+00, \
     12.34E+00, \
     12.25E+00, \
     12.08E+00, \
     11.92E+00, \
     11.77E+00, \
     11.62E+00, \
     11.48E+00, \
     11.36E+00, \
     11.23E+00, \
     11.12E+00, \
     10.91E+00, \
     10.72E+00, \
     10.55E+00, \
      6.137E+00, \
      3.555E+00, \
      2.378E+00, \
      1.000E+00, \
      0.974E+00, \
      0.960E+00, \
      0.924E+00, \
      0.899E+00, \
      0.882E+00 ))

  p_vec = np.array ( ( \
        1.0E+00, \
        5.0E+00, \
       10.0E+00, \
       25.0E+00, \
       50.0E+00, \
       75.0E+00, \
      100.0E+00, \
      125.0E+00, \
      150.0E+00, \
      175.0E+00, \
      200.0E+00, \
      225.0E+00, \
      250.0E+00, \
      275.0E+00, \
      300.0E+00, \
      350.0E+00, \
      400.0E+00, \
      450.0E+00, \
      500.0E+00, \
      550.0E+00, \
      600.0E+00, \
      650.0E+00, \
      700.0E+00, \
      800.0E+00, \
      900.0E+00, \
     1000.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00 ))

  tc_vec = np.array ( ( \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
       0.0E+00, \
      25.0E+00, \
      50.0E+00, \
      75.0E+00, \
     100.0E+00, \
     150.0E+00, \
     200.0E+00, \
     400.0E+00, \
     600.0E+00, \
     800.0E+00 ))


  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    tc = 0.0
    p = 0.0
    pr = 0.0
  else:
    tc = tc_vec[n_data]
    p = p_vec[n_data]
    pr = pr_vec[n_data]
    n_data = n_data + 1

  return n_data, tc, p, pr

def prandtl_values_test ( ):

#*****************************************************************************80
#
## PRANDTL_VALUES_TEST demonstrates the use of PRANDTL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'PRANDTL_VALUES_TEST:' )
  print ( '  PRANDTL_VALUES stores values of the PRANDTL function.' )
  print ( '' )
  print ( '      TC         P        PRANDTL(TC.P)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, tc, p, pr = prandtl_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16f' % ( tc, p, pr ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PRANDTL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  prandtl_values_test ( )
  timestamp ( )

