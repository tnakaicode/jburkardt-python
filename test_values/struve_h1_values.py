#! /usr/bin/env python
#
def struve_h1_values ( n_data ):

#*****************************************************************************80
#
## STRUVE_H1_VALUES returns some values of the Struve H1 function.
#
#  Discussion:
#
#    The function is defined by:
#
#      H1(x) = 2*x/pi * Integral ( 0 <= t <= pi/2 ) 
#        sin ( x * cos ( t ) )^2 * sin ( t ) dt
#
#    In Mathematica, the function can be evaluated by:
#
#      StruveH[1,x]
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
     0.80950369576367526071E-06, \
     0.12952009724113229165E-04, \
     0.82871615165407083021E-03, \
     0.13207748375849572564E-01, \
     0.19845733620194439894E+00, \
     0.29853823231804706294E+00, \
     0.64676372828356211712E+00, \
     0.10697266613089193593E+01, \
     0.38831308000420560970E+00, \
     0.74854243745107710333E+00, \
     0.84664854642567359993E+00, \
     0.58385732464244384564E+00, \
     0.80600584524215772824E+00, \
     0.53880362132692947616E+00, \
     0.72175037834698998506E+00, \
     0.58007844794544189900E+00, \
     0.60151910385440804463E+00, \
     0.70611511147286827018E+00, \
     0.61631110327201338454E+00, \
     0.62778480765443656489E+00 ))

  x_vec = np.array ( ( \
        0.0019531250E+00, \
       -0.0078125000E+00, \
        0.0625000000E+00, \
       -0.2500000000E+00, \
        1.0000000000E+00, \
        1.2500000000E+00, \
        2.0000000000E+00, \
       -4.0000000000E+00, \
        7.5000000000E+00, \
       11.0000000000E+00, \
       11.5000000000E+00, \
      -16.0000000000E+00, \
       20.0000000000E+00, \
       25.0000000000E+00, \
      -30.0000000000E+00, \
       50.0000000000E+00, \
       75.0000000000E+00, \
      -80.0000000000E+00, \
      100.0000000000E+00, \
     -125.0000000000E+00 ))

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

def struve_h1_values_test ( ):

#*****************************************************************************80
#
## STRUVE_H1_VALUES_TEST demonstrates the use of STRUVE_H1_VALUES.
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
  print ( 'STRUVE_H1_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STRUVE_H1_VALUES stores values of the STRUVE_H1 function.' )
  print ( '' )
  print ( '      X         STRUVE_H1(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = struve_h1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'STRUVE_H1_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  struve_h1_values_test ( )
  timestamp ( )

