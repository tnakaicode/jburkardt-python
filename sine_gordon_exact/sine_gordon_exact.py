#! /usr/bin/env python3
#
def sine_gordon_exact_test ( ):

#*****************************************************************************80
#
## sine_gordon_exact_test() tests sine_gordon_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( "" )
  print ( "sine_gordon_exact_test():" )
  print ( "  python version: " + platform.python_version ( ) )
  print ( "  numpy version:  " + np.version.version )
  print ( "  Test sine_gordon_exact()." )

  a = 1.5

  print ( "" )
  print ( "  Parameter values:" )
  print ( "    a     = ", a )

  print ( "" )
  print ( "  Evaluate solution and residual at selected points (X,Y)" )
  
  x = np.linspace ( 0.0, 1.0, 6 )
  y = np.linspace ( 0.0, 1.0, 6 )

  print ( "" )
  print ( "      X       Y       U(X,Y)      Resid(X,Y)" )
  print ( "" )
  for j in range ( 0, 6 ):
    for i in range ( 0, 6 ):
      u, uxy = sine_gordon_exact ( a, x[i], y[j] )
      r = sine_gordon_residual ( u, uxy )
      print ( "  %f  %f  %f  %g" % ( x[i], y[j], u, r ) )
    print ( "" )
#
#  Terminate.
#
  print ( "" )
  print ( "sine_gordon_exact_test():" )
  print ( "  Normal end of execution." )

  return

def sine_gordon_exact ( a, x, y ):

#*****************************************************************************80
#
## sine_gordon_exact() evaluates an exact solution of the Sine-Gordon PDE.
#
#  Discussion:
#
#    uxy = sin ( u )
#
#    This is a one-soliton solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Arrigo,
#    Analytical Techniques for Solving Nonlinear Partial Differential Equations,
#    Morgan and Clayfoot, 2019,
#    ISBN: 978 168 173 5351.
#
#  Input:
#
#    real A: a parameter.
#
#    real X, Y: the X and Y coordinates of a point.
#
#  Output:
#
#    real U, UXY: the values of the solution, and its first mixed derivative
#    at (X,Y).
#
  import numpy as np

  u = 4.0 * np.arctan ( np.exp ( a * x + y / a ) )

  uxy = 4.0 * ( np.exp ( a * x + y / a ) - np.exp ( 3 * a * x + 3 * y / a ) ) \
    / ( 1.0 + np.exp ( 2 * a * x + 2 * y / a ) ) ** 2

  return u, uxy

def sine_gordon_residual ( u, uxy ):

#*****************************************************************************80
#
## sine_gordon_residual() evaluates the residual for the Sine-Gordon PDE.
#
#  Discussion:
#
#    The governing equation is:
#
#      d2 u/dxdy = sin(u)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Arrigo,
#    Analytical Techniques for Solving Nonlinear Partial Differential Equations,
#    Morgan and Clayfoot, 2019,
#    ISBN: 978 168 173 5351.
#
#  Input:
#
#    real U, UXY: the values of the solution, and its first mixed derivative.
#
#  Output:
#
#    real R, the residual.
#
  import numpy as np

  r = uxy - np.sin ( u )

  return r

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

if ( __name__ == "__main__" ):
  timestamp ( )
  sine_gordon_exact_test ( )
  timestamp ( )

