#! /usr/bin/env python
#
def arcsinh_values ( n_data ):

#*****************************************************************************80
#
## ARCSINH_VALUES returns some values of the hyperbolic arc sine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ArcSinh[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2007
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

  n_max = 20

  fx_vec = np.array ( ( \
    -2.3124383412727526203, \
    -0.88137358701954302523, \
     0.00000000000000000000, \
     0.099834078899207563327, \
     0.19869011034924140647, \
     0.29567304756342243910, \
     0.39003531977071527608, \
     0.48121182505960344750, \
     0.56882489873224753010, \
     0.65266656608235578681, \
     0.73266825604541086415, \
     0.80886693565278246251, \
     0.88137358701954302523, \
     1.4436354751788103425, \
     1.8184464592320668235, \
     2.0947125472611012942, \
     2.3124383412727526203, \
     2.9982229502979697388, \
     5.2983423656105887574, \
     7.6009027095419886115 ) )

  x_vec = np.array ( ( \
       -5.0, \
       -1.0, \
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
        1.0, \
        2.0, \
        3.0, \
        4.0, \
        5.0, \
       10.0, \
      100.0, \
     1000.0 ) )

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

def arcsinh_values_test ( ):

#*****************************************************************************80
#
## ARCSINH_VALUES_TEST tests ARCSINH_VALUES.
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
  print ( 'ARCSINH_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCSINH_VALUES stores values of' )
  print ( '  the hyperbolic arc sine function.' )
  print ( '' )
  print ( '        X               F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = arcsinh_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCSINH_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  arcsinh_values_test ( )
  timestamp ( )

