#! /usr/bin/env python
#
def six_j_values ( n_data ):

#*****************************************************************************80
#
## SIX_J_VALUES returns some values of the Wigner 6J function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      SixJSymbol[{j1,j2,j3},{j4,j5,j6}]
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
#    Input, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each subsequent call, the input value should be
#    the output value from the previous call.
#
#    Output, integer N_DATA.  The routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real J1, J2, J3, J4, J5, J6, the arguments 
#    of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 15

  f_vec = np.array ( ( \
     0.03490905138373300,  \
    -0.03743025039659792,  \
     0.01890866390959560,  \
     0.007342448254928643, \
    -0.02358935185081794,  \
     0.01913476955215437,  \
     0.001288017397724172, \
    -0.01930018366290527,  \
     0.01677305949382889,  \
     0.005501147274850949, \
    -0.02135439790896831,  \
     0.003460364451435387, \
     0.02520950054795585,  \
     0.01483990561221713,  \
     0.002708577680633186 ))
  j1_vec = np.array ( ( \
    1.0, \
    2.0, \
    3.0, \
    4.0, \
    5.0, \
    6.0, \
    7.0, \
    8.0, \
    9.0, \
   10.0, \
   11.0, \
   12.0, \
   13.0, \
   14.0, \
   15.0 ))
  j2_vec = np.array ( ( \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0, \
    8.0 ))
  j3_vec = np.array ( ( \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0, \
    7.0 ))
  j4_vec = np.array ( ( \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5, \
    6.5 ))
  j5_vec = np.array ( ( \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5 ))
  j6_vec = np.array ( ( \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5, \
    7.5 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    j1 = 0.0
    j2 = 0.0
    j3 = 0.0
    j4 = 0.0
    j5 = 0.0
    j6 = 0.0
    f = 0.0
  else:
    j1 = j1_vec[n_data]
    j2 = j2_vec[n_data]
    j3 = j3_vec[n_data]
    j4 = j4_vec[n_data]
    j5 = j5_vec[n_data]
    j6 = j6_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, j1, j2, j3, j4, j5, j6, f

def six_j_values_test ( ):

#*****************************************************************************80
#
## SIX_J_VALUES_TEST demonstrates the use of SIX_J_VALUES.
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
  print ( 'SIX_J_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIX_J_VALUES stores values of the SIX_J function.' )
  print ( '' )
  print ( '    J1    J2    J3    J4    J5    J6    SIX_J(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, j1, j2, j3, j4, j5, j6, f = six_j_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4.1f  %4.1f  %4.1f  %4.1f  %4.1f  %4.1f  %24.16f' \
      % ( j1, j2, j3, j4, j5, j6, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIX_J_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  six_j_values_test ( )
  timestamp ( )

