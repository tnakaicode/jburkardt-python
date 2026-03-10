#! /usr/bin/env python3
#
from mpmath import *

def flame_deriv ( t, y ):

#*****************************************************************************80
#
## flame_deriv() evaluates the derivative of flame_ode().
#
#  Discussion:
#
#    1 equation.
#
#    Moler attributes this problem to Lawrence Shampine.
#
#    The equation describes the radius of a ball of flame that
#    begins, at time 0, at DELTA.
#
#      Y(0) = DELTA
#
#    The rate of fuel consumption is proportional to the volume, and
#    the rate of fuel intake is proportional to the area of the ball.
#    We take the constant of proportionality to be 1.
#
#      Y' = Y^2 - Y^3
#
#    The data is normalized so that Y = 1 is the equilibrium solution.
#
#    The computation is to be made from T = 0 to T = 2/DELTA.
#
#    For values of DELTA close to 1, such as 0.01, the equation is
#    not stiff.  But for DELTA = 0.0001, the equation can become
#    stiff as the solution approaches the equilibrium solution Y = 1,
#    and computed solutions may be wildly inaccurate or cautious
#    solvers may take very small timesteps.
#
#    The exact solution involves the Lambert W function, defined by
#
#      W(z) * exp ( W(z) ) = z
#
#    and if we set
#
#      A = ( 1 / DELTA - 1 )
#
#    then
#
#      Y(T) = 1 / ( W(A*exp(A-T)) + 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Cleve's Corner: Stiff Differential Equations,
#    MATLAB News and Notes,
#    May 2003, pages 12-13.
#
#  Input:
#
#    real T, Y: the arguments of the derivative.
#
#  Output:
#
#    real DYDT: the value of the derivative.
#
  dydt = y**2 * ( 1.0 - y )

  return dydt

def flame_exact ( t ):

#*****************************************************************************80
#
## flame_exact() evaluates the exact solution of flame_ode().
#
#  Discussion:
#
#    1 equation.
#
#    Moler attributes this problem to Lawrence Shampine.
#
#    The equation describes the radius of a ball of flame that
#    begins, at time 0, at DELTA.
#
#      Y(0) = DELTA
#
#    The rate of fuel consumption is proportional to the volume, and
#    the rate of fuel intake is proportional to the area of the ball.
#    We take the constant of proportionality to be 1.
#
#      Y' = Y^2 - Y^3
#
#    The data is normalized so that Y = 1 is the equilibrium solution.
#
#    The computation is to be made from T = 0 to T = 2/DELTA.
#
#    For values of DELTA close to 1, such as 0.01, the equation is
#    not stiff.  But for DELTA = 0.0001, the equation can become
#    stiff as the solution approaches the equilibrium solution Y = 1,
#    and computed solutions may be wildly inaccurate or cautious
#    solvers may take very small timesteps.
#
#    The exact solution involves the Lambert W function, defined by
#
#      W(z) * exp ( W(z) ) = z
#
#    and if we set
#
#      A = ( 1 / DELTA - 1 )
#
#    then
#
#      Y(T) = 1 / ( W(A*exp(A-T)) + 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Cleve's Corner: Stiff Differential Equations,
#    MATLAB News and Notes,
#    May 2003, pages 12-13.
#
#  Input:
#
#    real T(:): the times.
#
#  Output:
#
#    real Y(:), the exact solution values.
#
  t0, y0, tstop = flame_parameters ( )

  a = ( 1.0 - y0 ) / y0
  y = 1.0 / re ( lambertw ( a * exp ( a - ( t - t0 ) ) ) + 1.0 )

  return y

def flame_odefun_test ( ):

#*****************************************************************************80
#
## flame_odefun_test() solves flame_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'flame_odefun():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  odefun() solves flame_ode().' )

  t0, y0, tstop = flame_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0 =    ', t0 )
  print ( '    y0 =    ', y0 )
  print ( '    tstop = ', tstop )

  print ( '' )
  print ( mp )

  flame_odefun ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'flame_odefun():' )
  print ( '  Normal end of execution.' )
  return

def flame_odefun ( ):

#*****************************************************************************80
#
## flame_odefun() applies odefun() to flame_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 February 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  t0, y0, tstop = flame_parameters ( )
#
#  Plot the exact solution.
#
  plot ( lambda t: flame_exact ( t ), [ t0, tstop ], file = 'flame_exact.png' )
  plt.close ( )
#
#  Solve the ODE.
#
  f = odefun ( lambda t, y: flame_deriv ( t, y ), t0, y0 )
#
#  Plot the solution curve.
#
  plot ( lambda t: f ( t ), [ t0, tstop ], file = 'flame_odefun.png' )
  plt.close ( )

  return

def flame_parameters ( t0_user = None, y0_user = None, \
  tstop_user = None ):

#*****************************************************************************80
#
## flame_parameters() returns the parameters of flame_ode().
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
#    05 February 2022
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
#
#  Initialize defaults.
#
  if not hasattr ( flame_parameters, "t0_default" ):
    flame_parameters.t0_default = mpf ( 0.0 )

  if not hasattr ( flame_parameters, "y0_default" ):
    delta = mpf ( 0.01 )
    flame_parameters.y0_default = delta

  if not hasattr ( flame_parameters, "tstop_default" ):
    delta = flame_parameters.y0_default
    flame_parameters.tstop_default = mpf ( 2.0 ) / delta
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    flame_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    flame_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    flame_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = flame_parameters.t0_default
  y0 = flame_parameters.y0_default
  tstop = flame_parameters.tstop_default
  
  return t0, y0, tstop

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
  flame_odefun_test ( )
  timestamp ( )

