#! /usr/bin/env python3
#
def midpoint_adaptive_test ( ):

#*****************************************************************************80
#
## midpoint_adaptive_test() tests midpoint_adaptive().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'midpoint_adaptive_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test midpoint_adaptive().' )

  lotka_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'midpoint_adaptive_test():' )
  print ( '  Normal end of execution.' )

  return

def lotka_deriv ( t, y ):

#*****************************************************************************80
#
## lotka_deriv() evaluates the right hand side of a Lotka-Volterra ODE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T: the time
#
#    real Y(1,2): the current solution values.
#
#  Output:
#
#    real DYDT(2,1): the derivative values.
#
  import numpy as np

  u = y[0]
  v = y[1]

  dudt =    2.0 * u - 0.001 * u * v
  dvdt = - 10.0 * v + 0.002 * u * v

  dydt = np.array ( [ dudt, dvdt ] )

  return dydt

def lotka_test ( ):

#*****************************************************************************80
#
## lotka_test(): midpoint_adaptive() solves lotka_ode().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    George Lindfield, John Penny,
#    Numerical Methods Using MATLAB,
#    Second Edition,
#    Prentice Hall, 1999,
#    ISBN: 0-13-012641-1,
#    LC: QA297.P45.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'lotka_test():' )
  print ( '  midpoint_adaptive() solves lotka_ode().' )
  print ( '  A pair of ordinary differential equations for a population' )
  print ( '  of predators and prey are solved using midpoint().' )
  print ( '' )
  print ( '  The exact solution shows periodic behavior, with a fixed' )
  print ( '  period and amplitude.' )
  print ( '' )
  print ( '  Steady state at r = 5000, f = 2000.' )

  label = 'lotka'

  f = lotka_deriv
  t0 = 0.0
  tmax = 20.0
  m = 2
  y0 = np.array ( [ 5000.0, 100.0 ] )
  tau0 = 2.5e-2
  reltol = 1.0e-3
  abstol = 1.0e-3

  t, y, nstep, n_rejected = mad_compute ( f, t0, tmax, y0, tau0, reltol, abstol )

  mad_phase_plot ( m, t, y, label )

  mad_solution_plot ( m, t, y, label )

  mad_timestep_plot ( t, label )

  mad_stats ( nstep, n_rejected, t )

  return

def mad_compute ( f, t0, tmax, y0, tau0, reltol, abstol ):

#*****************************************************************************80
#
## mad_compute() estimates the solution of an ordinary differential equation.
#
#  Discussion:
#
#    mad_compute() uses an adaptive time stepping algorithm for the
#    implicit midpoint method, applied to a system of ordinary differential
#    equations.
#
#    The implicit midpoint method has local truncation error O(h^3).
# 
#    The time step is adaptively controlled with respect to relative and
#    absolute tolerances applied to the estimated local truncation error (LTE).
#    
#    The adaptivity with respect to relative and absolute error tolerances
#    is described on page 168 in the Hairer reference.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2024
#
#  Author:
#
#    John Burkardt, Catalin Trenchea
#
#  Reference:
#
#    Catalin Trenchea, John Burkardt,
#    Refactorization of the midpoint rule,
#    Applied Mathematics Letters,
#    Volume 107, September 2020.
#
#    Ernst Hairer, Syvert Norsett, Gerhard Wanner,
#    Solving ordinary differential equations, I. Nonstiff problems, 
#    Springer Series in Computational Mathematics, Number 8. 
#    Springer-Verlag, Berlin, 1987.
#
#  Input:
#
#    function handle f: the function that evaluates the right hand side 
#    of the differential equation, of the form 
#      dydt = f ( t, y )
#
#    real t0, tmax: the interval of integration.
#
#    real y0(m): the (row) vector of initial conditions at the starting time. 
#
#    real tau0: the initial timestep to take.
#
#    real reltol, abstol: the tolerances for the local truncation error.
#
#  Output:
#
#    real t(nsteps+1), y(nsteps+1,m): the sequence of times and solution estimates.
#
#    integer nsteps: the number of steps.
#
#    integer n_rejected: the number of rejected steps.
#
#  Local:
#
#    integer count: the number of stepsizes, whether accepted or rejected.
#    It should be the case that it <= count.
#
#    real kappa: a factor for the stepsize update.
#    0 < kappa <= 1.  The value kappa = 0.85 is suggested.
#
#    real theta: the theta-method parameter.
#    theta = 0.0 for the backward Euler method.
#    theta = 0.5 for the midpoint method.
#    theta = 1.0 for the forward Euler method.
#
  import numpy as np

  kappa = 0.85
  theta = 0.5

  m = len ( y0 )

  count = -1

  t = np.zeros ( 0 )
  y = np.zeros ( [ 1, m ] )
  nstep = -2
  n_rejected = 0

  tau = np.zeros ( 0 )

  while ( True ):

    nstep = nstep + 1
