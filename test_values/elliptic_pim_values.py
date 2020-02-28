#! /usr/bin/env python
#
def elliptic_pim_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_PIM_VALUES returns values of the complete elliptic integral Pi(M).
#
#  Discussion:
#
#    This is one form of what is sometimes called the complete elliptic
#    integral of the third kind.
#
#    The function is defined by the formula:
#
#      Pi(N,M) = integral ( 0 <= T <= PI/2 )
#        dT / (1 - N sin^2(T) ) sqrt ( 1 - M * sin ( T )^2 )
#
#    In MATLAB, the function can be evaluated by:
#
#      ellipticPi(n,m)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 May 2018
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
#    Output, real N, M, the arguments of the function.
#
#    Output, real PIM, the value of the function.
#
  import numpy as np

  n_max = 20

  m_vec = np.array ( ( \
    0.25, \
    0.50, \
    0.75, \
    0.95, \
    0.25, \
    0.50, \
    0.75, \
    0.95, \
    0.25, \
    0.50, \
    0.75, \
    0.95, \
    0.25, \
    0.50, \
    0.75, \
    0.95, \
    0.25, \
    0.50, \
    0.75, \
    0.95 ))

  n_vec = np.array ( ( \
    -10.0, \
    -10.0, \
    -10.0, \
    -10.0, \
     -3.0, \
     -3.0, \
     -3.0, \
     -3.0, \
     -1.0, \
     -1.0, \
     -1.0, \
     -1.0, \
      0.0, \
      0.0, \
      0.0, \
      0.0, \
      0.5, \
      0.5, \
      0.5, \
      0.5 ) )

  pim_vec = np.array ( ( \
    0.4892245275965397, \
    0.5106765677902629, \
    0.5460409271920561, \
    0.6237325893535237, \
    0.823045542660675,  \
    0.8760028274011437, \
    0.9660073560143946, \
    1.171952391481798, \
    1.177446843000566, \
    1.273127366749682, \
    1.440034318657551, \
    1.836472172302591, \
    1.685750354812596, \
    1.854074677301372, \
    2.156515647499643, \
    2.908337248444552, \
    2.413671504201195, \
    2.701287762095351, \
    3.234773471249465, \
    4.633308147279891 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    m = 0.0
    n = 0.0
    pim = 0.0
  else:
    m = m_vec[n_data]
    n = n_vec[n_data]
    pim = pim_vec[n_data]
    n_data = n_data + 1

  return n_data, n, m, pim

def elliptic_pim_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_PIM_VALUES_TEST demonstrates the use of ELLIPTIC_PIM_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 May 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ELLIPTIC_PIM_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPTIC_PIM_VALUES stores values of the complete elliptic' )
  print ( '  integral of the third kind, with parameter M.' )
  print ( '' )
  print ( '      N             M             Pi(N,M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, pim = elliptic_pim_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16f' % ( n, m, pim ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPTIC_PIM_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_pim_values_test ( )
  timestamp ( )

