#! /usr/bin/env python3
#
def tran05_values ( n_data ):

#*****************************************************************************80
#
## TRAN05_VALUES returns some values of the order 5 transportation function.
#
#  Discussion:
#
#    The function is defined by:
#
#      TRAN05(x) = Integral ( 0 <= t <= x ) t^5 exp(t) / ( exp(t) - 1 )^2 dt
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
     0.36379780361036116971E-11, \
     0.23840564453948442379E-06, \
     0.60982205372226969189E-04, \
     0.15410004586376649337E-01, \
     0.23661587923909478926E+00, \
     0.11198756851307629651E+01, \
     0.32292901663684049171E+01, \
     0.70362973105160654056E+01, \
     0.12770557691044159511E+02, \
     0.29488339015245845447E+02, \
     0.34471340540362254586E+02, \
     0.50263092218175187785E+02, \
     0.60819909101127165207E+02, \
     0.70873334429213460498E+02, \
     0.10147781242977788097E+03, \
     0.11638074540242071077E+03, \
     0.12409623901262967878E+03, \
     0.12442270155632550228E+03, \
     0.12443132790838589548E+03, \
     0.12443133061720432435E+03 ))

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

def tran05_values_test ( ):

#*****************************************************************************80
#
## TRAN05_VALUES_TEST demonstrates the use of TRAN05_VALUES.
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
  print ( 'TRAN05_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRAN05_VALUES stores values of the TRAN05 function.' )
  print ( '' )
  print ( '      X         TRAN05(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = tran05_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRAN05_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tran05_values_test ( )
  timestamp ( )

