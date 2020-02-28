#! /usr/bin/env python
#
def viscosity_values ( n_data ):

#*****************************************************************************80
#
## VISCOSITY_VALUES returns some values of the viscosity function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
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
#    TJ270.H3, page 263.
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
#    Output, real ETA, the viscosity, in MegaPascal seconds.
#
  import numpy as np

  n_max = 34

  eta_vec = np.array ( ( \
     1792.0E+00, \
     1791.0E+00, \
     1790.0E+00, \
     1786.0E+00, \
     1780.0E+00, \
     1775.0E+00, \
     1769.0E+00, \
     1764.0E+00, \
     1759.0E+00, \
     1754.0E+00, \
     1749.0E+00, \
     1744.0E+00, \
     1739.0E+00, \
     1735.0E+00, \
     1731.0E+00, \
     1722.0E+00, \
     1714.0E+00, \
     1707.0E+00, \
     1700.0E+00, \
     1694.0E+00, \
     1687.0E+00, \
     1682.0E+00, \
     1676.0E+00, \
     1667.0E+00, \
     1659.0E+00, \
     1653.0E+00, \
      890.8E+00, \
      547.1E+00, \
      378.4E+00, \
      12.28E+00, \
      16.18E+00, \
      24.45E+00, \
      32.61E+00, \
      40.38E+00 ))

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
    eta = 0.0
  else:
    tc = tc_vec[n_data]
    p = p_vec[n_data]
    eta = eta_vec[n_data]
    n_data = n_data + 1

  return n_data, tc, p, eta

def viscosity_values_test ( ):

#*****************************************************************************80
#
## VISCOSITY_VALUES_TEST demonstrates the use of VISCOSITY_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'VISCOSITY_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VISCOSITY_VALUES stores values of the VISCOSITY function.' )
  print ( '' )
  print ( '      TC         P        ETA(TC,P)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, tc, p, eta = viscosity_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %24.16g' % ( tc, p, eta ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'VISCOSITY_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  viscosity_values_test ( )
  timestamp ( )

