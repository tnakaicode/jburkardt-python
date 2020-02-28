#! /usr/bin/env python
#
def cos_values ( n_data ):

#*****************************************************************************80
#
## COS_VALUES returns some values of the cosine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Cos[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 June 2007
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

  n_max = 13

  fx_vec = np.array ( ( \
     1.0000000000000000000, \
     0.96592582628906828675, \
     0.87758256189037271612, \
     0.86602540378443864676, \
     0.70710678118654752440, \
     0.54030230586813971740, \
     0.50000000000000000000, \
     0.00000000000000000000, \
    -0.41614683654714238700, \
    -0.98999249660044545727, \
    -1.0000000000000000000, \
    -0.65364362086361191464, \
     0.28366218546322626447 ))

  x_vec = np.array ( ( \
    0.0000000000000000000, \
    0.26179938779914943654, \
    0.50000000000000000000, \
    0.52359877559829887308, \
    0.78539816339744830962, \
    1.0000000000000000000, \
    1.0471975511965977462, \
    1.5707963267948966192, \
    2.0000000000000000000, \
    3.0000000000000000000, \
    3.1415926535897932385, \
    4.0000000000000000000, \
    5.0000000000000000000 ))

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

def cos_values_test ( ):

#*****************************************************************************80
#
## COS_VALUES_TEST demonstrates the use of COS_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'COS_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COS_VALUES stores values of the cosine function.' )
  print ( '' )
  print ( '      X         COS(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = cos_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COS_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cos_values_test ( )
  timestamp ( )

