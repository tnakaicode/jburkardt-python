#! /usr/bin/env python
#
def c8_log_values ( n_data ):

#*****************************************************************************80
#
## C8_LOG_VALUES returns values of the complex logarithm function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 January 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Collens,
#    Algorithm 243: Logarithm of a Complex Number,
#    Communications of the Association for Computing Machinery,
#    Volume 7, Number 11, November 1964, page 660.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, complex X, the argument of the function.
#
#    Output, complex CAI, the value of the function.
#
  import numpy as np

  n_max = 12

  fz_vec = np.array ( [ \
  1.039720770839918 - 2.356194490192345j, \
  0.804718956217050 + 2.677945044588987j, \
  0.346573590279973 - 2.356194490192345j, \
  0.000000000000000 + 3.141592653589793j, \
  0.693147180559945 - 1.570796326794897j, \
  0.000000000000000 - 1.570796326794897j, \
  0.000000000000000 + 1.570796326794897j, \
  0.693147180559945 + 1.570796326794897j, \
  0.346573590279973 - 0.785398163397448j, \
  0.000000000000000 + 0.000000000000000j, \
  1.039720770839918 - 0.785398163397448j, \
  0.804718956217050 + 0.463647609000806j ] )

  z_vec = np.array ( [ \
    -2.0 - 2.0j, \
    -2.0 + 1.0j, \
    -1.0 - 1.0j, \
    -1.0 + 0.0j, \
     0.0 - 2.0j, \
     0.0 - 1.0j, \
     0.0 + 1.0j, \
     0.0 + 2.0j, \
     1.0 - 1.0j, \
     1.0 + 0.0j, \
     2.0 - 2.0j, \
     2.0 + 1.0j ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    z = 0.0 + 0.0j
    fz = 0.0 + 0.0j
  else:
    z = z_vec[n_data]
    fz = fz_vec[n_data]
    n_data = n_data + 1

  return n_data, z, fz

def c8_log_values_test ( ):

#*****************************************************************************80
#
## C8_LOG_VALUES_TEST tests C8_LOG_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 January 2019
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'C8_LOG_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8_LOG_VALUES stores values of' )
  print ( '  the complex logarithm function.' )
  print ( '' )
  print ( '        Z.real        Z.imag          FZ.real                FZ.imag' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, z, fz = c8_log_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %24.16g  %24.16g' \
      % ( z.real, z.imag, fz.real, fz.imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8_LOG_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8_log_values_test ( )
  timestamp ( )
