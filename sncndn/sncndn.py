#! /usr/bin/env python3
#
def sncndn_test ( ):

#*****************************************************************************80
#
## sncndn_test() tests sncndn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'sncndn_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test sncndn().' )

  jacobi_cn_test ( )
  jacobi_dn_test ( )
  jacobi_sn_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sncndn_test():' )
  print ( '  Normal end of execution.' )

  return

def jacobi_cn ( u, m ):

#*****************************************************************************80
#
## jacobi_cn() evaluates the Jacobi elliptic function CN(U,M).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2024
#
#  Author:
#
#    Original ALGOL version by Roland Bulirsch.
#    This version by John Burkardt
#
#  Reference:
#
#    Roland Bulirsch,
#    Numerical calculation of elliptic integrals and elliptic functions,
#    Numerische Mathematik,
#    Volume 7, Number 1, 1965, pages 78-90.
#
#  Input:
#
#    real U, M, the arguments.
#
#  Output:
#
#    real cn, the function value.
#
  sn, cn, dn = sncndn ( u, m )

  return cn

def jacobi_cn_test ( ):

#*****************************************************************************80
#
## jacobi_cn_test() tests jacobi_cn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'jacobi_cn_test():' )
  print ( '  jacobi_cn() evaluates the Jacobi elliptic function CN.' )
  print ( '' )
  print ( '    U       M       Exact CN                CN(U,M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, u, a, k, m, cn1 = jacobi_cn_values ( n_data )

    if ( n_data == 0 ):
      break

    cn2 = jacobi_cn ( u, m )

    print ( '%8.4f%8.4f%24.16g%24.16g' % ( u, m, cn1, cn2 ) )

  return

def jacobi_cn_values ( n_data ):

#*****************************************************************************80
#
## jacobi_cn_values() returns some values of the Jacobi elliptic function CN(U,M).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      JacobiCN[ u, m ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    real U, the argument of the function.
#
#    real A, K, M, the parameters of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  m_vec = np.array ( (\
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00 ))

  f_vec = np.array ( (\
      0.9950041652780258E+00, \
      0.9800665778412416E+00, \
      0.8775825618903727E+00, \
      0.5403023058681397E+00, \
     -0.4161468365471424E+00, \
      0.9950124626090582E+00, \
      0.9801976276784098E+00, \
      0.8822663948904403E+00, \
      0.5959765676721407E+00, \
     -0.1031836155277618E+00, \
      0.9950207489532265E+00, \
      0.9803279976447253E+00, \
      0.8868188839700739E+00, \
      0.6480542736638854E+00, \
      0.2658022288340797E+00, \
      0.3661899347368653E-01, \
      0.9803279976447253E+00, \
      0.8868188839700739E+00, \
      0.6480542736638854E+00, \
      0.2658022288340797E+00 ))

  u_vec = np.array ( (\
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      4.0E+00, \
     -0.2E+00, \
     -0.5E+00, \
     -1.0E+00, \
     -2.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    m = 0.0
    k = 0.0
    a = 0.0
    u = 0.0
    f = 0.0
  else:
    m = m_vec[n_data]
    k = np.sqrt ( m )
    a = np.arcsin ( k )
    u = u_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, u, a, k, m, f

def jacobi_dn ( u, m ):

#*****************************************************************************80
#
## jacobi_dn() evaluates the Jacobi elliptic function DN(U,M).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2024
#
#  Author:
#
#    Original ALGOL version by Roland Bulirsch.
#    This version by John Burkardt
#
#  Reference:
#
#    Roland Bulirsch,
#    Numerical calculation of elliptic integrals and elliptic functions,
#    Numerische Mathematik,
#    Volume 7, Number 1, 1965, pages 78-90.
#
#  Input:
#
#    real U, M, the arguments.
#
#  Output:
#
#    real dn, the function value.
#
  sn, cn, dn = sncndn ( u, m )

  return dn

def jacobi_dn_test ( ):

#*****************************************************************************80
#
## jacobi_dn_test() tests jacobi_dn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'jacobi_dn_test():' )
  print ( '  jacobi_dn() evaluates the Jacobi elliptic function DN.' )
  print ( '' )
  print ( '    U       M       Exact DN                DN(U,M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, u, a, k, m, dn1 = jacobi_dn_values ( n_data )

    if ( n_data == 0 ):
      break

    dn2 = jacobi_dn ( u, m )

    print ( '%8.4f%8.4f%24.16g%24.16g' % ( u, m, dn1, dn2 ) )

  return

def jacobi_dn_values ( n_data ):

#*****************************************************************************80
#
## jacobi_dn_values() returns some values of the Jacobi elliptic function DN(U,M).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      JacobiDN[ x, a ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    real U, the argument of the function.
#
#    real A, K, M, the parameters of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  m_vec = np.array ( ( \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00 ))

  f_vec = np.array ( ( \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.9975093485144243E+00, \
     0.9901483195224800E+00, \
     0.9429724257773857E+00, \
     0.8231610016315963E+00, \
     0.7108610477840873E+00, \
     0.9950207489532265E+00, \
     0.9803279976447253E+00, \
     0.8868188839700739E+00, \
     0.6480542736638854E+00, \
     0.2658022288340797E+00, \
     0.3661899347368653E-01, \
     0.9803279976447253E+00, \
     0.8868188839700739E+00, \
     0.6480542736638854E+00, \
     0.2658022288340797E+00  ))

  u_vec = np.array ( ( \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      4.0E+00, \
     -0.2E+00, \
     -0.5E+00, \
     -1.0E+00, \
     -2.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    k = 0.0
    m = 0.0
    u = 0.0
    f = 0.0
  else:
    m = m_vec[n_data]
    k = np.sqrt ( m )
    a = np.arcsin ( k )
    u = u_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, u, a, k, m, f

def jacobi_sn ( u, m ):

#*****************************************************************************80
#
## jacobi_sn() evaluates the Jacobi elliptic function SN(U,M).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2024
#
#  Author:
#
#    Original ALGOL version by Roland Bulirsch.
#    This version by John Burkardt
#
#  Reference:
#
#    Roland Bulirsch,
#    Numerical calculation of elliptic integrals and elliptic functions,
#    Numerische Mathematik,
#    Volume 7, Number 1, 1965, pages 78-90.
#
#  Input:
#
#    real U, M, the arguments.
#
#  Output:
#
#    real sn, function value.
#
  sn, cn, dn = sncndn ( u, m )

  return sn

def jacobi_sn_test ( ):

#*****************************************************************************80
#
## jacobi_sn_test() tests jacobi_sn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'jacobi_sn_test():' )
  print ( '  jacobi_sn() evaluates the Jacobi elliptic function SN.' )
  print ( '' )
  print ( '    U       M       Exact SN                SN(U,M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, u, a, k, m, sn1 = jacobi_sn_values ( n_data )

    if ( n_data == 0 ):
      break

    sn2 = jacobi_sn ( u, m )

    print ( '%8.4f%8.4f%24.16g%24.16g' % ( u, m, sn1, sn2 ) )

  return

def jacobi_sn_values ( n_data ):

#*****************************************************************************80
#
## jacobi_sn_values() returns some values of the Jacobi elliptic function SN(U,M).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      JacobiSN[ u, m ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    real U, the argument of the function.
#
#    real A, K, M, the parameters of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  m_vec = np.array ( ( \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.0E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     0.5E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00, \
     1.0E+00 ))

  f_vec = np.array ( ( \
      0.9983341664682815E-01, \
      0.1986693307950612E+00, \
      0.4794255386042030E+00, \
      0.8414709848078965E+00, \
      0.9092974268256817E+00, \
      0.9975068547462484E-01, \
      0.1980217429819704E+00, \
      0.4707504736556573E+00, \
      0.8030018248956439E+00, \
      0.9946623253580177E+00, \
      0.9966799462495582E-01, \
      0.1973753202249040E+00, \
      0.4621171572600098E+00, \
      0.7615941559557649E+00, \
      0.9640275800758169E+00, \
      0.9993292997390670E+00, \
     -0.1973753202249040E+00, \
     -0.4621171572600098E+00, \
     -0.7615941559557649E+00, \
     -0.9640275800758169E+00 ))

  u_vec = np.array ( ( \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.5E+00, \
      1.0E+00, \
      2.0E+00, \
      4.0E+00, \
     -0.2E+00, \
     -0.5E+00, \
     -1.0E+00, \
     -2.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    k = 0.0
    m = 0.0
    u = 0.0
    f = 0.0
  else:
    m = m_vec[n_data]
    k = np.sqrt ( m )
    a = np.arcsin ( k )
    u = u_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, u, a, k, m, f

def sncndn ( u, m ):

#*****************************************************************************80
#
## sncndn() evaluates Jacobi elliptic functions SN, CN, and DN.
#
#  Discussion:
#
#    Evaluation
#      a = - *cn / *sn;
#    corrected to
#      a = *cn / *sn;
#    after comparing to reference, 26 June 2025.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2025
#
#  Author:
#
#    Original ALGOL version by Roland Bulirsch.
#    This version by John Burkardt
#
#  Reference:
#
#    Roland Bulirsch,
#    Numerical calculation of elliptic integrals and elliptic functions,
#    Numerische Mathematik,
#    Volume 7, Number 1, 1965, pages 78-90.
#
#  Input:
#
#    real U, M, the arguments.
#
#  Output:
#
#    real SN, CN, DN, the value of the Jacobi
#    elliptic functions sn(u,m), cn(u,m), and dn(u,m).
#
  import numpy as np

  maxit = 25

  m_array = np.zeros ( maxit )
  n_array = np.zeros ( maxit )

  m_comp = 1.0 - m
  u_copy = u

  if ( m_comp == 0.0 ):
    sn = np.tanh ( u_copy )
    cn = 1.0 / np.cosh ( u_copy )
    dn = cn
    return sn, cn, dn

  if ( 1.0 < m ):
    d = 1.0 - m_comp
    m_comp = - m_comp / d
    d = np.sqrt ( d )
    u_copy = d * u_copy

  ca = np.sqrt ( np.finfo(float).eps )

  a = 1.0
  dn = 1.0
  l = maxit - 1

  for i in range ( 0, maxit ):

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
#   a = - cn / sn
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

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  sncndn_test ( )
  timestamp ( )
 
