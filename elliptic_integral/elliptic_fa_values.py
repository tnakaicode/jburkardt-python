#! /usr/bin/env python3
#
def elliptic_fa_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_FA_VALUES returns values of the complete elliptic integral F(A).
#
#  Discussion:
#
#    This is one form of what is sometimes called the complete elliptic integral
#    of the first kind.
#
#    The function is defined by the formula:
#
#      F(A) = integral ( 0 <= T <= PI/2 ) 
#        dT / sqrt ( 1 - sin ( A )^2 * sin ( T )^2 )
#
#    In Mathematica, the function can be evaluated by:
#
#      EllipticK[(Sin[a*Pi/180])^2]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
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
#    Output, real X, the argument of the function, measured 
#    in degrees.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 18

  fx_vec = np.array ( ( \
     0.1570796326794897E+01, \
     0.1573792130924768E+01, \
     0.1582842804338351E+01, \
     0.1598142002112540E+01, \
     0.1620025899124204E+01, \
     0.1648995218478530E+01, \
     0.1685750354812596E+01, \
     0.1731245175657058E+01, \
     0.1786769134885021E+01, \
     0.1854074677301372E+01, \
     0.1935581096004722E+01, \
     0.2034715312185791E+01, \
     0.2156515647499643E+01, \
     0.2308786798167196E+01, \
     0.2504550079001634E+01, \
     0.2768063145368768E+01, \
     0.3153385251887839E+01, \
     0.3831741999784146E+01 ))

  x_vec = np.array ( ( \
      0.0E+00, \
      5.0E+00, \
     10.0E+00, \
     15.0E+00, \
     20.0E+00, \
     25.0E+00, \
     30.0E+00, \
     35.0E+00, \
     40.0E+00, \
     45.0E+00, \
     50.0E+00, \
     55.0E+00, \
     60.0E+00, \
     65.0E+00, \
     70.0E+00, \
     75.0E+00, \
     80.0E+00, \
     85.0E+00 ))

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

def elliptic_fa_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_FA_VALUES_TEST demonstrates the use of ELLIPTIC_FA_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ELLIPTIC_FA_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPTIC_FA_VALUES stores values of the complete elliptic' )
  print ( '  integral of the first kind, with parameter A in degrees.' )
  print ( '' )
  print ( '      A             F(A)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = elliptic_fa_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPTIC_FA_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_fa_values_test ( )
  timestamp ( )

