#! /usr/bin/env python3
#
def glomin ( a, b, c, m, machep, e, t, f ):

#*****************************************************************************80
#
## glomin() seeks a global minimum of a function F(X) in an interval [A,B].
#
#  Discussion:
#
#    This function assumes: 
#    * F(X) is twice continuously differentiable over [A,B];
#    * F''(X) <= M for all X in [A,B];
#    * the user can supply the value of this upper bound M.
#
#    Thanks to Hans Bieshaar for supplying several corrections to the code,
#    28 May 2021
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2021
#
#  Author:
#
#    Original FORTRAN77 version by Richard Brent.
#    This version by John Burkardt.
#
#  Reference:
#
#    Richard Brent,
#    Algorithms for Minimization Without Derivatives,
#    Dover, 2002,
#    ISBN: 0-486-41998-3,
#    LC: QA402.5.B74.
#
#  Input:
#
#    real A, B, the endpoints of the interval.
#    It must be the case that A < B.
#
#    real C, an initial guess for the global
#    minimizer.  If no good guess is known, C = A or B is acceptable.
#
#    real M, the bound on the second derivative.
#
#    real MACHEP, an estimate for the relative machine
#    precision.
#
#    real E, a positive tolerance, a bound for the
#    absolute error in the evaluation of F(X) for any X in [A,B].
#
#    real T, a positive error tolerance.
#
#    function value = F ( x ), the name of a user-supplied
#    function whose global minimum is being sought.
#
#  Output:
#
#    real X, the estimated value of the abscissa
#    for which F attains its global minimum value in [A,B].
#
#    real FX, the value F(X).
#
#    integer CALLS: the number of function calls.
#
  import numpy as np

  calls = 0
  a0 = b
  x = a0
  a2 = a
  y0 = f ( b )
  calls = calls + 1
  yb = y0
  y2 = f ( a )
  calls = calls + 1
  y = y2

  if ( y0 < y ):
    y = y0
  else:
    x = a

  if ( m <= 0.0 or b <= a ):
    fx = y
    return x, fx, calls

  m2 = 0.5 * ( 1.0 + 16.0 * machep ) * m

  if ( c <= a or b <= c ):
    c = 0.5 * ( a + b )

  y1 = f ( c )
  calls = calls + 1
  k = 3
  d0 = a2 - c
  h = 9.0 / 11.0

  if ( y1 < y ):
    x = c
    y = y1

  while ( True ):

    d1 = a2 - a0
    d2 = c - a0
    z2 = b - a2
    z0 = y2 - y1
    z1 = y2 - y0
    r = d1 * d1 * z0 - d0 * d0 * z1
    p = r
    qs = 2.0 * ( d0 * z1 - d1 * z0 )
    q = qs
#
#  Loop control corrected by Hans Bieshaar, 28 May 2021.
#
    force_first = True

    if ( 100000 <= k and y < y2 ):
      k = ( ( 1611 * k ) % 1048576 )
      q = 1.0
      r = ( b - a ) * 0.00001 * float ( k )
      force_first = False

    while ( r < z2 or force_first ):

      force_first = False

      if ( q * ( r * ( yb - y2 ) + z2 * q * ( ( y2 - y ) + t ) ) < \
        z2 * m2 * r * ( z2 * q - r ) ):
        a3 = a2 + r / q
        y3 = f ( a3 )
        calls = calls + 1

        if ( y3 < y ):
          x = a3
          y = y3

      k = ( ( 1611 * k ) % 1048576 )
      q = 1.0
      r = ( b - a ) * 0.00001 * float ( k )

    r = m2 * d0 * d1 * d2
    s = np.sqrt ( ( ( y2 - y ) + t ) / m2 )
    h = 0.5 * ( 1.0 + h )
    p = h * ( p + 2.0 * r * s )
#
#  Correction by Hans Bieshaar, 27 May 2021.
#
    q = r + 0.5 * qs
    r = - 0.5 * ( d0 + ( z0 + 2.01 * e ) / ( d0 * m2 ) )

    if ( r < s or d0 < 0.0 ):
      r = a2 + s
    else:
      r = a2 + r

    if ( 0.0 < p * q ):
      a3 = a2 + p / q
    else:
      a3 = r

    while ( True ):

      a3 = max ( a3, r )

      if ( b <= a3 ):
        a3 = b
        y3 = yb
      else:
        y3 = f ( a3 )
        calls = calls + 1

      if ( y3 < y ):
        x = a3
        y = y3

      d0 = a3 - a2

      if ( a3 <= r ):
        break

      p = 2.0 * ( y2 - y3 ) / ( m * d0 )

      if ( ( 1.0 + 9.0 * machep ) * d0 <= abs ( p ) ):
        break

      if ( 0.5 * m2 * ( d0 * d0 + p * p ) <= ( y2 - y ) + ( y3 - y ) + 2.0 * t ):
        break

      a3 = 0.5 * ( a2 + a3 )
      h = 0.9 * h

    if ( b <= a3 ):
      break

    a0 = c
    c = a2
    a2 = a3
    y0 = y1
    y1 = y2
    y2 = y3

  fx = y
 
  return x, fx, calls

