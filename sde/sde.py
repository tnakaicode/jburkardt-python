#! /usr/bin/env python3
#
def sde_test ( ):

#*****************************************************************************80
#
## sde_test() tests sde().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 April 2025
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'sde_test():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  Test sde().' )

  rng = default_rng ( )

  bpath ( rng )
  bpath1 ( rng )
  bpath2 ( rng )
  bpath3 ( rng )
  bpath_average ( rng )
  bpath_vectorized ( rng )

  chain ( rng )

  em ( rng )
  emstrong ( rng )

  method = 0
  emweak ( rng, method )
  
  method = 1
  emweak ( rng, method )

  milstrong ( rng )

  stab ( rng )
  stab_asymptotic ( rng )
  stab_meansquare ( rng )

  stint ( rng )
  stochastic_integral_ito_test ( rng )
  stochastic_integral_strat_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'sde_test():' )
  print ( '  Normal end of execution.' )

  return

def bpath ( rng ):

#*****************************************************************************80
#
## bpath() performs a Brownian path simulation.
#
#  Discussion:
#
#    This routine computes one simulation of discretized Brownian 
#    motion over the time interval [0,1] using 500 time steps.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  from time import time
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'bpath():' )
  print ( '  Brownian path simulation' )

  tmax = 1.0 
  n = 500 
  dt = tmax / n
#
#  Begin timing.
#
  seconds = time ( )
#
#  Define the increments dW.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
#
#  W is the sum of the previous increments.
#
  t = np.linspace ( 0.0, tmax, n + 1 )
  w = np.zeros ( n + 1 )
  
  for j in range ( 0, n + 1 ):

    if ( j == 0 ):
      w[j] = 0.0
    else:
      w[j] = w[j-1] + dw[j-1] 
#
#  End timing.
#
  seconds = seconds - time ( )
  print ( '  Computation required ', seconds, ' seconds.' )
