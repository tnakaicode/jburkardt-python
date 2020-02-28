#! /usr/bin/env python
#
def r8_cos ( x ):

#*****************************************************************************80
#
## R8_COS evaluates the cosine of an R8 argument.
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
#    Input, real X, the argument.
#
#    Output, real VALUE, the cosine of X.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach
#
#  pihi + pilo = pi.  pihi is exactly representable on all machines
#  with at least 8 bits of precision.  whether it is exactly
#  represented depends on the compiler.  this routine is more
#  accurate if it is exactly represented.
#
  pi2 = 1.57079632679489661923132169163975
  pi2rec = 0.63661977236758134307553505349006
  pihi = 3.140625
  pilo = 9.6765358979323846264338327950288E-04
  pirec = 0.31830988618379067153776752674503

  sincs = np.array ( [ \
      -0.374991154955873175839919279977323464, \
      -0.181603155237250201863830316158004754, \
      +0.005804709274598633559427341722857921, \
      -0.000086954311779340757113212316353178, \
      +0.000000754370148088851481006839927030, \
      -0.000000004267129665055961107126829906, \
      +0.000000000016980422945488168181824792, \
      -0.000000000000050120578889961870929524, \
      +0.000000000000000114101026680010675628, \
      -0.000000000000000000206437504424783134, \
      +0.000000000000000000000303969595918706, \
      -0.000000000000000000000000371357734157, \
      +0.000000000000000000000000000382486123, \
      -0.000000000000000000000000000000336623, \
      +0.000000000000000000000000000000000256 ] )

  ntsn = r8_inits ( sincs, 15, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( 2.0 * r8_mach ( 3 ) )
  xmax = 1.0 / r8_mach ( 4 )
  xwarn = np.sqrt ( xmax )

  absx = abs ( x )
  y = absx + pi2

  if ( xmax < y ):
    print ( '' )
    print ( 'R8_COS - Warning!' )
    print ( '  No precision because |X| is big.' )
    value = 0.0
    return value

  if ( xwarn < y ):
    print ( '' )
    print ( 'R8_COS - Warning!' )
    print ( '  Answer < half precision because |X| is big.' )

  value = 1.0

  if ( absx < xsml ):
    return value

  xn = r8_aint ( y * pirec + 0.5 )
  n2 = r8_aint ( ( xn % 2.0 ) + 0.5 )
  xn = xn - 0.5
  f = ( absx - xn * pihi ) - xn * pilo

  xn = 2.0 * ( f * pi2rec ) * ( f * pi2rec ) - 1.0

  value = f + f * r8_csevl ( xn, sincs, ntsn )

  if ( n2 != 0 ):
    value = - value

  if ( value < -1.0 ):
    value = -1.0
  elif ( 1.0 < value ):
    value = 1.0

  return value

def r8_cos_test ( ):

#*****************************************************************************80
#
## R8_COS_TEST tests R8_COS.
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
  from cos_values import cos_values

  print ( '' )
  print ( 'R8_COS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_COS evaluates the cosine function.' )
  print ( '' )
  print ( '             X         COS(X)  R8_COS(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cos_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cos ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_COS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_cos_test ( )
  timestamp ( )

