#! /usr/bin/env python3
#
def elliptic_inc_em ( phi, m ):

#*****************************************************************************80
#
## ELLIPTIC_INC_EM evaluates the incomplete elliptic integral E(PHI,M).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#      E(phi,m) = 
#                sin ( phi )   RF ( cos^2 ( phi ), 1-m sin^2 ( phi ), 1 ) 
#        - 1/3 m sin^3 ( phi ) RD ( cos^2 ( phi ), 1-m sin^2 ( phi ), 1 ).
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
#    0 <= M sin^2(PHI) <= 1.
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
  y = 1.0 - m * sp ** 2
  z = 1.0
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_EM - Fatal error!' )
    print ( '  RF returned IERR = %d' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_EM - Fatal error!' )

  value2, ierr = rd ( x, y, z, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_EM - Fatal error!' )
    print ( '  RD returned IERR = %d' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_EM - Fatal error!' )

  value = sp * value1 - m * sp ** 3 * value2 / 3.0

  return value

def elliptic_inc_em_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_EM_TEST tests ELLIPTIC_INC_EM.
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
  from elliptic_inc_em_values import elliptic_inc_em_values

  print ( '' )
  print ( 'ELLIPTIC_INC_EM_TEST:' )
  print ( '  ELLIPTIC_INC_EM returns values of' )
  print ( '  the incomplete elliptic integral of the' )
  print ( '  second kind, with parameters PHI, M.' )
  print ( '  Compare with tabulated value.' )
  print ( '' )
  print ( '          Phi             M                Tabulated           elliptic_inc_em(phi,m)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, m, em1 = elliptic_inc_em_values ( n_data )

    if ( n_data == 0 ):
      break

    em2 = elliptic_inc_em ( phi, m )

    print ( '  %12f  %12f  %24.16f  %24.16f' % ( phi, m, em1, em2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp 
  timestamp ( )
  elliptic_inc_em_test ( )
  timestamp ( )
