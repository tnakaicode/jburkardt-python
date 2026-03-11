#! /usr/bin/env python3
#
def stetter_backward_euler ( n ):

#*****************************************************************************80
#
## stetter_backward_euler() uses the backward Euler method on stetter_ode().
#
#  Discussion:
#
#    We can't use a black-box backward Euler method, because we want to
#    alternate between two step sizes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
#  Output:
#
#    real T(N+1), Y(N+1): the times and estimated solutions.
#
  import numpy as np

  t0, y0, tstop = stetter_parameters ( )

  t = np.zeros ( n + 1 )
  y = np.zeros ( n + 1 )

  t[0] = t0
  y[0] = y0

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):
      dt = 0.5
    else:
      dt = 7.0

    t[i+1] = t[i] + dt
#
#                        y(i+1) = y(i) + dt * lambda(t(i+1)) * y(i+1)
#  1-dt*lambda(t(i+1)) * y(i+1) = y(i)
#                        y(i+1) = y(i) / ( 1-dt*lambda(t(i+1)) )
#
    y[i+1] = y[i] / ( 1.0 - dt * stetter_lambda ( t[i+1] ) )

  return t, y

def stetter_backward_euler_test ( n ):

#*****************************************************************************80
#
## stetter_backward_euler_test() uses backward Euler method on stetter_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stetter_backward_euler_test():' )
  print ( '  Solve stetter_ode() using backward_euler().' )

  t, y = stetter_backward_euler ( n )

  plt.plot ( t, y, 'r-o', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stetter, backward euler' )
  filename = 'stetter_backward_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def stetter_deriv ( t, y ):

#*****************************************************************************80
#
## stetter_deriv() evaluates the right hand side of stetter_ode().
#
#  Discussion:
#
#    y' = lam(t) * y
#
#    where lam(t) is periodic, piecewise linear, and discontinuous.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, Y: the time and solution value.
#
#  Output:
#
#    real DYDT: the derivative value.
#
  lam = stetter_lambda ( t )
#
#  Y might be a vector.
#  If so, we need to ensure that it is a column vector.
#
  dydt = lam * y

  return dydt

def stetter_euler ( n ):

#*****************************************************************************80
#
## stetter_euler() uses the Euler method on stetter_ode().
#
#  Discussion:
#
#    We can't use a black-box Euler method, because we want to
#    alternate between two step sizes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
#  Output:
#
#    real T(N+1), Y(N+1): the times and estimated solutions.
#
  import numpy as np

  t0, y0, tstop = stetter_parameters ( )

  t = np.zeros ( n + 1 )
  y = np.zeros ( n + 1 )

  t[0] = t0
  y[0] = y0

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):
      dt = 0.5
    else:
      dt = 7.0

    t[i+1] = t[i] + dt
    y[i+1] = y[i] + dt * stetter_lambda ( t[i] ) * y[i]

  return t, y

def stetter_euler_test ( n ):

#*****************************************************************************80
#
## stetter_euler_test() uses euler() on stetter_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stetter_euler_test():' )
  print ( '  Solve stetter_ode() using euler().' )

  t, y = stetter_euler ( n )

  plt.plot ( t, y, 'r-o', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stetter_ode(): euler' )
  filename = 'stetter_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def stetter_lambda ( t ):

#*****************************************************************************80
#
## stetter_lambda() evaluates the lambda factor of stetter_ode().
#
#  Discussion:
#
#    y' = lam(t) * y
#
#    t   lam(t)  mod(t,7.5)  mod(t-0.5,7.5)  - mod(t,7.5)/0.5
#  ----- --------   ----------  ----------------------------------------
#    0.0   0         0          7.0                  0
#    0.5  -1         0.5        0                   -1
#    7.5   0         0          7.0                  0
#    8.0  -1         0.5        0                   -1
#   15.0   0         0          7.0                  0
#   15.5  -1         0.5        0                   -1
#   22.5   0
#   23.0  -1
#   30.0   0
#   30.5  -1
#   37.5   0
#   38.0  -1
#   45.0   0
#   45.5  -1
#   52.5   0
#   53.0  -1
#   60.0   0
#   
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T the time and solution value.
#
#  Output:
#
#    real lam: the value of lam.
#

#
#  T  might be a vector.
#  If so, we need to ensure that it is a column vector.
#
  lam = - ( t % 7.5 ) / 0.5

  return lam

def stetter_lambda_test ( ):

#*****************************************************************************80
#
## stetter_lambda_test() tests stetter_lambda().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stetter_lambda_test():' )
  print ( '  Plot lam(t) for stetter_ode().' )

  n = 121
  t = np.linspace ( 0.0, 30.0, n )
  y = np.ones ( n )
  dydt = stetter_deriv ( t, y )

  plt.clf ( )
  plt.plot ( t, dydt, 'ro' )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- lambda(T) --->' )
  plt.title ( 'stetter_ode(): lambda(T)' )
  filename = 'stetter_lambda.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def stetter_midpoint ( n ):

#*****************************************************************************80
#
## stetter_midpoint() uses the midpoint method on stetter_ode().
#
#  Discussion:
#
#    We can't use a black-box midpoint method, because we want to
#    alternate between two step sizes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
#  Output:
#
#    real T(N+1), Y(N+1): the times and estimated solutions.
#
  import numpy as np

  t0, y0, tstop = stetter_parameters ( )

  t = np.zeros ( n + 1 )
  y = np.zeros ( n + 1 )

  t[0] = t0
  y[0] = y0

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):
      dt = 0.5
    else:
      dt = 7.0

    tm = t[i] + 0.5 * dt
    ym = y[i] / ( 1.0 - 0.5 * dt * stetter_lambda ( tm ) )

    t[i+1] = t[i] + dt
    y[i+1] = 2.0 * ym - y[i]
 
  return t, y

