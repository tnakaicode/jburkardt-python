#! /usr/bin/env python3
#
def zero_itp_test ( ):

#*****************************************************************************80
#
## zero_itp_test() tests zero_itp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import sys

  print ( '' )
  print ( 'zero_itp_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  zero_itp() seeks a root of a function f(x)' )
  print ( '  in an interval [a,b].' )

  eps = sys.float_info.epsilon

  f = f_01
  a = 1.0
  b = 2.0
  epsi = np.sqrt ( eps )
  k1 = 1.0 / ( b - a ) / 5.0
  k2 = 2.0
  n0 = 1
  verbose = False
  title = 'f_01(x) = sin ( x ) - x / 2'
  zero_itp_example ( f, a, b, epsi, k1, k2, n0, verbose, title )

  f = f_02
  a = 0.0
  b = 1.0
  epsi = np.sqrt ( eps )
  k1 = 1.0 / ( b - a ) / 5.0
  k2 = 2.0
  n0 = 1
  verbose = False
  title = 'f_02(x) = 2 * x - exp ( - x )'
  zero_itp_example ( f, a, b, epsi, k1, k2, n0, verbose, title )

  f = f_03
  a = -1.0
  b =  0.5
  epsi = np.sqrt ( eps )
  k1 = 1.0 / ( b - a ) / 5.0
  k2 = 2.0
  n0 = 1
  verbose = False
  title = 'f_03(x) = x * exp ( - x )'
  zero_itp_example ( f, a, b, epsi, k1, k2, n0, verbose, title )

  f = f_04
  a =  0.0001
  b =  20.0
  epsi = np.sqrt ( eps )
  k1 = 1.0 / ( b - a ) / 5.0
  k2 = 2.0
  n0 = 1
  verbose = False
  title = 'f_04(x) = exp ( x ) - 1 / ( 100 * x * x )'
  zero_itp_example ( f, a, b, epsi, k1, k2, n0, verbose, title )

  f = f_05
  a = -5.0
  b =  2.0
  epsi = np.sqrt ( eps )
  k1 = 1.0 / ( b - a ) / 5.0
  k2 = 2.0
  n0 = 1
  verbose = False
  title = 'f_05(x) = (x+3) * (x-1) * (x-1)'
  zero_itp_example ( f, a, b, epsi, k1, k2, n0, verbose, title )
#
#  These parameter values match the Wikipedia example.
#
  f = f_06
  a =  1.0
  b =  2.0
  epsi = 0.0005
  k1 = 0.1
  k2 = 2.0
  n0 = 1
  verbose = True
  title = 'f_06(x) = x^3 - x - 2'
  zero_itp_example ( f, a, b, epsi, k1, k2, n0, verbose, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'zero_itp_test():' )
  print ( '  Normal end of execution.' )

  return

def zero_itp ( f, a, b, epsi, k1, k2, n0, verbose ):

#*****************************************************************************80
#
## zero_itp() seeks the root of a function using Interpolate/Truncate/Project.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function f ( x ): the name of the user-supplied function.
#
#    real a, b: the endpoints of the change of sign interval.
#
#    real epsi: error tolerance between exact and computed roots.
#
#    real k1: a parameter, with suggested value 0.2 / ( b - a ).
#
#    real k2: a parameter, typically set to 2.
#
#    integer n0: a parameter that can be set to 0 for difficult problems,
#    but is usually set to 1, to take more advantage of the secant method.
#
#    logical verbose: if true, requests additional printed output.
#
#  Output:
#
#    real z, fz: the estimated root and its function value.
#
#    integer ncalls: the number of function calls.
#
  import numpy as np
#
#  Force a < b.
#
  if ( b < a ):
    c = a
    a = b
    b = c
#
#  Require f(a) and f(b) of opposite sign.
#
  ya = f ( a )
  yb = f ( b )

  if ( 0 < ya * yb ):
    print ( '' )
    print ( 'zero_itp(): Fatal error!' )
    print ( '  f(a) and f(b) have same sign.' )
    raise Exception ( "zero_itp(): sign(f(a)) = sign(f(b)).")
