#! /usr/bin/env python3
#
def machar_test ( ):

#*****************************************************************************80
#
## MACHAR_TEST tests the MACHAR library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'MACHAR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the MACHAR library.' )

  r4_machar_test ( )
  r8_machar_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'MACHAR_TEST' )
  print ( '  Normal end of execution.' )

  return

def r4_machar ( ):

#*****************************************************************************80
#
## R4_MACHAR determines single precision real machine constants.
#
#  Discussion:
#
#    This routine determines the parameters of the single precision
#    real arithmetic system.  The determination of the first
#    three uses an extension of an algorithm due to Malcolm,
#    incorporating some of the improvements suggested by Gentleman and
#    Marovich.
#
#    This routine appeared as ACM algorithm 665.
#
#    An earlier version of this program was published in Cody and Waite.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2016
#
#  Author:
#
#    Original FORTRAN77 version by William Cody.
#    Python version by John Burkardt.
#
#  Reference:
#
#    William Cody,
#    ACM Algorithm 665, MACHAR, a routine to dynamically determine
#    machine parameters,
#    ACM Transactions on Mathematical Software,
#    Volume 14, Number 4, pages 303-311, 1988.
#
#    William Cody, William Waite,
#    Software Manual for the Elementary Functions,
#    Prentice Hall, 1980.
#
#    Morvern Gentleman, Scott Marovich,
#    Communications of the ACM,
#    Volume 17, pages 276-277, 1974.
#
#    Michael Malcolm,
#    Communications of the ACM,
#    Volume 15, pages 949-951, 1972.
#
#  Parameters:
#
#    Output, integer IBETA, the radix for the floating-point representation.
#
#    Output, integer IT, the number of base IBETA digits in the floating-point
#    significand.
#
#    Output, integer IRND:
#    0, if floating-point addition chops.
#    1, if floating-point addition rounds, but not in the IEEE style.
#    2, if floating-point addition rounds in the IEEE style.
#    3, if floating-point addition chops, and there is partial underflow.
#    4, if floating-point addition rounds, but not in the IEEE style, and
#      there is partial underflow.
#    5, if floating-point addition rounds in the IEEE style, and there is
#      partial underflow.
#
#    Output, integer NGRD, the number of guard digits for multiplication with
#    truncating arithmetic.  It is
#    0, if floating-point arithmetic rounds, or if it truncates and only
#      IT base IBETA digits participate in the post-normalization shift of the
#      floating-point significand in multiplication
#    1, if floating-point arithmetic truncates and more than IT base IBETA
#      digits participate in the post-normalization shift of the floating-point
#      significand in multiplication.
#
#    Output, integer MACHEP, the largest negative integer such that
#      1.0 < 1.0 + real ( IBETA )^MACHEP,
#    except that MACHEP is bounded below by - ( IT + 3 ).
#
#    Output, integer NEGEPS, the largest negative integer such that
#      1.0 - real ( IBETA )^NEGEPS < 1.0,
#    except that NEGEPS is bounded below by - ( IT + 3 ).
#
#    Output, integer IEXP, the number of bits (decimal places if IBETA = 10)
#    reserved for the representation of the exponent (including the bias or
#    sign) of a floating-point number.
#
#    Output, integer MINEXP, the largest in magnitude negative integer such
#    that
#      real ( IBETA )^MINEXP
#    is positive and normalized.
#
#    Output, integer MAXEXP, the smallest positive power of BETA that overflows.
#
#    Output, single precision real EPS, the smallest positive floating-point
#    number such that
#      1.0 + EPS != 1.0.
#    in particular, if either IBETA = 2  or IRND = 0,
#      EPS = real ( IBETA )^MACHEP.
#    Otherwise,
#      EPS = ( real ( IBETA )^MACHEP ) / 2.
#
#    Output, single precision real EPSNEG, a small positive floating-point 
#    number such that
#      1.0 - EPSNEG < 1.0.
#    In particular, if IBETA = 2 or IRND = 0,
#      EPSNEG = real ( IBETA )^NEGEPS.
#    Otherwise,
#      EPSNEG = ( real ( IBETA )^NEGEPS ) / 2.
#    Because NEGEPS is bounded below by - ( IT + 3 ), EPSNEG might not be the
#    smallest number that can alter 1.0 by subtraction.
#
#    Output, single precision real XMIN, the smallest non-vanishing normalized
#    floating-point power of the radix:
#      XMIN = real ( IBETA )^MINEXP
#
#    Output, single precision real XMAX, the largest finite floating-point 
#    number.  In particular,
#      XMAX = ( 1.0 - EPSNEG ) * real ( IBETA )^MAXEXP
#    On some machines, the computed value of XMAX will be only the second,
#    or perhaps third, largest number, being too small by 1 or 2 units in
#    the last digit of the significand.
#
  import numpy as np

  a = np.float32 ( 0.0 )
  b = np.float32 ( 0.0 )
  beta = np.float32 ( 0.0 )
  betah = np.float32 ( 0.0 )
  betain = np.float32 ( 0.0 )
  eps = np.float32 ( 0.0 )
  epsneg = np.float32 ( 0.0 )
  one = np.float32 ( 0.0 )
  t = np.float32 ( 0.0 )
  temp = np.float32 ( 0.0 )
  temp1 = np.float32 ( 0.0 )
  tempa = np.float32 ( 0.0 )
  two = np.float32 ( 0.0 )
  xmax = np.float32 ( 0.0 )
  xmin = np.float32 ( 0.0 )
  y = np.float32 ( 0.0 )
  z = np.float32 ( 0.0 )
  zero = np.float32 ( 0.0 )

  one = np.float32 ( 1.0 )
  two = np.float32 ( one + one )
  zero = np.float32 ( one - one )
