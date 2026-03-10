#! /usr/bin/env python3
#
def delsq_test ( ):

#*****************************************************************************80
#
## delsq_test() tests delsq().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2023
#
#  Author:
#
#    John Burkardt
#
  from mpl_toolkits import mplot3d
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'delsq_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test delsq()' )
#
#  Just for DEBUG:
#
  R = 'L'
  n = 7
  G_07 = numgrid ( R, n )
  print ( 'G07' )
  print ( G_07 )
  D = delsq ( G_07 )
  print ( 'D' )
  print ( D )

  plt.clf ( )
  plt.spy ( D, markersize = 5 )
  plt.title ( 'L region: 7x7 Laplacian operator' )
  filename = 'delsq_7x7.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Start with small sample.
#
  R = 'L'
  n = 10
  G = numgrid ( R, n )
  print ( '' )
  print ( '  numgrid region "' + R + '" with n = ', n )
#
#  Count the grid points.
#
  grid_num = np.sum ( G > 0 )
  print ( '' )
  print ( '  This grid uses ', grid_num, ' interior nodes.' )

  print ( '' )
  print ( '  Node indices:' )
  print ( G )

  plt.clf ( )
  plt.spy ( G, markersize = 2 )
  plt.title ( 'L region: 10x10 finite difference grid' )
  filename = 'grid_10x10.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Now go to an interesting size.
#
  R = 'L'
  n = 32
  G = numgrid ( R, n )
  print ( '' )
  print ( '  numgrid region "' + R + '" with n = ', n )
#
#  Count the grid points.
#
  grid_num = np.sum ( G > 0 )
  print ( '' )
  print ( '  This grid uses ', grid_num, ' interior nodes.' )
#
#  Plot the grid.
#
  plt.clf ( )
  plt.spy ( G, markersize = 2 )
  plt.title ( 'L region: 32x32 finite difference grid' )
  filename = 'grid_32x32.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Generate the Laplacian operator.
#
  D = delsq ( G )
  print ( '' )
  print ( '  Sparse Laplacian operator D' )

  plt.clf ( )
  plt.spy ( D, markersize = 2 )
  plt.title ( 'L region: 32x32 Laplacian operator' )
  filename = 'delsq_10x10.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Define a boundary value problem for grid function u in the region:
#    delsq(u) = 1 in interior
#          u  = 0 on boundary.
#
  rhs = np.ones ( grid_num )
  D2 = D.toarray ( )
  u = np.linalg.solve ( D2, rhs )
#
#  Map the solution back onto the grid.
#  
  U = G.copy ( )
  U [ G > 0 ] = u [ G [ G > 0 ] - 1 ]
#  
#  Create a contour plot, labeling the contour lines.
#  Use the prism colormap.
#
  plt.clf ( )
  plt.contour ( U )
# clabel ( contour ( U ) )
  plt.prism ( )
# axis ( 'square', 'ij' )
  filename = 'contour_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Now show solution as a mesh plot.
#
  m, n = U.shape
  xvec = np.linspace ( 0, n, n )
  yvec = np.linspace ( 0, m, m )
  xmat, ymat = np.meshgrid ( xvec, yvec )  
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot_wireframe ( xmat, ymat, U, rstride = 3, cstride = 3 )
  filename = 'mesh_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'delsq_test():' )
  print ( '  Normal end of execution.' )

  return

def delsq ( G ):

#*****************************************************************************80
#
## delsq() constructs the five-point finite difference Laplacian.
#
#  Discussion:
#
#    delsq(G) is the sparse form of the two-dimensional,
#    5-point discrete negative Laplacian on the grid G.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 August 2023
#
#  Author:
#
#    Original MATLAB version by Cleve Moler.
#    This version by John Burkardt
#
#  Input:
#
#    integer G[m,m]: a grid whose positive entries are the indices of
#    nodes.
#
#  Output:
#
#    sparse matrix D(): defines the negative Laplacian operator 
#    for the grid.
#
  from scipy.sparse import coo_matrix
  import numpy as np

  m = np.shape ( G )[0]
