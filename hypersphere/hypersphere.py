#! /usr/bin/env python3
#
def cartesian_to_hypersphere ( d, n, c, x ):

#*****************************************************************************80
#
## cartesian_to_hypersphere(): Cartesian to hypersphere coordinate transform.
#
#  Discussion:
#
#    We allow the trivial case D = 1 in that case alone, the value R
#    must be assumed to have a sign.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the spatial dimension.
#    1 <= D.
#
#    integer N, the number of points to transform.
#
#    real C(D), the center of the hypersphere.
#
#    real X(D,N), the Cartesian coordinates of the points.
#
#  Output:
#
#    real R(N), the radius of the points on the hypersphere.
#    Except for the trivial case D = 1, R is assumed nonnegative.
#
#    real THETA(D-1,N), the coordinate angles of the points,
#    measured in radians.
#
  import numpy as np

  r = np.zeros ( n )
  theta = np.zeros ( [ d - 1, n ] )
#
#  Handle special case of D = 1.
#
  if ( d == 1 ):
    r[:] = x[0,:] - c[0]
    theta = []
    return r, theta

  x2 = x.copy ( )

  for j in range ( 0, n ):
#
#  Subtract the center.
#  Moronic Python can't "x[:,j]=x[:,j]-c[:]"...
#
    for i in range ( 0, d ):
      x2[i,j] = x2[i,j] - c[i]
#
#  Compute R.
#
    r[j] = np.linalg.norm ( x2[:,j] )
#
#  Compute D-2 components of THETA.
#
    for i in range ( 1, d - 1 ):
      theta[0:i,j] = theta[0:i,j] + x2[i,j]**2

    theta[0:d-2,j] = theta[0:d-2,j] + x2[d-1,j]**2
    theta[0:d-2,j] = np.arctan2 ( np.sqrt ( theta[0:d-2,j] ), x2[0:d-2,j] )
#
#  Compute last component of THETA.
#
    top = ( np.sqrt ( x2[d-1,j]**2 + x2[d-2,j]**2 ) + x2[d-2,j] )
    theta[d-2,j] = 2.0 * np.arctan2 ( x2[d-1,j], top )

  return r, theta

def hypersphere_test ( ):

#*****************************************************************************80
#
## hypersphere_test() tests hypersphere().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'hypersphere_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  hypersphere() performs various operations on hyperspheres.' )

  rng = default_rng ( )

  hypersphere_area_test ( )
  hypersphere_area_sample_test ( rng )
  hypersphere_to_cartesian_test ( rng )
  hypersphere_volume_test ( )
  hypersphere_volume_sample_test ( rng )

  hypersphere01_area_test ( )
  hypersphere01_area_sample_test ( rng )
  hypersphere01_stereograph_test ( rng )
  hypersphere01_volume_test ( )
  hypersphere01_volume_sample_test ( rng )
#
#  Terminate.
#
  print ( '\n' )
  print ( 'hypersphere_test():' )
  print ( '  Normal end of execution.' )

  return

def hypersphere_area ( d, r ):

#*****************************************************************************80
#
## hypersphere_area() computes the surface area of a hypersphere.
#
#  Discussion:
#
#    An implicit sphere in D dimensions satisfies the equation:
#
#      sum ( ( P(1:D) - CENTER(1:D) )^2 ) = R^2
#
#    D   Area
#
#    2      2       * PI   * R
#    3      4       * PI   * R^2
#    4      2       * PI^2 * R^3
#    5      (8/3)   * PI^2 * R^4
#    6                PI^3 * R^5
#    7      (16/15) * PI^3 * R^6
#
#    Hypersphere_Area ( D, R ) = 2 * PI^(D/2) * R^(D-1) / Gamma ( D / 2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the dimension of the space.
#
#    real R, the radius of the sphere.
#
#  Output:
#
#    real AREA, the area of the sphere.
#
  area = r ** ( d - 1  ) * hypersphere01_area ( d )

  return area

def hypersphere_area_test ( ) :