#
#  Determine IBETA and BETA ala Malcolm.
#
  a = np.float32 ( one )

  while ( True ):

    a = np.float32 ( a + a )
    temp = np.float32 ( a + one )
    temp1 = np.float32 ( temp - a )

    if ( np.float32 ( temp1 - one ) != zero ):
      break

  b = np.float32 ( one )

  while ( True ):

    b = np.float32 ( b + b )
    temp = np.float32 ( a + b )
    itemp = int ( temp - a )

    if ( itemp != 0 ):
      break

  ibeta = itemp
  beta = np.float32 ( ibeta )
#
#  Determine IT and IRND.
#
  it = 0
  b = np.float32 ( one )

  while ( True ):

    it = it + 1
    b = np.float32 ( b * beta )
    temp = np.float32 ( b + one )
    temp1 = np.float32 ( temp - b )

    if ( np.float32 ( temp1 - one ) != zero ):
      break

  irnd = 0
  betah = np.float32 ( beta / two )
  temp = np.float32 ( a + betah )

  if ( np.float32 ( temp - a ) != zero ):
    irnd = 1

  tempa = np.float32 ( a + beta )
  temp = np.float32 ( tempa + betah )

  if ( irnd == 0 and np.float32 ( temp - tempa ) != zero ):
    irnd = 2
#
#  Determine NEGEP and EPSNEG.
#
  negep = it + 3
  betain = np.float32 ( one / beta )
  a = np.float32 ( one )
  for i in range ( 0, negep ):
    a = np.float32 ( a * betain )

  b = np.float32 ( a )

  while ( True ):

    temp = np.float32 ( one - a )

    if ( np.float32 ( temp - one ) != zero ):
      break
 
    a = np.float32 ( a * beta )
    negep = negep - 1

  negep = -negep
  epsneg = np.float32 ( a )

  if ( ibeta != 2 and irnd != 0 ):

    a = np.float32 ( ( a * ( one + a ) ) / two )
    temp = np.float32 ( one - a )

    if ( np.float32 ( temp - one ) != zero ):
      epsneg = np.float32 ( a )
