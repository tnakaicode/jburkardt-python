#! /usr/bin/env python3
#

def continuity_exact_test ( ):

#*****************************************************************************80
#
## continuity_exact_test() tests continuity_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'continuity_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test continuity_exact().' )

  rng = default_rng ( )

  grid_2d_test ( )
  uv_spiral_test ( rng )
  resid_spiral_test ( rng )
  spiral_gnuplot_test ( )
  spiral_matplotlib_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'continuity_exact_test():' )
  print ( '  Normal end of execution.' )
  return

def grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi ):

#*****************************************************************************80
#
## grid_2d() returns a regular 2D grid.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X_NUM, the number of X values to use.
#
#    real X_LO, X_HI, the range of X values.
#
#    integer Y_NUM, the number of Y values to use.
#
#    real Y_LO, Y_HI, the range of Y values.
#
#  Output:
#
#    real X(X_NUM*Y_NUM), Y(X_NUM*Y_NUM), the coordinates of the grid.
#
  import numpy as np

  x = np.zeros ( x_num * y_num )
  y = np.zeros ( x_num * y_num )

  if ( x_num == 1 ):
    xi = ( x_lo + x_hi ) / 2.0
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        x[k] = xi
        k = k + 1
  else:
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        xi = ( float ( x_num - i - 1 ) * x_lo   \
             + float (         i     ) * x_hi ) \
             / float ( x_num     - 1 )
        x[k] = xi
        k = k + 1

  if ( y_num == 1 ):
    yj = ( y_lo + y_hi ) / 2.0
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        y[k] = yj
        k = k + 1
  else:
    k = 0
    for j in range ( 0, y_num ):
      yj = ( float ( y_num - j - 1 ) * y_lo   \
           + float (         j     ) * y_hi ) \
           / float ( y_num     - 1 )
      for i in range ( 0, x_num ):
        y[k] = yj
        k = k + 1

  return x, y

def grid_2d_test ( ):

#*****************************************************************************80
#
## grid_2d_test() makes a small 2D grid.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2024
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'grid_2d_test:' )
  print ( '  grid_2d() generates a regular grid.' )

  x_lo = 10.0
  x_hi = 20.0
  x_num = 5

  y_lo = 5.0
  y_hi = 6.0
  y_num = 3

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  print ( '' )
  k = 0
  for j in range ( 0, y_num ):
    for i in range ( 0, x_num):
      print ( '  %2d  %2d  %2d  %14.6f  %14.6f' % ( k, i, j, x[k], y[k] ) )
      k = k + 1

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def resid_spiral ( n, x, y, c ):

#*****************************************************************************80
#
## resid_spiral() computes the residual for a spiral velocity vector field.
#
#  Discussion:
#
#    Note that the continuous velocity field (U,V)(X,Y) that is discretely
#    sampled here satisfies the homogeneous continuity equation, that is,
#    it has zero divergence.  In other words:
#
#      dU/dX + dV/dY = 0.
#
#    This is by construction, since we have
#
#      U(X,Y) =  10 * d/dY ( PHI(X) * PHI(Y) )
#      V(X,Y) = -10 * d/dX ( PHI(X) * PHI(Y) )
#
#    which guarantees zero divergence.
#
#    The underlying function PHI is defined by
#
#      PHI(Z) = ( 1 - cos ( C * pi * Z ) ) * ( 1 - Z )^2
#
#    where C is a parameter.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the coordinates of the evaluation points.
#
#    real C, a parameter, typically between 0 and 2 * PI.
#
#  Output:
#
#    real PR(N), the residual in the continuity equation.
#
  import numpy as np

  pr = np.zeros ( n )
  u = np.zeros ( n )
  ux = np.zeros ( n )
  v = np.zeros ( n )
  vy = np.zeros ( n )

  u =   10.0 * ( 1.0 - np.cos ( c * np.pi * x ) ) \
           * ( 1.0 - x ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * y ) ) \
             * 2.0 * ( 1.0 - y ) \
             )

  ux =   10.0 * \
    ( \
      c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * x ) ) \
      * 2.0 * ( 1.0 - x ) \
    ) \
    * \
    ( \
      c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * y ) ) \
      * 2.0 * ( 1.0 - y ) \
    );

  v = - 10.0 * ( 1.0 - np.cos ( c * np.pi * y ) ) \
           * ( 1.0 - y ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * x ) ) \
             * 2.0 * ( 1.0 - x ) \
             );

  vy =  - 10.0 * \
    ( \
      c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * x ) ) \
      * 2.0 * ( 1.0 - x ) \
    ) \
    * \
    ( \
      c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
      - ( 1.0 - np.cos ( c * np.pi * y ) ) \
      * 2.0 * ( 1.0 - y ) \
    )

  pr = ux + vy;

  return pr

def resid_spiral_test ( rng ):

#*****************************************************************************80
#
## resid_spiral_test() tests resid_spiral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
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
  print ( 'resid_spiral_test():' )
  print ( '  Sample a spiral velocity field and estimate the' )
  print ( '  range of residuals in the continuity equation.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  t = 0.0

  c = 1.00

  pr = resid_spiral ( n, x, y, c )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) ) )

  return

def spiral_gnuplot ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## spiral_gnuplot() writes the spiral vector field to files for GNUPLOT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string HEADER, a header to be used to name the files.
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the coordinates of the evaluation points.
#
#    real U(N), V(N), the velocity components.
#
#    real S, a scale factor for the velocity vectors.
#

