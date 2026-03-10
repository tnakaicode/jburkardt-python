#! /usr/bin/env python3
#
def bowie_test ( ):

#*****************************************************************************80
#
## bowie_test() tests bowie().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'bowie_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test bowie(), a NASA ODE solver for certain second order' )
  print ( '  autonomous systems.' )

  test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'bowie_test():' )
  print ( '  Normal end of execution.' )
  return

def test01 ( ):

#*****************************************************************************80
#
## test01() solves y'' = - sin ( t ), y(0) = 0, y'(0) = 1.
#
#  Discussion:
#
#    The exact solution is the nonlinear pendulum function.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 January 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  y0 = np.array ( [ 0.0, 1.0 ] )

  tstart = 0.0
  tstop = 12.0
  tspan = np.array ( [ tstart, tstop ] )

  n = 100
#
#  Second order ODE has the form y'' = -sin(t), y(0) = 0, y'(0) = 1.
#
#  First order system has the form
#    z1' = z2
#    z2' = -sin(t)
#
  f   = lambda t: -np.sin(t)
  fp  = lambda t: -np.cos(t)
  fpp = lambda t:  np.sin(t)

  y = bowie_ode ( tspan, y0, n, f, fp, fpp )

  t = np.linspace ( tstart, tstop, n + 1 )

  time_plot ( t, y, 'pendulum_bowie' )

  phase_plot ( y, 'pendulum_bowie' )

  return

def phase_plot ( y, title ):

#*****************************************************************************80
#
## phase_plot() plots (y0(t),y1(t)).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 January 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  plt.clf ( )
  plt.plot ( y[0,0], y[0,1], 'g.', markersize = 15 )
  plt.plot ( y[-1,0], y[-1,1], 'r.', markersize = 15 )
  plt.plot ( y[:,0], y[:,1], 'b-', linewidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- Y(T) --->' )
  plt.ylabel ( '<--- Y\'(T) --->' )
  plt.axis ( 'equal' )
  plt.title ( title + ' phase plot' )
  filename = title + '_phase.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def time_plot ( t, y, title ):

#*****************************************************************************80
#
## time_plot() plots (t,y0(t)) and (t,y1(t)).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 January 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  plt.clf ( )
  plt.plot ( t, y[:,0], 'g-', linewidth = 2 )
  plt.plot ( t, y[:,1], 'r-', linewidth = 2 )
  plt.legend ( [ 'y0', 'y1'] )
  plt.grid ( True )
  plt.xlabel ( '<--- T --->' )
  plt.ylabel ( '<--- Y0(T), Y1(T) --->' )
  plt.title ( title + ' time plot' )
  filename = title + '_time.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def bowie_ode ( tspan, y0, n, f, fp, fpp ):

#*****************************************************************************80
#
## bowie_ode() solves an ODE of the form y" = f(y) given f, f' and f".
#
#  Discussion:
#
#    The method as described seems to require that the ODE not only be
#    autonomous (no explicit dependence on t), but also cannot involve
#    y' either.  The nonlinear pendulum equation y"=-sin(y) is an example
#    that satisfies these strong limitations.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 January 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Bowie integrator and the nonlinear pendulum,
#    https://www.johndcook.com/blog/2025/12/23/bowie-integrator-and-the-nonlinear-pendulum/
#    Posted 23 December 2025, updated 04 January 2026.
#
#    NASA Orbital Flight Handbook Part 1,
#    Pages IV-8 and IV-9,
#    https://ntrs.nasa.gov/api/citations/19630011221/downloads/19630011221.pdf
#
#    Alex Scarazzini,
#    3D Visualization of a Schwarzschild Black Hole Environment. 
#    Master's Thesis,
#    University of Bern, August 2025.
#
  import numpy as np

  y = np.zeros ( [ n + 1, 2 ] )

  h = ( tspan[1] - tspan[0] ) / n

  for i in range ( 0, n + 1 ):

    if ( i == 0 ):
      y[i,0] = y0[0]
      y[i,1] = y0[1]
    else:
      y[i,0] = y[i-1,0] \
        + h           * y[i-1,1] \
        + h**2 /  2.0 * f(y[i-1,0]) \
        + h**3 /  6.0 * fp(y[i-1,0])  * y[i-1,1] \
        + h**4 / 24.0 * fpp(y[i-1,1]) * y[i-1,1]**2 \
        + h**4 / 24.0 * fp(y[i-1,0])  * f(y[i-1,0])

      y[i,1] = y[i-1,1] \
        + h          * f(y[i-1,0]) \
        + h**2 / 2.0 * fp(y[i-1,0])  * y[i-1,1] \
        + h**3 / 6.0 * fpp(y[i-1,1]) * y[i-1,1]**2 * f(y[i-1,0]) \
        + h**3 / 6.0 * fp(y[i-1,0])  * f(y[i-1,0])

  return y

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
  bowie_test ( )
  timestamp ( )

