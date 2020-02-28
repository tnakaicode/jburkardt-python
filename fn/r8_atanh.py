#! /usr/bin/env python
#
def r8_atanh ( x ):

#*****************************************************************************80
#
## R8_ATANH evaluates the arc-hyperbolic tangent of an R8 argument.
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
#    Output, real VALUE, the arc-hyperbolic tangent of X.
#
  import numpy as np
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach
  from sys import exit

  atnhcs = np.array ( [ \
    +0.9439510239319549230842892218633E-01, \
    +0.4919843705578615947200034576668E-01, \
    +0.2102593522455432763479327331752E-02, \
    +0.1073554449776116584640731045276E-03, \
    +0.5978267249293031478642787517872E-05, \
    +0.3505062030889134845966834886200E-06, \
    +0.2126374343765340350896219314431E-07, \
    +0.1321694535715527192129801723055E-08, \
    +0.8365875501178070364623604052959E-10, \
    +0.5370503749311002163881434587772E-11, \
    +0.3486659470157107922971245784290E-12, \
    +0.2284549509603433015524024119722E-13, \
    +0.1508407105944793044874229067558E-14, \
    +0.1002418816804109126136995722837E-15, \
    +0.6698674738165069539715526882986E-17, \
    +0.4497954546494931083083327624533E-18, \
    +0.3032954474279453541682367146666E-19, \
    +0.2052702064190936826463861418666E-20, \
    +0.1393848977053837713193014613333E-21, \
    +0.9492580637224576971958954666666E-23, \
    +0.6481915448242307604982442666666E-24, \
    +0.4436730205723615272632320000000E-25, \
    +0.3043465618543161638912000000000E-26, \
    +0.2091881298792393474047999999999E-27, \
    +0.1440445411234050561365333333333E-28, \
    +0.9935374683141640465066666666666E-30, \
    +0.6863462444358260053333333333333E-31 ] )

  nterms = r8_inits ( atnhcs, 27, 0.1 * r8_mach ( 3 ) )
  dxrel = np.sqrt ( r8_mach ( 4 ) )
  sqeps = np.sqrt ( 3.0 * r8_mach ( 3 ) )

  y = abs ( x )

  if ( y <= sqeps ):
    value = x
  elif ( y <= 0.5 ):
    value = x * ( 1.0 + r8_csevl ( 8.0 * x * x - 1.0, atnhcs, nterms ) )
  elif ( y < 1.0 ):
    value = 0.5 * np.log ( ( 1.0 + x ) / ( 1.0 - x ) )
    if ( 1.0 - y < dxrel ):
      print ( '' )
      print ( 'R8_ATANH - Warning:' )
      print ( '  Answer lt half precision because |X| too near 1.' )
  else:
    print ( '' )
    print ( 'R8_ATANH - Fatal error!' )
    print ( '  1 <= |X|.' )
    exit ( 'R8_ATANH - Fatal error!' )

  return value

def r8_atanh_test ( ):

#*****************************************************************************80
#
## R8_ATANH_TEST tests R8_ATANH.
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
  from arctanh_values import arctanh_values

  print ( '' )
  print ( 'R8_ATANH_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_ATANH evaluates the hyperbolic arctangent function.' )
  print ( '' )
  print ( '             X     ARCTANH(X)  R8_ATANH(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = arctanh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_atanh ( x )

    print ( '  %14f  %14g  %14g  %14g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_ATANH_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_atanh_test ( )
  timestamp ( )