#
#  Write the data file.
#
  data_filename = header + '_data.txt'

  data_unit = open ( data_filename, 'w' )

  for i in range ( 0, n ):
    st = '  %g' % ( x[i] )
    data_unit.write ( st )
    st = '  %g' % ( y[i] )
    data_unit.write ( st )
    st = '  %g' % ( s * u[i] )
    data_unit.write ( st )
    st = '  %g' % ( s * v[i] )
    data_unit.write ( st )
    data_unit.write ( '\n' );

  data_unit.close ( )

  print ( '' )
  print ( '  Data written to "%s".' % ( data_filename ) )
#
#  Write the command file.
#
  command_filename = header + '_commands.txt'
  plot_filename = header + '.png'

  command_unit = open ( command_filename, 'w' )

  command_unit.write ( '#  %s\n' % ( command_filename ) )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set term png\n' )
  command_unit.write ( 'set output "%s"\n' % ( plot_filename ) )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Add titles and labels.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set xlabel "<--- X --->"\n' )
  command_unit.write ( 'set ylabel "<--- Y --->"\n' )
  command_unit.write ( 'set title "Spiral velocity flow"\n' )
  command_unit.write ( 'unset key\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Add grid lines.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set grid\n' )
  command_unit.write ( 'set size ratio -1\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Timestamp the plot.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set timestamp\n' )
  command_unit.write ( 'plot "%s" using 1:2:3:4 with vectors \\\n' % ( data_filename ) )
  command_unit.write ( '  head filled lt 2 linecolor rgb "blue"\n' )
  command_unit.write ( 'quit\n' )

  data_unit.close ( )

  print ( '  Commands written to "%s".' % ( command_filename ) )

  return

def spiral_gnuplot_test ( ):

#*****************************************************************************80
#
## spiral_gnuplot_test() tests spiral_gnuplot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'spiral_gnuplot_test:' )
  print ( '  Generate a spiral velocity field on a regular grid.' )
  print ( '  Store in GNUPLOT data and command files.' )

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
  c = 1.0

  u, v = uv_spiral ( n, x, y, c )

  header = 'continuity_exact'
  s = 0.05
  spiral_gnuplot ( header, n, x, y, u, v, s )

  return

def spiral_matplotlib ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## spiral_matplotlib() plots the velocity vector field with matplotlib.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string HEADER, a header to be used to name the files.
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the coordinates of the evaluation points.
#
#    real U(N), V(N), the velocity components.
#
#    real S, a scale factor for the velocity vectors.
#
  import matplotlib.pyplot as plt

  myplot = plt.figure ( )
  ax = plt.gca ( )
  ax.quiver ( x, y, u, v )
  ax.set_xlabel ( '<--X-->' )
  ax.set_ylabel ( '<--Y-->' )
  ax.set_title ( header )
  ax.axis ( 'equal' )
  plt.draw ( )
  plot_filename = header + '_matplotlib.png'
  myplot.savefig ( plot_filename )
  plt.show ( block = False )
  plt.close ( )

  return

def spiral_matplotlib_test ( ):

#*****************************************************************************80
#
## spiral_matplotlib_test() tests spiral_matplotlib().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'spiral_matplotlib_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Generate a spiral velocity field on a regular grid.' )
  print ( '  Display it using matplotlib' )

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
  c = 1.0

  u, v = uv_spiral ( n, x, y, c )

  header = 'continuity_exact'
  s = 0.05
  spiral_matplotlib ( header, n, x, y, u, v, s )

  return

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

def uv_spiral ( n, x, y, c ):

#*****************************************************************************80
#
## uv_spiral() computes a spiral velocity vector field.
#
#  Discussion:
#
#    Note that the continuous velocity field (U,V)(X,Y) that is discretely
#    sampled here satisfies the homogeneous continuity equation, that is,
#    it has zero divergence.  In other words:
#
#      dU/dX + dV/dY = 0.
#
#    This is by construction, since we have
#
#      U(X,Y) =  10 * d/dY ( PHI(X) * PHI(Y) )
#      V(X,Y) = -10 * d/dX ( PHI(X) * PHI(Y) )
#
#    which guarantees zero divergence.
#
#    The underlying function PHI is defined by
#
#      PHI(Z) = ( 1 - cos ( C * pi * Z ) ) * ( 1 - Z )^2
#
#    where C is a parameter.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the coordinates of the evaluation points.
#
#    real C, a parameter, typically between 0 and 2 * PI.
#
#  Output:
#
#    real U(N), V(N), the velocity components.
#
  import numpy as np

  u = np.zeros ( n )
  v = np.zeros ( n )

  u =   10.0 * ( 1.0 - np.cos ( c * np.pi * x ) ) \
           * ( 1.0 - x ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * y ) * ( 1.0 - y ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * y ) ) \
             * 2.0 * ( 1.0 - y ) \
             )

  v = - 10.0 * ( 1.0 - np.cos ( c * np.pi * y ) ) \
           * ( 1.0 - y ) ** 2 \
           * ( \
               c * np.pi * np.sin ( c * np.pi * x ) * ( 1.0 - x ) ** 2 \
             - ( 1.0 - np.cos ( c * np.pi * x ) ) \
             * 2.0 * ( 1.0 - x ) \
             )

  return u, v

def uv_spiral_test ( rng ):

#*****************************************************************************80
#
## uv_spiral_test() tests uv_spiral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
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

  nu = 1.0
  rho = 1.0

  print ( '' )
  print ( 'uv_spiral_test():' )
  print ( '  Sample a spiral velocity field and estimate' )
  print ( '  the range of the solution values.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )

  c = 1.0
  u, v = uv_spiral ( n, x, y, c )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  continuity_exact_test ( )
  timestamp ( )

