#! /usr/bin/env python
#
def nco_set ( n ):

#*****************************************************************************80
#
## NCO_SET sets abscissas and weights for open Newton-Cotes quadrature.
#
#  Discussion:
#
#    The open Newton-Cotes rules use equally spaced abscissas, and
#    hence may be used with equally spaced data.
#
#    The rules are called "open" because they do not include the interval
#    endpoints.
#
#    Most of the rules involve negative weights.  These can produce loss
#    of accuracy due to the subtraction of large, nearly equal quantities.
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Abramowitz and Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#    Daniel Zwillinger, editor,
#    Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Parameters:
#
#    Input, integer N, the order.
#    N must be between 1 and 10.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np
  from sys import exit

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n == 1 ):

    w = np.array ( [ \
            2.0 ] )

  elif ( n == 2 ):

    w = np.array ( [ \
           1.0, \
           1.0 ] )

  elif ( n == 3 ):

    d = 3.0

    w = np.array ( [ \
             4.0 / d, \
           - 2.0 / d, \
             4.0 / d ] )

  elif ( n == 4 ):

    d = 12.0

    w = np.array ( [ \
           11.0 / d, \
            1.0 / d, \
            1.0 / d, \
           11.0 / d ] )

  elif ( n == 5 ):

    d = 10.0

    w = np.array ( [ \
             11.0 / d, \
           - 14.0 / d, \
             26.0 / d, \
           - 14.0 / d, \
             11.0 / d ] )

  elif ( n == 6 ):

    d = 1440.0

    w = np.array ( [ \
            1222.0 / d, \
           - 906.0 / d, \
            1124.0 / d, \
            1124.0 / d, \
           - 906.0 / d, \
            1222.0 / d ] )

  elif ( n == 7 ):

    d = 945.0

    w = np.array ( [ \
              920.0 / d, \
           - 1908.0 / d, \
             4392.0 / d, \
           - 4918.0 / d, \
             4392.0 / d, \
           - 1908.0 / d, \
              920.0 / d ] )

  elif ( n == 8 ):

    d = 40320.0

    w = np.array ( [ \
             32166.0 / d, \
           - 50454.0 / d, \
             89406.0 / d, \
           - 30798.0 / d, \
           - 30798.0 / d, \
             89406.0 / d, \
           - 50454.0 / d, \
             32166.0 / d ] )

  elif ( n == 9 ):

    d = 4536.0

    w = np.array ( [ \
              4045.0 / d, \
           - 11690.0 / d, \
             33340.0 / d, \
           - 55070.0 / d, \
             67822.0 / d, \
           - 55070.0 / d, \
             33340.0 / d, \
           - 11690.0 / d, \
              4045.0 / d ] )

  elif ( n == 10 ):

    w = np.array ( [ \
              0.758508873456792, \
             -1.819664627425049, \
              4.319301146384676, \
             -4.708337742504753, \
              2.450192350088813, \
              2.450192350087711, \
             -4.708337742504625, \
              4.319301146384526, \
             -1.819664627425028, \
              0.758508873456790 ] )

  else:

    print ( '' )
    print ( 'NCO_SET - Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    print ( '  Legal values are 1 and 10.' )
    exit ( 'NCO_SET - Fatal error!' )
#
#  Set the abscissas.
#
  for i in range ( 0, n ):
    x[i] = float ( 2 * i - n + 1 ) / float ( n + 1 )

  return x, w

def nco_set_test ( ):

#*****************************************************************************80
#
## NCO_SET_TEST tests NCO_SET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NCO_SET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NCO_SET sets up a Newton-Cotes Open quadrature rule' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = nco_set ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %12g  %12g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NCO_SET_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  nco_set_test ( )
  timestamp ( )

