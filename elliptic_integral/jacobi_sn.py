#! /usr/bin/env python
#
def jacobi_sn ( u, m ):

#*****************************************************************************80
#
## JACOBI_SN evaluates the Jacobi elliptic function SN(U,M).
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
#    Output, real SN, the function value.
#
  from sncndn import sncndn

  sn, cn, dn = sncndn ( u, m )

  return sn

def jacobi_sn_test ( ):

#*****************************************************************************80
#
## JACOBI_SN_TEST tests JACOBI_SN.
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
  from jacobi_sn_values import jacobi_sn_values

  print ( '' )
  print ( 'JACOBI_SN_TEST:' )
  print ( '  JACOBI_SN evaluates the Jacobi elliptic function SN.' )
  print ( '' )
  print ( '    U       M       Exact SN                SN(U,M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, u, m, sn1 = jacobi_sn_values ( n_data )

    if ( n_data == 0 ):
      break

    sn2 = jacobi_sn ( u, m )

    print ( '%8.4f%8.4f%24.16g%24.16g' % ( u, m, sn1, sn2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp 
  timestamp ( )
  jacobi_sn_test ( )
  timestamp ( )

