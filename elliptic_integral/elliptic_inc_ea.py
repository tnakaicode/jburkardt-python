#! /usr/bin/env python3
#
def elliptic_inc_ea ( phi, a ):

#*****************************************************************************80
#
## ELLIPTIC_INC_EA evaluates the incomplete elliptic integral E(PHI,A).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#      k = sin ( a * pi / 180 )
#      E(phi,a) = 
#                  sin ( phi )   RF ( cos^2 ( phi ), 1-k^2 sin^2 ( phi ), 1 ) 
#        - 1/3 k^2 sin^3 ( phi ) RD ( cos^2 ( phi ), 1-k^2 sin^2 ( phi ), 1 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real PHI, A, the argument.
#    0 <= PHI <= PI/2.
#    0 <= sin^2 ( A * pi / 180 ) * sin^2(PHI) <= 1.
#
#    Output, real VALUE, the function value.
#
  import numpy as np
  import sys
  from rd import rd
  from rf import rf

  k = np.sin ( a * np.pi / 180.0 )

  cp = np.cos ( phi )
  sp = np.sin ( phi )
  x = cp * cp
  y = ( 1.0 - k * sp ) * ( 1.0 + k * sp )
  z = 1.0
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_EA - Fatal error!' )
    print ( '  RF returned IERR = %d' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_EA - Fatal error!' )

  value2, ierr = rd ( x, y, z, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_EA - Fatal error!' )
    print ( '  RD returned IERR = %d\n' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_EA - Fatal error!' )

  value = sp * value1 - k ** 2 * sp ** 3 * value2 / 3.0

  return value

def elliptic_inc_ea_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_EA_TEST tests ELLIPTIC_INC_EA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from elliptic_inc_ea_values import elliptic_inc_ea_values

  print ( '' )
  print ( 'ELLIPTIC_INC_EA_TEST:' )
  print ( '  ELLIPTIC_INC_EA returns values of' )
  print ( '  the incomplete elliptic integral of the' )
  print ( '  second kind, with parameters PHI, A.' )
  print ( '  Compare with tabulated value.' )
  print ( '' )
  print ( '          Phi             A                Tabulated           elliptic_inc_ea(phi,a)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, a, ea1 = elliptic_inc_ea_values ( n_data )

    if ( n_data == 0 ):
      break

    ea2 = elliptic_inc_ea ( phi, a )

    print ( '  %12f  %12f  %24.16f  %24.16f' % ( phi, a, ea1, ea2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_ea_test ( )
  timestamp ( )

