#! /usr/bin/env python
#
def r8_fac ( n ):

#*****************************************************************************80
#
## R8_FAC evaluates the factorial of an I4 argument.
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
#    Input, integer N, the argument.
#
#    Output, real VALUE, the factorial of N.
#
  import numpy as np
  from r8_aint import r8_aint
  from r8_csevl import r8_csevl
  from r8_gaml import r8_gaml
  from r8_inits import r8_inits
  from r8_lgmc import r8_lgmc
  from machine import r8_mach
  from sys import exit

  sq2pil = 0.91893853320467274178032973640562

  facn = np.array ( [ \
      +0.100000000000000000000000000000000E+01, \
      +0.100000000000000000000000000000000E+01, \
      +0.200000000000000000000000000000000E+01, \
      +0.600000000000000000000000000000000E+01, \
      +0.240000000000000000000000000000000E+02, \
      +0.120000000000000000000000000000000E+03, \
      +0.720000000000000000000000000000000E+03, \
      +0.504000000000000000000000000000000E+04, \
      +0.403200000000000000000000000000000E+05, \
      +0.362880000000000000000000000000000E+06, \
      +0.362880000000000000000000000000000E+07, \
      +0.399168000000000000000000000000000E+08, \
      +0.479001600000000000000000000000000E+09, \
      +0.622702080000000000000000000000000E+10, \
      +0.871782912000000000000000000000000E+11, \
      +0.130767436800000000000000000000000E+13, \
      +0.209227898880000000000000000000000E+14, \
      +0.355687428096000000000000000000000E+15, \
      +0.640237370572800000000000000000000E+16, \
      +0.121645100408832000000000000000000E+18, \
      +0.243290200817664000000000000000000E+19, \
      +0.510909421717094400000000000000000E+20, \
      +0.112400072777760768000000000000000E+22, \
      +0.258520167388849766400000000000000E+23, \
      +0.620448401733239439360000000000000E+24, \
      +0.155112100433309859840000000000000E+26, \
      +0.403291461126605635584000000000000E+27, \
      +0.108888694504183521607680000000000E+29, \
      +0.304888344611713860501504000000000E+30, \
      +0.884176199373970195454361600000000E+31, \
      +0.265252859812191058636308480000000E+33 ] )

  xmin, xmax = r8_gaml ( )
  nmax = int ( r8_aint ( xmax - 1.0 ) )

  if ( n < 0 ):

    print ( '' )
    print ( 'R8_FAC - Fatal error!' )
    print ( '  Input argument is negative.' )
    exit ( 'R8_FAC - Fatal error!' )

  elif ( n <= 30 ):

    value = facn[n]

  elif ( n <= nmax ):

    x = float ( n + 1 )
    value = np.exp ( ( x - 0.5 ) * np.log ( x ) - x + sq2pil + r8_lgmc ( x ) )

  else:

    print ( '' )
    print ( 'R8_FAC - Fatal error!' )
    print ( '  Factorial overflows.' )
    exit ( 'R8_FAC - Fatal error!' )

  return value

def r8_fac_test ( ):

#*****************************************************************************80
#
## R8_FAC_TEST tests R8_FAC.
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
  from r8_factorial_values import r8_factorial_values

  print ( '' )
  print ( 'R8_FAC_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FAC evaluates the factorial function.' )
  print ( '' )
  print ( '             N          FAC(N)  R8_FAC(N)        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fx1 = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_fac ( n )

    print ( '  %14d  %14.6g  %14.6g  %14.6g' % ( n, fx1, fx2, abs ( fx1 - fx2 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FAC_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_fac_test ( )
  timestamp ( )
