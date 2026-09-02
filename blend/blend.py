#! /usr/bin/env python3
#
def blend_test ( ):

#*****************************************************************************80
#
## blend_test() tests blend().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'blend_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test blend().' )

  blend_101_test ( )
  blend_102_test ( )
  blend_103_test ( )

  blend_112_test ( )
  blend_113_test ( )

  blend_123_test ( )

  blend_i_0d1_test ( )

  blend_ij_0d1_test ( )
  blend_ij_1d1_test ( )
  blend_ij_w_1d1_test ( )

  blend_ijk_0d1_test ( )
  blend_ijk_1d1_test ( )
  blend_ijk_2d1_test ( )

  blend_r_0dn_test ( )
  blend_r_0dn_identity_test ( )
  blend_r_0dn_stretch_test ( )

  blend_rs_0dn_test ( )
  blend_rs_0dn_identity_test ( )
  blend_rs_0dn_stretch_test ( )

  blend_rs_1dn_test ( )
  blend_rs_1dn_identity_test ( )
  blend_rs_1dn_stretch_test ( )

  blend_rst_0dn_identity_test ( )
  blend_rst_0dn_stretch_test ( )

  blend_rst_1dn_identity_test ( )
  blend_rst_1dn_stretch_test ( )

  blend_rst_2dn_identity_test ( )
  blend_rst_2dn_stretch_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'blend_test():' )
  print ( '  Normal end of execution.' )

  return

def blend_101 ( r, x0, x1 ):

#*****************************************************************************80
#
## blend_101() extends scalar endpoint data to a line.
#
#  Diagram:
#
#    0-----r-----1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, the coordinate where an interpolated
#    value is desired.
#
#    real X0, X1, the data values at the ends of the line.
#
#  Output:
#
#    real X, the interpolated data value at (R).
#
  x = ( 1.0 - r ) * x0  \
    +         r   * x1

  return x

def blend_101_test ( ):

#*****************************************************************************80
#
## blend_101_test() tests blend_101().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  n1 = 10

  d = np.zeros ( n1 )

  d[0] = 1
  d[n1-1] = n1

  print ( '' )
  print ( 'blend_101_test():' )
  print ( '  blend_101() blends endpoint values into a list.' )

  print ( '' )
  print ( '  Initial data list:' )
  pprint.pprint ( d )

  for i in range ( 0, n1 ):

    if ( i != 0 and i != n1 - 1 ):
      r = i / ( n1 - 1 )
      d[i] = blend_101 ( r, d[0], d[n1-1] )

  print ( '' )
  print ( '  Blended data list:' )
  pprint.pprint ( d )

  return

def blend_102 ( r, s, x00, x01, x10, x11 ):

#*****************************************************************************80
#
## blend_102() extends scalar point data into a square.
#
#  Diagram:
#
#    01------------11
#     |      .      |
#     |      .      |
#     |.....rs......|
#     |      .      |
#     |      .      |
#    00------------10
#
#  Formula:
#
#    Written in terms of R and S, the map has the form:
#
#      X(R,S) =
#               1     * ( + x00 )
#             + r     * ( - x00 + x10 )
#             + s     * ( - x00       + x01 )
#             + r * s * ( + x00 - x10 - x01 + x11 )
#
#    Written in terms of the coefficients, the map has the form:
#
#      X(R,S) = x00 * ( 1 - r - s + r * s )
#             + x01 * (         s - r * s )
#             + x10 * (     r     - r * s )
#             + x11 * (             r * s )
#
#             = x00 * ( 1 - r ) * ( 1 - s )
#             + x01 * ( 1 - r ) *       s
#             + x10 *       r   * ( 1 - s )
#             + x11 *       r           s
#
#    The nonlinear term ( r * s ) has an important role:
#
#      If ( x01 + x10 - x00 - x11 ) is zero, then the input data lies in
#      a plane, and the mapping is affine.  All the interpolated data
#      will lie on the plane defined by the four corner values.  In
#      particular, on any line through the square, data values at
#      intermediate points will lie between the values at the endpoints.
#
#      If ( x01 + x10 - x00 - x11 ) is not zero, then the input data does
#      not lie in a plane, and the interpolation map is nonlinear.  On
#      any line through the square, data values at intermediate points
#      may lie above or below the data values at the endpoints.  The
#      size of the coefficient of r * s will determine how severe this
#      effect is.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, S, the coordinates where an
#    interpolated value is desired.
#
#    real X00, X01, X10, X11, the data values
#    at the corners.
#
#  Output:
#
#    real X, the interpolated data value at (R,S).
#
  x =             + x00 \
      + r *     ( - x00 + x10 ) \
      + s *     ( - x00       + x01 ) \
      + r * s * ( + x00 - x10 - x01 + x11 )

  return x

def blend_102_test ( ):

#*****************************************************************************80
#
## blend_102_test() tests blend_102().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_102_test():' )
  print ( '  blend_102() blends corner values into a table.' )

  n1 = 5
  n2 = 5

  d = np.zeros ( [ n1, n2 ] )

  for i in [ 0, n1 - 1 ]:
    for j in [ 0, n2 - 1 ]:
      d[i,j] = i + 1 + j + 1

  print ( '' )
  print ( '  Initial data array:' )
  pprint.pprint ( d )

  for i in range ( 0, n1 ):

    r = i / ( n1 - 1 )

    for j in range ( 0, n2 ):

      s = j / ( n2 - 1 )

      if ( \
        ( i == 0 or i == n1 - 1 ) and \
        ( j == 0 or j == n2 - 1 ) ):
        continue

      d[i,j] = blend_102 ( r, s, d[0,0], d[0,n2-1], d[n1-1,0], d[n1-1,n2-1] )

  print ( '' )
  print ( '  Blended data array:' )
  pprint.pprint ( d )

  return

def blend_103 ( r, s, t, x000, x001, x010, x011, x100, x101, x110, x111 ):

#*****************************************************************************80
#
## blend_103() extends scalar point data into a cube.
#
#  Diagram:
#
#    011--------------111
#      |               |
#      |               |
#      |               |
#      |               |
#      |               |
#    001--------------101
#
#
#      *---------------*
#      |               |
#      |               |
#      |      rst      |
#      |               |
#      |               |
#      *---------------*
#
#
#    010--------------110
#      |               |
#      |               |
#      |               |
#      |               |
#      |               |
#    000--------------100
#
#
#  Formula:
#
#    Written as a polynomial in R, S and T, the interpolation map has the
#    form:
#
#      X(R,S,T) =
#        1         * ( + x000 )
#      + r         * ( - x000 + x100 )
#      +     s     * ( - x000        + x010 )
#      +         t * ( - x000               + x001 )
#      + r * s     * ( + x000 - x100 - x010                       + x110 )
#      + r     * t * ( + x000 - x100        - x001        + x101 )
#      +     s * t * ( + x000        - x010 - x001 + x011 )
#      + r * s * t * ( - x000 + x100 + x010 + x001 - x011 - x101 - x110 + x111 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, S, T, the coordinates where an
#    interpolated value is desired.
#
#    real X000, X001, X010, X011, X100, X101, X110,
#    X111, the data values at the corners.
#
#  Output:
#
#    real X, the interpolated data value at (R,S,T).
#

#
#  Interpolate the interior point.
#
  x = \
    1.0         * ( + x000 ) \
    + r         * ( - x000 + x100 ) \
    +     s     * ( - x000        + x010 ) \
    +         t * ( - x000               + x001 ) \
    + r * s     * ( + x000 - x100 - x010                      + x110 ) \
    + r     * t * ( + x000 - x100        - x001        + x101 ) \
    +     s * t * ( + x000        - x010 - x001 + x011 ) \
    + r * s * t * ( - x000 + x100 + x010 + x001 - x011 - x101 - x110 + x111 )

  return x

def blend_103_test ( ):

#*****************************************************************************80
#
## blend_103_test() tests blend_103().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_103_test():' )
  print ( '  blend_103() blends corner values into a table.' )

  n1 = 3
  n2 = 5
  n3 = 4

  d = np.zeros ( [ n1, n2, n3 ] )

  for i in [ 0, n1 - 1 ]:
    for j in [ 0, n2 - 1 ]:
      for k in [ 0, n3 - 1 ]:
        d[i,j,k] = ( i + 1 + j + 1 + k + 1 )

  print ( '' )
  print ( '  Initial data array:' )
  pprint.pprint ( d )

  for i in range ( 0, n1 ):

    r = i / ( n1 - 1 )

    for j in range ( 0, n2 ):

      s = j / ( n2 - 1 )

      for k in range ( 0, n3 ):

        t = k / ( n3 - 1 )

        if ( \
          ( i == 0 or i == n1 ) and \
          ( j == 0 or j == n2 ) and \
          ( k == 0 or k == n3  ) ):
          continue

        d[i,j,k] = blend_103 ( r, s, t, \
          d[0,0,0], d[0,0,n3-1], d[0,n2-1,0], d[0,n2-1,n3-1], \
          d[n1-1,0,0], d[n1-1,0,n3-1], d[n1-1,n2-1,0], d[n1-1,n2-1,n3-1] )

  print ( '' )
  print ( '  Blended data array:' )
  pprint.pprint ( d )

  return

def blend_112 ( r, s, x00, x01, x10, x11, xr0, xr1, x0s, x1s ):

#*****************************************************************************80
#
## blend_112() extends scalar line data into a square.
#
#  Diagram:
#
#    01-----r1-----11
#     |      .      |
#     |      .      |
#    0s.....rs.....1s
#     |      .      |
#     |      .      |
#    00-----r0-----10
#
#  Formula:
#
#    Written in terms of R and S, the interpolation map has the form:
#
#      X(R,S) =
#               1     * ( - x00       + x0s                   + xr0 )
#             + r     * (   x00       - x0s - x10       + x1s )
#             + s     * (   x00 - x01                         - xr0 + xr1 )
#             + r * s * ( - x00 + x01       + x10 - x11 )
#
#    Written in terms of the data, the map has the form:
#
#      X(R,S) =
#             - ( 1 - r ) * ( 1 - s ) * x00
#             + ( 1 - r )             * x0s
#             - ( 1 - r ) *       s   * x01
#             +             ( 1 - s ) * xr0
#             +                   s   * xr1
#             -       r   * ( 1 - s ) * x10
#             +       r               * x1s
#             -       r   *       s   * x11
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, S, the coordinates where an interpolated
#    value is desired.
#
#    real X00, X01, X10, X11, the data values
#    at the corners.
#
#    real XR0, XR1, X0S, X1S, the data values at
#    points along the edges corresponding to (R,0), (R,1), (0,S) and (1,S).
#
#  Output:
#
#    real X, the interpolated data value at (R,S).
#
  x = - ( 1.0 - r ) * ( 1.0 - s ) * x00 \
      + ( 1.0 - r )               * x0s \
      - ( 1.0 - r ) *         s   * x01 \
      +               ( 1.0 - s ) * xr0 \
      +                       s   * xr1 \
      -         r   * ( 1.0 - s ) * x10 \
      +         r                 * x1s \
      -         r   *         s   * x11

  return x

def blend_112_test ( ):

#*****************************************************************************80
#
## blend_112_test() tests blend_112().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_112_test():' )
  print ( '  blend_112() blends side values into a table.' )
  print ( '' )

  n1 = 5
  n2 = 5

  d = np.zeros ( [ n1, n2 ] )

  for i in range ( 0, n1 ):
    for j in range ( 0, n2 ):
      if ( i == 0 or i == n1 - 1 or j == 0 or j == n2 - 1 ):
        d[i,j] = i + 1 + j + 1

  print ( '' )
  print ( '  Initial data array' )
  pprint.pprint ( d )

  for i in range ( 0, n1 - 1 ):

    r = i  / ( n1 - 1 )

    for j in range ( 0, n2 ):

      s = j / ( n2 - 1 )

      d[i,j] = blend_112 ( r, s, d[0,0], d[0,n2-1], d[n1-1,0], d[n1-1,n2-1], \
        d[i,0], d[i,n2-1], d[0,j], d[n1-1,j] )

  print ( '' )
  print ( '  Blended data array' )
  pprint.pprint ( d )

  return

