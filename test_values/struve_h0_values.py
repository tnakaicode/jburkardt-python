#! /usr/bin/env python
#
def struve_h0_values ( n_data ):

#*****************************************************************************80
#
## STRUVE_H0_VALUES returns some values of the Struve H0 function.
#
#  Discussion:
#
#    The function is defined by:
#
#      HO(x) = 2/pi * Integral ( 0 <= t <= pi/2 ) sin ( x * cos ( t ) ) dt
#
#    In Mathematica, the function can be evaluated by:
#
#      StruveH[0,x]
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
      0.12433974658847434366E-02, \
     -0.49735582423748415045E-02, \
      0.39771469054536941564E-01, \
     -0.15805246001653314198E+00, \
      0.56865662704828795099E+00, \
      0.66598399314899916605E+00, \
      0.79085884950809589255E+00, \
     -0.13501457342248639716E+00, \
      0.20086479668164503137E+00, \
     -0.11142097800261991552E+00, \
     -0.17026804865989885869E+00, \
     -0.13544931808186467594E+00, \
      0.94393698081323450897E-01, \
     -0.10182482016001510271E+00, \
      0.96098421554162110012E-01, \
     -0.85337674826118998952E-01, \
     -0.76882290637052720045E-01, \
      0.47663833591418256339E-01, \
     -0.70878751689647343204E-01, \
      0.65752908073352785368E-01 ))

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

def struve_h0_values_test ( ):

#*****************************************************************************80
#
## STRUVE_H0_VALUES_TEST demonstrates the use of STRUVE_H0_VALUES.
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
  print ( 'STRUVE_H0_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STRUVE_H0_VALUES stores values of the STRUVE_H0 function.' )
  print ( '' )
  print ( '      X         STRUVE_H0(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = struve_h0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'STRUVE_H0_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  struve_h0_values_test ( )
  timestamp ( )

