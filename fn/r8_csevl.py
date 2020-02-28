#! /usr/bin/env python
#
def r8_csevl ( x, a, n ):

#*****************************************************************************80
#
## R8_CSEVL evaluates a Chebyshev series.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Roger Broucke,
#    Algorithm 446:
#    Ten Subroutines for the Manipulation of Chebyshev Series,
#    Communications of the ACM,
#    Volume 16, Number 4, April 1973, pages 254-256.
#
#  Parameters:
#
#    Input, real X, the evaluation point.
#
#    Input, real CS(N), the Chebyshev coefficients.
#
#    Input, integer N, the number of Chebyshev coefficients.
#
#    Output, real VALUE, the Chebyshev series evaluated at X.
#
  from sys import exit

  if ( n < 1 ):
    print ( '' )
    print ( 'R8_CSEVL - Fatal error!' )
    print ( '  Number of terms <= 0.' )
    exit ( 'R8_CSEVL - Fatal error!' )

  if ( 1000 < n ):
    print ( '' )
    print ( 'R8_CSEVL - Fatal error!' )
    print ( '  Number of terms > 1000.' )
    exit ( 'R8_CSEVL - Fatal error!' )

  if ( x < -1.1 or 1.1 < x ):
    print ( '' )
    print ( 'R8_CSEVL - Fatal error!' )
    print ( '  X outside (-1,+1)' )
    print ( '  X = %g' % ( x ) )
    exit ( 'R8_CSEVL - Fatal error!' )

  b1 = 0.0
  b0 = 0.0

  for i in range ( n - 1, -1, -1 ):
    b2 = b1
    b1 = b0
    b0 = 2.0 * x * b1 - b2 + a[i]

  value = 0.5 * ( b0 - b2 )

  return value

def r8_csevl_test ( ):

#*****************************************************************************80
#
## R8_CSEVL_TEST tests R8_CSEVL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  expcs = np.array ( [ \
   2.532131755504016E+00, \
   1.130318207984970E+00, \
   0.271495339534077E+00, \
   0.044336849848664E+00, \
   0.005474240442094E+00, \
   0.000542926311914E+00, \
   0.000044977322954E+00, \
   0.000003198436462E+00, \
   0.000000199212481E+00, \
   0.000000011036772E+00, \
   0.000000000550590E+00, \
   0.000000000024980E+00, \
   0.000000000001039E+00, \
   0.000000000000040E+00, \
   0.000000000000001E+00 ] )

  print ( '' )
  print ( 'R8_CSEVL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CSEVL evaluates a Chebyshev approximant' )
  print ( '  of N terms at a point X.' )
  print ( '' )
  print ( '  Here we use an approximant to the exponential function' )
  print ( '  and average the absolute error at 21 points.' )
  print ( '' )
  print ( '   N    error' )
  print ( '' )

  for n in range ( 1, 13 ):
    err = 0.0
    for i in range ( -10, 11 ):
      x = float ( i ) / 10.0
      s = r8_csevl ( x, expcs, n )
      err = err + abs ( s - np.exp ( x ) )
    err = err / 21.0
    print ( '  %2d  %14.6g' % ( n, err ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CSEVL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_csevl_test ( )
  timestamp ( )
