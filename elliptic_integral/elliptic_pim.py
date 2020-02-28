#! /usr/bin/env python3
#
def elliptic_pim ( n, m ):

#*****************************************************************************80
#
## ELLIPTIC_PIM evaluates the complete elliptic integral Pi(N,M).
#
#  Discussion:
#
#    This is one form of what is sometimes called the complete elliptic
#    integral of the third kind.
#
#    The function is defined by the formula:
#
#      Pi(N,M) = integral ( 0 <= T <= PI/2 )
#        dT / (1 - N sin^2(T) ) sqrt ( 1 - m * sin ( T )^2 )
#
#    In MATLAB, the function can be evaluated by:
#
#      ellipticPi(n,m)
#
#    The value is computed using Carlson elliptic integrals:
#
#      Pi(n,k) = RF ( 0, 1 - m, 1 ) + 1/3 n RJ ( 0, 1 - m, 1, 1 - n )
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
#    Input, real N, M, the arguments.
#
#    Output, real VALUE, the function value.
#
  from rf import rf
  from rj import rj

  x = 0.0
  y = 1.0 - m
  z = 1.0
  p = 1.0 - n
  errtol = 1.0E-03

  value1, ierr = rf ( x, y, z, errtol )
  value2, ierr = rj ( x, y, z, p, errtol )

  value = value1 + n * value2 / 3.0

  return value

def elliptic_pim_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_PIM_TEST tests ELLIPTIC_PIM.
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
  from elliptic_pim_values import elliptic_pim_values

  print ( '' )
  print ( 'ELLIPTIC_PIM_TEST:' )
  print ( '  ELLIPTIC_PIM returns values of' )
  print ( '  the complete elliptic integral of the' )
  print ( '  third kind, with parameter M.' )
  print ( '' )
  print ( '      N            M       Pi(N,M)           Pi(N,M)' )
  print ( '                           Tabulated         Calculated' )
  print ( '' )

  n_data = 0

  while  ( True ):

    n_data, n, m, pim = elliptic_pim_values ( n_data )

    if ( n_data == 0 ):
      break

    pim2 = elliptic_pim ( n, m )

    print ( '  %14.6f  %14.6f  %24.16g  %24.16g' % ( n, m, pim, pim2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_pim_test ( )
  timestamp ( )

