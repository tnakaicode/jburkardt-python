#! /usr/bin/env python
#
def r8_log ( x ):

#*****************************************************************************80
#
## R8_LOG evaluates the logarithm of an R8.
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
#    Input, real X, the evaluation point.
#
#    Output, real VALUE, the logarithm of X.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach
  from r8_pak import r8_upak
  from sys import exit

  aln2 = 0.06814718055994530941723212145818

  alncs = np.array ( [ \
      +0.13347199877973881561689386047187E+01, \
      +0.69375628328411286281372438354225E-03, \
      +0.42934039020450834506559210803662E-06, \
      +0.28933847795432594580466440387587E-09, \
      +0.20512517530340580901741813447726E-12, \
      +0.15039717055497386574615153319999E-15, \
      +0.11294540695636464284521613333333E-18, \
      +0.86355788671171868881946666666666E-22, \
      +0.66952990534350370613333333333333E-25, \
      +0.52491557448151466666666666666666E-28, \
      +0.41530540680362666666666666666666E-31 ] )

  center = np.array ( [ 1.0, 1.25, 1.50, 1.75 ] )

  alncen = np.array ( [ \
      +0.0, \
      +0.22314355131420975576629509030983, \
      +0.40546510810816438197801311546434, \
      +0.55961578793542268627088850052682, \
      +0.69314718055994530941723212145817 ] )

  nterms = r8_inits ( alncs, 11, 28.9 * r8_mach ( 3 ) )

  if ( x <= 0.0 ):
    print ( '' )
    print ( 'R8_LOG - Fatal error!' )
    print ( '  X <= 0.0' )
    exit ( 'R8_LOG - Fatal error!' )

  y, n = r8_upak ( x )

  xn = n - 1
  y = 2.0 * y
  ntrval = int ( r8_aint ( 4.0 * y - 2.5 ) )

  if ( ntrval == 5 ):
    t = ( ( y - 1.0 ) - 1.0 ) / ( y + 2.0 )
  elif ( ntrval < 5 ):
    t = ( y - center[ntrval-1] ) / ( y + center[ntrval-1] )

  t2 = t * t
  value = 0.625 * xn + ( aln2 * xn + alncen[ntrval-1] \
    + 2.0 * t + t * t2 \
    * r8_csevl ( 578.0 * t2 - 1.0, alncs, nterms ) )

  return value

def r8_log_test ( ):

#*****************************************************************************80
#
## R8_LOG_TEST tests R8_LOG.
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
  from log_values import log_values

  print ( '' )
  print ( 'R8_LOG_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_LOG evaluates the logarithm.' )
  print ( '' )
  print ( '             X          LOG(X)  R8_LOG(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_log ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_LOG_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_log_test ( )
  timestamp ( )
