#! /usr/bin/env python
#
def ker1_values ( n_data ):

#*****************************************************************************80
#
## KER1_VALUES returns some values of the Kelvin KER function of order NU = 1.
#
#  Discussion:
#
#    The function is defined by:
#
#      KER(NU,X) + i * KEI(NU,X) = exp(-nu*Pi*I/2) * K(NU,X*exp(PI*I/4))
#
#    where K(NU,X) is the K Bessel function.
#
#    In Mathematica, KER(NU,X) can be defined by:
#
#      Re [ Exp [ -NU * Pi * I / 2 ] * BesselK [ NU, X * Exp[ Pi * I / 4 ] ] ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
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
#    LC: QA47.A34,
#    ISBN: 0-486-61272-4.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    LC: QA76.95.W65,
#    ISBN: 0-521-64314-7.
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

  n_max = 10

  f_vec = np.array (( \
   -1.522403406532090, \
   -0.7403222768419827, \
   -0.4170442851662574, \
   -0.2308059295181230, \
   -0.1172561358598705, \
   -0.04989830778751491, \
   -0.01272324936181659, \
    0.005351296460277448, \
    0.01209090413515866, \
    0.01273739048421857 ))

  x_vec = np.array ( ( \
    0.5, \
    1.0, \
    1.5, \
    2.0, \
    2.5, \
    3.0, \
    3.5, \
    4.0, \
    4.5, \
    5.0  ) )

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

def ker1_values_test ( ):

#*****************************************************************************80
#
## KER1_VALUES_TEST demonstrates the use of KER1_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'KER1_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KER1_VALUES stores values of the Kelvin KER function of order 1.' )
  print ( '' )
  print ( '      X         KER(1,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = ker1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'KER1_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ker1_values_test ( )
  timestamp ( )
