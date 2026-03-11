#! /usr/bin/env python3
#
def zero_chandrupatla_test ( ):

#*****************************************************************************80
#
## zero_chandrupatla_test() tests zero_chandrupatla().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'zero_chandrupatla_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  zero_chandrupatla() seeks a root of a function f(x)' )
  print ( '  in an interval [a,b].' )

  f = f_01
  a = 2.0
  b = 3.0
  title = 'f_01(x) = x^3 - 2 x - 5'
  zero_chandrupatla_example ( f, a, b, title )

  f = f_02
  a = 0.5
  b = 1.51
  title = 'f_02(x) = 1 - 1/x^2'
  zero_chandrupatla_example ( f, a, b, title )

  f = f_03
  a = 0.0
  b = 5.0
  title = 'f_03(x) = ( x - 3 )^3'
  zero_chandrupatla_example ( f, a, b, title )

  f = f_04
  a = 0.0
  b = 5.0
  title = 'f_04(x) = 6 * ( x - 2 )^5'
  zero_chandrupatla_example ( f, a, b, title )

  f = f_05
  a = -1.0
  b = 4.0
  title = 'f_05(x) = x^9'
  zero_chandrupatla_example ( f, a, b, title )

  f = f_06
  a = -1.0
  b = 4.0
  title = 'f_06(x) = x^19'
  zero_chandrupatla_example ( f, a, b, title )

  f = f_07
  a = -1.0
  b = 4.0
  title = 'f_07(x) = x e^(-1/x2)'
  zero_chandrupatla_example ( f, a, b, title )

  f = f_08
  a = 0.0002
  b = 2.0
  title = 'f_08(x) = -(3062(1-xi)e^(-x)/(xi+(1-xi)e^(-x)) - 1013 + 1628/x'
  zero_chandrupatla_example ( f, a, b, title )

  f = f_09
  a = 0.0002
  b = 1.0
  title = 'f_09(x) = e^x - 2 - 0.01/x^2 + 0.000002/x^3'
  zero_chandrupatla_example ( f, a, b, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'zero_chandrupatla_test():' )
  print ( '  Normal end of execution.' )

  return

def zero_chandrupatla ( f, x1, x2 ):

#*****************************************************************************80
#
## zero_chandrupatla() seeks a zero of a function using Chandrupatla's algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2024
#
#  Author:
#
#    Original QBASIC version by Tirupathi Chandrupatla.
#    This version by John Burkardt.
#
#  Reference:
#
#    Tirupathi Chandrupatla,
#    A new hybrid quadratic/bisection algorithm for finding the zero of a
#    nonlinear function without using derivatives,
#    Advances in Engineering Software,
#    Volume 28, Number 3, pages 145-149, 1997.
#
#  Input:
#
#    function f ( x ): the name of the user-supplied function.
#
#    real a, b: the endpoints of the change of sign interval.
#
#  Output:
#
#    real z, fz: the estimated root and its function value.
#
#    integer calls: the number of function calls.
#
  import numpy as np

  epsilon = 1.0E-10
  delta = 0.00001

  f1 = f ( x1 )
  f2 = f ( x2 )
  calls = 2

  t = 0.5

  while ( True ):

    x0 = x1 + t * ( x2 - x1 )
    f0 = f ( x0 )
    calls = calls + 1
#
#  Arrange 2-1-3: 2-1 Interval, 1 Middle, 3 Discarded point.
#
    if ( np.sign ( f0 ) == np.sign ( f1 ) ):
      x3 = x1
      f3 = f1
      x1 = x0
      f1 = f0
    else:
      x3 = x2
      f3 = f2
      x2 = x1
      f2 = f1
      x1 = x0
      f1 = f0
#
#  Identify the one that approximates zero.
#
    if ( abs ( f2 ) < abs ( f1 ) ):
      xm = x2
      fm = f2
    else:
      xm = x1
      fm = f1

    tol = 2.0 * epsilon * abs ( xm ) + 0.5 * delta
    tl = tol / abs ( x2 - x1 )

    if ( 0.5 < tl or fm == 0.0 ):
      break
#
#  If inverse quadratic interpolation holds, use it.
#
    xi = ( x1 - x2 ) / ( x3 - x2 )
    ph = ( f1 - f2 ) / ( f3 - f2 )
    fl = 1.0 - np.sqrt ( 1.0 - xi )
    fh = np.sqrt ( xi )

    if ( fl < ph and ph < fh ):
      al = ( x3 - x1 ) / ( x2 - x1 )
      a = f1 / ( f2 - f1 )
      b = f3 / ( f2 - f3 )
      c = f1 / ( f3 - f1 )
      d = f2 / ( f3 - f2 )
      t = a * b + c * d * al
    else:
      t = 0.5
#
#  Adjust T away from the interval boundary.
#
    t = max ( t, tl )
    t = min ( t, 1.0 - tl )

  return xm, fm, calls

def zero_chandrupatla_example ( f, a, b, title ):

#*****************************************************************************80
#
## zero_chandrupatla_example() tests zero_chandrupatla() on a test function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 March 2024
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
#    string title: a title for the problem.
#
  z, fz, calls = zero_chandrupatla ( f, a, b )

  fz = f ( z )
  fa = f ( a )
  fb = f ( b )

  print ( '' )
  print ( title )
  print ( '' )
  print ( '      A                 Z             B' )
  print ( '    F(A)              F(Z)          F(B)' )
  print ( '' )
  print ( '  %14f  %14f  %14f' % ( a,  z,  b ) )
  print ( '  %14e  %14e  %14e' % ( fa, fz, fb ) )
  print ( '  Number of calls to F = ', calls )

  return

def f_01 ( x ):

  fx = x**3 - 2.0 * x - 5.0

  return fx

def f_02 ( x ):

  fx = 1 - 1.0 / x**2

  return fx

def f_03 ( x ):

  fx = ( x - 3.0 )**3

  return fx

def f_04 ( x ):

  fx = 6.0 * ( x - 2.0 )**5

  return fx

def f_05 ( x ):

  fx = x**9

  return fx

def f_06 ( x ):

  fx = x**19

  return fx

def f_07 ( x ):

  import numpy as np

  if ( abs ( x ) < 3.8E-04 ):
    fx = 0.0
  else:
    fx = x * np.exp ( - ( 1.0 / x**2 ) )

  return fx

def f_08 ( x ):

  import numpy as np

  xi = 0.61489
  top = ( 3062.0 * ( 1.0 - xi ) * np.exp ( - x ) )
  bot = ( xi + ( 1.0 - xi ) * np.exp ( - x ) )

  fx = - top / bot - 1013.0 + 1628.0 / x

  return fx

def f_09 ( x ):

  import numpy as np

  fx = np.exp ( x ) - 2.0 - 0.01 / x**2 + 0.000002 / x**3

  return fx

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
  zero_chandrupatla_test ( )
  timestamp ( )

