#! /usr/bin/env python3
#
def minimal_surface_exact_test ( ):

#*****************************************************************************80
#
## minimal_surface_exact_test() tests minimal_surface_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2025
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( "" )
  print ( "minimal_surface_exact_test():" )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( "  Test minimal_surface_exact()." )

  rng = default_rng ( )

  n = 5
  X = rng.random ( n )
  Y = rng.random ( n )
  a = 1.0
  b = 2.0
  c = 3.0
#
#  Linear solution.
#
  print ( "" )
  print ( "  Linear solution residual at random points:" )

  R = minimal_surface_linear_residual ( X, Y, a, b, c )

  print ( "  RMS norm of residuals = ", r8vec_norm_rms ( R ) )
#
#  Helicoid solution.
#
  print ( "" )
  print ( "  Helicoid solution residual at random points:" )

  R = minimal_surface_helicoid_residual ( X, Y )

  print ( "  RMS norm of residuals = ", r8vec_norm_rms ( R ) )
#
#  Catenoid solution.
#  Python arccosh(Z) requires 1 <= Z.
#  Hence we have to modify X and Y.
#
  print ( "" )
  print ( "  Catenoid solution residual at random points:" )

  X2 = X + 1
  Y2 = Y + 1
  R = minimal_surface_catenoid_residual ( X2, Y2, a )

  print ( "  RMS norm of residuals = ", r8vec_norm_rms ( R ) )
#
#  Scherk solution.
#
  print ( "" )
  print ( "  Scherk solution residual at random points:" )

  R = minimal_surface_scherk_residual ( X, Y, a )

  print ( "  RMS norm of residuals = ", r8vec_norm_rms ( R ) )
#
#  Terminate.
#
  print ( "" )
  print ( "minimal_surface_exact_test()" )
  print ( "  Normal end of execution." )

  return

def r8vec_norm_rms ( a ):

#*****************************************************************************80
#
## r8vec_norm_rms() returns the RMS norm of an R8VEC.
#
#  Discussion:
#
#    The vector RMS norm is defined as:
#
#      value = np.sqrt ( sum ( 1 <= I <= N ) A(I)^2 / N ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N), the vector.
#
#  Output:
#
#    real VALUE, the RMS norm.
#
  import numpy as np

  n = len ( a )

  value = np.sqrt ( np.sum ( a**2 ) / n )

  return value

def minimal_surface_catenoid_exact ( X, Y, a ):

#*****************************************************************************80
#
## minimal_surface_catenoid_exact() evaluates catenoid minimal surface solution U(X,Y).
#
#  Discussion:
#
#    The minimal surface equation describes a function with zero mean curvature.
#
#    The equation is:
#      (1+Ux^2) Uyy - 2 Ux Uy Uxy + (1+Uy^2) Uxx = 0
#
#    The helicoid solution is:
#      U(X,Y) = acosh ( a sqrt(X^2+Y^2) ) / a
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Closed-form minimal surface solutions,
#    https://www.johndcook.com/blog/2025/03/31/minimal-surface-solutions/
#    Posted 31 March 2025.
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a: a shape parameter.
#
#  Output:
#
#    real U, Ux, Uy, Uxx, Uxy, Uyy: the solution and first and second
#    partial derivatives evaluated at the points (X,Y).
#
  import numpy as np

  U = np.arccosh ( a * np.sqrt ( X**2 + Y**2 ) ) / a
  Ux = X / ( np.sqrt ( X**2 + Y**2 ) * np.sqrt ( a**2 * ( X**2 + Y**2 ) - 1 ) )
  Uy = Y / ( np.sqrt ( X**2 + Y**2 ) * np.sqrt ( a**2 * ( X**2 + Y**2 ) - 1 ) )
  Uxx = - ( a**2 * X**2 / ( a**2 * ( X**2 + Y**2 ) - 1 ) \
    + X**2 / ( X**2 + Y**2 ) - 1 ) / ( np.sqrt ( X**2 + Y**2 ) \
    * np.sqrt ( a**2 * ( X**2 + Y**2 ) - 1 ) )
  Uxy = - X * Y * ( a**2 / ( a**2 * ( X**2 + Y**2 ) - 1 ) \
    + 1 / ( X**2 + Y**2 ) ) / ( np.sqrt ( X**2 + Y**2 ) \
    * np.sqrt ( a**2 * ( X**2 + Y**2 ) - 1 ) )
  Uyy = - ( a**2 * Y**2 / ( a**2 * ( X**2 + Y**2 ) - 1 ) \
    + Y**2 / ( X**2 + Y**2 ) - 1 ) / ( np.sqrt ( X**2 + Y**2 ) \
    * np.sqrt ( a**2 * ( X**2 + Y**2 ) - 1 ) )

  return U, Ux, Uy, Uxx, Uxy, Uyy

