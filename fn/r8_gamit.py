#! /usr/bin/env python
#
def r8_lgic ( a, x, alx ):

#*****************************************************************************80
#
## R8_LGIC evaluates the log complementary incomplete gamma function for large X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real A, the parameter.
#
#    Input, real X, the argument.
#
#    Input, real ALX, the logarithm of X.
#
#    Output, real VALUE, the log complementary incomplete
#    gamma function.
#
  import numpy as np
  from machine import r8_mach
  from sys import exit

  eps = 0.5 * r8_mach ( 3 )

  xpa = x + 1.0 - a
  xma = x - 1.0 - a

  r = 0.0
  p = 1.0
  s = p

  for k in range ( 1, 301 ):

    fk = float ( k )
    t = fk * ( a - fk ) * ( 1.0 + r )
    r = - t / ( ( xma + 2.0 * fk ) * ( xpa + 2.0 * fk ) + t )
    p = r * p
    s = s + p

    if ( abs ( p ) < eps * s ):
      value = a * alx - x + np.log ( s / xpa )
      return value

  print ( '' )
  print ( 'R8_LGIC - Fatal error!' )
  print ( '  No convergence in 300 iterations.' )

  exit ( 'R8_LGIC - Fatal error!' )

def r8_lgit ( a, x, algap1 ):

#*****************************************************************************80
#
## R8_LGIT evaluates the log of Tricomi's incomplete gamma function.
#
#  Discussion:
#
#    Perron's continued fraction is used for large X and X <= A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real A, the parameter.
#
#    Input, real X, the argument.
#
#    Input, real ALGAP1, the logarithm of the gamma function of A+1.
#
#    Output, real VALUE, the log of Tricomi's incomplete gamma function.
#
  import numpy as np
  from machine import r8_mach
  from sys import exit

  eps = 0.5 * r8_mach ( 3 )
  sqeps = np.sqrt ( r8_mach ( 4 ) )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'R8_LGIT - Fatal error!' )
    print ( '  X <= 0.' )
    exit ( 'R8_LGIT - Fatal error!' )

  if ( a < x ):
    print ( '' )
    print ( 'R8_LGIT - Fatal error!' )
    print ( '  A < X.' )
    exit ( 'R8_LGIT - Fatal error!' )

  ax = a + x
  a1x = ax + 1.0
  r = 0.0
  p = 1.0
  s = p

  for k in range ( 1, 201 ):

    fk = float ( k )
    t = ( a + fk ) * x * ( 1.0 + r )
    r = t / ( ( ax + fk ) * ( a1x + fk ) - t )
    p = r * p
    s = s + p

    if ( abs ( p ) < eps * s ):
      hstar = 1.0 - x * s / a1x
      value = - x - algap1 - np.log ( hstar )
      return value

  print ( '' )
  print ( 'R8_LGIT - Fatal error!' )
  print ( '  No convergence after 200 iterations.' )
  exit ( 'R8_LGIT - Fatal error!' )

def r8_gamit ( a, x ):

#*****************************************************************************80
#
## R8_GAMIT evaluates Tricomi's incomplete gamma function for an R8 argument.
#
#  Discussion:
#
#      GAMIT = x^(-a) / gamma(a)
#        * Integral ( 0 <= t <= x ) exp(-t) * t^(a-1) dt
#
#    with analytic continuation for a <= 0.0.  Gamma(x) is the complete
#    gamma function of X.  GAMIT is evaluated for arbitrary real values of
#    A and for non-negative values of X (even though GAMIT is defined for
#    X < 0.0).
#
#    A slight deterioration of 2 or 3 digits accuracy will occur when
#    gamit is very large or very small in absolute value, because log-
#    arithmic variables are used.  Also, if the parameter A is very close
#    to a negative integer (but not a negative integer), there is a loss
#    of accuracy.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 September 2011
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#    Walter Gautschi,
#    A Computational Procedure for Incomplete Gamma Functions,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 4, December 1979, pages 466-481.
#
#  Parameters:
#
#    Input, real A, the parameter.
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the function value.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_gamr import r8_gamr
  from r8_lgams import r8_lgams
  from r8_lngam import r8_lngam
  from machine import r8_mach
  from sys import exit

  alneps = - np.log ( r8_mach ( 3 ) )
  sqeps = np.sqrt ( r8_mach ( 4 ) )
  bot = np.log ( r8_mach ( 1 ) )

  if ( x < 0.0 ):
    print ( '' )
    print ( 'R8_GAMIT - Fatal error!' )
    print ( '  X is negative.' )
    exit ( 'R8_GAMIT - Fatal error!' )
  elif ( x == 0.0 ):
    alx = 0.0
  else:
    alx = np.log ( x )

  if ( a < 0.0 ):
    sga = - 1.0
  else:
    sga = + 1.0

  ainta = r8_aint ( a + 0.5 * sga )
  aeps = a - ainta

  if ( x == 0.0 ):
    if ( 0.0 < ainta or aeps != 0.0 ):
      value = r8_gamr ( a + 1.0 )
    else:
      value = 0.0
    return value

  if ( x <= 1.0 ):
    if ( - 0.5 <= a or aeps != 0.0 ):
      algap1, sgngam = r8_lgams ( a + 1.0 )
    value = r8_gmit ( a, x, algap1, sgngam, alx )
    return value

  if ( x <= a ):
    t = r8_lgit ( a, x, r8_lngam ( a + 1.0 ) )
    value = np.exp ( t )
    return value

  alng = r8_lgic ( a, x, alx )
