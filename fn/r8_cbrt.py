#! /usr/bin/env python
#
def r8_cbrt ( x ):

#*****************************************************************************80
#
## R8_CBRT computes the cube root of an R8.
#
#  Discussion:
#
#    The approximation is a generalized Chebyshev series converted
#    to polynomial form.  The approximation is nearly best in the
#    sense of relative error with 4.085 digits accuracy.
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
#    Input, real X, the number whose square root is desired.
#
#    Output, real VALUE, the cube root of X.
#
  import numpy as np
  from r8_aint import r8_aint
  from machine import r8_mach
  from r8_pak import r8_pak
  from r8_pak import r8_upak

  cbrt2 = np.array ( [ \
      0.62996052494743658238360530363911, \
      0.79370052598409973737585281963615, \
      1.0, \
      1.25992104989487316476721060727823, \
      1.58740105196819947475170563927231 ] )

  niter = int ( r8_aint ( 1.443 * np.log ( - 0.106 \
      * np.log ( 0.1 * r8_mach ( 3 ) ) ) + 1.0 ) )

  value = 0.0

  if ( x != 0.0 ):

    y, n = r8_upak ( abs ( x ) )
    ixpnt = ( n // 3 )
    irem = n - 3 * ixpnt + 3

    value = 0.439581 + y * ( \
            0.928549 + y * ( \
          - 0.512653 + y * \
            0.144586 ) )

    for iter in range ( 0, niter ):
      vsq = value * value
      value = value + ( y - value * vsq ) / ( 3.0 * vsq )

    if ( x < 0.0 ):
      value = - abs ( value )
    else:
      value = + abs ( value )

    value = r8_pak ( cbrt2[irem-1] * value, ixpnt )

  return value

def r8_cbrt_test ( ):

#*****************************************************************************80
#
#% R8_CBRT_TEST tests R8_CBRT.
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
  from cbrt_values import cbrt_values

  print ( '' )
  print ( 'R8_CBRT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CBRT evaluates the cube root function.' )
  print ( '' )
  print ( '             X        CBRT(X)  R8_CBRT(X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = cbrt_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_cbrt ( x )

    print ( '  %14.4g  %14.6g  %14.6g  %14.6g' % ( x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CBRT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_cbrt_test ( )
  timestamp ( )

