#! /usr/bin/env python3
#
def reaction_conserved ( y ):

#*****************************************************************************80
#
## reaction_conserved() evaluates a quantity that should be conserved.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Y(3): the variable values.
#
#  Output:
#
#    real H: the conserved quantity.
#
  a = y[0]
  b = y[1]
  c = y[2]

  h = a + b + 2.0 * c

  return h

def reaction_deriv ( t, y ):

#*****************************************************************************80
#
## reaction_deriv() evaluates the right hand sides of reaction_ode().
#
#  Discussion:
#
#    The chemical reaction is A+B -> C with rate k.
#
#    dAdt = - kAB
#    dBdt = - kAB
#    dCdt = + kAB
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y(3): the time and variable values.
#
#  Output:
#
#    real DYDT(3): the right hand sides of the ODE.
#
  import numpy as np

  k, t0, y0, tstop = reaction_parameters ( )

  a = y[0]
  b = y[1]
  c = y[2]

  dadt = - k * a * b
  dbdt = - k * a * b
  dcdt = + k * a * b
  
  dydt = np.array ( [ dadt, dbdt, dcdt ] )

  return dydt

def reaction_exact ( t ):

#*****************************************************************************80
#
## reaction_exact() returns the exact solution of reaction_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Willem Hundsdorfer, Jan Verwer,
#    Numerical solution of time-dependent advection-diffusion-reaction equations,
#    Springer, 2003
#    ISBN: 978-3-662-09017-6
#
#  Input:
#
#    real T: the current time.
#
#  Output:
#
#    real Y(3): the exact solution.
#
  import numpy as np

  k, t0, y0, tstop = reaction_parameters ( )

  a0 = y0[0]
  b0 = y0[1]
  c0 = y0[2]
  d0 = a0 - b0

  if ( d0 == 0 ):
    qt = k * t
  else:
    qt = ( 1.0 - np.exp ( - k * t * d0 ) ) / d0

  at = a0 / ( 1.0 + b0 * qt )
  bt = at - d0
  ct = c0 + ( a0 - at )

  y = np.array ( [ at, bt, ct ] )

  return y

def reaction_ode_test ( ):

#*****************************************************************************80
#
## reaction_ode_test() solves reaction_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'reaction_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve reaction_ode().' )
  print ( '' )
  print ( '  Reaction differential equation:' )
  print ( '    da/dt = - k a b' )
  print ( '    db/dt = - k a b' )
  print ( '    dc/dt = + k a b' )
#
#  Get parameter values.
#
  k, t0, y0, tstop = reaction_parameters ( )
#
#  Report parameter values.
#
  print ( '' )
  print ( '  parameters:' )
  print ( '    k     = ', k,     ', (reaction rate)' )
  print ( '    t0    = ', t0,    ', (initial time, in seconds s)' )
  print ( '    a0    = ', y0[0], ', (initial amount of species a in Mol/L)' )
  print ( '    b0    = ', y0[1], ', (initial amount of species b in Mol/L)' )
  print ( '    c0    = ', y0[2], ', (initial amount of species c in Mol/L)' )
  print ( '    tstop = ', tstop, ', (final time, in seconds s)' )

  reaction_solve_ivp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'reaction_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def reaction_solve_ivp ( ):

#*****************************************************************************80
#
## reaction_solve_ivp() uses solve_ivp() to solve reaction_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2021
#
#  Author:
#
#    John Burkardt
#
  from scipy.integrate import solve_ivp
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'reaction_solve_ivp():' )
  print ( '  Use solve_ivp() to solve reaction_ode().' )
#
#  Get parameter values.
#
  k, t0, y0, tstop = reaction_parameters ( )
#
#  Solve the equation.
#
  f = reaction_deriv
  tspan = np.array ( [ t0, tstop ] )
  n = 101
  t = np.linspace ( t0, tstop, n )

  sol = solve_ivp ( f, tspan, y0, t_eval = t )
#
#  Evaluate exact solution.
#
  ye = reaction_exact ( t )
#
#  Plot.
#
  plt.plot ( t, sol.y[0], 'ro', linewidth = 3 )
  plt.plot ( t, sol.y[1], 'go', linewidth = 3 )
  plt.plot ( t, sol.y[2], 'bo', linewidth = 3 )
  plt.plot ( t, ye[0], 'c-', linewidth = 3 )
  plt.plot ( t, ye[1], 'm-', linewidth = 3 )
  plt.plot ( t, ye[2], 'y-', linewidth = 3 )
  plt.plot ( tspan, np.array([0.0,0.0]), 'k-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  Concentrations  --->' )
  plt.title ( 'A+B --k--> C reaction_ode(), solve_ivp()' )
  plt.legend ( ( 'A', 'B', 'C', 'Aexact', 'Bexact', 'Cexact', 'x axis' ) )
  filename = 'reaction_solve_ivp_solution.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  h = reaction_conserved ( sol.y )

  plt.plot ( t, h, 'r-', linewidth = 3 )
  plt.plot ( tspan, np.array ( [h[0],h[0]] ), 'b--', linewidth = 3 )
  plt.plot ( tspan, np.array ( [0.0,0.0] ), 'k-', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<---  t  --->' )
  plt.ylabel ( '<---  conserved quantity  --->' )
  plt.title ( 'reaction_ode() solve_ivp(): conservation' )
  plt.legend ( ( 'h', 'h initial', 'x axis' ) )
  filename = 'reaction_solve_ivp_conservation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def reaction_parameters ( k_user = None, t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## reaction_parameters() returns parameters for reaction_ode().
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
#    03 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real K_USER: the reaction rate.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER[3]: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real K: the reaction rate.
#
#    real T0: the initial time.
#
#    real Y0[3]: the initial condition.
#
#    real TSTOP: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( reaction_parameters, "k_default" ):
    reaction_parameters.k_default = 0.02

  if not hasattr ( reaction_parameters, "t0_default" ):
    reaction_parameters.t0_default = 0.0

  if not hasattr ( reaction_parameters, "y0_default" ):
    a0 = 10.0
    b0 = 12.0
    c0 = 3.0
    reaction_parameters.y0_default = np.array ( [ a0, b0, c0 ] )

  if not hasattr ( reaction_parameters, "tstop_default" ):
    reaction_parameters.tstop_default = 20.0
#
#  Update defaults if input was supplied.
#
  if ( k_user is not None ):
    reaction_parameters.k_default = k_user

  if ( t0_user is not None ):
    reaction_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    reaction_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    reaction_parameters.tstop_default = tstop_user
#
#  Return values.
#
  k = reaction_parameters.k_default
  t0 = reaction_parameters.t0_default
  y0 = reaction_parameters.y0_default
  tstop = reaction_parameters.tstop_default
  
  return k, t0, y0, tstop

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
  reaction_ode_test ( )
  timestamp ( )

