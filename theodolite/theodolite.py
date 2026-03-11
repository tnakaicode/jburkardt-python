#! /usr/bin/env python3
#
def theodolite_test ( ):

#*****************************************************************************80
#
## theodolite_test() tests theodolite().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'theodolite_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test theodolite().' )

  theodolite_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'theodolite_test():' )
  print ( '  Normal end of execution.' )

  return

def theodolite_test01 ( ):

#*****************************************************************************80
#
## theodolite_test01() tests theodolite().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2026
#
#  Author:
#
#    John Burkardt
#
  from scipy.optimize import least_squares
  import numpy as np
  import pprint

  print ( '' )
  print ( 'theodolite_test01():' )
  print ( '  Estimate the XYZ coordinates of an event in the sky' )
  print ( '  observed by 10 scattered stations.' )
  print ( '' )
  print ( '  Seek a position XYZ which minimizes the sum of squares' )
  print ( '  of the distance of the event to each of the lines defined' )
  print ( '  by an observer''s data.' )
  print ( '' )
  print ( '  The scipy.optimize function least_squares() is used.' )

  n = 10
#
#  Our initial guess is simply the average of the observer locations.
#
  xyz_star = np.array ( [ 1245.0, 759.0, 103.5 ] )
  f = theodolite_f ( xyz_star )
  f_norm = np.linalg.norm ( f )
#
#  Evaluate the residual at our initial guess.
#
  print ( '' )
  print ( '  Initial location estimate xyz:' )
  pprint.pprint ( xyz_star )
  print ( '' )
  print ( '  Initial residual vector f:' )
  pprint.pprint ( f )
  print ( '  Initial ||F|| =', f_norm )
#
#  Call least_squares to get an approximate minimizer.
#
  lsq = least_squares ( theodolite_f, xyz_star )
  xyz_star = lsq.x
  f = theodolite_f ( xyz_star )
  f_norm = np.linalg.norm ( f )

  print ( '' )
  print ( '  Final location estimate xyz:' )
  pprint.pprint ( xyz_star )
  print ( '' )
  print ( '  Final residual vector f:' )
  pprint.pprint ( f )
  print ( '  Final ||F|| =', f_norm )

  return

def line_par_point_dist_3d ( f, g, h, x0, y0, z0, p ):

#*****************************************************************************80
#
## line_par_point_dist_3d(): distance ( parametric line, point ) in 3D.
#
#  Discussion:
#
#    The parametric form of a line in 3D is:
#
#      X = X0 + F * T
#      Y = Y0 + G * T
#      Z = Z0 + H * T
#
#    We normalize by choosing F*F+G*G+H*H=1 and 0 <= F.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Adrian Bowyer and John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Input:
#
#    real F, G, H, X0, Y0, Z0, the parametric line
#    parameters.
#
#    real P(3), the point whose distance from the line is
#    to be measured.
#
#  Output:
#
#    real DIST, the distance from the point to the line.
#
  import numpy as np

  dx =   g * ( f * ( p[1] - y0 ) - g * ( p[0] - x0 ) ) \
       + h * ( f * ( p[2] - z0 ) - h * ( p[0] - x0 ) )

  dy =   h * ( g * ( p[2] - z0 ) - h * ( p[1] - y0 ) ) \
       - f * ( f * ( p[1] - y0 ) - g * ( p[0] - x0 ) )

  dz = - f * ( f * ( p[2] - z0 ) - h * ( p[0] - x0 ) ) \
       - g * ( g * ( p[2] - z0 ) - h * ( p[1] - y0 ) )

  dist = np.sqrt ( dx * dx + dy * dy + dz * dz ) \
    / ( f * f + g * g + h * h )

  return dist

def theodolite_data1 ( ):