#
#  Determine MACHEP and EPS.
#
  machep = - it - 3
  a = np.float32 ( b )

  while ( True ):

    temp = np.float32 ( one + a )

    if ( np.float32 ( temp - one ) != zero ):
      break

    a = np.float32 ( a * beta )
    machep = machep + 1

  eps = np.float32 ( a )
  temp = np.float32 ( tempa + beta * ( one + eps ) )

  if ( ibeta != 2 and irnd != 0 ):

    a = np.float32 ( ( a * ( one + a ) ) / two )
    temp = np.float32 ( one + a )

    if ( np.float32 ( temp - one ) != zero ):
      eps = a
#
#  Determine NGRD.
#
  ngrd = 0
  temp = np.float32 ( one + eps )

  if ( irnd == 0 and np.float32 ( temp * one - one ) != zero ):
    ngrd = 1
#
#  Determine IEXP, MINEXP and XMIN.
#
#  Loop to determine largest I and K = 2^I such that (1/BETA)^(2^(I))
#  does not underflow.  Exit from loop is signaled by an underflow.
#
  i = 0
  k = 1
  z = np.float32 ( betain )
  t = np.float32 ( one + eps )
  nxres = 0

  while ( True ):

    y = np.float32 ( z )
    z = np.float32 ( y * y )

    a = np.float32 ( z * one )
    temp = np.float32 ( z * t )

    if ( np.float32 ( a + a ) == zero or y <= abs ( z ) ):
      break

    temp1 = np.float32 ( temp * betain )

    if ( np.float32 ( temp1 * beta ) == z ):
      break

    i = i + 1
    k = k + k
#
#  This segment is for nondecimal machines.
#
  if ( ibeta != 10 ):

    iexp = i + 1
    mx = k + k
#
#  This segment is for decimal machines only.
#
  else:

    iexp = 2
    iz = ibeta

    while ( True ):

      if ( k < iz ):
        break

      iz = iz * ibeta
      iexp = iexp + 1

    mx = iz + iz - 1
#
#  Loop to determine MINEXP, XMIN.
#  Exit from loop is signaled by an underflow.
#
  while ( True ):

    xmin = np.float32 ( y )
    y = np.float32 ( y * betain )

    a = np.float32 ( y * one )
    temp = np.float32 ( y * t )

    if ( np.float32 ( a + a ) == zero or xmin <= abs ( y ) ):
      break

    k = k + 1
    temp1 = np.float32 ( temp * betain )

    if ( np.float32 ( temp1 * beta ) == y ):
      nxres = 3
      xmin = np.float32 ( y )
      break

  minexp = -k
#
#  Determine MAXEXP and XMAX.
#
  if ( mx <= k + k - 3 and ibeta != 10 ):
    mx = mx + mx
    iexp = iexp + 1

  maxexp = mx + minexp
#
#  Adjust IRND to reflect partial underflow.
#
  irnd = irnd + nxres
#
#  Adjust for IEEE-style machines.
#
  if ( irnd == 2 or irnd == 5 ):
    maxexp = maxexp - 2
#
#  Adjust for non-IEEE machines with partial underflow.
#
  if ( irnd == 3 or irnd == 4 ):
    maxexp = maxexp - it
#
#  Adjust for machines with implicit leading bit in binary significand,
#  and machines with radix point at extreme right of significand.
#
  i = maxexp + minexp

  if ( ibeta == 2 and i == 0 ):
    maxexp = maxexp - 1

  if ( 20 < i ):
    maxexp = maxexp - 1

  if ( a != y ):
    maxexp = maxexp - 2

  xmax = np.float32 ( one - epsneg )

  if ( np.float32 ( xmax * one ) != xmax ):
    xmax = np.float32 ( one - beta * epsneg )

  xmax = np.float32 ( xmax / ( beta * beta * beta * xmin ) )

  i = maxexp + minexp + 3

  for j in range ( 0, i ):

    if ( ibeta == 2 ):
      xmax = np.float32 ( xmax + xmax )
    else:
      xmax = np.float32 ( xmax * beta )

  return ibeta, it, irnd, ngrd, machep, negep, iexp, minexp, \
    maxexp, eps, epsneg, xmin, xmax

