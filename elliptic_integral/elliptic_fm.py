#! /usr/bin/env python3
#
def elliptic_fm ( m ):

#*****************************************************************************80
#
## ELLIPTIC_FA evaluates the complete elliptic integral F(M).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#      F(m) = RF ( 0, 1-m, 1 ).
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

  x = 0.0
  y = 1.0 - m
  z = 1.0
  errtol = 1.0E-03

  value, ierr = rf ( x, y, z, errtol )

  return value

def elliptic_fm_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_FM_TEST tests ELLIPTIC_FM.
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
  from elliptic_fm_values import elliptic_fm_values

  print ( '' )
  print ( 'ELLIPTIC_FM_TEST:' )
  print ( '  ELLIPTIC_FM returns values of' )
  print ( '  the complete elliptic integral of the' )
  print ( '  first kind, with parameter M.' )
  print ( '' )
  print ( '      M       F(M)          F(M)' )
  print ( '          Tabulated         Calculated' )
  print ( '' )

  n_data = 0

  while  ( True ):

    n_data, m, fx = elliptic_fm_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = elliptic_fm ( m )

    print ( '  %14.6f  %24.16g  %24.16g' % ( m, fx, fx2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_fm_test ( )
  timestamp ( )

