#! /usr/bin/env python
#
def r8_asinh ( x ):

#*****************************************************************************80
#
## R8_ASINH evaluates the arc-sine of an R8 argument.
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
#    Output, real VALUE, the arc-hyperbolic sine of X.
#
  import numpy as np
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach

  asnhcs = np.array ( [ \
      -0.12820039911738186343372127359268E+00, \
      -0.58811761189951767565211757138362E-01, \
      +0.47274654322124815640725249756029E-02, \
      -0.49383631626536172101360174790273E-03, \
      +0.58506207058557412287494835259321E-04, \
      -0.74669983289313681354755069217188E-05, \
      +0.10011693583558199265966192015812E-05, \
      -0.13903543858708333608616472258886E-06, \
      +0.19823169483172793547317360237148E-07, \
      -0.28847468417848843612747272800317E-08, \
      +0.42672965467159937953457514995907E-09, \
      -0.63976084654366357868752632309681E-10, \
      +0.96991686089064704147878293131179E-11, \
      -0.14844276972043770830246658365696E-11, \
      +0.22903737939027447988040184378983E-12, \
      -0.35588395132732645159978942651310E-13, \
      +0.55639694080056789953374539088554E-14, \
      -0.87462509599624678045666593520162E-15, \
      +0.13815248844526692155868802298129E-15, \
      -0.21916688282900363984955142264149E-16, \
      +0.34904658524827565638313923706880E-17, \
      -0.55785788400895742439630157032106E-18, \
      +0.89445146617134012551050882798933E-19, \
      -0.14383426346571317305551845239466E-19, \
      +0.23191811872169963036326144682666E-20, \
      -0.37487007953314343674570604543999E-21, \
      +0.60732109822064279404549242880000E-22, \
      -0.98599402764633583177370173440000E-23, \
      +0.16039217452788496315232638293333E-23, \
      -0.26138847350287686596716134399999E-24, \
      +0.42670849606857390833358165333333E-25, \
      -0.69770217039185243299730773333333E-26, \
      +0.11425088336806858659812693333333E-26, \
      -0.18735292078860968933021013333333E-27, \
      +0.30763584414464922794065920000000E-28, \
      -0.50577364031639824787046399999999E-29, \
      +0.83250754712689142224213333333333E-30, \
      -0.13718457282501044163925333333333E-30, \
      +0.22629868426552784104106666666666E-31 ] )

  nterms = r8_inits ( asnhcs, 39, 0.1 * r8_mach ( 3 ) )
  aln2 = 0.69314718055994530941723212145818
  sqeps = np.sqrt ( r8_mach ( 3 ) )
  xmax = 1.0 / sqeps
 
  y = abs ( x )

  if ( y <= sqeps ):
    value = x
  elif ( y <= 1.0 ):
    value = x * ( 1.0 + r8_csevl ( 2.0 * x * x - 1.0, asnhcs, nterms ) )
  elif ( y < xmax ):
    value = np.log ( y + np.sqrt ( y * y + 1.0 ) )
    if ( x < 0.0 ):
      value = - value
  else:
    value = aln2 + np.log ( y )
    if ( x < 0.0 ):
      value = - value

  return value

def r8_asinh_test ( ):

#*****************************************************************************80
#
## R8_ASINH_TEST tests R8_ASINH.
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
  from arcsinh_values import arcsinh_values

  print ( '' )
  print ( 'R8_ASINH_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_ASINH evaluates the arc hyperbolic sine function' )
  print ( '' )
  print ( '             X     ARCSINH(X)  R8_ASINH(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arcsinh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_asinh ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_ASINH_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_asinh_test ( )
  timestamp ( )

