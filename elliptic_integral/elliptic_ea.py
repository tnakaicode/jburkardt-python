#! /usr/bin/env python3
#
def elliptic_ea ( a ):

#*****************************************************************************80
#
## ELLIPTIC_EA evaluates the complete elliptic integral E(A).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#  E(a) = RF ( 0, 1-sin^2(a), 1 ) - 1/3 sin^2(a) RD ( 0, 1-sin^2(a), 1 ).
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
#  Parameters:
#
#    Input, real A, the argument.
#
#    Output, real VALUE, the function value.
#
  from rd import rd
  from rf import rf

  import numpy as np

  k = np.sin ( a * np.pi / 180.0 )

  x = 0.0
  y = ( 1.0 - k ) * ( 1.0 + k )
  z = 1.0
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )
  value2, ierr = rd ( x, y, z, errtol )
  value = value1 - k * k * value2 / 3.0

  return value

def elliptic_ea_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_EA_TEST tests ELLIPTIC_EA.
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
  from elliptic_ea_values import elliptic_ea_values

  print ( '' )
  print ( 'ELLIPTIC_EA_TEST:' )
  print ( '  ELLIPTIC_EA returns values of' )
  print ( '  the complete elliptic integral of the' )
  print ( '  second kind, with parameter angle A.' )
  print ( '' )
  print ( '      A       E(A)          E(A)' )
  print ( '          Tabulated         Calculated' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, fx = elliptic_ea_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = elliptic_ea ( a )

    print ( '  %14.6f  %24.16g  %24.16g' % ( a, fx, fx2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_ea_test ( )
  timestamp ( )

