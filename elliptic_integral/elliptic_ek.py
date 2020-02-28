#! /usr/bin/env python3
#
def elliptic_ek ( k ):

#*****************************************************************************80
#
## ELLIPTIC_EK evaluates the complete elliptic integral E(K).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#  E(k) = RF ( 0, 1-k^2, 1 ) - 1/3 k^2 RD ( 0, 1-k^2, 1 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   02 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real K, the argument.
#
#    Output, real VALUE, the function value.
#
  from rd import rd
  from rf import rf

  x = 0.0
  y = ( 1.0 - k ) * ( 1.0 + k )
  z = 1.0
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )
  value2, ierr = rd ( x, y, z, errtol )
  value = value1 - k * k * value2 / 3.0

  return value

def elliptic_ek_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_EK_TEST tests ELLIPTIC_EK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 June 2018
#
#  Author:
#
#    John Burkardt
#
  from elliptic_ek_values import elliptic_ek_values

  print ( '' )
  print ( 'ELLIPTIC_EK_TEST:' )
  print ( '  ELLIPTIC_EK returns values of' )
  print ( '  the complete elliptic integral of the' )
  print ( '  second kind, with parameter K.' )
  print ( '' )
  print ( '      K       E(K)          E(K)' )
  print ( '          Tabulated         Calculated' )
  print ( '' )

  n_data = 0

  while  ( True ):

    n_data, k, fx = elliptic_ek_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = elliptic_ek ( k )

    print ( '  %14.6f  %24.16g  %24.16g' % ( k, fx, fx2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_ek_test ( )
  timestamp ( )

