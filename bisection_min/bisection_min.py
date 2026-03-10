#! /usr/bin/env python3
#
def bisection_min_test ( ):

#*****************************************************************************80
#
## bisection_min_test() tests bisection_min().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'bisection_min_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  bisection_min() seeks a minimizer' )
  print ( '  of a function f(x) in the interval [a,b],' )
  print ( '  assuming f(x) is unimodal over [a,b],' )
#
#  humps(x) = 1 / ((x-0.3)^2 + 0.01) + 1 / ((x-0.9)^2 + 0.04) - 6.0
#
  a = 0.3
  b = 0.9
  x_tol = 0.000001

  print ( '' )
  print ( '  f = humps_fun(x)' )
  print ( '  f(', a, ') =', humps_fun ( a ) )
  print ( '  f(', b, ') =', humps_fun ( b ) )
  print ( '  x_tol =', x_tol )
  a, b, it = bisection_min ( humps_fun, a, b, x_tol )
  print ( '' )
  print ( '  ', it, 'iterations were taken' )
  print ( '  f(', a, ') =', humps_fun ( a ) )
  print ( '  f(', b, ') =', humps_fun ( b ) )
#
#  test_fun(x)=x^4+10*x*sin(x^2)
#
  a = -2.0
  b = 1.0
  x_tol = 0.000001

  print ( '' )
  print ( '  f = test_fun(x)' )
  print ( '  f(', a, ') = ', test_fun ( a ) )
  print ( '  f(', b, ') = ', test_fun ( b ) )
  print ( '  x_tol =', x_tol )
  a, b, it = bisection_min ( test_fun, a, b, x_tol )
  print ( '' )
  print ( '  ', it, 'iterations were taken' )
  print ( '  f(', a, ') = ', test_fun ( a ) )
  print ( '  f(', b, ') = ', test_fun ( b ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'bisection_min_test():' )
  print ( '  Normal end of execution.' )

  return

def bisection_min ( f, a_init, b_init, x_tol ):

#*****************************************************************************80
#
## bisection_min() uses bisection to find the minimum of a unimodal function.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real f(x): evaluated the unimodal function.
#
#    real a_init, b_init: the initial interval.
#
#    real x_tol: bisection stops when the interval is smaller than x_tol.
#
#  Output:
#
#    real a, b: the final interval.
#
  import numpy as np

  it = 0
  a = a_init
  b = b_init

  while ( True ):
#
#  Start the iteration by evaluating f at the midpoint.
#
    if ( it == 0 ):

      m = 0.5 * ( a + b )
      fa = f ( a )
      fm = f ( m )
      fb = f ( b )

#
#  Evaluate f at the left and right midpoints
#  and consider how to proceed.
#
    else:

      d = 0.5 * ( a + m )
      fd = f ( d )

      e = 0.5 * ( m + b )
      fe = f ( e )
#
#  Left midpoint is smaller than fm.
#  Shrink interval to [a, left midpoint, m].
#
      if ( fd <= fm ):
        b = m
        fb = fm
        m = d
        fm = fd
#
#  Right midpoint is smaller than fm.
#  Shrink interval to [m,right midpoint,b].
#
      elif ( fe <= fm ):
        a = m
        fa = fm
        m = e
        fm = fe
#
#  fm is smaller than right or left midpoints.
#  Shrink interval to [left midpoint,m,right midpoint].
#
      else:
        a = d
        fa = fd
        b = e
        fb = fe

    if ( np.abs ( b - a ) < x_tol ):
      break

    it = it + 1

  return a, b, it

def humps_fun ( x ):

#*****************************************************************************80
#
## humps_fun() evaluates a function used for demonstrations.
#
#  Discussion:
#
#    The "interesting" portion of the function is visible over the range
#    0 <= x <= 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 June 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(): the evaluation points.
#
#  Output:
#
#    real y(): the function values.
#
  y = 1.0 / ( (x-0.3)**2 + 0.01 ) + 1.0 / ( (x-0.9)**2 + 0.04 ) - 6.0

  return y

def test_fun ( x ):

#*****************************************************************************80
#
## test_fun() evaluates a function used for demonstrations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(): the evaluation points.
#
#  Output:
#
#    real y(): the function values.
#
  import numpy as np

  y = x**4 + 10.0 * x * np.sin ( x**2 )

  return y

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
#    06 April 2013
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
  bisection_min_test ( )
  timestamp ( )
