#! /usr/bin/env python
#
def r8_atan ( x ):

#*****************************************************************************80
#
## R8_ATAN evaluates the arc-tangent of an R8 argument.
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
#    Output, real VALUE, the arc-tangent of X.
#
  import numpy as np
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach

  atancs = np.array ( [ \
    +0.48690110349241406474636915902891E+00, \
    -0.65108316367174641818869794945974E-02, \
    +0.38345828265245177653569992430456E-04, \
    -0.26872212876223146539595410518788E-06, \
    +0.20500930985824269846636514686688E-08, \
    -0.16450717395484269455734135285348E-10, \
    +0.13650975274390773423813528484428E-12, \
    -0.11601779591998246322891309834666E-14, \
    +0.10038333943866273835797657402666E-16, \
    -0.88072747152163859327073696000000E-19, \
    +0.78136321005661722180580266666666E-21, \
    -0.69954535148267456086613333333333E-23, \
    +0.63105905713702136004266666666666E-25, \
    -0.57296075370213874346666666666666E-27, \
    +0.52274796280602282666666666666666E-29, \
    -0.48327903911608320000000000000000E-31 ] )

  conpi8 = np.array ( [ \
    0.375, \
    0.75, \
    1.125, \
    1.5 ] )

  pi8 = np.array ( [ \
    +0.17699081698724154807830422909937E-01, \
    +0.35398163397448309615660845819875E-01, \
    +0.53097245096172464423491268729813E-01, \
    +0.70796326794896619231321691639751E-01 ] )

  tanp8 = np.array ( [ \
    +0.41421356237309504880168872420969, \
    +1.0, \
    +2.4142135623730950488016887242096 ] )

  xbnd1 = +0.19891236737965800691159762264467
  xbnd2 = +0.66817863791929891999775768652308
  xbnd3 = +1.4966057626654890176011351349424
  xbnd4 = +5.0273394921258481045149750710640
  nterms = r8_inits ( atancs, 16, 0.1 * r8_mach ( 3 ) )
  sqeps = np.sqrt ( 6.0 * r8_mach ( 3 ) )
  xbig = 1.0 / r8_mach ( 3 )

  y = abs ( x )

  if ( y <= xbnd1 ):

    value = x
    if ( sqeps < y ):
      value = x * ( 0.75 + r8_csevl ( 50.0 * y * y - 1.0, atancs, nterms ) )

  elif ( y <= xbnd4 ):

    if ( xbnd3 < y ):
      n = 3
    elif ( xbnd2 < y ):
      n = 2
    else:
      n = 1

    t = ( y - tanp8[n-1] ) / ( 1.0 + y * tanp8[n-1] )

    value = conpi8[n-1] + ( pi8[n-1] + t * ( 0.75 + \
      r8_csevl ( 50.0 * t * t - 1.0, atancs, nterms ) ) )

  else:

    value = conpi8[3] + pi8[3]

    if ( y < xbig ):
      value = conpi8[3] + ( pi8[3] - ( 0.75 + \
        r8_csevl ( 50.0 / y / y - 1.0, atancs, nterms ) ) / y )

  if ( x < 0.0 ):
    value = - abs ( value )
  else:
    value = + abs ( value )

  return value


def r8_atan_test ( ):

#*****************************************************************************80
#
## R8_ATAN_TEST tests R8_ATAN.
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
  from arctan_values import arctan_values

  print ( '' )
  print ( 'R8_ATAN_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_ATAN evaluates the arc tangent function.' )
  print ( '' )
  print ( '             X      ARCTAN(X)  R8_ATAN(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arctan_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_atan ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_ATAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_atan_test ( )
  timestamp ( )
