#! /usr/bin/env python3
#
def elliptic_inc_pim ( phi, n, m ):

#*****************************************************************************80
#
## ELLIPTIC_INC_PIM evaluates the incomplete elliptic integral Pi(PHI,N,M).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#      Pi(PHI,N,M) = integral ( 0 <= T <= PHI )
#        dT / (1 - N sin^2(T) ) sqrt ( 1 - m * sin ( T )^2 )
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
#    Input, real PHI, N, M, the argument.
#    0 <= PHI <= PI/2
#         N   <= 1 / sin^2 ( PHI )
#    0 <= M * sin^2(PHI) <= 1.
#
#    Output, real VALUE, the function value.
#
  import numpy as np
  import sys
  from rf import rf
  from rj import rj

  cp = np.cos ( phi )
  sp = np.sin ( phi )
  x = cp * cp
  y = 1.0 - m * sp ** 2
  z = 1.0
  p = 1.0 - n * sp ** 2
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_PIM - Fatal error!' )
    print ( '  RF returned IERR = %d' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_PIM - Fatal error!' )

  value2, ierr = rj ( x, y, z, p, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_PIM - Fatal error!' )
    print ( '  RJ returned IERR = %d\n' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_PIM - Fatal error!' )

  value = sp * value1 + n * sp ** 3 * value2 / 3.0

  return value

def elliptic_inc_pim_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_PIM_TEST tests ELLIPTIC_INC_PIM.
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
  from elliptic_inc_pim_values import elliptic_inc_pim_values

  print ( '' )
  print ( 'ELLIPTIC_INC_PIM_TEST:' )
  print ( '  ELLIPTIC_INC_PIM returns values of' )
  print ( '  the incomplete elliptic integral of the' )
  print ( '  third kind, with parameters PHI, N, M.' )
  print ( '  Compare with tabulated value.' )
  print ( '' )
  print ( '          Phi             N             M                Tabulated           elliptic_inc_pim(phi,n,m)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, n, m, pim1 = elliptic_inc_pim_values ( n_data )

    if ( n_data == 0 ):
      break

    pim2 = elliptic_inc_pim ( phi, n, m )

    print ( '  %12f  %12f  %12f  %24.16f  %24.16f' % ( phi, n, m, pim1, pim2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_pim_test ( )
  timestamp ( )
