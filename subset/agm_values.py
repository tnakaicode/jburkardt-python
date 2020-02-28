#!/usr/bin/env python
#
def agm_values ( n_data ):

#*****************************************************************************80
#
## AGM_VALUES returns some values of the AGM.
#
#  Discussion:
#
#    The AGM is defined for nonnegative A and B.
#
#    The AGM of numbers A and B is defined by setting
#
#      A(0) = A,
#      B(0) = B
#
#      A(N+1) = ( A(N) + B(N) ) / 2
#      B(N+1) = sqrt ( A(N) * B(N) )
#
#    The two sequences both converge to AGM(A,B).
#
#    In Mathematica, the AGM can be evaluated by
#
#      ArithmeticGeometricMean [ a, b ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real A, B, the argument ofs the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 14

  a_vec = np.array ( ( \
     22.0, \
     83.0, \
     42.0, \
     26.0, \
      4.0, \
      6.0, \
     40.0, \
     80.0, \
     90.0, \
      9.0, \
     53.0, \
      1.0, \
      1.0, \
      1.0, \
      1.5 ) )
  b_vec = np.array ( ( \
     96.0, \
     56.0, \
      7.0, \
     11.0, \
     63.0, \
     45.0, \
     75.0, \
      0.0, \
     35.0, \
      1.0, \
     53.0, \
      2.0, \
      4.0, \
      8.0, \
      8.0 ) )
  fx_vec = np.array ( ( \
     52.274641198704240049, \
     68.836530059858524345, \
     20.659301196734009322, \
     17.696854873743648823, \
     23.867049721753300163, \
     20.717015982805991662, \
     56.127842255616681863, \
      0.000000000000000000, \
     59.269565081229636528, \
     3.9362355036495554780, \
     53.000000000000000000, \
     1.4567910310469068692, \
     2.2430285802876025701, \
     3.6157561775973627487, \
     4.0816924080221632670 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    b = 0.0
    fx = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, fx

def agm_values_test ( ):

#*****************************************************************************80
#
## AGM_VALUES_TEST demonstrates the use of AGM_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 February 2008
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'AGM_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  AGM_VALUES stores values of' )
  print ( '  the arithmetic geometric mean function.' )
  print ( '' )
  print ( '      A           B         AGM(A,B)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, fx = agm_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16f' % ( a, b, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'AGM_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  agm_values_test ( )
  timestamp ( )

