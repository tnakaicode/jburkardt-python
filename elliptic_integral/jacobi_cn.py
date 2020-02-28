#! /usr/bin/env python
#
def jacobi_cn ( u, m ):

#*****************************************************************************80
#
## JACOBI_CN evaluates the Jacobi elliptic function CN(U,M).
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
#    Output, real CN, the function value.
#
  from sncndn import sncndn

  sn, cn, dn = sncndn ( u, m )

  return cn

def jacobi_cn_test ( ):

#*****************************************************************************80
#
## JACOBI_CN_TEST tests JACOBI_CN.
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
  from jacobi_cn_values import jacobi_cn_values

  print ( '' )
  print ( 'JACOBI_CN_TEST:' )
  print ( '  JACOBI_CN evaluates the Jacobi elliptic function CN.' )
  print ( '' )
  print ( '    U       M       Exact CN                CN(U,M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, u, m, cn1 = jacobi_cn_values ( n_data )

    if ( n_data == 0 ):
      break

    cn2 = jacobi_cn ( u, m )

    print ( '%8.4f%8.4f%24.16g%24.16g' % ( u, m, cn1, cn2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp 
  timestamp ( )
  jacobi_cn_test ( )
  timestamp ( )

