#! /usr/bin/env python
#
def elliptic_fk_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_FK_VALUES returns values of the complete elliptic integral F(K).
#
#  Discussion:
#
#    This is one form of what is sometimes called the complete elliptic 
#    integral of the first kind.
#
#    The function is defined by the formula:
#
#      F(K) = integral ( 0 <= T <= PI/2 ) 
#        dT / sqrt ( 1 - K^2 * sin ( T )^2 )
#
#    In Mathematica, the function can be evaluated by:
#
#      EllipticK[k^2]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2018
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
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( (
     1.570796326794897E+00, \
     1.591003453790792E+00, \
     1.612441348720219E+00, \
     1.635256732264580E+00, \
     1.659623598610528E+00, \
     1.685750354812596E+00, \
     1.713889448178791E+00, \
     1.744350597225613E+00, \
     1.777519371491253E+00, \
     1.813883936816983E+00, \
     1.854074677301372E+00, \
     1.898924910271554E+00, \
     1.949567749806026E+00, \
     2.007598398424376E+00, \
     2.075363135292469E+00, \
     2.156515647499643E+00, \
     2.257205326820854E+00, \
     2.389016486325580E+00, \
     2.578092113348173E+00, \
     2.908337248444552E+00 ))

  x_vec = np.array ( (
     0.0000000000000000E+00, \
     0.2236067977499790E+00, \
     0.3162277660168379E+00, \
     0.3872983346207417E+00, \
     0.4472135954999579E+00, \
     0.5000000000000000E+00, \
     0.5477225575051661E+00, \
     0.5916079783099616E+00, \
     0.6324555320336759E+00, \
     0.6708203932499369E+00, \
     0.7071067811865476E+00, \
     0.7416198487095663E+00, \
     0.7745966692414834E+00, \
     0.8062257748298550E+00, \
     0.8366600265340756E+00, \
     0.8660254037844386E+00, \
     0.8944271909999159E+00, \
     0.9219544457292888E+00, \
     0.9486832980505138E+00, \
     0.9746794344808963E+00 ))

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

def elliptic_fk_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_FK_VALUES_TEST demonstrates the use of ELLIPTIC_FK_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 May 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ELLIPTIC_FK_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPTIC_FK_VALUES stores values of the complete elliptic' )
  print ( '  integral of the first kind, with parameter KM.' )
  print ( '' )
  print ( '      K         F(K)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = elliptic_fk_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPTIC_FK_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_fk_values_test ( )
  timestamp ( )

