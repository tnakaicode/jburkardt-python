#! /usr/bin/env python3
#
def elliptic_inc_fk ( phi, k ):

#*****************************************************************************80
#
## ELLIPTIC_INC_FK evaluates the incomplete elliptic integral F(PHI,K).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#      F(phi,k) = sin(phi) * RF ( cos^2 ( phi ), 1-k^2 sin^2 ( phi ), 1 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real PHI, K, the argument.
#    0 <= PHI <= PI/2.
#    0 <= K^2 * sin^2(PHI) <= 1.
#
#    Output, real VALUE, the function value.
#
  import numpy as np
  import sys
  from rd import rd
  from rf import rf

  cp = np.cos ( phi )
  sp = np.sin ( phi )
  x = cp * cp
  y = ( 1.0 - k * sp ) * ( 1.0 + k * sp )
  z = 1.0
  errtol = 1.0E-03

  value, ierr = rf ( x, y, z, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_FK - Fatal error!' )
    print ( '  RF returned IERR = %d' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_FK - Fatal error!' )

  value = sp * value

  return value

def elliptic_inc_fk_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_FK_TEST tests ELLIPTIC_INC_FK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 June 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from elliptic_inc_fk_values import elliptic_inc_fk_values

  print ( '' )
  print ( 'ELLIPTIC_INC_FK_TEST:' )
  print ( '  ELLIPTIC_INC_FK returns values of' )
  print ( '  the incomplete elliptic integral of the' )
  print ( '  first kind, with parameters PHI, K.' )
  print ( '  Compare with tabulated value.' )
  print ( '' )
  print ( '          Phi             K                Tabulated           elliptic_inc_fk(phi,k)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, k, fk1 = elliptic_inc_fk_values ( n_data )

    if ( n_data == 0 ):
      break

    fk2 = elliptic_inc_fk ( phi, k )

    print ( '  %12f  %12f  %24.16f  %24.16f' % ( phi, k, fk1, fk2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_fk_test ( )
  timestamp ( )
