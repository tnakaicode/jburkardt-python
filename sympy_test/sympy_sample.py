#! /usr/bin/env python3
#
from sympy import *

def sympy_sample ( ):

#*****************************************************************************80
#
## sympy_sample() does some sample calculations with sympy()
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import sympy

  print ( '' )
  print ( 'sympy_sample():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  sympy version : ' + sympy.__version__ )
  print ( '  sympy() is a symbolic mathematics package.' )
#
#  Simple sympy commands, evaluate, specify digits.
#
  print ( '' )
  print ( '  Simple calculations:' )
  print ( '' )

  print ( pi )
  print ( pi.evalf ( ) )
  print ( pi.evalf ( 30 ) )
  print ( sqrt ( pi ).evalf ( 20 ) )
  print ( sqrt ( 600 ) )
  print ( factorial ( 20 ) )
  print ( binomial ( 100, 30 ) )
#
#  Manipulate symbolic variables.
#
  print ( '' )
  print ( '  Manipulate symbolic variables:' )
  print ( '' )

  x = symbols ( 'x' )
  expr = sqrt ( 1 - cos ( x )**2 )
  print ( expr )
  expr2 = simplify ( expr )
  print ( expr2 )
  poly = ( x + 1 ) * ( x **2 - 4 * x + 3 )
  print ( poly )
  poly / ( x - 1 )
  print ( poly / ( x - 1 ) )
#
#  Define the humps function, plot it, differentiate it.
#
  print ( '' )
  print ( '  define a function, plot it, differentiate it:' )
  print ( '' )

  humps = 100 / ( ( 10 * x - 3 )**2 + 1 ) \
        + 100 / ( ( 10 * x - 9 )**2 + 4 ) \
        - 6

  plot ( humps, ( x, 0, 2 ), show = False )

  dhumpsdx = diff ( humps, x )
  print ( dhumpsdx )
  plot ( dhumpsdx, ( x, 0, 2 ), show = False )

  d2humpsdx2 = diff ( humps, x, 2 )
  plot ( d2humpsdx2, ( x, 0, 2 ), show = False )
#
#  Definite and indefinite integrals.
#
  print ( '' )
  print ( '  definite and indefinite integrals:' )
  print ( '' )

  humps_anti = integrate ( humps )
  print ( humps_anti )

  humps_def = integrate ( humps, ( x, 0, 2 ) )
  print ( humps_def )
  print ( humps_def.evalf() )
#
#  Polynomials.
#
  print ( '' )
  print ( '  polynomials:' )
  print ( '' )

  p = x**2 - 5 * x + 6
  q = 3 * x - 2
  print ( '  p(x) = ', p )
  print ( '  p(7) = ', p.subs(x,7) )
  print ( '  p.factor() = ', p.factor() )
#
#  Limits
#
  print ( '' )
  print ( '  limits:' )
  print ( '' )

  print ( limit ( sin ( x ) / x, x, 0 ) )
#
#  Series

  print ( '' )
  print ( '  series:' )
  print ( '' )

#
  print ( series ( exp ( sin(x) ), x, 0, 4 ) )
#
#  ODE
#
  print ( '' )
  print ( '  differential equations:' )
  print ( '' )

  t = symbols ( 't' )
  y = symbols ( 'y', cls = Function )

  sol = dsolve ( y(t).diff(t) + y(t) * ( 1-y(t)), y(t) )
  print ( sol )
#
#  Linear algebra
#
  print ( '' )
  print ( '  linear algebra:' )
  print ( '' )

  A = Matrix ( [ \
    [ 2, -1, 0, 0 ], \
    [ -1, 2, -1, 0 ], \
    [  0, -1, 2, -1], \
    [  0,  0, -1, 2 ] ] )

  x = Matrix ( [ 1, 2, 3, 4 ] )

  b = A * x

  print ( b )

  A2 = Matrix ( [ \
    [ 2, -1, 0, 0, b[0] ], \
    [ -1, 2, -1, 0, b[1] ], \
    [  0, -1, 2, -1, b[2] ], \
    [  0,  0, -1, 2, b[3] ] ] )

  x0, x1, x2, x3 = symbols ( 'x0, x1, x2, x3' )
  solution = solve_linear_system ( A2, x0, x1, x2, x3 )
  print ( solution )
#
#  Terminate.
#
  print ( '' )
  print ( 'sympy_sample():' )
  print ( '  Normal end of execution.' )

  return

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
  sympy_test ( )
  timestamp ( )