def minimal_surface_catenoid_residual ( X, Y, a ):

#*****************************************************************************80
#
## minimal_surface_catenoid_residual(): minimal surface residual for catenoid solution.
#
#  Discussion:
#
#    The equation is:
#      (1+Ux^2) Uyy - 2 Ux Uy Uxy + (1+Uy^2) Uxx = 0
#
#    The catenoid solution is:
#      U(X,Y) = acosh ( a * np.sqrt ( X^2 + Y^2 ) ) / a
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a: a shape parameter.
#
#  Output:
#
#    real R: the residual evaluated at the points (X,Y).
#
  U, Ux, Uy, Uxx, Uxy, Uyy = minimal_surface_catenoid_exact ( X, Y, a )

  R = ( 1.0 + Ux**2 ) * Uyy \
    - 2.0 * Ux * Uxy * Uy \
    + ( 1.0 + Uy**2 ) * Uxx

  return R

def minimal_surface_helicoid_exact ( X, Y ):

#*****************************************************************************80
#
## minimal_surface_helicoid_exact() evaluates helicoid minimal surface solution U(X,Y).
#
#  Discussion:
#
#    The minimal surface equation describes a function with zero mean curvature.
#
#    The equation is:
#      (1+Ux^2) Uyy - 2 Ux Uy Uxy + (1+Uy^2) Uxx = 0
#
#    The helicoid solution is:
#      U(X,Y) = arctan ( X / Y )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Closed-form minimal surface solutions,
#    https://www.johndcook.com/blog/2025/03/31/minimal-surface-solutions/
#    Posted 31 March 2025.
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#  Output:
#
#    real U, Ux, Uy, Uxx, Uxy, Uyy: the solution and first and second
#    partial derivatives evaluated at the points (X,Y).
#
  import numpy as np

  U = np.arctan ( X / Y )
  Ux = 1 / ( Y * ( X**2 / Y**2 + 1 ) )
  Uy = - X / ( Y**2 * ( X**2 / Y**2 + 1 ) )
  Uxx = - 2 * X / ( Y**3 * ( X**2 / Y**2 + 1 )**2 )
  Uxy = ( 2 * X**2 / ( Y**2 * ( X**2 / Y**2 + 1 ) ) - 1 ) \
    / ( Y**2 * ( X**2 / Y**2 + 1 ) )
  Uyy = 2 * X * ( - X**2 / ( Y**2 * ( X**2 / Y**2 + 1 ) ) + 1 ) \
    / ( Y**3 * ( X**2 / Y**2 + 1 ) )

  return U, Ux, Uy, Uxx, Uxy, Uyy

def minimal_surface_helicoid_residual ( X, Y ):

#*****************************************************************************80
#
## minimal_surface_helicoid_residual(): minimal surface residual for helicoid solution.
#
#  Discussion:
#
#    The equation is:
#      (1+Ux^2) Uyy - 2 Ux Uy Uxy + (1+Uy^2) Uxx = 0
#
#    The helicoid solution is:
#      U(X,Y) = arctan ( X / Y )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#  Output:
#
#    real R: the residual evaluated at the points (X,Y).
#
  U, Ux, Uy, Uxx, Uxy, Uyy = minimal_surface_helicoid_exact ( X, Y )

  R = ( 1.0 + Ux**2 ) * Uyy \
    - 2.0 * Ux * Uxy * Uy   \
    + ( 1.0 + Uy**2 ) * Uxx

  return R

def minimal_surface_linear_exact ( X, Y, a, b, c ):

