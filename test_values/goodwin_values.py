#! /usr/bin/env python
#
def goodwin_values ( n_data ):

#*****************************************************************************80
#
## GOODWIN_VALUES returns some values of the Goodwin and Staton function.
#
#  Discussion:
#
#    The function is defined by:
#
#      GOODWIN(x) = Integral ( 0 <= t < infinity ) exp ( -t^2 ) / ( t + x ) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#      special functions,
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
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
      0.59531540040441651584E+01, \
      0.45769601268624494109E+01, \
      0.32288921331902217638E+01, \
      0.19746110873568719362E+01, \
      0.96356046208697728563E+00, \
      0.60513365250334458174E+00, \
      0.51305506459532198016E+00, \
      0.44598602820946133091E+00, \
      0.37344458206879749357E+00, \
      0.35433592884953063055E+00, \
      0.33712156518881920994E+00, \
      0.29436170729362979176E+00, \
      0.25193499644897222840E+00, \
      0.22028778222123939276E+00, \
      0.19575258237698917033E+00, \
      0.17616303166670699424E+00, \
      0.16015469479664778673E+00, \
      0.14096116876193391066E+00, \
      0.13554987191049066274E+00, \
      0.11751605060085098084E+00 ))

  x_vec = np.array ( ( \
      0.0019531250E+00, \
      0.0078125000E+00, \
      0.0312500000E+00, \
      0.1250000000E+00, \
      0.5000000000E+00, \
      1.0000000000E+00, \
      1.2500000000E+00, \
      1.5000000000E+00, \
      1.8750000000E+00, \
      2.0000000000E+00, \
      2.1250000000E+00, \
      2.5000000000E+00, \
      3.0000000000E+00, \
      3.5000000000E+00, \
      4.0000000000E+00, \
      4.5000000000E+00, \
      5.0000000000E+00, \
      5.7500000000E+00, \
      6.0000000000E+00, \
      7.0000000000E+00 ))

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

def goodwin_values_test ( ):

#*****************************************************************************80
#
## GOODWIN_VALUE_TEST demonstrates the use of GOODWIN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GOODWIN_VALUES:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GOODWIN_VALUES stores values of the Gudermannian function.' )
  print ( '' )
  print ( '      X              GOODWIN(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = goodwin_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GOODWIN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  goodwin_values_test ( )
  timestamp ( )


