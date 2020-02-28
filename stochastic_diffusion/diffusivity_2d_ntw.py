#! /usr/bin/env python3
#
def diffusivity_2d_ntw ( cl, a0, m, omega, n, x, y ):

#*****************************************************************************80
#
## diffusivity_2d_ntw evaluates a 2D stochastic diffusivity function.
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
#    In this function, the domain is the rectangle [0,D]x[0,D] where D = 1.
#
#    Note that in this problem the diffusivity has a one-dimensional
#    spatial dependence on X, but not on Y!
#
#    The random variables OMEGA are independent, have zero mean and unit
#    variance, and are uniformly distributed in [-sqrt(3),+sqrt(3)].
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
#    Xiang Ma, Nicholas Zabaras,
#    An adaptive hierarchical sparse grid collocation algorithm for the solution
#    of stochastic differential equations,
#    Journal of Computational Physics,
#    Volume 228, pages 3084-3113, 2009.
#
#    Fabio Nobile, Raul Tempone, Clayton Webster,
#    A Sparse Grid Stochastic Collocation Method for Partial Differential
#    Equations with Random Input Data,
#    SIAM Journal on Numerical Analysis,
#    Volume 46, Number 5, 2008, pages 2309-2345.
#
#  Parameters:
#
#    Input, real CL, the desired physical correlation length for the
#    coefficient.
#
#    Input, real A0, the constant term in the expansion of the 
#    diffusion coefficient.  Take A0 = 0.5.
#
#    Input, integer M, the number of terms in the expansion.
#
#    Input, real OMEGA(M), the stochastic parameters.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), Y(N), the points where the diffusion coefficient is to 
#    be evaluated.
#
#    Output, real A(N), the value of the diffusion coefficient at (X,Y).
#
  import numpy as np

  d = 1.0
  lp = max ( d, 2.0 * cl )
  l = cl / lp

  dc_arg = 1.0 + omega[0] * np.sqrt ( np.sqrt ( np.pi ) * l / 2.0 )

  for i in range ( 2, m + 1 ):

    zeta_arg = - ( np.floor ( i / 2 ) * np.pi * l ) ** 2 / 8.0
    zeta = np.sqrt ( np.sqrt ( np.pi ) * l ) * np.exp ( zeta_arg )

    if ( np.mod ( i, 2 ) == 0 ):
      phi = np.sin ( np.floor ( i / 2 ) * np.pi * x / lp )
    else:
      phi = np.cos ( np.floor ( i / 2 ) * np.pi * x / lp )

    dc_arg = dc_arg + zeta * phi * omega[i-1]

  A = a0 + np.exp ( dc_arg )

  return A

def diffusivity_2d_ntw_contour ( ):

#*****************************************************************************80
#
## diffusivity_2d_ntw_contour displays a contour plot of a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is compute by diffusivity_2d_ntw.
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
#    Fabio Nobile, Raul Tempone, Clayton Webster,
#    A Sparse Grid Stochastic Collocation Method for Partial Differential
#    Equations with Random Input Data,
#    SIAM Journal on Numerical Analysis,
#    Volume 46, Number 5, 2008, pages 2309-2345.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import numpy as np

  print ( '' )
  print ( 'diffusivity_2d_ntw_contour' )
  print ( '  Display contour or surface plots of the stochastic' )
  print ( '  diffusivity function defined by diffusivity_2d_ntw.' )
#
#  Set the spatial grid.
#
  nx = 101
  ny = 101
  xvec = np.linspace ( 0.0, 1.0, nx )
  yvec = np.linspace ( 0.0, 1.0, ny )

  X, Y = np.meshgrid ( xvec, yvec )
#
#  Evaluate the diffusivity field.
#
  cl = 0.1
  a0 = 0.5
  m = 21
  omega = np.random.rand ( m )
  omega = ( 1.0 - omega ) * ( - np.sqrt ( 3.0 ) ) \
        +         omega   *     np.sqrt ( 3.0 )
  n = nx * ny

  A = diffusivity_2d_ntw ( cl, a0, m, omega, n, X, Y )
#
#  Make a surface plot of the diffusivity coefficient.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, A, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( 'Y' )
  ax.set_ylabel ( 'X' )
  ax.set_zlabel ( 'DC(X,Y)' )
  ax.set_title ( 'NTW Stochastic diffusivity function' )
  filename = 'diffusivity_2d_ntw.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )

  return

def diffusivity_2d_ntw_test ( ):

#*****************************************************************************80
#
## diffusivity_2d_ntw_test tests diffusivity_2d_ntw.
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
  print ( 'diffusivity_2d_ntw_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_2d_ntw.' )

  diffusivity_2d_ntw_contour ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_2d_ntw_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  diffusivity_2d_ntw_test ( )
  timestamp ( )

