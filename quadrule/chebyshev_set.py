#! /usr/bin/env python
#
def chebyshev_set ( n ):

#*****************************************************************************80
#
## CHEBYSHEV_SET sets abscissas and weights for Chebyshev quadrature.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#    The Chebyshev rule is distinguished by using equal weights.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964.
#
#    Hermann Engels,
#    Numerical Quadrature and Cubature,
#    Academic Press, 1980.
#
#    Zdenek Kopal,
#    Numerical Analysis,
#    John Wiley, 1955.
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, integer N, the order.
#    N may only have the values 1, 2, 3, 4, 5, 6, 7 or 9.
#    There are NO other Chebyshev rules with real abscissas.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np
  from sys import exit

  if ( n == 1 ):

    x = np.array ( [ \
      0.0 ] )

  elif ( n == 2 ):

    x = np.array ( [ \
      - 1.0 / np.sqrt ( 3.0 ), \
        1.0 / np.sqrt ( 3.0 ) ] )

  elif ( n == 3 ):

    x = np.array ( [ \
      - 1.0 / np.sqrt ( 2.0 ), \
        0.0, \
        1.0 / np.sqrt ( 2.0 ) ] )

  elif ( n == 4 ):

    x = np.array ( [ \
        - np.sqrt ( ( 1.0 + 2.0 / np.sqrt ( 5.0 ) ) / 3.0 ), \
        - np.sqrt ( ( 1.0 - 2.0 / np.sqrt ( 5.0 ) ) / 3.0 ), \
          np.sqrt ( ( 1.0 - 2.0 / np.sqrt ( 5.0 ) ) / 3.0 ), \
          np.sqrt ( ( 1.0 + 2.0 / np.sqrt ( 5.0 ) ) / 3.0 ) ] )

  elif ( n == 5 ):

    x = np.array ( [ \
      - np.sqrt ( ( 5.0 + np.sqrt ( 11.0) ) / 12.0 ), \
      - np.sqrt ( ( 5.0 - np.sqrt ( 11.0) ) / 12.0 ), \
        0.0, \
        np.sqrt ( ( 5.0 - np.sqrt ( 11.0) ) / 12.0 ), \
        np.sqrt ( ( 5.0 + np.sqrt ( 11.0) ) / 12.0 ) ] )

  elif ( n == 6 ):

    x = np.array ( [ \
      - 0.866246818107820591383598, \
      - 0.422518653761111529118546, \
      - 0.266635401516704720331534, \
        0.266635401516704720331534, \
        0.422518653761111529118546, \
        0.866246818107820591383598 ] )

  elif ( n == 7 ):

    x = np.array ( [ \
      - 0.883861700758049035704224, \
      - 0.529656775285156811385048, \
      - 0.323911810519907637519673, \
        0.0, \
        0.323911810519907637519673, \
        0.529656775285156811385048, \
        0.883861700758049035704224 ] )

  elif ( n == 9 ):

    x = np.array ( [ \
      - 0.911589307728434473664949, \
      - 0.601018655380238071428128, \
      - 0.528761783057879993260181, \
      - 0.167906184214803943068031, \
        0.0, \
        0.167906184214803943068031, \
        0.528761783057879993260181, \
        0.601018655380238071428128, \
        0.911589307728434473664949 ] )

  else:

    print ( '' )
    print ( 'CHEBYSHEV_SET - Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 through 7, and 9.' )
    exit ( 'CHEBYSHEV_SET - Fatal error!' )

  w = np.zeros ( n )
  for i in range ( 0, n ):
    w[i] = 2.0 / float ( n )

  return x, w

def chebyshev_set_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV_SET_TEST tests CHEBYSHEV_SET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHEBYSHEV_SET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHEBYSHEV_SET sets' )
  print ( '  a Chebyshev quadrature rule over [-1,1]' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 10 ):

    if ( n == 8 ):
      continue

    x, w = chebyshev_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBYSHEV_SET_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chebyshev_set_test ( )
  timestamp ( )

