#! /usr/bin/env python3
#
def tran03_values ( n_data ):

#*****************************************************************************80
#
## TRAN03_VALUES returns some values of the order 3 transportation function.
#
#  Discussion:
#
#    The function is defined by:
#
#      TRAN03(x) = Integral ( 0 <= t <= x ) t^3 exp(t) / ( exp(t) - 1 )^2 dt
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
     0.19073483296476379584E-05, \
     0.48826138243180786081E-03, \
     0.78074163848431205820E-02, \
     0.12370868718812031049E+00, \
     0.47984100657241749994E+00, \
     0.10269431622039754738E+01, \
     0.17063547219458658863E+01, \
     0.24539217444475937661E+01, \
     0.32106046629422467723E+01, \
     0.45792174372291563703E+01, \
     0.48722022832940370805E+01, \
     0.56143866138422732286E+01, \
     0.59984455864575470009E+01, \
     0.63033953673480961120E+01, \
     0.69579908688361166266E+01, \
     0.71503227120085929750E+01, \
     0.72110731475871876393E+01, \
     0.72123221966388461839E+01, \
     0.72123414161609465119E+01, \
     0.72123414189575656868E+01 ))

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

def tran03_values_test ( ):

#*****************************************************************************80
#
## TRAN03_VALUES_TEST demonstrates the use of TRAN03_VALUES.
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
  print ( 'TRAN03_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRAN03_VALUES stores values of the TRAN03 function.' )
  print ( '' )
  print ( '      X         TRAN03(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = tran03_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRAN03_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tran03_values_test ( )
  timestamp ( )

