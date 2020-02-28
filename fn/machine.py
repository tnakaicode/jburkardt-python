#! /usr/bin/env python
#
def r8_mach ( i ):

#*****************************************************************************80
#
## R8_MACH returns double precision real machine constants.
#
#  Discussion:
#
#    Assume that double precision real numbers are stored with a mantissa
#    of T digits in base B, with an exponent whose value must lie
#    between EMIN and EMAX.  Then for values of I between 1 and 5,
#    R8_MACH will return the following values:
#
#      R8_MACH(1) = B^(EMIN-1), the smallest positive magnitude.
#      R8_MACH(2) = B^EMAX*(1-B^(-T)), the largest magnitude.
#      R8_MACH(3) = B^(-T), the smallest relative spacing.
#      R8_MACH(4) = B^(1-T), the largest relative spacing.
#      R8_MACH(5) = log10(B)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    Original FORTRAN77 version by Phyllis Fox, Andrew Hall, Norman Schryer
#    Python version by John Burkardt.
#
#  Reference:
#
#    Phyllis Fox, Andrew Hall, Norman Schryer,
#    Algorithm 528,
#    Framework for a Portable Library,
#    ACM Transactions on Mathematical Software,
#    Volume 4, Number 2, June 1978, page 176-188.
#
#  Parameters:
#
#    Input, integer I, chooses the parameter to be returned.
#    1 <= I <= 5.
#
#    Output, real VALUE, the value of the chosen parameter.
#
  if ( i < 1 ):
    print ( '' )
    print ( 'R8_MACH - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    sys.exit ( 'R8_MACH - Fatal error!' )
  elif ( i == 1 ):
    value = 1.112536929253601E-308
  elif ( i == 2 ):
    value = 4.494232837155789E+307
  elif ( i == 3 ):
    value = 1.110223024625157E-016
  elif ( i == 4 ):
    value = 2.220446049250313E-016
  elif ( i == 5 ):
    value = 0.301029995663981
  elif ( 5 < i ):
    print ( '' )
    print ( 'R8_MACH - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    sys.exit ( 'R8_MACH - Fatal error!' )

  return value

def r8_mach_test ( ):

#*****************************************************************************80
#
## R8_MACH_TEST reports the constants returned by R8_MACH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_MACH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_MACH reports the value of constants associated' )
  print ( '  with real double precision computer arithmetic.' )

  print ( '' )
  print ( '  Assume that double precision numbers are stored ' )
  print ( '  with a mantissa of T digits in base B, with an' )
  print ( '  exponent whose value must lie between EMIN and EMAX.' )

  print ( '' )
  print ( '  For input arguments of 1 <= I <= 5,' )
  print ( '  R8_MACH will return the following values:' )

  print ( '' )
  print ( '  R8_MACH(1) = B^(EMIN-1), the smallest positive magnitude.' )
  print ( '  %26.16e' % ( r8_mach ( 1 ) ) )

  print ( '' )
  print ( '  R8_MACH(2) = B^EMAX*(1-B^(-T)), the largest magnitude.' )
  print ( '  %26.16e' % ( r8_mach ( 2 ) ) )

  print ( '' )
  print ( '  R8_MACH(3) = B^(-T), the smallest relative spacing.' )
  print ( '  %26.16e' % ( r8_mach ( 3 ) ) )

  print ( '' )
  print ( '  R8_MACH(4) = B^(1-T), the largest relative spacing.' )
  print ( '  %26.16e' % ( r8_mach ( 4 ) ) )

  print ( '' )
  print ( '  R8_MACH(5) = log10(B).' )
  print ( '  %26.16e' % ( r8_mach ( 5 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_MACH_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_mach ( i ):

#*****************************************************************************80
#
## I4_MACH returns integer machine constants.
#
#  Discussion:
#
#    Input/output unit numbers.
#
#      I4_MACH(1) = the standard input unit.
#      I4_MACH(2) = the standard output unit.
#      I4_MACH(3) = the standard punch unit.
#      I4_MACH(4) = the standard error message unit.
#
#    Words.
#
#      I4_MACH(5) = the number of bits per integer storage unit.
#      I4_MACH(6) = the number of characters per integer storage unit.
#
#    Integers.
#
#    Assume integers are represented in the S digit base A form:
#
#      Sign * (X(S-1)*A^(S-1) + ... + X(1)*A + X(0))
#
#    where 0 <= X(1:S-1) < A.
#
#      I4_MACH(7) = A, the base.
#      I4_MACH(8) = S, the number of base A digits.
#      I4_MACH(9) = A^S-1, the largest integer.
#
#    Floating point numbers
#
#    Assume floating point numbers are represented in the T digit
#    base B form:
#
#      Sign * (B^E) * ((X(1)/B) + ... + (X(T)/B^T) )
#
#    where 0 <= X(I) < B for I=1 to T, 0 < X(1) and EMIN <= E <= EMAX.
#
#      I4_MACH(10) = B, the base.
#
#    Single precision
#
#      I4_MACH(11) = T, the number of base B digits.
#      I4_MACH(12) = EMIN, the smallest exponent E.
#      I4_MACH(13) = EMAX, the largest exponent E.
#
#    Double precision
#
#      I4_MACH(14) = T, the number of base B digits.
#      I4_MACH(15) = EMIN, the smallest exponent E.
#      I4_MACH(16) = EMAX, the largest exponent E.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    Original FORTRAN77 version by Phyllis Fox, Andrew Hall, Norman Schryer
#    Python version by John Burkardt.
#
#  Reference:
#
#    Phyllis Fox, Andrew Hall, Norman Schryer,
#    Algorithm 528,
#    Framework for a Portable Library,
#    ACM Transactions on Mathematical Software,
#    Volume 4, Number 2, June 1978, page 176-188.
#
#  Parameters:
#
#    Input, integer I, chooses the parameter to be returned.
#    1 <= I <= 16.
#
#    Output, integer VALUE, the value of the chosen parameter.
#
  if ( i < 1 ):
    print ( '' )
    print ( 'I4_MACH - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 16.' )
    print ( '  I =   %d' % ( i ) )
    sys.exit ( 'I4_MACH - Fatal error!' )
  elif ( i == 1 ):
    value = 5
  elif ( i == 2 ):
    value = 6
  elif ( i == 3 ):
    value = 7
  elif ( i == 4 ):
    value = 6
  elif ( i == 5 ):
    value = 32
  elif ( i == 6 ):
    value = 4
  elif ( i == 7 ):
    value = 2
  elif ( i == 8 ):
    value = 31
  elif ( i == 9 ):
    value = 2147483647
  elif ( i == 10 ):
    value = 2
  elif ( i == 11 ):
    value = 24
  elif ( i == 12 ):
    value = -125
  elif ( i == 13 ):
    value = 128
  elif ( i == 14 ):
    value = 53
  elif ( i == 15 ):
    value = -1021
  elif ( i == 16 ):
    value = 1024
  elif ( 16 < i ):
    print ( '' )
    print ( 'I4_MACH - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 16.' )
    print ( '  I =   %d' % ( i ) )
    sys.exit ( 'I4_MACH - Fatal error!' )

  return value

def i4_mach_test ( ):

#*****************************************************************************80
#
## I4_MACH_TEST reports the constants returned by I4_MACH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_MACH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_MACH reports the value of constants associated' )
  print ( '  with integer computer arithmetic.' )

  print ( '' )
  print ( '  Numbers associated with input/output units:' )

  print ( '' )
  print ( '  I4_MACH(1) = the standard input unit.' )
  print ( '  %d' % ( i4_mach ( 1 ) ) )

  print ( '' )
  print ( '  I4_MACH(2) = the standard output unit.' )
  print ( '  %d' % ( i4_mach ( 2 ) ) )

  print ( '' )
  print ( '  I4_MACH(3) = the standard punch unit.' )
  print ( '  %d' % ( i4_mach ( 3 ) ) )

  print ( '' )
  print ( '  I4_MACH(4) = the standard error message unit.' )
  print ( '  %d' % ( i4_mach ( 4 ) ) )

  print ( '' )
  print ( '  Numbers associated with words:' )

  print ( '' )
  print ( '  I4_MACH(5) = the number of bits per integer.' )
  print ( '  %d' % ( i4_mach ( 5 ) ) )

  print ( '' )
  print ( '  I4_MACH(6) = the number of characters per integer.' )
  print ( '  %d' % ( i4_mach ( 6 ) ) )

  print ( '' )
  print ( '  Numbers associated with integer values:' )

  print ( '' )
  print ( '  Assume integers are represented in the S digit' )
  print ( '  base A form:' )
  print ( '' )
  print ( '    Sign * (X(S-1)*A^(S-1) + ... + X(1)*A + X(0))' )
  print ( '' )
  print ( '  where the digits X satisfy 0 <= X(1:S-1) < A.' )

  print ( '' )
  print ( '  I4_MACH(7) = A, the base.' )
  print ( '  %d' % ( i4_mach ( 7 ) ) )

  print ( '' )
  print ( '  I4_MACH(8) = S, the number of base A digits.' )
  print ( '  %d' % ( i4_mach ( 8 ) ) )

  print ( '' )
  print ( '  I4_MACH(9) = A^S-1, the largest integer.' )
  print ( '  %d' % ( i4_mach ( 9 ) ) )

  print ( '' )
  print ( '  Numbers associated with floating point values:' )
  print ( '' )
  print ( '  Assume floating point numbers are represented ' )
  print ( '  in the T digit base B form:' )
  print ( '' )
  print ( '    Sign * (B^E) * ((X(1)/B) + ... + (X(T)/B^T) )' )
  print ( '' )
  print ( '  where' )
  print ( '' )
  print ( '    0 <= X(1:T) < B,' )
  print ( '    0 < X(1) (unless the value being represented is 0),' )
  print ( '    EMIN <= E <= EMAX.' )

  print ( '' )
  print ( '  I4_MACH(10) = B, the base.' )
  print ( '  %d' % ( i4_mach ( 10 ) ) )

  print ( '' )
  print ( '  Numbers associated with single precision values:' )
  print ( '' )
  print ( '  I4_MACH(11) = T, the number of base B digits.' )
  print ( '  %d' % ( i4_mach ( 11 ) ) )

  print ( '' )
  print ( '  I4_MACH(12) = EMIN, the smallest exponent E.' )
  print ( '  %d' % ( i4_mach ( 12 ) ) )

  print ( '' )
  print ( '  I4_MACH(13) = EMAX, the largest exponent E.' )
  print ( '  %d' % ( i4_mach ( 13 ) ) )

  print ( '' )
  print ( '  Numbers associated with double precision values:' )
  print ( '' )
  print ( '  I4_MACH(14) = T, the number of base B digits.' )
  print ( '  %d' % ( i4_mach ( 14 ) ) )

  print ( '' )
  print ( '  I4_MACH(15) = EMIN, the smallest exponent E.' )
  print ( '  %d' % ( i4_mach ( 15 ) ) )

  print ( '' )
  print ( '  I4_MACH(16) = EMAX, the largest exponent E.' )
  print ( '  %d' % ( i4_mach ( 16 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_MACH_TEST' )
  print ( '  Normal end of execution.' )
  return

def machine_test ( ):

#*****************************************************************************80
#
## MACHINE_TEST tests the MACHINE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'MACHINE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the MACHINE library.' )

  r8_mach_test ( )
  i4_mach_test ( )
  r4_mach_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'MACHINE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4_mach ( i ):

#*****************************************************************************80
#
## R4_MACH returns single precision real machine constants.
#
#  Discussion:
#
#    Assume that single precision real numbers are stored with a mantissa
#    of T digits in base B, with an exponent whose value must lie
#    between EMIN and EMAX.  Then for values of I between 1 and 5,
#    R4_MACH will return the following values:
#
#      R4_MACH(1) = B^(EMIN-1), the smallest positive magnitude.
#      R4_MACH(2) = B^EMAX*(1-B^(-T)), the largest magnitude.
#      R4_MACH(3) = B^(-T), the smallest relative spacing.
#      R4_MACH(4) = B^(1-T), the largest relative spacing.
#      R4_MACH(5) = log10(B)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    Original FORTRAN77 version by Phyllis Fox, Andrew Hall, Norman Schryer
#    Python version by John Burkardt.
#
#  Reference:
#
#    Phyllis Fox, Andrew Hall, Norman Schryer,
#    Algorithm 528,
#    Framework for a Portable Library,
#    ACM Transactions on Mathematical Software,
#    Volume 4, Number 2, June 1978, page 176-188.
#
#  Parameters:
#
#    Input, integer I, chooses the parameter to be returned.
#    1 <= I <= 5.
#
#    Output, real VALUE, the value of the chosen parameter.
#
  if ( i < 1 ):
    print ( '' )
    print ( 'R4_MACH - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    sys.exit ( 'R4_MACH - Fatal error!' )
  elif ( i == 1 ):
    value = 1.1754944E-38
  elif ( i == 2 ):
    value = 3.4028235E+38
  elif ( i == 3 ):
    value = 5.9604645E-08
  elif ( i == 4 ):
    value = 1.1920929E-07
  elif ( i == 5 ):
    value = 0.3010300
  elif ( 5 < i ):
    print ( '' )
    print ( 'R4_MACH - Fatal error!' )
    print ( '  The input argument I is out of bounds.' )
    print ( '  Legal values satisfy 1 <= I <= 5.' )
    print ( '  I = %d' % ( i ) )
    sys.exit ( 'R4_MACH - Fatal error!' )

  return value

def r4_mach_test ( ):

#*****************************************************************************80
#
## R4_MACH_TEST reports the constants returned by R4_MACH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R4_MACH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4_MACH reports the value of constants associated' )
  print ( '  with real single precision computer arithmetic.' )

  print ( '' )
  print ( '  Assume that single precision numbers are stored ' )
  print ( '  with a mantissa of T digits in base B, with an ' )
  print ( '  exponent whose value must lie between EMIN and EMAX.' )

  print ( '' )
  print ( '  For input arguments of 1 <= I <= 5,' )
  print ( '  R4_MACH will return the following values:' )

  print ( '' )
  print ( '  R4_MACH(1) = B^(EMIN-1), the smallest positive magnitude.' )
  print ( '  %26.16e' % ( r4_mach ( 1 ) ) )

  print ( '' )
  print ( '  R4_MACH(2) = B^EMAX*(1-B^(-T)), the largest magnitude.' )
  print ( '  %26.16e' % ( r4_mach ( 2 ) ) )

  print ( '' )
  print ( '  R4_MACH(3) = B^(-T), the smallest relative spacing.' )
  print ( '  %26.16e' % ( r4_mach ( 3 ) ) )

  print ( '' )
  print ( '  R4_MACH(4) = B^(1-T), the largest relative spacing.' )
  print ( '  %26.16e' % ( r4_mach ( 4 ) ) )

  print ( '' )
  print ( '  R4_MACH(5) = log10(B).' )
  print ( '  %26.16e' % ( r4_mach ( 5 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4_MACH_TEST' )
  print ( '  Normal end of execution.' )
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
  machine_test ( )
  timestamp ( )

