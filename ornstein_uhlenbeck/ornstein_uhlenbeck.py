#! /usr/bin/env python3
#
def ornstein_uhlenbeck_euler ( theta, mu, sigma, x0, tmax, n, rng ):

#*****************************************************************************80
#
## ornstein_uhlenbeck_euler() applies the Euler method to the Ornstein-Uhlenbeck SDE.
#
#  Discussion:
#
#    The stochastic differential equation (SDE) is:
#
#      dx(t) = theta * ( mu - x(t) ) dt + sigma dW,   
#      x(0) = x0.
#
#    The discretized Brownian path uses a constant stepsize.
#
#    For an SDE of the form:
#
#      dx = f(x(t)) dt + g(x(t)) dW(t),
#
#    the Euler method has the form:
#
#      x(j) = x(j-1) + f(x(j-1)) * dt + g(x(j-1)) * dW(j-1)
#
#    Note that if SIGMA is zero, the problem becomes deterministic,
#    with solution:
#
#      x(t) = mu + ( x0 - mu ) * exp ( - theta * t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546
#
#  Input:
#
#    real THETA, MU, SIGMA, the value of problem parameters.
#
#    real X0, the initial condition.  When studying many
#    realizations of this problem, it is usual for X0 to be chosen
#    from a normal distribution.
#
#    real TMAX, the final time.
#
#    integer N, the number of time steps.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'ornstein_uhlenbeck_euler():' )
  print ( '  Use the Euler method to approximate the solution of' )
  print ( '  the Ornstein-Uhlenbeck stochastic differential equation:' )
  print ( '' )
  print ( '    d x(t) = theta * ( mu - x(t) ) dt + sigma dW' )
  print ( '' )
  print ( '  with initial condition x(0) = x0.' )
#
#  Set the discrete time stepsize.
#
  dt = tmax / n
#
#  Compute the Brownian increments.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
#
#  Carry out the Euler approximate integration process.
#
  t = np.linspace ( 0, tmax, n + 1 )
  x = np.zeros ( n + 1 )

  x[0] = x0
  for j in range ( 0, n ):
    x[j+1] = x[j] + dt * theta * ( mu - x[j] ) + sigma * dw[j]
#
#  Plot the approximate solution.
#
  plt.clf ( )
  plt.plot ( t, x, 'r-', linewidth = 3 )
  plt.xlabel ( 't' )
  plt.ylabel ( 'X(t)' )
  plt.title ( 'Euler solution of Ornstein-Uhlenbeck SDE' )
  plt.grid ( True )
  filename = 'ornstein_uhlenbeck_euler.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def ornstein_uhlenbeck_euler_maruyama ( theta, mu, sigma, x0, tmax, n, r, rng ):

#*****************************************************************************80
#
## ornstein_uhlenbeck_euler_maruyama() applies Euler-Maruyama to the Ornstein-Uhlenbeck SDE.
#
#  Discussion:
#
#    The stochastic differential equation (SDE) is:
#
#      dx = theta * ( mu - x(t) ) dt + sigma dW,   
#      x(0) = x0,
#
#    The discretized Brownian path uses a constant stepsize.
#
#    A "large" time step DT_LARGE is used for the smooth portion of the
#    equation, while a smaller time step DT_SMALL is used for the
#    discretized Brownian path.  We take R small steps to equal one 
#    large step, so that:
#
#      dt_large = r * dt_small = tmax / n
#
#    For an SDE of the form:
#
#      dx = f(x(t)) dt + g(x(t)) dW(t)
#
#    the Euler-Maruyama method has the form:
#
#      x(j) = x(j-1) + f(X(j-1)) * dt_large + g(X(j-1)) * dW(j-1)
#
#    where dW(j-1) is approximated by the sum of R normal random values
#    multiplied by the square root of DT_SMALL.
#
#    Note that if SIGMA is zero, the problem becomes deterministic,
#    with solution
#
#      x(t) = mu + ( x0 - mu ) * exp ( - theta * t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546
#
#  Input:
#
#    real THETA, MU, SIGMA, the value of problem parameters.
#
#    real X0, the initial condition.  When studying many
#    realizations of this problem, it is usual for X0 to be chosen
#    from a normal distribution.
#
#    real TMAX, the final time.
#
#    integer N, the number of large scale time steps.
#
#    integer R, the number of small scale time steps per single
#    large scale time step.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'ornstein_uhlenbeck_euler_maruyama():' )
  print ( '  Use the Euler-Maruyama method to approximate the solution of' )
  print ( '  the Ornstein-Uhlenbeck stochastic differential equation:' )
  print ( '' )
  print ( '    d x(t) = theta * ( mu - x(t) ) dt + sigma dW' )
  print ( '' )
  print ( '  with initial condition x(0) = x0.' )
