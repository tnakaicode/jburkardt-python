#! /usr/bin/env python
#
def arctan2_values ( n_data ):

#*****************************************************************************80
#
## ARCTAN2_VALUES: arc tangent function of two arguments.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ArcTan[x,y]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
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
#    Output, real X, Y, the arguments of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 19

  f_vec = np.array ( ( \
   -1.5707963267948966192, \
   -1.0471975511965977462, \
   -0.52359877559829887308, \
    0.00000000000000000000, \
    0.52359877559829887308, \
    1.0471975511965977462, \
    1.5707963267948966192, \
    2.0943951023931954923, \
    2.6179938779914943654, \
    3.1415926535897932385, \
   -2.6179938779914943654, \
   -2.0943951023931954923, \
   -1.5707963267948966192, \
   -1.0471975511965977462, \
   -0.52359877559829887308, \
    0.00000000000000000000, \
    0.52359877559829887308, \
    1.0471975511965977462, \
    1.5707963267948966192 ) )

  x_vec = np.array ( ( \
    0.00000000000000000000, \
    0.50000000000000000000, \
    0.86602540378443864676, \
    1.00000000000000000000, \
    0.86602540378443864676, \
    0.50000000000000000000, \
    0.00000000000000000000, \
   -0.50000000000000000000, \
   -0.86602540378443864676, \
   -1.00000000000000000000, \
   -0.86602540378443864676, \
   -0.50000000000000000000, \
    0.00000000000000000000, \
    0.50000000000000000000, \
    0.86602540378443864676, \
    1.00000000000000000000, \
    0.86602540378443864676, \
    0.50000000000000000000, \
    0.00000000000000000000 ) )

  y_vec = np.array ( ( \
   -1.00000000000000000000, \
   -0.86602540378443864676, \
   -0.50000000000000000000, \
    0.00000000000000000000, \
    0.50000000000000000000, \
    0.86602540378443864676, \
    1.00000000000000000000, \
    0.86602540378443864676, \
    0.50000000000000000000, \
    0.00000000000000000000, \
   -0.50000000000000000000, \
   -0.86602540378443864676, \
   -1.00000000000000000000, \
   -0.86602540378443864676, \
   -0.50000000000000000000, \
    0.00000000000000000000, \
    0.50000000000000000000, \
    0.86602540378443864676, \
    1.00000000000000000000 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    y = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    y = y_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, y, f

def arctan2_values_test ( ):

#*****************************************************************************80
#
## ARCTAN2_VALUES_TEST tests ARCTAN2 VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ARCTAN2_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCTAN_VALUES stores values of' )
  print ( '  the arc tangent function.' )
  print ( '' )
  print ( '        X           Y               F(X,Y)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, y, f = arctan2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( x, y, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCTAN2_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  arctan2_values_test ( )
  timestamp ( )