#*****************************************************************************80
#
## hypersphere_area_test() tests hypersphere_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hypersphere_area_test():' )
  print ( '  hypersphere_area() returns the area of a hypersphere' )
  print ( '  in D dimensions.' )
  print ( '' )
  print ( '   D      R                 Area' )
  print ( '' )

  r = 1.5
  for d in range ( 1, 21 ):

    area = hypersphere_area ( d, r )

    print ( '  %2d  %g  %20.16f' % ( d, r, area ) )

  return

def hypersphere_area_sample ( d, r, n, rng ):

#*****************************************************************************80
#
## hypersphere_area_sample(): uniform points on the surface of a hypersphere.
#
#  Discussion:
#
#    The sphere has center 0 and radius R.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Russell Cheng,
#    Random Variate Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998, pages 168.
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Wiley, 1986, page 232.
#
#  Input:
#
#    integer D, the dimension of the space.
#
#    real R: the radius of the hypersphere.
#
#    integer N, the number of points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(D,N), the points.
#
  x = r * hypersphere01_area_sample ( d, n, rng )

  return x

def hypersphere_area_sample_test ( rng ):

#*****************************************************************************80
#
## hypersphere_area_sample_test() tests hypersphere_area_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'hypersphere_area_sample_test():' )
  print ( '  hypersphere_area_sample() returns sample points from the surface' )
  print ( '  of a hypersphere in D dimensions.' )
  
  d = 4
  r = 1.5
  n = 5
  x = hypersphere_area_sample ( d, r, n, rng )

  print ( '' )
  print ( '  hypersphere_area_sample ( ', d, ',', r, ',', n, '):' )
  print ( x )

  return

def hypersphere_to_cartesian ( d, n, c, r, theta ):

#*****************************************************************************80
#
## hypersphere_to_cartesian(): hypersphere to Cartesian coordinate transform.
#
#  Discussion:
#
#    We allow the trivial case M = 1; in that case alone, the value R
#    must be assumed to have a sign.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the spatial dimension.
#    1 <= D.
#
#    integer N, the number of points to transform.
#
#    real C(D), the center of the hypersphere.
#
#    real R(N), the radius of the points on the hypersphere.
#    Except for the trivial case D = 1, R is assumed nonnegative.
#
#    real THETA(D-1,N), the coordinate angles of the points,
#    measured in radians.
#
#  Output:
#
#    real X(D,N), the Cartesian coordinates of the points.
#
  import numpy as np

  x = np.zeros ( [ d, n ] )
#
#  Handle special case of D = 1.
#
  if ( d == 1 ):
    for j in range ( 0, n ):
      x[:,j] = c[:] + r[j]
    return x

  for j in range ( 0, n ):

    x[:,j] = r[j]

    for i1 in range ( 0, d - 1 ):
      x[i1,j] = x[i1,j] * np.cos ( theta[i1,j] )
      for i2 in range ( i1 + 1, d ):
        x[i2,j] = x[i2,j] * np.sin ( theta[i1,j] )
#
#  Add the center.
#
    for i in range ( 0, d ):
      x[i,j] = x[i,j] + c[i]

  return x

def hypersphere_to_cartesian_test ( rng ):

#*****************************************************************************80
#
## hypersphere_to_cartesian_test() tests hypersphere_to_cartesian().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'hypersphere_to_cartesian_test():' )
  print ( '  hypersphere_to_cartesian(): R,Theta -> X.' )
  print ( '  cartesian_to_hypersphere(): X       -> R,Theta' )
  print ( '' )
  print ( '  Pick a random X, and compute X2 by converting X' )
  print ( '  to hypersphere and back.  Consider norm of difference.' )
  print ( '' )
  print ( '  D    | X - X2 |' )

  n = 1
  for d in range ( 1, 6 ): 
    print ( '' )
    for j in range ( 0, 5 ):
      x = rng.random ( size = [ d, n ] )
      c = rng.random ( size = d )
      r, theta = cartesian_to_hypersphere ( d, n, c, x )
      x2 = hypersphere_to_cartesian ( d, n, c, r, theta )
      err = np.linalg.norm ( x - x2 )
      print ( '  ', d, '  ', err )

  return

def hypersphere_volume ( d, r ):

