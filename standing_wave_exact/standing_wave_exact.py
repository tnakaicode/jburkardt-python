#! /usr/bin/env python3
#
def standing_wave_exact_test ( ):

#*****************************************************************************80
#
## standing_wave_exact_test() tests standing_wave_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'standing_wave_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test standing_wave_exact(),' )
  print ( '  an exact standing wave solution of the wave equation.' )
#
#  Report the current parameter values.
#
  c, xmin, xmax, t0, tstop = standing_wave_parameters ( )
  print ( '' )
  print ( '  parameters:' )
  print ( '    c     = ', c )
  print ( '    xmin  = ', xmin )
  print ( '    xmax  = ', xmax )
  print ( '    t0    = ', t0 )
  print ( '    tstop = ', tstop )

  standing_wave_residual_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'standing_wave_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def standing_wave_exact ( x, t ):

#*****************************************************************************80
#
## standing_wave_exact() evaluates an exact solution of the 1D wave equation.
#
#  Discussion:
#
#    d^2u/dt^2 = c^2 d^2u/dx^2
#    u[x,t] = sin(x) * cos(c*t)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 April 2025
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

  c, xmin, xmax, t0, tstop = standing_wave_parameters ( )

  u = np.sin ( x ) * np.cos ( c * t )

  ut = - c * np.sin ( x ) * np.sin ( c * t )

  utt = - c**2 * np.sin ( x ) * np.cos ( c * t )

  ux = np.cos ( x ) * np.cos ( c * t )

  uxx = - np.sin ( x ) * np.cos ( c * t )

  return u, ut, utt, ux, uxx

def standing_wave_residual_test ( ):

#*****************************************************************************80
#
## standing_wave_residual_test() tests standing_wave_residual().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 April 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'standing_wave_residual_test():' )
  print ( '  Evaluate solution and residual at selected points (X,T)' )
  
  c, xmin, xmax, t0, tstop = standing_wave_parameters ( )

  n = 11
  m = 5
  x = np.linspace ( xmin, xmax, n )
  t = np.linspace ( t0, tstop, m )

  print ( '' )
  print ( '      X       T       U(X,T)      Resid(X,T)' )
  print ( '' )
  for j in range ( 0, m ):
    for i in range ( 0, n ):
      u, ut, utt, ux, uxx = standing_wave_exact ( x[i], t[j] )
      r = standing_wave_residual ( x[i], t[j] )
      print ( '  %8.4f  %8.4f  %10.4g  %g' % ( x[i], t[j], u, r ) )
    print ( '' )

  return

def standing_wave_parameters ( c_user = None, xmin_user = None, \
  xmax_user = None, t0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## standing_wave_parameters() returns parameters for the standing wave equation.
#
#  Discussion:
#
#    d^2u/dt^2 = c^2 d^2u/dx^2
#    u[x,t] = sin(x) * cos(c*t)
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
#    05 April 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real c_user: the wave speed.
#
#    real xmin_user, xmax_user: the left and right interval endpoints.
#
#    real t0_user: the initial time.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real c: the wave speed. 
#
#    real xmin, xmax: the left and right interval endpoints.
#
#    real t0: the initial time.
#
#    real tstop: the final time.
#

#
#  Initialize defaults.
#
  if not hasattr ( standing_wave_parameters, "c_default" ):
    standing_wave_parameters.c_default = 0.2

  if not hasattr ( standing_wave_parameters, "xmin_default" ):
    standing_wave_parameters.xmin_default = -1.0

  if not hasattr ( standing_wave_parameters, "xmax_default" ):
    standing_wave_parameters.xmax_default = 1.0

  if not hasattr ( standing_wave_parameters, "t0_default" ):
    standing_wave_parameters.t0_default = 0.0

  if not hasattr ( standing_wave_parameters, "tstop_default" ):
    standing_wave_parameters.tstop_default = 5.0
#
#  Update defaults if input was supplied.
#
  if ( c_user is not None ):
    standing_wave_parameters.c_default = c_user

  if ( xmin_user is not None ):
    standing_wave_parameters.xmin_default = xmin_user

  if ( xmax_user is not None ):
    standing_wave_parameters.xmax_default = xmax_user

  if ( t0_user is not None ):
    standing_wave_parameters.t0_default = t0_user

  if ( tstop_user is not None ):
    standing_wave_parameters.tstop_default = tstop_user
#
#  Return values.
#
  c = standing_wave_parameters.c_default
  xmin = standing_wave_parameters.xmin_default
  xmax = standing_wave_parameters.xmax_default
  t0 = standing_wave_parameters.t0_default
  tstop = standing_wave_parameters.tstop_default

  return c, xmin, xmax, t0, tstop

def standing_wave_residual ( t, x ):

#*****************************************************************************80
#
## standing_wave_residual() computes the residual of the standing wave equation.
#
#  Discussion:
#
#    d^2u/dt^2 = c^2 d^2u/dx^2
#    u[x,t] = sin(x) * cos(c*t)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 April 2025
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
  c, xmin, xmax, t0, tstop = standing_wave_parameters ( )

  u, ut, utt, ux, uxx = standing_wave_exact ( t, x )

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
  standing_wave_exact_test ( )
  timestamp ( )

