#! /usr/bin/env python
#
def debye2_values ( n_data ):

#*****************************************************************************80
#
## DEBYE2_VALUES returns some values of Debye's function of order 2.
#
#  Discussion:
#
#    The function is defined by:
#
#      DEBYE2(x) = 2 / x^2 * Integral ( 0 <= t <= x ) t^2 / ( exp ( t ) - 1 ) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#      special functions,
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
      0.99934911727904599738E+00, \
      0.98962402299599181205E+00, \
      0.95898426200345986743E+00, \
      0.84372119334725358934E+00, \
      0.70787847562782928288E+00, \
      0.59149637225671282917E+00, \
      0.49308264399053185014E+00, \
      0.41079413579749669069E+00, \
      0.34261396060786351671E+00, \
      0.24055368752127897660E+00, \
      0.22082770061202308232E+00, \
      0.17232915939014138975E+00, \
      0.14724346738730182894E+00, \
      0.12666919046715789982E+00, \
      0.74268805954862854626E-01, \
      0.47971498020121871622E-01, \
      0.21369201683658373846E-01, \
      0.12020564476446432799E-01, \
      0.53424751249537071952E-02, \
      0.19232910450553508562E-02 ))

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0312500000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       1.5000000000E+00, \
       2.0000000000E+00, \
       2.5000000000E+00, \
       3.0000000000E+00, \
       4.0000000000E+00, \
       4.2500000000E+00, \
       5.0000000000E+00, \
       5.5000000000E+00, \
       6.0000000000E+00, \
       8.0000000000E+00, \
      10.0000000000E+00, \
      15.0000000000E+00, \
      20.0000000000E+00, \
      30.0000000000E+00, \
      50.0000000000E+00 ))

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

def debye2_values_test ( ):

#*****************************************************************************80
#
## DEBYE2_VALUES_TEST demonstrates the use of DEBYE2_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DEBYE2_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DEBYE2_VALUES stores values of the Debye function of order 2.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = debye2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DEBYE2_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  debye2_values_test ( )
  timestamp ( )