#
#  nstep = -1: y0.
#
    if ( nstep == -1 ):
      t = np.append ( t, t0 )
      y[0,:] = y0[:]
      tau = np.append ( tau, tau0 )
      count = count + 1

    elif ( tmax <= t[-1] ):
 
      break
#
#  nstep = 0, 1: y1, y2
#
    elif ( nstep <= 1 ):
      t, y = mad_step ( nstep, t, y, tau, f, theta )
      tau = np.append ( tau, tau0 )
      count = count + 1

    else:
#
#  Several step reductions may be necessary before the LTE test is met.
#
      while ( True ):

        count = count + 1

        t, y = mad_step ( nstep, t, y, tau, f, theta )
#
#  Estimate local truncation error.
# 
        tnmin, tnmax = mad_lte ( nstep, y, tau, reltol, abstol )
#
#  If the LTE test was met, we accept T and Y, set the next time step,
#  and can advance to the next time.
#
        if ( tnmin <= 1.0 ):
          factor = kappa * ( 1.0 / tnmax ) ** ( 1.0 / 3.0 )
          factor = min ( factor, 1.5 )
          factor = max ( factor, 0.02 )
          tau = np.append ( tau, factor * tau[nstep] )
          break

        n_rejected = n_rejected + 1

  print ( '' )
  print ( '  mad_compute(): count = ', count )

  return t, y, nstep, n_rejected

def mad_lte ( it, y, tau, reltol, abstol ):

#*****************************************************************************80
#
## mad_lte() estimates the local truncation error.
#
#  Discussion:
#
#    This function is called by mad_compute() to estimate the local truncation
#    error incurred during a single step of the implicit midpoint method.
#
#    We assume the step has been taken over an interval which we will 
#    represent as going from (t1,y1) to (t2,y2).  We may regard y2 as the
#    estimated solution of the local ODE:
#      dy/dt = f(t,y), y(t1) = y1.
#    We suppose that a function y*() is the EXACT solution of this system
#    and we define the local truncation error for this step as
#      lte = y*(t2) - y2
#    We wish to accept this step as long as lte is small, that is:
#      lte = y*(t2) - y2 < abstol + reltol * max ( y1, y2 )
#
#    To carry out this check, we need to estimate lte or y*(t2).
#    This is done using the Milne Device, described in the Milne reference.
#    Essentially, lte is estimated using a weighted difference of solution
#    estimates y2 and an estimate formed by an Adams-Bashforth AB2-like 
#    method.  See page 5 of the Burkardt reference for details.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2022
#
#  Author:
#
#    John Burkardt, Catalin Trenchea
#
#  Reference:
#
#    John Burkardt, Catalin Trenchea,
#    Refactorization of the midpoint rule,
#    Appl. Math. Lett. 107 (2020), 106438.
#
#    William Milne,
#    Numerical Integration of Ordinary Differential Equations,
#    American Mathematical Monthly,
#    Volume 33, number 9, pages 455–460, 1926.
#
#  Input:
#
#    integer it: the index of the most recently accepted step.
#
#    real y(it+1,m): the solution vector.
#
#    real tau[it]: the stepsize vector.
#
#    real reltol, abstol: the tolerances for the local truncation error.
#
#  Output:
#
#    real tnmin, tnmax: the minimum and maximum entries of an lte
#    error estimator.
#
  import numpy as np
