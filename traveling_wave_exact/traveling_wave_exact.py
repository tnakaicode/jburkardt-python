#! /usr/bin/env python3
#
def traveling_wave_exact_test ( ):

#*****************************************************************************80
#
## traveling_wave_exact_test() tests traveling_wave_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'traveling_wave_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test traveling_wave_exact(),' )
  print ( '  an exact traveling wave solution of the wave equation.' )
#
#  Report the current parameter values.
#
  a, k, w, phi, xmin, xmax, t0, tstop = traveling_wave_parameters ( )
  print ( '' )
  print ( '  parameters:' )
  print ( '    a     = ', a )
  print ( '    k     = ', k )
  print ( '    w     = ', w )
  print ( '    phi   = ', phi )
  print ( '    xmin  = ', xmin )
  print ( '    xmax  = ', xmax )
  print ( '    t0    = ', t0 )
  print ( '    tstop = ', tstop )

  traveling_wave_residual_test ( )

  traveling_wave_plot ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'traveling_wave_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def traveling_wave_exact ( x, t ):

#*****************************************************************************80
#
## traveling_wave_exact() evaluates an exact solution of the 1D wave equation.
#
#  Discussion:
#
#    d^2u/dt^2 = c^2 d^2u/dx^2
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 April 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x, t: the position and time.
#
#  Output:
#
#    real u, ut, utt, ux, uxx: the values of the exact solution, its time
#    derivative, and its first and second spatial derivatives at (x,t).
#
  import numpy as np

  a, k, w, phi, xmin, xmax, t0, tstop = traveling_wave_parameters ( )

  u = a * np.sin ( k * x + w * t + phi )

  ut = a * w * np.cos ( k * x + w * t + phi )

  utt = - a * w * w * np.sin ( k * x + w * t + phi )

  ux = a * k * np.cos ( k * x + w * t + phi )

  uxx = - a * k * k * np.sin ( k * x + w * t + phi )

  return u, ut, utt, ux, uxx

def traveling_wave_plot ( ):

#*****************************************************************************80
#
## traveling_wave_plot() tests the traveling wave.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'traveling_wave_plot():' )
  print ( '  Plot the traveling wave over several time steps' )
  
  a, k, w, phi, xmin, xmax, t0, tstop = traveling_wave_parameters ( )

  n = 51
  x = np.linspace ( xmin, xmax, n )

  m = 5
  t = np.linspace ( t0, tstop, m )
  
  plt.clf ( )
  plt.grid ( True )

  for i in range ( 0, m ):
    u, ut, utt, ux, uxx = traveling_wave_exact ( x, t[i] )
    plt.plot ( x, u, linewidth = 2 )

  plt.title ( 'Traveling wave' )
  filename = 'traveling_wave_exact.png';
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  
  return

def traveling_wave_residual_test ( ):

#*****************************************************************************80
#
## traveling_wave_residual_test() tests traveling_wave_residual().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'traveling_wave_residual_test():' )
  print ( '  Evaluate solution and residual at selected points (X,T)' )
  
  a, k, w, phi, xmin, xmax, t0, tstop = traveling_wave_parameters ( )

  n = 11
  x = np.linspace ( xmin, xmax, n )

  m = 5
  t = np.linspace ( t0, tstop, m )

  print ( '' )
  print ( '      X       T       U(X,T)      Resid(X,T)' )
  print ( '' )
  for j in range ( 0, m ):
    for i in range ( 0, n ):
      u, ut, utt, ux, uxx = traveling_wave_exact ( x[i], t[j] )
      r = traveling_wave_residual ( x[i], t[j] )
      print ( '  %8.4f  %8.4f  %10.4g  %g' % ( x[i], t[j], u, r ) )
    print ( '' )

  return

def traveling_wave_parameters ( a_user = None, k_user = None, w_user = None, \
  phi_user = None, xmin_user = None, xmax_user = None, t0_user = None, 
  tstop_user = None ):

#*****************************************************************************80
#
## traveling_wave_parameters() returns parameters for the traveling wave equation.
#
#  Discussion:
#
#    d^2u/dt^2 = c^2 d^2u/dx^2
#
#    If input values are specified, this resets the default parameters.
#    Otherwise, the output will be the current defaults.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real a_user: the amplitude.
#
#    real k_user: the wave number.
#
#    real w_user: angular frequency.
#
#    real phi_user: the phase angle.
#
#    real xmin_user, xmax_user: the left and right interval endpoints.
#
#    real t0_user: the initial time.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real a: the amplitude.
#
#    real k: the wave number.
#
#    real w: angular frequency.
#
#    real phi: the phase angle.
#
#    real xmin, xmax: the left and right interval endpoints.
#
#    real t0: the initial time.
#
#    real tstop: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( traveling_wave_parameters, "a_default" ):
    traveling_wave_parameters.a_default = 2.0

  if not hasattr ( traveling_wave_parameters, "k_default" ):
    traveling_wave_parameters.k_default = 6.0

  if not hasattr ( traveling_wave_parameters, "w_default" ):
    traveling_wave_parameters.w_default = 1.0

  if not hasattr ( traveling_wave_parameters, "phi_default" ):
    traveling_wave_parameters.phi_default = np.pi / 4.0

  if not hasattr ( traveling_wave_parameters, "xmin_default" ):
    traveling_wave_parameters.xmin_default = -1.0

  if not hasattr ( traveling_wave_parameters, "xmax_default" ):
    traveling_wave_parameters.xmax_default = 1.0

  if not hasattr ( traveling_wave_parameters, "t0_default" ):
    traveling_wave_parameters.t0_default = 0.0

  if not hasattr ( traveling_wave_parameters, "tstop_default" ):
    traveling_wave_parameters.tstop_default = 5.0
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    traveling_wave_parameters.a_default = a_user

  if ( k_user is not None ):
    traveling_wave_parameters.k_default = k_user

  if ( w_user is not None ):
    traveling_wave_parameters.w_default = w_user

  if ( phi_user is not None ):
    traveling_wave_parameters.phi_default = phi_user

  if ( xmin_user is not None ):
    traveling_wave_parameters.xmin_default = xmin_user

  if ( xmax_user is not None ):
    traveling_wave_parameters.xmax_default = xmax_user

  if ( t0_user is not None ):
    traveling_wave_parameters.t0_default = t0_user

  if ( tstop_user is not None ):
    traveling_wave_parameters.tstop_default = tstop_user
#
#  Return values.
#
  a = traveling_wave_parameters.a_default
  k = traveling_wave_parameters.k_default
  w = traveling_wave_parameters.w_default
  phi = traveling_wave_parameters.phi_default
  xmin = traveling_wave_parameters.xmin_default
  xmax = traveling_wave_parameters.xmax_default
  t0 = traveling_wave_parameters.t0_default
  tstop = traveling_wave_parameters.tstop_default

  return a, k, w, phi, xmin, xmax, t0, tstop

def traveling_wave_residual ( t, x ):

#*****************************************************************************80
#
## traveling_wave_residual() computes the residual of the traveling wave equation.
#
#  Discussion:
#
#    d^2u/dt^2 = c^2 d^2u/dx^2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 April 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, X: the time and position where the solution is evaluated.
#
#  Output:
#
#    real R: the residual at that time and position.
#
  a, k, w, phi, xmin, xmax, t0, tstop = traveling_wave_parameters ( )

  u, ut, utt, ux, uxx = traveling_wave_exact ( t, x )

  c = w / k

  r = utt - c**2 * uxx

  return r

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
  traveling_wave_exact_test ( )
  timestamp ( )

