#! /usr/bin/env python
#
def legendre_function_q_values ( n_data ):

#*****************************************************************************80
#
## LEGENDRE_FUNCTION_Q_VALUES returns values of the Legendre Q function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreQ[n,x]
#
#  Differential equation:
#
#    (1-X*X) Y'' - 2 X Y' + N (N+1) = 0
#
#  First terms:
#
#    Q(0)(X) = 0.5 * log((1+X)/(1-X))
#    Q(1)(X) = Q(0)(X)*X - 1 
#    Q(2)(X) = Q(0)(X)*(3*X*X-1)/4 - 1.5*X
#    Q(3)(X) = Q(0)(X)*(5*X*X*X-3*X)/4 - 2.5*X^2 + 2/3
#    Q(4)(X) = Q(0)(X)*(35*X^4-30*X^2+3)/16 - 35/8 * X^3 + 55/24 * X
#    Q(5)(X) = Q(0)(X)*(63*X^5-70*X^3+15*X)/16 - 63/8*X^4 + 49/8*X^2 - 8/15
#
#  Recursion:
#
#    Q(0) = 0.5 * log ( (1+X) / (1-X) )
#    Q(1) = 0.5 * X * log ( (1+X) / (1-X) ) - 1.0
#
#    Q(N) = ( (2*N-1) * X * Q(N-1) - (N-1) * Q(N-2) ) / N
#
#  Restrictions:
#
#    -1 < X < 1
#
#  Special values:
#
#    Note that the Legendre function Q(N)(X) is equal to the
#    associated Legendre function of the second kind,
#    Q(N,M)(X) with M = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
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
#    Output, integer N, the order of the function.
#
#    Output, real X, the point where the function is evaluated.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 21

  f_vec = np.array ( ( \
      0.2554128118829953E+00, \
     -0.9361467970292512E+00, \
     -0.4787614548274669E+00, \
      0.4246139251747229E+00, \
      0.5448396833845414E+00, \
     -0.9451328261673470E-01, \
     -0.4973516573531213E+00, \
     -0.1499018843853194E+00, \
      0.3649161918783626E+00, \
      0.3055676545072885E+00, \
     -0.1832799367995643E+00, \
      0.6666666666666667E+00, \
      0.6268672028763330E+00, \
      0.5099015515315237E+00, \
      0.3232754180589764E+00, \
      0.8026113738148187E-01, \
     -0.1986547714794823E+00, \
     -0.4828663183349136E+00, \
     -0.7252886849144386E+00, \
     -0.8454443502398846E+00, \
     -0.6627096245052618E+00 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3 ))

  x_vec = np.array ( ( \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.00E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.90E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def legendre_function_q_values_test ( ):

#*****************************************************************************80
#
## LEGENDRE_FUNCTION_Q_VALUES_TEST demonstrates the use of LEGENDRE_FUNCTION_Q_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LEGENDRE_FUNCTION_Q_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LEGENDRE_FUNCTION_Q_VALUES stores values of the Legendre Q function' )
  print ( '' )
  print ( '      N            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = legendre_function_q_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LEGENDRE_FUNCTION_Q_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_function_q_values_test ( )
  timestamp ( )

