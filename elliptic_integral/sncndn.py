#! /usr/bin/env python
#
def sncndn ( u, m ):

#*****************************************************************************80
#
## SNCNDN evaluates Jacobi elliptic functions.
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
#    Output, real SN, CN, DN, the value of the Jacobi
#    elliptic functions sn(u,m), cn(u,m), and dn(u,m).
#
  import numpy as np

  m_comp = 1.0 - m
  u_copy = u

  if ( m_comp == 0.0 ):
    cn = 1.0 / np.cosh ( u_copy )
    dn = cn
    sn = np.tanh ( u_copy )
    return sn, cn, dn

  if ( 1.0 < m ):
    d = 1.0 - m_comp
    m_comp = - m_comp / d
    d = np.sqrt ( d )
    u_copy = d * u_copy

  eps = np.finfo(float).eps

  ca = np.sqrt ( eps )

  a = 1.0
  dn = 1.0
  l = 24

  m_array = np.zeros ( 25 )
  n_array = np.zeros ( 25 )

  for i in range ( 0, 25 ):

    m_array[i] = a
    m_comp = np.sqrt ( m_comp )
    n_array[i] = m_comp
    c = 0.5 * ( a + m_comp )

    if ( abs ( a - m_comp ) <= ca * a ):
      l = i
      break

    m_comp = a * m_comp
    a = c

  u_copy = c * u_copy
  sn = np.sin ( u_copy )
  cn = np.cos ( u_copy )

  if ( sn != 0.0 ):

    a = cn / sn
    c = a * c

    for i in range ( l, -1, -1 ):
      b = m_array[i]
      a = c * a
      c = dn * c
      dn = ( n_array[i] + a ) / ( b + a )
      a = c / b

    a = 1.0 / np.sqrt ( c * c + 1.0 )

    if ( sn < 0.0 ):
      sn = - a
    else:
      sn = a

    cn = c * sn

  if ( 1.0 < m ):
    a = dn
    dn = cn
    cn = a
    sn = sn / d

  return sn, cn, dn

def sncndn_test ( ):

#*****************************************************************************80
#
## SNCNDN_TEST tests SNCNDN.
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
  from jacobi_cn import jacobi_cn
  from jacobi_cn_values import jacobi_cn_values
  from jacobi_dn import jacobi_dn
  from jacobi_dn_values import jacobi_dn_values
  from jacobi_sn import jacobi_sn
  from jacobi_sn_values import jacobi_sn_values

  print ( '' )
  print ( 'SNDNCN_TEST:' )
  print ( '  SNCNDN evaluates the Jacobi elliptic functions SN, DN, CN.' )
  print ( '' )
  print ( '    U       M       SN(U,M)                CN(U,M)                DN(U,M)' )

  n_datas = 0
  n_datac = 0
  n_datad = 0

  while ( True ):

    n_datas, u, m, sn1 = jacobi_sn_values ( n_datas )
    n_datac, u, m, cn1 = jacobi_cn_values ( n_datac )
    n_datad, u, m, dn1 = jacobi_dn_values ( n_datad )

    if ( n_datas == 0 ):
      break

    print ( '' )
    print ( 'Tab:  %8.4f%8.4f%24.16f%24.16f%24.16f' % ( u, m, sn1, cn1, dn1 ) )

    sn2 = jacobi_sn ( u, m )
    cn2 = jacobi_cn ( u, m )
    dn2 = jacobi_dn ( u, m )

    print ( 'Calc: %8.4f%8.4f%24.16f%24.16f%24.16f' % ( u, m, sn2, cn2, dn2 ) )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp 
  timestamp ( )
  sncndn_test ( )
  timestamp ( )

