#! /usr/bin/env python
#
def sound_values ( n_data ):

#*****************************************************************************80
#
## SOUND_VALUES returns some values of the speed of sound.
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
#    Lester Haar, John Gallagher and George Kell,
#    NBS/NRC Steam Tables:
#    Thermodynamic and Transport Properties and Computer Programs
#    for Vapor and Liquid States of Water in SI Units,
#    Hemisphere Publishing Corporation, Washington, 1984,
#    TJ270.H3, page 238-246.
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
#    Output, real C, the speed of sound, in m/s.
#
  import numpy as np

  n_max = 20

  c_vec = np.array ( ( \
     1401.0E+00, \
      472.8E+00, \
      533.7E+00, \
      585.7E+00, \
      609.5E+00, \
      632.2E+00, \
      674.6E+00, \
      713.9E+00, \
      802.0E+00, \
      880.1E+00, \
     1017.8E+00, \
     1115.9E+00, \
     1401.7E+00, \
     1402.6E+00, \
     1409.6E+00, \
     1418.1E+00, \
     1443.1E+00, \
     1484.6E+00, \
     1577.1E+00, \
     1913.4E+00 ))

  p_vec = np.array ( ( \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        1.0E+00, \
        5.0E+00, \
       10.0E+00, \
       50.0E+00, \
      100.0E+00, \
      250.0E+00, \
      500.0E+00, \
     1000.0E+00, \
     2500.0E+00 ))

  tc_vec = np.array ( ( \
        0.0E+00, \
      100.0E+00, \
      200.0E+00, \
      300.0E+00, \
      350.0E+00, \
      400.0E+00, \
      500.0E+00, \
      600.0E+00, \
      850.0E+00, \
     1100.0E+00, \
     1600.0E+00, \
     2000.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00, \
        0.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    tc = 0.0
    p = 0.0
    c = 0.0
  else:
    tc = tc_vec[n_data]
    p = p_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, tc, p, c

def sound_values_test ( ):

#*****************************************************************************80
#
## SOUND_VALUES_TEST demonstrates the use of SOUND_VALUES.
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
  print ( 'SOUND_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SOUND_VALUES stores values of the SOUND function.' )
  print ( '' )
  print ( '      TC         P        SOUND(TC.P)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, tc, p, c = sound_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16f' % ( tc, p, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SOUND_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sound_values_test ( )
  timestamp ( )

