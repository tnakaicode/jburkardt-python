#! /usr/bin/env python
#
def jacobi_cn_values ( n_data ):

#*****************************************************************************80
#
## JACOBI_CN_VALUES returns some values of the Jacobi elliptic function CN(U,M).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      JacobiCN[ u, m ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 June 2018
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real U, M, the argument of the function.
#
#    Output, real F, the value of the function.
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
    u = 0.0
    f = 0.0
  else:
    m = m_vec[n_data]
    u = u_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, u, m, f

def jacobi_cn_values_test ( ):

#*****************************************************************************80
#
## JACOBI_CN_VALUES_TEST demonstrates the use of JACOBI_CN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 June 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'JACOBI_CN_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  JACOBI_CN_VALUES stores values of the Jacobi CN function.' )
  print ( '' )
  print ( '      U         M        JACOBI_CN(U,M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, u, m, f = jacobi_cn_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( u, m, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'JACOBI_CN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  jacobi_cn_values_test ( )
  timestamp ( )