def glomin_test ( ):

#*****************************************************************************80
#
## glomin_test() tests glomin();
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'glomin_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  glomin() seeks a global minimizer of a' )
  print ( '  a function F(X) in an interval [A,B],' )
  print ( '  given some upper bound M for F".' )

  machep = 2.220446049250313E-016
  e = np.sqrt ( machep )
  t = np.sqrt ( machep )

  print ( '' )
  print ( '  Tolerances:' )
  print ( '  e = ', e )
  print ( '  t = ', t )

  a = 7.0
  b = 9.0
  c = ( a + b ) / 2.0
  m = 0.0

  glomin_example ( a, b, c, m, machep, e, t, h_01, 'h_01(x) = 2 - x' )

  a = 7.0
  b = 9.0
  c = ( a + b ) / 2.0
  m = 100.0

  glomin_example ( a, b, c, m, machep, e, t, h_01, 'h_01(x) = 2 - x' )

  a = -1.0
  b = +2.0
  c = ( a + b ) / 2.0
  m = 2.0

  glomin_example ( a, b, c, m, machep, e, t, h_02, 'h_02(x) = x * x' )

  a = -1.0
  b = +2.0
  c = ( a + b ) / 2.0
  m = 2.1

  glomin_example ( a, b, c, m, machep, e, t, h_02, 'h_02(x) = x * x' )

  a = -0.5
  b =  +2.0
  c = ( a + b ) / 2.0
  m = 14.0

  glomin_example ( a, b, c, m, machep, e, t, h_03, 'h_03(x) = x^3 + x^2' )

  a = -0.5
  b =  +2.0
  c = ( a + b ) / 2.0
  m = 28.0

  glomin_example ( a, b, c, m, machep, e, t, h_03, 'h_03(x) = x^3 + x^2' )

  a = -10.0
  b = +10.0
  c = ( a + b ) / 2.0
  m = 72.0

  glomin_example ( a, b, c, m, machep, e, t, h_04, \
    'h_04(x) = ( x + sin(x) ) * exp(-x*x)' )

  a = -10.0
  b = +10.0
  c = ( a + b ) / 2.0
  m = 72.0

  glomin_example ( a, b, c, m, machep, e, t, h_05, \
    'h_05(x) = ( x - sin(x) ) * exp(-x*x)' )
#
#  Terminate.
#
  print ( '' )
  print ( 'glomin_test():' )
  print ( '  Normal end of execution.' )
  return

def glomin_example ( a, b, c, m, machep, e, t, f, title ):

#*****************************************************************************80
#
## glomin_example() tests glomin() on one test function.
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
#    real A, B, the endpoints of the interval.
#
#    real C, an initial guess for the global
#    minimizer.  If no good guess is known, C = A or B is acceptable.
#
#    real M, the bound on the second derivative.
#
#    real MACHEP, an estimate for the relative machine
#    precision.
#
#    real E, a positive tolerance, a bound for the
#    absolute error in the evaluation of F(X) for any X in [A,B].
#
#    real T, a positive absolute error tolerance.
#
#    function value = F ( X ), the name of a user-supplied
#    function whose global minimum is being sought.
#
#    string TITLE, a title for the problem.
#
  x, fx, calls = glomin ( a, b, c, m, machep, e, t, f )
  fa = f ( a )
  fb = f ( b )

  print ( '' )
  print ( '  %s' % ( title ) )
  print ( '  M = ', m )
  print ( '' )
  print ( '      A                 X             B' )
  print ( '    F(A)              F(X)          F(B)' )
  print ( '' )
  print ( '  %14f  %14f  %14f' % ( a,  x,  b ) )
  print ( '  %14e  %14e  %14e' % ( fa, fx, fb ) )
  print ( '  Number of calls to F = ', calls )

  return

def h_01 ( x ):

#*****************************************************************************80
#
## h_01() evaluates 2 - x.
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
  value = 2.0 - x

  return value

def h_02 ( x ):

#*****************************************************************************80
#
## h_02() evaluates x^2.
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
  value = x * x

  return value

def h_03 ( x ):

#*****************************************************************************80
#
## h_03() evaluates x^3+x^2.
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
  value = x * x * ( x + 1.0 )

  return value

def h_04 ( x ):

#*****************************************************************************80
#
## h_04() evaluates ( x + sin ( x ) ) * exp ( - x * x ).
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

  value = ( x + np.sin ( x ) ) * np.exp ( - x * x )

  return value

def h_05 ( x ):

#*****************************************************************************80
#
## h_05() evaluates ( x - sin ( x ) ) * exp ( - x * x ).
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

  value = ( x - np.sin ( x ) ) * np.exp ( - x * x )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  glomin_test ( )
  timestamp ( )

