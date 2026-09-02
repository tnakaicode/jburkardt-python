#! /usr/bin/env python3
#
def shepard_interp_2d_test ( ):

#*****************************************************************************80
#
## shepard_interp_2d_test() tests shepard_interp_2d().
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
  import sys
  sys.path.insert ( 0, '/home/john/public_html/py_src/test_interp_2d' )
  from test_interp_2d import f00_num

  import matplotlib
  import numpy as np
  import platform
  import sys

  print ( '' )
  print ( 'shepard_interp_2d_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test shepard_interp_2d().' )
  print ( '  This test also needs the test_interp_2d() library.' )

  prob_num = f00_num ( )
  g = 1

  for prob in range ( 1, prob_num + 1 ):

    for p in [ 1.0, 2.0, 4.0, 8.0 ]:
      shepard_interp_2d_test01 ( prob, g, p )
#
#  Terminate.
#
  print ( '' )
  print ( 'shepard_interp_2d_test():' )
  print ( '  Normal end of execution.' )

  return

def shepard_interp_2d_test01 ( prob, g, p ):

#*****************************************************************************80
#
## shepard_interp_2d_test01() tests shepard_interp_2d().
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
#  Input:
#
#    integer PROB, the problem number.
#
#    integer G, the grid number.
#
#    real P, the power used in the distance weighting.
#
  import sys
  sys.path.insert ( 0, '/home/john/public_html/py_src/test_interp_2d' )
  from test_interp_2d import f00_f0
  from test_interp_2d import f00_title
  from test_interp_2d import g00_size
  from test_interp_2d import g00_xy

  from matplotlib import cm
  from matplotlib.tri import Triangulation
  from mpl_toolkits.mplot3d import Axes3D
  from scipy.spatial import Delaunay
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'shepard_interp_2d_test01():' )
  print ( '  Interpolate data from test_interp_2d() problem ', prob )
  print ( '  using grid ', g )
  print ( '  using Shepard interpolation with P = ', p )

  nd = g00_size ( g )
  print ( '  Number of data points = ', nd )

  xd, yd = g00_xy ( g, nd )
  
  zd = f00_f0 ( prob, nd, xd, yd )

  if ( p == 1.0 ):
    r8vec3_print ( nd, xd, yd, zd, '  X, Y, Z data:' )
#
#  #1:  Does interpolant match function at interpolation points?
#
  ni = nd
  xi = xd
  yi = yd
  zi = shepard_interp_2d ( nd, xd, yd, zd, p, ni, xi, yi )

  int_error = np.linalg.norm ( zi - zd ) / ni

  print ( '' )
  print ( '  L2 interpolation error averaged per interpolant node = ', int_error )
#
#  #2:  Sample the interpolant away from data.
#
  if ( p == 1.0 ):
    nix = 5
    niy = 5
    xmin = 0.0
    xmax = 1.0
    ymin = 0.0
    ymax = 1.0
    xi = np.linspace ( xmin, xmax, nix )
    yi = np.linspace ( ymin, ymax, niy )
    XI, YI = np.meshgrid ( xi, yi )
    NIvec = nix * niy
    XIvec = np.reshape ( XI, [ NIvec ] )
    YIvec = np.reshape ( YI, [ NIvec ] )
    ZIvec = shepard_interp_2d ( nd, xd, yd, zd, p, NIvec, XIvec, YIvec )
    r8vec3_print ( NIvec, XIvec, YIvec, ZIvec, '  sample X, Y, Z interpolated data:' )
#
#  #3: Plot the linear interpolant.
#
  if ( p == 1.0 ):

    xyd = np.stack ( ( xd, yd ), axis = -1 )

    fig = plt.figure ( )
    ax = fig.add_subplot ( 111, projection = '3d' )
    tri = Triangulation ( xd, yd )
    ax.plot_trisurf ( xd, yd, zd, triangles = tri.triangles, cmap=cm.coolwarm )
    ft = f00_title ( prob )
    ax.set_title ( ft )
    plt.grid ( True )
    ax.set_xlabel ( '<--- X --->' )
    ax.set_ylabel ( '<--- Y --->' )
    ax.set_zlabel ( '<---Z(X,Y)--->' )
    filename = ( 'p%02ddata.png' % ( prob ) )
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )
#
#  #4: Set the Shepard interpolant.
# 
  nix = 21
  niy = 21
  xmin = 0.0
  xmax = 1.0
  ymin = 0.0
  ymax = 1.0
  xi = np.linspace ( xmin, xmax, nix )
  yi = np.linspace ( ymin, ymax, niy )
  XI, YI = np.meshgrid ( xi, yi )
  NIvec = nix * niy
  XIvec = np.reshape ( XI, [ NIvec ] )
  YIvec = np.reshape ( YI, [ NIvec ] )
  ZIvec = shepard_interp_2d ( nd, xd, yd, zd, p, NIvec, XIvec, YIvec )
#
#  Reshape interpolant vector as a matrix.
#
  ZI = np.reshape ( ZIvec, [ nix, niy ] )
#
#  #5: Plot the Shepard interpolant.
# 
  fig = plt.figure ( )
  plt.clf ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot_surface ( XI, YI, ZI, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( '<--- X --->' )
  ax.set_ylabel ( '<--- Y --->' )
  ax.set_zlabel ( '<---Z(X,Y)--->' )
  s = ( 'Shepard interpolant for problem %d with P = %g' % ( prob, p ) )
  ax.set_title ( s )
  plt.grid ( True )
  filename = ( 'p%02d_power%g.png' % ( prob, p ) )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '".' )
  plt.close ( )

  return

def r8vec3_print ( n, a1, a2, a3, title ):

#*****************************************************************************80
#
## r8vec3_print() prints an R8VEC3.
#
#  Discussion:
#
#    An R8VEC3 is a dataset consisting of 3 vectors of N real values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), A3(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g  %12g' % ( i, a1[i], a2[i], a3[i] ) )

  return

def shepard_interp_2d ( nd, xd, yd, zd, p, ni, xi, yi ):

#*****************************************************************************80
#
## shepard_interp_2d() evaluates a 2D Shepard interpolant.
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
#    Donald Shepard,
#    A two-dimensional interpolation function for irregularly spaced data,
#    ACM '68: Proceedings of the 1968 23rd ACM National Conference,
#    ACM, pages 517-524, 1969.
#
#  Input:
#
#    integer ND, the number of data points.
#
#    real XD(ND), YD(ND), the data points.
#
#    real ZD(ND), the data values.
#
#    real P, the power.
#
#    integer NI, the number of interpolation points.
#
#    real XI(NI), YI(NI), the interpolation points.
#
#  Output:
#
#    real ZI(NI), the interpolated values.
# 
  import numpy as np

  zi = np.zeros ( ni )

  for i in range ( 0, ni ):

    if ( p == 0.0 ):

      w = np.ones ( nd ) / nd

    else:

      w = np.zeros ( nd )
#
#  Compute distances,
#  but also check whether this interpolation point is already a data point.
#
      z = -1
      for j in range ( 0, nd ):
        vi = np.array ( [ xi[i], yi[i] ] )
        vd = np.array ( [ xd[j], yd[j] ] )
        w[j] = np.linalg.norm ( vi - vd )
        if ( w[j] == 0.0 ):
          z = j
          break

      if ( z != -1 ):
        w[:] = 0.0
        w[z] = 1.0
      else:
        w = 1.0 / w ** p
        w = w / np.sum ( w )

    zi[i] = np.dot ( w, zd )

  return zi

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
  shepard_interp_2d_test ( )
  timestamp ( )