def blend_113 ( r, s, t, x000, x001, x010, x011, x100, x101, x110, \
  x111, xr00, xr01, xr10, xr11, x0s0, x0s1, x1s0, x1s1, x00t, x01t, x10t, \
  x11t ):

#*****************************************************************************80
#
## blend_113() extends scalar line data into a cube.
#
#  Diagram:
#
#     011-----r11-----111
#      |               |
#      |               |
#     0s1             1s1
#      |               |
#      |               |
#     001-----r01-----101
#
#
#     01t-------------11t
#      |               |
#      |               |
#      |      rst      |
#      |               |
#      |               |
#     00t-------------10t
#
#
#     010-----r10-----110
#      |               |
#      |               |
#     0s0             1s0
#      |               |
#      |               |
#     000-----r00-----100
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, S, T, the coordinates where an interpolated
#    value is desired.
#
#    real X000, X001, X010, X011, X100, X101, X110,
#    X111, the data values at the corners.
#
#    real XR00, XR01, XR10, XR11, X0S0, X0S1, X1S0,
#    X1S1, X00T, X01T, X10T, X11T, the data values at points along the edges.
#
#  Output:
#
#    real X, the interpolated data value at (R,S,T).
#

#
#  Interpolate the points in the centers of the faces.
#
  x0st = blend_112 ( s, t, x000, x001, x010, x011, x0s0, x0s1, x00t, x01t )
  x1st = blend_112 ( s, t, x100, x101, x110, x111, x1s0, x1s1, x10t, x11t )
  xr0t = blend_112 ( r, t, x000, x001, x100, x101, xr00, xr01, x00t, x10t )
  xr1t = blend_112 ( r, t, x010, x011, x110, x111, xr10, xr11, x01t, x11t )
  xrs0 = blend_112 ( r, s, x000, x010, x100, x110, xr00, xr10, x0s0, x1s0 )
  xrs1 = blend_112 ( r, s, x001, x011, x101, x111, xr01, xr11, x0s1, x1s1 )
#
#  Interpolate the I-th coordinate component of the interior point.
#
  x = blend_123 ( r, s, t, x000, x001, x010, x011, x100, x101, x110, x111, \
    xr00, xr01, xr10, xr11, x0s0, x0s1, x1s0, x1s1, x00t, x01t, x10t, x11t, \
    x0st, x1st, xr0t, xr1t, xrs0, xrs1 )

  return x

def blend_113_test ( ):

#*****************************************************************************80
#
## blend_113_test() tests blend_113().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_113_test():' )
  print ( '  blend_113() blends edge values into a table.' )

  n1 = 3
  n2 = 5
  n3 = 4

  d = np.zeros ( [ n1, n2, n3 ] )

  for i in range ( 0, n1 ):
    for j in range ( 0, n2 ):
      for k in range ( 0, n3 ):
        if ( \
          ( ( i == 0 or i == n1 - 1 ) and ( j == 0 or j == n2 - 1 ) ) or \
          ( ( i == 0 or i == n1 - 1 ) and ( k == 0 or k == n3 - 1 ) ) or \
          ( ( j == 0 or j == n2 - 1 ) and ( k == 0 or k == n3 - 1 ) ) ):
          d[i,j,k] = i + 1 + j + 1 + k + 1

  print ( '' )
  print ( '  Initial data array' )
  pprint.pprint ( d )

  for i in range ( 0, n1 ):

    r = i / ( n1 - 1 )

    for j in range ( 0, n2 ):

      s = j / ( n2 - 1 )

      for k in range ( 0, n3 ):

        t = k / ( n3 - 1 )

        if ( \
          ( ( i == 0 or i == n1 - 1 ) and ( j == 0 or j == n2 - 1 ) ) or \
          ( ( i == 0 or i == n1 - 1 ) and ( k == 0 or k == n3 - 1 ) ) or \
          ( ( j == 0 or j == n2 - 1 ) and ( k == 0 or k == n3 - 1 ) ) ):
          continue

        d[i,j,k] = blend_113 ( r, s, t, \
          d[0,0,0], d[0,0,n3-1], d[0,n2-1,0], d[0,n2-1,n3-1], \
          d[n1-1,0,0], d[n1-1,0,n3-1], d[n1-1,n2-1,0], d[n1-1,n2-1,n3-1], \
          d[i,0,0], d[i,0,n3-1], d[i,n2-1,0], d[i,n2-1,n3-1], \
          d[0,j,0], d[0,j,n3-1], d[n1-1,j,0], d[n1-1,j,n3-1], \
          d[0,0,k], d[0,n2-1,k], d[n1-1,0,k], d[n1-1,n2-1,k] )

  print ( '' )
  print ( '  Initial data array' )
  pprint.pprint ( d )

  return

def blend_123 ( r, s, t, x000, x001, x010, x011, x100, x101, x110, \
  x111, xr00, xr01, xr10, xr11, x0s0, x0s1, x1s0, x1s1, x00t, x01t, x10t, \
  x11t, x0st, x1st, xr0t, xr1t, xrs0, xrs1 ):

#*****************************************************************************80
#
## blend_123() extends scalar face data into a cube.
#
#  Diagram:
#
#    010-----r10-----110        011-----r11-----111
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    0s0.....rs0.....1s0        0s1.....rs1.....1s1     S
#      |       .       |          |       .       |     |
#      |       .       |          |       .       |     |
#    000-----r00-----100        001-----r01-----101     +----R
#           BOTTOM                      TOP
#
#    011-----0s1-----001        111-----1s1-----101
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    01t.....0st.....00t        11t.....1st.....10t          T
#      |       .       |          |       .       |          |
#      |       .       |          |       .       |          |
#    010-----0s0-----000        110-----1s0-----100     S----+
#           LEFT                       RIGHT
#
#    001-----r01-----101        011-----r11-----111
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    00t.....r0t.....100        01t.....r1t.....11t     T
#      |       .       |          |       .       |     |
#      |       .       |          |       .       |     |
#    000-----r00-----100        010-----r10-----110     +----R
#           FRONT                       BACK
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, S, T, the coordinates where an interpolated
#    value is desired.
#
#    real X000, X001, X010, X011, X100, X101, X110,
#    X111, the data values at the corners.
#
#    real XR00, XR01, XR10, XR11, X0S0, X0S1, X1S0,
#    X1S1, X00T, X01T, X10T, X11T, the data values at points along the edges.
#
#    real X0ST, X1ST, XR0T, XR1T, XRS0, XRS1, the
#    data values at points on the faces.
#
#  Output:
#
#    real X, the interpolated data value at (R,S,T).
#

#
#  Interpolate the interior point.
#
  x =        ( 1.0 - r ) * ( 1.0 - s ) * ( 1.0 - t ) * x000 \
           - ( 1.0 - r ) * ( 1.0 - s )               * x00t \
           + ( 1.0 - r ) * ( 1.0 - s ) *         t   * x001 \
           - ( 1.0 - r )               * ( 1.0 - t ) * x0s0 \
           + ( 1.0 - r )                             * x0st \
           - ( 1.0 - r )                   *     t   * x0s1 \
           + ( 1.0 - r ) *         s   * ( 1.0 - t ) * x010 \
           - ( 1.0 - r ) *         s                 * x01t \
           + ( 1.0 - r ) *         s   *         t   * x011 \
           -               ( 1.0 - s ) * ( 1.0 - t ) * xr00 \
           +               ( 1.0 - s )               * xr0t \
           -               ( 1.0 - s ) *         t   * xr01 \
           +                             ( 1.0 - t ) * xrs0 \
           +                                     t   * xrs1 \
           -                       s   * ( 1.0 - t ) * xr10 \
           +                       s                 * xr1t \
           -                       s   *         t   * xr11 \
           +         r   * ( 1.0 - s ) * ( 1.0 - t ) * x100 \
           -         r   * ( 1.0 - s )               * x10t \
           +         r   * ( 1.0 - s ) *         t   * x101 \
           -         r                 * ( 1.0 - t ) * x1s0 \
           +         r                               * x1st \
           -         r                 *         t   * x1s1 \
           +         r   *         s   * ( 1.0 - t ) * x110 \
           -         r   *         s                 * x11t \
           +         r   *         s   *         t   * x111

  return x

def blend_123_test ( ):

#*****************************************************************************80
#
## blend_123_test() tests blend_123().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_123_test():' )
  print ( '  blend_123() blends face values into a table.' )

  n1 = 3
  n2 = 5
  n3 = 4

  d = np.zeros ( [ n1, n2, n3 ] )

  for i in range ( 0, n1 ):
    for j in range ( 0, n2 ):
      for k in range ( 0, n3 ):
        if ( i == 0 or i == n1 - 1 \
          or j == 0 or j == n2 - 1 \
          or k == 0 or k == n3 - 1 ):
          d[i,j,k] = i + 1 + j + 1 + k + 1

  print ( '' )
  print ( '  Initial data array' )
  pprint.pprint ( d )

  for i in range ( 1, n1 - 1 ):

    r = i / ( n1 - 1 )

    for j in range ( 1, n2 - 1 ):

      s = j / ( n2 - 1 )

      for k in range ( 1, n3 - 1 ):

        t = k / ( n3 - 1 )

        d[i,j,k] = blend_123 ( r, s, t, \
          d[0,0,0], d[0,0,n3-1], d[0,n2-1,0], d[0,n2-1,n3-1], \
          d[n1-1,0,0], d[n1-1,0,n3-1], d[n1-1,n2-1,0], d[n1-1,n2-1,n3-1], \
          d[i,0,0], d[i,0,n3-1], d[i,n2-1,0], d[i,n2-1,n3-1], \
          d[0,j,0], d[0,j,n3-1], d[n1-1,j,0], d[n1-1,j,n3-1], \
          d[0,0,k], d[0,n2-1,k], d[n1-1,0,k], d[n1-1,n2-1,k], \
          d[0,j,k], d[n1-1,j,k], d[i,0,k], d[i,n2-1,k], d[i,j,0], d[i,j,n3-1] )

  print ( '' )
  print ( '  Blended data array' )
  pprint.pprint ( d )

  return

def blend_i_0d1 ( x, m ):

#*****************************************************************************80
#
## blend_i_0d1() extends indexed scalar data at endpoints along a line.
#
#  Diagram:
#
#    ( X1, ..., ..., ..., ..., ..., XM )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real X(M).  X(1) and X(M) contain scalar values which are to be
#    interpolated through the entries X(2) through X(M).  It is assumed
#    that the dependence of the data is linear in the vector index I.
#
#    integer M, the number of entries in X.
#
#  Output:
#
#    real X(M).  X(2) through X(M-1) have been assigned interpolated
#    values.
#
  for i in range ( 1, m - 1 ):
    r = i / ( m - 1 )
    x[i] = blend_101 ( r, x[0], x[m-1] )

  return x

def blend_i_0d1_test ( ):

#*****************************************************************************80
#
## blend_i_0d1_test() tests blend_i_0d1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  m = 5

  x = np.zeros ( m )

  x[0] = 100.0
  x[m-1] = 100.0 + ( m - 1 ) * 5

  print ( '' )
  print ( 'blend_i_0d1_test():' )
  print ( '  blend_i_0d1() interpolates data in a vector.' )

  print ( '' )
  print ( '  Data values:' )
  pprint.pprint ( x )

  x = blend_i_0d1 ( x, m )

  print ( '' )
  print ( '  Blended values:' )
  pprint.pprint ( x )

  return

def blend_ij_0d1 ( x, m1, m2 ):