#
#  Set time steps.
#
  dt_large = tmax / n
  dt_small = tmax / n / r
#
#  Carry out the Euler-Maruyama approximate integration process.
#
  t = np.linspace ( 0, tmax, n + 1 )
  x = np.zeros ( n + 1 )

  x[0] = x0
  for j in range ( 0, n ):
    dw = np.sqrt ( dt_small ) * rng.standard_normal ( size = r )
    x[j+1] = x[j] + dt_large * theta * ( mu - x[j] ) + sigma * np.sum ( dw )
#
#  Plot the approximate solution.
#
  plt.clf ( )
  plt.plot ( t, x, 'r-', linewidth = 3 )
  plt.xlabel ( 't' )
  plt.ylabel ( 'X(t)' )
  plt.title ( 'Euler-Maruyama solution of Ornstein-Uhlenbeck SDE' )
  plt.grid ( True )
  filename = 'ornstein_uhlenbeck_maruyama.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def ornstein_uhlenbeck_euler_maruyama_test ( rng ):

#*****************************************************************************80
#
## ornstein_uhlenbeck_euler_maruyama_test() tests ornstein_uhlenbeck_euler_maruyama().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'ornstein_uhlenbeck_euler_maruyama_test():' )
  print ( '  Estimate a solution to the Ornstein-Uhlenbeck equation' )
  print ( '  using the Euler-Maruyama method for stochastic ' )
  print ( '  differential equations.' )
  print ( '' )

  theta = 2.0
  print ( '  Using decay rate THETA = ', theta )
  mu = 1.0
  print ( '  Using mean MU = ', mu )
  sigma = 0.15
  print ( '  Using variance SIGMA = ', sigma )
  x0 = 2.0
  print ( '  Using initial value X0 = ', x0 )
  tmax = 3.0
  print ( '  Using final time TMAX = ', tmax )
  n = 10000
  print ( '  Using number of large timesteps N = ', n )
  r = 16
  print ( '  Using R = ', r, ' small time steps per one large time step' )

  ornstein_uhlenbeck_euler_maruyama ( theta, mu, sigma, x0, tmax, n, r, rng )

  return

def ornstein_uhlenbeck_euler_test ( rng ):

#*****************************************************************************80
#
## ornstein_uhlenbeck_euler_test() tests ornstein_uhlenbeck_euler().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'ornstein_uhlenbeck_euler_test():' )
  print ( '  Estimate a solution to the Ornstein-Uhlenbeck equation' )
  print ( '  using the Euler method for stochastic differential equations.' )
  print ( '' )

  theta = 2.0
  print ( '  Using decay rate THETA = ', theta )
  mu = 1.0
  print ( '  Using mean MU = ', mu )
  sigma = 0.15
  print ( '  Using variance SIGMA = ', sigma )
  x0 = 2.0
  print ( '  Using initial value X0 = ', x0 )
  tmax = 3.0
  print ( '  Using final time TMAX = ', tmax )
  n = 10000
  print ( '  Using number of timesteps N = ', n )

  ornstein_uhlenbeck_euler ( theta, mu, sigma, x0, tmax, n, rng )

  return

def ornstein_uhlenbeck_test ( ):

#*****************************************************************************80
#
## ornstein_uhlenbeck_test() tests ornstein_uhlenbeck().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'ornstein_uhlenbeck_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ornstein_uhlenbeck().' )

  rng = default_rng ( )

  ornstein_uhlenbeck_euler_test ( rng )
  ornstein_uhlenbeck_euler_maruyama_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'ornstein_uhlenbeck_test():' )
  print ( '  Normal end of execution.' )

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

if ( __name__ == "__main__" ):
  timestamp ( )
  ornstein_uhlenbeck_test ( )
  timestamp ( )

