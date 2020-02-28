#! /usr/bin/env python
#
def debye1_values ( n_data ):

#*****************************************************************************80
#
## DEBYE1_VALUES returns some values of Debye's function of order 1.
#
#  Discussion:
#
#    The function is defined by:
#
#      DEBYE1(x) = 1 / x * Integral ( 0 <= t <= x ) t / ( exp ( t ) - 1 ) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#      special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#   
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
      0.99951182471380889183E+00, \
      0.99221462647120597836E+00, \
      0.96918395997895308324E+00, \
      0.88192715679060552968E+00, \
      0.77750463411224827642E+00, \
      0.68614531078940204342E+00, \
      0.60694728460981007205E+00, \
      0.53878956907785587703E+00, \
      0.48043521957304283829E+00, \
      0.38814802129793784501E+00, \
      0.36930802829242526815E+00, \
      0.32087619770014612104E+00, \
      0.29423996623154246701E+00, \
      0.27126046678502189985E+00, \
      0.20523930310221503723E+00, \
      0.16444346567994602563E+00, \
      0.10966194482735821276E+00, \
      0.82246701178200016086E-01, \
      0.54831135561510852445E-01, \
      0.32898681336964528729E-01 ))

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0312500000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       1.5000000000E+00, \
       2.0000000000E+00, \
       2.5000000000E+00, \
       3.0000000000E+00, \
       4.0000000000E+00, \
       4.2500000000E+00, \
       5.0000000000E+00, \
       5.5000000000E+00, \
       6.0000000000E+00, \
       8.0000000000E+00, \
      10.0000000000E+00, \
      15.0000000000E+00, \
      20.0000000000E+00, \
      30.0000000000E+00, \
      50.0000000000E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def debye1_values_test ( ):

#*****************************************************************************80
#
## DEBYE1_VALUES_TEST demonstrates the use of DEBYE1_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DEBYE1_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DEBYE1_VALUES stores values of the Debye function of order 1.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = debye1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DEBYE1_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  debye1_values_test ( )
  timestamp ( )

