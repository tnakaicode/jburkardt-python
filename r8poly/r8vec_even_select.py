#! /usr/bin/env python3
#
def r8vec_even_select ( n, xlo, xhi, ival ):

#*****************************************************************************80
#
## R8VEC_EVEN_SELECT returns the I-th of N evenly spaced values in [ XLO, XHI ].
#
#  Discussion:
#
#    XVAL = ( (N-IVAL) * XLO + (IVAL-1) * XHI ) / dble ( N - 1 )
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
#  Parameters:
#
#    Input, integer N, the number of values.
#
#    Input, real XLO, XHI, the low and high values.
#
#    Input, integer IVAL, the index of the desired point.
#    IVAL is normally between 1 and N, but may be any
#    integer value.
#
#    Output, real XVAL, the IVAL-th of N evenly spaced values
#    between XLO and XHI.
#
#    Unless N = 1, X(1) = XLO and X(N) = XHI.
#
#    If N = 1, then X(1) = 0.5*(XLO+XHI).
#
  if ( n == 1 ):

    xval = 0.5 * ( xlo + xhi )

  else:

    xval = ( float ( n - ival     ) * xlo   \
           + float (     ival - 1 ) * xhi ) \
           / float ( n        - 1 )

  return xval

def r8vec_even_select_test ( ):

#*****************************************************************************80
#
## R8VEC_EVEN_SELECT_TEST tests R8VEC_EVEN_SELECT.
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
  n = 10
  xlo = 0.0
  xhi = 99.0
 
  print ( '' )
  print ( 'R8VEC_EVEN_SELECT_TEST' )
  print ( '  R8VEC_EVEN_SELECT returns the I-th of N evenly spaced values' )
  print ( '  between XLO and XHI.' )
  print ( '' )
  print ( '  XLO = %f' % ( xlo ) )
  print ( '  XHI = %f' % ( xhi ) )
  print ( '  while N = %d' % ( n ) )
  print ( '' )
 
  for i in range ( 2, n + 1, 3 ):
    xi = r8vec_even_select ( n, xlo, xhi, i )
    print ( '  X(%d) = %g' % ( i, xi ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_EVEN_SELECT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_even_select_test ( )
  timestamp ( )