#
#  Modify f(x) so that y(a) < 0, 0 < y(b);
#
  if ( 0.0 < ya ):
    s = -1.0
    ya = - ya
    yb = - yb
  else:
    s = +1.0

  n1_2 = np.ceil ( max ( np.log2 ( ( b - a ) / epsi ) - 1, 0 ) )
  nmax = n0 + n1_2

  calls = 0

  if ( verbose ):
    print ( '' )
    print ( '  User has requested additional verbose output.' )
    print ( '  step   [a,    b]    x    f(x)' )
    print ( '' )
#
#  Iterate.
#
  while ( 2.0 * epsi < ( b - a ) ):
#
#  Calculate parameters:
#
    xh = 0.5 * ( a + b )
    r = epsi * 2.0 ** ( nmax - calls ) - 0.5 * ( b - a )
    delta = k1 * ( b - a ) ** k2
#
#  Interpolate:
#
    xf = ( yb * a - ya * b ) / ( yb - ya )
#
#  Truncate:
#
    sigma = np.sign ( xh - xf )

    if ( delta < np.abs ( xh - xf ) ):
      xt = xf + sigma * delta
    else:
      xt = xh
#
#  Project:
#
    if ( np.abs ( xt - xh ) <= r ):
      xitp = xt
    else:
      xitp = xh - sigma * r
#
#  Update the interval:
#
    yitp = s * f ( xitp );

    if ( verbose ):
      print ( '%d  [%g,%g]  f(%g)=%g' % ( calls, a, b, xitp, yitp ) )

    if ( 0.0 < yitp ):
      b = xitp
      yb = yitp
    elif ( yitp < 0.0 ):
      a = xitp
      ya = yitp
    else:
      a = xitp
      b = xitp
      break

    calls = calls + 1

  z = 0.5 * ( a + b )
  fz = f ( z )

  return z, fz, calls

def zero_itp_example ( f, a, b, epsi, k1, k2, n0, verbose, title ):

#*****************************************************************************80
#
## zero_itp_example() tests zero_itp() on a test function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function f ( x ): the user-supplied function.
#
#    real a, b: the endpoints of the change of sign interval.
#
#    real epsi: error tolerance between exact and computed roots.
#
#    real k1: a parameter, with suggested value 0.2 / ( b - a ).
#
#    real k2: a parameter, typically set to 2.
#
#    integer n0: a parameter that can be set to 0 for difficult problems,
#    but is usually set to 1, to take more advantage of the secant method.
#
#    logical verbose: if true, requests additional output from zero_itp().
#
#    string title: a title for the problem.
#
  z, fz, calls = zero_itp ( f, a, b, epsi, k1, k2, n0, verbose )

  fz = f ( z )
  fa = f ( a )
  fb = f ( b )

  print ( '' )
  print ( '  ' + title )
  print ( '' )
  print ( '      A                 Z             B' )
  print ( '    F(A)              F(Z)          F(B)' )
  print ( '' )
  print ( '  %14f  %14f  %14f' % ( a,  z,  b ) )
  print ( '  %14e  %14e  %14e' % ( fa, fz, fb ) )
  print ( '  Number of calls to F = ', calls )
  print ( '  Tolerance epsi = ', epsi )
  print ( '  Parameter k1 = ', k1, ', k2 = ', k2, ', n0 = ', n0 )

  return

def f_01 ( x ):

#*****************************************************************************80
#
## f_01() evaluates sin ( x ) - x / 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = np.sin ( x ) - 0.5 * x

  return value

def f_02 ( x ):

#*****************************************************************************80
#
## f_02() evaluates 2*x-exp(-x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = 2.0 * x - np.exp ( - x )

  return value

def f_03 ( x ):

#*****************************************************************************80
#
## f_03() evaluates x*exp(-x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = x * np.exp ( - x )

  return value

def f_04 ( x ):

#*****************************************************************************80
#
## f_04() evaluates exp(x) - 1 / (100*x*x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  import numpy as np

  value = np.exp ( x ) - 1.0 / 100.0 / x / x

  return value

def f_05 ( x ):

#*****************************************************************************80
#
## f_05() evaluates (x+3)*(x-1)*(x-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  value = ( x + 3.0 ) * ( x - 1.0 ) * ( x - 1.0 )

  return value

def f_06 ( x ):

#*****************************************************************************80
#
## f_06() evaluates x^3 - x - 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the point at which F is to be evaluated.
#
#  Output:
#
#    real VALUE, the value of the function at X.
#
  value = x**3 - x - 2.0

  return value

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  zero_itp_test ( )
  timestamp ( )