#
#  Interior points have a nonzero value in G.
#
  p = np.flatnonzero ( G )
  p_num = np.shape ( p )[0]
#
#  Make flattened version of G.
#
  Gflat = G.flatten ( )
#
#  Connect interior points to themselves with 4's.
#
  i = Gflat[p] - 1
  j = Gflat[p] - 1
  s = 4.0 * np.ones ( p_num )
#
#  Using 1-dimensional array index, the neighbors of node p are
#  p-1 (north)
#  p+m (east)
#  p+1 (south)
#  p-m (west)
#  Each of these neighbors gets a coefficient of -1.
#
  for k in [ -1, m, 1, -m ]:
    Q = Gflat[p+k]
    q = np.flatnonzero ( Q )
    q_num = np.shape ( q )[0]
    i = np.append ( i, Gflat[p[q]] - 1 )
    j = np.append ( j, Q[q] - 1 )
    s = np.append ( s, -np.ones(q_num) )
#
#  Define D as a sparse matrix.
#
  D = coo_matrix ( ( s, ( i, j ) ), shape = ( p_num, p_num ) )

  return D

def numgrid ( R, n ):

#*****************************************************************************80
#
## numgrid() numbers grid points in a two-dimensional region.
#
#  Discussion:
#
#    G = NUMGRID(R,N) numbers the points on an N-by-N grid in
#    the subregion of -1<=x<=1 and -1<=y<=1 determined by R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 August 2023
#
#  Author:
#
#    Original MATLAB version by The MathWorks, Inc.
#    This version by John Burkardt
#
#  Input:
#
#    character R: specifies the region:
#      'S' - the entire square.
#      'L' - the L-shaped domain made from 3/4 of the entire square.
#      'C' - like the 'L', but with a quarter circle in the 4-th square.
#      'D' - the unit disc.
#      'A' - an annulus.
#      'H' - a heart-shaped cardioid.
#      'B' - the exterior of a "Butterfly".
#
#    integer n: the number of rows and columns in the grid.
#
#  Output:
#
#    real G(n,n): a grid containing node numbers.
#
  import numpy as np

  if ( n < 2 ):
    raise Exception ( 'numgrid(): Invalid number of points.' )

  x = np.outer ( np.ones ( n ), np.linspace ( -1.0, 1.0, n ) )
  y = np.flipud ( np.transpose ( x ) )

  if ( R == 'S' ):
    G = (x > -1) & (x < 1) & (y > -1) & (y < 1)
  elif ( R == 'L' ):
    G = (x > -1) & (x < 1) & (y > -1) & (y < 1) & ( (x > 0) | (y > 0))
  elif ( R == 'C' ):
    G = (x > -1) & (x < 1) & (y > -1) & (y < 1) & ((x+1) ** 2 + (y+1) ** 2 > 1)
  elif ( R == 'D' ):
    G = ( x ** 2 + y ** 2 < 1 )
  elif ( R == 'A' ):
    G = ( x ** 2 + y ** 2 < 1 ) & ( x ** 2 + y ** 2 > 1/3 )
  elif ( R == 'H' ):
    RHO = 0.75
    SIGMA = 0.75
    G = ( x ** 2 + y ** 2 ) * ( x ** 2 + y ** 2 - SIGMA * y ) < RHO * x ** 2
  elif ( R == 'B' ):
    t = np.arctan2 ( y, x )
    r = np.sqrt ( x ** 2 + y ** 2 )
    G = ( r >= np.sin ( 2.0 * t ) + 0.2 * np.sin ( 8.0 * t ) ) & \
        ( x > -1 ) & ( x < 1 ) & ( y > -1 ) & ( y < 1 )
  else:

    raise Exception ( 'numgrid(): Invalid region type.' )
#
#  Convert from logical to int.
#
  k = np.nonzero ( G )
  nz = np.shape ( k )[1]
  G = 0 * G
  G[k] = list ( range ( 1, nz + 1 ) )

  return G

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
  delsq_test ( )
  timestamp ( )

