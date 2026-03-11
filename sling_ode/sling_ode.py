#! /usr/bin/env python3
#
def sling_conserved ( y1, y2 ):

#*****************************************************************************80
#
## sling_conserved() returns a conserved quantity for sling_ode().
#
#  Discussion:
#
#    This is not a typical conservation quantity.
#    The value of H is only conserved when H=1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Y(:,2): the current solution.
#
#  Output:
#
#    real H(:): the value of the conserved quantity.
#
  h = y1**2 + y2**2

  return h

def sling_deriv ( t, y ):

#*****************************************************************************80
#
## sling_deriv() returns the right hand side of sling_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, the current time.
#
#    real Y(2), the current state values.
#
#  Output:
#
#    real dydt(2), the time derivatives of the current state values.
#
  import numpy as np

  s, t0, y0, tstop = sling_parameters ( )

  u = y[0]
  v = y[1]

  r = np.sqrt ( u**2 + v**2 )
  dudt = - v + s * u * ( r - 1.0 )
  dvdt =   u + s * v * ( r - 1.0 )

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def sling_ode_test ( ):

#*****************************************************************************80
#
## sling_ode_test() solves sling_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'sling_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve sling_ode().' )

  s, t0, y0, tstop = sling_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    s     = ', s )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  sling_solve_ivp ( )
#
#  Repeat calculation, with smaller value of S.
#
  s = 0.40
  [ s, t0, y0, tstop ] = sling_parameters ( s, t0, y0, tstop )

  print ( '' )
  print ( '  parameters:' )
  print ( '    s     = ', s )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  sling_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sling_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def sling_parameters ( s_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## sling_parameters() returns parameters for sling_ode().
#
#  Discussion:
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
#    08 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real S_USER: the strength of the stiffness term.
#
#    real T0_USER: the initial time
#
#    real Y0_USER(2): the initial values.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real S: the strength of the stiffness term.
#
#    real T0: the initial time
#
#    real Y0(2): the initial values.
#
#    real TSTOP: the final time.
#
  import numpy as np

  if not hasattr ( sling_parameters, "s_default" ):
    sling_parameters.s_default = 1.0

  if not hasattr ( sling_parameters, "t0_default" ):
    sling_parameters.t0_default = 0.0

  if not hasattr ( sling_parameters, "y0_default" ):
    sling_parameters.y0_default = np.array ( [ 1.0, 0.0 ] )

  if not hasattr ( sling_parameters, "tstop_default" ):
    sling_parameters.tstop_default = 30.0
#
#  New values, if supplied on input, overwrite the current values.
#
  if ( s_user is not None ):
    sling_parameters.s_default = s_user

  if ( t0_user is not None ):
    sling_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    sling_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    sling_parameters.tstop_default = tstop_user
#
#  Return values.
#
  s = sling_parameters.s_default
  t0 = sling_parameters.t0_default
  y0 = sling_parameters.y0_default
  tstop = sling_parameters.tstop_default
  
  return s, t0, y0, tstop

def sling_solve_ivp ( ):

#*****************************************************************************80
#
## sling_solve_ivp() solves sling_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sling_solve_ivp():' )
  print ( '  Test sling_ode() using solve_ivp().' )

  s, t0, y0, tstop = sling_parameters ( )

  f = sling_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  y1 = sol.y[0]
  y2 = sol.y[1]
#
#  Plot u, v.
#
  plt.plot ( t, y1, 'r-', linewidth = 2 )
  plt.plot ( t, y2, 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Solution components -->' )
  title_string = ( 'sling_ode() solve_ivp: plot, s = %g' % ( s ) )
  plt.title ( title_string )
  plt.legend ( ( 'x', 'y' ) )
  filename = ( 'sling_solve_ivp_plot_%g.png' % ( s ) )
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Phase plot.
#
  plt.plot ( y1, y2, 'b-', linewidth = 2 )
  plt.plot ( y1[0], y2[0], 'g.', markersize = 20 )
  plt.plot ( y1[-1], y2[-1], 'r.', markersize = 20 )
  plt.grid ( True )
  plt.xlabel ( '<-- x -->' )
  plt.ylabel ( '<-- y -->' )
  title_string = ( 'sling_ode() solve_ivp: phase, s = %g' % ( s ) )
  plt.title ( title_string )
  plt.axis ( 'equal' )
  filename = ( 'sling_solve_ivp_phase_%g.png' % ( s ) )
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )
#
#  Plot energy.
#
  h = sling_conserved ( y1, y2 )

  plt.clf ( )
  plt.plot ( t, h, 'r-', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ h[0], h[0] ] ), 'b--', linewidth = 2 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- Energy -->' )
  title_string = ( 'sling_ode() solve_ivp: energy, s = %g' % ( s ) )
  plt.title ( title_string )
  plt.legend ( ( 'Computed energy', 'Exact energy', 'Zero energy' ) )
  filename = ( 'sling_solve_ivp_conservation_%g.png' % ( s ) )
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

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
  sling_ode_test ( )
  timestamp ( )


