#! /usr/bin/env python3
#
def golden_section_test ( ):

#*****************************************************************************80
#
## golden_section_test() tests golden_section().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'golden_section_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  golden_section() seeks a minimizer' )
  print ( '  of a function f(x) in the interval [a,b],' )
  print ( '  assuming f(x) is unimodal over [a,b],' )
#
#  humps(x) = 1 / ((x-0.3)^2 + 0.01) + 1 / ((x-0.9)^2 + 0.04) - 6.0
#
  a = 0.3
  b = 0.9
  n = 25
  x_tol = 0.000001

  print ( '' )
  print ( '  f = humps_fun(x)' )
  print ( '  f(', a, ') =', humps_fun ( a ) )
  print ( '  f(', b, ') =', humps_fun ( b ) )
  print ( '  iteration limit n =', n )
  print ( '  x_tol =', x_tol )
  a, b, it = golden_section ( humps_fun, a, b, n, x_tol )
  print ( '' )
  print ( '  ',it,'iterations were taken', it )
  print ( '  f(', a, ') =', humps_fun ( a ) )
  print ( '  f(', b, ') =', humps_fun ( b ) )
#
#  test_fun(x)=x^4+10*x*sin(x^2)
#
  a = -2.0
  b = 1.0
  n = 35
  x_tol = 0.000001

  print ( '' )
  print ( '  f = test_fun(x)' )
  print ( '  f(', a, ') = ', test_fun ( a ) )
  print ( '  f(', b, ') = ', test_fun ( b ) )
  print ( '  iteration limit n =', n )
  print ( '  x_tol =', x_tol )
  a, b, it = golden_section ( test_fun, a, b, n, x_tol )
  print ( '' )
  print ( '  ', it, 'iterations were taken' )
  print ( '  f(', a, ') = ', test_fun ( a ) )
  print ( '  f(', b, ') = ', test_fun ( b ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'golden_section_test():' )
  print ( '  Normal end of execution.' )

  return

def golden_section ( f, a, b, n, x_tol ):

#*****************************************************************************80
#
## golden_section() seeks a minimizer of a unimodal function in [a,b].
#
#  Discussion:
#
#    A unimodal function f(x) in [a,b] has a minimizer a <= c <= b such that
#    f(x) strictly decreases between a and c, and strictly increases between
#    c and b.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 August 2019
#
#  Author:
#
#    Original MATLAB code by J Nathan Kutz.
#    This version by John Burkardt.
#
#  Reference:
#
#    J Nathan Kutz,
#    Data Driven Modeling and Scientific Computation,
#    Oxford University Press, 2013,
#    ISBN: 978-0-19-966034-6.
#
#  Input:
#
#    function handle f: the function to be minimized.
#
#    real a, b: the left and right endpoints.
#
#    integer n: the maximum number of iterations allowed.
#    n must be at least 1.
#
#    real x_tol: a tolerance for the width of the x interval.
#
#  Output:
#
#    real a, b: the current interval containing the minimizer.
#
#    integer it: the number of steps taken.
#
  import numpy as np

  for it in range ( 0, n + 1 ):

    if ( it == 0 ):

      g = ( - 1.0 + np.sqrt ( 5.0 ) ) / 2.0
      x1 =         g   * a + ( 1.0 - g ) * b
      x2 = ( 1.0 - g ) * a +         g   * b
      f1 = f ( x1 )
      f2 = f ( x2 )

    else:

      if ( f1 < f2 ):

        b = x2
        x2 = x1
        f2 = f1
        x1 = g * a + ( 1.0 - g ) * b
        f1 = f ( x1 )

      else:

        a = x1
        x1 = x2
        f1 = f2
        x2 = ( 1.0 - g ) * a + g * b
        f2 = f ( x2 )

    if ( np.abs ( b - a ) <= x_tol ):
      break

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
  golden_section_test ( )
  timestamp ( )