def r4_machar_test ( ):

#*****************************************************************************80
#
## R4_MACHAR_TEST tests R4_MACHAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R4_MACHAR_TEST' )
  print ( '  R4_MACHAR computes single' )
  print ( '  precision machine constants.' )

  ibeta, it, irnd, ngrd, machep, negep, iexp, minexp, maxexp, eps, epsneg, \
    xmin, xmax = r4_machar ( )

  print ( '' )
  print ( '  IBETA is the internal base for machine arithmetic.' )
  print ( '    IBETA =  %d' % ( ibeta ) )
  print ( '' )
  print ( '  IT is the number of digits, base IBETA, in the' )
  print ( '  floating point significand.' )
  print ( '    IT =     %d' % ( it ) )
  print ( '' )
  print ( '  IRND reports on floating point addition rounding:' )
  print ( '  0, for chopping' )
  print ( '  1, for non-IEEE rounding' )
  print ( '  2, for IEEE rounding' )
  print ( '  3, for chopping with partial underflow' )
  print ( '  4, for non-IEEE rounding with partial underflow.' )
  print ( '  5, for IEEE rounding with partial underflow.' )
  print ( '    IRND =   %d' % ( irnd ) )
  print ( '' )
  print ( '  NGRD is the number of guard digits for floating point' )
  print ( '  multiplication with truncating arithmetic.' )
  print ( '    NGRD =   %d' % ( ngrd ) )
  print ( '' )
  print ( '  MACHEP is the largest negative integer such that' )
  print ( '  1.0 < 1.0 + BETA^MACHEP.' )
  print ( '    MACHEP = %d' % ( machep ) )
  print ( '' )
  print ( '  NEGEPS is the largest negative integer such that' )
  print ( '  1.0 - BETA^NEGEPS < 1.0:' )
  print ( '    NEGEP =  %d' % ( negep ) )
  print ( '' )
  print ( '  IEXP is the number of bits reserved for the exponent' )
  print ( '  of a floating point number:' )
  print ( '    IEXP =   %d' % ( iexp ) )
  print ( '' )
  print ( '  MINEXP is the most negative power of BETA such that' )
  print ( '  BETA^MINEXP is positive and normalized.' )
  print ( '    MINEXP = %d' % ( minexp ) )
  print ( '' )
  print ( '  MAXEXP is the smallest positive power of BETA that' )
  print ( '  overflows:' )
  print ( '    MAXEXP = %d' % ( maxexp ) )
  print ( '' )
  print ( '  EPS is a small positive floating point number' )
  print ( '  such that 1.0 < 1.0 + EPS.' )
  print ( '    EPS    = %26.16e' % ( eps ) )
  print ( '' )
  print ( '  EPSNEG is a small positive floating point number' )
  print ( '  such that 1.0 - EPSNEG < 1.0.' )
  print ( '    EPSNEG = %26.16e' % ( epsneg ) )
  print ( '' )
  print ( '  XMIN is the smallest positive normalized floating' )
  print ( '  point power of the radix:' )
  print ( '    XMIN =   %26.16e' % ( xmin ) )
  print ( '' )
  print ( '  XMAX is the largest finite floating point number:' )
  print ( '    XMAX   = %26.16e' % ( xmax ) )

  return

def r8_machar ( ):

