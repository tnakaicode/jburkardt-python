#! /usr/bin/env python
#
def r8_poch ( a, x ):

#*****************************************************************************80
#
## R8_POCH evaluates Pochhammer's function of R8 arguments.
#
#  Discussion:
#
#    POCH ( A, X ) = Gamma ( A + X ) / Gamma ( A ).
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
#    Input, real A, X, the arguments.
#
#    Output, real VALUE, the Pochhammer function of A and X.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_fac import r8_fac
  from r8_gamma import r8_gamma
  from r8_gamr import r8_gamr
  from r8_lgams import r8_lgams
  from r8_lgmc import r8_lgmc
  from r8_lnrel import r8_lnrel
  from machine import r8_mach
  from r8_mop import r8_mop
  from sys import exit

  eps = r8_mach ( 4 )
  sqeps = np.sqrt ( eps )

  ax = a + x

  if ( ax <= 0.0 and r8_aint ( ax ) == ax ):

    if ( 0.0 < a or r8_aint ( a ) != a ):
      print ( '' )
      print ( 'R8_POCH - Fatal error!' )
      print ( '  A + X is nonpositive integer,' )
      print ( '  but A is not.' )
      exit ( 'R8_POCH - Fatal error!' )
#
#  We know here that both A+X and A are non-positive integers.
#
    if ( x == 0.0 ):
      value = 1.0
    elif ( - 20.0 < min ( a + x, a ) ):
      n = int ( r8_aint ( x ) )
      ia = int ( r8_aint ( a ) )
      value = r8_mop ( n ) * r8_fac ( - ia ) / r8_fac ( - ia - n )
    else:
      n = int ( r8_aint ( x ) )
      value = r8_mop ( n ) * np.exp ( ( a - 0.5 ) \
        * r8_lnrel ( x / ( a - 1.0 ) ) \
        + x * np.log ( - a + 1.0 - x ) - x \
        + r8_lgmc ( - a + 1.0 ) \
        - r8_lgmc ( - a - x + 1.0 ) )

    return value
#
#  A + X is not zero or a negative integer.
#
  if ( a <= 0.0 and r8_aint ( a ) == a ):
    value = 0.0
    return value

  n = int ( abs ( r8_aint ( x ) ) )
#
#  X is a small non-positive integer, presummably a common case.
#
  if ( n == x and n <= 20 ):
    value = 1.0
    for i in range ( 0, n ):
      value = value * ( a + i )
    return value

  absax = abs ( a + x )
  absa = abs ( a )

  if ( max ( absax, absa ) <= 20.0 ):
    value = r8_gamma ( a + x ) * r8_gamr ( a )
    return value

  if ( 0.5 * absa < abs ( x ) ):
    alngax, sgngax = r8_lgams ( a + x )
    alnga, sgnga = r8_lgams ( a )
    value = sgngax * sgnga * np.exp ( alngax - alnga )
    return value
#
#  abs(x) is small and both abs(a+x) and abs(a) are large.  thus,
#  a+x and a must have the same sign.  for negative a, we use
#  gamma(a+x)/gamma(a) = gamma(-a+1)/gamma(-a-x+1) *
#  sin(pi*a)/sin(pi*(a+x))
#
  if ( a < 0.0 ):
    b = - a - x + 1.0
  else:
    b = a

  value = np.exp ( ( b - 0.5 ) * r8_lnrel ( x / b ) \
    + x * np.log ( b + x ) - x + r8_lgmc ( b + x ) - r8_lgmc ( b ) )

  if ( 0.0 <= a or value == 0.0 ):
    return value

  cospix = np.cos ( np.pi * x )
  sinpix = np.sin ( np.pi * x )
  cospia = np.cos ( np.pi * a )
  sinpia = np.sin ( np.pi * a )

  errpch = abs ( x ) * ( 1.0 + np.log ( b ) )
  den = cospix + cospia * sinpix / sinpia
  err = ( abs ( x ) * ( abs ( sinpix ) \
    + abs ( cospia * cospix / sinpia ) ) \
    + abs ( a * sinpix ) / sinpia / sinpia ) * pi
  err = errpch + err / abs ( den )

  value = value / den

  return value

def r8_poch_test ( ):

#*****************************************************************************80
#
## R8_POCH_TEST tests R8_POCH.
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
  from r8_rise_values import r8_rise_values

  print ( '' )
  print ( 'R8_POCH_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_POCH evaluates the Pochhammer symbol.' )
  print ( '' )
  print ( '             A               X      POCH(A,X)  R8_POCH(A,X)         Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, n, fx1 = r8_rise_values ( n_data )

    if ( n_data == 0 ):
      break

    x = n
    fx2 = r8_poch ( a, x )

    print ( '  %14.4g  %14.4g  %14.6g  %14.6g  %14.6g' \
      % ( a, x, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_POCH_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_poch_test ( )
  timestamp ( )