#
#  Plot t, W(t).
#
  plt.clf ( )
  plt.plot ( t, w, linewidth = 3, color = 'b' )
  plt.plot ( [0, tmax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.title ( 'Brownian motion realization by BPATH' )
  plt.xlabel ( 't', fontsize = 16 )
  plt.ylabel ( 'W_t', fontsize = 16, rotation = 0 )

  filename = 'bpath.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def bpath1 ( rng ):

#*****************************************************************************80
#
## bpath1() performs a Brownian path simulation.
#
#  Discussion:
#
#    This routine computes one simulation of discretized Brownian 
#    motion over the time interval [0,1] using 500 time steps.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'bpath1():' )
  print ( '  Brownian path simulation' )

  tmax = 1.0 
  n = 500 
  dt = tmax / n
#
#  Define the increments dW.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
#
#  W is the sum of the previous increments.
#
  t = np.linspace ( 0.0, tmax, n + 1 )
  w = np.zeros ( n + 1 )
  
  for j in range ( 0, n + 1 ):

    if ( j == 0 ):
      w[j] = 0.0
    else:
      w[j] = w[j-1] + dw[j-1] 
#
#  Plot W(t) against t.
#  We can include time 0 and value W0 in the plot.
#
  plt.clf ( )
  plt.plot ( t, w, linewidth = 3, color = 'b' )
  plt.plot ( [0, tmax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.title ( 'Brownian motion realization by BPATH1' )
  plt.xlabel ( 't', fontsize = 16 ) 
  plt.ylabel ( 'W_t', fontsize = 16, rotation = 0 )
  plt.grid ( True )

  filename = 'bpath1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def bpath2 ( rng ):

#*****************************************************************************80
#
## bpath2() performs a vectorized Brownian path simulation.
#
#  Discussion:
#
#    This routine computes one simulation of discretized Brownian 
#    motion over the time interval [0,1] using 500 time steps.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
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
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'bpath2():' )
  print ( '  Brownian path simulation' )

  T = 1.0 
  n = 500 
  dt = T / n
#
#  dW contains the increments.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
#
#  W(I) contains the cumulative sum of the increments 1 through I.
#
  w0 = 0.0
  w = np.cumsum ( dw )
  t = np.linspace ( 0, T, n + 1 )
#
#  Plot t versus W(t).
#
  plt.clf ( )
  plt.plot ( t, np.hstack ( ( [w0], w ) ), linewidth = 3, color = 'b' )
  plt.plot ( [0, T], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.title ( 'Brownian path realization computed by BPATH2' )
  plt.xlabel ( 't', fontsize = 16 )
  plt.ylabel ( 'W(t)', fontsize = 16, rotation = 0 )

  filename = 'bpath2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def bpath3 ( rng ):

#*****************************************************************************80
#
## bpath3() displays the average of 1000 Brownian paths.
#
#  Discussion:
#
#    This routine computes 1000 simulations of discretized Brownian 
#    motion W(t) over the time interval [0,1] using 500 time steps.
#
#    Actually, we are interested in a function u(W(t)):
#
#      u(W(t)) = exp ( t + W(t)/2 )
#
#    The routine plots 5 of the simulations, as well as the average
#    of all the simulations.  
#
#    The plot of the average should be quite smooth.  Its expected
#    value is exp ( 9 * t / 8 ), and we compute the 'error', that is,
#    the difference between the averaged value and this expected
#    value.  This 'error' should decrease as the number of simulation
#    is increased.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'bpath3():' )
  print ( '  Average 1000 Brownian path simulations.' )

  T = 1.0
  n = 500
  dt = T / n
  t = np.linspace ( 0.0, T, n + 1 )
#
#  We will be computing M paths simultaneously.
#
  M = 1000
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = [ M, n ] )
  w = np.cumsum ( dw, axis = 1 )
  w = np.hstack ( [ np.zeros ( [ M, 1 ] ), w ] )
  U = np.exp ( t + 0.5 * w )
  Umean = np.mean ( U, axis = 0 )
#
#  Plot the mean of the M paths.
#
  plt.clf ( )
  plt.plot ( t, Umean, 'b-' )
#
#  Overlay the plots of the first 5 paths.
#
  plt.plot ( t, np.transpose ( U[0:5,:] ), 'r--' )
  plt.grid ( True )

  plt.xlabel ( 't', fontsize = 16 )
  plt.ylabel ( 'U(t)', fontsize = 16, rotation = 0 )
  plt.legend ( [ 'mean of 1000 paths', '5 individual paths' ] )
  plt.title ( '1000 paths computed by bpath3()' )

  filename = 'bpath3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Sample error:
#
  averr = np.linalg.norm ( ( Umean - np.exp ( 9.0 * t / 8.0 ) ), np.inf )
  print ( '' )
  print ( '  Maximum error in averaged data is ', averr )

  return

def bpath_average ( rng ):

#*****************************************************************************80
#
## bpath_average() displays the average of 1000 Brownian paths.
#
#  Discussion:
#
#    This routine computes 1000 simulations of discretized Brownian 
#    motion W(t) over the time interval [0,1] using 500 time steps.
#
#    We are interested in a function u(W(t)):
#
#      u(W(t)) = exp ( t + W(t)/2 )
#
#    The routine plots 5 of the simulations, as well as the average
#    of all the simulations.  
#
#    The plot of the average should be quite smooth.  Its expected
#    value is exp ( 9 * t / 8 ), and we compute the 'error', that is,
#    the difference between the averaged value and this expected
#    value.  This 'error' should decrease as the number of simulation
#    is increased.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  from time import time
  import matplotlib.pyplot as plt
  import numpy as np
#
#  We will be computing M paths simultaneously.
#
  m = 1000
  print ( '' )
  print ( 'bpath_average():' )
  print ( '  Average ', m, ' Brownian path simulations.' )

  tmax = 1.0
  n = 500
  dt = tmax / n
  t = np.linspace ( 0.0, tmax, n + 1 )
#
#  Begin timing.
#
  seconds = time ( )
#
#  Set the increments.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = [ m, n ] )
#
#  Sum the increments.
#
  w = np.cumsum ( dw, axis = 1 )
  w = np.hstack ( [ np.zeros ( [ m, 1 ] ), w ] )
  U = np.exp ( t + 0.5 * w )
  umean = np.mean ( U, axis = 0 )
#
#  End timing.
#
  seconds = time ( ) - seconds
  print ( '  Computation required ', seconds, ' seconds.' )
#
#  Plot the mean of the M paths.
#
  plt.clf ( )

  plt.plot ( t, umean, 'b-', linewidth = 2 )
#
#  Overlay the plots of the first 5 paths.
#
  plt.plot ( t, np.transpose ( U[0:5,:] ), 'r--' )
  plt.grid ( True )

  plt.xlabel ( 't', fontsize = 16 )
  plt.ylabel ( 'U(t)', fontsize = 16, rotation = 0 )
  plt.title ( 'bpath_average: Mean of 1000 paths, and 5 sample paths' )

  filename = 'bpath_average.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Sample error:
#
  averr = np.linalg.norm ( ( umean - np.exp ( 9.0 * t / 8.0 ) ), ord = np.inf )
  print ( '' )
  print ( '  Maximum error in averaged data is ', averr )

  return

def bpath_vectorized ( rng ):

#*****************************************************************************80
#
## bpath_vectorized() performs a vectorized Brownian path simulation.
#
#  Discussion:
#
#    This routine computes one simulation of discretized Brownian 
#    motion over the time interval [0,1] using 500 time steps.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
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
#    rng(): the current random number generator.
#
  from time import time
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'bpath_vectorized():' )
  print ( '  Brownian path simulation' )

  tmax = 1.0 
  n = 500 
  dt = tmax / n
#
#  Begin timing.
#
  seconds = time ( )
#
#  dW contains the increments.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
#
#  W(I) contains the cumulative sum of the increments 1 through I.
#
  w = np.cumsum ( dw )
  w = np.hstack ( ( [0.0], w ) )
  t = np.linspace ( 0.0, tmax, n + 1 )
#
#  End timing.
#
  seconds = time ( ) - seconds
  print ( '  Computation required ', seconds, ' seconds' )
#
#  Plot t, W(t).
#
  plt.clf ( )
  plt.plot ( t, w, linewidth = 3, color = 'b' )
  plt.plot ( [0, tmax], [0.0, 0.0], linewidth = 2, color = 'k' )
  plt.grid ( True )
  plt.title ( 'Brownian path realization computed by BPATH_VECTORIZED' )
  plt.xlabel ( 't', fontsize = 16 )
  plt.ylabel ( 'W(t)', fontsize = 16, rotation = 0 )
 
  filename = 'bpath_vectorized.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def chain ( rng ):

#*****************************************************************************80
#
## chain() tests the stochastic Chain Rule.
#
#  Discussion:
#
#    This function solves a stochastic differential equation for 
#
#      V = sqrt(X) 
#
#    where X satisfies the stochastic differential equation:
# 
#      dX = ( alpha - X ) * dt + beta * sqrt(X) dW,
#      X(0) = Xzero,
#
#    with 
#
#      alpha = 2,
#      beta = 1,
#      Xzero = 1.
#
#    From the stochastic Chain Rule, the SDE for V is therefore:
#
#      dV = ( ( 4 * alpha - beta^2 ) / ( 8 * V ) - 1/2 V ) dt + 1/2 beta dW
#      V(0) = np.sqrt ( Xzero ).
#
#    Xem is the Euler-Maruyama solution for X. 
#
#    Vem is the Euler-Maruyama solution of the SDE for V from
#    the stochastic Chain Rule.
#
#    Hence, we compare sqrt(Xem) and Vem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'chain():' )
  print ( '  Solve a stochastic differential equation involving a function' )
  print ( '  of a stochastic variable X.' )
  print ( '  We can solve for X(t), and then evaluate V(X(t)).' )
  print ( '  Or, apply the stochastic chain rule to derive an' )
  print ( '  an SDE for V, and solve that.' )
#
#  Set problem parameters.
#
  alpha = 2.0 
  beta = 1.0
#
#  Stepping parameters.
#  dt2 is the size of the Euler-Maruyama steps.
#
  tmax = 1.0
  n = 200
  dt = tmax / n
  dt2 = dt
  t2 = np.linspace ( 0, tmax, n + 1 )
#
#  Define the increments dW.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
#
#  Solve for X(t).
#
  xzero = 1.0 
  xem = np.zeros ( n )
  xtemp = xzero

  for j in range ( 0, n ):
    f1 = ( alpha - xtemp )
    g1 = beta * np.sqrt ( np.abs ( xtemp ) )
    xtemp = xtemp + dt2 * f1 + dw[j] * g1
    xem[j] = xtemp
#
#  Solve for V(t).
#
  vzero = np.sqrt ( xzero )
  vem = np.zeros ( n )
  vtemp = vzero

  for j in range ( 0, n ):
    f2 = ( 4 * alpha - beta**2 ) / ( 8 * vtemp ) - vtemp / 2
    g2 = beta / 2.0
    vtemp = vtemp + dt2 * f2 + dw[j] * g2
    vem[j] = vtemp
#
#  Compare sqrt(X) and V.
#
  xdiff = np.linalg.norm ( np.sqrt ( xem ) - vem, ord = np.inf )
  print ( '' )
  print ( '  Maximum difference = ', xdiff )
#
#  Plot the results.
#
  plt.clf ( )
  plt.plot ( t2, np.sqrt ( np.hstack ( ( [xzero], np.abs(xem) ) ) ), 'b-' )
  plt.plot ( t2, np.hstack ( ( [vzero], vem ) ), 'ro' )

  plt.legend ( [ 'Direct Solution', 'Solution via Chain Rule' ] )
  plt.xlabel ( 't', fontsize = 12 ) 
  plt.ylabel ( 'V(X)' )
  plt.title ( 'Stochastic Differential Equation Solution by chain()' )
  plt.grid ( True )

  filename = 'chain.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def em ( rng ):

#*****************************************************************************80
#
## em() applies the Euler-Maruyama method to a linear SDE.
#
#  Discussion:
#
#    The SDE is 
#
#      dX = lambda * X dt + mu * X dW,   
#      X(0) = Xzero,
#
#    where 
#
#      lambda = 2,
#      mu = 1,
#      Xzero = 1.
#
#    The discretized Brownian path over [0,1] uses
#    a stepsize dt = 2^(-8).
#
#    The Euler-Maruyama method uses a larger timestep Dt = R*dt,
#    where R is an integer.  For an SDE of the form
#
#      dX = f(X(t)) dt + g(X(t)) dW(t)
#
#    it has the form
#
#      X(j) = X(j-1) + f(X(j-1)) * Dt + g(X(j-1)) * ( W(j*Dt) - W((j-1)*Dt) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
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
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'em():' )
  print ( '  Apply the Euler-Maruyama method to an SDE.' )
#
#  Set problem parameters.
#
  lamb = 2.0
  mu = 1.0
  xzero = 1.0
#
#  Set stepping parameters.
#
  tmax = 1.0
  n = 2**8
  dt = tmax / n
#
#  Compute the Brownian increments.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
#
#  Sum the Brownian increments.
#
  w = np.cumsum ( dw )
#
#  Compute the discretized Brownian path.
#
  t = np.linspace ( dt, tmax, n )
  xtrue = xzero * np.exp ( ( lamb - 0.5 * mu**2 ) * t + mu * w ) 
#
#  Set:
#  R, the multiplier for the EM step, 
#  Dt, the EM stepsize,
#  L, the number of EM steps.
#
  r = 4
  dt2 = r * dt
  n2 = n // r
#
#  Preallocate Xem for efficiency.
#
  xem = np.zeros ( n2 )
  xtemp = xzero
  for j in range ( 0, n2 ):
    winc = np.sum ( dw [ r*j : r*(j+1)-1 ] ) 
    xtemp = xtemp + dt2 * lamb * xtemp + mu * xtemp * winc
    xem[j] = xtemp

  emerr = np.abs ( xem[-1] - xtrue[-1] )
  print ( '' )
  print ( '  Xem(Tfinal) - Xtrue(Tfinal) = ', emerr )
#
#  Plotting.
#
  t = np.linspace ( 0.0, tmax, n + 1 )
  t2 = np.linspace ( 0.0, tmax, n2 + 1 )
  plt.clf ( )
  plt.plot ( t, np.hstack ( ( [xzero], xtrue ) ), 'b-' )
  plt.plot ( t2, np.hstack ( ( [xzero], xem ) ), 'r--*' )
  plt.legend ( [ 'true', 'EM Approximation' ] )
  plt.xlabel ( 't', fontsize = 12 )
  plt.ylabel ( 'X(t)', fontsize = 16, rotation = 0 )
  plt.title ( 'Euler-Maruyama solution of SDE' )
  plt.grid ( True )

  filename = 'em.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def emstrong ( rng ):

#*****************************************************************************80
#
## emstrong() tests the strong convergence of the EM method.
#
#  Discussion:
#
#    The SDE is 
#
#      dX = lambda * X dt + mu * X dW,   
#      X(0) = Xzero,
#
#    where 
#
#      lambda = 2,
#      mu = 1,
#      Xzero = 1.
#
#    The discretized Brownian path over [0,1] has dt = 2^(-9).
#
#    The Euler-Maruyama method uses 5 different timesteps: 
#      16*dt, 8*dt, 4*dt, 2*dt, dt.
#
#    We are interested in examining strong convergence at T=1,
#    that is
#
#      E | X_L - X(T) |.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'emstrong():' )
  print ( '  Test the strong convergence of the Euler-Maruyama method.' )
#
#  Set problem parameters.
#
  lamb = 2.0 
  mu = 1.0 
  xzero = 1.0
#
#  Set stepping parameters.
#
  tmax = 1.0
  n = 2**9 
  dt = tmax / n
#
#  Set the number of paths sampled.
#
  m = 1000
#
#  Preallocate arrays.
#
  xerr = np.zeros ( [ m, 5 ] )
#
#  Sample over discrete Brownian paths.
#
  for s in range ( 0, m ):
#
#  Compute the Brownian increments.
#
    dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
#
#  Sum the increments to get the Brownian path.
#
    w = np.cumsum ( dw )
#
#  Determine the true solution.
#
    xtrue = xzero * np.exp ( ( lamb - 0.5 * mu**2 ) + mu * w[-1] )
#
#  Use the Euler-Maruyama method with 5 different time steps dt2 = r * dt
#
    for p in range ( 0, 5 ):                          
      r = 2**p
      dt2 = r * dt
      l = n // r
      xtemp = xzero
      for j in range ( 0, l ):
        winc = np.sum ( dw[r*j:r*(j+1)] )
        xtemp = xtemp + dt2 * lamb * xtemp + mu * xtemp * winc
      xerr[s,p] = np.abs ( xtemp - xtrue )

  powers = np.array ( [ 0, 1, 2, 3, 4 ] )
  dtvals = dt * 2.0 ** powers
#
#  Least squares fit of error = c * dt^q.
#
  A = np.array ( [ \
    [ 1.0, dtvals[0] ], \
    [ 1.0, dtvals[1] ], \
    [ 1.0, dtvals[2] ], \
    [ 1.0, dtvals[3] ], \
    [ 1.0, dtvals[4] ] ] )

  rhs = np.log ( np.mean ( xerr, axis = 0 ) )
  sol, _, _, _ = np.linalg.lstsq ( A, rhs, rcond = None )
  q = sol[1]
  print ( '' )
  print ( '  Least squares solution to Error = c * dt ^ q' )
  print ( '  Expecting a value near 0.5' )
  print ( '  q = ', q )
  resid = np.linalg.norm ( np.dot ( A, sol ) - rhs )
  print ( '  Residual is ', resid )
#
#  Plot.
#  Include a reference slope of 1/2.
#
  plt.clf ( )
  plt.loglog ( dtvals, np.mean ( xerr, axis = 0 ), 'b*-', linewidth = 2 ) 
  plt.loglog ( dtvals, np.sqrt ( dtvals ), 'r--', linewidth = 2 )
  plt.axis ( [ 1e-3, 1e-1, 1e-4, 1 ] )
  plt.xlabel ( '\Delta t' )
  plt.ylabel ( 'Sample average of | X(T) - X_L |' )
  plt.title ( 'Euler-Maruyama error with various stepsizes', fontsize = 10 )
  plt.grid ( True )

  filename = 'emstrong.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def emweak ( rng, method ):

#*****************************************************************************80
#
## emweak() tests the weak convergence of the Euler-Maruyama method.
#
#  Discussion:
#
#    The SDE is 
#
#      dX = lambda * X dt + mu * X dW,   
#      X(0) = Xzero,
#
#    where 
#
#      lambda = 2,
#      mu = 1,
#      Xzero = 1.
#
#    The discretized Brownian path over [0,1] has dt = 2^(-9).
#
#    The Euler-Maruyama method will use 5 different timesteps:
#
#      2^(p-10),  p = 1,2,3,4,5.
#
#    We examine weak convergence at T=1:
#
#      | E (X_L) - E (X(T)) |.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
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
#    rng(): the current random number generator.
#
#    integer METHOD.
#    0, use the standard Euler-Maruyama method
#    1, use the weak Euler-Maruyama method.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'emweak():' )
  print ( '  Test the weak convergence of the Euler-Maruyama method.' ) 
#
#  Problem parameters
#
  lamb = 2.0
  mu = 0.1
  xzero = 1.0
#
#  Stepping parameters.
#
  tmax = 1.0
  lvals = np.array ( [ 2**9, 2**8, 2**7, 2**6, 2**5 ] )
  dtvals = 1.0 / lvals
#
#  The number of paths to sample.
#
  m = 50000
#
#  Take various Euler timesteps.
#  For stepsize dt, we will need to take L Euler steps to reach time TMAX.
#
  xem = np.zeros ( 5 )

  for p in range ( 0, 5 ):

    dt = dtvals[p]
    l = lvals[p]
    xtemp = xzero * np.ones ( m )            

    for j in range ( 0, l ):

      if ( method == 0 ):
        winc = np.sqrt ( dt ) * rng.standard_normal ( size = m )
      else:
        winc = np.sqrt ( dt ) * np.sign ( rng.standard_normal ( size = m ) )

      xtemp = xtemp + dt * lamb * xtemp + mu * xtemp * winc
#
#  Average the M results for this stepsize.
#
    xem[p] = np.mean ( xtemp )
#
#  Compute the error in the estimates for each stepsize.
#
  xerr = np.abs ( xem - np.exp ( lamb ) )
#
#  Least squares fit of error = C * dt^q
#
  A = np.array ( [ \
    [ 1.0, np.log ( 1.0/2.0**9 ) ], \
    [ 1.0, np.log ( 1.0/2.0**8 ) ], \
    [ 1.0, np.log ( 1.0/2.0**7 ) ], \
    [ 1.0, np.log ( 1.0/2.0**6 ) ], \
    [ 1.0, np.log ( 1.0/2.0**5 ) ] ] )
  rhs = np.log ( xerr )
#
#  The least squares interface is pointlessly cluttered.
#
  sol, _, _, _ = np.linalg.lstsq ( A, rhs, rcond = None )
  q = sol[1]

  print ( '' )
  if ( method == 0 ):
    print ( '  Using standard Euler-Maruyama method.' )
  else:
    print ( '  Using weak Euler-Maruyama method.' )
  print ( '  Least squares solution to Error = c * dt ^ q' )
  print ( '  Expecting a q value near 1' )
  print ( '  q = ', q )
  resid = np.linalg.norm ( np.dot ( A, sol ) - rhs )
  print ( '  Residual is ', resid )
#
#  Plotting.
#  Include a reference slope of 1.
#    
  plt.clf ( )
  plt.loglog ( dtvals, xerr, 'b*-', linewidth = 2 )
  plt.loglog ( dtvals, dtvals, 'r--', linewidth = 2 )
  plt.axis ( [ 1e-3, 1e-1, 1e-4, 1.0 ] )
  plt.xlabel ( '\Delta t' )
  plt.ylabel ( '| E(X(T)) - Sample average of X_L |' )
  if ( method == 0 ):
    plt.title ( 'Weak convergence of Euler-Maruyama method', fontsize = 10 )
  else:
    plt.title ( 'Weak convergence of weak Euler-Maruyama method', fontsize = 10 ) 

  plt.grid ( True )

  if ( method == 0 ):
    filename = 'emweak0.png'
  else:
    filename = 'emweak1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def milstrong ( rng ):

#*****************************************************************************80
#
## milstrong() tests the strong convergence of the Milstein method.
#
#  Discussion:
#
#    Solve the stochastic differential equation
#
#      dX = sigma * X * ( k - X ) dt + beta * X dW,  
#      X(0) = Xzero,
#
#    where 
#
#       sigma = 2, 
#       k = 1, 
#       beta = 1,
#       Xzero = 0.5.
#
#    The discretized Brownian path over [0,1] has dt = 2^(-11).
#
#    The Milstein method uses timesteps 128*dt, 64*dt, 32*dt, 16*dt 
#    (also dt for reference).
#
#    We examine strong convergence at T=1:  
#
#      E | X_L - X(T) |.
#
#    The code is vectorized: all paths computed simultaneously.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'milstrong():' )
  print ( '  Test the strong convergence of the Milstein method.' )
#
#  Set problem parameters
#
  sigma = 2.0
  k = 1.0
  beta = 0.25
  xzero = 0.5
#
#  Set stepping parameters
#
  tmax = 1.0
  n = 2**(11)
  dt = tmax / n
#
#  Number of paths sampled.
#
  m = 500
#
#  R is used to derive the Milstein step size R*dt.
#
  r = np.array ( [ 1, 16, 32, 64, 128 ] )
#
#  Set the Brownian increments.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = [ m, n ] )
#
#  For each stepsize, compute the Milstein estimate at T = 1.
#
  xmil = np.zeros ( [ m, 5 ] )

  for p in range ( 0, 5 ):                               

    dtp = r[p] * dt
    l = n // r[p]
    xtemp = xzero * np.ones ( m )

    for j in range ( 0, l ):
      winc = np.sum ( dw[:,r[p]*j:r[p]*(j+1)], axis = 1 )
      xtemp = xtemp + dtp * sigma * xtemp * ( k - xtemp ) \
        + beta * xtemp * winc \
        + 0.5 * beta**2 * xtemp * ( winc**2 - dtp )

    xmil[:,p] = xtemp.copy()
#
#  XREF is the reference solution with the full time step.
#
  xref = xmil[:,0]
#
#  XERR is the difference between the reference solution and each path
#  with larger step.
#
  xerr = np.zeros ( [ m, 4 ] )
  for p in range ( 1, 5 ):
    xerr[:,p-1] = np.abs ( xmil[:,p] - xmil[:,0] )
#
#  Least squares fit of error = C * dt^q
#
  dtvals = dt * r[1:]

  A = np.array ( [ 
    [ 1.0, np.log ( dt * r[1] ) ], \
    [ 1.0, np.log ( dt * r[2] ) ], \
    [ 1.0, np.log ( dt * r[3] ) ], \
    [ 1.0, np.log ( dt * r[4] ) ] ] )
  rhs = np.log ( np.mean ( xerr, axis = 0 ) )
  sol, _, _, _ = np.linalg.lstsq ( A, rhs, rcond = None )
  q = sol[1]
  print ( '' )
  print ( '  Least squares solution to Error = c * dt ^ q' )
  print ( '  Expecting a value near 0.5' )
  print ( '  q = ', q )
  resid = np.linalg.norm ( np.dot ( A, sol ) - rhs )
  print ( '  Residual is ', resid )
#
#  Plotting.
#  Include a reference slope of 1.
#
  plt.clf ( )
  plt.loglog ( dtvals, np.mean ( xerr, axis = 0 ), 'b*-' )
  plt.loglog ( dtvals, dtvals, 'r--' )
  plt.axis ( [ 1e-3, 1e-1, 1e-4, 1 ] )
  plt.xlabel ( '\Delta t' )
  plt.ylabel ( 'Sample average of | X(T) - X_L |' )
  plt.title ( 'Strong convergence of Milstein', fontsize = 10 )
  plt.grid ( True )

  filename = 'milstrong.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def stab ( rng ):

#*****************************************************************************80
#
## stab() examines mean-square and asymptotic stability.
#
#  Discussion:
#
#    Test the mean-square and asymptotic stability
#    of the Euler-Maruyama method applied to a stochastic differential
#    equation (SDE).
#
#    The SDE is
#
#      dX = lambda*X dt + mu*X dW,
#      X(0) = Xzero,
#
#    where 
#
#      lambda is a constant,
#      mu is a constant,
#      Xzero = 1.
#
#    We will examine different values of lambda and mu.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stab():' )
  print ( '  Check asymptotic and mean-square stability.' )
#
#  Set problem parameters.
#
  tmax = 20.0
  m = 50000
  xzero = 1          
#
#  Set line types for the plot.
#
  ltype = { 'b-', 'r--', 'm-.' }
#
#  Mean square.
#
  lamb = -3.0
  mu = np.sqrt ( 3.0 )
#
#  XMS is the mean square estimate of M paths.
#
  plt.clf ( )

  for k in range ( 0, 3 ):

    if ( k == 0 ):
      ltype = 'b-'
      dt = 2.0
      n = 10
    elif ( k == 1 ):
      ltype = 'r--'
      dt = 1.0
      n = 20
    else:
      ltype = 'm-.'
      dt = 0.50
      n = 40                 

    xms = np.zeros ( n )
    xtemp = xzero * np.ones ( m )

    for j in range ( 0, n ):
      winc = np.sqrt ( dt ) * rng.standard_normal ( size = m )
      xtemp = xtemp + dt * lamb * xtemp + mu * xtemp * winc
      xms[j] = np.mean ( xtemp**2 )

    t = np.linspace ( 0.0, tmax, n + 1 )

    plt.semilogy ( t, np.hstack ( [ [ xzero ], xms ] ), ltype, linewidth = 2 ) 

  plt.legend ( [ '\Delta t = 1','\Delta t = 1/2','\Delta t = 1/4' ] )
  plt.title ( 'Mean-Square: \lambda = -3, \mu = \surd 3', fontsize = 16 )
  plt.ylabel ( 'E[X^2]',fontsize = 12 )
  plt.axis ( [ 0.0, tmax, 1e-20, 1e+20 ] )
  filename = 'stab1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Asymptotic, a single path.
#
  tmax = 500.0
#
#  Problem parameters.
#
  lamb = 0.5
  mu = np.sqrt ( 6.0 )

  plt.clf ( )

  for k in range ( 0, 3 ):

    if ( k == 0 ):
      ltype = 'b-'
      dt = 2.0
      n = 250
    elif ( k == 1 ):
      ltype = 'r--'
      dt = 1.0
      n = 500
    else:
      ltype = 'm-.'
      dt = 0.50
      n = 1000  

    xemabs = np.zeros ( n )
    xtemp = xzero

    for j in range ( 0, n ):
      winc = np.sqrt ( dt ) * rng.standard_normal ( ) 
      xtemp = xtemp + dt * lamb * xtemp + mu * xtemp * winc
      xemabs[j] = np.abs ( xtemp )

    t = np.linspace ( 0.0, tmax, n + 1 )

    plt.semilogy ( t, np.hstack ( [ [ xzero ], xemabs ] ), ltype, linewidth = 2 )

  plt.legend ( [ '\Delta t = 1','\Delta t = 1/2','\Delta t = 1/4' ] )
  plt.title ( 'Single Path: \lambda = 1/2, \mu = \surd 6', fontsize = 16 )
  plt.ylabel ( '|X|',fontsize = 12 )
  plt.axis ( [ 0.0, tmax, 1e-50, 1e+100 ] )

  filename = 'stab2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def stab_asymptotic ( rng ):

#*****************************************************************************80
#
## stab_asymptotic() examines asymptotic stability.
#
#  Discussion:
#
#    Test the asymptotic stability
#    of the Euler-Maruyama method applied to a stochastic differential
#    equation (SDE).
#
#    The SDE is
#
#      dX = lambda*X dt + mu*X dW,
#      X(0) = Xzero,
#
#    where 
#
#      lambda is a constant,
#      mu is a constant,
#      Xzero = 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stab_asymptotic():' )
  print ( '  Investigate asymptotic stability of Euler-Maruyama' )
  print ( '  solution with stepsize DT and MU.' )
  print ( '' )
  print ( '  SDE is asymptotically stable if' )
  print ( '    Real ( lambda - 1/2 mu^2 ) < 0.' )
  print ( '' )
  print ( '  EM with DT is asymptotically stable if' )
  print ( '    E log ( 1 + lambda dt - sqrt(dt) mu n(0,1) ) < 0.' )
  print ( '  where n(0,1) is a normal random value.' )
#
#  Step parameters.
#
  tmax = 500.0
#
#  Problem parameters.
#
  lamb = 0.5
  mu = np.sqrt ( 6.0 )
  xzero = 1.0
#
#  Test the SDE.
#
  print ( '' )
  print ( '  Lambda = ', lamb )
  print ( '  Mu =     ', mu )
  test = lamb - 0.5 * mu * mu
  print ( '  SDE asymptotic test = ', test )

  plt.clf ( )

  for i in range ( 0, 3 ):

    if ( i == 0 ):
      n = 500
      ltype = 'b-'
    elif ( i == 1 ):
      n = 1000
      ltype = 'r--'
    else:
      n = 2000
      ltype = 'm-.'
 
    dt = tmax / n
#
#  Test the EM for this DT.
# 
    xemabs = np.zeros ( n )
    xtemp = xzero

    for j in range ( 0, n ):
      winc = np.sqrt ( dt ) * rng.standard_normal ( ) 
      xtemp = xtemp + dt * lamb * xtemp + mu * xtemp * winc
      xemabs[j] = np.abs ( xtemp )

    t = np.linspace ( 0.0, tmax, n + 1 )
    plt.semilogy ( t, np.hstack ( ([xzero],xemabs)), ltype, linewidth = 2 )

  plt.legend ( [ '\Delta t = 1','\Delta t = 1/2','\Delta t = 1/4' ] )
  plt.title ( 'Single Path: \lambda = 1/2, \mu = \surd 6', fontsize = 16 )
  plt.ylabel ( '|X|', fontsize = 12 )
  plt.xlabel ( '<---T--->' )
  plt.axis ( [ 0, tmax, 1e-50, 1e+100 ] )
  plt.grid ( True )

  filename = 'stab_asymptotic.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def stab_meansquare ( rng ):

#*****************************************************************************80
#
## stab_meansquare() examines mean-square stability.
#
#  Discussion:
#
#    Test the mean-square stability
#    of the Euler-Maruyama method applied to a stochastic differential
#    equation (SDE).
#
#    The SDE is
#
#      dX = lambda*X dt + mu*X dW,
#      X(0) = Xzero,
#
#    where 
#
#      lambda is a constant,
#      mu is a constant,
#      Xzero = 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'stabmeansquare():' )
  print ( '  Check mean-square stability.' )
#
#  Set problem parameters.
#
  tmax = 20.0
  m = 50000
  xzero = 1          
#
#  Problem parameters.
#
  lamb = -3.0
  mu = np.sqrt ( 3.0 )
#
#  XMS is the mean square estimate of M paths.
#
  plt.clf ( )

  for k in range ( 0, 3 ):

    if ( k == 0 ):
      ltype = 'b-'
      dt = 1.0
      n = 20
    elif ( k == 1 ):
      ltype = 'r--'
      dt = 0.5
      n = 40
    else:
      ltype = 'm-.'
      dt = 0.25
      n = 80

    xms = np.zeros ( n )
    xtemp = xzero * np.ones ( m )

    for j in range ( 0, n ):
      winc = np.sqrt ( dt ) * rng.standard_normal ( size = m )
      xtemp = xtemp + dt * lamb * xtemp + mu * xtemp * winc
      xms[j] = np.mean ( xtemp**2 )

    t = np.linspace ( 0.0, tmax, n + 1 )
    plt.semilogy ( t, np.hstack ( [[xzero],xms] ), ltype, linewidth = 2 ) 

  plt.legend ( [ '\Delta t = 1', '\Delta t = 1/2', '\Delta t = 1/4' ] )
  plt.title ( 'Mean-Square: \lambda = -3, \mu = \surd 3', fontsize = 16 )
  plt.ylabel ( 'E[X^2]', fontsize = 12 )
  plt.xlabel ( '<---T--->' )
  plt.axis ( [ 0, tmax, 1e-20, 1e+20 ] )
  plt.grid ( True )

  filename = 'stab_meansquare.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def stint ( rng ):

#*****************************************************************************80
#
## stint() approximates a stochastic integral.
#
#  Discussion:
#
#    Estimate both the Ito and Stratonovich 
#    integrals of W(t) dW over the interval [0,1].
#
#    Both estimates are made by taking N steps.  Increasing
#    N will improve the approximation of the integrals by
#    the sums.  However, the Ito and Stratonovich integrals
#    are not equal, and therefore the sums that approximate
#    them will also not tend to the same value. 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'strint():' )
  print ( '  Approximate a stochastic integral.' )

  T = 1
  n = 100000
  dt = T / n
#
#  Set the increments and the cumulative sums.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
  w = np.cumsum ( dw )
#
#  Form the sums that approximates the Ito and Stratonovich integrals.
#
  ito_exact = 0.5 * ( w[-1]**2 - T )
  ito_estimate = np.sum ( np.hstack ( ( [ 0 ], w[0:-1] ) ) * dw )
  ito_error = np.abs ( ito_estimate - ito_exact )

  strat_exact = 0.5 * w[-1]**2
  strat_estimate = np.sum ( ( 0.5 * ( np.hstack ( ( [ 0 ], w[0:-1] ) ) + w ) \
    + 0.5 * np.sqrt ( dt ) * rng.standard_normal ( size = n ) ) * dw )
  strat_error = np.abs ( strat_estimate - strat_exact )
   
  print ( '                                                  Abs      Rel' )
  print ( '              N        Exact        Estimate      Error    Error' )
  print ( '' )
  print ( '    Ito  %8d  %12.8g  %12.8g  %8.2g  %8.2g' % \
      ( n, ito_exact, ito_estimate, ito_error, ito_error / ito_exact ) )
  print ( '  Strat  %8d  %12.8g  %12.8g  %8.2g  %8.2g' % \
      ( n, strat_exact, strat_estimate, strat_error, strat_error / strat_exact ) )

  return

def stochastic_integral_ito_test ( rng ):

#*****************************************************************************80
#
## stochastic_integral_ito_test() tests stochastic_integral_ito().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
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
  print ( 'stochastic_integral_ito_test():' )
  print ( '  Estimate the Ito integral of W(t) dW over [0,1].' )
  print ( '' )
  print ( '                                             Abs      Rel' )
  print ( '         N        Exact        Estimate      Error    Error' )
  print ( '' )

  n = 100

  for i in range ( 0, 7 ):

    estimate, exact, error = stochastic_integral_ito ( rng, n )

    print ( '  %8d  %12.8g  %12.8g  %8.2g  %8.2g' % \
      ( n, exact, estimate, error, error / exact ) )

    n = n * 4

  return

def stochastic_integral_ito ( rng, n ):

#*****************************************************************************80
#
## stochastic_integral_ito() approximates the Ito integral of W(t) dW.
#
#  Discussion:
#
#    This function estimates the Ito integral of W(t) dW over 
#    the interval [0,1].
#
#    The estimates is made by taking N steps.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
#    integer N, the number of steps to take.
#
#  Output:
#
#    real ESTIMATE, the estimate of the integral.
#
#    real EXACT, the exact value of the integral.
#
#    real ERROR, the error in the integral estimate.
#
  import numpy as np
#
#  Set step parameters.
#
  tmax = 1.0
  dt = tmax / n
#
#  Set the increments.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
#
#  Set the cumulative sums.
#
  w = np.cumsum ( dw )
#
#  Approximate the Ito integral.
#
  estimate = np.sum ( np.hstack ( ( [ 0 ], w[0:-1] ) ) * dw )
#
#  Compare with the exact solution.
#
  exact = 0.5 * ( w[-1]**2 - tmax )
  error = np.abs ( estimate - exact )

  return estimate, exact, error

def stochastic_integral_strat_test ( rng ):

#*****************************************************************************80
#
## stochastic_integral_strat_test() tests stochastic_integral_strat().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
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
  print ( 'stochastic_integral_strat_test():' )
  print ( '  stochastic_integral_strat() estimates the Stratonovich' )
  print ( '  integral of W(t) dW over [0,1].' )
  print ( '' )
  print ( '                                             Abs      Rel' )
  print ( '         N        Exact        Estimate      Error    Error' )
  print ( '' )

  n = 100

  for i in range ( 0, 7 ):

    estimate, exact, error = stochastic_integral_strat ( rng, n )

    print ( '  %8d  %12.8g  %12.8g  %8.2g  %8.2g' % \
      ( n, exact, estimate, error, error / exact ) )

    n = n * 4

  return

def stochastic_integral_strat ( rng, n ):

#*****************************************************************************80
#
## stochastic_integral_strat() approximates the Stratonovich integral of W(t) dW.
#
#  Discussion:
#
#    Estimate the Stratonovich integral of W(t) dW over 
#    the interval [0,1].
#
#    The estimates is made by taking N steps.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2025
#
#  Author:
#
#    Original MATLAB version by Desmond Higham.
#    This version by John Burkardt.
#
#  Reference:
#
#    Desmond Higham,
#    An Algorithmic Introduction to Numerical Simulation of
#    Stochastic Differential Equations,
#    SIAM Review,
#    Volume 43, Number 3, September 2001, pages 525-546.
#
#  Input:
#
#    rng(): the current random number generator.
#
#    integer N, the number of steps to take.
#
#  Output:
#
#    real ESTIMATE, the estimate of the integral.
#
#    real EXACT, the exact value of the integral.
#
#    real ERROR, the error in the integral estimate.
#
  import numpy as np

  tmax = 1.0
  dt = tmax / n
#
#  Set the increments.
#
  dw = np.sqrt ( dt ) * rng.standard_normal ( size = n )
#
#  Set the cumulative sums.
#
  w = np.cumsum ( dw )
#
#  Approximate the Stratonovich integral.
#
  estimate = np.sum ( ( 0.5 * ( np.hstack ( ( [ 0 ], w[0:-1] ) ) + w ) \
    + 0.5 * np.sqrt ( dt ) * rng.standard_normal ( size = n ) ) * dw )
#
#  Compare with the exact solution.
#
  exact = 0.5 * w[-1]**2
  error = np.abs ( estimate - exact )

  return estimate, exact, error

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
  sde_test ( )
  timestamp ( )

