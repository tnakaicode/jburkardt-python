#! /usr/bin/env python3
#
def asa103_test ( ):

#*****************************************************************************80
#
## ASA103_TEST tests the ASA103 library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ASA103_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the ASA103 library.' )

  digamma_test ( )
  psi_values_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ASA103_TEST:' )
  print ( '  Normal end of execution.' )
  return

def digamma ( x ):

#*****************************************************************************80
#
## DIGAMMA calculates DIGAMMA ( X ) = d ( LOG ( GAMMA ( X ) ) ) / dX
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    Original FORTRAN77 version by Jose Bernardo.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jose Bernardo,
#    Algorithm AS 103:
#    Psi ( Digamma ) Function,
#    Applied Statistics,
#    Volume 25, Number 3, 1976, pages 315-317.
#
#  Parameters:
#
#    Input, real X, the argument of the digamma function.
#    0 < X.
#
#    Output, real DIGAMMA, the value of the digamma function at X.
#
#    Output, integer IFAULT, error flag.
#    0, no error.
#    1, X <= 0.
#
  import numpy as np
#
#  Check the input.
#
  if ( x <= 0.0 ):
    value = 0.0
    ifault = 1
    return value, ifault
#
#  Initialize.
#
  ifault = 0
  value = 0.0
#
#  Use approximation for small argument.
#
  if ( x <= 0.000001 ):
    euler_mascheroni = 0.57721566490153286060
    value = - euler_mascheroni - 1.0 / x + 1.6449340668482264365 * x
    return value, ifault
#
#  Reduce to DIGAMA(X + N).
#
  while ( x < 8.5 ):
    value = value - 1.0 / x
    x = x + 1.0
#
#  Use Stirling's (actually de Moivre's) expansion.
#
  r = 1.0 / x
  value = value + np.log ( x ) - 0.5 * r
  r = r * r
  value = value \
    - r * ( 1.0 / 12.0 \
    - r * ( 1.0 / 120.0 \
    - r * ( 1.0 / 252.0 \
    - r * ( 1.0 / 240.0 \
    - r * ( 1.0 / 132.0 ) ) ) ) )

  return value, ifault

def digamma_test ( ):

#*****************************************************************************80
#
## DIGAMMA_TEST tests DIGAMMA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DIGAMMA_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIGAMMA computes the Digamma or Psi function.' )
  print ( '  Compare the result to tabulated values.' )
  print ( '' )
  print ( '          X         FX                        FX2' )
  print ( '                    (Tabulated)               (DIGAMMA)               DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, ifault = digamma ( x )

    print ( '  %12.4f  %24.16e  %24.16e  %10.4e' % ( x, fx, fx2, abs ( fx - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIGAMMA_TEST:' )
  print ( '  Normal end of execution.' )
  return

def psi_values ( n_data ):

#*****************************************************************************80
#
## PSI_VALUES returns some values of the Psi or Digamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyGamma[x]
#
#    or
#
#      PolyGamma[0,x]
#
#    PSI(X) = d ln ( Gamma ( X ) ) / d X = Gamma'(X) / Gamma(X)
#
#    PSI(1) = -Euler's constant.
#
#    PSI(X+1) = PSI(X) + 1 / X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
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
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
    -10.42375494041108E+00, \
     -5.289039896592188E+00, \
     -3.502524222200133E+00, \
     -2.561384544585116E+00, \
     -1.963510026021423E+00, \
     -1.540619213893190E+00, \
     -1.220023553697935E+00, \
     -0.9650085667061385E+00, \
     -0.7549269499470514E+00, \
     -0.5772156649015329E+00, \
     -0.4237549404110768E+00, \
     -0.2890398965921883E+00, \
     -0.1691908888667997E+00, \
     -0.6138454458511615E-01, \
      0.3648997397857652E-01, \
      0.1260474527734763E+00, \
      0.2085478748734940E+00, \
      0.2849914332938615E+00, \
      0.3561841611640597E+00, \
      0.4227843350984671E+00 ))

  x_vec = np.array ( ( \
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
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ))

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

def psi_values_test ( ):

#*****************************************************************************80
#
## PSI_VALUES_TEST demonstrates the use of PSI_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PSI_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PSI_VALUES stores values of the PSI function.' )
  print ( '' )
  print ( '      X         PSI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PSI_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  asa103_test ( )
  timestamp ( )