#
#  Evaluate the AB2-like solution.
#
  c1 = ( tau[it] + tau[it-1] ) * ( tau[it] + tau[it-1] + tau[it-2] ) \
    / ( tau[it-1] * ( tau[it-1] + tau[it-2] ) )

  c2 = - tau[it] * ( tau[it] + tau[it-1] + tau[it-2] ) \
    / ( tau[it-1] * tau[it-2] )

  c3 = tau[it] * ( tau[it] + tau[it-1] ) \
     / ( tau[it-2] * ( tau[it-1] + tau[it-2] ) )

  uab2 = c1 * y[it,:] + c2 * y[it-1,:] + c3 * y[it-2,:]
#
#  Evaluate R, the variable error coefficient in the LTE.
#
  r = 1.0 / 24.0 + 1.0 / 8.0 * ( 1.0 + tau[it-1] / tau[it] ) \
    * ( 1.0 + 2.0 * tau[it-1] / tau[it] + tau[it-2] / tau[it] )
#
#  Use AB2 estimator to approximate the LTE vector.
#
  tn = ( y[it+1,:] - uab2 ) * 24.0 * r / ( 24.0 * r - 1.0 ) \
    / ( abstol + np.abs ( y[it+1,:] ) * reltol )
   
  tnmax = np.max ( np.abs ( tn ) )
  tnmin = np.min ( np.abs ( tn ) )

  return tnmin, tnmax

def mad_phase_plot ( m, t, y, label ):