#
#  Evaluate in terms of log (r8_gamic (a, x))
#
  h = 1.0

  if ( aeps != 0.0 or 0.0 < ainta ):

    algap1, sgngam = r8_lgams ( a + 1.0 )
    t = np.log ( abs ( a ) ) + alng - algap1

    if ( alneps < t ):
      t = t - a * alx
      value = - sga * sgngam * np.exp ( t )
      return value

    if ( - alneps < t ):
      h = 1.0 - sga * sgngam * np.exp ( t )

  t = - a * alx + np.log ( abs ( h ) )

  if ( h < 0.0 ):
    value = - np.exp ( t )
  else:
    value = + np.exp ( t )

  return value

def r8_gamit_test ( ):

#*****************************************************************************80
#
## R8_GAMIT_TEST tests R8_GAMIT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from gamma_inc_tricomi_values import gamma_inc_tricomi_values

  print ( '' )
  print ( 'R8_GAMIT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMIT evaluates Tricomi\'s incomplete Gamma function' )
  print ( '' )
  print ( '             A               X     GAMIT(A,X)  R8_GAMIT(A,X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, fx1 = gamma_inc_tricomi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamit ( a, x )

    print ( '  %14.4g  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( a, x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMIT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_gmit ( a, x, algap1, sgngam, alx ):

#*****************************************************************************80
#
## R8_GMIT: Tricomi's incomplete gamma function for small X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Wayne Fullerton,
#    Portable Special Function Routines,
#    in Portability of Numerical Software,
#    edited by Wayne Cowell,
#    Lecture Notes in Computer Science, Volume 57,
#    Springer 1977,
#    ISBN: 978-3-540-08446-4,
#    LC: QA297.W65.
#
#  Parameters:
#
#    Input, real A, the parameter.
#
#    Input, real X, the argument.
#
#    Input, real ALGAP1, the logarithm of Gamma ( A + 1 ).
#
#    Input, real SGNGAM, the sign of Gamma ( A + 1 ).
#
#    Input, real ALX, the logarithm of X.
#
#    Output, real VALUE, the Tricomi incomplete gamma function.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_lngam import r8_lngam
  from machine import r8_mach
  from r8_sign import r8_sign
  from sys import exit

  eps = 0.5 * r8_mach ( 3 )
  bot = np.log ( r8_mach ( 1 ) )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'R8_GMIT - Fatal error!' )
    print ( '  X <= 0.' )
    exit ( 'R8_GMIT - Fatal error!' )

  if ( a < 0.0 ):
    ma = int ( r8_aint ( a - 0.5 ) )
  else:
    ma = int ( r8_aint ( a + 0.5 ) )

  aeps = a - ma

  if ( a < - 0.5 ):
    ae = aeps
  else:
    ae = a

  t = 1.0
  te = ae
  s = t
  converged = False
  for k in range ( 1, 201 ):
    fk = float ( k )
    te = - x * te / fk
    t = te / ( ae + fk )
    s = s + t
    if ( abs ( t ) < eps * abs ( s ) ):
      converged = True
      break

  if ( not converged ):
    print ( '' )
    print ( 'R8_GMIT - Fatal error!' )
    print ( '  No convergence in 200 iterations.' )
    exit ( 'R8_GMIT - Fatal error!' )

  if ( - 0.5 <= a ):
    algs = - algap1 + np.log ( s )
    value = np.exp ( algs )
    return value

  algs = - r8_lngam ( 1.0 + aeps ) + np.log ( s )
  s = 1.0
  m = - ma - 1
  t = 1.0
  for k in range ( 1, m + 1 ):
    t = x * t / ( aeps - ( m + 1 - k ) )
    s = s + t
    if ( abs ( t ) < eps * abs ( s ) ):
      break

  value = 0.0
  algs = - ma * np.log ( x ) + algs

  if ( s == 0.0 or aeps == 0.0 ):
    value = np.exp ( algs )
    return value

  sgng2 = sgngam * r8_sign ( s )
  alg2 = - x - algap1 + np.log ( abs ( s ) )

  if ( bot < alg2 ):
    value = sgng2 * np.exp ( alg2 )

  if ( bot < algs ):
    value = value + np.exp ( algs )

  return value

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_gamit_test ( )
  timestamp ( )
