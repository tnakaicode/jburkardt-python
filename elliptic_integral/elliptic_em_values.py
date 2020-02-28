#! /usr/bin/env python3
#
def elliptic_em_values ( n_data ):

#*****************************************************************************80
#
## ELLIPTIC_EM_VALUES returns values of the complete elliptic integral E(M).
#
#  Discussion:
#
#    This is one form of what is sometimes called the complete elliptic 
#    integral of the second kind.
#
#    The function is defined by the formula:
#
#      E(M) = integral ( 0 <= T <= PI/2 ) 
#        sqrt ( 1 - M * sin ( T )^2 ) dT
#
#    In Mathematica, the function can be evaluated by:
#
#      EllipticE[m]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 September 2004
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
     0.00E+00, \
     0.05E+00, \
     0.10E+00, \
     0.15E+00, \
     0.20E+00, \
     0.25E+00, \
     0.30E+00, \
     0.35E+00, \
     0.40E+00, \
     0.45E+00, \
     0.50E+00, \
     0.55E+00, \
     0.60E+00, \
     0.65E+00, \
     0.70E+00, \
     0.75E+00, \
     0.80E+00, \
     0.85E+00, \
     0.90E+00, \
     0.95E+00, \
     1.00E+00 ))

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

def elliptic_em_values_test ( ):

#*****************************************************************************80
#
## ELLIPTIC_EM_VALUES_TEST demonstrates the use of ELLIPTIC_EM_VALUES.
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
  import platform

  print ( '' )
  print ( 'ELLIPTIC_EM_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPTIC_EM_VALUES stores values of the complete elliptic' )
  print ( '  integral of the second kind, with parameter modulus M.' )
  print ( '' )
  print ( '      M         E(M)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = elliptic_em_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPTIC_EM_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  elliptic_em_values_test ( )
  timestamp ( )

