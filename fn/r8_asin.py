#! /usr/bin/env python
#
def r8_asin ( x ):

#*****************************************************************************80
#
## R8_ASIN evaluates the arc-sine of an R8 argument.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2016
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
#    Output, real VALUE, the arc-sine of X.
#
  import numpy as np
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach
  from sys import exit

  asincs = np.array ( [ \
    +0.10246391753227159336573148305785E+00, \
    +0.54946487221245833306011195902924E-01, \
    +0.40806303925449692851307056149246E-02, \
    +0.40789006854604435455598823905612E-03, \
    +0.46985367432203691616048530136218E-04, \
    +0.58809758139708058986454385552074E-05, \
    +0.77732312462777632750557528163795E-06, \
    +0.10677423340082039235047504956587E-06, \
    +0.15092399536022808262386434401064E-07, \
    +0.21809724080055385496609614713930E-08, \
    +0.32075984262789614433261959667376E-09, \
    +0.47855369646781034461493133918953E-10, \
    +0.72251287362910432263848754537112E-11, \
    +0.11018334742255783705372701334987E-11, \
    +0.16947632539203354877423745651078E-12, \
    +0.26261558667348224162283241502416E-13, \
    +0.40958299813281178408828069291110E-14, \
    +0.64244793108803655891727944887091E-15, \
    +0.10128142198228221693973361222041E-15, \
    +0.16039221897380787560050597464746E-16, \
    +0.25503501355807141715298789676373E-17, \
    +0.40701403797862382855487165672106E-18, \
    +0.65172671712881144437889267575466E-19, \
    +0.10467453037096796954244891716266E-19, \
    +0.16858725563380328094989095185066E-20, \
    +0.27221936305040227625164341247999E-21, \
    +0.44059293900347550617126830079999E-22, \
    +0.71466685243375937853063168000000E-23, \
    +0.11615793343859516051798971733333E-23, \
    +0.18915234552354685801184187733333E-24, \
    +0.30855772044244342399827968000000E-25, \
    +0.50416366022162453412970495999999E-26, \
    +0.82502725502400865081753600000000E-27, \
    +0.13520032631020947208055466666666E-27, \
    +0.22184326876541720216644266666666E-28, \
    +0.36442494054085079212578133333333E-29, \
    +0.59920218558643813307733333333333E-30, \
    +0.98584812059573785810261333333333E-31, \
    +0.16222501166399014393173333333333E-31 ] )

  nterms = r8_inits ( asincs, 39, 0.1 * r8_mach ( 3 ) )

  sqeps = np.sqrt ( 6.0 * r8_mach ( 3 ) )

  y = abs ( x )

  if ( x < - 1.0 - sqeps ):

    print ( '' )
    print ( 'R8_ASIN - Fatal error!' )
    print ( '  X < - 1.0' )
    error ( 'R8_ASIN - Fatal error!' )

  elif ( x < - 1.0 ):

    value = - 0.5 * np.pi

  elif ( x < 1.0 ):

    z = 0.0
    if ( sqeps < y ):
      z = y * y

    if ( z <= 0.5 ):
      value = x * ( 1.0 + r8_csevl ( 4.0 * z - 1.0, asincs, nterms ) )
    else:
      value = 0.5 * np.pi - np.sqrt ( 1.0 - z ) * ( 1.0 + \
        r8_csevl ( 3.0 - 4.0 * z, asincs, nterms ) )

    if ( x < 0.0 ):
      value = - abs ( value )
    elif ( 0.0 < x ):
      value = + abs ( value )

  elif ( x < 1.0 + sqeps ):

    value = 0.5 * np.pi

  else:

    print ( '' )
    print ( 'R8_ASIN - Fatal error!' )
    print ( '  1.0 < X' )
    exit ( 'R8_ASIN - Fatal error!' )

  return value

def r8_asin_test ( ):

#*****************************************************************************80
#
## R8_ASIN_TEST tests R8_ASIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from arcsin_values import arcsin_values

  print ( '' )
  print ( 'R8_ASIN_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_ASIN evaluates the arc-sine function' )
  print ( '' )
  print ( '             X      ARCSIN(X)  R8_ASIN(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arcsin_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_asin ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_ASIN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_asin_test ( )
  timestamp ( )
