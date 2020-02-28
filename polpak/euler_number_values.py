#! /usr/bin/env python
#
def euler_number_values ( n_data ):

#*****************************************************************************80
#
## EULER_NUMBER_VALUES returns some values of the Euler numbers.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      EulerE[n]
#
#    These numbers rapidly get too big to store in an ordinary integer!
#
#    The terms of odd index are 0.
#
#    E(N) = -C(N,N-2) * E(N-2) - C(N,N-4) * E(N-4) - ... - C(N,0) * E(0).
#
#  First terms:
#
#    E0  = 1
#    E1  = 0
#    E2  = -1
#    E3  = 0
#    E4  = 5
#    E5  = 0
#    E6  = -61
#    E7  = 0
#    E8  = 1385
#    E9  = 0
#    E10 = -50521
#    E11 = 0
#    E12 = 2702765
#    E13 = 0
#    E14 = -199360981
#    E15 = 0
#    E16 = 19391512145
#    E17 = 0
#    E18 = -2404879675441
#    E19 = 0
#    E20 = 370371188237525
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the order of the Euler number.
#
#    Output, integer C, the value of the Euler number.
#
  import numpy as np

  n_max = 8

  c_vec = np.array ( (
    1, 0, -1, 5, -61, 1385, -50521, 2702765 ))

  n_vec = np.array ( (
     0, 1, 2, 4, 6, 8, 10, 12 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def euler_number_values_test ( ):

#*****************************************************************************80
#
## EULER_NUMBER_VALUES_TEST demonstrates the use of EULER_NUMBER_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'EULER_NUMBER_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EULER_NUMBER_VALUES returns values of ' )
  print ( '  the Euler numbers.' )
  print ( '' )
  print ( '     N         Euler_Number(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = euler_number_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %10d' % ( n, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EULER_NUMBER_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  euler_number_values_test ( )
  timestamp ( )
