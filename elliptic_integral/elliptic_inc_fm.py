#! /usr/bin/env python3
#
def elliptic_inc_fm ( phi, m ):

#*****************************************************************************80
#
## ELLIPTIC_INC_FM evaluates the incomplete elliptic integral F(PHI,M).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#      F(phi,m) = sin(phi) * RF ( cos^2 ( phi ), 1-m sin^2 ( phi ), 1 ).
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
#    Input, real PHI, M, the argument.
#    0 <= PHI <= PI/2.
#    0 <= M * sin^2(PHI) <= 1.
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

  value, ierr = rf ( x, y, z, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_FM - Fatal error!' )
    print ( '  RF returned IERR = %d' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_FM - Fatal error!' )

  value = sp * value

  return value

def elliptic_inc_fm_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_FM_TEST tests ELLIPTIC_INC_FM.
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
  from elliptic_inc_fm_values import elliptic_inc_fm_values

  print ( '' )
  print ( 'ELLIPTIC_INC_FM_TEST:' )
  print ( '  ELLIPTIC_INC_FM returns values of' )
  print ( '  the incomplete elliptic integral of the' )
  print ( '  first kind, with parameters PHI, M.' )
  print ( '  Compare with tabulated value.' )
  print ( '' )
  print ( '          Phi             M                Tabulated           elliptic_inc_fm(phi,m)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, m, fm1 = elliptic_inc_fm_values ( n_data )

    if ( n_data == 0 ):
      break

    fm2 = elliptic_inc_fm ( phi, m )

    print ( '  %12f  %12f  %24.16f  %24.16f' % ( phi, m, fm1, fm2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_fm_test ( )
  timestamp ( )