#*****************************************************************************80
#
## blend_ij_0d1() extends indexed scalar data at corners into a table.
#
#  Diagram:
#
#    ( X11,  ..., ..., ..., ..., ..., X1M2  )
#    ( ...,  ..., ..., ..., ..., ..., ...   )
#    ( ...,  ..., ..., ..., ..., ..., ...   )
#    ( ...,  ..., ..., ..., ..., ..., ...   )
#    ( XM11, ..., ..., ..., ..., ..., XM1M2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2008
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real X(M1,M2).  On X(1,1), X(1,M2), X(M1,1) and X(M1,M2) 
#    contain scalar values which are to be interpolated throughout the table, 
#    using the table indices I and J as independent variables.
#
#    integer M1, M2, the number of rows and columns in X.
#
#  Output:
#
#    real X(M1,M2), all entries in X have been assigned a value.
#
  import numpy as np
#
#  Interpolate values along the edges.
#
  for i in range ( 1, m1 - 1 ):
    r = i / ( m1 - 1 )
    x[i,0] = blend_101 ( r, x[0,0], x[m1-1,0] )
    x[i,m2-1] = blend_101 ( r, x[0,m2-1], x[m1-1,m2-1] )

  for j in range ( 1, m2 - 1 ):
    s = j / ( m2 - 1 )
    x[0,j] = blend_101 ( s, x[0,0], x[0,m2-1] )
    x[m1-1,j] = blend_101 ( s, x[m1-1,0], x[m1-1,m2-1] )
#
#  Interpolate values in the interior.
#
  for i in range ( 1, m1 - 1 ):
    r = i / ( m1 - 1 )
    for j in range ( 1, m2 - 1 ):
      s = j / ( m2 - 1 )
      x[i,j] = blend_112 ( r, s, x[0,0], x[0,m2-1], x[m1-1,0], x[m1-1,m2-1], \
        x[i,0], x[i,m2-1], x[0,j], x[m1-1,j] )

  return x

def blend_ij_0d1_test ( ):

#*****************************************************************************80
#
## blend_ij_0d1_test() tests blend_ij_0d1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  m1 = 5
  m2 = 4

  print ( '' )
  print ( 'blend_ij_0d1_test():' )
  print ( '  blend_ij_0d1() interpolates data in a table,' )
  print ( '  from corner data.' )

  x = np.zeros ( [ m1, m2 ] )
#
#  Load data in the corners only.
#
  for i in [ 0, m1 - 1 ]:
    for j in [ 0, m2 - 1 ]:
      r = i / ( m1 - 1 )
      s = j / ( m2 - 1 )
      x[i,j] = cubic_rs ( r, s, 1 )

  print ( '' )
  print ( '  Data:' )
  pprint.pprint ( x )

  x = blend_ij_0d1 ( x, m1, m2 )

  print ( '' )
  print ( '  Blended data:' )
  pprint.pprint ( x )

  return

def blend_ij_1d1 ( x, m1, m2 ):

#*****************************************************************************80
#
## blend_ij_1d1() extends indexed scalar data along edges into a table.
#
#  Diagram:
#
#    ( X11,  X12,  X13,  X14,  X15,  X16,  X1M2  )
#    ( X21,  \,  \,  \,  \,  \,  X2M2  )
#    ( X31,  \,  \,  \,  \,  \,  X3M2  )
#    ( X41,  \,  \,  \,  \,  \,  X4M2  )
#    ( XM11, XM12, XM13, XM14, XM15, XM16, XM1M2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real X(M1,M2).  On data is contained in the "edge entries" 
#    X(1,J), X(I,1), X(M1,J) and X(I,M2), for I = 1 to M1, and J = 1 to M2.
#
#    integer M1, M2, the number of rows and columns in X.
#
#  Output:
#
#    real X(M1,M2), all entries in X have been assigned a value.
#

#
#  Interpolate values in the interior.
#
  for i in range ( 1, m1 - 1 ):

    r = i / ( m1 - 1 )

    for j in range ( 1, m2 - 1 ):

      s = j / ( m2 - 1 )

      x[i,j] = blend_112 ( r, s, x[0,0], x[0,m2-1], x[m1-1,0], x[m1-1,m2-1], \
        x[i,0], x[i,m2-1], x[0,j], x[m1-1,j] )

  return x

def blend_ij_1d1_test ( ):

#*****************************************************************************80
#
## blend_ij_1d1_test() tests blend_ij_1d1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  m1 = 5
  m2 = 4

  print ( '' )
  print ( 'blend_ij_1d1_test():' )
  print ( '  blend_ij_1d1() interpolates data in a table,' )
  print ( '  from edge data.' )

  x = np.zeros ( [ m1, m2 ] )
#
#  Load data in the edges.
#
  for i in [ 0, m1 - 1 ]:
    for j in range ( 0, m2 - 1 ):
      r = i / ( m1 - 1 )
      s = j / ( m2 - 1 )
      x[i,j] = cubic_rs ( r, s, 1 )

  for j in [ 0, m2 - 1 ]:
    for i in range ( 0, m1 - 1 ):
      r = i / ( m1 - 1 )
      s = j / ( m2 - 1 )
      x[i,j] = cubic_rs ( r, s, 1 )

  print ( '' )
  print ( '  Data:' )
  pprint.pprint ( x )

  x = blend_ij_1d1 ( x, m1, m2 )

  print ( '' )
  print ( '  Blended data:' )
  pprint.pprint ( x )

  return

def blend_ij_w_1d1 ( x, r, s, m1, m2 ):

#*****************************************************************************80
#
## blend_ij_w_1d1() extends weighted indexed scalar data along edges into a table.
#
#  Diagram:
#
#    Instead of assuming that the data in the table is equally spaced,
#    the arrays R and S are supplied, which should behave as
#    "coordinates" for the data.
#
#            S(1)  S(2)  S(3)  S(4)  S(5)  S(6)  S(M2)
#
#    R(1)  ( X11,  X12,  X13,  X14,  X15,  X16,  X1M2  )
#    R(2)  ( X21,  ...,  ...,  ...,  ...,  ...,  X2M2  )
#    R(3)  ( X31,  ...,  ...,  ...,  ...,  ...,  X3M2  )
#    R(4)  ( X41,  ...,  ...,  ...,  ...,  ...,  X4M2  )
#    R(M1) ( XM11, XM12, XM13, XM14, XM15, XM16, XM1M2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real X(M1,M2).
#    On data is contained in the "edge entries" X(1,J), X(I,1),
#    X(M1,J) and X(I,M2), for I = 1 to M1, and J = 1 to M2.
#
#    real R(M1), S(M2), are "coordinates" for the rows and
#    columns of the array.  The values in R, and the values in S, should
#    be strictly increasing or decreasing.
#
#    integer M1, M2, the number of rows and columns in X.
#
#  Output:
#
#    real X(M1,M2), all entries in X have been assigned a value.
#

#
#  Interpolate values in the interior.
#
  for i in range ( 1, m1 - 1 ):

    rr = ( r[i] - r[0] ) / ( r[m1-1] - r[0] )

    for j in range ( 1, m2 - 1 ):

      ss = ( s[j] - s[0] ) / ( s[m2-1] - s[0] )

      x[i,j] = blend_112 ( rr, ss, x[0,0], x[0,m2-1], x[m1-1,0], x[m1-1,m2-1], \
        x[i,0], x[i,m2-1], x[0,j], x[m1-1,j] )

  return x

def blend_ij_w_1d1_test ( ):

#*****************************************************************************80
#
## blend_ij_w_1d1_test() tests blend_ij_w_1d1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_ij_w_1d1_test():' )
  print ( '  blend_ij_w_1d1() uses blending to fill in the' )
  print ( '  interior of a table.' )

  n1 = 5
  n2 = 5

  rad = 3.0

  r = np.zeros ( n1 )
  s = np.zeros ( n2 )
  x = np.zeros ( [ n1, n2 ] )
  y = np.zeros ( [ n1, n2 ] )
#
#  Set the boundary values.
#
#  It turns out that our values correspond to the X and Y
#  coordinates of a quarter circle of radius 3, although
#  it is by no means necessary that a formula for the data
#  be known.
#
  for i in range ( 0, n1 ):
    rr = ( i / ( n1 - 1 ) )**2
    r[i] = rr
    x[i,n2-1] = rad * np.cos ( 0.5 * np.pi * ( 1.0 - rr ) )
    y[i,n2-1] = rad * np.sin ( 0.5 * np.pi * ( 1.0 - rr ) )

  for j in range ( 0, n2 ):
    ss = ( j / ( n2 - 1 ) )**2
    s[j] = ss
    y[0,j] = rad * ss
    x[n1-1,j] = rad * ss

  print ( '' )
  print ( '  X data:' )
  pprint.pprint ( x )

  print ( '' )
  print ( '  Y data:' )
  pprint.pprint ( y )

  x = blend_ij_w_1d1 ( x, r, s, n1, n2 )
  y = blend_ij_w_1d1 ( y, r, s, n1, n2 )

  print ( '' )
  print ( '  Blended X data:' )
  pprint.pprint ( x )

  print ( '' )
  print ( '  Blended Y data:' )
  pprint.pprint ( y )

  return

def blend_ijk_0d1 ( x, m1, m2, m3 ):

#*****************************************************************************80
#
## blend_ijk_0d1() extends indexed scalar corner data into a cubic table.
#
#  Diagram:
#
#    ( X111,   ...,  ...,  ...,  ...,  ...,  X1M21   )
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...     )
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...     )   First "layer"
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...     )
#    ( XM111,  ...,  ...,  ...,  ...,  ...,  XM1M21  )
#
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...     )
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...    )
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...     )   Middle "layers"
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...     )
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...     )
#
#    ( X11M3,  ...,  ...,  ...,  ...,  ...,  X1M2M3  )
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...     )
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...     )   Last "layer"
#    ( ....,   ...,  ...,  ...,  ...,  ...,  ...     )
#    ( XM11M3, ...,  ...,  ...,  ...,  ...,  XM1M2M3 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real x[M1,M2,M3).
#    On x[1,1,1), x[1,M2,1), x[M1,1,1), x[M1,M2,1), x[1,1,M3),
#    x[1,M2,M3), x[M1,1,M3) and x[M1,M2,M3) contain scalar values
#    which are to be interpolated throughout the table, using the table
#    indices I and J as independent variables.
#
#    integer M1, M2, M3, the number of rows, columns, and layers
#    in X.
#
#  Output:
#
#    real x[M1,M2,M3), all entries in X have been assigned a value.
#

#
#  Interpolate values along the "edges", that is, index triplets (i,j,k)
#  with exactly two of I, J, K an "extreme" value.
#
  for i in range ( 1, m1 - 1 ):

    r = i / ( m1 - 1 )

    x[ i, 0, 0] = blend_101 ( r, x[ 0, 0, 0], x[m1-1, 0, 0] )
    x[ i,m2-1, 0] = blend_101 ( r, x[ 0,m2-1, 0], x[m1-1,m2-1, 0] )
    x[ i, 0,m3-1] = blend_101 ( r, x[ 0, 0,m3-1], x[m1-1, 0,m3-1] )
    x[ i,m2-1,m3-1] = blend_101 ( r, x[ 0,m2-1,m3-1], x[m1-1,m2-1,m3-1] )

  for j in range ( 1, m2 - 1 ):

    s = j / ( m2 - 1 )

    x[ 0, j, 0] = blend_101 ( s, x[ 0, 0, 0], x[ 0,m2-1, 0] )
    x[m1-1, j, 0] = blend_101 ( s, x[m1-1, 0, 0], x[m1-1,m2-1, 0] )
    x[ 0, j,m3-1] = blend_101 ( s, x[ 0, 0,m3-1], x[ 0,m2-1,m3-1] )
    x[m1-1, j,m3-1] = blend_101 ( s, x[m1-1, 0,m3-1], x[m1-1,m2-1,m3-1] )

  for k in range ( 1, m3 - 1 ):

    t = k / ( m3 - 1 )

    x[ 0, 0,k] = blend_101 ( t, x[ 0, 0,0], x[ 0, 0,m3-1] )
    x[m1-1, 0,k] = blend_101 ( t, x[m1-1, 0,0], x[m1-1, 0,m3-1] )
    x[ 0,m2-1,k] = blend_101 ( t, x[ 0,m2-1,0], x[ 0,m2-1,m3-1] )
    x[m1-1,m2-1,k] = blend_101 ( t, x[m1-1,m2-1,0], x[m1-1,m2-1,m3-1] )
