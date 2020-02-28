#! /usr/bin/env python3
#
def diffusivity_2d_elman ( a, cl, dc0, m_1d, omega, n1, n2, x, y ):

#*****************************************************************************80
#
## DIFFUSIVITY_2D_ELMAN evaluates a 2D stochastic diffusivity function.
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
#    In this function, the domain is assumed to be the square [-A,+A]x[-A,+A].
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
#    Howard Elman, Darran Furnaval,
#    Solving the stochastic steady-state diffusion problem using multigrid,
#    IMA Journal on Numerical Analysis,
#    Volume 27, Number 4, 2007, pages 675-688.
#
#    Roger Ghanem, Pol Spanos,
#    Stochastic Finite Elements: A Spectral Approach,
#    Revised Edition,
#    Dover, 2003,
#    ISBN: 0486428184,
#    LC: TA347.F5.G56.
#
#  Parameters:
#
#    Input, real A, the "radius" of the square region.  The region
#    is assumed to be [-A,+A]x[-A,+A].
#    0 < A.
#
#    Input, real CL, the correlation length.
#    0 < CL.
#
#    Input, real DC0, the constant term in the expansion of the 
#    diffusion coefficient.  Take DC0 = 10.
#
#    Input, integr M_1D, the first and second dimensions of the stochastic
#    parameter array.
#
#    Input, real OMEGA(M_1D*M_1D), the stochastic parameters.
#
#    Input, integer N1, N2, the dimensions of the X and Y arrays.
#
#    Input, real X(N1,N2), Y(N1,N2), the points where the diffusion coefficient is to 
#    be evaluated.
#
#    Output, real DC(N1,N2), the value of the diffusion coefficient at X.
#
  import numpy as np
#
#  Compute THETA.
#
  theta_1d = theta_solve ( a, cl, m_1d )
#
#  Compute LAMBDA_1D.
#
  lambda_1d = 2.0 * cl / ( 1.0 + cl ** 2 * theta_1d ** 2 )
#
#  Compute C_1DX(1:M1D)  and C_1DY(1:M1D) at (X,Y).
#
  c_1dx = np.zeros ( [ m_1d, n1, n2 ] )
  c_1dy = np.zeros ( [ m_1d, n1, n2 ] )

  k = -1

  while ( True ):

    k = k + 1

    if ( m_1d <= k ):
      break

    c_1dx[k,0:n1,0:n2] = np.cos ( theta_1d[k] * a * x[0:n1,0:n2] ) \
      / np.sqrt ( a + np.sin ( 2.0 * theta_1d[k] * a ) / ( 2.0 * theta_1d[k] ) )
    c_1dy[k,0:n1,0:n2] = np.cos ( theta_1d[k] * a * y[0:n1,0:n2] ) \
      / np.sqrt ( a + np.sin ( 2.0 * theta_1d[k] * a ) / ( 2.0 * theta_1d[k] ) )

    k = k + 1

    if ( m_1d <= k ):
      break

    c_1dx[k,0:n1,0:n2] = np.sin ( theta_1d[k] * a * x[0:n1,0:n2] ) \
      / np.sqrt ( a - np.sin ( 2.0 * theta_1d[k] * a ) / ( 2.0 * theta_1d[k] ) )
    c_1dy[k,0:n1,0:n2] = np.sin ( theta_1d[k] * a * y[0:n1,0:n2] ) \
      / np.sqrt ( a - np.sin ( 2.0 * theta_1d[k] * a ) / ( 2.0 * theta_1d[k] ) )
#
#  Evaluate the diffusion coefficient DC at (X,Y).
#  This nonsense of fussy array shapes really frustrates me!
#
  k = 0
  dc3 = dc0 * np.ones ( [ 1, n1, n2 ] )
  for j in range ( 0, m_1d ):
    for i in range ( 0, m_1d ):
      dc3[0,0:n1,0:n2] = dc3[0,0:n1,0:n2] + np.sqrt ( lambda_1d[i] * lambda_1d[j] ) \
        * c_1dx[i,0:n1,0:n2] * c_1dy[j,0:n1,0:n2] * omega[k]
      k = k + 1

  dc = np.zeros ( [ n1, n2 ] )
  dc[0:n1,0:n2] = dc3[0,0:n1,0:n2]

  return dc

def theta_solve ( a, cl, m ):

