#! /usr/bin/env python
#
def r8_cinh ( x ):

#*****************************************************************************80
#
## R8_CINH: alternate hyperbolic cosine integral Cinh of an R8 argument.
#
#  Discussion:
#
#    Cinh ( x ) = Integral ( 0 <= t <= x ) ( cosh ( t ) - 1 ) dt / t
#
#    The original text of this program had a mistake:
#      y = x * x / 9.0 - 1.0
#    has been corrected to
#      y = x * x / 4.5 - 1.0
#    JVB, 27 March 2010
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
#    Output, real VALUE, the hyperbolic cosine integral Cinh
#    evaluated at X.
#
  import numpy as np
  from r8_chi import r8_chi
  from r8_csevl import r8_csevl
  from r8_inits import r8_inits
  from machine import r8_mach

  eul = 0.57721566490153286060651209008240

  cinhcs = np.array ( [ \
      0.1093291636520734431407425199795917, \
      0.0573928847550379676445323429825108, \
      0.0028095756978830353416404208940774, \
      0.0000828780840721356655731765069792, \
      0.0000016278596173914185577726018815, \
      0.0000000227809519255856619859083591, \
      0.0000000002384484842463059257284002, \
      0.0000000000019360829780781957471028, \
      0.0000000000000125453698328172559683, \
      0.0000000000000000663637449497262300, \
      0.0000000000000000002919639263594744, \
      0.0000000000000000000010849123956107, \
      0.0000000000000000000000034499080805, \
      0.0000000000000000000000000094936664, \
      0.0000000000000000000000000000228291, \
      0.0000000000000000000000000000000484 ] )

  ncinh = r8_inits ( cinhcs, 16, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( r8_mach ( 3 ) )
  xmin = 2.0 * np.sqrt ( r8_mach ( 1 ) )

  absx = abs ( x )

  if ( x == 0.0 ):
    value = 0.0
  elif ( absx <= xmin ):
    value = 0.0
  elif ( x <= xsml ):
    y = - 1.0
    value = x * x * ( 0.25 + r8_csevl ( y, cinhcs, ncinh ) )
  elif ( x <= 3.0 ):
    y = x * x / 4.5 - 1.0
    value = x * x * ( 0.25 + r8_csevl ( y, cinhcs, ncinh ) )
  else:
    value = r8_chi ( absx ) - eul - np.log ( absx )

  return value

def r8_cinh_test ( ):

#*****************************************************************************80
#
## R8_CINH_TEST tests R8_CINH.
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
  from cinh_values import cinh_values

  print ( '' )
  print ( 'R8_CINH_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CINH evaluates the alternate hyperbolic cosine integral.' )
  print ( '' )
  print ( '             X         CINH(X)  R8_CINH(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cinh_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cinh ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CINH_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_cinh_test ( )
  timestamp ( )
