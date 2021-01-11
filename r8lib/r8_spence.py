#! /usr/bin/env python
#
def r8_spence ( x ):

#*****************************************************************************80
#
## R8_SPENCE evaluates a form of Spence's function for an R8 argument.
#
#  Discussion:
#
#    This function evaluates a form of Spence's function defined by
#
#      f(x) = Integral ( 0 <= y <= x ) - log ( abs ( 1 - y ) ) / y dy
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2011
#
#  Author:
#
#    Original FORTRAN77 version by Wayne Fullerton.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions, page 1004,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
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
#    K Mitchell,
#    Tables of the function Integral ( 0 < y < x ) - log | 1 - y | dy / y
#    with an account of some properties of this and related functions,
#    Philosophical Magazine,
#    Volume 40, pages 351-368, 1949.
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, Spence's function evaluated at X.
#
  import numpy as np
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach

  pi26 = +1.644934066848226436472415166646025189219

  spencs = np.array ( [ \
      +0.1527365598892405872946684910028, \
      +0.8169658058051014403501838185271E-01, \
      +0.5814157140778730872977350641182E-02, \
      +0.5371619814541527542247889005319E-03, \
      +0.5724704675185826233210603054782E-04, \
      +0.6674546121649336343607835438589E-05, \
      +0.8276467339715676981584391689011E-06, \
      +0.1073315673030678951270005873354E-06, \
      +0.1440077294303239402334590331513E-07, \
      +0.1984442029965906367898877139608E-08, \
      +0.2794005822163638720201994821615E-09, \
      +0.4003991310883311823072580445908E-10, \
      +0.5823462892044638471368135835757E-11, \
      +0.8576708692638689278097914771224E-12, \
      +0.1276862586280193045989483033433E-12, \
      +0.1918826209042517081162380416062E-13, \
      +0.2907319206977138177795799719673E-14, \
      +0.4437112685276780462557473641745E-15, \
      +0.6815727787414599527867359135607E-16, \
      +0.1053017386015574429547019416644E-16, \
      +0.1635389806752377100051821734570E-17, \
      +0.2551852874940463932310901642581E-18, \
      +0.3999020621999360112770470379519E-19, \
      +0.6291501645216811876514149171199E-20, \
      +0.9933827435675677643803887752533E-21, \
      +0.1573679570749964816721763805866E-21, \
      +0.2500595316849476129369270954666E-22, \
      +0.3984740918383811139210663253333E-23, \
      +0.6366473210082843892691326293333E-24, \
      +0.1019674287239678367077061973333E-24, \
      +0.1636881058913518841111074133333E-25, \
      +0.2633310439417650117345279999999E-26, \
      +0.4244811560123976817224362666666E-27, \
      +0.6855411983680052916824746666666E-28, \
      +0.1109122433438056434018986666666E-28, \
      +0.1797431304999891457365333333333E-29, \
      +0.2917505845976095173290666666666E-30, \
      +0.4742646808928671061333333333333E-31 ] )

  nspenc = r8_inits ( spencs, 38, 0.1 * r8_mach ( 3 ) )
  xbig = 1.0 / r8_mach ( 3 )

  if ( x <= - xbig ):

    aln = np.log ( 1.0 - x )
    value = - pi26  - 0.5 * aln * ( 2.0 * np.log ( - x ) - aln )

  elif ( x <= - 1.0 ):

    aln = np.log ( 1.0 - x )

    value = - pi26 - 0.5 * aln * ( 2.0 \
      * np.log ( - x ) - aln ) + ( 1.0 + r8_csevl ( \
      4.0 / ( 1.0 - x ) - 1.0, spencs, nspenc ) ) / ( 1.0 - x )

  elif ( x <= 0.0 ):

    value = - 0.5 * np.log ( 1.0 - x ) \
      * np.log ( 1.0 - x ) - x * ( 1.0 + r8_csevl ( \
      4.0 * x / ( x - 1.0 ) - 1.0, spencs, nspenc ) ) \
      / ( x - 1.0 )

  elif ( x <= 0.5 ):

    value = x * ( 1.0 + r8_csevl ( 4.0 * x - 1.0, spencs, nspenc ) )

  elif ( x < 1.0 ):

    value = pi26 - np.log ( x ) * np.log ( 1.0 - x ) \
      - ( 1.0 - x ) * ( 1.0 + r8_csevl ( 4.0 \
      * ( 1.0 - x ) - 1.0, spencs, nspenc ) )

  elif ( x == 1.0 ):

    value = pi26

  elif ( x <= 2.0 ):

    value = pi26 - 0.5 * np.log ( x ) \
      * np.log ( ( x - 1.0 ) * ( x - 1.0 ) / x ) \
      + ( x - 1.0 ) * ( 1.0 + r8_csevl ( 4.0 \
      * ( x - 1.0 ) / x - 1.0, spencs, nspenc ) ) / x

  elif ( x < xbig ):

    value = 2.0 * pi26 - 0.5 * np.log ( x ) * np.log ( x ) \
      - ( 1.0 + r8_csevl ( 4.0 / x - 1.0, spencs, \
      nspenc ) ) / x

  else:

    value = 2.0 * pi26 - 0.5 * np.log ( x ) * np.log ( x )

  return value

def r8_spence_test ( ):

#*****************************************************************************80
#
## R8_SPENCE_TEST tests R8_SPENCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from dilogarithm_values import dilogarithm_values

  print ( '' )
  print ( 'R8_SPENCE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SPENCE evaluates Spence\'s integral.' )
  print ( '' )
  print ( '             X       SPENCE(X)  R8_SPENCE(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = dilogarithm_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_spence ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SPENCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_spence_test ( )
  timestamp ( )

