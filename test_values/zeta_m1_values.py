#! /usr/bin/env python
#
def zeta_m1_values ( n_data ):

#*****************************************************************************80
#
## ZETA_M1_VALUES returns some values of the Riemann Zeta function minus 1.
#
#  Discussion:
#
#    ZETA_M1(N) = ZETA(N) - 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2016
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
#    Output, real P, the argument.
#
#    Output, real F, the value.
#
  import numpy as np

  n_max = 17

  p_vec = np.array ( ( \
     2.0, \
     2.5, \
     3.0, \
     3.5, \
     4.0, \
     5.0, \
     6.0, \
     7.0, \
     8.0, \
     9.0, \
    10.0, \
    11.0, \
    12.0, \
    16.0, \
    20.0, \
    30.0, \
    40.0 ))

  f_vec = np.array ( ( \
     0.64493406684822643647E+00, \
     0.3414872573E+00, \
     0.20205690315959428540E+00, \
     0.1267338673E+00, \
     0.8232323371113819152E-01, \
     0.3692775514336992633E-01, \
     0.1734306198444913971E-01, \
     0.834927738192282684E-02, \
     0.407735619794433939E-02, \
     0.200839292608221442E-02, \
     0.99457512781808534E-03, \
     0.49418860411946456E-03, \
     0.24608655330804830E-03, \
     0.1528225940865187E-04, \
     0.95396203387280E-06, \
     0.93132743242E-10, \
     0.90949478E-12 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    p = 0.0
    f = 0.0
  else:
    p = p_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, p, f

def zeta_m1_values_test ( ):

#*****************************************************************************80
#
## ZETA_M1_VALUES_TEST demonstrates the use of ZETA_M1_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ZETA_M1_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ZETA_M1_VALUES stores values of the ZETA_MINUS_ONE function.' )
  print ( '' )
  print ( '      N         ZETA_M1(N)' )
  print ( '' )

  n_data = 0

  while ( True ):
    n_data, p, f = zeta_m1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8f  %24.16e' % ( p, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ZETA_M1_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  zeta_m1_values_test ( )
  timestamp ( )

