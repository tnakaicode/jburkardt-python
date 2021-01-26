#! /usr/bin/env python
#
def erfc_values ( n_data ):

#*****************************************************************************80
#
## ERFC_VALUES returns some values of the ERFC or "complementary error" function.
#
#  Discussion:
#
#    The complementary error function is defined by:
#
#      ERFC(X) = 1 - ( 2 / sqrt ( PI ) * integral ( 0 <= T <= X ) exp ( - T^2 ) dT
#
#    In Mathematica, the function can be evaluated by:
#
#      Erfc[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
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
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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
    1.000000000000000E+00, \
    0.7772974107895215E+00, \
    0.5716076449533315E+00, \
    0.3961439091520741E+00, \
    0.2578990352923395E+00, \
    0.1572992070502851E+00, \
    0.08968602177036462E+00, \
    0.04771488023735119E+00, \
    0.02365161665535599E+00, \
    0.01090949836426929E+00, \
    0.004677734981047266E+00, \
    0.001862846297981891E+00, \
    0.0006885138966450786E+00, \
    0.0002360344165293492E+00, \
    0.00007501319466545902E+00, \
    0.00002209049699858544E+00, \
    6.025761151762095E-06, \
    1.521993362862285E-06, \
    3.558629930076853E-07, \
    7.700392745696413E-08, \
    1.541725790028002E-08 ) )

  x_vec = np.array ( ( \
    0.0E+00, \
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
    4.0E+00 ) )

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

def erfc_values_test ( ):

#*****************************************************************************80
#
## ERFC_VALUES_TEST demonstrates the use of ERFC_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ERFC_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ERFC_VALUES stores values of the complementary error function.' )
  print ( '' )
  print ( '      X         ERFC(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = erfc_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ERFC_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  erfc_values_test ( )
  timestamp ( )

