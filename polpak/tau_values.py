#! /usr/bin/env python
#
def tau_values ( n_data ):

#*****************************************************************************80
#
## TAU_VALUES returns some values of the Tau function.
#
#  Discussion:
#
#    TAU(N) is the number of divisors of N, including 1 and N.
#
#    In Mathematica, the function can be evaluated by:
#
#      DivisorSigma[1,n]
#
#  First values:
#
#     N   TAU(N)
#
#     1    1
#     2    2
#     3    2
#     4    3
#     5    2
#     6    4
#     7    2
#     8    4
#     9    3
#    10    4
#    11    2
#    12    6
#    13    2
#    14    4
#    15    4
#    16    5
#    17    2
#    18    6
#    19    2
#    20    6
#
#  Formula:
#
#    If the prime factorization of N is
#
#      N = P1^E1 * P2^E2 * ... * PM^EM,
#
#    then
#
#      TAU(N) = ( E1 + 1 ) * ( E2 + 1 ) * ... * ( EM + 1 ).
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
#    Output, integer N, the argument of the Tau function.
#
#    Output, integer C, the value of the Tau function.
#
  import numpy as np

  n_max = 20

  c_vec = np.array ( ( \
    1,  2,  2,  3,  2,  4,  2,  4,  3,  4, \
    2, 12, 12,  4, 18, 24,  2,  8, 14, 28 ))

  n_vec = np.array ( ( \
      1,   2,   3,   4,   5,   6,   7,   8,   9,  10, \
     23,  72, 126, 226, 300, 480, 521, 610, 832, 960 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    c = 0
  else:
    n = n_vec[n_data]
    c = c_vec[n_data]
    n_data = n_data + 1

  return n_data, n, c

def tau_values_test ( ):

#*****************************************************************************80
#
## TAU_VALUES_TEST demonstrates the use of TAU_VALUES.
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
  print ( 'TAU_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TAU_VALUES stores values of the TAU function.' )
  print ( '' )
  print ( '             N    TAU(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, c = tau_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12d  %12d' % ( n, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TAU_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tau_values_test ( )
  timestamp ( )