#
#  Interpolate values along the "faces", that is, index triplets (i,j,k)
#  with exactly one of I, J, K is an "extreme" value.
#
  for j in range ( 1, m2 - 1 ):

    s = j / ( m2 - 1 )

    for k in range ( 1, m3 - 1 ):

      t = k / ( m3 - 1 )

      x[0,j,k] = blend_112 ( s, t, x[0,0,0], x[0,0,m3-1], x[0,m2-1,0], x[0,m2-1,m3-1], \
        x[0,j,0], x[0,j,m3-1], x[0,0,k], x[0,m2-1,k] )

      x[m1-1,j,k] = blend_112 ( s, t, x[m1-1,0,0], x[m1-1,0,m3-1], x[m1-1,m2-1,0], \
        x[m1-1,m2-1,m3-1], x[m1-1,j,0], x[m1-1,j,m3-1], x[m1-1,0,k], x[m1-1,m2-1,k] )

  for i in range ( 1, m1 - 1 ):

    r = i / ( m1 - 1 )

    for k in range ( 1, m3 - 1 ):

      t = k / ( m3 - 1 )

      x[i,0,k] = blend_112 ( r, t, x[0,0,0], x[0,0,m3-1], x[m1-1,0,0], \
        x[m1-1,0,m3-1], x[i,0,0], x[i,0,m3-1], x[0,0,k], x[m1-1,0,k] )

      x[i,m2-1,k] = blend_112 ( r, t, x[0,m2-1,0], x[0,m2-1,m3-1], x[m1-1,m2-1,0], \
        x[m1-1,m2-1,m3-1], x[i,m2-1,0], x[i,m2-1,m3-1], x[0,m2-1,k], x[m1-1,m2-1,k] )

  for i in range ( 1, m1 - 1 ):

    r = i / ( m1 - 1 )

    for j in range ( 1, m2 - 1 ):

      s = j / ( m2 - 1 )

      x[i,j,0] = blend_112 ( r, s, x[0,0,0], x[1,m2-1,0], x[m1-1,0,0], \
        x[m1-1,m2-1,0], x[i,0,0], x[i,m2-1,0], x[0,j,0], x[m1-1,j,0] )

      x[i,j,m3-1] = blend_112 ( r, s, x[0,0,m3-1], x[0,m2-1,m3-1], x[m1-1,0,m3-1], \
        x[m1-1,m2-1,m3-1], x[0,1,m3-1], x[i,m2-1,m3-1], x[0,j,m3-1], x[m1-1,j,m3-1] )
#
#  Interpolate values in the interior.
#
  for i in range ( 1, m1 - 1 ):

    r = i  / ( m1 - 1 )

    for j in range ( 1, m2 - 1 ):

      s = j / ( m2 - 1 )

      for k in range ( 1, m3 - 1 ):

        t = k / ( m3 - 1 )

        x[i,j,k] = blend_123 ( r, s, t, \
          x[ 0,0,0], x[ 0, 0,m3-1], x[ 0,m2-1,0], x[ 0,m2-1,m3-1], \
          x[m1-1,0,0], x[m1-1, 0,m3-1], x[m1-1,m2-1,0], x[m1-1,m2-1,m3-1], \
          x[ i,0,0], x[ i, 0,m3-1], x[ i,m2-1,0], x[ i,m2-1,m3-1], \
          x[ 0,j,0], x[ 0, j,m3-1], x[m1-1, j,0], x[m1-1, j,m3-1], \
          x[ 0,0,k], x[ 0,m2-1, k], x[m1-1, 0,k], x[m1-1,m2-1, k], \
          x[ 0,j,k], x[m1-1, j, k], x[ i, 0,k], x[ i,m2-1, k], \
          x[ i,j,0], x[ i, j,m3-1] )

  return x

def blend_ijk_0d1_test ( ):

#*****************************************************************************80
#
## blend_ijk_0d1_test() tests blend_ijk_0d1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_ijk_0d1_test():' )
  print ( '  blend_ijk_0d1() interpolates data in a table,' )
  print ( '  from corner data.' )

  m1 = 4
  m2 = 3
  m3 = 3

  x = np.zeros ( [ m1, m2, m3 ] )
#
#  Load data on the faces.
#
  for i in range ( 1, m1 ):
    r = i / ( m1 - 1 )
    for j in range ( 1, m2 ):
      s = j / ( m2 - 1 )
      for k in range ( 1, m3 ):
        t = k / ( m3 - 1 )
#
#  Count extreme indices.
#
        num_extreme = 0
        if ( i == 0 or i == m1 - 1 ):
          num_extreme = num_extreme + 1
        if ( j == 0 or j == m2 - 1 ):
          num_extreme = num_extreme + 1
        if ( k == 0 or k == m3 - 1 ):
          num_extreme = num_extreme + 1

        if ( num_extreme == 3 ):
          x[i,j,k] = quad_rst ( r, s, t, 1 )

  print ( '' )
  print ( '  Data:' )
  pprint.pprint ( x )

  x = blend_ijk_0d1 ( x, m1, m2, m3 )

  print ( '' )
  print ( '  Blended data:' )
  pprint.pprint ( x )

  return

def blend_ijk_1d1 ( x, m1, m2, m3 ):

#*****************************************************************************80
#
## blend_ijk_1d1() extends indexed scalar edge data into a cubic table.
#
#  Diagram:
#
#    [ X111,   X121,   X131,   X141,   X151,   X1M21   ]
#    [ X211,   ...,    ...,    ...,    ...,    X2M21   ]
#    [ X311,   ...,    ...,    ...,    ...,    X3M21   ]   Layer 1
#    [ X411,   ...,    ...,    ...,    ...,    X4M21   ]
#    [ XM111,  XM121,  XM131,  XM141,  XM151,  XM1M21  ]
#
#    [ X11K,   ...,    ...,    ...,    ...,    X1M2K   ]
#    [ ....,   ...,    ...,    ...,    ...,    ...     ]
#    [ ....,   ...,    ...,    ...,    ...,    ...     ]   Layer K
#    [ ....,   ...,    ...,    ...,    ...,    ...     ]   1 < K < M3
#    [ XM11K,  ...,    ...,    ...,    ...,    XM1M2K  ]
#
#    [ X11M3,  X12M3,  X13M3,  X14M3,  X15M3,  X1M2M3  ]
#    [ X21M3,  ...,    ...,    ...,    ...,    X2M2M3  ]
#    [ X31M3,  ...,    ...,    ...,    ...,    X3M2M3  ]   Layer M3
#    [ X41M3   ...,    ...,    ...,    ...,    X4M2M3  ]
#    [ XM11M3, XM12M3, XM13M3, XM14M3, XM15M3, XM1M2M3 ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 0, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 0, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real X[M1,M2,M3]: there is already scalar data in the entries X[I,J,K]
#    corresponding to "edges" of the table, that is, entries for which
#    at least two of the three indices I, J and K are equal to their
#    minimum or maximum possible values.
#
#    integer M1, M2, M3, the number of rows, columns, and layers
#    in X.
#
#  Output:
#
#    real X[M1,M2,M3], all entries in X have been assigned a value,
#    using the table indices as independent variables.
#

#
#  Interpolate values along the "faces", that is, index triplets [i,j,k]
#  where exactly one of I, J, K is an "extreme" value.
#
  for j in range ( 0, m2 - 1 ):

    s = j / ( m2 - 1 )

    for k in range ( 0, m3 - 1 ):

      t =  k - 1 / ( m3 - 1 )

      x[0,j,k] = blend_112 ( s, t, x[0,0,0], x[0,0,m3-1], x[0,m2-1,0], \
        x[0,m2-1,m3-1], x[0,j,0], x[0,j,m3-1], x[0,0,k], x[0,m2-1,k] )

      x[m1-1,j,k] = blend_112 ( s, t, x[m1-1,0,0], x[m1-1,0,m3-1], x[m1-1,m2-1,0], \
        x[m1-1,m2-1,m3-1], x[m1-1,j,0], x[m1-1,j,m3-1], x[m1-1,0,k], x[m1-1,m2-1,k] )

  for i in range ( 0, m1 - 1 ):

    r = i / ( m1 - 1 )

    for k in range ( 0, m3 - 1 ):

      t = k / ( m3 - 1 )

      x[i,0,k] = blend_112 ( r, t, x[0,0,0], x[0,0,m3-1], x[m1-1,0,0], \
        x[m1-1,0,m3-1], x[i,0,0], x[i,0,m3-1], x[0,0,k], x[m1-1,0,k] )

      x[i,m2-1,k] = blend_112 ( r, t, x[0,m2-1,0], x[0,m2-1,m3-1], x[m1-1,m2-1,0], \
        x[m1-1,m2-1,m3-1], x[i,m2-1,0], x[i,m2-1,m3-1], x[0,m2-1,k], x[m1-1,m2-1,k] )

  for i in range ( 0, m1 - 1 ):

    r = i / ( m1 - 1 )

    for j in range ( 0, m2 - 1 ):

      s = j / ( m2 - 1 )

      x[i,j,0] = blend_112 ( r, s, x[0,0,0], x[0,m2-1,0], x[m1-1,0,0], \
        x[m1-1,m2-1,0], x[i,0,0], x[i,m2-1,0], x[0,j,0], x[m1-1,j,0] )

      x[i,j,m3-1] = blend_112 ( r, s, x[0,0,m3-1], x[0,m2-1,m3-1], x[m1-1,0,m3-1], \
        x[m1-1,m2-1,m3-1], x[i,0,m3-1], x[i,m2-1,m3-1], x[0,j,m3-1], x[m1-1,j,m3-1] )
#
#  Interpolate values in the interior.
#
  for i in range ( 0, m1 - 1 ):

    r = i / ( m1 - 1 )

    for j in range ( 0, m2 - 1 ):

      s = j / ( m2 - 1 )

      for k in range ( 0, m3 - 1 ):

        t = k / ( m3 - 1 )

        x[i,j,k] = blend_123 ( r, s, t, \
          x[ 0,0,0], x[ 0, 0,m3-1], x[ 0,m2-1,0], x[ 0,m2-1,m3-1], \
          x[m1-1,0,0], x[m1-1, 0,m3-1], x[m1-1,m2-1,0], x[m1-1,m2-1,m3-1], \
          x[ i,0,0], x[ i, 0,m3-1], x[ i,m2-1,0], x[ i,m2-1,m3-1], \
          x[ 0,j,0], x[ 0, j,m3-1], x[m1-1, j,0], x[m1-1, j,m3-1], \
          x[ 0,0,k], x[ 0,m2-1, k], x[m1-1, 0,k], x[m1-1,m2-1, k], \
          x[ 0,j,k], x[m1-1, j, k], x[ i, 0,k], x[ i,m2-1, k], \
          x[ i,j,0], x[ i, j,m3-1] )

  return x

def blend_ijk_1d1_test ( ):

#*****************************************************************************80
#
## blend_ijk_1d1_test() tests blend_ijk_1d1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_ijk_1d1_test():' )
  print ( '  blend_ijk_1d1() interpolates data in a table,' )
  print ( '  from edge data.' )

  m1 = 4
  m2 = 3
  m3 = 3

  x = np.zeros ( [ m1, m2, m3 ] )
