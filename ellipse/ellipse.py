#! /usr/bin/env python3
#
def ellipse_test ( ):

#*****************************************************************************80
#
## ellipse_test() tests ellipse().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ellipse_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ellipse().' )

  ellipse_area1_test ( )
  ellipse_area2_test ( )
  ellipse_area3_test ( )
  ellipse_aspect_ratio_test ( )
  ellipse_eccentricity_test ( )
  ellipse_flattening_test ( )
  ellipse_grid_test ( )
  ellipse_perimeter_test ( )
  ellipse_point_near_test ( )
  ellipse_sample_test ( )

  ellipsoid_area_test ( )
  ellipsoid_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ellipse_test():' )
  print ( '  Normal end of execution.' )
  return

def ellipse_area1 ( a, r ):

#*****************************************************************************80
#
## ellipse_area1() returns the area of an ellipse defined by a matrix.
#
#  Discussion:
#
#    The points X in the ellipse are described by a 2 by 2
#    positive definite symmetric matrix A, and a "radius" R, such that
#      X' * A * X <= R * R
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(2,2), the matrix that describes
#    the ellipsoid.  A must be symmetric and positive definite.
#
#    real R, the "radius" of the ellipse.
#
#  Output:
#
#    Output, real VALUE, the area of the ellipse.
#
  import numpy as np

  value = r * r * np.pi / np.sqrt ( a[0,0] * a[1,1] - a[1,0] * a[0,1] )

  return value

def ellipse_area1_test ( ):

#*****************************************************************************80
#
## ellipse_area1_test() tests ellipse_area1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ellipse_area1_test():' )
  print ( '  ellipse_area1() computes the area of an ellipse.' )

  r = 10.0
  A = np.array ( [ [ 5.0, 1.0 ], [ 1.0, 2.0 ] ] )
  area = ellipse_area1 ( A, r )
  print ( '' )
  print ( '  R = %g' % ( r ) )
  print ( '  Matrix A in ellipse definition x*A*x=r^2' )
  print ( A )
  print ( '  Area = %g' % ( area ) )

  return

def ellipse_area2 ( a, b, c, d ):

#*****************************************************************************80
#
## ellipse_area2() returns the area of an ellipse defined by an equation.
#
#  Discussion:
#
#    The ellipse is described by the formula
#      a x^2 + b xy + c y^2 = d
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, coefficients on the left hand side.
#
#    real D, the right hand side.
#
#  Output:
#
#    real VALUE, the area of the ellipse.
#
  import numpy as np

  value = 2.0 * d * d * np.pi / np.sqrt ( 4.0 * a * c - b * b )

  return value

def ellipse_area2_test ( ):

#*****************************************************************************80
#
## ellipse_area2_test() tests ellipse_area2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ellipse_area2_test():' )
  print ( '  ellipse_area2() computes the area of an ellipse.' )

  a = 5.0
  b = 2.0
  c = 2.0
  d = 10.0

  area = ellipse_area2 ( a, b, c, d )
  print ( '' )
  print ( '  Ellipse: %g * x^2 + %g * xy + %g * y^2 = %g' % ( a, b, c, d ) )
  print ( '  Area = %g' % ( area ) )

  return

def ellipse_area3 ( r1, r2 ):

#*****************************************************************************80
#
## ellipse_area3() returns the area of an ellipse defined by the axes.
#
#  Discussion:
#
#    The ellipse is described by the formula
#      (x/r1)^2 + (y/r2)^2 = 1
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
#    real R1, R2, the major and minor radii.
#
#  Output:
#
#    real VALUE, the area of the ellipse.
#
  import numpy as np

  value = np.pi * r1 * r2

  return value

def ellipse_area3_test ( ):

#*****************************************************************************80
#
## ellipse_area3_test() tests ellipse_area3().
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
  print ( 'ellipse_area3_test():' )
  print ( '  ellipse_area3() computes the area of an ellipse.' )

  r1 = 10.0
  r2 = 10.0 / 3.0

  area = ellipse_area3 ( r1, r2 )
  print ( '' )
  print ( '  Ellipse: (x/%g)^2 + (y/%g)^2 = 1' % ( r1, r2 ) )
  print ( '  Area = %g' % ( area ) )

  return

def ellipse_aspect_ratio ( a, b ):

