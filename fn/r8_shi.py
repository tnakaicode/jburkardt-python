#! /usr/bin/env python
#
def r8_shi ( x ):

#*****************************************************************************80
#
## R8_SHI evaluates the hyperbolic sine integral Shi of an R8 argument.
#
#  Discussion:
#
#    Shi ( x ) = Integral ( 0 <= t <= x ) sinh ( t ) dt / t
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
#    Output, real VALUE, the hyperbolic sine integral
#    Shi evaluated at X.
#
  import numpy as np
  from r8_csevl import r8_csevl
  from r8_e1 import r8_e1
  from r8_ei import r8_ei
  from r8_inits import r8_inits
  from machine import r8_mach

  shics = np.array ( [ \
      0.0078372685688900950695200984317332, \
      0.0039227664934234563972697574427225, \
      0.0000041346787887617266746747908275, \
      0.0000000024707480372882742135145302, \
      0.0000000000009379295590763630457157, \
      0.0000000000000002451817019520867353, \
      0.0000000000000000000467416155257592, \
      0.0000000000000000000000067803072389, \
      0.0000000000000000000000000007731289, \
      0.0000000000000000000000000000000711 ] )

  nshi = r8_inits ( shics, 10, 0.1 * r8_mach ( 3 ) )
  xsml = np.sqrt ( r8_mach ( 3 ) )

  absx = abs ( x )

  if ( absx <= xsml ):
    value = x
  elif ( absx <= 0.375 ):
    value = x * ( 1.0 + r8_csevl ( 128.0 * x * x / 9.0 - 1.0, shics, nshi ) )
  else:
    value = 0.5 * ( r8_ei ( x ) + r8_e1 ( x ) )

  return value

def r8_shi_test ( ):

#*****************************************************************************80
#
## R8_SHI_TEST tests R8_SHI.
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
  from shi_values import shi_values

  print ( '' )
  print ( 'R8_SHI_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SHI evaluates the hyperbolic sine integral.' )
  print ( '' )
  print ( '             X          SHI(X)  R8_SHI(X)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = shi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_shi ( x )

    print ( '  %14.4f  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SHI_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_shi_test ( )
  timestamp ( )

