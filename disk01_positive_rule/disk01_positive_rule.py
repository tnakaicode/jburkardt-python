#! /usr/bin/env python3
#
def disk01_positive_rule_test ( ):

#*****************************************************************************80
#
## disk01_positive_rule_test() tests disk01_positive_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk01_positive_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test disk01_positive_rule().' )

  n = 3
  d = 2

  disk01_positive_rule ( n, d )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk01_positive_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def disk01_positive_area ( ):

#*****************************************************************************80
#
## disk01_positive_area() returns the area of the unit positive disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real AREA, the area of the unit positive disk.
#
  import numpy as np

  r = 1.0
  area = 0.25 * np.pi * r * r

  return area

def disk01_positive_monomial_integral ( e ):

#*****************************************************************************80
#
## disk01_positive_monomial_integral(): monomial integrals in unit positive disk.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 <= 1.
#      0 <= X, 0 <= Y.
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E(2), the exponents of X and Y in the 
#    monomial.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  from scipy.special import gamma

  f1 = gamma ( ( e[0]        + 3 ) / 2.0 )
  f2 = gamma ( (        e[1] + 1 ) / 2.0 )
  f3 = gamma ( ( e[0] + e[1] + 4 ) / 2.0 )

  integral = f1 * f2 / f3 / 2.0 / ( 1.0 + e[0] )

  return integral

def disk01_positive_rule ( n, d ):

#*****************************************************************************80
#
## disk01_positive_rule() computes a quadrature rule for the unit positive disk.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 <= 1.
#      0 <= X, 0 <= Y.
#
#    The number of degrees of freedom is DOF = 3 * N.  This should be
#    greater than or equal to ( D + 1 ) * ( D + 2 ) / 2.
#  
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    integer D, the total degree precision of the rule.
#
  from scipy.optimize import least_squares
  import numpy as np
  import pprint

  print ( '' )
  print ( 'disk01_positive_rule():' )
  print ( '  Determine a quadrature rule for the unit positive disk.' )

  dof = 3 * n
  resid_num = int ( ( d + 1 ) * ( d + 2 ) // 2 )

  print ( '' )
  print ( '  Number of points in rule is ', n )
  print ( '  The degree of precision will be ', d )
  print ( '  The number of degrees of freedom is ', dof )
  print ( '  The number of monomial integrals to match is ', resid_num ) 

  if ( dof < resid_num ):
    print ( '' )
    print ( 'disk01_positive_rule(): Warning!' )
    print ( '  Number of degrees of freedom is lower than number of integrals to match.' )
    print ( '  A quadrature rule, if found, is unlikely to be exact.' )
#
#  WXY0 contains the initial guess for the W's, X's, and Y's.
#
  angle = ( np.pi / 2.0 ) * ( 2 * np.arange ( 0, n ) + 1 ) / ( 2 * n )

  wxy0 = np.zeros ( [ n, 3 ] )
  wxy0[:,0] = disk01_positive_area ( ) / n
  wxy0[:,1] = 0.5 * np.cos ( angle )
  wxy0[:,2] = 0.5 * np.sin ( angle )
#
#  Print the initial quess.
#
  print ( '' )
  print ( '  Initial guess for W, X, Y values:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %14.6g  %14.6g  %14.6g' % ( wxy0[i,0], wxy0[i,1], wxy0[i,2] ) )
#
#  Flatten WXY0.
#
  wxy0_flat = wxy0.flatten ( )
#
#  Determine solution of nonlinear system defining the
#  quadrature rule.
#
  lsq = least_squares ( disk01_positive_resid, wxy0_flat )
  wxy_flat = lsq.x
#
#  Unflatten the result.
#
  wxy = wxy_flat.reshape ( n, 3 )
#
#  Print solution.
#
  print ( '' )
  print ( '  FSOLVE solves for W, X, Y values:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %14.6g  %14.6g  %14.6g' % ( wxy[i,0], wxy[i,1], wxy[i,2] ) )

  resid = disk01_positive_resid ( wxy )
  print ( '' )
  print ( '  Residuals for WXY:' )
  pprint.pprint ( resid )
#
#  Test the quadrature rule.
#
  w = wxy[:,0]
  x = wxy[:,1]
  y = wxy[:,2]

  print ( '' )
  print ( '  Monomial       Estimate           Exact       Error' )
  print ( '' )

  k = 0
  for dsub in range ( 0, d + 1 ):
    for d1 in range ( dsub, -1, -1 ):
      d2 = dsub - d1
      e = np.array ( [ d1, d2 ] )
      r = disk01_positive_monomial_integral ( e )
      resid[k] = np.sum ( w * x**d1 * y**d2 )
      print ( '  x^%d*y^%d  %14.6g  %14.6g  %14.6g' \
        % ( d1, d2, resid[k], r, np.abs ( resid[k] - r ) ) )
      k = k + 1

  return

def disk01_positive_resid ( wxy_flat ):

#*****************************************************************************80
#
## disk01_positive_resid() evaluates the unit positive disk quadrature rule residual.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 <= 1.
#      0 <= X, 0 <= Y.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real WXY[N,3], the W, X and Y values of a quadrature rule
#    of desired precision D.
#
#  Output:
#
#    real resid( D * ( D + 1 ) / 2 ), the residual of the quadrature equations:
#    resid(0) = Q(1) - I(1)
#    resid(1) = Q(x) - I(x)
#    resid(2) = Q(y) - I(y)
#    resid(3) = Q(x^2) - I(x^2)
#    resid(4) = Q(xy) - I(xy)
#    resid(5) = Q(y^2) - I(y^2) and so on.
#
  import numpy as np

  n = 3
  dof = 3 * n
  d = 2

  wxy = wxy_flat.reshape ( n, 3 )

  w = wxy[:,0]
  x = wxy[:,1]
  y = wxy[:,2]

  resid_num = int ( ( ( d + 1 ) * ( d + 2 ) ) // 2 )
  resid = np.zeros ( resid_num )
  
  k = 0
  for dsub in range ( 0, d + 1 ):
    for d1 in range ( dsub, -1, -1 ):
      d2 = dsub - d1
      e = np.array ( [ d1, d2 ] )
      r = disk01_positive_monomial_integral ( e )
      resid[k] = np.sum ( w * x**d1 * y**d2 ) - r
      k = k + 1

  return resid

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  disk01_positive_rule_test ( )
  timestamp ( )