#*****************************************************************************80
#
## ellipse_aspect_ratio() computes the aspect ratio of an ellipse.
#
#  Discussion:
#
#    The ellipse has major and minor semi-axes a and b.  In particular, it
#    could have the form:
#
#      (x/a)^2 + (y/b)^2 = 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Eccentricity, Flattening, and Aspect Ratio,
#    https://www.johndcook.com/blog/2022/10/14/eccentricity-flatness-aspect/
#    Posted 14 October 2022.
#
#  Input:
#
#    real A, B, the major and minor semi-axes.
#
#  Output:
#
#    real VALUE, the aspect ratio of the ellipse.
#
  import numpy as np

  a = abs ( a )
  b = abs ( b )

  if ( a < b ):
    c = a
    a = b
    b = c

  value = b / a

  return value

def ellipse_aspect_ratio_test ( ):

#*****************************************************************************80
#
## ellipse_aspect_ratio_test() tests ellipse_aspect_ratio().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ellipse_aspect_ratio_test():' )
  print ( '  ellipse_aspect_ratio() computes the aspect ratio of an ellipse.' )
  print ( '' )
  print ( '      A      B      Ratio' )
  print ( '' )
  a = 1.0
  n = 10
  for i in range ( 0, n + 1 ):
    b = float ( i ) / n
    e = ellipse_aspect_ratio ( a, b )
    print ( '  %5.1f  %5.1f  %10.6f' % ( a, b, e ) )

  return

def ellipse_eccentricity ( a, b ):

#*****************************************************************************80
#
## ellipse_eccentricity() computes the eccentricity of an ellipse.
#
#  Discussion:
#
#    The ellipse has major and minor semi-axes a and b.  In particular, it
#    could have the form:
#
#      (x/a)^2 + (y/b)^2 = 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Eccentricity, Flattening, and Aspect Ratio,
#    https://www.johndcook.com/blog/2022/10/14/eccentricity-flatness-aspect/
#    Posted 14 October 2022.
#
#  Input:
#
#    real A, B, the major and minor semi-axes.
#
#  Output:
#
#    real VALUE, the eccentricity of the ellipse.
#
  import numpy as np

  a = abs ( a )
  b = abs ( b )

  if ( a < b ):
    c = a
    a = b
    b = c

  value = np.sqrt ( 1.0 - ( b / a )**2 )

  return value

def ellipse_eccentricity_test ( ):

#*****************************************************************************80
#
## ellipse_eccentricity_test() tests ellipse_eccentricity().
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
  print ( 'ellipse_eccentricity_test():' )
  print ( '  ellipse_eccentricity() computes the eccentricity of an ellipse.' )
  print ( '' )
  print ( '      A      B      Ecc' )
  print ( '' )
  a = 1.0
  n = 10
  for i in range ( 0, n + 1 ):
    b = float ( i ) / n
    e = ellipse_eccentricity ( a, b )
    print ( '  %5.1f  %5.1f  %10.6f' % ( a, b, e ) )

  return

def ellipse_flattening ( a, b ):

#*****************************************************************************80
#
## ellipse_flattening() computes the flattening of an ellipse.
#
#  Discussion:
#
#    The ellipse has major and minor semi-axes a and b.  In particular, it
#    could have the form:
#
#      (x/a)^2 + (y/b)^2 = 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Eccentricity, Flattening, and Aspect Ratio,
#    https://www.johndcook.com/blog/2022/10/14/eccentricity-flatness-aspect/
#    Posted 14 October 2022.
#
#  Input:
#
#    real A, B, the major and minor semi-axes.
#
#  Output:
#
#    real VALUE: the flattening of the ellipse.
#
  import numpy as np

  a = abs ( a )
  b = abs ( b )

  if ( a < b ):
    c = a
    a = b
    b = c

  value = ( a - b ) / a

  return value

def ellipse_flattening_test ( ):

#*****************************************************************************80
#
## ellipse_flattening_test() tests ellipse_flattening().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ellipse_flattening_test():' )
  print ( '  ellipse_flattening() computes the flattening of an ellipse.' )
  print ( '' )
  print ( '      A      B      Flat' )
  print ( '' )
  a = 1.0
  n = 10
  for i in range ( 0, n + 1 ):
    b = float ( i ) / n
    e = ellipse_flattening ( a, b )
    print ( '  %5.1f  %5.1f  %10.6f' % ( a, b, e ) )

  return

def ellipse_grid ( a, b, n ):

