#! /usr/bin/env python3
#
def correlation_test ( ):

#*****************************************************************************80
#
## correlation_test() tests correlation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
 
  print ( '' )
  print ( 'correlation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test correlation().' )

  correlation_test01 ( )
  correlation_test02 ( )
  correlation_test03 ( )
  correlation_test04 ( )
  correlation_test05 ( )
  correlation_test06 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'correlation_test():' )
  print ( '  Normal end of execution.' )

  return

def correlation_test01 ( ):

#*****************************************************************************80
#
## correlation_test01() plots the correlation functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'correlation_test01()' )
  print ( '  Plot correlation functions.' )
#
#  besselj
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 8.0, 8.0, n )
  c = correlation_besselj ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 8.0, 8.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Bessel J correlation function' )
  filename = 'besselj_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  besselk
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 4.0, 4.0, n )
  c = correlation_besselk ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 4.0, 4.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Bessel K correlation function' )
  filename = 'besselk_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  circular
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  c = correlation_circular ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Circular correlation function' )
  filename =  'correlation_circular_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  constant
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  c = correlation_constant ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 4 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Constant correlation function' )
  filename = 'constant_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  cubic
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  c = correlation_cubic ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Cubic correlation function' )
  filename = 'cubic_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  damped cosine
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 6.0, 6.0, n )
  c = correlation_damped_cosine ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 6.0, 6.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Damped cosine correlation function' )
  filename = 'damped_cosine_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  damped sine
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 12.0, 12.0, n )
  c = correlation_damped_sine ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 12.0, 12.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Damped sine correlation function' )
  filename = 'damped_sine_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  exponential
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  c = correlation_exponential ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Exponential correlation function' )
  filename = 'exponential_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  gaussian
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  c = correlation_gaussian ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Gaussian correlation function' )
  filename = 'gaussian_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  hole
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  c = correlation_hole ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Hole correlation function' )
  filename = 'hole_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  linear
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  c = correlation_linear ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Linear correlation function' )
  filename = 'linear_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  matern, nu = 2.5
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  nu = 2.5
  c = correlation_matern ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Matern correlation function (NU=2.5)' )
  filename = 'matern_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  pentaspherical
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  c = correlation_pentaspherical ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Pentaspherical correlation function' )
  filename = 'pentaspherical_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  power, e = 2.0
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  e = 2.0
  c = correlation_power ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Power correlation function (E=2.0)' )
  filename = 'power_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  rational quadratic
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 4.0, 4.0, n )
  c = correlation_rational_quadratic ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 4.0, 4.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Rational quadratic correlation function' )
  filename = 'rational_quadratic_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  spherical
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  c = correlation_spherical ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Spherical correlation function' )
  filename = 'spherical_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  white noise
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( - 2.0, 2.0, n )
  c = correlation_white_noise ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 3 )
  plt.plot ( [ - 2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'White noise correlation function' )
  filename = 'white_noise_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def correlation_test02 ( ):

#*****************************************************************************80
#
## correlation_test02() plots sample paths with SAMPLE_PATHS_CHOLESKY/EIGEN/FFT.
#
#  Discussion:
#
#    Most paths will be blue, but make the LAST one red so that there will
#    always be one distinguished path that is easy to follow.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'correlation_test02()' )
  print ( '  sample_paths_cholesky() generates sample paths from the' )
  print ( '  correlation matrix, factored using the Cholesky factor.' )
  print ( '  It requires that the correlation matrix is nonnegative definite.' )
  print ( '' )
  print ( '  sample_paths_eigen() generates sample paths from the' )
  print ( '  correlation matrix, factored using the eigen factorization.' )
  print ( '  If the correlation matrix is not nonnegative definite,' )
  print ( '  we simply suppress negative eigenvalues.' )
  print ( '' )
  print ( '  SAMPLE_PATHS_FFT generates sample paths from the' )
  print ( '  correlation matrix, factored using the FFT factorization' )
  print ( '  of the correlation matrix after embedding in a circulant.' )
  print ( '' )
#
#  besselj
#  nonpositive eigenvalues observed.
#
# plt.clf ( )
# n = 1001
# n2 = 3
# rhomax = 10.0
# rho = np.linspace ( 0.0, rhomax, n )
# x = sample_paths_eigen ( n, n2, rhomax, 1.0, correlation_besselj )
# plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
# plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
# plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
# plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
# plt.grid ( True )
# plt.xlabel ( '<-- Distance -->' )
# plt.title ( 'Bessel J sample paths' )
# filename = 'besselj_paths.png'
# plt.savefig ( filename )
# print ( '  Graphics saved as "' + filename + '"' )
#
#  besselk
#
  plt.clf ( )
  n = 1001
  n2 = 3
  rhomax = 10.0
  rho = np.linspace ( 0.0, rhomax, n )
  x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_besselk )
  plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
  plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
  plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
  plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Bessel K sample paths' )
  filename = 'besselk_paths.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  circular
