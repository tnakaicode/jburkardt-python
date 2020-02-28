#! /usr/bin/env python
#
def exp_values ( n_data ):

#*****************************************************************************80
#
## EXP_VALUES returns some values of the exponential function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Exp[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
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

  n_max = 24

  fx_vec = np.array ( (
    0.000045399929762484851536E+00, \
    0.0067379469990854670966E+00, \
    0.36787944117144232160E+00, \
    1.0000000000000000000E+00, \
    1.0000000100000000500E+00, \
    1.0001000050001666708E+00, \
    1.0010005001667083417E+00, \
    1.0100501670841680575E+00, \
    1.1051709180756476248E+00, \
    1.2214027581601698339E+00, \
    1.3498588075760031040E+00, \
    1.4918246976412703178E+00, \
    1.6487212707001281468E+00, \
    1.8221188003905089749E+00, \
    2.0137527074704765216E+00, \
    2.2255409284924676046E+00, \
    2.4596031111569496638E+00, \
    2.7182818284590452354E+00, \
    7.3890560989306502272E+00, \
    23.140692632779269006E+00, \
     148.41315910257660342E+00, \
    22026.465794806716517E+00, \
    4.8516519540979027797E+08, \
    2.3538526683701998541E+17 ))

  x_vec = np.array ( (
     -10.0E+00, \
      -5.0E+00, \
      -1.0E+00, \
       0.0E+00, \
       0.00000001E+00, \
       0.0001E+00, \
       0.001E+00, \
       0.01E+00, \
       0.1E+00, \
       0.2E+00, \
       0.3E+00, \
       0.4E+00, \
       0.5E+00, \
       0.6E+00, \
       0.7E+00, \
       0.8E+00, \
       0.9E+00, \
       1.0E+00, \
       2.0E+00, \
       3.1415926535897932385E+00, \
       5.0E+00, \
      10.0E+00, \
      20.0E+00, \
      40.0E+00 ))

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

def exp_values_test ( ):

#*****************************************************************************80
#
## EXP_VALUES_TEST demonstrates the use of EXP_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'EXP_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EXP_VALUES stores values of the exponential function.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = exp_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EXP_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  exp_values_test ( )
  timestamp ( )

