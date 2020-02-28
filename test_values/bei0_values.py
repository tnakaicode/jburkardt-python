#! /usr/bin/env python
#
def bei0_values ( n_data ):

#*****************************************************************************80
#
## BEI0_VALUES returns some values of the Kelvin BEI function of order NU = 0.
#
#  Discussion:
#
#    The function is defined by:
#
#      BER(NU,X) + i * BEI(NU,X) = exp(NU*Pi*I) * J(NU,X*exp(-PI*I/4))
#
#    where J(NU,X) is the J Bessel function.
#
#    In Mathematica, BEI(NU,X) can be defined by:
#
#      Im [ Exp [ NU * Pi * I ] * BesselJ [ NU, X * Exp[ -Pi * I / 4 ] ] ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2006
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
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 11

  fx_vec = np.array ( ( \
    0.0000000000000000, \
    0.06249321838219946, \
    0.2495660400366597, \
    0.5575600623030867, \
    0.9722916273066612, \
    1.457182044159804, \
   1.937586785266043, \
   2.283249966853915, \
   2.292690322699300, \
   1.686017203632139, \
   0.1160343815502004 ) )

  x_vec = np.array ( ( \
    0.0, \
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
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def bei0_values_test ( ):

#*****************************************************************************80
#
## BEI0_VALUES_TEST demonstrates the use of BEI0_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BEI0_VALUES_TEST:' )
  print ( '  BEI0_VALUES stores values of the Kelvin BEI function. of order 0.' )
  print ( '' )
  print ( '      X         BEI(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bei0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BEI0_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bei0_values_test ( )
  timestamp ( )

