#! /usr/bin/env python
#
def arccos_values ( n_data ):

#*****************************************************************************80
#
## ARCCOS_VALUES returns some values of the arc cosine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ArcCos[x]
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
    1.6709637479564564156, \
    1.5707963267948966192, \
    1.4706289056333368229, \
    1.3694384060045658278, \
    1.2661036727794991113, \
    1.1592794807274085998, \
    1.0471975511965977462, \
    0.92729521800161223243, \
    0.79539883018414355549, \
    0.64350110879328438680, \
    0.45102681179626243254, \
    0.00000000000000000000 ) )

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

def arccos_values_test ( ):

#*****************************************************************************80
#
## ARCCOS_VALUES_TEST tests ARCCOS VALUES.
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
  print ( 'ARCCOS_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCCOS_VALUES stores values of' )
  print ( '  the arc cosine function.' )
  print ( '' )
  print ( '        X               F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = arccos_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCCOS_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  arccos_values_test ( )
  timestamp ( )

