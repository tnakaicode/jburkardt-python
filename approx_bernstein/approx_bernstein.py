#! /usr/bin/env python3
#
def approx_bernstein_test ( ):

#*****************************************************************************80
#
## approx_bernstein_test() tests approx_bernstein().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'approx_bernstein_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test approx_bernstein().' )
#
#  Approximate |x-0.5| using 5, 11, and 31 basis functions.
#
  print ( '' )
  print ( '  Approximate |x-0.5| using 5, 11, and 31 basis functions:' )

  a = 0.0
  b = 1.0

  for n in [ 5, 11, 31 ]:

    xp, yp, maxerr = approx_bernstein_compute ( lambda x: np.abs(x-0.5), a, b, n )
    plt.clf ( )
    fp = np.abs ( xp - 0.5 )
    plt.plot ( xp, fp, 'b-', linewidth = 3 )
    plt.plot ( xp, yp, 'r-', linewidth = 3 )
    label = str ( n ) + '-point Bernstein Approximation'
    plt.title ( label )
    plt.grid ( True )
    if ( n == 31 ):
      filename = 'abs_bernstein.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
#
#  Approximate humps(x) using 1 through 20 basis functions,
#  and compute the maximum approximation error at 101 points.
#
  print ( '' )
  print ( '  Approximate humps(x) using 1 through 20 basis functions' )
  print ( '  and compute the maximum approximation error.' )

  a = 0.0
  b = 2.0

  m = 101
  xp = np.linspace ( a, b, m )
  fp = humps_fun ( xp )

  print ( '' )
  print ( '  N  Maxerr' )
  print ( '' )
  for n in range ( 1, 21 ):
    xp, yp, maxerr = approx_bernstein_compute ( humps_fun, a, b, n )
    print ( '  %2d  %14.6g' % ( n, maxerr ) )
#
#  Plot approximations to humps(x).
#
  print ( '' )
  print ( '  Approximate humps(x) with 1, 3, 5, 9, 17, 33, 65, 129 functions.' )

  for n in [ 1, 3, 5, 9, 17, 33, 65, 129 ]:

    xp, yp, maxerr = approx_bernstein_compute ( humps_fun, a, b, n )

    plt.clf ( )
    plt.plot ( xp, fp, 'b-', linewidth = 3 )
    plt.plot ( xp, yp, 'r-', linewidth = 3 )
    label = str ( n ) + '-point Bernstein Approximation'
    plt.title ( label )
    plt.grid ( True )
    if ( n == 129 ):
      filename = 'humps_bernstein.png'
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'approx_bernstein_test():' )
  print ( '  Normal end of execution.' )

  return

def approx_bernstein_compute ( f, a, b, n ):

#*****************************************************************************80
#
## approx_bernstein_compute() computes a Bernstein approximation.
#
#  Discussion:
#
#    This function uses n equally spaced nodes to approximate a function f(x)
#    in the interval a <= x <= b, using Bernstein polynomials.
#
#    The user enters a formula for f(x), the values of a and b,
#    and the number of equally spaced approximation points n.
#
#    The program returns a set of 101 pairs of values (xp,yp) that can be
#    used to plot the approximation polynomial.
#
#    The string specifying f(x) must be quoted:
#      [ xp, yp, maxerr ] = approx_bernstein ( 'x^2', -1, 3, 2 )
#
#    The function is specified as a string which is either:
#    * an expression using the argument 'x', 
#    * the name of an M-file followed by the argument '(x)'.
#
#    The string should not contain any spaces between symbols, except
#    when it is passed as a function argument in quotes.
#
#    Examples of function specifications:
#
#      x^2
#      x.^2
#      3/(x^4+5*x-6)
#      sin(7*x)*sqrt(x)/8
#      wiggle(x)     <-- where "wiggle.m" is a user-provided M file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string f_string: the function to be approximated.
#
#    real a, b: the interval.
#
#    integer n: the number of points to use.
#
#  Output:
#
#    real xp(*), yp(*): sample values of the approximant over [a,b].
#
#    real maxerr: an estimate for the maximum error between the
#    function f(x) and the n-point Bernstein approximant over [a,b].
#
  import numpy as np
#
#  Get the data at equally spaced points.
#
  if ( n == 1 ):
    xd = ( a + b ) / 2.0
  else:
    xd = np.linspace ( a, b, n )

  yd = f ( xd )
#
#  Estimate maximum error at 10001 points.
#
  ne = 10001
  xe = np.linspace ( a, b, ne )
  ye = bernstein_approximant ( n, a, b, yd, ne, xe )
  fe = f ( xe )
  maxerr = np.max ( abs ( ye - fe ) )
#
#  Return a small number of points for plotting.
#
  nplot = 101
  xp = np.linspace ( a, b, nplot )
  yp = bernstein_approximant ( n, a, b, yd, nplot, xp )
 
  return xp, yp, maxerr

def bernstein_approximant ( nd, a, b, yd, ne, xe ):

#*****************************************************************************80
#
## bernstein_approximant(): Bernstein polynomial approximant to F(X) on [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    David Kahaner, Cleve Moler, Steven Nash,
#    Numerical Methods and Software,
#    Prentice Hall, 1989,
#    ISBN: 0-13-627258-4,
#    LC: TA345.K34.
#
#  Input:
#
#    integer nd, the number of approximation points.
#
#    real a, b, the endpoints of the approximation interval.
#
#    real yd(nd), the data values at nd equally spaced points in [A,B].
#
#    integer ne, the number of evaluation points.
#
#    real xe(ne), the evaluation points.
#
#  Output:
#
#    real ye(ne), the Bernstein approximant values.
#
  import numpy as np

  ye = np.zeros ( ne )
  be = np.zeros ( [ ne, nd ] )

  if ( nd <= 0 ):

    return be

  elif ( nd == 1 ):

    be = np.ones ( [ ne, 1 ] )
 
  else:

    be[0:ne,0] = ( b - xe ) / ( b - a )
    be[0:ne,1] = ( xe - a ) / ( b - a )

    for j in range ( 2, nd ):

      k = j
      be[0:ne,k] = ( xe - a ) / ( b - a ) * be[0:ne,k-1]

      for k in range ( j - 1, 0, -1 ):
        be[0:ne,k] = ( xe - a ) / ( b - a ) * be[0:ne,k-1] \
                   + ( b - xe ) / ( b - a ) * be[0:ne,k]

      k = 0
      be[0:ne,k] = ( b - xe ) / ( b - a ) * be[0:ne,k]

    for j in range ( 0, nd ):
      ye[0:ne] = ye[0:ne] + yd[j] * be[0:ne,j]
 
  return ye

def humps_fun ( x ):

#*****************************************************************************80
#
## humps_fun() evaluates the humps function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 August 2019
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
  y = 1.0 / ( ( x - 0.3 )**2 + 0.01 ) \
    + 1.0 / ( ( x - 0.9 )**2 + 0.04 ) \
    - 6.0

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
  approx_bernstein_test ( )
  timestamp ( )

