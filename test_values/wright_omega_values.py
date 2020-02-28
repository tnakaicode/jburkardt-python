#! /usr/bin/env python
#
def wright_omega_values ( n_data ):

#*****************************************************************************80
#
## WRIGHT_OMEGA_VALUES returns values of the Wright Omega function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Corless, David Jeffrey,
#    The Wright Omega Function,
#    in Artificial Intelligence, Automated Reasoning, and Symbolic Computation,
#    ed J Calmet, B Benhamou, O Caprotti, L Henocque, V Sorge,
#    Lecture Notes in Artificial Intelligence, volume 2385,
#    Springer, 2002, pages 76-89.
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

  n_max = 10

  fz_vec = np.array ( [ \
    +0.5671432904097838  +0.0000000000000000j, \
    +1.000000000000000   +0.0000000000000000j, \
    +2.718281828459045   +0.0000000000000000j, \
    -1.000000000000000   +0.0000000000000000j, \
    -1.000000000000000   +0.0000000000000000j, \
    -2.000000000000000   +0.0000000000000000j, \
    -0.40637573995996    +0.0000000000000000j, \
    +0.000000000000000   +1.0000000000000000j, \
    -0.3181315052047641  +1.337235701430689j, \
    +0.9372082083733697  +0.5054213160131512j ] )

  z_vec = np.array ( [ \
     +0.000000000000000   +0.000000000000000j, \
     +1.000000000000000   +0.000000000000000j, \
     +3.718281828459045   +0.000000000000000j, \
     -1.000000000000000   +3.141592653589793j, \
     -1.000000000000000   -3.141592653589793j, \
     -1.306852819440055   +3.141592653589793j, \
     -1.306852819440055   -3.141592653589793j, \
     +0.000000000000000   +2.570796326794897j, \
     +0.000000000000000   +3.141592653589793j, \
     +1.000000000000000   +1.000000000000000j ] )

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

def wright_omega_values_test ( ):

#*****************************************************************************80
#
## WRIGHT_OMEGA_VALUES_TEST demonstrates the use of WRIGHT_OMEGA_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 May 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'WRIGHT_OMEGA_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WRIGHT_OMEGA_VALUES stores values of' )
  print ( '  the Wright Omega function.' )
  print ( '' )
  print ( '        Z.real        Z.imag          FZ.real                FZ.imag' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, z, fz = wright_omega_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %24.16g  %24.16g' \
      % ( z.real, z.imag, fz.real, fz.imag ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'WRIGHT_OMEGA_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  wright_omega_values_test ( )
  timestamp ( )

