#! /usr/bin/env python3
#
def bisection_test ( ):

#*****************************************************************************80
#
## bisection_test() tests bisection().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'bisection_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test bisection()' )

  bisection_example ( 0.0, 8.0, lambda x: x**2 - 2*x - 15, 'x.^2 - 2*x - 15' )

  bisection_example ( 0.0, 1.0, lambda x: np.cos(x) - x, 'cos(x) - x' )

  bisection_example ( 0.0, 10.0, lambda x: kepler(x), 'Kepler function'  )
#
#  Terminate.
#
  print ( '' )
  print ( 'bisection_test():' )
  print ( '  Normal end of execution.' )

  return

def bisection_example ( a, b, f, f_string ):

#*****************************************************************************80
#
## bisection_example() applies bisection() to a particular example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  tol = 10.0 * np.finfo ( float ).eps * ( b - a )
  a, b, it = bisection ( a, b, tol, f )
  x = ( a + b ) / 2.0
  fa = f(a)
  fb = f(b)
  fx = f(x)

  print ( ' ' )
  print ( '  Function = "' + f_string + '"' )
  print ( '  a = ', a, ', f(a) = ', fa )
  print ( '  b = ', b, ', f(b) = ', fb )
  print ( '  Interval tolerance = ', tol )
  print ( '  Number of bisections = ', it )
  print ( '  x = ', x, ' , f(x) = ', fx )

  return

def kepler ( x ):

#*****************************************************************************80
#
## kepler evaluates a version of Kepler's equation.
#
#  Discussion:
#
#    Kepler's equation relates the mean anomaly M, the eccentric anomaly E,
#    andthe eccentricity e of a planetary orbit.
#
#    Typically, e is a fixed feature of the orbit, the value of M is determined
#    by observation, and the value of E is desired.
#
#    Kepler's equation states that:
#      M = E - e sin(E)
#
#    Suppose we have an orbit with e = 2, and we have observed M = 5.  What is
#    the value of E?  The equation becomes:
#      5 = E - 2 sin ( E ).
#
#    To solve for E, we need to rewrite this as a function:
#      F(E) = 5 - E + 2 sin ( E )
#    and then use a nonlinear equation solver to solve for the value of E
#    such that F(E)=0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2023
#
#  Input:
#
#    real x, the current estimate for the value of E.
#
#  Output:
#
#    real value, the Kepler equation residual F(E).
#
  import numpy as np

  value = 5.0 - x + 2.0 * np.sin ( x )

  return value

def bisection ( a, b, tol, f ):

#*****************************************************************************80
#
## bisection() carries out the bisection method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 December 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B: the endpoints of a change of sign interval.
#
#    real TOL: the interval size tolerance.  Once |B-A| < TOL,
#    the iteration will stop.
#
#    pointer value=F(x): a pointer to a function.  This can be
#    an anonymous function or the name of a MATLAB M-file function.
#
#  Output:
#
#    real A, B: the new endpoints that constitute an
#    change of sign interval no larger than TOL.
#
#    integer IT: the number of bisections.
#
  import numpy as np

  it = 0

  fa = f ( a )
  if ( fa == 0.0 ):
    b = a
    return a, b, it

  fb = f ( b )
  if ( fb == 0.0 ):
    a = b
    return a, b, it

  if ( 0.0 < fa * fb ):
    raise Exception ( 'bisection(): [A,B] not a change of sign interval!' )

  while ( tol < np.abs ( b - a ) ):

    c = ( a + b ) / 2.0
    fc = f ( c )
    it = it + 1

    if ( 100 <= it ):
      raise Exception ( 'bisection(): too many iterations!' )

    if ( fc == 0.0 ):
      a = c
      b = c
      return a, b, it
    elif ( np.sign ( fc ) == np.sign ( fa ) ):
      a = c
      fa = fc
    else:
      b = c
      fb = fc

  return a, b, it

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
  bisection_test ( )
  timestamp ( )

