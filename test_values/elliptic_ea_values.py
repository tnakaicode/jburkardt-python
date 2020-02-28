#! /usr/bin/env python
#
def elliptic_ea_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_EA_VALUES returns values of the complete elliptic integral E(A).
#
#  Discussion:
#
#    This is one form of what is sometimes called the complete elliptic 
#    integral of the second kind.
#
#    The function is defined by the formula:
#
#      E(A) = integral ( 0 <= T <= PI/2 ) 
#        sqrt ( 1 - sin ( A )^2 * sin ( T )^2 ) dT
#
#    In Mathematica, the function can be evaluated by:
#
#      EllipticE[(Sin[Pi*a/180])^2]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
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

  n_max = 19

  fx_vec = np.array ( ( \
     1.570796326794897E+00, \
     1.567809073977622E+00, \
     1.558887196601596E+00, \
     1.544150496914673E+00, \
     1.523799205259774E+00, \
     1.498114928422116E+00, \
     1.467462209339427E+00, \
     1.432290969306756E+00, \
     1.393140248523812E+00, \
     1.350643881047676E+00, \
     1.305539094297794E+00, \
     1.258679624779997E+00, \
     1.211056027568459E+00, \
     1.163827964493139E+00, \
     1.118377737969864E+00, \
     1.076405113076403E+00, \
     1.040114395706010E+00, \
     1.012663506234396E+00, \
     1.000000000000000E+00 ))

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
     85.0E+00, \
     90.0E+00 ) )

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

def elliptic_ea_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_EA_VALUES_TEST demonstrates the use of ELLIPTIC_EA_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ELLIPTIC_EA_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPTIC_EA_VALUES stores values of the complete elliptic' )
  print ( '  integral of the second kind, with parameter A in degrees.' )
  print ( '' )
  print ( '      A             E(A)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = elliptic_ea_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPTIC_EA_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_ea_values_test ( )
  timestamp ( )
