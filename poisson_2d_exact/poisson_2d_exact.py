#! /usr/bin/env python3
#
def poisson_2d_exact_test ( ):

#*****************************************************************************80
#
## poisson_2d_exact_test() tests poisson_2d_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2025
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'poisson_2d_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test poisson_2d_exact().' )

  n = 5
  X = rng.random ( n )
  Y = rng.random ( n )

  U, Ux, Uy, Uxx, Uxy, Uyy = poisson_2d_exact ( X, Y )
  F = np.zeros ( n )
  R = Uxx + Uyy + F

  print ( '  RMS norm of residuals = ', r8vec_norm_rms ( R ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'poisson_2d_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def poisson_2d_exact ( x, y ):

#*****************************************************************************80
#
## poisson_2d_exact() evaluates an exact solution of the Poisson equation.
#
#  Discussion:
#
#    The equation is:
#      - Uxx - Uyy = F(x,y)
#
#    The domain is the unit square:
#      Omega = 0 <= x, y <= 1
#
#    The solution is:
#      U(X,Y) = 2 * ( 1 + Y ) / ( ( 3 + X )^2 + ( 1 + Y )^2 )
#
#    The boundary conditions are determined by evaluating the exact
#    solution U(X,Y).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2025
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
#    real U, Ux, Uy, Uxx, Uxy, Uyy: the solution and first and second
#    partial derivatives evaluated at the points (X,Y).
#
  u = 2.0 * ( 1.0 + y ) / ( ( 3.0 + x )**2 + ( 1.0 + y )**2 )
  ux = ( - 2 * x - 6 ) * ( 2 * y + 2 ) / ( ( x + 3 )**2 + ( y + 1 )**2 )**2
  uy = ( - 2 * y - 2 ) * ( 2 * y + 2 ) \
    / ( ( x + 3 )**2 + ( y + 1 )**2 )**2 + 2 / ( ( x + 3 )**2 + ( y + 1 )**2 )
  uxx = 4 * ( y + 1 ) * ( 4 * ( x + 3 )**2 \
    / ( ( x + 3 )**2 + ( y + 1 )**2 ) - 1 ) \
    / ( ( x + 3 )**2 + ( y + 1 )**2 )**2
  uxy = 4 * ( x + 3 )* ( 4 * ( y + 1 )**2 \
    / ( ( x + 3 )**2 + ( y + 1 )**2 ) - 1 ) \
    / ( ( x + 3 )**2 + ( y + 1 )**2 )**2
  uyy = 4 * ( y + 1 ) * ( 4 * ( y + 1 ) **2 \
    / ( ( x + 3 )**2 + ( y + 1 )**2 ) - 3 ) \
    / ( ( x + 3 )**2 + ( y + 1 )**2 )**2

  return u, ux, uy, uxx, uxy, uyy

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
  poisson_2d_exact_test ( )
  timestamp ( )