#*****************************************************************************80
#
## R8_MACHAR determines double precision real machine constants.
#
#  Discussion:
#
#    This routine determines the parameters of the double precision
#    real arithmetic system.  The determination of the first
#    three uses an extension of an algorithm due to Malcolm,
#    incorporating some of the improvements suggested by Gentleman and
#    Marovich.
#
#    This routine appeared as ACM algorithm 665.
#
#    An earlier version of this program was published in Cody and Waite.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2016
#
#  Author:
#
#    Original FORTRAN77 version by William Cody.
#    Python version by John Burkardt.
#
#  Reference:
#
#    William Cody,
#    ACM Algorithm 665, MACHAR, a routine to dynamically determine
#    machine parameters,
#    ACM Transactions on Mathematical Software,
#    Volume 14, Number 4, pages 303-311, 1988.
#
#    William Cody, William Waite,
#    Software Manual for the Elementary Functions,
#    Prentice Hall, 1980.
#
#    Morvern Gentleman, Scott Marovich,
#    Communications of the ACM,
#    Volume 17, pages 276-277, 1974.
#
#    Michael Malcolm,
#    Communications of the ACM,
#    Volume 15, pages 949-951, 1972.
#
#  Parameters:
#
#    Output, integer IBETA, the radix for the floating-point representation.
#
#    Output, integer IT, the number of base IBETA digits in the floating-point
#    significand.
#
#    Output, integer IRND:
#    0, if floating-point addition chops.
#    1, if floating-point addition rounds, but not in the IEEE style.
#    2, if floating-point addition rounds in the IEEE style.
#    3, if floating-point addition chops, and there is partial underflow.
#    4, if floating-point addition rounds, but not in the IEEE style, and
#      there is partial underflow.
#    5, if floating-point addition rounds in the IEEE style, and there is
#      partial underflow.
#
#    Output, integer NGRD, the number of guard digits for multiplication with
#    truncating arithmetic.  It is
#    0, if floating-point arithmetic rounds, or if it truncates and only
#      IT base IBETA digits participate in the post-normalization shift of the
#      floating-point significand in multiplication
#    1, if floating-point arithmetic truncates and more than IT base IBETA
#      digits participate in the post-normalization shift of the floating-point
#      significand in multiplication.
#
#    Output, integer MACHEP, the largest negative integer such that
#      1.0 < 1.0 + real ( IBETA )^MACHEP,
#    except that MACHEP is bounded below by - ( IT + 3 ).
#
#    Output, integer NEGEPS, the largest negative integer such that
#      1.0 - real ( IBETA )^NEGEPS < 1.0,
#    except that NEGEPS is bounded below by - ( IT + 3 ).
#
#    Output, integer IEXP, the number of bits (decimal places if IBETA = 10)
#    reserved for the representation of the exponent (including the bias or
#    sign) of a floating-point number.
#
#    Output, integer MINEXP, the largest in magnitude negative integer such
#    that
#      real ( IBETA )^MINEXP
#    is positive and normalized.
#
#    Output, integer MAXEXP, the smallest positive power of BETA that overflows.
#
#    Output, real EPS, the smallest positive floating-point number
#    such that
#      1.0 + EPS != 1.0.
#    in particular, if either IBETA = 2  or IRND = 0,
#      EPS = real ( IBETA )^MACHEP.
#    Otherwise,
#      EPS = ( real ( IBETA )^MACHEP ) / 2.
#
#    Output, real EPSNEG, a small positive floating-point number
#    such that
#      1.0 - EPSNEG < 1.0.
#    In particular, if IBETA = 2 or IRND = 0,
#      EPSNEG = real ( IBETA )^NEGEPS.
#    Otherwise,
#      EPSNEG = ( real ( IBETA )^NEGEPS ) / 2.
#    Because NEGEPS is bounded below by - ( IT + 3 ), EPSNEG might not be the
#    smallest number that can alter 1.0 by subtraction.
#
#    Output, real XMIN, the smallest non-vanishing normalized
#    floating-point power of the radix:
#      XMIN = real ( IBETA )^MINEXP
#
#    Output, real XMAX, the largest finite floating-point number.
#    In particular,
#      XMAX = ( 1.0 - EPSNEG ) * real ( IBETA )^MAXEXP
#    On some machines, the computed value of XMAX will be only the second,
#    or perhaps third, largest number, being too small by 1 or 2 units in
#    the last digit of the significand.
#
  import numpy as np

  one = np.float64 ( 1.0 )
  two = one + one
  zero = one - one
