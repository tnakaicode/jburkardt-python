#! /usr/bin/env python3
#
def axon_current ( t ):

#*****************************************************************************80
#
## axon_current() evaluates the time dependent current I(t) of axon_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the time.
#
#  Output:
#
#    real I: the current.
#
  I = 75.0 * ( t <= 0.80 )

  return I

def axon_deriv ( t, y ):

#*****************************************************************************80
#
## axon_deriv() evaluates the right hand side of axon_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Hodgkin, Andrew Huxley,
#    A quantitative description of membrane current and its
#    application to conduction and excitation in nerve,
#    The Journal of Physiology,
#    Volume 117, Number 4, pages 500-544, August 1952.
#
#  Input:
#
#    real T, Y(4): the time and solution value.
#
#  Output:
#
#    real DYDT(4): the derivative value.
#
  import numpy as np
#
#  Extract individual variable values at time t.
#
  V = y[0]
  n = y[1]
  m = y[2]
  h = y[3]
#
#  Get parameter values.
#
  C, E_K, E_Na, E_rest, G_K, G_Na, t0, y0, tstop = axon_parameters ( )
#
#  Compute alpha and beta for n:
#  Equations 12 and 13.
#
  alpha_n = 0.01 * ( ( 10.0 - V ) / ( np.exp ( ( 10.0 - V ) / 10.0 ) - 1.0 ) )
  beta_n = 0.125 * np.exp ( - V / 80.0 )
#
#  Compute alpha and beta for m:
#  Equations 20 and 21.
#
  alpha_m = 0.1 * ( ( 25.0 - V ) / ( np.exp ( ( 25.0 - V ) / 10.0 ) - 1.0 ) )
  beta_m = 4.0 * np.exp ( - V / 18.0 )
#
#  Compute alpha and beta for h:
#  Equations 23 and 24.
#
  alpha_h = 0.07 * np.exp ( - V / 20.0 )
  beta_h = 1.0 / ( np.exp ( ( 30.0 - V ) / 10.0 ) + 1.0 )
#
#  Calculate the currents.
#  I_Na:  equations 3 and 14.
#  I_K:   equations 4 and 6.
#  I_ion: equation 26.
#
  I_Na = m**3 * G_Na * h * ( V - E_Na )
  I_K = n**4 * G_K * ( V - E_K )
  I_ion = axon_current ( t ) - I_K - I_Na
#
#  Evaluate the derivatives.
#
#  dndt: equation 7
#  dmdt: equation 15
#  dhdt: equation 16
#
  dVdt = I_ion / C
  dndt = alpha_n * ( 1.0 - n ) - beta_n * n
  dmdt = alpha_m * ( 1.0 - m ) - beta_m * m
  dhdt = alpha_h * ( 1.0 - h ) - beta_h * h
#
#  Pack derivatives into vector.
#
  dydt = np.array ( [ dVdt, dndt, dmdt, dhdt ] )

  return dydt

def axon_euler ( ):

#*****************************************************************************80
#
## axon_euler() solves axon_ode() using euler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'axon_euler():' )
  print ( '  Solve axon_ode() using euler()' )
  print ( '' )
#
#  Get the parameters.
#
  C, E_K, E_Na, E_rest, G_K, G_Na, t0, y0, tstop = axon_parameters ( )

  f = axon_deriv
  tspan = np.array ( [ t0, tstop ] )
  nt = 1000
  print ( '  Number of fixed time steps = ', nt )

  t, y = euler ( f, tspan, y0, nt )
#
#  Plots.
#
  plt.clf ( )
  plt.plot ( t, y[:,0], 'r-', linewidth = 3 )
  plt.title ( 'axon_ode(): euler, V(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- V(T) --->' )
  filename = 'axon_euler_v.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, y[:,1], 'g-', linewidth = 3 )
  plt.title ( 'axon_ode(): euler, N(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- N(T) --->' )
  filename = 'axon_euler_n.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, y[:,2], 'b-', linewidth = 3 )
  plt.title ( 'axon_ode(): euler, M(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- M(T) --->' )
  filename = 'axon_euler_m.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, y[:,3], 'c-', linewidth = 3 )
  plt.title ( 'axon_ode(): euler, H(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H(T) --->' )
  filename = 'axon_euler_h.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  return

