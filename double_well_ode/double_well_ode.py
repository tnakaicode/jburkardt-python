#! /usr/bin/env python3
#
def double_well_conserved ( q, p ):

#*****************************************************************************80
#
## double_well_conserved() returns a conserved quantity for double_well_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q(:), P(:): the current solution.
#
#  Output:
#
#    real H(:): the value of the conserved quantity.
#
  u, dudq = double_well_potential ( q, p )

  h = u + 0.5 * p * p

  return h

def double_well_deriv ( t, y ):

#*****************************************************************************80
#
## double_well_deriv() evaluates the derivative of double_well_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the current time.
#
#    real Y(:,2): the current solution.
#
#  Output:
#
#    real DYDT(:): the right hand side of the ODE.
#
  import numpy as np

  q = y[0]
  p = y[1]

  u, dudq = double_well_potential ( q, p )

  dqdt = p
  dpdt = - dudq

  dydt = np.array ( [ dqdt, dpdt ] )

  return dydt

def double_well_ode_test ( ):

#*****************************************************************************80
#
## double_well_ode_test() solves double_well_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'double_well_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve double_well_ode().' )

  t0, y0, tstop = double_well_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )

  double_well_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'double_well_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def double_well_parameters ( t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## double_well_parameters() returns the parameters of double_well_ode().
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
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np

  if not hasattr ( double_well_parameters, "t0_default" ):
    double_well_parameters.t0_default = 0.0

  if not hasattr ( double_well_parameters, "y0_default" ):
    double_well_parameters.y0_default = np.array ( [ 1.0, 1.0 ] )

  if not hasattr ( double_well_parameters, "tstop_default" ):
    double_well_parameters.tstop_default = 10.0
#
#  New values, if supplied on input, overwrite the current values.
#
  if ( t0_user is not None ):
    double_well_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    double_well_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    double_well_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = double_well_parameters.t0_default
  y0 = double_well_parameters.y0_default
  tstop = double_well_parameters.tstop_default
 
  return t0, y0, tstop

def double_well_potential ( q, p ):

#*****************************************************************************80
#
## double_well_potential() evaluates the potential for double_well_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Q(:), P(:): the current solution.
#
#  Output:
#
#    real U(:): the potential.
#
#    real DUDQ(:): the derivative of the potential with respect to Q = Y(1).
#
  u = ( q**2 - 1.0 )**2
  dudq = 4.0 * ( q**2 - 1.0 ) * q

  return u, dudq
 
def double_well_solve_ivp ( ):

#*****************************************************************************80
#
## double_well_solve_ivp() uses solve_ivp() on double_well_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 June 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'double_well_solve_ivp()' )
  print ( '  Solve double_well_ode() using solve_ivp().' )

  t0, y0, tstop = double_well_parameters ( )

  f = double_well_deriv
  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )

  plt.plot ( t, sol.y[0], 'r-', linewidth = 3 )
  plt.plot ( t, sol.y[1], 'b-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'double_well_ode(): solve_ivp, time plot' )
  plt.legend ( ( 'Q', 'P' ) )
  filename = 'double_well_solve_ivp_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  plt.plot ( sol.y[0], sol.y[1], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Q -->' )
  plt.ylabel ( '<-- P -->' )
  plt.title ( 'double_well_ode(): solve_ivp, phase plot' )
  filename = 'double_well_solve_ivp_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  q = sol.y[0]
  p = sol.y[1]
  h = double_well_conserved ( q, p )

  plt.plot ( t, h, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ h[0], h[0] ] ), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [ 0.0, 0.0 ] ), 'k--', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- Time -->' )
  plt.ylabel ( '<-- H(t) -->' )
  plt.title ( 'double_well_ode(): solve_ivp, conservation' )
  filename = 'double_well_solve_ivp_conservation.png'
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
  double_well_ode_test ( )
  timestamp ( )