#*****************************************************************************80
#
## mad_phase_plot() creates a phase plot.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 July 2024
#
#  Author:
#
#    John Burkardt, Catalin Trenchea
#
#  Input:
#
#    integer m: the spatial dimension.
#
#    real t[n+1]: the sequence of time values.
#
#    real y[n+1,m]: the sequence of solution values.
#
#    string label: an identifier for the problem.
#    The plotfile will be 'label_phase.png'.
#
  import matplotlib.pyplot as plt
  import numpy as np

  plt.plot ( y[:,0], y[:,1], 'r-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'midpoint_adaptive(): ' + label + ' phase' )
  filename = label + '_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def mad_solution_plot ( m, t, y, label ):

#*****************************************************************************80
#
## mad_solution_plot() creates a solution plot.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 July 2024
#
#  Author:
#
#    John Burkardt, Catalin Trenchea
#
#  Input:
#
#    integer m: the spatial dimension.
#
#    real t[n+1]: the sequence of time values.
#
#    real y[n+1,m]: the sequence of solution values.
#
#    string label: an identifier for the problem.
#    The plotfile will be 'label_solution.png'.
#
  import matplotlib.pyplot as plt
  import numpy as np

  plt.plot ( t, y[:,0], 'r-', linewidth = 2 )
  plt.plot ( t, y[:,1], 'g-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Prey --->' )
  plt.ylabel ( '<--- Predators --->' )
  plt.title ( 'midpoint_adaptive(): ' + label + ' solution' )
  plt.legend ( [ 'prey', 'predator' ] )
  filename = label + '_solution.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def mad_stats ( nstep, n_rejected, t ):

#*****************************************************************************80
#
## mad_stats() reports statistics for mad_compute().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 July 2024
#
#  Author:
#
#    John Burkardt, Catalin Trenchea
#
#  Input:
#
#    integer nstep: the number of time steps.
#
#    integer n_rejected: the number of rejected time steps.
#
#    real t(nstep+1): the sequence of time values.
#
  import numpy as np

  tau = np.diff ( t )
  r = tau[1:] / tau[0:-1]

  print ( '' )
  print ( 'mad_stats():' )
  print ( '' )
  print ( '  Number of timesteps ', nstep )
  print ( '  Rejected timesteps  ', n_rejected )
  print ( '  First time interval is [', t[0], ',', t[1], ']' )
  print ( '  Final time interval is [', t[-2], ',', t[-1], ']' )
  print ( '  Minimum timestep is ', np.min ( tau ) )
  print ( '  Maximum timestep is ', np.max ( tau ) )

  return

def mad_step ( it, t, y, tau, f, theta ):

#*****************************************************************************80
#
## mad_step() extends the (t,y) solution sequence by one more step.
#
#  Discussion:
#
#    Given a sequence of solution values (t,y) for an ODE, this function
#    starts at time t[it], with solution y[it,:] and stepsize tau[it].
#
#    It uses the implicit midpoint method to estimate a solution ym[:] at
#    time tm = t[it] + theta * tau[it], from which it constructs
#    the values t[it+1] and y[it+1,:].
#
#    In other words, it adds one more (t,y) pair to the solution sequence.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2022
#
#  Author:
#
#    John Burkardt, Catalin Trenchea
#
#  Reference:
#
#    John Burkardt, Catalin Trenchea,
#    Refactorization of the midpoint rule,
#    Appl. Math. Lett. 107 (2020), 106438.
#
#  Input:
#
#    integer it: the current number of time steps.
#
#    real t[it], y(it,m): the sequence of times and solution estimates.
#
#    real tau[it]: the sequence of time steps.  The final entry is tentative.
#
#    function f: the function that evaluates the right hand side 
#    of the differential equation, of the form 
#      dydt = f ( t, y )
#
#    real theta: the theta-method parameter.
#    theta = 0.0 for the backward Euler method.
#    theta = 0.5 for the midpoint method.
#    theta = 1.0 for the forward Euler method.
#
#  Output:
#
#    real t[it+1], y[it+1,m]: the sequence of times and solution estimates,
#    augmented by one new time step.
#
  from scipy.optimize import fsolve
  import numpy as np

  tm = t[it] + theta * tau[it]
  ym = y[it,:] + theta * tau[it] * f ( tm, y[it,:] )
  ym = fsolve ( midpoint_residual, ym, args = ( f, t[it], y[it,:], tm ) )

  tn = t[it] + tau[it]
  yn = (       1.0 / theta ) * ym \
     + ( 1.0 - 1.0 / theta ) * y[it,:]

  t = np.append ( t, tn )
  y = np.vstack ( ( y, yn ) )

  return t, y

def mad_timestep_plot ( t, label ):

#*****************************************************************************80
#
## mad_timestep_plot() creates a timestep plot.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 July 2024
#
#  Author:
#
#    John Burkardt, Catalin Trenchea
#
#  Input:
#
#    real t(n+1): the sequence of time values.
#
#    string label: an identifier for the problem.
#    The plotfile will be 'label_timestep.png'.
#
  import matplotlib.pyplot as plt
  import numpy as np

  tau = np.diff ( t )

  plt.clf ( )
  plt.plot ( t[0:-1], tau, '.-' )
  plt.grid ( True )
  plt.title ( 'midpoint_adaptive(): ' + label + ' timestep' )
  plt.xlabel ( '<-- t(i) -->' )
  plt.ylabel ( '<-- dt(i) -->' )
  filename = label +'_timestep.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def midpoint_residual ( yh, f, to, yo, th ):

#*****************************************************************************80
#
## midpoint_residual() evaluates the midpoint residual.
#
#  Discussion:
#
#    We are seeking a value YH defined by the implicit equation:
#
#      YH = YO + ( TH - TO ) * F ( TH, YH )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real yh: the estimated solution value at the midpoint time.
#
#    function f: evaluates the right hand side of the ODE.  
#
#    real to, yo: the old time and solution value.
#
#    real th: the midpoint time.
#
#  Output:
#
#    real value: the midpoint residual.
#
  value = yh - yo - ( th - to ) * f ( th, yh )

  return value

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
  midpoint_adaptive_test ( )
  timestamp ( )

