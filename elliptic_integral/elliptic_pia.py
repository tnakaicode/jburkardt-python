#! /usr/bin/env python3
#
def elliptic_pia ( n, a ):

#*****************************************************************************80
#
## ELLIPTIC_PIA evaluates the complete elliptic integral Pi(N,A).
#
#  Discussion:
#
#    This is one form of what is sometimes called the complete elliptic
#    integral of the third kind.
#
#    The function is defined by the formula:
#
#      Pi(N,A) = integral ( 0 <= T <= PI/2 )
#        dT / (1 - N sin^2(T) ) sqrt ( 1 - sin^2(A) * sin ( T )^2 )
#
#    In MATLAB, the function can be evaluated by:
#
#      ellipticPi(n,(sin(a*pi/180)^2)
#
#    The value is computed using Carlson elliptic integrals:
#
#      k = sin ( a * pi / 180 )
#      Pi(n,k) = RF ( 0, 1 - k^2, 1 ) + 1/3 n RJ ( 0, 1 - k^2, 1, 1 - n )
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
#    Input, real N, A, the arguments.
#
#    Output, real VALUE, the function value.
#
  from rf import rf
  from rj import rj

  import numpy as np

  k = np.sin ( a * np.pi / 180.0 )

  x = 0.0
  y = ( 1.0 - k ) * ( 1.0 + k )
  z = 1.0
  p = 1.0 - n
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )
  value2, ierr = rj ( x, y, z, p, errtol )

  value = value1 + n * value2 / 3.0

  return value

def elliptic_pia_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_PIA_TEST tests ELLIPTIC_PIA.
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
  from elliptic_pia_values import elliptic_pia_values

  print ( '' )
  print ( 'ELLIPTIC_PIA_TEST:' )
  print ( '  ELLIPTIC_PIA returns values of' )
  print ( '  the complete elliptic integral of the' )
  print ( '  third kind, with parameter angle A.' )
  print ( '' )
  print ( '      N            A       Pi(N,A)           Pi(N,A)' )
  print ( '                           Tabulated         Calculated' )
  print ( '' )

  n_data = 0

  while  ( True ):

    n_data, n, a, pia = elliptic_pia_values ( n_data )

    if ( n_data == 0 ):
      break

    pia2 = elliptic_pia ( n, a )

    print ( '  %14.6f  %14.6f  %24.16g  %24.16g' % ( n, a, pia, pia2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_pia_test ( )
  timestamp ( )