#
  plt.clf ( )
  n = 1001
  n2 = 3
  rhomax = 10.0
  rho = np.linspace ( 0.0, rhomax, n )
  x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_circular )
  plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
  plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
  plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
  plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Circular sample paths' )
  filename = 'circular_paths.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  constant
#  nonpositive eigenvalues observed
#
# plt.clf ( )
# n = 1001
# n2 = 3
# rhomax = 10.0
# rho = np.linspace ( 0.0, rhomax, n )
# x = sample_paths_eigen ( n, n2, rhomax, 1.0, correlation_constant )
# plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
# plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
# plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
# plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
# plt.grid ( True )
# plt.xlabel ( '<-- Distance -->' )
# plt.title ( 'Constant sample paths' )
# filename = 'constant_paths.png'
# plt.savefig ( filename )
# print ( '  Graphics saved as "' + filename + '"' )
#
#  cubic
#  ? Not positive definite?
#
# plt.clf ( )
# n = 1001
# n2 = 3
# rhomax = 10.0
# rho = np.linspace ( 0.0, rhomax, n )
# x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_cubic )
# plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
# plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
# plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
# plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
# plt.grid ( True )
# plt.xlabel ( '<-- Distance -->' )
# plt.title ( 'Cubic sample paths' )
# filename = 'cubic_paths.png'
# plt.savefig ( filename )
# print ( '  Graphics saved as "' + filename + '"' )
#
#  damped cosine
#
  plt.clf ( )
  n = 1001
  n2 = 3
  rhomax = 10.0
  rho = np.linspace ( 0.0, rhomax, n )
  x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_damped_cosine )
  plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
  plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
  plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
  plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Damped cosine sample paths' )
  filename = 'damped_cosine_paths.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  damped sine
#  nonpositive eigenvalues observed
#
# plt.clf ( )
# n = 1001
# n2 = 3
# rhomax = 10.0
# rho = np.linspace ( 0.0, rhomax, n )
# x = sample_paths_eigen ( n, n2, rhomax, 1.0, correlation_damped_sine )
# plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
# plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
# plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
# plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
# plt.grid ( True )
# plt.xlabel ( '<-- Distance -->' )
# plt.title ( 'Damped sine sample paths' )
# filename = 'damped_sine_paths.png'
# plt.savefig ( filename )
# print ( '  Graphics saved as "' + filename + '"' )
#
#  exponential
#  Let's try the FFT approach instead of Cholesky.
#
# plt.clf ( )
# n = 1001
# n2 = 3
# rhomax = 10.0
# rho = np.linspace ( 0.0, rhomax, n )
# x = sample_paths_fft ( n, n2, rhomax, 1.0, correlation_exponential )
# plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
# plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
# plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
# plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
# plt.grid ( True )
# plt.xlabel ( '<-- Distance -->' )
# plt.title ( 'Exponential sample paths' )
# filename = 'exponential_paths.png'
# plt.savefig ( filename )
# print ( '  Graphics saved as "' + filename + '"' )
#
#  gaussian
#  nonpositive eigenvalues observed
#
# plt.clf ( )
# n = 1001
# n2 = 3
# rhomax = 10.0
# rho = np.linspace ( 0.0, rhomax, n )
# x = sample_paths_eigen ( n, n2, rhomax, 1.0, correlation_gaussian )
# plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
# plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
# plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
# plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
# plt.grid ( True )
# plt.xlabel ( '<-- Distance -->' )
# plt.title ( 'Gaussian sample paths' )
# filename = 'gaussian_paths.png'
# plt.savefig ( filename )
# print ( '  Graphics saved as "' + filename + '"' )
#
#  hole
#
  plt.clf ( )
  n = 1001
  n2 = 3
  rhomax = 10.0
  rho = np.linspace ( 0.0, rhomax, n )
  x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_hole )
  plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
  plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
  plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
  plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Hole sample paths' )
  filename = 'hole_paths.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  linear
#
  plt.clf ( )
  n = 1001
  n2 = 3
  rhomax = 10.0
  rho = np.linspace ( 0.0, rhomax, n )
  x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_linear )
  plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
  plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
  plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
  plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Linear sample paths' )
  filename = 'linear_paths.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  matern ( nu = 2.5 )
#
  plt.clf ( )
  n = 1001
  n2 = 3
  rhomax = 10.0
  rho = np.linspace ( 0.0, rhomax, n )
  nu = 2.5
  x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_matern )
  plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
  plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
  plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
  plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Matern (NU=2.5) sample paths' )
  filename = 'matern_paths.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  pentaspherical
