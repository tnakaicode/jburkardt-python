#! /usr/bin/env python3
#
def r8_sincos_sum ( a, b ):

#*****************************************************************************80
#
## R8_SINCOS_SUM simplifies a*sin(cx)+b*cos(cx).
#
#  Discussion:
#
#    The expression
#      a * sin ( c * x ) + b * cos ( c * x )
#    can be rewritten as
#      d * sin ( c * x + e )
#    or
#      d * cos ( c * x + f ) 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the coefficients in the linear combination.
#
#    Output, real D, E, F, the new coefficient, and the shift for
#    sine or for cosine.
#
  import numpy as np

  d = np.sqrt ( a * a + b * b )
  e = np.arctan2 ( b, a )
  f = np.arctan2 ( b, a ) - np.pi / 2.0
  if ( f < - np.pi ):
    f = f + 2.0 * np.pi

  return d, e, f
  
def r8_sincos_sum_test ( ):

#*****************************************************************************80
#
## R8_SINCOS_SUM_TEST tests R8_SINCOS_SUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'R8_SINCOS_SUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SINCOS_SUM simplifies a linear sine and cosine sum' )

  seed = 123456789
  a, seed = r8_uniform_ab ( -5.0, +5.0, seed )
  b, seed = r8_uniform_ab ( -5.0, +5.0, seed )
  c, seed = r8_uniform_ab ( -5.0, +5.0, seed )

  d, e, f = r8_sincos_sum ( a, b )

  print ( '' )
  print ( '    %g * sin ( %g * x ) + %g * cos ( %g * x )' % ( a, c, b, c ) )
  print ( '  = %g * sin ( %g * x + %g )' % ( d, c, e ) )
  print ( '  = %g * cos ( %g * x + %g )' % ( d, c, f ) )

  x = np.linspace ( 0.0, np.pi, 11 )
  y1 = a * np.sin ( c * x ) + b * np.cos ( c * x )
  y2 = d * np.sin ( c * x + e )
  y3 = d * np.cos ( c * x + f )

  print ( '' )
  print ( '   I      X              form 1        form 2        form 3' )
  print ( '' )

  for i in range ( 0, 11 ):
    print ( '  %2d  %10f  %12.6g  %12.6g  %12.6g' % ( i, x[i], y1[i], y2[i], y3[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SINCOS_SUM_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_sincos_sum_test ( )
  timestamp ( )
 