def axon_solve_ivp ( ):

#*****************************************************************************80
#
## axon_solve_ivp() solves axon_ode() using solve_ivp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'axon_solve_ivp():' )
  print ( '  Solve axon_ode() using solve_ivp()' )
  print ( '' )
#
#  Get the parameters.
#
  C, E_K, E_Na, E_rest, G_K, G_Na, t0, y0, tstop = axon_parameters ( )

  f = axon_deriv

  tspan = np.array ( [ t0, tstop ] )
  t = np.linspace ( t0, tstop, 101 )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Plots.
#
  plt.clf ( )
  plt.plot ( t, sol.y[0], 'r-', linewidth = 3 )
  plt.title ( 'axon_ode(): solve ivp, V(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- V(T) --->' )
  filename = 'axon_solve_ivp_v.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, sol.y[1], 'g-', linewidth = 3 )
  plt.title ( 'axon_ode(): solve ivp, N(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- N(T) --->' )
  filename = 'axon_solve_ivp_n.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, sol.y[2], 'b-', linewidth = 3 )
  plt.title ( 'axon_ode(): solve ivp, M(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- M(T) --->' )
  filename = 'axon_solve_ivp_m.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )

  plt.clf ( )
  plt.plot ( t, sol.y[3], 'c-', linewidth = 3 )
  plt.title ( 'axon_ode(): solve_ivp, H(t)' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- H(T) --->' )
  filename = 'axon_solve_ivp_h.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def axon_ode_test ( ):

#*****************************************************************************80
#
## axon_ode_test() tests axon_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'axon_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve axon_ode().' )

  C, E_K, E_Na, E_rest, G_K, G_Na, t0, y0, tstop = axon_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    C =      ', C )
  print ( '    E_K =    ', E_K )
  print ( '    E_Na =   ', E_Na )
  print ( '    E_rest = ', E_rest )
  print ( '    G_K =    ', G_K )
  print ( '    G_Na =   ', G_Na )
  print ( '    t0 =     ', t0 )
  print ( '    V(0) =   ', y0[0] )
  print ( '    N(0) =   ', y0[1] )
  print ( '    M(0) =   ', y0[2] )
  print ( '    H(0) =   ', y0[3] )
  print ( '    tstop =  ', tstop )

  axon_euler ( )
  axon_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'axon_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def axon_parameters ( C_user = None, E_K_user = None, E_Na_user = None, \
  E_rest_user = None, G_K_user = None, G_Na_user = None, t0_user = None, \
  y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## axon_parameters() returns parameters for axon_ode().
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
#    04 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real C_USER: the membrane capacity per unit area.
#
#    real E_K_USER: the equilibrium potential for potassium.
#
#    real E_Na_USER: the equilibrium potential for sodium.
#
#    real E_rest_USER: the resting potential.
#
#    real G_K_USER: the potassium conductance.
#
#    real G_Na_USER: the sodium conductance.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[4]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real C: the membrane capacity per unit area.
#
#    real E_K: the equilibrium potential for potassium.
#
#    real E_Na: the equilibrium potential for sodium.
#
#    real E_rest: the resting potential.
#
#    real G_K: the potassium conductance.
#
#    real G_Na: the sodium conductance.
#
#    real T0: the initial time.
#
#    real Y0[4]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( axon_parameters, "C_default" ):
    axon_parameters.C_default = 1.0

  if not hasattr ( axon_parameters, "E_K_default" ):
    axon_parameters.E_K_default = -74.7

  if not hasattr ( axon_parameters, "E_Na_default" ):
    axon_parameters.E_Na_default = 54.2

  if not hasattr ( axon_parameters, "E_rest_default" ):
    axon_parameters.E_rest_default = -68.0

  if not hasattr ( axon_parameters, "G_K_default" ):
    axon_parameters.G_K_default = 12.0

  if not hasattr ( axon_parameters, "G_Na_default" ):
    axon_parameters.G_Na_default = 30.0

  if not hasattr ( axon_parameters, "t0_default" ):
    axon_parameters.t0_default = 0.0

  if not hasattr ( axon_parameters, "y0_default" ):
    V_init = 0.0
    alpha_n = 0.01 * ( 10.0 - V_init ) / \
      ( np.exp ( ( 10.0 - V_init ) / 10.0 ) - 1.0 )
    beta_n = 0.125 * np.exp ( - V_init / 80.0 )
    n_init = alpha_n / ( alpha_n + beta_n )
    alpha_m = 0.1 * ( 25.0 - V_init ) / \
      ( np.exp ( ( 25.0 - V_init ) / 10.0 ) - 1.0 )
    beta_m = 4.0 * np.exp ( - V_init / 18.0 )
    m_init = alpha_m / ( alpha_m + beta_m )
    alpha_h = 0.07 * np.exp ( - V_init / 20.0 )
    beta_h = 1.0 / ( np.exp ( ( 30.0 - V_init ) / 10.0 ) + 1.0 )
    h_init = alpha_h / ( alpha_h + beta_h )
    axon_parameters.y0_default = np.array ( [ V_init, n_init, m_init, h_init ] )

  if not hasattr ( axon_parameters, "tstop_default" ):
    axon_parameters.tstop_default = 10.0
#
#  Update defaults if input was supplied.
#
  if ( C_user is not None ):
    axon_parameters.C_default = C_user

  if ( E_K_user is not None ):
    axon_parameters.E_K_default = E_K_user

  if ( E_Na_user is not None ):
    axon_parameters.E_Na_default = E_Na_user

  if ( E_rest_user is not None ):
    axon_parameters.E_rest_default = E_rest_user

  if ( G_K_user is not None ):
    axon_parameters.G_K_default = G_K_user

  if ( G_Na_user is not None ):
    axon_parameters.G_Na_default = G_Na_user

  if ( t0_user is not None ):
    axon_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    axon_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    axon_parameters.tstop_default = tstop_user
#
#  Return values.
#
  C = axon_parameters.C_default
  E_K = axon_parameters.E_K_default
  E_Na = axon_parameters.E_Na_default
  E_rest = axon_parameters.E_rest_default
  G_K = axon_parameters.G_K_default
  G_Na = axon_parameters.G_Na_default
  t0 = axon_parameters.t0_default
  y0 = axon_parameters.y0_default
  tstop = axon_parameters.tstop_default
  
  return C, E_K, E_Na, E_rest, G_K, G_Na, t0, y0, tstop

def euler ( dydt, tspan, y0, n ):

#*****************************************************************************80
#
## euler() approximates the solution to an ODE using Euler's method.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    function dydt: points to a function that evaluates the right
#    hand side of the ODE.
#
#    real tspan[2]: contains the initial and final times.
#
#    real y0[m]: an array containing the initial condition.
#
#    integer n: the number of steps to take.
#
#  Output:
#
#    real t[n+1], y[n+1,m]: the times and solution values.
#
  import numpy as np

  if ( np.ndim ( y0 ) == 0 ):
    m = 1
  else:
    m = len ( y0 )

  t0 = tspan[0]
  tstop = tspan[1]
  dt = ( tstop - t0 ) / n
  t = np.zeros ( n + 1 )
  y = np.zeros ( [ n + 1, m ] )
  t[0] = t0
  y[0,:] = y0

  for i in range ( 0, n ):
    t[i+1] = t[i] + dt
    y[i+1,:] = y[i,:] + dt * ( dydt ( t[i], y[i,:] ) )

  return t, y

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
  axon_ode_test ( )
  timestamp ( )