#  Not positive definite?
#
# plt.clf ( )
# n = 1001
# n2 = 3
# rhomax = 10.0
# rho = np.linspace ( 0.0, rhomax, n )
# x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_pentaspherical )
# plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
# plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
# plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
# plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
# plt.grid ( True )
# plt.xlabel ( '<-- Distance -->' )
# plt.title ( 'Pentaspherical sample paths' )
# filename = 'pentaspherical_paths.png'
# plt.savefig ( filename )
# print ( '  Graphics saved as "' + filename + '"' )
#
#  power ( e = 2.0 )
#  ? not positive definite ?
#
# plt.clf ( )
# n = 1001
# n2 = 3
# rhomax = 10.0
# rho = np.linspace ( 0.0, rhomax, n )
# nu = 2.5
# x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_power )
# plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
# plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
# plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
# plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
# plt.grid ( True )
# plt.xlabel ( '<-- Distance -->' )
# plt.title ( 'Power (E=2.0) sample paths' )
# filename = 'power_paths.png'
# plt.savefig ( filename )
# print ( '  Graphics saved as "' + filename + '"' )
#
#  rational quadratic
#  nonpositive eigenvalues observed
#
# plt.clf ( )
# n = 1001
# n2 = 3
# rhomax = 10.0
# rho = np.linspace ( 0.0, rhomax, n )
# x = sample_paths_eigen ( n, n2, rhomax, 1.0, correlation_rational_quadratic )
# plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
# plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
# plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
# plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
# plt.grid ( True )
# plt.xlabel ( '<-- Distance -->' )
# plt.title ( 'Rational quadratic sample paths' )
# filename = 'rational_quadratic_paths.png'
# plt.savefig ( filename )
# print ( '  Graphics saved as "' + filename + '"' )
#
#  spherical
#  ? Not positive definite.
#
# plt.clf ( )
# n = 1001
# n2 = 3
# rhomax = 10.0
# rho = np.linspace ( 0.0, rhomax, n )
# x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_spherical )
# plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
# plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
# plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
# plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
# plt.grid ( True )
# plt.xlabel ( '<-- Distance -->' )
# plt.title ( 'Spherical sample paths' )
# filename = 'spherical_paths.png'
# plt.savefig ( filename )
# print ( '  Graphics saved as "' + filename + '"' )
#
#  white noise
#
  plt.clf ( )
  n = 1001
  n2 = 3
  rhomax = 10.0
  rho = np.linspace ( 0.0, rhomax, n )
  x = sample_paths_cholesky ( n, n2, rhomax, 1.0, correlation_white_noise )
  plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
  plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
  plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
  plt.plot ( [ 0.0, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'White noise sample paths' )
  filename = 'white_noise_paths.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def correlation_test03 ( ):

#*****************************************************************************80
#
## correlation_test03() plots a correlation function for several values of RH00.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'correlation_test03():' )
  print ( '  Make plots of correlation functions.' )
  print ( '' )
#
#  besselj
#
  plt.clf ( )
  n = 101
  rho0 = np.array ( [ 1.0, 1.5, 2.0, 4.0, 8.0 ] )
  rho = np.linspace ( -8.0, 8.0, n )
  for rho0i in rho0:
    c = correlation_besselj ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )

  plt.plot ( [ -8.0, 8.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Bessel J, RHO0 = 1, 1.5, 2, 4, 8' )
  plt.axis ( [-8.0, 8.0, -1.0, +1.0] )
  filename = 'besselj_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  besselk
#
  plt.clf ( )
  n = 101
  rho0 = [ 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -4.0, 4.0, n )
  for rho0i in rho0:
    c = correlation_besselk ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -4.0, 4.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Bessel K correlation function, RHO0 = 1, 1.5, 2, 4, 8' )
  plt.axis ( [-4.0, 4.0, -1.0, +1.0] )
  filename = 'besselk_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  circular
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  for rho0i in rho0:
    c = correlation_circular ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0 ], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Circular correlation function, RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [-2.0, 2.0, -1.0, +1.0] )
  filename = 'circular_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  constant