#*****************************************************************************80
#
## ellipse_grid() computes equally spaced points on an ellipse.
#
#  Discussion:
#
#    The ellipse could have the form:
#
#      (x/a)^2 + (y/b)^2 = 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Uniform Sampling from an Ellipse,
#    https://www.johndcook.com/blog/2022/11/02/ellipse-rng/
#    Posted 02 November 2022.
#
#  Input:
#
#    real A, B: the major and minor semi-axes.
#
#    integer N: the number of grid points.
#
#  Output:
#
#    real X(N), Y(N): the grid points.
#
  import numpy as np

  x = np.zeros ( n )
  y = np.zeros ( n )

  if ( n == 1 ):
    x = np.array ( [ a ] )
    y = np.array ( [ 0.0 ] )
  else:
    perim = ellipse_perimeter ( a, b )
    ell = np.linspace ( 0.0, perim, n + 1 )
    ell = np.delete ( ell, n )
    t = ellipse_t_from_arc_length ( a, b, ell )
    x, y = ellipse_xy_from_t ( a, b, t )

  return x, y

def ellipse_grid_test ( ):

#*****************************************************************************80
#
## ellipse_grid_test() tests ellipse_grid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'ellipse_grid_test()' )
  print ( '  ellipse_grid() computes equally spaced points on the' )
  print ( '  perimeter of an ellipse.' )

  a = 10.0
  b = 3.0
  n = 32
  x, y = ellipse_grid ( a, b, n )

  ne = 501
  te = np.linspace ( 0.0, 2.0 * np.pi, n )
  xe = a * np.cos ( te )
  ye = b * np.sin ( te )

  plt.clf ( )
  plt.plot ( xe, ye, 'k-', linewidth = 2 )
  plt.plot ( x, y, 'go', markersize = 10 )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.title ( 'Equally spaced points on an ellipse' )
  filename = 'ellipse_grid.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def ellipse_perimeter ( a, b ):

#*****************************************************************************80
#
## ellipse_perimeter() computes the length of the perimeter of an ellipse.
#
#  Discussion:
#
#    The ellipse has major and minor semi-axes a and b.  In particular, it
#    could have the form:
#
#      (x/a)^2 + (y/b)^2 = 1
#
#    Computing the exact value requires evaluating the complete elliptic
#    integral of the second kind.
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
#    Simple approximation of the perimeter of an ellipse,
#    24 March 2021
#    https://www.johndcook.com/blog/2021/03/24/perimeter-of-an-ellipse/
#
#  Input:
#
#    real A, B, the major and minor semi-axes.
#
#  Output:
#
#    real VALUE, the length of the perimeter.
#
  from scipy.special import ellipe
  import numpy as np

  a = abs ( a )
  b = abs ( b )

  if ( a < b ):
    c = a
    a = b
    b = c

  ecc_sq = 1.0 - ( b / a )**2

  value = 4.0 * a * ellipe ( ecc_sq )

  return value

def ellipse_perimeter_test ( ):

#*****************************************************************************80
#
## ellipse_perimeter_test() tests ellipse_perimeter().
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
  print ( 'ellipse_perimeter_test():' )
  print ( '  ellipse_perimeter() computes the perimeter of an ellipse.' )
  print ( '' )
  print ( '      A      B      P' )
  print ( '' )
  a = 1.0
  n = 10
  for i in range ( 0, n + 1 ):
    b = float ( i ) / n
    p = ellipse_perimeter ( a, b )
    print ( '  %5.1f  %5.1f  %10.6f' % ( a, b, p ) )

  return

def ellipse_point_near ( a, b, p ):

#*****************************************************************************80
#
## ellipse_point_near() finds the nearest point on an ellipse in 2D.
#
#  Discussion:
#
#    The ellipse is required to have the canonical form:
#
#      (X/A)^2 + (Y/B)^2 = 1
#
#    The nearest point PN on the ellipse has the property that the
#    line from PN to P is normal to the ellipse.  Points on the ellipse
#    can be parameterized by T, to have the form
#
#      ( A * cos ( T ), B * sin ( T ) ).
#
#    The tangent vector to the ellipse has the form
#
#      ( - A * sin ( T ), B * cos ( T ) ) 
#
#    At PN, the dot product of this vector with  ( P - PN ) must be
#    zero:
#
#      - A * sin ( T ) * ( X - A * cos ( T ) )
#      + B * cos ( T ) * ( Y - B * sin ( T ) ) = 0
#
#    This nonlinear equation for T can be solved by Newton's method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the ellipse parameters.  Normally,
#    these are both positive quantities.  Generally, they are also
#    distinct.
#
#    real P(2), the point.
#
#  Output:
#
#    real PN(2), the point on the ellipse which
#    is closest to P.
#
  import numpy as np

  iteration_max = 100
  eps = np.finfo ( float ).eps

  x = abs ( p[0] )
  y = abs ( p[1] )

  if ( y == 0.0 and a * a - b * b <= a * x ):

    t = 0.0

  elif ( x == 0.0 and b * b - a * a <= b * y ):

    t = np.pi / 2.0

  else:

    if ( y == 0.0 ):
      y = np.sqrt ( eps ) * abs ( b )

    if ( x == 0.0 ):
      x = np.sqrt ( eps ) * abs ( a )