#
#  Determine IBETA and BETA ala Malcolm.
#
  a = one

  while ( True ):

    a = a + a
    temp = a + one
    temp1 = temp - a

    if ( temp1 - one != zero ):
      break

  b = one

  while ( True ):

    b = b + b
    temp = a + b
    itemp = int ( temp - a )

    if ( itemp != 0 ):
      break

  ibeta = itemp
  beta = ibeta
#
#  Determine IT and IRND.
#
  it = 0
  b = one

  while ( True ):

    it = it + 1
    b = b * beta
    temp = b + one
    temp1 = temp - b

    if ( temp1 - one != zero ):
      break

  irnd = 0
  betah = beta / two
  temp = a + betah

  if ( temp - a != zero ):
    irnd = 1

  tempa = a + beta
  temp = tempa + betah

  if ( irnd == 0 and temp - tempa != zero ):
    irnd = 2
#
#  Determine NEGEP and EPSNEG.
#
  negep = it + 3
  betain = one / beta
  a = one
  for i in range ( 0, negep ):
    a = a * betain

  b = a

  while ( True ):

    temp = one - a

    if ( temp - one != zero ):
      break

    a = a * beta
    negep = negep - 1

  negep = -negep
  epsneg = a

  if ( ibeta != 2 and irnd != 0 ):

    a = ( a * ( one + a ) ) / two
    temp = one - a

    if ( temp - one != zero ):
      epsneg = a
#
#  Determine MACHEP and EPS.
#
  machep = -it - 3
  a = b

  while ( True ):

    temp = one + a

    if ( temp - one != zero ):
      break

    a = a * beta
    machep = machep + 1

  eps = a
  temp = tempa + beta * ( one + eps )

  if ( ibeta != 2 and irnd != 0 ):

    a = ( a * ( one + a ) ) / two
    temp = one + a

    if ( temp - one != zero ):
      eps = a
#
#  Determine NGRD.
#
  ngrd = 0
  temp = one + eps

  if ( irnd == 0 and temp * one - one != zero ):
    ngrd = 1
#
#  Determine IEXP, MINEXP and XMIN.
#
#  Loop to determine largest I and K = 2^I such that (1/BETA)^(2^(I))
#  does not underflow.  Exit from loop is signaled by an underflow.
#
  i = 0
  k = 1
  z = betain
  t = one + eps
  nxres = 0

  while ( True ):

    y = z
    z = y * y

    a = z * one
    temp = z * t

    if ( a + a == zero or y <= abs ( z ) ):
      break
 
    temp1 = temp * betain

    if ( temp1 * beta == z ):
      break

    i = i + 1
    k = k + k
#
#  This segment is for nondecimal machines.
#
  if ( ibeta != 10 ):

    iexp = i + 1
    mx = k + k
#
#  This segment is for decimal machines only.
#
  else:

    iexp = 2
    iz = ibeta

    while ( True ):

      if ( k < iz ):
        break

      iz = iz * ibeta
      iexp = iexp + 1

    mx = iz + iz - 1
#
#  Loop to determine MINEXP, XMIN.
#  Exit from loop is signaled by an underflow.
#
  while ( True ):

    xmin = y
    y = y * betain

    a = y * one
    temp = y * t

    if ( a + a == zero or xmin <= abs ( y ) ):
      break

    k = k + 1
    temp1 = temp * betain

    if ( temp1 * beta == y ):
      nxres = 3
      xmin = y
      break

  minexp = -k
#
#  Determine MAXEXP and XMAX.
#
  if ( mx <= k + k - 3 and ibeta != 10 ):
    mx = mx + mx
    iexp = iexp + 1

  maxexp = mx + minexp
#
#  Adjust IRND to reflect partial underflow.
#
  irnd = irnd + nxres
#
#  Adjust for IEEE-style machines.
#
  if ( irnd == 2 or irnd == 5 ):
    maxexp = maxexp - 2
#
#  Adjust for non-IEEE machines with partial underflow.
#
  if ( irnd == 3 or irnd == 4 ):
    maxexp = maxexp - it
