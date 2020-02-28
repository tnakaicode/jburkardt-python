#! /usr/bin/env python3
#
def elliptic_inc_pik ( phi, n, k ):

#*****************************************************************************80
#
## ELLIPTIC_INC_PIK evaluates the incomplete elliptic integral Pi(PHI,N,K).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#      Pi(PHI,N,K) = integral ( 0 <= T <= PHI )
#        dT / (1 - N sin^2(T) ) sqrt ( 1 - k^2 * sin ( T )^2 )
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
#    Input, real PHI, N, K, the argument.
#    0 <= PHI <= PI/2
#         N   <= 1 / sin^2 ( PHI )
#    0 <= K^2 * sin^2(PHI) <= 1.
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
  y = ( 1.0 - k * sp ) * ( 1.0 + k * sp )
  z = 1.0
  p = 1.0 - n * sp ** 2
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_PIK - Fatal error!' )
    print ( '  RF returned IERR = %d' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_PIK - Fatal error!' )

  value2, ierr = rj ( x, y, z, p, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_PIK - Fatal error!' )
    print ( '  RJ returned IERR = %d\n' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_PIK - Fatal error!' )

  value = sp * value1 + n * sp ** 3 * value2 / 3.0

  return value

def elliptic_inc_pik_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_PIK_TEST tests ELLIPTIC_INC_PIK.
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
  from elliptic_inc_pik_values import elliptic_inc_pik_values

  print ( '' )
  print ( 'ELLIPTIC_INC_PIK_TEST:' )
  print ( '  ELLIPTIC_INC_PIK returns values of' )
  print ( '  the incomplete elliptic integral of the' )
  print ( '  third kind, with parameters PHI, N, K.' )
  print ( '  Compare with tabulated value.' )
  print ( '' )
  print ( '          Phi             N             K                Tabulated           elliptic_inc_pik(phi,n,k)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, n, k, pik1 = elliptic_inc_pik_values ( n_data )

    if ( n_data == 0 ):
      break

    pik2 = elliptic_inc_pik ( phi, n, k )

    print ( '  %12f  %12f  %12f  %24.16f  %24.16f' % ( phi, n, k, pik1, pik2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_pik_test ( )
  timestamp ( )