def stetter_midpoint_test ( n ):

#*****************************************************************************80
#
## stetter_midpoint_test() uses the midpoint method on stetter_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stetter_midpoint_test()' )
  print ( '  Solve stetter_ode() using midpoint().' )

  t, y = stetter_midpoint ( n )

  plt.clf ( )
  plt.plot ( t, y, 'r-o', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stetter_ode(): midpoint' )
  filename = 'stetter_midpoint.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.close ( )

  return

def stetter_ode_test ( ):

#*****************************************************************************80
#
## stetter_ode_test() solves stetter_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'stetter_ode_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Solve stetter_ode().' )

  t0, z0, tstop = stetter_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    t0    = ', t0 )
  print ( '    z0    = ', z0 )
  print ( '    tstop = ', tstop )

  n = 10
  stetter_backward_euler_test ( n )

  n = 10
  stetter_euler_test ( n )

  stetter_lambda_test ( )

  n = 10
  stetter_midpoint_test ( n )

  n = 10
  stetter_trapezoidal_test ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'stetter_ode_test():' )
  print ( '  Normal end of execution.' )

  return

def stetter_parameters ( t0_user = None, y0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## stetter_parameters() returns the parameters for stetter_ode().
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
#    12 June 2021
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

  if not hasattr ( stetter_parameters, "t0_default" ):
    stetter_parameters.t0_default = 0.0

  if not hasattr ( stetter_parameters, "y0_default" ):
    stetter_parameters.y0_default = 1.0

  if not hasattr ( stetter_parameters, "tstop_default" ):
    stetter_parameters.tstop_default = 75.0
#
#  New values, if supplied on input, overwrite the current values.
#
  if ( t0_user is not None ):
    stetter_parameters.t0_default = t0_user

  if ( y0_user is not None ):
    stetter_parameters.y0_default = y0_user

  if ( tstop_user is not None ):
    stetter_parameters.tstop_default = tstop_user
#
#  Return values.
#
  t0 = stetter_parameters.t0_default
  y0 = stetter_parameters.y0_default
  tstop = stetter_parameters.tstop_default
  
  return t0, y0, tstop

def stetter_trapezoidal ( n ):

#*****************************************************************************80
#
## stetter_trapezoidal() uses the trapezoidal method on stetter_ode().
#
#  Discussion:
#
#    We can't use a black-box trapezoidal method, because we want to
#    alternate between two step sizes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
#  Output:
#
#    real T(N+1), Y(N+1): the times and estimated solutions.
#
  import numpy as np

  t0, y0, tstop = stetter_parameters ( )

  t = np.zeros ( n + 1 )
  y = np.zeros ( n + 1 )

  t[0] = t0
  y[0] = y0

  for i in range ( 0, n ):

    if ( ( i % 2 ) == 0 ):
      dt = 0.5
    else:
      dt = 7.0
#
#                          yn = yo + 0.5 * dt * ( lam(to)*yo + lam(tn)*yn )
#  (1-0.5*dt*lam(tn)) * yn = yo * (1+0.5*dt*lam(to)
#                          yn = yo * (1+0.5*dt*lam(to) / (1-0.5*dt*lam(tn))
#
    t[i+1] = t[i] + dt

    c = ( 1.0 + 0.5 * dt * stetter_lambda ( t[i] ) ) \
      / ( 1.0 - 0.5 * dt * stetter_lambda ( t[i+1] ) )

    y[i+1] = y[i] * c

  return t, y 

def stetter_trapezoidal_test ( n ):

#*****************************************************************************80
#
## stetter_trapezoidal_test() uses the trapezoidal method on stetter_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the number of steps to take.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stetter_trapezoidal_test():' )
  print ( '  Use stetter_trapezoidal() to solve stetter_ode().' )

  t, y = stetter_trapezoidal ( n )

  plt.clf ( )
  plt.plot ( t, y, 'r-o', linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<-- t -->' )
  plt.ylabel ( '<-- y(t) -->' )
  plt.title ( 'stetter_ode(): trapezoidal' )
  filename = 'stetter_trapezoidal.png'
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
  stetter_ode_test ( )
  timestamp ( )

