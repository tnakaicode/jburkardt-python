#! /usr/bin/env python
#
def r8_lgmc ( x ):

#*****************************************************************************80
#
## R8_LGMC evaluates the log gamma correction factor for an R8 argument.
#
#  Discussion:
#
#    For 10 <= X, compute the log gamma correction factor so that
#
#      log ( gamma ( x ) ) = log ( sqrt ( 2 * pi ) )
#                          + ( x - 0.5 ) * log ( x ) - x
#                          + r8_lgmc ( x )
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
#    Output, real VALUE, the correction factor.
#
  import numpy as np
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach
  from sys import exit

  algmcs = np.array ( [ \
      +0.1666389480451863247205729650822, \
      -0.1384948176067563840732986059135E-04, \
      +0.9810825646924729426157171547487E-08, \
      -0.1809129475572494194263306266719E-10, \
      +0.6221098041892605227126015543416E-13, \
      -0.3399615005417721944303330599666E-15, \
      +0.2683181998482698748957538846666E-17, \
      -0.2868042435334643284144622399999E-19, \
      +0.3962837061046434803679306666666E-21, \
      -0.6831888753985766870111999999999E-23, \
      +0.1429227355942498147573333333333E-24, \
      -0.3547598158101070547199999999999E-26, \
      +0.1025680058010470912000000000000E-27, \
      -0.3401102254316748799999999999999E-29, \
      +0.1276642195630062933333333333333E-30 ] )

  nalgm = r8_inits ( algmcs, 15, r8_mach ( 3 ) )
  xbig = 1.0 / np.sqrt ( r8_mach ( 3 ) )
  xmax = np.exp ( min ( np.log ( r8_mach ( 2 ) / 12.0 ), \
    - np.log ( 12.0 * r8_mach ( 1 ) ) ) )

  if ( x < 10.0 ):

    print ( '' )
    print ( 'R8_LGMC - Fatal error!' )
    print ( '  X must be at least 10.' )
    exit ( 'R8_LGMC - Fatal error!' )

  elif ( x < xbig ):

    value = r8_csevl ( 2.0 * ( 10.0 / x ) * ( 10.0 / x ) - 1.0, algmcs, nalgm ) / x

  elif ( x < xmax ):

    value = 1.0 / ( 12.0 * x )

  else:

    value = 0.0

  return value

def r8_lgmc_test ( ):

#*****************************************************************************80
#
## R8_LGMC_TEST tests R8_LGMC.
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
  import numpy as np
  import platform
  from gamma_log_values import gamma_log_values

  print ( '' )
  print ( 'R8_LGMC_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_LGMC evaluates the correction log gamma factor.' )
  print ( '  r8_lgmc(x) = log ( gamma ( x ) ) - log ( sqrt ( 2 * pi )' )
  print ( '    - ( x - 0.5 ) * log ( x ) + x' )
  print ( '' )
  print ( '             X        LGMC(X)  R8_LGMC(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, gamma_log = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break
#
#  Function requires 10 <= x.
#
    if ( 10.0 <= x ):
      fx1 = gamma_log - np.log ( np.sqrt ( 2.0 * np.pi ) ) \
        - ( x - 0.5 ) * np.log ( x ) + x
      fx2 = r8_lgmc ( x )
      print ( '  %14.4f  %14.6g  %14.6g  %14.6g' \
        % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_LGMC_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_lgmc_test ( )
  timestamp ( )
