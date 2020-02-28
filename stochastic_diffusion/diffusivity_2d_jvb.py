#! /usr/bin/env python3
#
def diffusivity_2d_jvb ( a0, m, omega, n, x, y ):

#*****************************************************************************80
#
## diffusivity_2d_jvb evaluates a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The 2D stochastic diffusion equation has the form
#
#      - Del ( A(X,Y;OMEGA) Del U(X,Y;OMEGA) ) = F(X,Y).
#
#    The stochastic parameters OMEGA(1:4*M) are assumed to be independent
#    identically distributed random variables with mean value zero and 
#    variance 1.  The distribution is typically taken to be Gaussian or
#    uniform.
#
#    For physical and mathematical reasons, the diffusivity function 
#    A(X,Y;OMEGA) must be positive.  Our random KL expansion can guarantee
#    this by using an exponential format:
#
#      A(X,Y;OMEGA) = A0 + exp ( sum(j=1:4*m) OMEGA(J) * PSI(J)(X,Y) )
#
#    This function generalizes the 4-term expansion in diffusivity_2d_bnt,
#    used by Babuska, Nobile, Tempone, to a 4*M term expansion.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ivo Babuska, Fabio Nobile, Raul Tempone,
#    A stochastic collocation method for elliptic partial differential equations
#    with random input data,
#    SIAM Journal on Numerical Analysis,
#    Volume 45, Number 3, 2007, pages 1005-1034.
#
#  Parameters:
#
#    Input, real A0, the constant term in the expansion.
#
#    Input, integer M, controls the number of values OMEGA.
#    0 <= M.
#
#    Input, real OMEGA(4*M), the stochastic parameters.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), Y(N), the points where the diffusion coefficient is to 
#    be evaluated.
#
#    Output, real A(N), the value of the diffusion coefficient at (X,Y).
#
  import numpy as np

  ma, na = x.shape
  arg = np.zeros ( [ ma, na ] )
  
  for j in range ( 0, m ):
#
#  Reduce strength of higher order terms.
#
    jsq = 1.0 / ( float ( j + 1 ) ) ** 2;

    arg = arg + jsq * ( \
        omega[4* j ] * np.cos ( ( j + 1 ) * np.pi * x ) \
      + omega[4*j+1] * np.sin ( ( j + 1 ) * np.pi * x ) \
      + omega[4*j+2] * np.cos ( ( j + 1 ) * np.pi * y ) \
      + omega[4*j+3] * np.sin ( ( j + 1 ) * np.pi * y ) )
#
#  Add the (positive) terms.
#
  a = a0 + np.exp ( arg );

  return a

def diffusivity_2d_jvb_contour ( m ):

#*****************************************************************************80
#
## diffusivity_2d_jvb_contour displays contour plots of a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is compute by DIFFUSIVITY_2D_BNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ivo Babuska, Fabio Nobile, Raul Tempone,
#    A stochastic collocation method for elliptic partial differential equations
#    with random input data,
#    SIAM Journal on Numerical Analysis,
#    Volume 45, Number 3, 2007, pages 1005-1034.
#
#  Parameters:
#
#    Input, integer M, controls the number of random coefficients, which
#    will be 4*M.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import numpy as np

  print ( '' )
  print ( 'diffusivity_2d_jvb_contour' )
  print ( '  Display contour or surface plots of the stochastic' )
  print ( '  diffusivity function defined by diffusivity_2d_jvb.' )
#
#  Set the spatial grid.
#
  nx = 101
  ny = 101

  x_1d = np.linspace ( -1.0, 0.0, nx )
  y_1d = np.linspace ( -1.0, 1.0, ny )

  X, Y = np.meshgrid ( x_1d, y_1d )
#
#  Compute the diffusivity field, using a uniform OMEGA.
#
  a0 = 2.0
  omega = -1.0 + 2.0 * np.random.rand ( 4 * m )
  n = nx * ny
  A = diffusivity_2d_jvb ( a0, m, omega, n, X, Y )
#
#  Plot the diffusivity field as a surface plot.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, A, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( 'Y' )
  ax.set_ylabel ( 'X' )
  ax.set_zlabel ( 'A(X,Y)' )
  ax.set_title ( 'JVB Stochastic diffusivity function' )
  filename = 'diffusivity_2d_jvb.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )

  return

def diffusivity_2d_jvb_test ( ):

#*****************************************************************************80
#
## diffusivity_2d_jvb_test tests diffusivity_2d_jvb.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2019
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
  print ( 'diffusivity_2d_jvb_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_2d_jvb.' )

  m = 3
  diffusivity_2d_jvb_contour ( m )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_2d_jvb_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  diffusivity_2d_jvb_test ( )
  timestamp ( )
