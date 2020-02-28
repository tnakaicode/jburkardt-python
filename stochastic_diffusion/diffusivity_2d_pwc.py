#! /usr/bin/env python3
#
def diffusivity_2d_pwc ( h, w, a, b, c, d, omega, n, x, y ):

#*****************************************************************************80
#
## diffusivity_2d_pwc evaluates a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The 2D stochastic diffusion equation has the form
#
#      - Del ( RHO(X,Y;OMEGA) Del U(X,Y;OMEGA) ) = F(X,Y).
#
#    Here, the diffusivity RHO is assumed to be a piecewise constant function,
#    defined on rectangular grid over [A,B]x[C,D] that is H cells high
#    and W cells wide.  The parameters OMEGA(H*W) are assumed to be given 
#    positive values that are bounded away from 0.
#
#    The underlying grid is assumed to be equally spaced, so each cell
#    is (D-C)/M units high and (B-A)/N wide.
#
#       ^  ^  +-------+-------+-------+-------+
#       D  H  | (H,1) | (H,2) | ----- | (H,W) |
#       |  |  +-------+-------+-------+-------+
#             | ----- | ----- | (I,J) | ----- |
#       Y  I  +-------+-------+-------+-------+
#             | (2,1) | (2,2) | ----- | (2,W) |
#       |  |  +-------+-------+-------+-------+
#       |  |  | (1,1) | (1,2) | ----- | (1,W) |
#       C  1  +-------+-------+-------+-------+
#       |  |
#       +--+--1-------------- J --------------W->
#       +--+--A-------------- X --------------B->
#
#    Indexing is tricky, since our (X,Y) coordinate system indexing and
#    conventions for indexing an array and for ordering indices do not
#    match up.  An arbitrary choice must be made, and here we associate
#    "width" and "X" and "J", as well as "height" and "Y" and "I".
#    We start in the lower left corner, and proceed right first, and
#    then move up one row.
#
#    The following coordinate systems are available:
#
#    * cell index (I,J):  (1,1) <= (I,J) <= (H,W). 
#      I refers to "height" and J to "width".
#
#    * cell counter K:    1     <= K     <= H*W
#      Count from lower left to lower right, then
#      go up one row.
#
#    * physical cell center coordinates (XC,YC)
#      the (X,Y) coordinates of the centers of a cell
#
#    * physical coordinates (X,Y) in [A,B]x[C,D].
#      the (X,Y) coordinates of any point
#      
#    * normalized coordinates (X01,Y01) in [0,1]x[0,1].
#   
#    Transformations from one coordinate system to another:
#
#    * (I,J) --> (XC,YC)
#                X01 = (2*J-1)/2/W
#                Y01 = (2*I-1)/2/H
#                XC = A + (B-A) * X01
#                YC = C + (D-C) * Y01
#
#    * (I,J) --> K
#                K = (I-1)*W+J
#
#    * K     --> (I,J)
#                I = floor ( K - 1 ) / W ) + 1
#                J = mod ( K - 1, W ) + 1
#
#    * K     --> (XC,YC)
#                I = floor ( K - 1 ) / W ) + 1
#                J = mod ( K - 1, W ) + 1
#                X01 = (2*J-1)/2/W
#                Y01 = (2*I-1)/2/H
#                XC = A + (B-A) * X01
#                YC = C + (D-C) * Y01
#
#    * (X,Y) --> (I,J)
#                X01 = ( X - A ) / ( B - A )
#                Y01 = ( Y - C ) / ( D - C )
#                I = round ( ( 2 * h * Y01 + 1 ) / 2 );
#                J = round ( ( 2 * w * X01 + 1 ) / 2 );
#
#    * (X,Y) --> K
#                X01 = ( X - A ) / ( B - A )
#                Y01 = ( Y - C ) / ( D - C )
#                I = round ( ( 2 * h * Y01 + 1 ) / 2 );
#                J = round ( ( 2 * w * X01 + 1 ) / 2 );
#                K = (I-1)*W+J
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int H, W, specifies the number of elements.
#
#    Input, float A, B, the lower and upper limits of X.
#
#    Input, float C, D, the lower and upper limits of Y.
#
#    Input, float OMEGA(H*W), the parameters.
#
#    Input, int N, the number of evaluation points.
#
#    Input, float X(N), Y(N), the points where the diffusion coefficient is to 
#    be evaluated.
#
#    Output, float RHO(N), the value of the diffusion coefficient at each point.
#
  import numpy as np

  drat = x.shape
  n1 = drat[0]
  n2 = drat[1]

  rho = x.copy( )
  
  for ii in range ( 0, n1 ):
    for jj in range ( 0, n2 ):

      x01 = ( x[ii,jj] - a ) / ( b - a )
      y01 = ( y[ii,jj] - c ) / ( d - c )

      i = int ( np.round ( ( 2 * h * y01 - 1 ) / 2 ) )
      i = max ( i, 0 )
      i = min ( i, h - 1 )

      j = int ( np.round ( ( 2 * w * x01 - 1 ) / 2 ) )
      j = max ( j, 0 )
      j = min ( j, w - 1 )

      k = i * w + j

      rho[ii,jj] = omega[k]
 
  return rho

def diffusivity_2d_pwc_contour ( h, w, a, b, c, d ):

#*****************************************************************************80
#
## diffusivity_2d_pwc_contour displays contour plots of a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is computed by diffusivity_2d_pwc.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int H, W, the height and width of the element grid.
#
#    Input, float A, B, C, D, the lower and upper limits of X, and of Y.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import numpy as np

  print ( '' )
  print ( 'diffusivity_2d_pwc_contour' )
  print ( '  Display contour or surface plots of the stochastic' )
  print ( '  diffusivity function defined by diffusivity_2d_pwc.' )
  print ( '' )
  print ( '  Underlying grid is %d elements wide (X) and %d high (Y)' % ( w, h ) )
#
#  Set the spatial grid.
#
  nx = 101
  ny = 101

  x_1d = np.linspace ( a, b, nx )
  y_1d = np.linspace ( c, d, ny )

  X, Y = np.meshgrid ( x_1d, y_1d )
#
#  Sample OMEGA.
#
  omega = 1.0 - 0.5 * np.random.rand ( h * w )
#
#  Compute the diffusivity field, using a uniform OMEGA.
#
  n = nx * ny
  RHO = diffusivity_2d_pwc ( h, w, a, b, c, d, omega, n, X, Y );
#
#  Plot the diffusivity field as a surface plot.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, RHO, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( 'Y' )
  ax.set_ylabel ( 'X' )
  ax.set_zlabel ( 'Rho(X,Y)' )
  ax.set_title ( 'PWC Stochastic diffusivity function' )
  filename = 'diffusivity_2d_pwc.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )

  return

def diffusivity_2d_pwc_test ( ):

#*****************************************************************************80
#
## diffusivity_2d_pwc_test tests diffusivity_2d_pwc.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'diffusivity_2d_pwc_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_2d_pwc.' )

  h = 5
  w = 4
  a = - 1.0
  b = + 1.0
  c = - 1.0
  d = + 1.0

  diffusivity_2d_pwc_contour ( h, w, a, b, c, d )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_2d_pwc_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  diffusivity_2d_pwc_test ( )
  timestamp ( )