#*****************************************************************************80
#
## THETA_SOLVE solves a pair of transcendental equations.
#
#  Discussion:
#
#    The vector THETA returned by this function is needed in order to define
#    the terms in a Karhunen-Loeve expansion of a diffusion coefficient.
#
#    The two equations are:
#
#      1/CL - THETA * TAN ( A * THETA ) = 0
#      THETA - 1/CL * TAN ( A * THETA ) = 0
#
#    A and CL are taken to be positive.  Over each open interval 
#
#      ( n - 1/2 pi, n + 1/2 pi ) / A, for N = 0, 1, ...
#
#    the function TAN ( A * THETA ) monotonically rises from -oo to +00 
#    therefore, it can be shown that there is one root of each equation 
#    in every interval of this form.  Moreover, because of the positivity
#    of A and CL, we can restrict our search to the interval 
#
#      [ n pi, n + 1/2 pi ) / A, for N = 0, 1, ...
#
#    This function computes K such roots, starting in the first interval,
#    finding those two roots, moving to the next interval, and so on, until
#    the requested number of roots have been found.  Odd index roots will
#    correspond to the first equation, and even index roots to the second.
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
#    Howard Elman, Darran Furnival,
#    Solving the Stochastic Steady-State Diffusion Problem Using Multigrid,
#    University of Maryland Department of Computer Science,
#    Technical Report TR-4786.
#
#  Parameters:
#
#    Input, real A, the "radius" of the domain, D = (-A,A)x(-A,A).
#    0 < A.
#
#    Input, real CL, the correlation length.
#    0 < CL.
#
#    Input, integer M, the number of values to compute.
#
#    Output, real THETA(M), the values of Theta.
#
  import numpy as np

  eps = np.finfo(float).eps

  k = -1
  theta = np.zeros ( m )
#
#  [ XA_INIT, XB_INIT] = [ n * pi, n+1/2 pi ] / a, n = 0, 1, 2, ...
#
  xa_init = 0.0
  xb_init = ( np.pi / 2.0 ) / a

  while ( True ):
#
#  Seek root of equation 1 in interval.
#
    k = k + 1

    if ( m <= k ):
      break

    xa = xa_init
    fa = 1.0 / cl - xa * np.tan ( a * xa )
    ftol = eps * ( abs ( fa ) + 1.0 )
    xb = xb_init
    fb = - fa
    fc = fa
    bmatol = 100.0 * eps * ( abs ( xa ) + abs ( xb ) )

    while ( bmatol < xb - xa ):

      xc = ( xa + xb ) / 2.0
      fc = 1.0 / cl - xc * np.tan ( a * xc )

      if ( abs ( fc ) <= ftol ):
        break
      elif ( 0 < fc ):
        xa = xc
      else:
        xb = xc

    theta[k] = xc
#
#  Seek root of equation 2 in interval.
#
    k = k + 1
    if ( m <= k ):
      break
#
#  In the first interval, we need to skip the zero root of equation 2.
#
    if ( k == 1 ):

      k = k - 1

    else:

      xa = xa_init
      fa = xa - np.tan ( a * xa ) / cl
      ftol = eps * ( abs ( fa ) + 1.0 )
      xb = xb_init
      fb = - fa

      while ( bmatol < xb - xa ):

        xc = ( xa + xb ) / 2.0
        fc = xc - np.tan ( a * xc ) / cl

        if ( abs ( fc ) <= ftol ):
          break
        elif ( 0.0 < fc ):
          xa = xc
        else:
          xb = xc

      theta[k] = xc
#
#  Advance the interval.
#
    xa_init = xa_init + np.pi / a
    xb_init = xb_init + np.pi / a

  return theta

def diffusivity_2d_elman_contour ( ):

#*****************************************************************************80
#
## diffusivity_2d_elman_contour displays a contour plot of a 2D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is compute by DIFFUSIVITY_2D_ELMAN.
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
#    Howard Elman, Darran Furnaval,
#    Solving the stochastic steady-state diffusion problem using multigrid,
#    IMA Journal on Numerical Analysis,
#    Volume 27, Number 4, 2007, pages 675-688.
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm
  import numpy as np

  print ( '' )
  print ( 'diffusivity_2d_elman_contour' )
  print ( '  Display contour or surface plots of the stochastic' )
  print ( '  diffusivity function defined by DIFFUSIVITY_2D_ELMAN.' )
#
#  Specify the X and Y evaluation points.
#
  nx = 51
  a = 1.0
  xvec = np.linspace ( -a, +a, nx )
  yvec = np.linspace ( -a, +a, nx )

  X, Y = np.meshgrid ( xvec, yvec )
#
#  Sample OMEGA.
#
  m_1d = 5
  msq = m_1d * m_1d
  omega = np.random.randn ( msq )
#
#  Compute the diffusivity field.
#
  cl = 0.1
  ac0 = 10.0
  A = diffusivity_2d_elman ( a, cl, ac0, m_1d, omega, nx, nx, X, Y )
#
#  Make a surface plot.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( X, Y, A, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_xlabel ( 'Y' )
  ax.set_ylabel ( 'X' )
  ax.set_zlabel ( 'DC(X,Y)' )
  ax.set_title ( 'ELMAN Stochastic diffusivity function' )
  filename = 'diffusivity_2d_elman.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )

  return

def diffusivity_2d_elman_test ( ):

#*****************************************************************************80
#
## diffusivity_2d_elman_test tests diffusivity_2d_elman.
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
  print ( 'diffusivity_2d_elman_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_2d_elman.' )

  diffusivity_2d_elman_contour ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_2d_elman_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  diffusivity_2d_elman_test ( )
  timestamp ( )