#
#  Load data on the faces.
#
  for i in range ( 0, m1 ):
    r = i / ( m1 - 1 )
    for j in range ( 0, m2 ):
      s = j / ( m2 - 1 )
      for k in range ( 0, m3 ):
        t = k / ( m3 - 1 )

        num_extreme = 0
        if ( i == 0 or i == m1 - 1 ):
          num_extreme = num_extreme + 1
        if ( j == 0 or j == m2 - 1 ):
          num_extreme = num_extreme + 1
        if ( k == 0 or k == m3 - 1 ):
          num_extreme = num_extreme + 1

        if ( 2 <= num_extreme ):
          x[i,j,k] = quad_rst ( r, s, t, 1 )

  print ( '' )
  print ( '  Data:' )
  pprint.pprint ( x )

  x = blend_ijk_1d1 ( x, m1, m2, m3 )

  print ( '' )
  print ( '  Blended data:' )
  pprint.pprint ( x )

  return

def blend_ijk_2d1 ( x, m1, m2, m3 ):

#*****************************************************************************80
#
## blend_ijk_2d1() extends indexed scalar face data into a cubic table.
#
#  Diagram:
#
#    ( X111    X121    X131    X141    X151    X1M21   )
#    ( X211    X221    X231    X241    X251    X2M21   )
#    ( X311    X321    X331    X341    X351    X3M21   )   Layer 1
#    ( X411    X421    X431    X441    X451    X4M21   )
#    ( XM111   XM121   XM131   XM141   XM151   XM1M21  )
#
#    ( X11K    X12K    X13K    X14K    X15K    X1M2K   )
#    ( X21K    ...     ....    ....    ....    X2M2K   )
#    ( X31K    ...     ....    ....    ....    X3M2K   )   Layer K
#    ( X41K    ...     ....    ....    ....    X4M2K   )   1 < K < M3
#    ( XM11K   XM12K   XM13K   XM14K   XM15K   XM1M2K  )
#
#    ( X11M3   X12M3   X13M3   X14M3   X15M3   X1M2M3  )
#    ( X21M3   X22M3   X23M3   X24M3   X25M3   X2M2M3  )
#    ( X31M3   X32M3   X33M3   X34M3   X35M3   X3M2M3  )   Layer M3
#    ( X41M3   X42M3   X43M3   X44M3   X45M3   X4M2M3  )
#    ( XM11M3  XM12M3  XM13M3  XM14M3  XM15M3  XM1M2M3 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real x[M1,M2,M3).
#    On there is already scalar data in the entries x[I,J,K)
#    corresponding to "faces" of the table, that is, entries for which
#    at least one of the three indices I, J and K is equal to their
#    minimum or maximum possible values.
#
#    integer M1, M2, M3, the number of rows, columns, and
#    layers in X.
#
#  Output:
#
#    real x[M1,M2,M3), all entries in X have been assigned a value,
#    using the table indices as independent variables.
#

#
#  Interpolate values in the interior.
#
  for i in range ( 1, m1 - 1 ):

    r = i / ( m1 - 1 )

    for j in range ( 1, m2 - 1 ):

      s = j / ( m2 - 1 )

      for k in range ( 1, m3 - 1 ):

        t = k / ( m3 - 1 )

        x[i,j,k] = blend_123 ( r, s, t, \
          x[ 0,0,0], x[ 0, 0,m3-1], x[ 0,m2-1,0], x[ 0,m2-1,m3-1], \
          x[m1-1,0,0], x[m1-1, 0,m3-1], x[m1-1,m2-1,0], x[m1-1,m2-1,m3-1], \
          x[ i,0,0], x[ i, 0,m3-1], x[ i,m2-1,0], x[ i,m2-1,m3-1], \
          x[ 0,j,0], x[ 0, j,m3-1], x[m1-1, j,0], x[m1-1, j,m3-1], \
          x[ 0,0,k], x[ 0,m2-1, k], x[m1-1, 0,k], x[m1-1,m2-1, k], \
          x[ 0,j,k], x[m1-1, j, k], x[ i, 0,k], x[ i,m2-1, k], \
          x[ i,j,0], x[ i, j,m3-1] )

  return x

def blend_ijk_2d1_test ( ):

#*****************************************************************************80
#
## blend_ijk_2d1_test() tests blend_ijk_2d1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_ijk_2d1_test():' )
  print ( '  blend_ijk_2d1() interpolates data in a table,' )
  print ( '  from face data.' )

  m1 = 4
  m2 = 3
  m3 = 3

  x = np.zeros ( [ m1, m2, m3 ] )
#
#  Load data on the faces.
#
  for i in range ( 0, m1 ):
    r = i / ( m1 - 1 )
    for j in range ( 0, m2 ):
      s = j / ( m2 - 1 )
      for k in range ( 0, m3 ):
        t = k / ( m3 - 1 )

        num_extreme = 0
        if ( i == 1 or i == m1 ):
          num_extreme = num_extreme + 1
        if ( j == 1 or j == m2 ):
          num_extreme = num_extreme + 1
        if ( k == 1 or k == m3 ):
          num_extreme = num_extreme + 1

        if ( 1 <= num_extreme ):
          x[i,j,k] = quad_rst ( r, s, t, 1 )

  print ( '' )
  print ( '  Data:' )
  pprint.pprint ( x )

  x = blend_ijk_2d1 ( x, m1, m2, m3 )

  print ( '' )
  print ( '  Blended data:' )
  pprint.pprint ( x )

  return

def blend_r_0dn ( r, n, bound_r ):

#*****************************************************************************80
#
## blend_r_0dn() extends vector data at endpoints into a line.
#
#  Diagram:
#
#    0-----r-----1
#
#  Discussion:
#
#    This is simply linear interpolation.  BLEND_R_0DN is provided
#    mainly as a "base routine" which can be compared to its
#    generalizations, such as BLEND_RS_0DN.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, the (R) coordinate of the point to
#    be evaluated.
#
#    integer N, the dimension of the vector space.
#
#    function BOUND_R, is a function which is given (R) coordinates
#    and an component value I, and returns XI, the value of the I-th
#    component of the N-vector at that point.  BOUND_R will only be
#    called for "corners", that is, for values (R) where R is either
#    0.0 or 1.0.  BOUND_R has the form:
#      function xi = bound_r ( r, i )
#
#  Output:
#
#    real X(N), the interpolated value at the point (R).
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
#
#  Get the I-th coordinate component at the two corners.
#
    x0 = bound_r ( 0.0, i + 1 )
    x1 = bound_r ( 1.0, i + 1 )
#
#  Interpolate the I-th coordinate component of the interior point.
#
    x[i] = blend_101 ( r, x0, x1 )

  return x

def blend_r_0dn_test ( ):

#*****************************************************************************80
#
## blend_r_0dn_test() tests blend_r_0dn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_r_0dn_test():' )
  print ( '  blend_r_0dn() interpolates endpoint vector data' )
  print ( '  into a list.' )

  m = 11
  n = 2
  x = np.zeros ( [ m, n ] )

  for j in [ 0, n - 1 ]:
    for i in [ 0, m - 1 ]:
      r = i / ( m - 1 )
      x[i,j] = powers_r ( r, i )

  print ( '' )
  print ( '  Data:' )
  pprint.pprint ( x )

  for i in range ( 0, m ):
    r = i / ( m - 1 )
    x[i,:] = blend_r_0dn ( r, n, powers_r )

  print ( '' )
  print ( '  Blended data:' )
  pprint.pprint ( x )

  return

def blend_r_0dn_identity_test ( ):

#*****************************************************************************80
#
## blend_r_0dn_identity_test() checks for a gross error in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2026
#
#  Author:
#
#    John Burkardt
#
  nmax = 3

  print ( '' )
  print ( 'blend_r_0dn_identity_test():' )
  print ( '  Simple identity test on blend_r_0dn() to detect gross errors.' )
#
#  Set N to 1.
#
  n = 1
#
#  Test blend_r_0dn() on identity.
#
  print ( '' )
  print ( 'Identity test for blend_r_0dn():' )
  print ( '' )

  for r in [ 0.0, 1.0, 0.5 ]:
    x = blend_r_0dn ( r, n, identity_r )
    print ( '  %8f  %8f' % ( r, x[0] ) )

  return

def blend_r_0dn_stretch_test ( ):

#*****************************************************************************80
#
## blend_r_0dn_stretch_test() checks for simple errors in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2026
#
#  Author:
#
#    John Burkardt
#
  nmax = 3

  print ( '' )
  print ( 'blend_r_0dn_stretch_test():' )
  print ( '  Shift and stretch test for blend_r_0dn() to detect simple errors.' )
#
#  Set N to 1.
#
  n = 1
#
#  Test blend_r_0dn() on shift by 1, stretch by 2.
#
  print ( '' )
  print ( 'Shift and stretch test for blend_r_0dn():' )
  print ( '' )

  for r in [ 0.0, 1.0, 0.5 ]:
    x = blend_r_0dn ( r, n, stretch_r )
    print ( '  %8f  %8f' % ( r, x[0] ) )

  return

def blend_rs_0dn ( r, s, n, bound_rs ):

#*****************************************************************************80
#
## blend_rs_0dn() extends vector data at corners into a square.
#
#  Diagram:
#
#    01-----r1-----11
#     |      .      |
#     |      .      |
#    0s.....rs.....1s
#     |      .      |
#     |      .      |
#    00-----r0-----10
#
#  Discussion:
#
#    BLEND_RS_0DN should be equivalent to the use of a bilinear finite
#    element method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, S, the (R,S) coordinates of the point to be evaluated.
#
#    integer N, the dimension of the vector space.
#
#    function BOUND_RS, is a function which is given (R,S)
#    coordinates and an component value I, and returns XI, the value
#    of the I-th component of the N-vector at that point.  BOUND_RS
#    will only be called for "corners", that is, for values (R,S) where
#    R and S are either 0.0 or 1.0.  BOUND_RS has the form:
#      function xi = bound_rs ( r, s, i, xi )
#
#  Output:
#
#    real X(N), the interpolated value at the point (R,S).
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
#
#  Get the I-th coordinate component at the four corners.
#
    x00 = bound_rs ( 0.0, 0.0, i + 1 )
    x01 = bound_rs ( 0.0, 1.0, i + 1 )
    x10 = bound_rs ( 1.0, 0.0, i + 1 )
    x11 = bound_rs ( 1.0, 1.0, i + 1 )
#
#  Interpolate the I-th coordinate component at the sides.
#
    xr0 = blend_101 ( r, x00, x10 )
    xr1 = blend_101 ( r, x01, x11 )
    x0s = blend_101 ( s, x00, x01 )
    x1s = blend_101 ( s, x10, x11 )
#
#  Interpolate the I-th coordinate component of the interior point.
#
    x[i] = blend_112 ( r, s, x00, x01, x10, x11, xr0, xr1, x0s, x1s )

  return x

def blend_rs_0dn_test ( ):

#*****************************************************************************80
#
## blend_rs_0dn_test() tests blend_rs_0dn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'blend_rs_0dn_test():' )
  print ( '  blend_rs_0dn() interpolates data in a table,' )
  print ( '  from corner data.' )

  m1 = 5
  m2 = 4
  n = 1

  x = np.zeros ( [ m1, m2, n ] )

  for i in [ 0, m1 - 1 ]:
    r = i / ( m1 - 1 )
    for j in [ 0, m2 - 1]:
      s = j / ( m2 - 1 )
      x[i,j,0] = cubic_rs ( r, s, 1 )

  print ( '' )
  print ( '  Data:' )
  pprint.pprint ( x )

  for i in range ( 0, m1 ):
    r = i / ( m1 - 1 )
    for j in range ( 0, m2 ):
      s = j / ( m2 - 1 )
      x[i,j,0:n] = blend_rs_0dn ( r, s, 1, cubic_rs )

  print ( '' )
  print ( '  Blended data:' )
  pprint.pprint ( x )

  return