#  Pointless to make multiple plots for this one.
#
  plt.clf ( )
  n = 101
  rho0 = 1.0
  rho = np.linspace ( -2.0, 2.0, n )
  c = correlation_constant ( n, rho, rho0 )
  plt.plot ( rho, c, linewidth = 4 )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Constant correlation function, RHO0 = 1' )
  plt.axis ( [ -2.0, 2.0, -1.0, +1.0] )
  filename = 'constant_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  cubic
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  for rho0i in rho0:
    c = correlation_cubic ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Cubic correlation function, RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [ -2.0, 2.0, -1.0, +1.0] )
  filename = 'cubic_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  damped_cosine
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -6.0, 6.0, n )
  for rho0i in rho0:
    c = correlation_damped_cosine ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -6.0, 6.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Damped cosine correlation function, RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [ -6.0, 6.0, -1.0, +1.0] )
  filename = 'damped_cosine_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  damped_sine
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -12.0, 12.0, n )
  for rho0i in rho0:
    c = correlation_damped_sine ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -12.0, 12.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Damped sine correlation function, RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [ -12.0, 12.0, -1.0, +1.0] )
  filename = 'damped_sine_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  exponential
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.25, 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  for rho0i in rho0:
    c = correlation_exponential ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Exponential correlation function, RHO0 = 0.25, 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [ -2.0, 2.0, -1.0, +1.0] )
  filename = 'exponential_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  gaussian
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.25, 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  for rho0i in rho0:
    c = correlation_gaussian ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Gaussian correlation function, RHO0 = 0.25, 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [-2.0, 2.0, -1.0, +1.0] )
  filename = 'gaussian_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  hole
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.25, 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  for rho0i in rho0:
    c = correlation_hole ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Hole correlation function, RHO0 = 0.25, 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [-2.0, 2.0, -1.0, +1.0] )
  filename = 'hole_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  linear
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  for rho0i in rho0:
    c = correlation_linear ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Linear correlation function, RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [-2.0, 2.0, -1.0, +1.0] )
  filename = 'linear_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  matern, nu = 2.5
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  nu = 2.5
  for rho0i in rho0:
    c = correlation_matern ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Matern correlation function (NU=2.5), RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [-2.0, 2.0, -1.0, +1.0] )
  filename = 'matern_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  pentaspherical
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  for rho0i in rho0:
    c = correlation_pentaspherical ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Pentaspherical correlation function, RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [ -2.0, 2.0, -1.0, +1.0] )
  filename = 'pentaspherical_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  power, e = 2.0
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  e = 2.0
  for rho0i in rho0:
    c = correlation_power ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'power correlation function (E=20), RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [-2.0, 2.0, -1.0, +1.0] )
  filename = 'power_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  rational quadratic
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -4.0, 4.0, n )
  for rho0i in rho0:
    c = correlation_rational_quadratic ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -4.0, 4.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Rational quadratic correlation function, RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [ -4.0, 4.0, -1.0, +1.0] )
  filename = 'rational_quadratic_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  spherical
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  for rho0i in rho0:
    c = correlation_spherical ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Spherical correlation function, RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [ -2.0, 2.0, -1.0, +1.0] )
  filename = 'spherical_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  white_noise
#
  plt.clf ( )
  n = 101
  rho0 = [ 0.5, 1.0, 1.5, 2.0, 4.0, 8.0 ]
  rho = np.linspace ( -2.0, 2.0, n )
  for rho0i in rho0:
    c = correlation_white_noise ( n, rho, rho0i )
    if ( rho0i == 1.0 ):
      plt.plot ( rho, c, linewidth = 3, color = 'r' )
    else:
      plt.plot ( rho, c, linewidth = 3, color = 'b' )
  plt.plot ( [ -2.0, 2.0], [0.0, 0.0], linewidth = 3, color = 'k' )
  plt.grid ( True )
  plt.ylabel ( '<-- Correlation Strength -->' )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'White noise correlation function, RHO0 = 0.5, 1, 1.5, 2, 4, 8' )
  plt.axis ( [-2.0, 2.0, -1.0, +1.0] )
  filename = 'white_noise_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def correlation_test04 ( ):

#*****************************************************************************80
#
## correlation_test04() converts between covariance and correlation matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 'correlation_test04():' )
  print ( '  Convert between a correlation and a covariance matrix.' )

  n = 5
  K = minij ( n, n )
  print ( '' )
  print ( '  Covariance matrix K:' )
  pprint.pprint ( K )

  C, sigma = covariance_to_correlation ( n, K )
  print ( '' )
  print ( '  Correlation matrix C:' )
  pprint.pprint ( C )
  print ( '' )
  print ( '  Variances sigma:' )
  pprint.pprint ( sigma )

  K2 = correlation_to_covariance ( n, C, sigma )
  print ( '' )
  print ( '  Recovered covariance matrix K2:' )
  pprint.pprint ( K2 )

  return

def correlation_test05 ( ):

#*****************************************************************************80
#
## correlation_test05() calls correlation_brownian_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'correlation_test05():' )
  print ( '  correlation_brownian_display() displays the Brownian correlation' )

  correlation_brownian_display ( )

  filename = 'correlation_brownian_plots.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def correlation_test06 ( ):

