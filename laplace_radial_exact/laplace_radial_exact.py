#! /usr/bin/env python3
#
def laplace_radial_exact_test ( ):

#*****************************************************************************80
#
## laplace_radial_exact_test() tests laplace_radial_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2025
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'laplace_radial_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test laplace_radial_exact().' )

  rng = default_rng ( )

  n = 5
  X = rng.random ( n )
  Y = rng.random ( n )
  Z = rng.random ( n )
  a = 1.0
  b = 2.0
  c = 3.0
#
#  2D case.
#
  print ( '' )
  print ( '  Radial solution in 2D:' )

  U, Ux, Uy, Uxx, Uxy, Uyy = laplace_radial_2d_exact ( X, Y, a, b )
  R = Uxx + Uyy

  print ( '  RMS norm of residuals = ', r8vec_norm_rms ( R ) )
#
#  3D case.
#
  print ( '' )
  print ( '  Radial solution in 3D:' )

  U, Ux, Uy, Uz, Uxx, Uxy, Uxz, Uyy, Uyz, Uzz = \
    laplace_radial_3d_exact ( X, Y, Z, a, b )
  R = Uxx + Uyy + Uzz

  print ( '  RMS norm of residuals = ', r8vec_norm_rms ( R ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'laplace_radial_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def laplace_radial_2d_exact ( x, y, a, b ):

#*****************************************************************************80
#
## laplace_radial_2d_exact() evaluates an exact radial solution of the Laplace equation.
#
#  Discussion:
#
#    The equation is:
#      Uxx + Uyy = 0
#
#    The radial solution in 2D, with parameters a and b, is:
#      R = sqrt ( X^2 + Y^2 )
#      U(X,Y) = a * log ( R ) + b
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b: parameters.
#
#  Output:
#
#    real U, Ux, Uy, Uxx, Uxy, Uyy: the solution and first and second
#    partial derivatives evaluated at the points (X,Y).
#
  import numpy as np

  r = np.sqrt ( x**2 + y**2 )

  u = a * np.log ( r ) + b
  ux = a * x / ( x**2 + y**2 )
  uy = a * y / ( x**2 + y**2 )
  uxx = a * ( - 2 * x**2 / ( x**2 + y**2 ) + 1 ) / ( x**2 + y**2 )
  uxy = - 2 * a * x * y / ( x**2 + y**2 )**2
  uyy = a * ( - 2 * y**2 / ( x**2 + y**2 ) + 1 ) / ( x**2 + y**2 )

  return u, ux, uy, uxx, uxy, uyy

def laplace_radial_3d_exact ( x, y, z, a, b ):

#*****************************************************************************80
#
## laplace_radial_3d_exact() evaluates an exact radial solution of the Laplace equation.
#
#  Discussion:
#
#    The equation is:
#      Uxx + Uyy = 0
#
#    The radial solution in 3D, with parameters a and b, is:
#      R = sqrt ( X^2 + Y^2 + Z^2 )
#      U(X,Y,Z) = a * log ( R ) + b
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y, Z: the coordinates of the points.
#
#    real a, b: shape parameters.
#
#  Output:
#
#    real U, Ux, Uy, Uz, Uxx, Uxy, Uxz, Uyy, Uyz, Uzz: 
#    the solution and first and second partial derivatives evaluated 
#    at the points (X,Y).
#
  import numpy as np

  r = np.sqrt ( x**2 + y**2 + z**2 )

  u = - a / r + b 
  ux = a * x / ( x**2 + y**2 + z**2 )**(3/2)
  uy = a * y / ( x**2 + y**2 + z**2 )**(3/2)
  uz = a * z / ( x**2 + y**2 + z**2 )**(3/2)
  uxx = a * ( - 3 * x**2 / ( x**2 + y**2 + z**2 ) + 1 ) \
    / ( x**2 + y**2 + z**2 )**(3/2)
  uxy = - 3 * a * x * y / ( x**2 + y**2 + z**2 )**(5/2)
  uxz = - 3 * a * x * z / ( x**2 + y**2 + z**2 )**(5/2)
  uyy = a * ( - 3 * y**2 / ( x**2 + y**2 + z**2 ) + 1 ) \
    / ( x**2 + y**2 + z**2 )**(3/2)
  uyz = - 3 * a * y * z / ( x**2 + y**2 + z**2 )**(5/2)
  uzz = a * ( - 3 * z**2 / ( x**2 + y**2 + z**2 ) + 1 ) \
    / ( x**2 + y**2 + z**2 )**(3/2)

  return u, ux, uy, uz, uxx, uxy, uxz, uyy, uyz, uzz
 
def r8vec_norm_rms ( a ):

#*****************************************************************************80
#
## r8vec_norm_rms() returns the RMS norm of an R8VEC.
#
#  Discussion:
#
#    The vector RMS norm is defined as:
#
#      value = sqrt ( 1/N * sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N), the vector whose norm is desired.
#
#  Output:
#
#    real VALUE, the RMS norm of A.
#
  import numpy as np

  value = np.sqrt ( (a**2).mean() )

  return value

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
  laplace_radial_exact_test ( )
  timestamp ( )