#
#  Initial parameter T:
#
    t = np.arctan2 ( y, x )

    iteration = 0

    while ( True ):

      ct = np.cos ( t )
      st = np.sin ( t )

      f = ( x - abs ( a ) * ct ) * abs ( a ) * st \
        - ( y - abs ( b ) * st ) * abs ( b ) * ct

      if ( abs ( f ) <= 100.0 * eps ):
        break

      if ( iteration_max <= iteration ):
        print ( '' )
        print ( 'ellipse_point_near - Warning!' )
        print ( '  Reached iteration limit.' )
        print ( '  T = %f' % ( t ) )
        print ( '  F = %f' % ( f ) )
        break

      iteration = iteration + 1

      fp = a * a * st * st + b * b * ct * ct \
         + ( x - abs ( a ) * ct ) * abs ( a ) * ct \
         + ( y - abs ( b ) * st ) * abs ( b ) * st

      t = t - f / fp
#
#  From the T value, we get the nearest point.
#
  pn = np.zeros ( 2 )

  pn[0] = abs ( a ) * np.cos ( t )
  pn[1] = abs ( b ) * np.sin ( t )
#
#  Take care of case where the point was in another quadrant.
#
  pn[0] = r8_sign ( p[0] ) * pn[0]
  pn[1] = r8_sign ( p[1] ) * pn[1]

  return pn

def ellipse_point_near_test ( ):

#*****************************************************************************80
#
## ellipse_point_near_test() tests ellipse_point_near().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  a = 3.0
  b = 2.0
  n = 10

  print ( '' )
  print ( 'ellipse_point_near_test():' )
  print ( '  ellipse_point_near() is given a point P, and' )
  print ( '  finds the nearest point PN on an ellipse in 2D.' )
  print ( '' )
  print ( '  The ellipse is (X/A)^2 + (Y/B)^2 = 1' )
  print ( '' )
  print ( '  A = %f' % ( a ) )
  print ( '  B = %f' % ( b ) )
  print ( '' )
  print ( '           P                PN' )
  print ( '' )

  p = np.zeros ( 2 )

  for i in range ( -3, n + 4 ):

    p[0] = ( float ( n - i ) * 0.0 + float ( i ) * 4.0 ) / float ( n )
    p[1] = ( float ( n - i ) * 3.0 + float ( i ) * 0.0 ) / float ( n )

    pn = ellipse_point_near ( a, b, p )

    print ( '  %10f  %10f    %10f  %10f' % ( p[0], p[1], pn[0], pn[1] ) )

  return

def ellipse_sample ( a, b, n, rng ):

#*****************************************************************************80
#
## ellipse_sample() samples uniform random points on an ellipse.
#
#  Discussion:
#
#    The ellipse could have the form:
#
#      (x/a)^2 + (y/b)^2 = 1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Uniform Sampling from an Ellipse,
#    https://www.johndcook.com/blog/2022/11/02/ellipse-rng/
#    Posted 02 November 2022.
#
#  Input:
#
#    real A, B: the major and minor semi-axes.
#
#    integer N: the number of grid points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(N), Y(N): the sample points.
#
  import numpy as np

  perim = ellipse_perimeter ( a, b )
  ell = perim * rng.random ( size = n )
  t = ellipse_t_from_arc_length ( a, b, ell )
  x, y = ellipse_xy_from_t ( a, b, t )

  return x, y

def ellipse_sample_test ( ):

#*****************************************************************************80
#
## ellipse_sample_test() tests ellipse_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'ellipse_sample_test()' )
  print ( '  ellipse_sample() samples random points on the' )
  print ( '  perimeter of an ellipse.' )

  rng = default_rng ( )

  a = 10.0
  b = 3.0
  n = 128
  x, y = ellipse_sample ( a, b, n, rng )

  ne = 501
  te = np.linspace ( 0.0, 2.0 * np.pi, n )
  xe = a * np.cos ( te )
  ye = b * np.sin ( te )

  plt.clf ( )
# plt.plot ( xe, ye, 'k-', linewidth = 2 )
  plt.plot ( x, y, 'go', markersize = 5 )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.title ( 'Random points on an ellipse' )
  filename = 'ellipse_sample.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def ellipse_t_from_arc_length ( a, b, ell ):