def blend_rs_0dn_identity_test ( ):

#*****************************************************************************80
#
## blend_rs_0dn_identity_test() checks for a gross error in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'blend_rs_0dn_identity_test():' )
  print ( '  Simple identity test to detect gross errors.' )
#
#  Set N to 2.
#
  n = 2
#
#  Test blend_rs_0dn() on identity.
#
  print ( '' )
  print ( 'Identity test for blend_rs_0dn():' )
  print ( '' )

  for r in [ 0.0, 0.5, 1.0 ]:
    for s in [ 0.0, 0.5, 1.0 ]:
      x = blend_rs_0dn ( r, s, n, identity_rs )
      print ( '  %8f  %8f  %8f  %8f' % ( r, s, x[0], x[1] ) )

  return

def blend_rs_0dn_stretch_test ( ):

#*****************************************************************************80
#
## blend_rs_0dn_stretch_test(): checks for simple errors in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2026
#
#  Author:
#
#    John Burkardt
#

#
#  Set N to 2.
#
  n = 2
#
#  Test blend_rs_0dn() on shift by (1,2), stretch by (3,4).
#
  print ( '' )
  print ( 'blend_rs_0dn_stretch_test():' )
  print ( 'Shift and stretch test for blend_rs_0dn():' )
  print ( '' )
  for r in [ 0.0, 0.5, 1.0 ]:
    for s in [ 0.0, 0.5, 1.0 ]:
      x = blend_rs_0dn ( r, s, n, stretch_rs )
      print ( '  %8f  %8f  %8f  %8f' % ( r, s, x[0], x[1] ) )

  return

def blend_rs_1dn ( r, s, n, bound_rs ):

#*****************************************************************************80
#
## blend_rs_1dn() extends vector data along sides into a square.
#
#  Diagram:
#
#    01-----r1-----11
#     |      .      |
#     |      .      |
#    0s.....rs.....1s
#     |      .      |
#     |      .      |
#    00-----r0-----10
#
#  Discussion:
#
#    BLEND_RS_1DN is NOT equivalent to a bilinear finite element method,
#    since the data is sampled everywhere along the boundary lines,
#    rather than at a finite number of nodes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, S, the (R,S) coordinates of the point to be
#    evaluated.
#
#    integer N, the dimension of the vector space.
#
#    function BOUND_RS, is a function which is given (R,S)
#    coordinates and an component value I, and returns XI, the value
#    of the I-th component of the N-vector at that point.  BOUND_RS
#    will only be called for "sides", that is, for values (R,S) where
#    at least one of R and S is either 0.0 or 1.0.  BOUND_RS has the
#    form:
#      function xi = bound_rs ( r, s, i )
#
#  Output:
#
#    real X(N), the interpolated value at the point (R,S).
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
#
#  Get the I-th coordinate component at the four corners.
#
    x00 = bound_rs ( 0.0, 0.0, i + 1 )
    x01 = bound_rs ( 0.0, 1.0, i + 1 )
    x10 = bound_rs ( 1.0, 0.0, i + 1 )
    x11 = bound_rs ( 1.0, 1.0, i + 1 )
#
#  Get the I-th coordinate component at the sides.
#
    xr0 = bound_rs ( r, 0.0, i + 1 )
    xr1 = bound_rs ( r, 1.0, i + 1 )
    x0s = bound_rs ( 0.0, s, i + 1 )
    x1s = bound_rs ( 1.0, s, i + 1 )
#
#  Interpolate the I-th coordinate component of the interior point.
#
    x[i] = blend_112 ( r, s, x00, x01, x10, x11, xr0, xr1, x0s, x1s )

  return x

def blend_rs_1dn_test ( ):

#*****************************************************************************80
#
## blend_rs_1dn_test() tests blend_rs_1dn().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  m1 = 5
  m2 = 4
  n = 1

  print ( '' )
  print ( 'blend_rs_1dn_test()' )
  print ( '  blend_rs_1dn() interpolates data in a table,' )
  print ( '  from edge data.' )

  x = np.zeros ( [ m1, m2, n ] )

  for i in range ( 0, m1 ):
    for j in [ 0, m2 - 1 ]:
      r = i / ( m1 - 1 )
      s = j / ( m2 - 1 )
      x[i,j,0] = cubic_rs ( r, s, 1 )

  for j in range ( 0, m2 ):
    for i in [ 0, m1 - 1 ]:
      r = i / ( m1 - 1 )
      s = j / ( m2 - 1 )
      x[i,j,0] = cubic_rs ( r, s, 1 )

  print ( '' )
  print ( '  Data:' )
  pprint.pprint ( x )

  for i in range ( 0, m1 ):
    r = i / ( m1 - 1 )
    for j in range ( 0, m2 ):
      s = j / ( m2 - 1 )
      x[i,j,0:n] = blend_rs_1dn ( r, s, 1, cubic_rs )

  print ( '' )
  print ( '  Blended data:' )
  pprint.pprint ( x )

  return

def blend_rs_1dn_identity_test ( ):

#*****************************************************************************80
#
## blend_rs_1dn_identity_test() checks for a gross error in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'blend_rs_1dn_identity_test():' )
  print ( '  Simple identity test on blend_rs_1dn() to detect gross errors.' )
#
#  Set N to 2.
#
  n = 2
#
#  Test blend_rs_1dn() on identity.
#
  print ( '' )
  for r in [ 0.0, 0.5, 1.0 ]:
    for s in [ 0.0, 0.5, 1.0 ]:
      x = blend_rs_1dn ( r, s, n, identity_rs )
      print ( '  %8f  %8f  %8f  %8f' % ( r, s, x[0], x[1] ) )

  return

def blend_rs_1dn_stretch_test ( ):

#*****************************************************************************80
#
## blend_rs_1dn_stretch_test() checks for simple errors in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'blend_rs_1dn_stretch_test():' )
  print ( '  Shift and stretch test for blend_rs_1dn() to detect simple errors.' )
#
#  Set N to 2.
#
  n = 2
#
#  Shift by (1,2), stretch by (3,4).
#
  print ( '' )
  for r in [ 0.0, 0.5, 1.0 ]:
    for s in [ 0.0, 0.5, 1.0 ]:
      x = blend_rs_1dn ( r, s, n, stretch_rs )
      print ( '  %8f  %8f  %8f  %8f' % ( r, s, x[0], x[1] ) )

  return

def blend_rst_0dn ( r, s, t, n, bound_rst ):

#*****************************************************************************80
#
## blend_rst_0dn() extends vector data at corners into a cube.
#
#  Diagram:
#
#    010-----r10-----110        011-----r11-----111
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    0s0.....rs0.....1s0        0s1.....rs1.....1s1     S
#      |       .       |          |       .       |     |
#      |       .       |          |       .       |     |
#    000-----r00-----100        001-----r01-----101     +----R
#           BOTTOM                      TOP
#
#    011-----0s1-----001        111-----1s1-----101
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    01t.....0st.....00t        11t.....1st.....10t          T
#      |       .       |          |       .       |          |
#      |       .       |          |       .       |          |
#    010-----0s0-----000        110-----1s0-----100     S----+
#           LEFT                       RIGHT
#
#    001-----r01-----101        011-----r11-----111
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    00t.....r0t.....100        01t.....r1t.....11t     T
#      |       .       |          |       .       |     |
#      |       .       |          |       .       |     |
#    000-----r00-----100        010-----r10-----110     +----R
#           FRONT                       BACK
#
#  Discussion:
#
#    BLEND_RST_0DN is equivalent to a trilinear finite element method.
#    Data along the edges, faces, and interior of the cube is
#    interpolated from the data at the corners.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, S, T, the (R,S,T) coordinates of the
#    point to be evaluated.
#
#    integer N, the dimension of the vector space.
#
#    function BOUND_RST, is a function which is given (R,S,T)
#    coordinates and an component value I, and returns XI, the value
#    of the I-th component of the N-vector at that point.  BOUND_RST
#    will only be called for "corners", that is, for values (R,S,T)
#    where R, S and T are either 0.0 or 1.0.  BOUND_RST has the form:
#      function xi = bound_rst ( r, s, t, i )
#
#  Output:
#
#    real X(N), the interpolated value at the point (R,S,T).
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
#
#  Get the I-th coordinate component at the corners.
#
    x000 = bound_rst ( 0.0, 0.0, 0.0, i + 1 )
    x001 = bound_rst ( 0.0, 0.0, 1.0, i + 1 )
    x010 = bound_rst ( 0.0, 1.0, 0.0, i + 1 )
    x011 = bound_rst ( 0.0, 1.0, 1.0, i + 1 )
    x100 = bound_rst ( 1.0, 0.0, 0.0, i + 1 )
    x101 = bound_rst ( 1.0, 0.0, 1.0, i + 1 )
    x110 = bound_rst ( 1.0, 1.0, 0.0, i + 1 )
    x111 = bound_rst ( 1.0, 1.0, 1.0, i + 1 )
#
#  Interpolate the I-th coordinate component at the edges.
#
    xr00 = blend_101 ( r, x000, x100 )
    xr01 = blend_101 ( r, x001, x101 )
    xr10 = blend_101 ( r, x010, x110 )
    xr11 = blend_101 ( r, x011, x111 )

    x0s0 = blend_101 ( s, x000, x010 )
    x0s1 = blend_101 ( s, x001, x011 )
    x1s0 = blend_101 ( s, x100, x110 )
    x1s1 = blend_101 ( s, x101, x111 )

    x00t = blend_101 ( t, x000, x001 )
    x01t = blend_101 ( t, x010, x011 )
    x10t = blend_101 ( t, x100, x101 )
    x11t = blend_101 ( t, x110, x111 )
#
#  Interpolate the I-th component on the faces.
#
    x0st = blend_112 ( s, t, x000, x001, x010, x011, x0s0, x0s1, x00t, x01t )

    x1st = blend_112 ( s, t, x100, x101, x110, x111, x1s0, x1s1, x10t, x11t )

    xr0t = blend_112 ( r, t, x000, x001, x100, x101, xr00, xr01, x00t, x10t )

    xr1t = blend_112 ( r, t, x010, x011, x110, x111, xr10, xr11, x01t, x11t )

    xrs0 = blend_112 ( r, s, x000, x010, x100, x110, xr00, xr10, x0s0, x1s0 )

    xrs1 = blend_112 ( r, s, x001, x011, x101, x111, xr01, xr11, x0s1, x1s1 )
#
#  Interpolate the I-th coordinate component of the interior point.
#
    x[i] = blend_123 ( r, s, t, x000, x001, x010, x011, x100, x101, x110, x111, \
      xr00, xr01, xr10, xr11, x0s0, x0s1, x1s0, x1s1, x00t, x01t, x10t, x11t, \
      x0st, x1st, xr0t, xr1t, xrs0, xrs1 )

  return x

def blend_rst_0dn_identity_test ( ):

#*****************************************************************************80
#
## blend_rst_0dn_identity_test() checks for a gross error in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2026
#
#  Author:
#
#    John Burkardt
#
  nmax = 3

  print ( '' )
  print ( 'blend_rst_0dn_identity_test():' )
  print ( '  Simple identity test for blend_rst_0dn() to detect gross errors.' )
#
#  Set N to 3.
#
  n = 3

  print ( '' )
  for r in [ 0.0, 0.5, 1.0 ]:
    for s in [ 0.0, 0.5, 1.0 ]:
      for t in [ 0.0, 0.5, 1.0 ]:
        x = blend_rst_0dn ( r, s, t, n, identity_rst )
        print ( '  %8f  %8f  %8f  %8f  %8f  %8f' % ( r, s, t, x[0], x[1], x[2] ) )

  return

def blend_rst_0dn_stretch_test ( ):

