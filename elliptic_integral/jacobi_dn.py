#! /usr/bin/env python
#
def jacobi_dn ( u, m ):

#*****************************************************************************80
#
## JACOBI_DN evaluates the Jacobi elliptic function DN(U,M).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 June 2018
#
#  Author:
#
#    Original ALGOL version by Roland Bulirsch.
#    Python version by John Burkardt
#
#  Reference:
#
#    Roland Bulirsch,
#    Numerical calculation of elliptic integrals and elliptic functions,
#    Numerische Mathematik,
#    Volume 7, Number 1, 1965, pages 78-90.
#
#  Parameters:
#
#    Input, real U, M, the arguments.
#
#    Output, real DN, the function value.
#
  from sncndn import sncndn

  sn, cn, dn = sncndn ( u, m )

  return dn

def jacobi_dn_test ( ):

#*****************************************************************************80
#
## JACOBI_DN_TEST tests JACOBI_DN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 June 2018
#
#  Author:
#
#    John Burkardt
#
  from jacobi_dn_values import jacobi_dn_values

  print ( '' )
  print ( 'JACOBI_DN_TEST:' )
  print ( '  JACOBI_DN evaluates the Jacobi elliptic function DN.' )
  print ( '' )
  print ( '    U       M       Exact DN                DN(U,M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, u, m, dn1 = jacobi_dn_values ( n_data )

    if ( n_data == 0 ):
      break

    dn2 = jacobi_dn ( u, m )

    print ( '%8.4f%8.4f%24.16g%24.16g' % ( u, m, dn1, dn2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp 
  timestamp ( )
  jacobi_dn_test ( )
  timestamp ( )

