#! /usr/bin/env python
#
def arcsin_values ( n_data ):

#*****************************************************************************80
#
## ARCSIN_VALUES returns some values of the arc sine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ArcSin[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
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

  n_max = 12

  fx_vec = np.array ( ( \
    -0.10016742116155979635, \
     0.00000000000000000000, \
     0.10016742116155979635, \
     0.20135792079033079146, \
     0.30469265401539750797, \
     0.41151684606748801938, \
     0.52359877559829887308, \
     0.64350110879328438680, \
     0.77539749661075306374, \
     0.92729521800161223243, \
     1.1197695149986341867, \
     1.5707963267948966192 ) )

  x_vec = np.array ( ( \
    -0.1, \
     0.0, \
     0.1, \
     0.2, \
     0.3, \
     0.4, \
     0.5, \
     0.6, \
     0.7, \
     0.8, \
     0.9, \
     1.0 ) )

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

def arcsin_values_test ( ):

#*****************************************************************************80
#
## ARCSIN_VALUES_TEST tests ARCSIN VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ARCSIN_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCSIN_VALUES stores values of' )
  print ( '  the arc sine function.' )
  print ( '' )
  print ( '        X               F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = arcsin_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCSIN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  arcsin_values_test ( )
  timestamp ( )

