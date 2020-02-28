#! /usr/bin/env python
#
def r8_gamma ( x ):

#*****************************************************************************80
#
## R8_GAMMA evaluates the gamma function of an R8 argument.
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
#    Output, real VALUE, the gamma function of X.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_csevl import r8_csevl
  from r8_gaml import r8_gaml
  from r8_lgmc import r8_lgmc
  from r8_inits import r8_inits
  from machine import r8_mach
  from sys import exit

  sq2pil = 0.91893853320467274178032973640562

  gcs = np.array ( [ \
      +0.8571195590989331421920062399942E-02, \
      +0.4415381324841006757191315771652E-02, \
      +0.5685043681599363378632664588789E-01, \
      -0.4219835396418560501012500186624E-02, \
      +0.1326808181212460220584006796352E-02, \
      -0.1893024529798880432523947023886E-03, \
      +0.3606925327441245256578082217225E-04, \
      -0.6056761904460864218485548290365E-05, \
      +0.1055829546302283344731823509093E-05, \
      -0.1811967365542384048291855891166E-06, \
      +0.3117724964715322277790254593169E-07, \
      -0.5354219639019687140874081024347E-08, \
      +0.9193275519859588946887786825940E-09, \
      -0.1577941280288339761767423273953E-09, \
      +0.2707980622934954543266540433089E-10, \
      -0.4646818653825730144081661058933E-11, \
      +0.7973350192007419656460767175359E-12, \
      -0.1368078209830916025799499172309E-12, \
      +0.2347319486563800657233471771688E-13, \
      -0.4027432614949066932766570534699E-14, \
      +0.6910051747372100912138336975257E-15, \
      -0.1185584500221992907052387126192E-15, \
      +0.2034148542496373955201026051932E-16, \
      -0.3490054341717405849274012949108E-17, \
      +0.5987993856485305567135051066026E-18, \
      -0.1027378057872228074490069778431E-18, \
      +0.1762702816060529824942759660748E-19, \
      -0.3024320653735306260958772112042E-20, \
      +0.5188914660218397839717833550506E-21, \
      -0.8902770842456576692449251601066E-22, \
      +0.1527474068493342602274596891306E-22, \
      -0.2620731256187362900257328332799E-23, \
      +0.4496464047830538670331046570666E-24, \
      -0.7714712731336877911703901525333E-25, \
      +0.1323635453126044036486572714666E-25, \
      -0.2270999412942928816702313813333E-26, \
      +0.3896418998003991449320816639999E-27, \
      -0.6685198115125953327792127999999E-28, \
      +0.1146998663140024384347613866666E-28, \
      -0.1967938586345134677295103999999E-29, \
      +0.3376448816585338090334890666666E-30, \
      -0.5793070335782135784625493333333E-31 ] )

  ngcs = r8_inits ( gcs, 42, 0.1 * r8_mach ( 3 ) )
  xmin, xmax = r8_gaml ( )
  xsml = np.exp ( max ( np.log ( r8_mach ( 1 ) ), \
    - np.log ( r8_mach ( 2 ) ) ) + 0.01 )
  dxrel = np.sqrt ( r8_mach ( 4 ) )

  y = abs ( x )

  if ( y <= 10.0 ):

    n = int ( r8_aint ( x ) )

    if ( x < 0.0 ):
      n = n - 1

    y = x - n
    n = n - 1
    value = 0.9375 + r8_csevl ( 2.0 * y - 1.0, gcs, ngcs )

    if ( n == 0 ):

      return value

    elif ( n < 0 ):

      n = - n

      if ( x == 0.0 ):
        print ( '' )
        print ( 'R8_GAMMA - Fatal error!' )
        print ( '  X is 0.' )
        exit ( 'R8_GAMMA - Fatal error!' )

      if ( x < 0.0 and x + n - 2 == 0.0 ):
        print ( '' )
        print ( 'R8_GAMMA - Fatal error!' )
        print ( '  X is a negative integer.' )
        exit ( 'R8_GAMMA - Fatal error!' )


      if ( x < - 0.5 and abs ( ( x - r8_aint ( x - 0.5 ) ) / x ) < dxrel ):
        print ( '' )
        print ( 'R8_GAMMA - Warning!' )
        print ( '  X too near a negative integer,' )
        print ( '  answer is half precision.' )

      if ( y < xsml ):
        print ( '' )
        print ( 'R8_GAMMA - Fatal error!' )
        print ( '  X is so close to zero that Gamma overflows.' )
        exit ( 'R8_GAMMA - Fatal error!' )

      for i in range ( 1, n + 1 ):
        value = value / ( x + i - 1 )

    elif ( n == 0 ):

      pass

    else:

      for i in range ( 1, n + 1 ):
        value = ( y + i ) * value

  else:

    if ( xmax < x ):
      print ( '' )
      print ( 'R8_GAMMA - Fatal error!' )
      print ( '  X so big that Gamma overflows.' )
      exit ( 'R8_GAMMA - Fatal error!' )
#
#  Underflow.
#
    if ( x < xmin ):
      value = 0.0
      return value

    value = np.exp ( ( y - 0.5 ) * np.log ( y ) - y + sq2pil + r8_lgmc ( y ) )

    if ( 0.0 < x ):
      return value

    if ( abs ( ( x - r8_aint ( x - 0.5 ) ) / x ) < dxrel ):
      print ( '' )
      print ( 'R8_GAMMA - Warning!' )
      print ( '  X too near a negative integer,' )
      print ( '  answer is half precision.' )

    sinpiy = sin ( np.pi * y )

    if ( sinpiy == 0.0 ):
      print ( '' )
      print ( 'R8_GAMMA - Fatal error!' )
      print ( '  X is a negative integer.' )
      exit ( 'R8_GAMMA - Fatal error!' )

    value = - np.pi / ( y * sinpiy * value )

  return value

def r8_gamma_test ( ):

#*****************************************************************************80
#
## R8_GAMMA_TEST tests R8_GAMMA.
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
  from gamma_values import gamma_values

  print ( '' )
  print ( 'R8_GAMMA_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMMA computes the Gamma function.' )
  print ( '' )
  print ( '             X        GAMMA(X)  R8_GAMMA(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamma ( x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMMA_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_gamma_test ( )
  timestamp ( )


