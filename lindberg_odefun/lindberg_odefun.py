#! /usr/bin/env python3
#
from mpmath import *

def lindberg_deriv ( t, y ):

#*****************************************************************************80
#
## lindberg_deriv() returns the derivative for lindberg_ode().
#
#  Discussion:
#
#    Note that components y1(t) and y2(t) first sink to extraordinarily
#    small values, and then undergo explosive growth, sometime before t=1.
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
#    Bengt Lindberg,
#    On a dangerous property of methods for stiff differential equations,
#    BIT Numerical Mathematics,
#    Volume 14, 1974, pages 430-436.
#
#    Daniel Watanabe, Qasim Sheikh,
#    One-leg formulas for stiff ordinary differential equations,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 5, Number 2, June 1984, pages 489-496.
#
#  Input:
#
#    real T: the current time.
#
#    real Y(4): the current solution value.
#
#  Output:
#
#    real DYDT(4): the value of dY/dT.
#
  y1 = y[0]
  y2 = y[1]
  y3 = y[2]
  y4 = y[3]

  dydt = [ \
      10.0**4 * y1 * y3 + 10.0**4 * y2 * y4, \
    - 10.0**4 * y1 * y4 + 10.0**4 * y2 * y3, \
      1.0 - y3, \
    - 0.5 * y3 - y4 + 0.5 ]
 
  return dydt

def lindberg_exact ( x ):

#*****************************************************************************80
#
## lindberg_exact() evaluates the exact solution of lindberg_ode().
#
#  Discussion:
#
#    The formula was supplied by Wenlong Pei.
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
#    real x(n): the evaluation points.
#
#  Output:
#
#    real y(n,4): the function values.
#
  import numpy as np

  g1 = 10.0**4 * ( x + 2.0 * exp ( - x ) - 2.0 )
  g2 = 10.0**4 * ( 1.0 - exp ( - x ) - x * exp ( -x ) )

  y = [ \
    exp ( g1 ) * ( cos ( g2 ) + sin ( g2 ) ), \
    exp ( g1 ) * ( cos ( g2 ) - sin ( g2 ) ), \
    1.0 - 2.0 * exp ( - x ), \
    x * exp ( - x ) ]
 
  return y

def lindberg_odefun ( ):

#*****************************************************************************80
#
## lindberg_odefun() solves lindberg_ode() using odefun().
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
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'lindberg_odefun():' )
  print ( '  Solve lindberg_ode() using odefun().' )

  t0, y0, tstop = lindberg_parameters ( )
#
#  Plot the 4 components of the exact solution.
#
  plot ( lambda t: lindberg_exact ( t )[0], [ t0, tstop ], file = 'lindberg0_exact.png' )
  plt.close ( )

  plot ( lambda t: lindberg_exact ( t )[1], [ t0, tstop ], file = 'lindberg1_exact.png' )
  plt.close ( )

  plot ( lambda t: lindberg_exact ( t )[2], [ t0, tstop ], file = 'lindberg2_exact.png' )
  plt.close ( )

  plot ( lambda t: lindberg_exact ( t )[3], [ t0, tstop ], file = 'lindberg3_exact.png' )
  plt.close ( )
#
#  Call odefun() to approximate the solution.
#
  f = odefun ( lambda t, y: lindberg_deriv ( t, y ), t0, y0 )
#
#  Plot the 4 components of the solution curve.
#
  plot ( lambda t: f ( t )[0], [ t0, tstop ], file = 'lindberg0_odefun.png' )
  plt.close ( )

  plot ( lambda t: f ( t )[1], [ t0, tstop ], file = 'lindberg1_odefun.png' )
  plt.close ( )

  plot ( lambda t: f ( t )[2], [ t0, tstop ], file = 'lindberg2_odefun.png' )
  plt.close ( )

  plot ( lambda t: f ( t )[3], [ t0, tstop ], file = 'lindberg3_odefun.png' )
  plt.close ( )

  return

def lindberg_odefun_test ( ):

#*****************************************************************************80
#
## lindberg_odefun_test() tests lindberg_odefun().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'lindberg_odefun_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve lindberg_odefun().' )

  t0, y0, tstop = lindberg_parameters ( )
#
#  Perhaps reduce the default stopping time. 
#
# tstop = mpf ( 0.55 )
# tstop = mpf ( 0.60 )
# tstop = mpf ( 0.80 )
  tstop = mpf ( 1.50 )

  t0, y0, tstop = lindberg_parameters ( t0, y0, tstop )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0    = ', t0 )
  print ( '    y0    = ', y0 )
  print ( '    tstop = ', tstop )
#
#  Print MP settings.
#
  print ( '' )
  print ( mp )
#
#  Solve the equation.
#
  lindberg_odefun ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lindberg_odefun_test():' )
  print ( '  Normal end of execution.' )

  return

def lindberg_parameters ( t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## lindberg_parameters() returns the parameters of lindberg_ode().
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
#    real T0_USER: the initial time.
#
#    real Y0_USER(4): the initial condition.
#
#    real TSTOP_USER: the final time.
#
#  Output:
#
#    real T0: the initial time.
#
#    real Y0(4): the initial condition.
#
#    real TSTOP: the final time.
#

#
#  Initialize defaults.
#
  if not hasattr ( lindberg_parameters, "t0_default" ):
    lindberg_parameters.t0_default = mpf ( 0.0 )

  if not hasattr ( lindberg_parameters, "y0_default" ):
    lindberg_parameters.y0_default = [ 1.0, 1.0, -1.0, 0.0 ]

  if not hasattr ( lindberg_parameters, "tstop_default" ):
    lindberg_parameters.tstop_default = mpf ( 3.91 )
#
#  Update defaults if input was supplied.
#
  if ( t0_user is not None ):
    lindberg_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    lindberg_parameters.y0_default = y0_user.copy()

  if ( tstop_user is not None ):
    lindberg_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = lindberg_parameters.t0_default
  y0 = lindberg_parameters.y0_default.copy ( )
  tstop = lindberg_parameters.tstop_default
  
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

if ( __name__ == "__main__" ):
  timestamp ( )
  lindberg_odefun_test ( )
  timestamp ( )