#
#  Adjust for machines with implicit leading bit in binary significand,
#  and machines with radix point at extreme right of significand.
#
  i = maxexp + minexp

  if ( ibeta == 2 and i == 0 ):
    maxexp = maxexp - 1

  if ( 20 < i ):
    maxexp = maxexp - 1

  if ( a != y ):
    maxexp = maxexp - 2

  xmax = one - epsneg

  if ( xmax * one != xmax ):
    xmax = one - beta * epsneg

  xmax = xmax / ( beta * beta * beta * xmin )

  i = maxexp + minexp + 3

  for j in range ( 0, i ):

    if ( ibeta == 2 ):
      xmax = xmax + xmax
    else:
      xmax = xmax * beta

  return ibeta, it, irnd, ngrd, machep, negep, iexp, minexp, maxexp, eps, \
    epsneg, xmin, xmax

def r8_machar_test ( ):

#*****************************************************************************80
#
## R8_MACHAR_TEST tests R8_MACHAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 December 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8_MACHAR_TEST' )
  print ( '  R8_MACHAR computes double' )
  print ( '  precision machine constants.' )

  ibeta, it, irnd, ngrd, machep, negep, iexp, minexp, maxexp, eps, epsneg, \
    xmin, xmax = r8_machar ( )

  print ( '' )
  print ( '  IBETA is the internal base for machine arithmetic.' )
  print ( '    IBETA =  %d' % ( ibeta ) )
  print ( '' )
  print ( '  IT is the number of digits, base IBETA, in the' )
  print ( '  floating point significand.' )
  print ( '    IT =     %d' % ( it ) )
  print ( '' )
  print ( '  IRND reports on floating point addition rounding:' )
  print ( '  0, for chopping' )
  print ( '  1, for non-IEEE rounding' )
  print ( '  2, for IEEE rounding' )
  print ( '  3, for chopping with partial underflow' )
  print ( '  4, for non-IEEE rounding with partial underflow.' )
  print ( '  5, for IEEE rounding with partial underflow.' )
  print ( '    IRND =   %d' % ( irnd ) )
  print ( '' )
  print ( '  NGRD is the number of guard digits for floating point' )
  print ( '  multiplication with truncating arithmetic.' )
  print ( '    NGRD =   %d' % ( ngrd ) )
  print ( '' )
  print ( '  MACHEP is the largest negative integer such that' )
  print ( '  1.0 < 1.0 + BETA^MACHEP.' )
  print ( '    MACHEP = %d' % ( machep ) )
  print ( '' )
  print ( '  NEGEPS is the largest negative integer such that' )
  print ( '  1.0 - BETA^NEGEPS < 1.0:' )
  print ( '    NEGEP =  %d' % ( negep ) )
  print ( '' )
  print ( '  IEXP is the number of bits reserved for the exponent' )
  print ( '  of a floating point number:' )
  print ( '    IEXP =   %d' % ( iexp ) )
  print ( '' )
  print ( '  MINEXP is the most negative power of BETA such that' )
  print ( '  BETA^MINEXP is positive and normalized.' )
  print ( '    MINEXP = %d' % ( minexp ) )
  print ( '' )
  print ( '  MAXEXP is the smallest positive power of BETA that' )
  print ( '  overflows:' )
  print ( '    MAXEXP = %d' % ( maxexp ) )
  print ( '' )
  print ( '  EPS is a small positive floating point number' )
  print ( '  such that 1.0 < 1.0 + EPS.' )
  print ( '    EPS    = %26.16e' % ( eps ) )
  print ( '' )
  print ( '  EPSNEG is a small positive floating point number' )
  print ( '  such that 1.0 - EPSNEG < 1.0.' )
  print ( '    EPSNEG = %26.16e' % ( epsneg ) )
  print ( '' )
  print ( '  XMIN is the smallest positive normalized floating' )
  print ( '  point power of the radix:' )
  print ( '    XMIN =   %26.16e' % ( xmin ) )
  print ( '' )
  print ( '  XMAX is the largest finite floating point number:' )
  print ( '    XMAX   = %26.16e' % ( xmax ) )

  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  machar_test ( )
  timestamp ( )