#*****************************************************************************80
#
## theodolite_data1() returns theodolite data for problem 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Hall,
#    Industrial Mathematics: A Course in Realism,
#    American Mathematical Monthly,
#    Volume 82, Number 6, June-July 1975, pages 651-659.
#
#  Output:
#
#    real XYZ(10,3), the coordinates of 10 sighting stations.
#
#    real AE(10,2), the azimuth (horizontal angle) and elevation
#    (vertical angle) of an event, as measured from each station.  The
#    angles are measured in degrees.
#
  import numpy as np

  xyz = np.array ( [ \
  [  4000.0,  5000.0, 1000.0 ], \
  [  1300.0,  1200.0,    0.0 ], \
  [  1300.0, -1200.0,    0.0 ], \
  [  2800.0,  1700.0,    5.0 ], \
  [  2800.0, -1700.0,    5.0 ], \
  [   200.0,  2500.0,    0.0 ], \
  [  1600.0,   100.0,   10.0 ], \
  [ -2000.0,  -800.0,   15.0 ], \
  [  -600.0,   700.0,    0.0 ], \
  [  1050.0,    90.0,    0.0 ], ] )

  ae = np.array ( [ \
   [ 237.0364,   0.0    ], \
   [ 255.9639,  38.9539 ], \
   [ 107.0361,  38.9538 ], \
   [ 219.3633,  21.8942 ], \
   [ 136.6367,  21.8942 ], \
   [ 287.7447,  20.8553 ], \
   [ 190.4622,  58.4325 ], \
   [  15.9314,  17.6014 ], \
   [ 336.3706,  29.7953 ], \
   [ 245.9453,  84.1217 ] ] )

  return xyz, ae

def theodolite_f ( xyz_star ):

#*****************************************************************************80
#
## theodolite_f() evaluates the residual for a theodolite solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Hall,
#    Industrial Mathematics: A Course in Realism,
#    American Mathematical Monthly,
#    Volume 82, Number 6, June-July 1975, pages 651-659.
#
#  Input:
#
#    integer N, the number of locations.
#
#    real XYZ(N,3), the locations of the cameras.
#
#    real AE(N,2), the azimuth and elevations of the event
#    at each camera, measured in degrees.
#
#    real XYZ_STAR(3), a possible location for the event.
#
#  Output:
#
#    real F(N), the distance of an event at XYZ_STAR
#    from each of the lines through a given camera, at the 
#    given angles.
#
  import numpy as np

  n = 10

  xyz = np.array ( [ \
   [ 4000.0,  5000.0, 1000.0 ], \
   [ 1300.0,  1200.0,    0.0 ], \
   [ 1300.0, -1200.0,    0.0 ], \
   [ 2800.0,  1700.0,    5.0 ], \
   [ 2800.0, -1700.0,    5.0 ], \
   [  200.0,  2500.0,    0.0 ], \
   [ 1600.0,   100.0,   10.0 ], \
   [-2000.0,  -800.0,   15.0 ], \
   [ -600.0,   700.0,    0.0 ], \
   [ 1050.0,    90.0,    0.0 ] ] )

  ae = np.array ( [ \
   [ 237.0364,   0.0    ], \
   [ 255.9639,  38.9539 ], \
   [ 107.0361,  38.9538 ], \
   [ 219.3633,  21.8942 ], \
   [ 136.6367,  21.8942 ], \
   [ 287.7447,  20.8553 ], \
   [ 190.4622,  58.4325 ], \
   [  15.9314,  17.6014 ], \
   [ 336.3706,  29.7953 ], \
   [ 245.9453,  84.1217 ] ] )

  f = np.zeros ( n )

  for i in range ( 0, n ):

    x0 = xyz[i,0]
    y0 = xyz[i,1]
    z0 = xyz[i,2]

    a = ae[i,0] * np.pi / 180.0
    e = ae[i,1] * np.pi / 180.0

    ff = np.cos ( e ) * np.cos ( a )
    gg = np.cos ( e ) * np.sin ( a )
    hh = np.sin ( e )

    dist = line_par_point_dist_3d ( ff, gg, hh, x0, y0, z0, xyz_star )

    f[i] = dist

  return f

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
  theodolite_test ( )
  timestamp ( )

