#! /usr/bin/env python
#
def r8_gamic ( a, x ):

#*****************************************************************************80
#
## R8_GAMIC evaluates the complementary incomplete gamma function.
#
#  Discussion:
#
#    GAMIC = integral ( x <= t < oo ) exp(-t) * t^(a-1) dt
#
#    GAMIC is evaluated for arbitrary real values of A and non-negative
#    values X (even though GAMIC is defined for X < 0.0), except that
#    for X = 0 and A <= 0.0, GAMIC is undefined.
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
#    Walter Gautschi,
#    A Computational Procedure for Incomplete Gamma Functions,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 4, December 1979, pages 466-481.
#
#  Parameters:
#
#    Input, real A, the parameter.
#
#    Input, real X, the evaluation point.
#
#    Output, real VALUE, the value of the incomplete gamma function.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_gamit import r8_gmit
  from r8_lgams import r8_lgams
  from r8_gamit import r8_lgic
  from r8_gamit import r8_lgit
  from r8_lngam import r8_lngam
  from machine import r8_mach
  from r8_sign import r8_sign

  eps = 0.5 * r8_mach ( 3 )
  sqeps = np.sqrt ( r8_mach ( 4 ) )
  alneps = - np.log ( r8_mach ( 3 ) )
  bot = np.log ( r8_mach ( 1 ) )

  if ( x < 0.0 ):
    print ( '' )
    print ( 'R8_GAMIC - Fatal error!' )
    print ( '  X < 0.' )
    exit ( 'R8_GAMIC - Fatal error!' )

  if ( x == 0.0 ):

    if ( a <= 0.0 ):
      print ( '' )
      print ( 'R8_GAMIC - Fatal error!' )
      print ( '  X = 0 and A <= 0.' )
      exit ( 'R8_GAMIC - Fatal error!' )

    value = np.exp ( r8_lngam ( a + 1.0 ) - np.log ( a ) )

    return value

  alx = np.log ( x )

  if ( a < 0.0 ):
    sga = - 1.0
  else:
    sga = + 1.0

  ainta = r8_aint ( a + 0.5 * sga )
  aeps = a - ainta

  izero = 0

  if ( x < 1.0 ):

    if ( a <= 0.5 and abs ( aeps ) <= 0.001 ):

      if ( - ainta <= 1.0 ):
        e = 2.0
      else:
        e = 2.0 * ( - ainta + 2.0 ) / ( ainta * ainta - 1.0 )

      e = e - alx * x ** ( - 0.001 )

      if ( e * abs ( aeps ) <= eps ):
        value = r8_gmic ( a, x, alx )
        return value

    algap1, sgngam = r8_lgams ( a + 1.0 )
    gstar = r8_gmit ( a, x, algap1, sgngam, alx )

    if ( gstar == 0.0 ):
      izero = 1
    else:
      alngs = np.log ( abs ( gstar ) )
      sgngs = r8_sign ( gstar )

  else:

    if ( a < x ):
      value = np.exp ( r8_lgic ( a, x, alx ) )
      return value

    sgngam = 1.0
    algap1 = r8_lngam ( a + 1.0 )
    sgngs = 1.0
    alngs = r8_lgit ( a, x, algap1 )

  h = 1.0

  if ( izero != 1 ):

    t = a * alx + alngs

    if ( alneps < t ):
      sgng = - sgngs * sga * sgngam
      t = t + algap1 - np.log ( abs ( a ) )
      value = sgng * np.exp ( t )
      return value

    if ( - alneps < t ):
      h = 1.0 - sgngs * np.exp ( t )

  sgng = r8_sign ( h ) * sga * sgngam
  t = np.log ( abs ( h ) ) + algap1 - np.log ( abs ( a ) )
  value = sgng * np.exp ( t )

  return value

def r8_gamic_test ( ):

#*****************************************************************************80
#
#% R8_GAMIC_TEST tests R8_GAMIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from gamma_inc_values import gamma_inc_values

  print ( '' )
  print ( 'R8_GAMIC_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMIC evaluates the incomplete Gamma function.' )
  print ( '' )
  print ( '             A               X     GAMIC(A,X)  R8_GAMIC(A,X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, fx1 = gamma_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamic ( a, x )

    print ( '  %14.4g  %14.4f  %14.6g  %14.6g  %14.6g' \
      % ( a, x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMIC_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_gmic ( a, x, alx ):

#*****************************************************************************80
#
## R8_GMIC: complementary incomplete gamma, small X, A near negative integer.
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
#    Output, real VALUE, the complementary incomplete
#    gamma function.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_lngam import r8_lngam
  from machine import r8_mach
  from r8_sign import r8_sign
  from sys import exit

  euler = 0.57721566490153286060651209008240

  eps = 0.5 * r8_mach ( 3 )
  bot = np.log ( r8_mach ( 1 ) )

  if ( 0.0 < a ):
    print ( '' )
    print ( 'R8_GMIC - Fatal error!' )
    print ( '  A must be near a negative integer.' )
    exit ( 'R8_GMIC - Fatal error!' )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'R8_GMIC - Fatal error!' )
    print ( '  X <= 0.' )
    exit ( 'R8_GMIC - Fatal error!' )

  m = - int ( r8_aint ( a - 0.5 ) )
  fm = float ( m )

  te = 1.0
  t = 1.0
  s = t
  converged = False

  for k in range ( 1, 201 ):

    fkp1 = float ( k + 1 )
    te = - x * te / ( fm + fkp1 )
    t = te / fkp1
    s = s + t

    if ( abs ( t ) < eps * s ):
      converged = True
      break

  if ( not converged ):
    print ( '' )
    print ( 'R8_GMIC - Fatal error!' )
    print ( '  No convergence after 200 iterations.' )
    exit ( 'R8_GMIC - Fatal error!' )

  value = - alx - euler + x * s / ( fm + 1.0 )

  if ( m == 0 ):
    return value
  elif ( m == 1 ):
    value = - value - 1.0 + 1.0 / x
    return value

  te = fm
  t = 1.0
  s = t
  mm1 = m - 1

  for k in range ( 1, mm1 + 1 ):

    fk = float ( k )
    te = - x * te / fk
    t = te / ( fm - fk )
    s = s + t

    if ( abs ( t ) < eps * abs ( s ) ):
      break

  for k in range ( 1, m + 1 ):
    value = value + 1.0 / float ( k )

  if ( ( m % 2 ) == 1 ):
    sgng = - 1.0
  else:
    sgng = + 1.0

  alng = np.log ( value ) - r8_lngam ( fm + 1.0 )

  if ( bot < alng ):
    value = sgng * np.exp ( alng )
  else:
    value = 0.0

  if ( s != 0.0 ):
    value = value + abs ( np.exp ( - fm * alx + np.log ( abs ( s ) / fm ) ) ) * r8_sign ( s )

  return value

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_gamic_test ( )
  timestamp ( )

