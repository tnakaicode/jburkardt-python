#! /usr/bin/env python3
#
def ellipsoid_test ( ):

#*****************************************************************************80
#
## ellipsoid_test() tests ellipsoid().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 January 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ellipsoid_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ellipsoid().' )

  ellipsoid_abc_area_test ( )
  ellipsoid_abc_volume_test ( )
  ellipsoid_conic_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ellipsoid_test():' )
  print ( '  Normal end of execution.' )
  return

def ellipsoid_abc_area ( a, b, c ):

#*****************************************************************************80
#
## ellipsoid_abc_area() returns the surface area  of an ellipsoid.
#
#  Discussion:
#
#    The ellipsoid may be represented by the equation
#
#      (x/a)^2 + (y/b)^2 + (z/c)^2 = 1
#
#    with a => b => c
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Ellipsoid surface area,
#    6 July 2014,
#    https://www.johndcook.com/blog/2014/07/06/ellipsoid-surface-area/
#
#  Input:
#
#    real A, B, C, the semi-axes of the ellipsoid.
#
#  Output:
#
#    real VALUE, the surface area of the ellipsoid.
#
  from scipy.special import ellipeinc
  from scipy.special import ellipkinc
  import numpy as np

  a = abs ( a )
  b = abs ( b )
  c = abs ( c )

  if ( a < b ):
    t = a
    a = b
    b = t

  if ( a < c ):
    t = a
    a = c
    c = t

  if ( b < c ):
    t = b
    b = c
    c = t

  phi = np.arccos ( c / a )

  if ( a**2 - c**2 == 0 ):
    m = 1
  else:
    m = ( a**2 * ( b**2 - c**2 ) ) / ( b**2 * ( a**2 - c**2 ) )

  temp = ellipeinc ( phi, m ) * np.sin ( phi )**2 \
       + ellipkinc ( phi, m ) * np.cos ( phi )**2

  if ( np.sin ( phi ) == 0 ):
    temp2 = 1
  else:
    temp2 = temp / np.sin ( phi )

  value = 2.0 * np.pi * ( c**2 + a * b * temp2 )
  
  return value

def ellipsoid_abc_area_test ( ):

#*****************************************************************************80
#
## ellipsoid_abc_area_test() tests ellipsoid_abc_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 March 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ellipsoid_abc_area_test():' )
  print ( '  ellipsoid_abc_area_test() computes the surface area of the ellipsoid' )
  print ( '    (x/a)^2+(y/b)^2+(z/c)^2=1' )

  print ( '' )
  print ( '           A           B           C        Area' )
  print ( '' )

  a = 1.0
  b = 0.8
  c = 0.625
  area = ellipsoid_abc_area ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 1.0
  b = 1.0
  c = 0.5
  area = ellipsoid_abc_area ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 1.0
  b = 1.0
  c = 1.0
  area = ellipsoid_abc_area ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 2.0
  b = 1.0
  c = 0.25
  area = ellipsoid_abc_area ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 2.0
  b = 3.0
  c = 4.0
  area = ellipsoid_abc_area ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  return

def ellipsoid_abc_volume ( a, b, c ):

#*****************************************************************************80
#
## ellipsoid_abc_volume() returns the volume of an ellipsoid.
#
#  Discussion:
#
#    The ellipsoid may be represented by the equation
#
#      (x/a)^2 + (y/b)^2 + (z/c)^2 = 1
#
#    with a => b => c
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the semi-axes of the ellipsoid.
#
#  Output:
#
#    real VALUE, the volume of the ellipsoid.
#
  import numpy as np

  a = abs ( a )
  b = abs ( b )
  c = abs ( c )

  value = ( 4.0 / 3.0 ) * np.pi * ( a * b * c )
  
  return value

def ellipsoid_abc_volume_test ( ):

#*****************************************************************************80
#
## ellipsoid_abc_volume_test() tests ellipsoid_abc_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ellipsoid_abc_volume_test():' )
  print ( '  ellipsoid_abc_volume_test() computes the volume of the ellipsoid' )
  print ( '    (x/a)^2+(y/b)^2+(z/c)^2=1' )

  print ( '' )
  print ( '           A           B           C        Volume' )
  print ( '' )

  a = 1.0
  b = 0.8
  c = 0.625
  area = ellipsoid_abc_volume ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 1.0
  b = 1.0
  c = 0.5
  area = ellipsoid_abc_volume ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 1.0
  b = 1.0
  c = 1.0
  area = ellipsoid_abc_volume ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 2.0
  b = 1.0
  c = 0.25
  area = ellipsoid_abc_volume ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 2.0
  b = 3.0
  c = 4.0
  area = ellipsoid_abc_volume ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  return

