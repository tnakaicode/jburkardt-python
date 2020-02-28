#! /usr/bin/env python3
#
def elliptic_fa ( a ):

#*****************************************************************************80
#
## ELLIPTIC_FA evaluates the complete elliptic integral F(A).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#      F(a) = RF ( 0, 1-sin^2(a), 1 ).
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
  from rf import rf

  import numpy as np

  k = np.sin ( a * np.pi / 180.0 )

  x = 0.0
  y = ( 1.0 - k ) * ( 1.0 + k )
  z = 1.0
  errtol = 1.0E-03

  value, ierr = rf ( x, y, z, errtol )

  return value

def elliptic_fa_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_FA_TEST tests ELLIPTIC_FA.
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
  from elliptic_fa_values import elliptic_fa_values

  print ( '' )
  print ( 'ELLIPTIC_FA_TEST:' )
  print ( '  ELLIPTIC_FA returns values of' )
  print ( '  the complete elliptic integral of the' )
  print ( '  first kind, with parameter angle A.' )
  print ( '' )
  print ( '      A       F(A)          F(A)' )
  print ( '          Tabulated         Calculated' )
  print ( '' )

  n_data = 0

  while  ( True ):

    n_data, a, fx = elliptic_fa_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = elliptic_fa ( a )

    print ( '  %14.6f  %24.16g  %24.16g' % ( a, fx, fx2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_fa_test ( )
  timestamp ( )

