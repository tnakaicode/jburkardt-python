#! /usr/bin/env python3
#
from mpmath import *

def reaction_twoway_conserved ( y1, y2 ):

#*****************************************************************************80
#
## reaction_twoway_conserved() evaluates a quantity that should be conserved.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Y(:,2): the variable values.
#
#  Output:
#
#    real H(:): the conserved quantity.
#
  h = y1 + y2

  return h

def reaction_twoway_deriv ( t, y ):

#*****************************************************************************80
#
## reaction_twoway_deriv(): right hand side of reaction_twoway_ode().
#
#  Discussion:
#
#    The reactions involve chemicals W1 and W2, and have the form
#
#    dW1dt = - k1 W1(t) + k2 W2(t)
#    dW2dt = + k1 W1(t) - k2 W2(t)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2022
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
#    real T, Y(2): the time and variable values.
#
#  Output:
#
#    real DYDT(2): the right hand sides of the ODE.
#
  k1, k2, t0, y0, tstop = reaction_twoway_parameters ( )

  w1 = y[0]
  w2 = y[1]

  dw1dt = - k1 * w1 + k2 * w2
  dw2dt = + k1 * w1 - k2 * w2
 
  dydt = [ dw1dt, dw2dt ]

  return dydt

def reaction_twoway_odefun ( ):

#*****************************************************************************80
#
## reaction_twoway_odefun() solves reaction_twoway_ode() using odefun().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2022
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
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'reaction_twoway_odefun():' )
  print ( '  Solve reaction_twoway_ode() using odefun()' )
#
#  Get parameter values.
#
  k1, k2, t0, y0, tstop = reaction_twoway_parameters ( )
#
#  Report MP settings.
#
  print ( '' )
  print ( mp )
#
#  Plot the exact solution.
#
  plot ( lambda t: reaction_twoway_exact ( t )[0], [ t0, tstop ], file = 'reaction_twoway0_exact.png' )
  plt.close ( )

  plot ( lambda t: reaction_twoway_exact ( t )[1], [ t0, tstop ], file = 'reaction_twoway1_exact.png' )
  plt.close ( )
#
#  Solve the ODE.
#
  f = odefun ( lambda t, y: reaction_twoway_deriv ( t, y ), t0, y0 )
#
#  Plot the solution curve.
#
  plot ( lambda t: f ( t )[0], [ t0, tstop ], file = 'reaction_twoway0_odefun.png' )
  plt.close ( )

  plot ( lambda t: f ( t )[1], [ t0, tstop ], file = 'reaction_twoway1_odefun.png' )
  plt.close ( )

  return

def reaction_twoway_exact ( t ):

#*****************************************************************************80
#
## reaction_twoway_exact() returns the exact solution of reaction_twoway_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2022
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
#    real Y(2): the exact solution.
#
  k1, k2, t0, y0, tstop = reaction_twoway_parameters ( )

  w10 = y0[0]
  w20 = y0[1]

  w1 = ( k2 * ( w10 + w20 ) \
     + exp ( - ( k1 + k2 ) * t ) * ( k1 * w10 - k2 * w20 ) ) / ( k1 + k2 )
  w2 = ( k1 * ( w10 + w20 ) \
     - exp ( - ( k1 + k2 ) * t ) * ( k1 * w10 - k2 * w20 ) ) / ( k1 + k2 )

  y =  [ w1, w2 ]

  return y

def reaction_twoway_odefun_test ( ):

#*****************************************************************************80
#
## reaction_twoway_odefun_test() solves reaction_twoway_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2022
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'reaction_twoway_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve reaction_twoway_ode().' )
  print ( '' )
  print ( '  Reaction differential equation:' )
  print ( '    dW1/dt = - k1 W1 + k2 W2' )
  print ( '    dW2/dt = + k1 W1 - k2 W2' )
#
#  Get parameter values.
#
  k1, k2, t0, y0, tstop = reaction_twoway_parameters ( )
#
#  Report parameter values.
#
  print ( '' )
  print ( '  parameters:' )
  print ( '    k1    = ', k1, ', (reaction rate)' )
  print ( '    k2    = ', k2, ', (reaction rate)' )
  print ( '    t0    = ', t0, ', (initial time, in seconds s)' )
  print ( '    w10   = ', y0[0], ', (initial amount of species W1)' )
  print ( '    w20   = ', y0[1], ', (initial amount of species W2)' )
  print ( '    tstop = ', tstop, ', (final time, in seconds s)' )
#
#  Call the solver.
#
  reaction_twoway_odefun ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'reaction_twoway_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def reaction_twoway_parameters ( k1_user = None, k2_user = None, \
  t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## reaction_twoway_parameters() returns parameters for reaction_twoway_ode().
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
#    07 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real K1_USER, K2_USER: the reaction rates.
#    The value of K2 is suggested to be 10, 100, or 1000.
#
#    real T0_USER: the initial time.
#
#    real Y0_USER: the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real K1, K2: the reaction rates.
#
#    real T0: the initial time.
#
#    real Y0: the initial condition.
#
#    real TSTOP: the final time.
#

#
#  Initialize defaults.
#
  if not hasattr ( reaction_twoway_parameters, "k1_default" ):
    reaction_twoway_parameters.k1_default = mpf ( 1.0 )

  if not hasattr ( reaction_twoway_parameters, "k2_default" ):
    reaction_twoway_parameters.k2_default = mpf ( 10.0 )

  if not hasattr ( reaction_twoway_parameters, "t0_default" ):
    reaction_twoway_parameters.t0_default = mpf ( 0.0 )

  if not hasattr ( reaction_twoway_parameters, "y0_default" ):
    reaction_twoway_parameters.y0_default = [ 0.1, 0.9 ]

  if not hasattr ( reaction_twoway_parameters, "tstop_default" ):
    reaction_twoway_parameters.tstop_default =  mpf ( 1.0 )
#
#  Update defaults if input was supplied.
#
  if ( k1_user is not None ):
    reaction_twoway_parameters.k1_default = k1_user

  if ( k2_user is not None ):
    reaction_twoway_parameters.k2_default = k2_user

  if ( t0_user is not None ):
    reaction_twoway_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    reaction_twoway_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    reaction_twoway_parameters.tstop_default = tstop_user
#
#  Return values.
#
  k1 = reaction_twoway_parameters.k1_default
  k2 = reaction_twoway_parameters.k2_default
  t0 = reaction_twoway_parameters.t0_default
  y0 = reaction_twoway_parameters.y0_default
  tstop = reaction_twoway_parameters.tstop_default
  
  return k1, k2, t0, y0, tstop

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
  reaction_twoway_odefun_test ( )
  timestamp ( )

