#! /usr/bin/env python
#
def stromgen_values ( n_data ):

#*****************************************************************************80
#
## STROMGEN_VALUES returns some values of the STROMGEN function.
#
#  Discussion:
#
#    The function is defined by:
#
#      STROMGEN(X) = Integral ( 0 <= t <= X ) t^7 * exp(2*t) / (exp(t)-1)^3 dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
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
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
     0.21901065985698662316E-15, \
     0.22481399438625244761E-12, \
     0.23245019579558857124E-09, \
     0.24719561475975007037E-06, \
     0.28992610989833245669E-03, \
     0.10698146390809715091E-01, \
     0.89707650964424730705E-01, \
     0.40049605719592888440E+00, \
     0.30504104398079096598E+01, \
     0.11367704858439426431E+02, \
     0.12960679405324786954E+02, \
     0.18548713944748505675E+02, \
     0.27866273821903121400E+02, \
     0.51963334071699323351E+02, \
     0.10861016747891228129E+03, \
     0.15378903316556621624E+03, \
     0.19302665532558721516E+03, \
     0.19636850166006541482E+03, \
     0.19651946766008214217E+03, \
     0.19651956920868316152E+03 ))

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0078125000E+00, \
       0.0312500000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       1.5000000000E+00, \
       2.0000000000E+00, \
       3.0000000000E+00, \
       4.0000000000E+00, \
       4.1250000000E+00, \
       4.5000000000E+00, \
       5.0000000000E+00, \
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
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def stromgen_values_test ( ):

#*****************************************************************************80
#
## STROMGEN_VALUES_TEST demonstrates the use of STROMGEN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'STROMGEN_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STROMGEN_VALUES stores values of the STROMGEN function.' )
  print ( '' )
  print ( '      X         STROMGEN(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = stromgen_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'STROMGEN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  stromgen_values_test ( )
  timestamp ( )

