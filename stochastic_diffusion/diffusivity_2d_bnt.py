#! /usr/bin/env python3
#
def diffusivity_2d_bnt ( dc0, omega, n, x, y ):

#*****************************************************************************80
#
## DIFFUSIVITY_2D_BNT evaluates a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The 2D diffusion equation has the form
#
#      - Del ( DC(X,Y) Del U(X,Y) ) = F(X,Y)
#
#    where DC(X,Y) is a function called the diffusivity.
#
#    In the stochastic version of the problem, the diffusivity function
#    includes the influence of stochastic parameters:
#
#      - Del ( DC(X,YOMEGA) Del U(X,YOMEGA) ) = F(X,Y).
#
#    In this function, the domain is the rectangle [-1.5,0]x[-0.4,0.8].
#
#    The four stochastic parameters OMEGA(1:4) are assumed to be independent
#    identically distributed random variables with mean value zero and 
#    variance 1.  The distribution is typically taken to be Gaussian or
#    uniform.
#
#    A collocation approach to this problem would then use the roots of
#    Hermite or Legendre polynomials.
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
#    Input, real DC0, the constant term in the expansion of the 
#    diffusion coefficient.  Take DC0 = 10.
#
#    Input, real OMEGA(4), the stochastic parameters.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), Y(N), the points where the diffusion coefficient is to 
#    be evaluated.
#
#    Output, real DC(N), the value of the diffusion coefficient at (X,Y).
#
  import numpy as np

  arg = omega[0] * np.cos ( np.pi * x ) \
      + omega[1] * np.sin ( np.pi * x ) \
      + omega[2] * np.cos ( np.pi * y ) \
      + omega[3] * np.sin ( np.pi * y )

  arg = np.exp ( - 0.125 ) * arg

  dc = dc0 + np.exp ( arg )

  return dc

def diffusivity_2d_bnt_contour ( ):

#*****************************************************************************80
#
## diffusivity_2d_bnt_contour displays contour plots of a 2D stochastic diffusivity function.
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
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import numpy as np

  print ( '' )
  print ( 'diffusivity_2d_bnt_contour' )
  print ( '  Display contour or surface plots of the stochastic' )
  print ( '  diffusivity function defined by DIFFUSIVITY_2D_BNT.' )
#
#  Set the spatial grid.
#
  nx = 151
  ny = 121

  x_1d = np.linspace ( -1.5, 0.0, nx )
  y_1d = np.linspace ( -0.4, 0.8, ny )

  X, Y = np.meshgrid ( x_1d, y_1d )
#
#  Sample OMEGA.
#
  m = 4
  omega = np.random.rand ( m )
#
#  Compute the diffusivity field, using a uniform OMEGA.
#
  dc0 = 10.0
  n = nx * ny
  DC = diffusivity_2d_bnt ( dc0, omega, n, X, Y )
#
#  Plot the diffusivity field as a surface plot.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, DC, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( 'Y' )
  ax.set_ylabel ( 'X' )
  ax.set_zlabel ( 'DC(X,Y)' )
  ax.set_title ( 'BNT Stochastic diffusivity function' )
  filename = 'diffusivity_2d_bnt.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )

  return

def diffusivity_2d_bnt_test ( ):

#*****************************************************************************80
#
## diffusivity_2d_bnt_test tests diffusivity_2d_bnt.
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
  print ( 'diffusivity_2d_bnt_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_2d_bnt.' )

  diffusivity_2d_bnt_contour ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_2d_bnt_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  diffusivity_2d_bnt_test ( )
  timestamp ( )
