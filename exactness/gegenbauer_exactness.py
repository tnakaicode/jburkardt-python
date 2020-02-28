#! /usr/bin/env python
#
def gegenbauer_exactness ( n, x, w, p_max, lam ):

#*****************************************************************************80
#
## GEGENBAUER_EXACTNESS investigates exactness of Gegenbauer quadrature.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of points in the rule.
#
#    Input, real X(N), the quadrature points.
#
#    Input, real W(N), the quadrature weights.
#
#    Input, integer P_MAX, the maximum exponent.
#    0 <= P_MAX.
#
#    Input, real LAMBDA, the parameter.
#    -1/2 < LMMBDA.
#
  import numpy as np
  from gegenbauer_integral import gegenbauer_integral

  print ( '' )
  print ( 'GEGENBAUER_EXACTNESS:' )
  print ( '  Quadrature rule for Gegenbauer integral.' )
  print ( '  Lambda = %g' % ( lam ) )
  print ( '  Rule of order N = %d' % ( n ) )
  print ( '  Degree          Relative Error' )
  print ( '' )

  for p in range ( 0, p_max + 1 ):

    s = gegenbauer_integral ( p, lam )

    v = np.zeros ( n )

    for i in range ( 0, n ):
      v[i] = x[i] ** p

    q = np.dot ( w, v )

    if ( s == 0.0 ):
      e = abs ( q - s )
    else:
      e = abs ( ( q - s ) / s )

    print ( '  %6d  %24.16f' % ( p, e ) )

  return

def gegenbauer_exactness_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_EXACTNESS_TEST tests Gauss-Gegenbauer rules for Gegenbauer integrals.
#
#  Discussion:
#
#    The Gegenbauer integral includes a parameter LAMBDA.  Thus the
#    corresponding quadrature rules depend both on the order and LAMBDA.
#    Thus it is usual to compute a particular rule when needed, rather
#    than trying to maintain tabulated data.  Here, we simply supply
#    precomputed rules of orders 1 through 5 for the case LAMBDA = 1.75.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from gegenbauer_integral import gegenbauer_integral

  lam = 1.75

  print ( '' )
  print ( 'GEGENBAUER_EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test Gauss-Gegenbauer rules on Gegenbauer integrals.' )
  print ( '  Density function rho(x) = 1.' )
  print ( '  Using Lambda = %g' % ( lam ) )
  print ( '  Region: -1 <= x <= +1.' )
  print ( '  Exactness: 2*N-1.' )

  for n in range ( 1, 6 ):

    if ( n == 1 ):
      x = np.array ( [ \
        0.0000000000000000 ] )
      w = np.array ( [ \
        1.2485988353771993 ] )
    elif ( n == 2 ):
      x = np.array ( [ \
       -0.4264014327112208, \
        0.4264014327112208 ] )
      w = np.array ( [ \
        0.6242994176885995, \
        0.6242994176885995 ] )
    elif ( n == 3 ):
      x = np.array ( [ \
       -0.6324555320336757, \
        0.0000000000000000, \
        0.6324555320336757 ] )
      w = np.array ( [ \
        0.2837724625857273, \
        0.6810539102057455, \
        0.2837724625857273 ] )
    elif ( n == 4 ):
      x = np.array ( [ \
       -0.7455376618816977, \
       -0.2752317970082527, \
        0.2752317970082527, \
        0.7455376618816980 ] )
      w = np.array ( [ \
        0.1379302690657785, \
        0.4863691486228214, \
        0.4863691486228208, \
        0.1379302690657786 ] )
    elif ( n == 5 ):
      x = np.array ( [ \
       -0.8137803260309515, \
       -0.4553315257658559, \
        0.0000000000000001, \
        0.4553315257658557, \
        0.8137803260309517 ] )
      w = np.array ( [ \
        0.0725955752894624, \
        0.3156051535278124, \
        0.4721973777426502, \
        0.3156051535278118, \
        0.0725955752894624 ] )

    p_max = 2 * n
    gegenbauer_exactness ( n, x, w, p_max, lam )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  gegenbauer_exactness_test ( )
  timestamp ( )
 
