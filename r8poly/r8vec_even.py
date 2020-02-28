#! /usr/bin/env python3
#
def r8vec_even ( n, alo, ahi ):

#*****************************************************************************80
#
## R8VEC_EVEN returns N real values, evenly spaced between ALO and AHI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 January 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of values.
#
#    Input, real ALO, AHI, the low and high values.
#
#    Output, real A(N), N evenly spaced values.
#    Normally, A(1) = ALO and A(N) = AHI.
#    However, if N = 1, then A(1) = 0.5*(ALO+AHI).
#
  import numpy as np

  a = np.zeros ( n )

  if ( n == 1 ):

    a[0] = 0.5 * ( alo + ahi )

  else:

    for i in range ( 0, n ):
      a[i] = ( ( n - 1 - i ) * alo + i * ahi ) / float ( n - 1 )

  return a

def r8vec_even_test ( ):

#*****************************************************************************80
#
## R8VEC_EVEN_TEST tests R8VEC_EVEN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
  from r8vec_print import r8vec_print

  n = 10
  xlo = 0.0
  xhi = 99.0
 
  print ( '' )
  print ( 'R8VEC_EVEN_TEST' )
  print ( '  R8VEC_EVEN computes N evenly spaced values' )
  print ( '  between XLO and XHI.' )
  print ( '' )
  print ( '  XLO = %f' % ( xlo ) )
  print ( '  XHI = %f' % ( xhi ) )
  print ( '  while N = %d' % ( n ) )
 
  x = r8vec_even ( n, xlo, xhi )
 
  r8vec_print ( n, x, '  Resulting array:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_EVEN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_even_test ( )
  timestamp ( )

