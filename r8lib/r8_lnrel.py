#! /usr/bin/env python
#
def r8_lnrel ( x ):

#*****************************************************************************80
#
## R8_LNREL evaluates log ( 1 + X ) for an R8 argument.
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
#    Output, real VALUE, the value of LOG ( 1 + X ).
#
  import numpy as np
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from r8_log import r8_log
  from machine import r8_mach
  from sys import exit

  alnrcs = np.array ( [ \
      +0.10378693562743769800686267719098E+01, \
      -0.13364301504908918098766041553133, \
      +0.19408249135520563357926199374750E-01, \
      -0.30107551127535777690376537776592E-02, \
      +0.48694614797154850090456366509137E-03, \
      -0.81054881893175356066809943008622E-04, \
      +0.13778847799559524782938251496059E-04, \
      -0.23802210894358970251369992914935E-05, \
      +0.41640416213865183476391859901989E-06, \
      -0.73595828378075994984266837031998E-07, \
      +0.13117611876241674949152294345011E-07, \
      -0.23546709317742425136696092330175E-08, \
      +0.42522773276034997775638052962567E-09, \
      -0.77190894134840796826108107493300E-10, \
      +0.14075746481359069909215356472191E-10, \
      -0.25769072058024680627537078627584E-11, \
      +0.47342406666294421849154395005938E-12, \
      -0.87249012674742641745301263292675E-13, \
      +0.16124614902740551465739833119115E-13, \
      -0.29875652015665773006710792416815E-14, \
      +0.55480701209082887983041321697279E-15, \
      -0.10324619158271569595141333961932E-15, \
      +0.19250239203049851177878503244868E-16, \
      -0.35955073465265150011189707844266E-17, \
      +0.67264542537876857892194574226773E-18, \
      -0.12602624168735219252082425637546E-18, \
      +0.23644884408606210044916158955519E-19, \
      -0.44419377050807936898878389179733E-20, \
      +0.83546594464034259016241293994666E-21, \
      -0.15731559416479562574899253521066E-21, \
      +0.29653128740247422686154369706666E-22, \
      -0.55949583481815947292156013226666E-23, \
      +0.10566354268835681048187284138666E-23, \
      -0.19972483680670204548314999466666E-24, \
      +0.37782977818839361421049855999999E-25, \
      -0.71531586889081740345038165333333E-26, \
      +0.13552488463674213646502024533333E-26, \
      -0.25694673048487567430079829333333E-27, \
      +0.48747756066216949076459519999999E-28, \
      -0.92542112530849715321132373333333E-29, \
      +0.17578597841760239233269760000000E-29, \
      -0.33410026677731010351377066666666E-30, \
      +0.63533936180236187354180266666666E-31 ] )
  
  nlnrel = r8_inits ( alnrcs, 43, 0.1 * r8_mach ( 3 ) )
  xmin = - 1.0 + np.sqrt ( r8_mach ( 4 ) )

  if ( x <= - 1.0 ):
    print ( '' )
    print ( 'R8_LNREL - Fatal error!' )
    print ( '  X <= -1.' )
    exit ( 'R8_LNREL - Fatal error!' )
  elif ( x < xmin ):
    print ( '' )
    print ( 'R8_LNREL - Warning!' )
    print ( '  Result is less than half precision.' )
    print ( '  X is too close to - 1.' )

  if ( abs ( x ) <= 0.375 ):
    value = x * ( 1.0 - x * r8_csevl ( x / 0.375, alnrcs, nlnrel ) )
  else:
    value = r8_log ( 1.0 + x )

  return value

def r8_lnrel_test ( ):

#*****************************************************************************80
#
#% R8_LNREL_TEST tests R8_LNREL.
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
  from log_values import log_values

  print ( '' )
  print ( 'R8_LNREL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_LNREL evaluates  ln(1+X).' )
  print ( '' )
  print ( '             X          LN(1+X)  R8_LNREL(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = log_values ( n_data )

    if ( n_data == 0 ):
      break

    x = x - 1.0
    fx2 = r8_lnrel ( x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_LNREL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_lnrel_test ( )
  timestamp ( )
