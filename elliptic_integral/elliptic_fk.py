#! /usr/bin/env python3
#
def elliptic_fk ( k ):

#*****************************************************************************80
#
## ELLIPTIC_FK evaluates the complete elliptic integral F(K).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#      F(k) = RF ( 0, 1-k^2, 1 ).
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
#    Input, real K, the argument.
#
#    Output, real VALUE, the function value.
#
  from rf import rf

  x = 0.0
  y = ( 1.0 - k ) * ( 1.0 + k )
  z = 1.0
  errtol = 1.0E-03

  value, ierr = rf ( x, y, z, errtol )

  return value

def elliptic_fk_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_FK_TEST tests ELLIPTIC_FK.
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
  from elliptic_fk_values import elliptic_fk_values

  print ( '' )
  print ( 'ELLIPTIC_FK_TEST:' )
  print ( '  ELLIPTIC_FK returns values of' )
  print ( '  the complete elliptic integral of the' )
  print ( '  first kind, with parameter K.' )
  print ( '' )
  print ( '      K       F(K)          F(K)' )
  print ( '          Tabulated         Calculated' )
  print ( '' )

  n_data = 0

  while  ( True ):

    n_data, k, fx = elliptic_fk_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = elliptic_fk ( k )

    print ( '  %14.6f  %24.16g  %24.16g' % ( k, fx, fx2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_fk_test ( )
  timestamp ( )

