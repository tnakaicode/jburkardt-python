#! /usr/bin/env python
#
def airy_ai_int_values ( n_data ):

#*****************************************************************************80
#
## AIRY_AI_INT_VALUES returns some values of the integral of the Airy function.
#
#  Discussion:
#
#    The function is defined by:
#
#      AIRY_AI_INT(x) = Integral ( 0 <= t <= x ) Ai(t) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
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

  fx_vec = np.array ( ( \
     -0.75228838916610124300E+00, \
     -0.57348350185854889466E+00, \
     -0.76569840313421291743E+00, \
     -0.65181015505382467421E+00, \
     -0.55881974894471876922E+00, \
     -0.56902352870716815309E+00, \
     -0.47800749642926168100E+00, \
     -0.46567398346706861416E+00, \
     -0.96783140945618013679E-01, \
     -0.34683049857035607494E-03, \
      0.34658366917927930790E-03, \
      0.27657581846051227124E-02, \
      0.14595330491185717833E+00, \
      0.23631734191710977960E+00, \
      0.33289264538612212697E+00, \
      0.33318759129779422976E+00, \
      0.33332945170523851439E+00, \
      0.33333331724248357420E+00, \
      0.33333333329916901594E+00, \
      0.33333333333329380187E+00 ) )

  x_vec = np.array ( ( \
     -12.0000000000E+00, \
     -11.0000000000E+00, \
     -10.0000000000E+00, \
      -9.5000000000E+00, \
      -9.0000000000E+00, \
      -6.5000000000E+00, \
      -4.0000000000E+00, \
      -1.0000000000E+00, \
      -0.2500000000E+00, \
      -0.0009765625E+00, \
       0.0009765625E+00, \
       0.0078125000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       4.0000000000E+00, \
       4.5000000000E+00, \
       6.0000000000E+00, \
       8.0000000000E+00, \
      10.0000000000E+00, \
      12.0000000000E+00 ) ) 

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data =n_data + 1

  return n_data, x, fx

def airy_ai_int_values_test ( ):

#*****************************************************************************80
#
## AIRY_AI_INT_VALUES_TEST demonstrates the use of AIRY_AI_INT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'AIRY_AI_INT_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  AIRY_AI_INT_VALUES stores values of' )
  print ( '  the integral of the Airy Ai function.' )
  print ( '' )
  print ( '      X           FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = airy_ai_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'AIRY_AI_INT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  airy_ai_int_values_test ( )
  timestamp ( )

