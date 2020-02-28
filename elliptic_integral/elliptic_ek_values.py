#! /usr/bin/env python3
#
def elliptic_ek_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_EK_VALUES returns values of the complete elliptic integral E(K).
#
#  Discussion:
#
#    This is one form of what is sometimes called the complete elliptic 
#    integral of the second kind.
#
#    The function is defined by the formula:
#
#      E(K) = integral ( 0 <= T <= PI/2 ) 
#        sqrt ( 1 - K^2 * sin ( T )^2 ) dT
#
#    In Mathematica, the function can be evaluated by:
#
#      EllipticE[k^2]
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

  n_max = 21

  fx_vec = np.array ( ( \
     1.570796326794897E+00, \
     1.550973351780472E+00, \
     1.530757636897763E+00, \
     1.510121832092819E+00, \
     1.489035058095853E+00, \
     1.467462209339427E+00, \
     1.445363064412665E+00, \
     1.422691133490879E+00, \
     1.399392138897432E+00, \
     1.375401971871116E+00, \
     1.350643881047676E+00, \
     1.325024497958230E+00, \
     1.298428035046913E+00, \
     1.270707479650149E+00, \
     1.241670567945823E+00, \
     1.211056027568459E+00, \
     1.178489924327839E+00, \
     1.143395791883166E+00, \
     1.104774732704073E+00, \
     1.060473727766278E+00, \
     1.000000000000000E+00 ))

  x_vec = np.array (( \
     0.0000000000000000, \
     0.2236067977499790, \
     0.3162277660168379, \
     0.3872983346207417, \
     0.4472135954999579, \
     0.5000000000000000, \
     0.5477225575051661, \
     0.5916079783099616, \
     0.6324555320336759, \
     0.6708203932499369, \
     0.7071067811865476, \
     0.7416198487095663, \
     0.7745966692414834, \
     0.8062257748298550, \
     0.8366600265340756, \
     0.8660254037844386, \
     0.8944271909999159, \
     0.9219544457292888, \
     0.9486832980505138, \
     0.9746794344808963, \
     1.0000000000000000 ))

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

def elliptic_ek_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_EK_VALUES_TEST demonstrates the use of ELLIPTIC_EK_VALUES.
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
  print ( 'ELLIPTIC_EK_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPTIC_EK_VALUES stores values of the complete elliptic' )
  print ( '  integral of the second kind, with parameter K.' )
  print ( '' )
  print ( '      K         E(K)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = elliptic_ek_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPTIC_EK_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_ek_values_test ( )
  timestamp ( )

