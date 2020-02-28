#! /usr/bin/env python3
#
def elliptic_em ( m ):

#*****************************************************************************80
#
## ELLIPTIC_EM evaluates the complete elliptic integral E(M).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#  E(m) = RF ( 0, 1-m, 1 ) - 1/3 m RD ( 0, 1-m, 1 ).
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
#    Input, real M, the argument.
#
#    Output, real VALUE, the function value.
#
  from rd import rd
  from rf import rf

  x = 0.0
  y = 1.0 - m
  z = 1.0
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )
  value2, ierr = rd ( x, y, z, errtol )
  value = value1 - m * value2 / 3.0

  return value

def elliptic_em_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_EM_TEST tests ELLIPTIC_EM.
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
  from elliptic_em_values import elliptic_em_values

  print ( '' )
  print ( 'ELLIPTIC_EM_TEST:' )
  print ( '  ELLIPTIC_EM returns values of' )
  print ( '  the complete elliptic integral of the' )
  print ( '  second kind, with parameter M.' )
  print ( '' )
  print ( '      M       E(M)          E(M)' )
  print ( '          Tabulated         Calculated' )
  print ( '' )

  n_data = 0

  while  ( True ):

    n_data, m, fx = elliptic_em_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = elliptic_em ( m )

    print ( '  %14.6f  %24.16g  %24.16g' % ( m, fx, fx2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_em_test ( )
  timestamp ( )