#*****************************************************************************80
#
## ellipse_t_from_arclength() converts arclength to angle for ellipse points.
#
#  Discussion:
#
#    The ellipse has major and minor semi-axes a and b.  In particular, it
#    could have the form:
#
#      (x/a)^2 + (y/b)^2 = 1
#
#    The arclength ell of a point (x,y) is the distance along the ellipse 
#    from (a,0) to (x,y).  The angle t is related to (x,y) by:
#
#      x = a cos ( t )
#      y = b sin ( t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Uniform Sampling from an Ellipse,
#    https://www.johndcook.com/blog/2022/11/02/ellipse-rng/
#    Posted 02 November 2022.
#
#  Input:
#
#    real A, B: the major and minor semi-axes.
#
#    real ELL(N): the arc length coordinates of the points.
#
#  Output:
#
#    real T(N): the angular coordinates of the points.
#
  from scipy.special import ellipe
  import numpy as np
#
#  Force A to be major axis.
#
  a = np.abs ( a )
  b = np.abs ( b )
  if ( a < b ):
    c = a
    a = b
    b = c
#
#  Compute eccentricity.
#
  m = 1.0 - ( b / a )**2

  arg = ellipe ( m ) - ell / a

  t = 0.5 * np.pi - e_inverse ( arg, m )

  return t

def e_inverse ( z, m ):

#*****************************************************************************80
#
## e_inverse() does something.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Uniform Sampling from an Ellipse,
#    https://www.johndcook.com/blog/2022/11/02/ellipse-rng/
#    Posted 02 November 2022.
#
#  Input:
#
#    real Z: ?.
#
#    real M: the eccentricity of the ellipse, 1-(b/a)**2
#
#  Output:
#
#    real R: ?
#
  from scipy.optimize import newton
  from scipy.special import ellipe
  from scipy.special import ellipeinc
  import numpy as np

  em = ellipe ( m )
  t = ( z / em ) * ( np.pi / 2.0 )
  f = lambda y: ellipeinc ( y, m ) - z
  r = newton ( f, t )

  return r

def ellipse_xy_from_t ( a, b, t ):

#*****************************************************************************80
#
## ellipse_xy_from_t() converts points on an ellipse from angle to Cartesian coordinates.
#
#  Discussion:
#
#    The ellipse has major and minor semi-axes a and b.  In particular, it
#    could have the form:
#
#      (x/a)^2 + (y/b)^2 = 1
#
#    We compute
#
#      x = a cos ( t )
#      y = b sin ( t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Uniform Sampling from an Ellipse,
#    https://www.johndcook.com/blog/2022/11/02/ellipse-rng/
#    Posted 02 November 2022.
#
#  Input:
#
#    real A, B: the major and minor semi-axes.
#
#    real T(N): the angular coordinates of the points.
#
#  Output:
#
#    real X(N), Y(N): the Cartesian coordinates of the points.
#
  import numpy as np

  x = a * np.cos ( t )
  y = b * np.sin ( t )

  return x, y

def ellipsoid_area ( a, b, c ):

#*****************************************************************************80
#
## ellipsoid_area() returns the surface area  of an ellipsoid.
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

def ellipsoid_area_test ( ):

#*****************************************************************************80
#
## ellipsoid_area_test() tests ellipsoid_area().
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
  print ( 'ellipsoid_area_test():' )
  print ( '  ellipsoid_area_test() computes the surface area of the ellipsoid' )
  print ( '    (x/a)^2+(y/b)^2+(z/c)^2=1' )

  print ( '' )
  print ( '           A           B           C        Area' )
  print ( '' )

  a = 1.0
  b = 0.8
  c = 0.625
  area = ellipsoid_area ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 1.0
  b = 1.0
  c = 0.5
  area = ellipsoid_area ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 1.0
  b = 1.0
  c = 1.0
  area = ellipsoid_area ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 2.0
  b = 1.0
  c = 0.25
  area = ellipsoid_area ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  a = 2.0
  b = 3.0
  c = 4.0
  area = ellipsoid_area ( a, b, c )
  print ( '  %10.4g  %10.4g  %10.4g  %10.4g' % ( a, b, c, area ) )

  return

def ellipsoid_volume ( m, A, v, r ):

#*****************************************************************************80
#
## ellipsoid_volume() returns the volume of an ellipsoid.
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

def ellipsoid_volume_test ( ):

#*****************************************************************************80
#
## ellipsoid_volume_test() tests ellipsoid_volume().
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
  print ( 'ellipsoid_volume_test():' )
  print ( '  ellipsoid_volume() computes the volume of the ellipsoid' )
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

  volume = ellipsoid_volume ( m, A, v, r )

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
  ellipse_test ( )
  timestamp ( )