#*****************************************************************************80
#
## blend_rst_0dn_stretch_test() checks for simple errors in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2008
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'blend_rst_0dn_stretch_test():' )
  print ( '  Shift and stretch test for blend_rst_0dn() to detect simple errors.' )
#
#  Set N to 3.
#
  n = 3
#
#  Shift by (1,2,3), stretch by (4,5,6).
#
  print ( '' )
  for r in [ 0.0, 0.5, 1.0 ]:
    for s in [ 0.0, 0.5, 1.0 ]:
      for t in [ 0.0, 0.5, 1.0 ]:
        x = blend_rst_0dn ( r, s, t, n, stretch_rst )
        print ( '  %8f  %8f  %8f  %8f  %8f  %8f' % ( r, s, t, x[0], x[1], x[2] ) )

  return

def blend_rst_1dn ( r, s, t, n, bound_rst ):

#*****************************************************************************80
#
## blend_rst_1dn() extends vector data on edges into a cube.
#
#  Diagram:
#
#    010-----r10-----110        011-----r11-----111
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    0s0.....rs0.....1s0        0s1.....rs1.....1s1     S
#      |       .       |          |       .       |     |
#      |       .       |          |       .       |     |
#    000-----r00-----100        001-----r01-----101     +----R
#           BOTTOM                      TOP
#
#    011-----0s1-----001        111-----1s1-----101
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    01t.....0st.....00t        11t.....1st.....10t          T
#      |       .       |          |       .       |          |
#      |       .       |          |       .       |          |
#    010-----0s0-----000        110-----1s0-----100     S----+
#           LEFT                       RIGHT
#
#    001-----r01-----101        011-----r11-----111
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    00t.....r0t.....100        01t.....r1t.....11t     T
#      |       .       |          |       .       |     |
#      |       .       |          |       .       |     |
#    000-----r00-----100        010-----r10-----110     +----R
#           FRONT                       BACK
#
#  Discussion:
#
#    BLEND_RST_1D is NOT equivalent to a trilinear finite element method,
#    since the data is sampled everywhere along the corners and edges,
#    rather than at a finite number of nodes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 October 2008
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, S, T, the (R,S,T) coordinates of the
#    point to be evaluated.
#
#    integer N, the dimension of the vector space.
#
#    function BOUND_RST, is a function which is given (R,S,T)
#    coordinates and an component value I, and returns XI, the value
#    of the I-th component of the N-vector at that point.  BOUND_RST
#    will only be called for "edges", that is, for values (R,S,T)
#    where at least two of R, S and T are either 0.0 or 1.0.
#    BOUND_RST has the form:
#      function xi = bound_rst ( r, s, t, i + 1 )
#
#  Output:
#
#    real X(N), the interpolated value at the
#    point (R,S,T).
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
#
#  Get the I-th coordinate component at the corners.
#
    x000 = bound_rst ( 0.0, 0.0, 0.0, i + 1 )
    x001 = bound_rst ( 0.0, 0.0, 1.0, i + 1 )
    x010 = bound_rst ( 0.0, 1.0, 0.0, i + 1 )
    x011 = bound_rst ( 0.0, 1.0, 1.0, i + 1 )
    x100 = bound_rst ( 1.0, 0.0, 0.0, i + 1 )
    x101 = bound_rst ( 1.0, 0.0, 1.0, i + 1 )
    x110 = bound_rst ( 1.0, 1.0, 0.0, i + 1 )
    x111 = bound_rst ( 1.0, 1.0, 1.0, i + 1 )
#
#  Get the I-th coordinate component at the edges.
#
    xr00 = bound_rst ( r, 0.0, 0.0, i + 1 )
    xr01 = bound_rst ( r, 0.0, 1.0, i + 1 )
    xr10 = bound_rst ( r, 1.0, 0.0, i + 1 )
    xr11 = bound_rst ( r, 1.0, 1.0, i + 1 )

    x0s0 = bound_rst ( 0.0, s, 0.0, i + 1 )
    x0s1 = bound_rst ( 0.0, s, 1.0, i + 1 )
    x1s0 = bound_rst ( 1.0, s, 0.0, i + 1 )
    x1s1 = bound_rst ( 1.0, s, 1.0, i + 1 )

    x00t = bound_rst ( 0.0, 0.0, t, i + 1 )
    x01t = bound_rst ( 0.0, 1.0, t, i + 1 )
    x10t = bound_rst ( 1.0, 0.0, t, i + 1 )
    x11t = bound_rst ( 1.0, 1.0, t, i + 1 )
#
#  Interpolate the I-th component on the faces.
#
    x0st = blend_112 ( s, t, x000, x001, x010, x011, x0s0, x0s1, x00t, x01t )

    x1st = blend_112 ( s, t, x100, x101, x110, x111, x1s0, x1s1, x10t, x11t )

    xr0t = blend_112 ( r, t, x000, x001, x100, x101, xr00, xr01, x00t, x10t )

    xr1t = blend_112 ( r, t, x010, x011, x110, x111, xr10, xr11, x01t, x11t )

    xrs0 = blend_112 ( r, s, x000, x010, x100, x110, xr00, xr10, x0s0, x1s0 )

    xrs1 = blend_112 ( r, s, x001, x011, x101, x111, xr01, xr11, x0s1, x1s1 )
#
#  Interpolate the I-th coordinate component of the interior point.
#
    x[i] = blend_123 ( r, s, t, x000, x001, x010, x011, x100, x101, x110, x111, \
      xr00, xr01, xr10, xr11, x0s0, x0s1, x1s0, x1s1, x00t, x01t, x10t, x11t, \
      x0st, x1st, xr0t, xr1t, xrs0, xrs1 )

  return x

def blend_rst_1dn_identity_test ( ):

#*****************************************************************************80
#
## blend_rst_1dn_identity_test() checks for a gross error in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2026
#
#  Author:
#
#    John Burkardt
#
  nmax = 3

  print ( '' )
  print ( 'blend_rst_1dn_identity_test():' )
  print ( '  Simple identity test for blend_rst_1dn() to detect gross errors.' )
#
#  Set N to 3.
#
  n = 3
#
#  Test on identity.
#
  print ( '' )
  for r in [ 0.0, 0.5, 1.0 ]:
    for s in [ 0.0, 0.5, 1.0 ]:
      for t in [ 0.0, 0.5, 1.0 ]:
        x = blend_rst_1dn ( r, s, t, n, identity_rst )
        print ( '  %8f  %8f  %8f  %8f  %8f  %8f' % ( r, s, t, x[0], x[1], x[2] ) )

  return

def blend_rst_1dn_stretch_test ( ):

#*****************************************************************************80
#
## blend_rst_1dn_stretch_test() checks for simple errors in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'blend_rst_1dn_stretch_test():' )
  print ( '  Shift and stretch test for blend_rst_1dn() to detect simple errors.' )
#
#  Set N to 3.
#
  n = 3
#
#  Shift by (1,2,3), stretch by (4,5,6).
#
  print ( '' )
  for r in [ 0.0, 0.5, 1.0 ]:
    for s in [ 0.0, 0.5, 1.0 ]:
      for t in [ 0.0, 0.5, 1.0 ]:
        x = blend_rst_1dn ( r, s, t, n, stretch_rst )
        print ( '  %8f  %8f  %8f  %8f  %8f  %8f' % ( r, s, t, x[0], x[1], x[2] ) )

  return

def blend_rst_2dn ( r, s, t, n, bound_rst ):

#*****************************************************************************80
#
## blend_rst_2dn() extends vector data on faces into a cube.
#
#  Diagram:
#
#    010-----r10-----110        011-----r11-----111
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    0s0.....rs0.....1s0        0s1.....rs1.....1s1     S
#      |       .       |          |       .       |     |
#      |       .       |          |       .       |     |
#    000-----r00-----100        001-----r01-----101     +----R
#           BOTTOM                      TOP
#
#    011-----0s1-----001        111-----1s1-----101
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    01t.....0st.....00t        11t.....1st.....10t          T
#      |       .       |          |       .       |          |
#      |       .       |          |       .       |          |
#    010-----0s0-----000        110-----1s0-----100     S----+
#           LEFT                       RIGHT
#
#    001-----r01-----101        011-----r11-----111
#      |       .       |          |       .       |
#      |       .       |          |       .       |
#    00t.....r0t.....100        01t.....r1t.....11t     T
#      |       .       |          |       .       |     |
#      |       .       |          |       .       |     |
#    000-----r00-----100        010-----r10-----110     +----R
#           FRONT                       BACK
#
#  Discussion:
#
#    BLEND_RST_2DN is NOT equivalent to a trilinear finite element
#    method, since the data is sampled everywhere along the corners,
#    edges, and faces, rather than at a finite number of nodes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Gordon,
#    Blending-Function Methods of Bivariate and Multivariate Interpolation
#    and Approximation,
#    SIAM Journal on Numerical Analysis,
#    Volume 8, Number 1, March 1971, pages 158-177.
#
#    William Gordon and Charles Hall,
#    Transfinite Element Methods: Blending-Function Interpolation over
#    Arbitrary Curved Element Domains,
#    Numerische Mathematik,
#    Volume 21, Number 1, 1973, pages 109-129.
#
#    William Gordon and Charles Hall,
#    Construction of Curvilinear Coordinate Systems and Application to
#    Mesh Generation,
#    International Journal of Numerical Methods in Engineering,
#    Volume 7, 1973, pages 461-477.
#
#    Joe Thompson, Bharat Soni, Nigel Weatherill,
#    Handbook of Grid Generation,
#    CRC Press, 1999.
#
#  Input:
#
#    real R, S, T, the (R,S,T) coordinates of the point
#    to be evaluated.
#
#    integer N, the dimension of the vector space.
#
#    function BOUND_RST, is a function which is given (R,S,T)
#    coordinates and an component value I, and returns XI, the value
#    of the I-th component of the N-vector at that point.  BOUND_RST
#    will only be called for "faces", that is, for values (R,S,T) where
#    at least one of R, S and T is either 0.0 or 1.0.  BOUND_RST has 
#    the form:
#      function xi = bound_rst ( r, s, t, i + 1 )
#
#  Output:
#
#    real X(N), the interpolated value at the
#    point (R,S,T).
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
#
#  Get the I-th coordinate component at the corners.
#
    x000 = bound_rst ( 0.0, 0.0, 0.0, i + 1 )
    x001 = bound_rst ( 0.0, 0.0, 1.0, i + 1 )
    x010 = bound_rst ( 0.0, 1.0, 0.0, i + 1 )
    x011 = bound_rst ( 0.0, 1.0, 1.0, i + 1 )
    x100 = bound_rst ( 1.0, 0.0, 0.0, i + 1 )
    x101 = bound_rst ( 1.0, 0.0, 1.0, i + 1 )
    x110 = bound_rst ( 1.0, 1.0, 0.0, i + 1 )
    x111 = bound_rst ( 1.0, 1.0, 1.0, i + 1 )
#
#  Get the I-th coordinate component at the edges.
#
    xr00 = bound_rst ( r, 0.0, 0.0, i + 1 )
    xr01 = bound_rst ( r, 0.0, 1.0, i + 1 )
    xr10 = bound_rst ( r, 1.0, 0.0, i + 1 )
    xr11 = bound_rst ( r, 1.0, 1.0, i + 1 )

    x0s0 = bound_rst ( 0.0, s, 0.0, i + 1 )
    x0s1 = bound_rst ( 0.0, s, 1.0, i + 1 )
    x1s0 = bound_rst ( 1.0, s, 0.0, i + 1 )
    x1s1 = bound_rst ( 1.0, s, 1.0, i + 1 )

    x00t = bound_rst ( 0.0, 0.0, t, i + 1 )
    x01t = bound_rst ( 0.0, 1.0, t, i + 1 )
    x10t = bound_rst ( 1.0, 0.0, t, i + 1 )
    x11t = bound_rst ( 1.0, 1.0, t, i + 1 )
