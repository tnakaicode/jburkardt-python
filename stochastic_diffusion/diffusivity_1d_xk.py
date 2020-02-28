#! /usr/bin/env python3
#
def diffusivity_1d_xk ( dc0, m, omega, n, x ):

#*****************************************************************************80
#
## DIFFUSIVITY_1D_XK evaluates a 1D stochastic diffusivity function.
#
#  Discussion:
#
#    The 1D diffusion equation has the form
#
#      - d/dx ( DC(X) Del U(X) ) = F(X)
#
#    where DC(X) is a function called the diffusivity.
#
#    In the stochastic version of the problem, the diffusivity function
#    includes the influence of stochastic parameters:
#
#      - d/dx ( DC(XOMEGA) d/dx U(X) ) = F(X).
#
#    In this function, the domain is assumed to be the unit interval [0.1].
#
#
#    For DC0 = 1 and F(X) = 0, with boundary conditions U(0:OMEGA) = 0,
#    U(1OMEGA) = 1, the exact solution is
#
#    If OMEGA ~= 0:
#
#      U(XOMEGA) = log ( 1 + OMEGA * X ) / log ( 1 + OMEGA )
#
#    If OMEGA = 0:
#
#      U(XOMEGA) = X
#
#    In the numerical experiments described in the paper, OMEGA was taken
#    to be a random variable with a Beta, or Uniform, or Gaussian or 
#    Poisson or Binomial distribution.
#
#    For the Gaussian and Poisson distributions, the positivity requirement could not
#    be guaranteed, and the experiments were simply made with a "small"
#    variance of 0.1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 December 2009
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dongbin Xiu, George Karniadakis,
#    Modeling uncertainty in steady state diffusion problems via
#    generalized polynomial chaos,
#    Computer Methods in Applied Mechanics and Engineering,
#    Volume 191, 2002, pages 4927-4948.
#
#  Parameters:
#
#    Input, real DC0, the constant term in the expansion of the 
#    diffusion coefficient.
#
#    Input, integer M, the number of stochastic parameters.
#
#    Input, real OMEGA(M), the stochastic parameters.  
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real X(N), the point where the diffusion coefficient is to 
#    be evaluated.
#
#    Output, real DC(N), the value of the diffusion coefficient at X.
#
  import numpy as np

  k = 0
  w = 1.0
  arg = np.zeros(n)

  while ( k < m ):

    if ( k < m ):
      arg = arg + omega[k] * np.sin ( w * np.pi * x )
      k = k + 1

    if ( k < m ):
      arg = arg + omega[k] * np.cos ( w * np.pi * x )    
      k = k + 1

    w = w + 1.0

  arg = np.exp ( - 0.125 ) * arg

  dc = dc0 + np.exp ( arg )

  return dc

def diffusivity_1d_xk_contour ( ):

#*****************************************************************************80
#
## diffusivity_1d_xk_contour displays contour plots of a 1D stochastic diffusivity function.
#
#  Discussion:
#
#    The diffusivity function is compute by DIFFUSIVITY_1D_XK.
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
#    Dongbin Xiu, George Karniadakis,
#    Modeling uncertainty in steady state diffusion problems via
#    generalized polynomial chaos,
#    Computer Methods in Applied Mechanics and Engineering,
#    Volume 191, 2002, pages 4927-4948.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'diffusivity_1d_xk_contour' )
  print ( '  Display the stochastic diffusivity function' )
  print ( '  defined by DIFFUSIVITY_1D_XK.' )
#
#  Set the spatial grid.
#
  n = 51
  x_min = -1.0
  x_max = +1.0
  x = np.linspace ( x_min, x_max, n )
#
#  Sample the OMEGA values.
#  Use a seed of 0 for the MATLAB random number generator.
#
  m = 5
  omega = np.random.randn ( m )
#
#  Compute the diffusivity field.
#
  dc0 = 10.0
  dc = diffusivity_1d_xk ( dc0, m, omega, n, x )
#
#  Plot the diffusivity field.
#
  plt.plot ( x, dc, linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( 'DC(X)' )
  plt.title ( 'XK Stochastic diffusivity function' )
  filename = 'diffusivity_1d_xk.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s".' % ( filename ) )

  return

def diffusivity_1d_xk_test ( ):

#*****************************************************************************80
#
## diffusivity_1d_xk_test tests diffusivity_1d_xk.
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
  print ( 'diffusivity_1d_xk_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test diffusivity_1d_xk.' )

  diffusivity_1d_xk_contour ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diffusivity_1d_xk_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  diffusivity_1d_xk_test ( )
  timestamp ( )
