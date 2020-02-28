#! /usr/bin/env python
#
def struve_l0_values ( n_data ):

#*****************************************************************************80
#
## STRUVE_L0_VALUES returns some values of the Struve L0 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      StruveL[0,x]
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
      0.12433985199262820188E-02, \
     -0.19896526647882937004E-01, \
      0.79715713253115014945E-01, \
     -0.32724069939418078025E+00, \
      0.71024318593789088874E+00, \
      0.19374337579914456612E+01, \
     -0.11131050203248583431E+02, \
      0.16850062034703267148E+03, \
     -0.28156522493745948555E+04, \
      0.89344618796978400815E+06, \
      0.11382025002851451057E+07, \
     -0.23549701855860190304E+07, \
      0.43558282527641046718E+08, \
      0.49993516476037957165E+09, \
     -0.57745606064408041689E+10, \
      0.78167229782395624524E+12, \
     -0.14894774793419899908E+17, \
      0.29325537838493363267E+21, \
      0.58940770556098011683E+25, \
     -0.12015889579125463605E+30 ))

  x_vec = np.array ( ( \
       0.0019531250E+00, \
      -0.0312500000E+00, \
       0.1250000000E+00, \
      -0.5000000000E+00, \
       1.0000000000E+00, \
       2.0000000000E+00, \
      -4.0000000000E+00, \
       7.0000000000E+00, \
     -10.0000000000E+00, \
      16.0000000000E+00, \
      16.2500000000E+00, \
     -17.0000000000E+00, \
      20.0000000000E+00, \
      22.5000000000E+00, \
     -25.0000000000E+00, \
      30.0000000000E+00, \
     -40.0000000000E+00, \
      50.0000000000E+00, \
      60.0000000000E+00, \
     -70.0000000000E+00 ))

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

def struve_l0_values_test ( ):

#*****************************************************************************80
#
## STRUVE_L0_VALUES_TEST demonstrates the use of STRUVE_L0_VALUES.
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
  print ( 'STRUVE_L0_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STRUVE_L0_VALUES stores values of the STRUVE_L0 function.' )
  print ( '' )
  print ( '      X         STRUVE_L0(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = struve_l0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'STRUVE_L0_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  struve_l0_values_test ( )
  timestamp ( )