#*****************************************************************************80
#
## minimal_surface_linear_exact() evaluates linear minimal surface solution U(X,Y).
#
#  Discussion:
#
#    The minimal surface equation describes a function with zero mean curvature.
#
#    The equation is:
#      (1+Ux^2) Uyy - 2 Ux Uy Uxy + (1+Uy^2) Uxx = 0
#
#    The linear solution is:
#      U(X,Y) = a * X + b * Y + C
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Closed-form minimal surface solutions,
#    https://www.johndcook.com/blog/2025/03/31/minimal-surface-solutions/
#    Posted 31 March 2025.
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c: parameters.
#
#  Output:
#
#    real U, Ux, Uy, Uxx, Uxy, Uyy: the solution and first and second
#    partial derivatives evaluated at the points (X,Y).
#
  import numpy as np

  U = a * X + b * Y + c
  Ux = a * np.ones_like ( U )
  Uy = b * np.ones_like ( U )
  Uxx = np.zeros_like ( U )
  Uxy = np.zeros_like ( U )
  Uyy = np.zeros_like ( U )

  return U, Ux, Uy, Uxx, Uxy, Uyy

def minimal_surface_linear_residual ( X, Y, a, b, c ):

#*****************************************************************************80
#
## minimal_surface_linear_residual(): minimal surface residual for linear solution.
#
#  Discussion:
#
#    The equation is:
#      (1+Ux^2) Uyy - 2 Ux Uy Uxy + (1+Uy^2) Uxx = 0
#
#    The linear solution is:
#      U(X,Y) = a * X + b * Y + C
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c: parameters.
#
#  Output:
#
#    real R: the residual evaluated at the points (X,Y).
#
  U, Ux, Uy, Uxx, Uxy, Uyy = minimal_surface_linear_exact ( X, Y, a, b, c )

  R = ( 1.0 + Ux**2 ) * Uyy \
    - 2.0 * Ux * Uxy * Uy   \
    + ( 1.0 + Uy**2 ) * Uxx

  return R

def minimal_surface_scherk_exact ( X, Y, a ):

#*****************************************************************************80
#
## minimal_surface_scherk_exact() evaluates Scherk minimal surface solution U(X,Y).
#
#  Discussion:
#
#    The minimal surface equation describes a function with zero mean curvature.
#
#    The equation is:
#      (1+Ux^2) Uyy - 2 Ux Uy Uxy + (1+Uy^2) Uxx = 0
#
#    The Scherk solution is:
#      U(X,Y) = log ( cos ( a Y ) / cos ( a X ) ) / a
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Closed-form minimal surface solutions,
#    https://www.johndcook.com/blog/2025/03/31/minimal-surface-solutions/
#    Posted 31 March 2025.
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a: a shape parameter.
#
#  Output:
#
#    real U, Ux, Uy, Uxx, Uxy, Uyy: the solution and first and second
#    partial derivatives evaluated at the points (X,Y).
#
  import numpy as np

  U = np.log ( np.cos ( a * Y ) / np.cos ( a * X ) ) / a
  Ux =  np.sin ( a * X ) / np.cos ( a * X )
  Uy =  - np.sin ( a * Y ) / np.cos ( a * Y )
  Uxx =  a * ( np.sin ( a * X )**2 / np.cos ( a * X )**2 + 1 )
  Uxy =  np.zeros_like ( X )
  Uyy =  - a * ( np.sin ( a * Y )**2 / np.cos ( a * Y )**2 + 1 )

  return U, Ux, Uy, Uxx, Uxy, Uyy

def minimal_surface_scherk_residual ( X, Y, a ):

#*****************************************************************************80
#
## minimal_surface_scherk_residual(): minimal surface residual for Scherk solution.
#
#  Discussion:
#
#    The equation is:
#      (1+Ux^2) Uyy - 2 Ux Uy Uxy + (1+Uy^2) Uxx = 0
#
#    The Scherk solution is:
#      U(X,Y) = log ( cos ( a * Y ) / cos ( a * X ) ) / a
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a: a shape parameter.
#
#  Output:
#
#    real R: the residual evaluated at the points (X,Y).
#
  U, Ux, Uy, Uxx, Uxy, Uyy = minimal_surface_scherk_exact ( X, Y, a )

  R = ( 1.0 + Ux**2 ) * Uyy \
    - 2.0 * Ux * Uxy * Uy   \
    + ( 1.0 + Uy**2 ) * Uxx

  return R

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
  minimal_surface_exact_test ( )
  timestamp ( )
