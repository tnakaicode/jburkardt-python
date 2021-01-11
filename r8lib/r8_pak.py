#! /usr/bin/env python
#
def r8_pak ( y, n ):

#*****************************************************************************80
#
## R8_PAK packs a base 2 exponent into an R8.
#
#  Discussion:
#
#    This routine is almost the inverse of R8_UPAK.  It is not exactly
#    the inverse, because abs ( x ) need not be between 0.5 and 1.0.
#    If both R8_PAK and 2.0^n were known to be in range, we could compute
#    R8_PAK = x * 2.0^n.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 216
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, real Y, the mantissa.
#
#    Input, integer N, the exponent.
#
#    Output, real VALUE, the packed value.
#
  from machine import i4_mach
  from machine import r8_mach
  from sys import exit

  aln210 = 3.321928094887362347870319429489

  aln2b = 1.0
  if ( i4_mach ( 10 ) != 2 ):
    aln2b = r8_mach ( 5 ) * aln210
  nmin = aln2b * i4_mach ( 15 )
  nmax = aln2b * i4_mach ( 16 )

  value, ny = r8_upak ( y )

  nsum = n + ny

  if ( nsum < nmin ):
    print ( '' )
    print ( 'R8_PAK - Warning!' )
    print ( '  Packed number underflows.' )
    value = 0.0
    return value

  if ( nmax < nsum ):
    print ( '' )
    print ( 'R8_PAK - Fatal error!' )
    print ( '  Packed number overflows.' )
    exit ( 'R8_PAK - Fatal error!' )

  while ( nsum < 0 ):
    value = 0.5 * value
    nsum = nsum + 1

  while ( 0 < nsum ):
    value = 2.0 * value
    nsum = nsum - 1

  return value

def r8_pak_test ( ):

#*****************************************************************************80
#
## R8_PAK_TEST tests R8_PAK.
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
  import numpy as np
  import platform

  n_test = np.array ( [ 7, 8, 7, 7, 4, 0, -1, 0, 7, 2, 0 ] )

  y_test = np.array ( [ \
    0.5, \
    0.5, \
   -0.5, \
    0.75, \
    0.9375, \
    0.5, \
    0.5, \
    0.625, \
    0.5048828125, \
    0.7853981633974483, \
    0.0 ] )

  print ( '' )
  print ( 'R8_PAK_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_PAK converts a mantissa and base 2 exponent to an R8.' )
  print ( '' )
  print ( '    Mantissa     Exponent         R8' )
  print ( '' )

  for i in range ( 0, 11 ):

    y = y_test[i];
    n = n_test[i]

    x = r8_pak ( y, n )

    print ( '  %24.16g  %8d  %14.16g' % ( y, n, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_PAK_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_upak ( x ):

#*****************************************************************************80
#
## R8_UPAK unpacks an R8 into a mantissa and exponent.
#
#  Discussion:
#
#    This function unpacks a floating point number x so that
#
#      x = y * 2.0^n
#
#    where
#
#      0.5 <= abs ( y ) < 1.0.
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
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, real X, the number to be unpacked.
#
#    Output, real Y, the mantissa.
#
#    Output, integer N, the exponent.
#
  absx = abs ( x )
  n = 0
  y = 0.0

  if ( x == 0.0 ):
    return y, n

  while ( absx < 0.5 ):
    n = n - 1
    absx = absx * 2.0

  while ( 1.0 <= absx ):
    n = n + 1
    absx = absx * 0.5

  if ( x < 0.0 ):
    y = - absx
  else:
    y = + absx

  return y, n

def r8_upak_test ( ):

#*****************************************************************************80
#
## R8_UPAK_TEST tests R8_UPAK.
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
  import numpy as np
  import platform

  x_test = np.array ( [ \
    64.0, \
   128.0, \
   -64.0, \
    96.0, \
    15.0, \
    0.5, \
    0.25, \
    0.625, \
   64.625, \
    3.141592653589793, \
    0.0 ] )

  print ( '' )
  print ( 'R8_UPAK_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UPAK converts an R8 to a mantissa and base 2 exponent.' )
  print ( '' )
  print ( '             X         Mantissa     Exponent' )
  print ( '' )

  for i in range ( 0, 11 ):

    x = x_test[i];

    y, n = r8_upak ( x )

    print ( '  %24.16g  %24.16g  %8d' % ( x, y, n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UPAK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_pak_test ( )
  r8_upak_test ( )
  timestamp ( )