#*****************************************************************************80
#
## hypersphere_volume() computes the volume of a hypersphere.
#
#  Discussion:
#
#    A hypersphere in D dimensions satisfies the equation:
#
#      sum ( ( X(1:D) - CENTER(1:D) )^2 ) = R^2
#
#    where R is the radius and CENTER is the center.
#
#    Results for the first few values of D are:
#
#    D     Volume
#    -     -----------------------
#    2                PI   * R^2
#    3     (4/3)    * PI   * R^3
#    4     (1/2)    * PI^2 * R^4
#    5     (8/15)   * PI^2 * R^5
#    6     (1/6)    * PI^3 * R^6
#    7     (16/105) * PI^3 * R^7
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the dimension of the space.
#
#    real R, the radius of the sphere.
#
#  Output:
#
#    real VOLUME, the volume of the sphere.
#
  volume = r ** d * hypersphere01_volume ( d )

  return volume

def hypersphere_volume_test ( ) :

#*****************************************************************************80
#
## hypersphere_volume_test() tests hypersphere_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hypersphere_volume_test():' )
  print ( '  hypersphere_volume() returns the volume of a hypersphere' )
  print ( '  in D dimensions.' )
  print ( '' )
  print ( '   D      R                 Volume' )
  print ( '' )

  r = 1.5
  for d in range ( 1, 21 ):

    area = hypersphere_volume ( d, r )

    print ( '  %2d  %g  %20.16f' % ( d, r, area ) )

  return

def hypersphere_volume_sample ( d, r, n, rng ):

#*****************************************************************************80
#
## hypersphere_volume_sample(): uniform points inside a hypersphere.
#
#  Discussion:
#
#    The sphere has center 0 and radius R.
#
#    We first generate a point ON the sphere, and then distribute it
#    IN the sphere.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Russell Cheng,
#    Random Variate Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998, pages 168.
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Wiley, 1986, page 232.
#
#  Input:
#
#    integer D, the dimension of the space.
#
#    real R, the radius of the hypersphere.
#
#    integer N, the number of points.
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(D,N), the points.
#
  x = r * hypersphere01_volume_sample ( d, n, rng )

  return x

def hypersphere_volume_sample_test ( rng ) :

#*****************************************************************************80
#
## hypersphere_volume_sample_test() tests hypersphere_volume_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'hypersphere_volume_sample_test():' )
  print ( '  hypersphere_volume_sample() returns sample points from the volume' )
  print ( '  of a hypersphere in D dimensions.' )
  
  d = 4
  r = 1.5
  n = 5
  x = hypersphere_volume_sample ( d, r, n, rng )

  print ( '' )
  print ( '  hypersphere_volume_sample ( ', d, ',', r, ',', n, '):' )
  print ( x )

  return

def hypersphere01_area ( d ):

