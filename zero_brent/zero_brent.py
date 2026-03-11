#! /usr/bin/env python3
#
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

def zero_brent ( a, b, t, f ):

#*****************************************************************************80
#
## zero_brent() seeks a root of a function F(X) in an interval [A,B].
#
#  Discussion:
#
#    The interval [A,B] must be a change of sign interval for F.
#    That is, F(A) and F(B) must be of opposite signs.  Then
#    assuming that F is continuous implies the existence of at least
#    one value C between A and B for which F(C) = 0.
#
#    The location of the zero is determined to within an accuracy
#    of 4 * EPSILON * abs ( C ) + 2 * T.
#
#    Thanks to Thomas Secretin for pointing out a transcription error in the
#    setting of the value of P, 11 February 2013.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2024
#
#  Author:
#
#    Original FORTRAN77 version by Richard Brent
#    This version by John Burkardt
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
#    real A, B: the endpoints of the change of sign interval.
#
#    real T, a positive error tolerance.
#
#    function F ( x ), evaluates the function whose zero is being sought.
#
#  Output:
#
#    real VALUE, the estimated value of a zero of the function F.
#
#    integer CALLS: the number of calls to F.
#
  import sys

  calls = 0
  eps = sys.float_info.epsilon
#
#  Make local copies of A and B.
#
  sa = a
  fa = f ( sa )
  calls = calls + 1

  sb = b
  fb = f ( sb )
  calls = calls + 1

  c = sa
  fc = fa
  e = sb - sa
  d = e

  while ( True ):

    if ( abs ( fc ) < abs ( fb ) ):

      sa = sb
      sb = c
      c = sa
      fa = fb
      fb = fc
      fc = fa

    tol = 2.0 * eps * abs ( sb ) + t
    m = 0.5 * ( c - sb )

    if ( abs ( m ) <= tol or fb == 0.0 ):
      break

    if ( abs ( e ) < tol or abs ( fa ) <= abs ( fb ) ):

      e = m
      d = e

    else:

      s = fb / fa

      if ( sa == c ):

        p = 2.0 * m * s
        q = 1.0 - s

      else:

        q = fa / fc
        r = fb / fc
        p = s * ( 2.0 * m * q * ( q - r ) - ( sb - sa ) * ( r - 1.0 ) )
        q = ( q - 1.0 ) * ( r - 1.0 ) * ( s - 1.0 )

      if ( 0.0 < p ):
        q = - q
      else:
        p = - p

      s = e
      e = d

      if ( 2.0 * p < 3.0 * m * q - abs ( tol * q ) and p < abs ( 0.5 * s * q ) ):
        d = p / q
      else:
        e = m
        d = e

    sa = sb
    fa = fb

    if ( tol < abs ( d ) ):
      sb = sb + d
    elif ( 0.0 < m ):
      sb = sb + tol
    else:
      sb = sb - tol

    fb = f ( sb )
    calls = calls + 1

    if ( ( 0.0 < fb and 0.0 < fc ) or ( fb <= 0.0 and fc <= 0.0 ) ):
      c = sa
      fc = fa
      e = sb - sa
      d = e

  value = sb

  return value, calls

def zero_example ( a, b, f, title ):

#*****************************************************************************80
#
## zero_example tests zero_brent() on one test function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the endpoints of the interval.
#
#    function value = F ( X ), the function whose zero is being sought.
#
#    string TITLE, a title for the problem.
#
  import numpy as np
  import sys

  eps = sys.float_info.epsilon
  t = np.sqrt ( eps )

  x, calls = zero_brent ( a, b, t, f )
  fa = f ( a )
  fx = f ( x )
  fb = f ( b )

  print ( '' )
  print ( '  ' + title )
  print ( '' )
  print ( '      A                 X             B' )
  print ( '    F(A)              F(X)          F(B)' )
  print ( '' )
  print ( '  %14f  %14f  %14f' % ( a,  x,  b ) )
  print ( '  %14e  %14e  %14e' % ( fa, fx, fb ) )
  print ( '  Number of calls to F = ', calls )

  return

def zero_brent_test ( ):

#*****************************************************************************80
#
## zero_brent_test() tests zero_brent();
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'zero_brent_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  zero_brent() seeks a root X of a function F()' )
  print ( '  in an interval [A,B].' )

  a = 1.0
  b = 2.0
  f = f_01
  title = 'f_01(x) = sin ( x ) - x / 2'
  zero_example ( a, b, f, title ) 

  a = 0.0
  b = 1.0
  f = f_02
  title = 'f_02(x) = 2 * x - exp ( - x )'
  zero_example ( a, b, f, title ) 

  a = -1.0
  b =  0.5
  f = f_03
  title = 'f_03(x) = x * exp ( - x )'
  zero_example ( a, b, f, title ) 

  a =  0.0001
  b =  20.0
  f = f_04
  title = 'f_04(x) = exp ( x ) - 1 / ( 100 * x * x )'
  zero_example ( a, b, f, title ) 

  a = -5.0
  b =  2.0
  f = f_05
  title = 'f_05(x) = (x+3) * (x-1) * (x-1)'
  zero_example ( a, b, f, title ) 
#
#  Terminate.
#
  print ( '' )
  print ( 'zero_brent_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  zero_brent_test ( )
  timestamp ( )