#*****************************************************************************80
#
## correlation_test06() plots sample paths with sample_paths2_cholesky/eigen/fft.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'correlation_test06():' )
  print ( '  For non-stationary correlation functions:' )
  print ( '' )
  print ( '  sample_paths2_cholesky() generates sample paths from the' )
  print ( '  correlation matrix, factored using the Cholesky factor.' )
  print ( '  It requires that the correlation matrix is nonnegative definite.' )
  print ( '' )
  print ( '  sample_paths2_eigen() generates sample paths from the' )
  print ( '  correlation matrix, factored using the eigen factorization.' )
  print ( '  If the correlation matrix is not nonnegative definite,' )
  print ( '  we simply suppress negative eigenvalues.' )
  print ( '' )
  print ( '  sample_paths2_fft() generates sample paths from the' )
  print ( '  correlation matrix, factored using the FFT factorization' )
  print ( '  of the correlation matrix after embedding in a circulant.' )
  print ( '' )
#
#  brownian
#
  n = 1001
  n2 = 3
  rhomin = 0.0
  rhomax = 10.0
  rho0 = 1.0
  x = sample_paths2_cholesky ( n, n2, rhomin, rhomax, rho0, correlation_brownian )

  rho = np.linspace ( rhomin, rhomax, n )

  plt.clf ( )
  plt.plot ( rho, x[:,0], linewidth = 2, color = 'r' )
  plt.plot ( rho, x[:,1], linewidth = 2, color = 'g' )
  plt.plot ( rho, x[:,2], linewidth = 2, color = 'b' )
  plt.plot ( [ rhomin, rhomax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance -->' )
  plt.title ( 'Brownian sample paths' )
  filename = 'correlation_brownian_paths.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def correlation_besselj ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_besselj() evaluates the Bessel J correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  from scipy.special import jv
  import numpy as np

  rhohat = np.abs ( rho ) / rho0

  c = jv ( 0, rhohat )

  return c

def correlation_besselk ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_besselk() evaluates the Bessel K correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  from scipy.special import kv
  import numpy as np

  i = rho != 0.0
  rhohat = np.abs ( rho ) / rho0
  c = np.ones_like ( rho )
  c[i] = rhohat[i] * kv ( 1.0, rhohat[i] )

  return c

def correlation_brownian_display ( ):

#*****************************************************************************80
#
## correlation_brownian_display() displays 4 slices of the Brownian Correlation.
#
#  Discussion:
#
#    The correlation function is C(S,T) = sqrt ( min ( s, t ) / max ( s, t ) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  m = 4
  n = 101
  s = np.array ( [ 0.25, 1.5, 2.5, 3.75 ] )
  t = np.linspace ( 0.0, 5.0, n )
  rho0 = 1.0

  c = correlation_brownian ( m, n, s, t, rho0 )

  for i in range ( 0, m ):
    plt.plot ( t, c[i,:], linewidth = 3 ) 

  plt.grid ( True ) 
  plt.title ( 'Brownian correlation, C(S,T), S = 0.25, 1.5, 2.5, 3.75' )

  return

def correlation_brownian ( m, n, s, t, rho0 ):

#*****************************************************************************80
#
## correlation_brownian() computes the Brownian correlation function.
#
#  Discussion:
#
#    C(I,J) is the correlation Cor ( S(I), T(J) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of arguments.
#
#    real S(M), T(N), two sets of arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(M,N), the correlations.
#
  import numpy as np

  C = np.ones ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      stmax = max ( s[i], t[j] )
      stmin = min ( s[i], t[j] )
      if ( stmax != 0.0 ):
        C[i,j] = np.sqrt ( stmin / stmax )
 
  return C

def correlation_circular ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_circular() evaluates the circular correlation function.
#
#  Discussion:
#
#    This correlation is based on the area of overlap of two circles
#    of radius RHO0 and separation RHO.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  i = np.abs ( rho ) <= rho0
  rhohat = np.ones_like ( rho )
  rhohat[i] = np.abs ( rho[i] ) / rho0

  c = ( 1.0 - ( 2.0 / np.pi ) \
    * ( rhohat * np.sqrt ( 1.0 - rhohat**2 ) + np.arcsin ( rhohat ) ) )

  return c

def correlation_constant ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_constant() evaluates the constant correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  c = np.ones_like ( rho )

  return c

def correlation_cubic ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_cubic() evaluates the cubic correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

# rhohat = np.min ( np.abs ( rho ) / rho0, 1.0 )

  rhohat = np.abs ( rho ) / rho0

  c = 1.0 \
    - 7.0  * rhohat**2 \
    + 8.75 * rhohat**3 \
    - 3.5  * rhohat**5 \
    + 0.75 * rhohat**7

  return c

def correlation_damped_cosine ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_damped_cosine() evaluates the damped cosine correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  rhohat = np.abs ( rho ) / rho0

  c = np.exp ( - rhohat ) * np.cos ( rhohat )

  return c

def correlation_damped_sine ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_damped_sine() evaluates the damped sine correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  i = rho != 0.0
  rhohat = rho / rho0
  c = np.ones_like ( rho )
  c[i] = np.sin ( rhohat[i] ) / rhohat[i]

  return c
  
def correlation_exponential ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_exponential() evaluates the exponential correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  rhohat = np.abs ( rho ) / rho0

  c = np.exp ( - rhohat )

  return c

def correlation_gaussian ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_gaussian() evaluates the Gaussian correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  rhohat = rho / rho0

  c = np.exp ( - rhohat**2 )

  return c

def correlation_hole ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_hole() evaluates the hole correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  rhohat = np.abs ( rho ) / rho0

  c = ( 1.0 - rhohat ) * np.exp ( - rhohat )

  return c

def correlation_linear ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_linear() evaluates the linear correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  c = ( np.abs ( rho ) <= rho0 ) * ( rho0 - np.abs ( rho ) ) / rho0

  return c

def correlation_matern ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_matern() evaluates the Matern correlation function.
#
#  Discussion:
#
#    The Matern correlation is
#
#      rho1 = 2 * sqrt ( nu ) * rho / rho0
#
#      c(rho) = ( rho1 )^nu * BesselK ( nu, rho1 ) / gamma ( nu ) / 2 ^ ( nu - 1 )
#
#    The Matern covariance has the form:
#
#      K(rho) = sigma^2 * c(rho)
#
#    A Gaussian process with Matern covariance has sample paths that are
#    differentiable (nu - 1) times.
#
#    When nu = 0.5, the Matern covariance is the exponential covariance.
#
#    As nu goes to infinity, the correlation converges to exp ( - (rho/rho0)^2 ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#    0.0 <= RHO.
#
#    real RHO0, the correlation length.
#    0.0 < RHO0.
#
#    real NU, the smoothness parameter.
#    NU has a default value of 2.5
#    0 < NU.
#
#  Output:
#
#    real C(N), the correlations.
#
  from scipy.special import gamma
  from scipy.special import kv
  import numpy as np

  nu = 2.5

  rho1 = 2.0 * np.sqrt ( nu ) * np.abs ( rho ) / rho0
  i = rho1 != 0.0
  c = np.ones_like ( rho )
  c[i] = ( rho1[i] ) ** nu * kv ( nu, rho1[i] ) / gamma ( nu ) / 2.0 ** ( nu - 1 )

  return c

def correlation_pentaspherical ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_pentaspherical() evaluates the pentaspherical correlation function.
#
#  Discussion:
#
#    This correlation is based on the volume of overlap of two spheres
#    of radius RHO0 and separation RHO.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  rhohat = np.abs ( rho ) / rho0

  c = 1.0 - 1.875 * rhohat + 1.25 * rhohat**3 - 0.375 * rhohat**5

  return c

def correlation_power ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_power() evaluates the power correlation function.
#
#  Discussion:
#
#    The power correlation is
#
#      C(rho) = ( 1 - |rho| )^e  if 0 <= |rho| <= 1
#             = 0                otherwise
#
#      The constraint on the exponent is 2 <= e.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#    0.0 <= RHO.
#
#    real RHO0, the correlation length.
#    0.0 < RHO0.
#
#    real E, the exponent.
#    E has a default value of 2
#    2 <= E.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  e = 2.0

  rho1 = np.abs ( rho ) / rho0
   
  c = ( 1.0 - rho1 ) ** e

  return c

def correlation_rational_quadratic ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_rational_quadratic() evaluates the rational quadratic correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  rhohat = rho / rho0

  c = 1.0 / ( 1.0 + rhohat**2 )

  return c

def correlation_spherical ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_spherical() evaluates the spherical correlation function.
#
#  Discussion:
#
#    This correlation is based on the volume of overlap of two spheres
#    of radius RHO0 and separation RHO.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np

  rhohat = np.abs ( rho ) / rho0

  c = 1.0 - 1.5 * rhohat + 0.5 * rhohat**3

  return c

def correlation_to_covariance ( n, C, sigma ):

#*****************************************************************************80
#
## correlation_to_covariance(): covariance matrix from a correlation matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real C(N,N), the correlation matrix.
#
#    real SIGMA(N), the standard deviations.
#
#  Output:
#
#    real K(N,N), the covariance matrix.
#
  import numpy as np

  eps = np.finfo(float).eps
  tol = np.sqrt ( eps )
#
#  C must be symmetric.
#
  error_frobenius = r8mat_is_symmetric ( C )

  if ( tol < error_frobenius ):
    print ( '' )
    print ( 'CORRELATION_TO_COVARIANCE(): Fatal error!' )
    print ( '  Input matrix C fails symmetry test with error ', error_frobenius )
    raise Exception ( 'CORRELATION_TO_COVARIANCE(): Fatal error!' )
#
#  The diagonal must be 1.
#
  error_l1 = 0.0
  for i in range ( 0, n ):
    error_l1 = error_l1 + np.abs ( C[i,i] - 1.0 )
  error_l1 = error_l1 / n

  if ( tol < error_l1 ):
    print ( '' )
    print ( 'CORRELATION_TO_COVARIANCE(): Fatal error!' )
    print ( '  Input matrix C has non-unit diagonal entries.' )
    print ( '  Average error is ', error_l1 )
    raise Exception ( 'CORRELATION_TO_COVARIANCE(): Fatal error!' )
#
#  Off-diagonals must be between -1 and 1.
#
  if ( np.min ( C ) < - 1.0 - tol ):
    print ( '' )
    print ( 'CORRELATION_TO_COVARIANCE(): Fatal error!' )
    print ( '  Input matrix C has entries less than -1.0' )
    raise Exception ( 'CORRELATION_TO_COVARIANCE(): Fatal error!' )

  if ( 1.0 + tol < np.max ( C ) ):
    print ( '' )
    print ( 'CORRELATION_TO_COVARIANCE(): Fatal error!' )
    print ( '  Input matrix C has entries greater than +1.0' )
    raise Exception ( 'CORRELATION_TO_COVARIANCE(): Fatal error!' )
#
#  Form K.
#
  K = np.matmul ( np.diag ( sigma ), \
    np.matmul ( C, np.diag ( sigma ) ) )

  return K

def correlation_white_noise ( n, rho, rho0 ):

#*****************************************************************************80
#
## correlation_white_noise() evaluates the white noise correlation function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Petter Abrahamsen,
#    A Review of Gaussian Random Fields and Correlation Functions,
#    Norwegian Computing Center, 1997.
#
#  Input:
#
#    integer N, the number of arguments.
#
#    real RHO(N), the arguments.
#
#    real RHO0, the correlation length.
#
#  Output:
#
#    real C(N), the correlations.
#
  import numpy as np
#
#  We need to insist that C is a real quantity, not a logical,
#  otherwise we can't call the toeplitz function later on!
#
  c = ( rho == 0.0 )

  return c

def covariance_to_correlation ( n, K ):

#*****************************************************************************80
#
## covariance_to_correlation(): correlation matrix from a covariance matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real K(N,N), the covariance matrix.
#
#  Output:
#
#    real C(N,N), the correlation matrix.
#
#    real SIGMA(N), the standard deviations.
#
  import numpy as np

  eps = np.finfo(float).eps
  tol = np.sqrt ( eps )
#
#  K must be symmetric.
#
  error_frobenius = r8mat_is_symmetric ( K )

  if ( tol < error_frobenius ):
    print ( '' )
    print ( 'COVARIANCE_TO_CORRELATION(): Fatal error!' )
    print ( '  Matrix K fails symmetry test with error ', error_frobenius )
    raise Exception ( 'COVARIANCE_TO_CORRELATION(): Fatal error!' )
#
#  It must be the case that K(I,J)^2 <= K(I,I) * K(J,J).
#
  error_max = 0.0
  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      error_max = max ( error_max, K[i,j]**2 - K[i,i] * K[j,j] )

  if ( tol < error_max ):
    print ( '' )
    print ( 'COVARIANCE_TO_CORRELATION(): Fatal error!' )
    print ( '  Input matrix K fails K(I,J)^2 <= K(I,I)*K(J,J)' )
    raise Exception ( 'COVARIANCE_TO_CORRELATION(): Fatal error!' )
#
#  Get the diagonal of K.
#
  sigma = np.diag ( K )
#
#  Ensure the diagonal is positive.
#
  sigma_min = np.min ( sigma )

  if ( sigma_min <= 0.0 ):
    print ( '' )
    print ( 'COVARIANCE_TO_CORRELATION(): Fatal error!' )
    print ( '  Input matrix K has nonpositive diagonal entry = ', sigma_min )
    raise Exception ( 'COVARIANCE_TO_CORRELATION(): Fatal error!' )
#
#  Convert from variance to standard deviation.
#
  sigma = np.sqrt ( sigma )
#
#  Form C.
#
  C = np.matmul ( np.diag ( 1.0 / sigma ), \
      np.matmul ( K, np.diag ( 1.0 / sigma ) ) )

  return C, sigma

def minij ( m, n ):

#*****************************************************************************80
#
## minij() returns the MINIJ matrix.
#
#  Formula:
#
#    A(I,J) = min ( I, J )
#
#  Example:
#
#    N = 5
#
#    1 1 1 1 1
#    1 2 2 2 2
#    1 2 3 3 3
#    1 2 3 4 4
#    1 2 3 4 5
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    The inverse of A is tridiagonal.
#
#    The eigenvalues of A are
#
#      LAMBDA(I) = 0.5 / ( 1 - cos ( ( 2 * I - 1 ) * pi / ( 2 * N + 1 ) ) ),
#
#    For N = 12, the characteristic polynomial is
#      P(X) = X^12 - 78 X^11 + 1001 X^10 - 5005 X^9 + 12870 X^8
#        - 19448 X^7 + 18564 X^6 - 11628 X^5 + 4845 X^4 - 1330 X^3
#        + 231 X^2 - 23 X + 1.
#
#    (N+1)*ONES(N) - A also has a tridiagonal inverse.
#
#    Gregory and Karney consider the matrix defined by
#
#      B(I,J) = N + 1 - MAX(I,J)
#
#    which is equal to the MINIJ matrix, but with the rows and
#    columns reversed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.12, Example 4.14,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 41, page 74, 
#    LC: QA263.G68.
#
#    Daniel Rutherford,
#    Some continuant determinants arising in physics and chemistry II,
#    Proceedings of the Royal Society Edinburgh,
#    Volume 63, A, 1952, pages 232-241.
#
#    John Todd,
#    Basic Numerical Mathematics, Vol. 2: Numerical Algebra,
#    Academic Press, 1977, page 158.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer M, N, the number of rows and columns 
#    of the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  A = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      A[i,j] = min ( i, j ) + 1

  return A

def r8mat_is_symmetric ( A ):

#*****************************************************************************80
#
## r8mat_is_symmetric() checks a real matrix for symmetry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N), the matrix.
#
#  Output:
#
#    real ERROR_FROBENIUS, measures the Frobenius norm of ( A - A' ).
#
  import numpy as np

  m, n = A.shape

  if ( m != n ):
    error_frobenius = np.inf
    return error_frobenius

  error_frobenius = np.linalg.norm ( A - A.T, 'fro' )

  return error_frobenius

def sample_paths_cholesky ( n, n2, rhomax, rho0, correlation ):

#*****************************************************************************80
#
## sample_paths_cholesky(): sample paths for stationary correlation functions.
#
#  Discussion:
#
#    This method uses the Cholesky factorization of the correlation matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points on each path.
#
#    integer N2, the number of paths.
#
#    real RHOMAX, the maximum value of RHO.
#
#    real RHO0, the correlation length.
#
#    CORRELATION, a handle for a correlation function.
#
#  Output:
#
#    real X(N,N2), the sample paths.
#
  import numpy as np
  from numpy.random import default_rng

  rng = default_rng ( )
#
#  Choose N equally spaced sample points from 0 to RHOMAX.
#
  rho_vec = np.linspace ( 0.0, rhomax, n )
#
#  Evaluate the correlation function.
#
  cor_vec = correlation ( n, rho_vec, rho0 )

  cor = np.zeros ( [ n, n ] )
#
#  From the vector 
#    [ C(0), C(1), C(2), ... C(N-1) ]
#  construct the vector
#    [ C(N-1), ..., C(2), C(1), C(0), C(1), C(2), ...  C(N-1) ]
#
  cor_vec = np.concatenate ( ( cor_vec[-1:0:-1], cor_vec ) )
#
#  Every row of the correlation matrix can be constructed by a subvector
#  of this vector.
#
  for i in range ( 0, n ):
    cor[i,:] = cor_vec[n-i-1:2*n-i-1]
#
#  Get the Cholesky factorization of COR:
#
#    COR = L * L'.
#
  l = np.linalg.cholesky ( cor )
#
#  Compute N independent random normal values.
#
  r = rng.standard_normal ( size = [ n, n2 ] )
#
#  Compute the sample path.
#
  x = np.matmul ( l, r )

  return x

def sample_paths2_cholesky ( n, n2, rhomin, rhomax, rho0, correlation2 ):

#*****************************************************************************80
#
## sample_paths2_cholesky(): sample paths for nonstationary correlation functions.
#
#  Discussion:
#
#    This function assumes does not assume that the correlation function
#    C(S,T) is actually a function of |S-T|. 
#
#    This method uses the Cholesky factorization of the correlation matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points on each path.
#
#    integer N2, the number of paths.
#
#    real RHOMIN, RHOMAX, the argument range to examine.
#
#    real RHO0, the correlation length.
#
#    CORRELATION2, a handle for a correlation function, which has
#    the form c = correlation2 ( m, n, s, t, rho0 ).
#
#  Output:
#
#    real X(N,N2), the sample paths.
#
  import numpy as np
  from numpy.random import default_rng

  rng = default_rng ( )
#
#  Choose 2 equal N vectors of equally spaced sample points from RHOMIN to RHOMAX.
#
  s = np.linspace ( rhomin, rhomax, n )
#
#  Evaluate the correlation function of two arguments.
#
  cor = correlation2 ( n, n, s, s, rho0 )
#
#  Get the Cholesky factorization of COR:
#
#    COR = L * L'.
#
  l = np.linalg.cholesky ( cor )
#
#  Compute N independent random normal values.
#
  r = rng.standard_normal ( size = [ n, n2 ] )
#
#  Compute the sample path.
#
  x = np.matmul ( l, r )

  return x

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
  correlation_test ( )
  timestamp ( )