#*****************************************************************************80
#
## hypersphere01_area() returns the surface area of the unit hypersphere.
#
#  Discussion:
#
#     D   Area
#
#     2    2        * PI
#     3    4        * PI
#     4  ( 2 /   1) * PI^2
#     5  ( 8 /   3) * PI^2
#     6  ( 1 /   1) * PI^3
#     7  (16 /  15) * PI^3
#     8  ( 1 /   3) * PI^4
#     9  (32 / 105) * PI^4
#    10  ( 1 /  12) * PI^5
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the spatial dimension.
#
#  Output:
#
#    real VALUE, the area of the unit hypersphere.
#
  import numpy as np

  if ( ( d % 2 ) == 0 ):
    d_half = ( d // 2 )
    value = 2.0 * np.pi ** d_half
    for i in range (  1, d_half ):
      value = value / float ( i )
  else:
    d_half = ( ( d - 1 ) // 2 )
    value = np.pi ** d_half * 2.0 ** d
    for i in range ( d_half + 1, 2 * d_half + 1 ):
      value = value / float ( i )

  return value

def hypersphere01_area_test ( ) :

#*****************************************************************************80
#
## hypersphere01_area_test() tests hypersphere01_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hypersphere01_area_test():' )
  print ( '  hypersphere01_area() returns the area of the unit hypersphere' )
  print ( '  in D dimensions.' )
  print ( '' )
  print ( '   D      Area                 Area' )
  print ( '          Exact                Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, d, area1 = hypersphere01_area_values ( n_data )

    if ( n_data == 0 ):
      break

    area2 = hypersphere01_area ( d )

    print ( '  %2d  %20.16f  %20.16f' % ( d, area1, area2 ) )

  return

def hypersphere01_area_sample ( d, n, rng ):

#*****************************************************************************80
#
## hypersphere01_area_sample(): uniform points on the surface of the unit hypersphere.
#
#  Discussion:
#
#    The sphere has center 0 and radius 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Russell Cheng,
#    Random Variate Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998, pages 168.
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Wiley, 1986, page 232.
#
#  Input:
#
#    integer D, the dimension of the space.
#
#    integer N, the number of points.
#
#  Input:
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(D,N), the points.
#
  import numpy as np

  exponent = 1.0 / float ( d )

  x = np.zeros ( [ d, n ] )

  for j in range ( 0, n ):
#
#  Fill a vector with normally distributed values.
#
    v = rng.standard_normal ( size = d )
#
#  Compute the length of the vector.
#
    v_norm = np.linalg.norm ( v )
#
#  Normalize the vector.
#
    v = v / v_norm

    x[:,j] = v

  return x

def hypersphere01_area_sample_test ( rng ):

#*****************************************************************************80
#
## hypersphere01_area_sample_test() tests hypersphere01_area_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'hypersphere01_area_sample_test():' )
  print ( '  hypersphere01_area_sample() returns sample points from the surface' )
  print ( '  of the unit hypersphere in D dimensions.' )
  
  d = 4
  n = 5
  x = hypersphere01_area_sample ( d, n, rng )

  print ( '' )
  print ( '  hypersphere01_area_sample ( ', d, ',', n, '):' )
  print ( x )

  return

def hypersphere01_area_values ( n_data ):

#*****************************************************************************80
#
## hypersphere01_area_values() returns some areas of the unit hypersphere.
#
#  Discussion:
#
#    The formula for the surface area of the unit sphere in N dimensions is:
#
#      sphere_unit_area ( N ) = 2 * PI^(N/2) / Gamma ( N / 2 )
#
#    Some values of the function include:
#
#       N   Area
#
#       2    2        * PI
#       3  ( 4 /    ) * PI
#       4  ( 2 /   1) * PI^2
#       5  ( 8 /   3) * PI^2
#       6  ( 1 /   1) * PI^3
#       7  (16 /  15) * PI^3
#       8  ( 1 /   3) * PI^4
#       9  (32 / 105) * PI^4
#      10  ( 1 /  12) * PI^5
#
#    For the unit sphere, Area(N) = N * Volume(N)
#
#    In Mathematica, the function can be evaluated by:
#
#      2 * Pi^(n/2) / Gamma[n/2]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_data.  The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer N_data.  On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    integer D, the spatial dimension.
#
#    real AREA, the area of the unit sphere 
#    in that dimension.
#
  import numpy as np

  n_max = 20

  area_vec = np.array ( ( \
     0.2000000000000000E+01, \
     0.6283185307179586E+01, \
     0.1256637061435917E+02, \
     0.1973920880217872E+02, \
     0.2631894506957162E+02, \
     0.3100627668029982E+02, \
     0.3307336179231981E+02, \
     0.3246969701133415E+02, \
     0.2968658012464836E+02, \
     0.2550164039877345E+02, \
     0.2072514267328890E+02, \
     0.1602315322625507E+02, \
     0.1183817381218268E+02, \
     0.8389703410491089E+01, \
     0.5721649212349567E+01, \
     0.3765290085742291E+01, \
     0.2396678817591364E+01, \
     0.1478625959000308E+01, \
     0.8858104195716824E+00, \
     0.5161378278002812E+00 ))

  d_vec = np.array ( ( \
     1, \
     2, \
     3, \
     4, \
     5, \
     6, \
     7, \
     8, \
     9, \
    10, \
    11, \
    12, \
    13, \
    14, \
    15, \
    16, \
    17, \
    18, \
    19, \
    20 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    d = 0.0
    area = 0.0
  else:
    d = d_vec[n_data]
    area = area_vec[n_data]
    n_data = n_data + 1

  return n_data, d, area

def hypersphere01_stereograph ( d, n, x ):

#*****************************************************************************80
#
## hypersphere01_stereograph() applies a stereographic map to points on a unit hypersphere.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the spatial dimension.
#    D must be at least 2.
#
#    integer N, the number of points.
#
#    real X(D,N), the points to be mapped.
#
#  Output:
#
#    real X2(D-1,N), the stereographically mapped points.
#
  import numpy as np

  x2 = np.zeros ( [ d - 1, n ] )
  x2[:,:] = x[0:d-1,:]
  for j in range ( 0, n ):
    x2[:,j] = x2[:,j] / ( 1.0 - x[d-1,j] )
  
  return x2

def hypersphere01_stereograph_inverse ( d, n, x2 ):

#*****************************************************************************80
#
## hypersphere01_stereograph_inverse() inverts a stereographic map.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the spatial dimension.
#    D must be at least 2.
#
#    integer N, the number of points.
#
#    real X2(D-1,N), points in the plane.
#
#  Output:
#
#    real X(D,N), points mapped back to the hypersphere.
#
  import numpy as np

  x = np.zeros ( [ d, n ] )

  x[0:d-1,:] = 2.0 * x2

  for j in range ( 0, n ):
    z = np.sum ( x2[:,j] ** 2 )
    x[d-1,j] = z - 1.0
    x[:,j] = x[:,j] / ( z + 1.0 )

  return x

def hypersphere01_stereograph_test ( rng ):

#*****************************************************************************80
#
## hypersphere01_stereograph_test() tests hypersphere01_stereograph().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'hypersphere01_stereograph_test():' )
  print ( '  hypersphere01_stereograph() applies a stereograph map to points.' )
  print ( '  hypersphere01_stereograph_inverse() inverts the mapping.' )
  print ( '' )
  print ( '  Pick a random X1 on the hypersphere.' )
  print ( '  Map it to a point X2 on the plane.' )
  print ( '  Map it back to a point X3 on the hypersphere.' )
  print ( '  Consider norm of difference.' )
  print ( '' )
  print ( '  D    || X1 - X3 ||' )

  n = 1
  for d in range ( 2, 6 ):
    print ( '' )
    for j in range ( 0, 5 ):
      x1 = hypersphere01_area_sample ( d, n, rng )
      x2 = hypersphere01_stereograph ( d, n, x1 )
      x3 = hypersphere01_stereograph_inverse ( d, n, x2 )
      err = np.linalg.norm ( x1 - x3 )
      print ( '  ', d, '  ', err )

  return

def hypersphere01_volume ( d ):

#*****************************************************************************80
#
## hypersphere01_volume() computes the volume of a unit hypersphere.
#
#  Discussion:
#
#    The unit sphere in D dimensions satisfies:
#
#      sum ( 1 <= I <= D ) X(I) * X(I) = 1
#
#    Results for the first few values of D are:
#
#     D    Volume
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
#    For the unit sphere, Volume(D) = 2 * PI * Volume(D-2)/ D
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the dimension of the space.
#
#  Output:
#
#    real VOLUME, the volume of the sphere.
#
  import numpy as np

  if ( ( d % 2 ) == 0 ):
    m = ( d // 2 )
    volume = np.pi ** m
    for i in range ( 1, m + 1 ):
      volume = volume / float ( i )
  else:
    m = ( ( d - 1 ) // 2 )
    volume = np.pi ** m * 2.0 ** d
    for i in range ( m + 1, 2 * m + 2 ):
      volume = volume / float ( i )

  return volume

def hypersphere01_volume_test ( ) :

#*****************************************************************************80
#
## hypersphere01_volume_test() tests hypersphere01_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hypersphere01_volume_test():' )
  print ( '  hypersphere01_volume() returns the volume of the unit hypersphere' )
  print ( '  in D dimensions.' )
  print ( '' )
  print ( '   D      Volume               Volume' )
  print ( '          Exact                Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, d, volume1 = hypersphere01_volume_values ( n_data )

    if ( n_data == 0 ):
      break

    volume2 = hypersphere01_volume ( d )

    print ( '  %2d  %20.16f  %20.16f' % ( d, volume1, volume2 ) )

  return

def hypersphere01_volume_sample ( d, n, rng ):

#*****************************************************************************80
#
## hypersphere01_volume_sample(): uniform points inside unit hypersphere.
#
#  Discussion:
#
#    The sphere has center 0 and radius 1.
#
#    We first generate a point ON the sphere, and then distribute it
#    IN the sphere.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Russell Cheng,
#    Random Variate Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998, pages 168.
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Wiley, 1986, page 232.
#
#  Input:
#
#    integer D, the dimension of the space.
#
#    integer N, the number of points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(D,N), the points.
#
  import numpy as np

  exponent = 1.0 / float ( d )

  x = np.zeros ( [ d, n ] )

  for j in range ( 0, n ):
#
#  Fill a vector with normally distributed values.
#
    v = rng.standard_normal ( size = d )
#
#  Compute the length of the vector.
#
    v_norm = np.linalg.norm ( v )
#
#  Normalize the vector.
#
    v = v / v_norm
#
#  Now compute a value to map the point ON the sphere INTO the sphere.
#
    r = rng.random ( )

    x[:,j] = r ** exponent * v

  return x

def hypersphere01_volume_sample_test ( rng ):

#*****************************************************************************80
#
## hypersphere01_volume_sample_test() tests hypersphere01_volume_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'hypersphere01_volume_sample_test():' )
  print ( '  hypersphere01_volume_sample() returns sample points from the volume' )
  print ( '  of a unit hypersphere in D dimensions.' )
  
  d = 4
  n = 5
  x = hypersphere01_volume_sample ( d, n, rng )

  print ( '' )
  print ( '  hypersphere01_volume_sample ( ', d, ',', n, '):' )
  print ( x )

  return

def hypersphere01_volume_values ( n_data ):

#*****************************************************************************80
#
## hypersphere01_volume_values returns some volumes of the unit hypersphere.
#
#  Discussion:
#
#    The formula for the volume of the unit sphere in D dimensions is
#
#      Volume(D) = 2 * PI^(D/2) / ( D * Gamma ( D / 2 ) )
#
#    This function satisfies the relationships:
#
#      Volume(D) = 2 * PI * Volume(D-2) / D
#      Volume(D) = Area(D) / D
#
#    Some values of the function include:
#
#       D  Volume
#
#       1    1
#       2    1        * PI
#       3  ( 4 /   3) * PI
#       4  ( 1 /   2) * PI^2
#       5  ( 8 /  15) * PI^2
#       6  ( 1 /   6) * PI^3
#       7  (16 / 105) * PI^3
#       8  ( 1 /  24) * PI^4
#       9  (32 / 945) * PI^4
#      10  ( 1 / 120) * PI^5
#
#    In Mathematica, the function can be evaluated by:
#
#      2 * Pi^(d/2) / ( d * Gamma[d/2] )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_data.  The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer N_data.  On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    integer D, the spatial dimension.
#
#    real VOLUME, the volume of the unit 
#    sphere in that dimension.
#
  import numpy as np

  n_max = 20

  d_vec = np.array ( ( \
     1, \
     2, \
     3, \
     4, \
     5, \
     6, \
     7, \
     8, \
     9, \
    10, \
    11, \
    12, \
    13, \
    14, \
    15, \
    16, \
    17, \
    18, \
    19, \
    20 ))

  volume_vec = np.array ( ( \
     0.2000000000000000E+01, \
     0.3141592653589793E+01, \
     0.4188790204786391E+01, \
     0.4934802200544679E+01, \
     0.5263789013914325E+01, \
     0.5167712780049970E+01, \
     0.4724765970331401E+01, \
     0.4058712126416768E+01, \
     0.3298508902738707E+01, \
     0.2550164039877345E+01, \
     0.1884103879389900E+01, \
     0.1335262768854589E+01, \
     0.9106287547832831E+00, \
     0.5992645293207921E+00, \
     0.3814432808233045E+00, \
     0.2353306303588932E+00, \
     0.1409811069171390E+00, \
     0.8214588661112823E-01, \
     0.4662160103008855E-01, \
     0.2580689139001406E-01  ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    d = 0.0
    volume = 0.0
  else:
    d = d_vec[n_data]
    volume = volume_vec[n_data]
    n_data = n_data + 1

  return n_data, d, volume

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
#    06 April 2013
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
  hypersphere_test ( )
  timestamp ( )