#
#  Get the I-th component on the faces.
#
    x0st = bound_rst ( 0.0, s, t, i + 1 )
    x1st = bound_rst ( 1.0, s, t, i + 1 )
    xr0t = bound_rst ( r, 0.0, t, i + 1 )
    xr1t = bound_rst ( r, 1.0, t, i + 1 )
    xrs0 = bound_rst ( r, s, 0.0, i + 1 )
    xrs1 = bound_rst ( r, s, 1.0, i + 1 )
#
#  Interpolate the I-th coordinate component of the interior point.
#
    x[i] = blend_123 ( r, s, t, x000, x001, x010, x011, x100, x101, x110, x111, \
      xr00, xr01, xr10, xr11, x0s0, x0s1, x1s0, x1s1, x00t, x01t, x10t, x11t, \
      x0st, x1st, xr0t, xr1t, xrs0, xrs1 )

  return x

def blend_rst_2dn_identity_test ( ):

#*****************************************************************************80
#
## blend_rst_2dn_identity_test() checks for a gross error in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2026
#
#  Author:
#
#    John Burkardt
#
  nmax = 3

  print ( '' )
  print ( 'blend_rst_2dn_identity_test():' )
  print ( '  Simple identity test for blend_rst_2dn() to detect gross errors.' )
#
#  Set N to 3.
#
  n = 3
#
#  Test on identity.
#
  print ( '' )
  for r in [ 0.0, 0.5, 1.0 ]:
    for s in [ 0.0, 0.5, 1.0 ]:
      for t in [ 0.0, 0.5, 1.0 ]:
        x = blend_rst_2dn ( r, s, t, n, identity_rst )
        print ( '  %8f  %8f  %8f  %8f  %8f  %8f' % ( r, s, t, x[0], x[1], x[2] ) )

  return

def blend_rst_2dn_stretch_test ( ):

#*****************************************************************************80
#
## blend_rst_2dn_stretch_test() checks for simple errors in the blend coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'blend_rst_2dn_stretch_test():' )
  print ( '  Shift and stretch test for blend_rst_2dn() to detect simple errors.' )
#
#  Set N to 3.
#
  n = 3
#
#  Shift by (1,2,3), stretch by (4,5,6).
#
  print ( '' )
  for r in [ 0.0, 0.5, 1.0 ]:
    for s in [ 0.0, 0.5, 1.0 ]:
      for t in [ 0.0, 0.5, 1.0 ]:
        x = blend_rst_2dn ( r, s, t, n, stretch_rst )
        print ( '  %8f  %8f  %8f  %8f  %8f  %8f' % ( r, s, t, x[0], x[1], x[2] ) )

  return

def cubic_rs ( r, s, i ):

#*****************************************************************************80
#
## cubic_rs() evaluates a function of R and S used for some tests.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, S, the (local) coordinates of a point.
#
#    integer I, the component of X to be returned.
#
#  Output:
#
#    real X, the value of the I-th component of X at the point whose
#    local coordinates are (R,S).
#
  x = 20.0 * ( r * r * s * s * s )

  return x

def ellipse_rs ( r, s, i ):

#*****************************************************************************80
#
## ellipse_rs() maps the boundary of the unit square to an ellipse.
#
#  Discussion:
#
#    The ellipse is ( 3 * cos ( THETA ), 2 * sin ( THETA ) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, S, the coordinates of a point that lies on the
#    boundary of the square.
#
#    integer I, the component of the data which is to be returned.
#
#  Output:
#
#    real X, the I-th component of the data vector X, evaluated
#    at the point (R,S), which is on a corner, or edge, of the unit square.
#
  import numpy as np

  if ( r == 0.0 ):
    theta = 0.25 * np.pi * ( 5.0 * ( 1.0 - s ) + 3.0 * s  )
  elif ( r == 1.0 ):
    theta = 0.25 * np.pi * ( - 1.0 * ( 1.0 - s ) + 1.0 * s )
  elif ( s == 0.0 ):
    theta = 0.25 * np.pi * ( 5.0 * ( 1.0 - r ) + 7.0 * r )
  elif ( s == 1.0 ):
    theta = 0.25 * np.pi * ( 3.0 * ( 1.0 - r ) + 1.0 * r )

  if ( i == 1 ):

    x = 3.0 * np.cos ( theta )

  elif ( i == 2 ):

    x = 2.0 * np.sin ( theta )

  else:

    print ( '' )
    print ( 'ellipse_rs(): Fatal error!' )
    print ( '  Illegal component index I = #d', i )
    raise Exception ( 'ellipse_rs(): Fatal error!' )

  return x

def identity_r ( r, i ):

#*****************************************************************************80
#
## identity_r() returns a data component given (R).
#
#  Discussion:
#
#    This is a dummy routine, which simply returns (R).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the coordinate of a point that lies on the
#    boundary of the cube.
#
#    integer I, the component of the data which is to be returned.
#
#  Output:
#
#    real X, the I-th component of the data vector X, evaluated
#    at the point (R), which is on an endpoint of the unit line segment.
#
  if ( i == 1 ):
    x = r
  else:
    print ( '' )
    print ( 'identity_r(): Fatal error!' )
    print ( '  Illegal component index I = ', i )
    raise Exception ( 'identity_r(): Fatal error!' )

  return x

def identity_rs ( r, s, i ):

#*****************************************************************************80
#
## identity_rs() returns a data component given (R,S).
#
#  Discussion:
#
#    This is a dummy routine, which simply returns (R,S).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, S, the coordinates of a point that lies on the
#    boundary of the square.
#
#    integer I, the component of the data which is to be returned.
#
#  Output:
#
#    real X, the I-th component of the data vector X, evaluated
#    at the point (R,S), which is on a corner, or edge, of the unit square.
#
  if ( i == 1 ):
    x = r
  elif ( i == 2 ):
    x = s
  else:
    print ( '' )
    print ( 'identity_rs(): Fatal error!' )
    print ( '  Illegal component index I = ', i )
    raise Exception ( 'identity_rs(): Fatal error!' )

  return x

def identity_rst ( r, s, t, i ):

#*****************************************************************************80
#
## identity_rst() returns a data component given (R,S,T).
#
#  Discussion:
#
#    This is a dummy routine, which simply returns (R,S,T).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, S, T, the coordinates of a point that lies on the
#    boundary of the cube.
#
#    integer I, the component of the data which is to be returned.
#
#  Output:
#
#    real X, the I-th component of the data vector X, evaluated
#    at the point (R,S), which is on a corner, edge or face of the unit cube.
#
  if ( i == 1 ):
    x = r
  elif ( i == 2 ):
    x = s
  elif ( i == 3 ):
    x = t
  else:
    print ( '' )
    print ( 'identity_rst(): Fatal error!' )
    print ( '  Illegal component index I = ', i )
    raise Exception ( 'identity_rst(): Fatal error!' )

  return x

def powers_r ( r, i ):

#*****************************************************************************80
#
## powers_r() returns a data component given (R).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the coordinate of a point that lies on the boundary.
#
#    integer I, the component of the data which is to be returned.
#
#  Output:
#
#    real X, the I-th component of the data vector X, evaluated
#    at the point (R), which is on the unit line segment.
#
  x = r ** i;

  return x

def quad_rst ( r, s, t, i ):

#*****************************************************************************80
#
## quad_rst() evaluates a function of (R,S,T) used for some tests.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, S, T, the (local) coordinates of a point.
#
#    integer I, the component of X to be returned.
#
#  Output:
#
#    real X, the value of the I-th component of X at the point whose
#    local coordinates are (R,S,T).
#
  x = 18.0 * ( r * r + s + t )

  return x

def sphere_rst ( r, s, t, i ):

#*****************************************************************************80
#
## sphere_rst() maps the boundary of the unit cube to a sphere.
#
#  Discussion:
#
#    The sphere is
#      x = cos ( theta ) * cos ( phi )
#      y = sin ( theta ) * cos ( phi )
#      z = sin ( phi )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, S, the coordinates of a point that lies on the
#    boundary of the square.
#
#    integer I, the component of the data which is to be returned.
#
#  Output:
#
#    real X, the I-th component of the data vector X, evaluated
#    at the point (R,S), which is on a corner, or edge, of the unit square.
#
  import numpy as np
#
#  Compute length of vector from ( 0.5, 0.5, 0.5 ) to ( r, s, t )
#
  norm = np.sqrt ( ( r - 0.5 )**2 + ( s - 0.5 )**2 + ( t - 0.5 )**2 )
#
#  Compute ( x, y, z ) coordinates of a point on the sphere
#  ( x - 0.5 )^2 + ( y - 0.5 )^2 + ( z - 0.5 )^2 = 0.25 that is
#  the projection of the point ( r, s, t ) on the unit cube.
#
  if ( i == 1 ):

    x = 0.5 + 0.5 * ( r - 0.5 ) / norm

  elif ( i == 2 ):

    x = 0.5 + 0.5 * ( s - 0.5 ) / norm

  elif ( i == 3 ):

    x = 0.5 + 0.5 * ( t - 0.5 ) / norm

  else:

    printf ( '' )
    printf ( 'sphere_rst(): Fatal error!' )
    printf ( '  Illegal component index I =', i )
    raise Exception ( 'sphere_rst(): Fatal error!' )

  return x

def stretch_r ( r, i ):

#*****************************************************************************80
#
## stretch_r() returns a data component given (R).
#
#  Discussion:
#
#    This routine shifts by 1 and stretches by 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the coordinate of a point that lies on the boundary.
#
#    integer I, the component of the data which is to be returned.
#
#  Output:
#
#    real X, the I-th component of the data vector X, evaluated
#    at the point (R), which is on an endpoint of the unit line segment.
#
  if ( i == 1 ):
    x = 2.0 * r + 1.0
  else:
    print ( '' )
    print ( 'stretch_r(): Fatal error!' )
    print ( '  Illegal component index I = ', i )
    raise Exception ( 'stretch_r(): Fatal error!' )

  return x

def stretch_rs ( r, s, i ):

#*****************************************************************************80
#
## stretch_rs() returns a data component given (R,S).
#
#  Discussion:
#
#    This routine shifts by (1,2) and stretches by (3,4).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, S, the coordinates of a point that lies on the
#    boundary of the square.
#
#    integer I, the component of the data which is to be returned.
#
#  Output:
#
#    real X, the I-th component of the data vector X, evaluated
#    at the point (R,S), which is on a corner, or edge, of the unit square.
#
  if ( i == 1 ):
    x = 3.0 * r + 1.0
  elif ( i == 2 ):
    x = 4.0 * s + 2.0
  else:
    print ( '' )
    print ( 'stretch_rs(): Fatal error!' )
    print ( '  Illegal component index I = ', i )
    raise Exception ( 'stretch_rs(): Fatal error!' )

  return x

def stretch_rst ( r, s, t, i ):

#*****************************************************************************80
#
## stretch_rst() returns a data component given (R,S,T).
#
#  Discussion:
#
#    This routine shifts by (1,2,3) and stretches by (4,5,6)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, S, T, the coordinates of a point that lies on the
#    boundary of the cube.
#
#    integer I, the component of the data which is to be returned.
#
#  Output:
#
#    real X, the I-th component of the data vector X, evaluated
#    at the point (R,S), which is on a corner, edge or face of the unit cube.
#
  if ( i == 1 ):
    x = 4.0 * r + 1.0
  elif ( i == 2 ):
    x = 5.0 * s + 2.0
  elif ( i == 3 ):
    x = 6.0 * t + 3.0
  else:
    print ( '' )
    print ( 'stretch_rst(): Fatal error!' )
    print ( '  Illegal component index I = ', i )
    raise Exception ( 'stretch_rst(): Fatal error!' )

  return x

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
  blend_test ( )
  timestamp ( )

