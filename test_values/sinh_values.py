#! /usr/bin/env python
#
def sinh_values ( n_data ):

#*****************************************************************************80
#
## SINH_VALUES returns some values of the hyperbolic sine function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Sinh[x]
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
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 18

  f_vec = np.array ( ( \
      -74.203210577788758977, \
       -1.1752011936438014569, \
        0.00000000000000000000, \
        0.10016675001984402582, \
        0.20133600254109398763, \
        0.30452029344714261896, \
        0.41075232580281550854, \
        0.52109530549374736162, \
        0.63665358214824127112, \
        0.75858370183953350346, \
        0.88810598218762300657, \
        1.0265167257081752760, \
        1.1752011936438014569, \
        3.6268604078470187677, \
       10.017874927409901899, \
       27.289917197127752449, \
       74.203210577788758977, \
    11013.232874703393377 ))

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
   10.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def sinh_values_test ( ):

#*****************************************************************************80
#
## SINH_VALUES_TEST demonstrates the use of SINH_VALUES.
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
  print ( 'SINH_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SINH_VALUES stores values of the SINH function.' )
  print ( '' )
  print ( '      X         SINH(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = sinh_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SINH_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sinh_values_test ( )
  timestamp ( )

