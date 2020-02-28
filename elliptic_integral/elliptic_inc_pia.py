#! /usr/bin/env python3
#
def elliptic_inc_pia ( phi, n, a ):

#*****************************************************************************80
#
## ELLIPTIC_INC_PIA evaluates the incomplete elliptic integral Pi(PHI,N,A).
#
#  Discussion:
#
#    The value is computed using Carlson elliptic integrals:
#
#      Pi(PHI,N,A) = integral ( 0 <= T <= PHI )
#        dT / (1 - N sin^2(T) ) sqrt ( 1 - sin^2(A*pi/180) * sin ( T )^2 )
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
#    Input, real PHI, N, A, the argument.
#    0 <= PHI <= PI/2
#         N   <= 1 / sin^2 ( PHI )
#    0 <= sin^2 ( A * pi / 180 ) * sin^2(PHI) <= 1.
#
#    Output, real VALUE, the function value.
#
  import numpy as np
  import sys
  from rf import rf
  from rj import rj

  k = np.sin ( a * np.pi / 180.0 )

  cp = np.cos ( phi )
  sp = np.sin ( phi )
  x = cp * cp
  y = ( 1.0 - k * sp ) * ( 1.0 + k * sp )
  z = 1.0
  p = 1.0 - n * sp ** 2
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_PIA - Fatal error!' )
    print ( '  RF returned IERR = %d' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_PIA - Fatal error!' )

  value2, ierr = rj ( x, y, z, p, errtol )

  if ( ierr != 0 ):
    print ( 'ELLIPTIC_INC_PIA - Fatal error!' )
    print ( '  RJ returned IERR = %d\n' % ( ierr ) )
    sys.exit ( 'ELLIPTIC_INC_PIA - Fatal error!' )

  value = sp * value1 + n * sp ** 3 * value2 / 3.0

  return value

def elliptic_inc_pia_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_INC_PIA_TEST tests ELLIPTIC_INC_PIA.
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
  from elliptic_inc_pia_values import elliptic_inc_pia_values

  print ( '' )
  print ( 'ELLIPTIC_INC_PIA_TEST:' )
  print ( '  ELLIPTIC_INC_PIA returns values of' )
  print ( '  the incomplete elliptic integral of the' )
  print ( '  third kind, with parameters PHI, N, A.' )
  print ( '  Compare with tabulated value.' )
  print ( '' )
  print ( '          Phi             N             A                Tabulated           elliptic_inc_pia(phi,n,a)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, phi, n, a, pia1 = elliptic_inc_pia_values ( n_data )

    if ( n_data == 0 ):
      break

    pia2 = elliptic_inc_pia ( phi, n, a )

    print ( '  %12f  %12f  %12f  %24.16f  %24.16f' % ( phi, n, a, pia1, pia2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_inc_pia_test ( )
  timestamp ( )
