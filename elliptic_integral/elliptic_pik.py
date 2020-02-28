#! /usr/bin/env python3
#
def elliptic_pik ( n, k ):

#*****************************************************************************80
#
## ELLIPTIC_PIK evaluates the complete elliptic integral Pi(N,K).
#
#  Discussion:
#
#    This is one form of what is sometimes called the complete elliptic
#    integral of the third kind.
#
#    The function is defined by the formula:
#
#      Pi(N,K) = integral ( 0 <= T <= PI/2 )
#        dT / (1 - N sin^2(T) ) sqrt ( 1 - k^2 * sin ( T )^2 )
#
#    In MATLAB, the function can be evaluated by:
#
#      ellipticPi(n,k^2)
#
#    The value is computed using Carlson elliptic integrals:
#
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
#    Input, real N, K, the arguments.
#
#    Output, real VALUE, the function value.
#
  from rf import rf
  from rj import rj

  x = 0.0
  y = ( 1.0 - k ) * ( 1.0 + k )
  z = 1.0
  p = 1.0 - n
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )
  value2, ierr = rj ( x, y, z, p, errtol )

  value = value1 + n * value2 / 3.0

  return value

def elliptic_pik_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_PIK_TEST tests ELLIPTIC_PIK.
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
  from elliptic_pik_values import elliptic_pik_values

  print ( '' )
  print ( 'ELLIPTIC_PIK_TEST:' )
  print ( '  ELLIPTIC_PIK returns values of' )
  print ( '  the complete elliptic integral of the' )
  print ( '  third kind, with parameter K.' )
  print ( '' )
  print ( '      N            K       Pi(N,K)           Pi(N,K)' )
  print ( '                           Tabulated         Calculated' )
  print ( '' )

  n_data = 0

  while  ( True ):

    n_data, n, k, pik = elliptic_pik_values ( n_data )

    if ( n_data == 0 ):
      break

    pik2 = elliptic_pik ( n, k )

    print ( '  %14.6f  %14.6f  %24.16g  %24.16g' % ( n, k, pik, pik2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_pik_test ( )
  timestamp ( )

