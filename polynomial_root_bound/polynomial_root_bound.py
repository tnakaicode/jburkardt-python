#! /usr/bin/env python3
#
def polynomial_root_bound_test ( ):

#*****************************************************************************80
#
## polynomial_root_bound_test() tests polynomial_root_bound().
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
  print ( 'polynomial_root_bound_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polynomial_root_bound()' )

  polynomial1_test ( )
  polynomial2_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polynomial_root_bound_test():' )
  print ( '  Normal end of execution.' )

  return

def polynomial1_test ( ):

#*****************************************************************************80
#
## polynomial1_test() deals with a particular polynomial.
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
  from numpy.polynomial import polynomial as P
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'polynomial1_test():' )
  print ( '  Bound the roots of a specific polynomial:' )
  print ( '    12z^5 + 2z^2 + 23i.' )

  c = np.array ( [ 23.0j, 0.0, 2.0, 0.0, 0.0, 12.0 ] )
  
  b = polynomial_root_bound ( c )

  print ( '' )
  print ( '  Root magnitude bound is ', b )

  r = P.polyroots ( c )
  print ( '' )
  print ( '  Polynomial roots are:' )
  print ( r )

  plt.clf ( )
  plt.plot ( r.real, r.imag, 'b.', markersize = 20 )
  t = np.linspace ( 0.0, 2.0 * np.pi, 49 )
  cx = b * np.cos ( t )
  cy = b * np.sin ( t )
  plt.plot ( cx, cy, 'r', linewidth = 3 )
  plt.grid ( 'on' )
  plt.axis ( 'equal' )
  plt.title ( 'Polynomial #1' )
  filename = 'polynomial1_test.png'
  plt.savefig ( filename )  
  print ( '  Graphics saved as "' + filename + '"' )

  return

def polynomial2_test ( ):

#*****************************************************************************80
#
## polynomial2_test() deals with a random polynomial.
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
  from numpy.polynomial import polynomial as P
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'polynomial2_test():' )
  print ( '  Bound the roots of a random polynomial:' )

  rng = default_rng ( )

  n = 5

  r = rng.standard_normal ( size = n ) + 1j * rng.standard_normal ( size = n )
  print ( '' )
  print ( '  Polynomial roots are:' )
  print ( r )

  c = P.polyfromroots ( r )
  print ( '' )
  print ( '  Polynomial coefficients are:' )
  print ( c )

  b = polynomial_root_bound ( c )

  print ( '' )
  print ( '  Root magnitude bound is ', b )

  plt.clf ( )
  plt.plot ( r.real, r.imag, 'b.', markersize = 20 )
  t = np.linspace ( 0.0, 2.0 * np.pi, 49 )
  cx = b * np.cos ( t )
  cy = b * np.sin ( t )
  plt.plot ( cx, cy, 'r', linewidth = 3 )
  plt.grid ( 'on' )
  plt.axis ( 'equal' )
  plt.title ( 'Polynomial #2' )
  filename = 'polynomial2_test.png'
  plt.savefig ( filename )  
  print ( '  Graphics saved as "' + filename + '"' )

  return

def polynomial_root_bound ( c ):

#*****************************************************************************80
#
## polynomial_root_bound() bounds the roots of a polynomial.
#
#  Discussion:
#
#    The method is due to Cauchy, and the bound is called the Cauchy bound.
#
#    MATLAB made a counter-intuitive choice in indexing polynomial coefficients
#    with c(1) multiplying the highest order term!
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
#  Reference:
#
#    John D Cook,
#    Bounding complex roots by a positive root,
#    https://www.johndcook.com/blog/2023/12/02/cauchy-radius/
#    02 December 2023.
#
#  Input:
#
#    complex c(n+1): the coefficients of the polynomial.
#    c(1) multiplies x^n and c(n+1) is the constant term (multiplying x^0).
#
#  Output:
#
#    real b: a bound on the norm of all roots of the polynomial.
#
  from numpy.polynomial.polynomial import polyval
  import numpy as np

  n = len ( c ) - 1
#
#  If the constant term is zero, the problem reduces to finding roots of p(z)/z.
#  Shift coefficients, repeatedly if necessary.
#
  while ( True ):
#
#  Polynomial could be identically zero.
#
    if ( n + 1 <= 0 ):
      b = 0.0
      return b

    if ( c[0] != 0.0 ):
      break
#
#  Drop the constant coefficient, which is zero and reduce the order.
#
    c = c[1:n+1]
    n = n - 1
#
#  Define associated real polynomial q(x):
#    q(x) = |cn| x^(n) - |cn-1| x^(n-1) - |cn-2| x^(n-2) - ... - |c0|
#
  q = np.zeros ( n + 1 )

  for i in range ( 0, n ):
    q[i] = - np.abs ( c[i] )
  q[n] = np.abs ( c[n] )
#
#  Determine change of sign interval for Q(x).
#
  xneg = 0.0
  qneg = q[n]

  xpos = 1.0
  qpos = polyval ( xpos, q )
  while ( qpos <= 0.0 ):
    xpos = xpos * 2.0
    qpos = polyval ( xpos, q )
#
#  Use bisection to find X such that Q(X)=0.
#
  tol = 10.0 * np.finfo ( float ).eps * np.abs ( xpos - xneg )

  xneg, xpos, it = bisect ( xneg, xpos, tol, lambda x: polyval(x,q) )

  b = 0.5 * ( xneg + xpos )

  return b

def bisect ( a, b, tol, f ):

#*****************************************************************************80
#
## bisect() carries out the bisection method.
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
#    real A, B, the endpoints of a change of sign interval.
#
#    real TOL, the interval size tolerance.  Once |B-A| < TOL,
#    the iteration will stop.
#
#    pointer value=F(x), a pointer to a function.  This can be
#    an anonymous function or the name of a MATLAB M-file function.
#
#  Output:
#
#    real A, B, the new endpoints that constitute an
#    change of sign interval no larger than TOL.
#
#    integer IT, the number of bisections.
#
  import numpy as np

  fa = f ( a )
  fb = f ( b )
  it = 0

  while ( tol < np.abs ( b - a ) ):

    c = ( a + b ) / 2.0
    fc = f ( c )
    it = it + 1

    if ( 100 <= it ):
      raise Exception ( 'bisect(): too many iterations!' )

    if ( np.sign ( fc ) == np.sign ( fa ) ):
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
  polynomial_root_bound_test ( )
  timestamp ( )

