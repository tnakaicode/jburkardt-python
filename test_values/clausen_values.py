#! /usr/bin/env python
#
def clausen_values ( n_data ):

#*****************************************************************************80
#
## CLAUSEN_VALUES returns some values of the Clausen's integral.
#
#  Discussion:
#
#    The function is defined by:
#
#      CLAUSEN(x) = Integral ( 0 <= t <= x ) -ln ( 2 * sin ( t / 2 ) ) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964, page 1006.
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
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
      0.14137352886760576684E-01, \
      0.13955467081981281934E+00, \
     -0.38495732156574238507E+00, \
      0.84831187770367927099E+00, \
      0.10139591323607685043E+01, \
     -0.93921859275409211003E+00, \
      0.72714605086327924743E+00, \
      0.43359820323553277936E+00, \
     -0.98026209391301421161E-01, \
     -0.56814394442986978080E+00, \
     -0.70969701784448921625E+00, \
      0.99282013254695671871E+00, \
     -0.98127747477447367875E+00, \
     -0.64078266570172320959E+00, \
      0.86027963733231192456E+00, \
      0.39071647608680211043E+00, \
      0.47574793926539191502E+00, \
      0.10105014481412878253E+01, \
      0.96332089044363075154E+00, \
     -0.61782699481929311757E+00 ) )

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0312500000E+00, \
      -0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
      -1.5000000000E+00, \
       2.0000000000E+00, \
       2.5000000000E+00, \
      -3.0000000000E+00, \
       4.0000000000E+00, \
       4.2500000000E+00, \
      -5.0000000000E+00, \
       5.5000000000E+00, \
       6.0000000000E+00, \
       8.0000000000E+00, \
     -10.0000000000E+00, \
      15.0000000000E+00, \
      20.0000000000E+00, \
     -30.0000000000E+00, \
      50.0000000000E+00  ) )

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

def clausen_values_test ( ):

#*****************************************************************************80
#
## CLAUSEN_VALUES_TEST demonstrates the use of CLAUSEN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CLAUSEN_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CLAUSEN_VALUES stores values of the Clausen integral function.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = clausen_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CLAUSEN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  clausen_values_test ( )
  timestamp ( )