def ellipsoid_conic_volume ( m, A, v, r ):

#*****************************************************************************80
#
## ellipsoid_conic_volume() returns the volume of an ellipsoid.
#
#  Discussion:
#
#    The points X in the ellipsoid are described by an M by M
#    positive definite symmetric matrix A, an M-dimensional point V,
#    and a "radius" R, such that
#      (X-V)' * A * (X-V) <= R * R
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    real A(M,M), the matrix that describes
#    the ellipsoid.  A must be symmetric positive definite.
#
#    real V(M), the "center" of the ellipse.
#    The value of V is not actually needed by this function.
#
#    real R, the "radius" of the ellipse.
#
#  Output:
#
#    real VOLUME, the volume of the ellipsoid.
#
  import numpy as np

  L = np.linalg.cholesky ( A )
 
  sqrt_det = 1.0
  for i in range ( 0, m ):
    sqrt_det = sqrt_det * L[i,i]

  volume = r ** m * hyperball01_volume ( m ) / sqrt_det

  return volume

def ellipsoid_conic_volume_test ( ):

#*****************************************************************************80
#
## ellipsoid_conic_volume_test() tests ellipsoid_conic_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ellipsoid_conic_volume_test():' )
  print ( '  ellipsoid_conic_volume() computes the volume of the ellipsoid' )
  print ( '    (X-V)\' * A * (X-V) <= R * R.' )

  m = 3
  A = np.array ( [ \
    [ 9.0, 3.0, 3.0 ], \
    [ 3.0, 5.0, 3.0 ], \
    [ 3.0, 3.0, 3.0 ] ] )
  v = np.array ( [ 2.0, 3.0, 1.0 ] )
  r = 1.0

  print ( '' )
  print ( '  M = %d' % ( m ) )
  print ( '  Matrix A:' )
  print ( A )
  print ( '  Vector V:' )
  print ( v )

  volume = ellipsoid_conic_volume ( m, A, v, r )

  print ( '' )
  print ( '  Volume = %14.6g' % ( volume ) )

  return

def hyperball01_volume ( m ):

#*****************************************************************************80
#
## hyperball01_volume() returns the volume of the unit hyperball in M dimensions.
#
#  Discussion:
#
#     M  Volume
#
#     1    2
#     2    1        * PI
#     3  ( 4 /   3) * PI
#     4  ( 1 /   2) * PI^2
#     5  ( 8 /  15) * PI^2
#     6  ( 1 /   6) * PI^3
#     7  (16 / 105) * PI^3
#     8  ( 1 /  24) * PI^4
#     9  (32 / 945) * PI^4
#    10  ( 1 / 120) * PI^5
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real VOLUME, the volume of the unit ball.
#
  import numpy as np

  if ( ( m % 2 ) == 0 ):
    m_half = ( m // 2 )
    volume = np.pi ** m_half
    for i in range ( 1, m_half + 1 ):
      volume = volume / float ( i )
  else:
    m_half = ( ( m - 1 ) // 2 )
    volume = np.pi ** m_half * 2.0 ** m
    for i in range ( m_half + 1, 2 * m_half + 2 ):
      volume = volume / float ( i )

  return volume

def hyperball01_volume_test ( ) :

#*****************************************************************************80
#
## hyperball01_volume() tests hyperball01_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hyperball01_volume_test():' )
  print ( '  hyperball01_volume() returns the volume of the unit hyperball' )
  print ( '  in M dimensions.' )
  print ( '' )
  print ( '   M  Volume' )
  print ( '' )

  for m in range ( 1, 11 ):
    value = hyperball01_volume ( m )
    print ( '  %2d  %g' % ( m, value ) )

  return

def r8_sign ( x ):

#*****************************************************************************80
#
## r8_sign() returns the sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose sign is desired.
#
#  Output:
#
#    real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  else:
    value = +1.0
 
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
  ellipsoid_test ( )
  timestamp ( )

