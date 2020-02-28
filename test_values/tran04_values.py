#! /usr/bin/env python3
#
def tran04_values ( n_data ):

#*****************************************************************************80
#
## TRAN04_VALUES returns some values of the order 4 transportation function.
#
#  Discussion:
#
#    The function is defined by:
#
#      TRAN04(x) = Integral ( 0 <= t <= x ) t^4 exp(t) / ( exp(t) - 1 )^2 dt
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
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
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
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
     0.24835263919461834041E-08, \
     0.10172029353616724881E-04, \
     0.65053332405940765479E-03, \
     0.41150448004155727767E-01, \
     0.31724404523442648241E+00, \
     0.10079442901142373591E+01, \
     0.22010881024333408363E+01, \
     0.38846508619156545210E+01, \
     0.59648223973714765245E+01, \
     0.10731932392998622219E+02, \
     0.11940028876819364777E+02, \
     0.15359784316882182982E+02, \
     0.17372587633093742893E+02, \
     0.19122976016053166969E+02, \
     0.23583979156921941515E+02, \
     0.25273667677030441733E+02, \
     0.25955198214572256372E+02, \
     0.25975350935212241910E+02, \
     0.25975757522084093747E+02, \
     0.25975757609067315288E+02 ))

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
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def tran04_values_test ( ):

#*****************************************************************************80
#
## TRAN04_VALUES_TEST demonstrates the use of TRAN04_VALUES.
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
  print ( 'TRAN04_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRAN04_VALUES stores values of the TRAN04 function.' )
  print ( '' )
  print ( '      X         TRAN04(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = tran04_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRAN04_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tran04_values_test ( )
  timestamp ( )

