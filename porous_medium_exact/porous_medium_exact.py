#! /usr/bin/env python3
#
def porous_medium_exact_test ( ):

#*****************************************************************************80
#
## porous_medium_exact_test() tests porous_medium_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'porous_medium_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test porous_medium_exact(),' )
  print ( '  an exact solution of the porous medium equation.' )
#
#  Report the current parameter values.
#
  c, delta, m, t0, tstop = porous_medium_parameters ( )

  print ( '' )
  print ( '  parameters:' )
  print ( '    c = ', c )
  print ( '    delta = ', delta )
  print ( '    m = ', m )
  print ( '    t0 = ', t0 )
  print ( '    tstop = ', tstop )

  porous_medium_residual_test ( tstop )
#
#  Terminate.
#
  print ( '' )
  print ( 'porous_medium_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def porous_medium_exact ( x, t ):

#*****************************************************************************80
#
## porous_medium_exact() evaluates an exact solution of the porous medium equation.
#
#  Discussion:
#
#    du/dt = Del^2 ( u^m )
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Grigory Barenblatt,
#    On some unsteady fluid and gas motions in a porous medium,
#    Prikladnaya Matematika i Mekhanika (Applied Mathematics and Mechanics, 
#    Volume 16, Number 1, pages 67-78, 1952.
#
#    Rouben Rostamian,
#    Programming Projects in C 
#    for Students of Engineering, Science, and Mathematics,
#    SIAM, 2014,
#    ISBN: 978-1-611973-49-5
#
#  Input:
#
#    real x, t: the position and time.
#
#  Output:
#
#    real u, ut, ux, uxx: the values of the exact solution, its time
#    derivative, and its first and second spatial derivatives at (x,t).
#
  c, delta, m, t0, tstop = porous_medium_parameters ( )

  alpha =         1.0 / ( m - 1.0 )
  beta =          1.0 / ( m + 1.0 )
  gamma = ( m - 1.0 ) / ( 2.0 * m * ( m + 1.0 ) )

  bot = ( t + delta )**beta
  factor = c - gamma * ( x / bot )**2

  if ( 0.0 < factor ):

    u = 1.0 / ( t + delta)**beta * factor**alpha

    ut = 2.0 * alpha * beta * gamma * ( t + delta )**(-1.0-3.0*beta) \
      * x**2 * factor**(alpha - 1.0) \
      - beta * ( t + delta )**(-1.0-beta) * factor**alpha

    ux = - 2.0 * alpha * gamma \
      * ( t + delta )**(-3.0 * beta ) * x * factor**(alpha-1.0)

    uxx = 4.0 * ( alpha - 1.0 ) * alpha * gamma**2 \
      * ( t + delta )**(-5.0*beta) * x**2 * factor**(alpha-2.0) \
      - 2.0 * alpha * gamma * ( t + delta )**(-3.0 * beta ) * factor**(alpha-1.0)

  else:

    u = 0.0
    ut = 0.0
    ux = 0.0
    uxx = 0.0

  return u, ut, ux, uxx

def porous_medium_residual_test ( tstop ):

#*****************************************************************************80
#
## porous_medium_residual_test() tests porous_medium_residual().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'porous_medium_residual_test():' )
  print ( '  Evaluate solution and residual at selected points (X,T)' )
  
  n = 11
  m = 5
  x = np.linspace ( -1.0, 1.0, n )
  t = np.linspace ( 0.0, tstop, m )

  print ( '' )
  print ( '      X       T       U(X,T)      Resid(X,T)' )
  print ( '' )
  for j in range ( 0, m ):
    for i in range ( 0, n ):
      u, ut, ux, uxx = porous_medium_exact ( x[i], t[j] )
      r = porous_medium_residual ( x[i], t[j] )
      print ( '  %8.4f  %8.4f  %10.4g  %g' % ( x[i], t[j], u, r ) )
    print ( '' )

  return

def porous_medium_parameters ( c_user = None, delta_user = None, \
  m_user = None, t0_user = None, tstop_user = None ):

#*****************************************************************************80
#
## porous_medium_parameters() returns parameters for the porous medium equation.
#
#  Discussion:
#
#    du/dt = Del^2 ( u^m )
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
#    19 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real c_user: a linear factor for the volume of the solution at any time. 
#
#    real delta_user: an offset to the time t.
#
#    real m_user: the power of u in the equation.  m must be greater than 1.
#
#    real t0_user: the initial time.
#
#    real tstop_user: the final time.
#
#  Output:
#
#    real c: a linear factor for the volume of the solution at any time. 
#
#    real delta: an offset to the time t.
#
#    real m: the power of u in the equation.  m must be greater than 1.
#
#    real t0: the initial time.
#
#    real tstop: the final time.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( porous_medium_parameters, "c_default" ):
    porous_medium_parameters.c_default = np.sqrt ( 3.0 ) / 15.0

  if not hasattr ( porous_medium_parameters, "delta_default" ):
    porous_medium_parameters.delta_default = 1.0 / 75.0

  if not hasattr ( porous_medium_parameters, "m_default" ):
    porous_medium_parameters.m_default = 3

  if not hasattr ( porous_medium_parameters, "t0_default" ):
    porous_medium_parameters.t0_default = 0.0

  if not hasattr ( porous_medium_parameters, "tstop_default" ):
    porous_medium_parameters.tstop_default = 4.0
#
#  Update defaults if input was supplied.
#
  if ( c_user is not None ):
    porous_medium_parameters.c_default = c_user

  if ( delta_user is not None ):
    porous_medium_parameters.delta_default = delta_user

  if ( m_user is not None ):
    porous_medium_parameters.m_default = m_user

  if ( t0_user is not None ):
    porous_medium_parameters.t0_default = t0_user

  if ( tstop_user is not None ):
    porous_medium_parameters.tstop_default = tstop_user
#
#  Return values.
#
  c = porous_medium_parameters.c_default
  delta = porous_medium_parameters.delta_default
  m = porous_medium_parameters.m_default
  t0 = porous_medium_parameters.t0_default
  tstop = porous_medium_parameters.tstop_default

  return c, delta, m, t0, tstop

def porous_medium_residual ( t, x ):

#*****************************************************************************80
#
## porous_medium_residual() computes the residual of the porous medium equation.
#
#  Discussion:
#
#    ut = Del^2 ( u^m )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T, X: the time and position where the solution is evaluated.
#
#  Output:
#
#    real R: the residual at that time and position.
#
  c, delta, m, t0, tstop = porous_medium_parameters ( )

  u, ut, ux, uxx = porous_medium_exact ( t, x )

  r = ut - m * ( m - 1 ) * u**(m-2) * ux**2 - m * u**(m-1) * uxx

  return r

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
  porous_medium_exact_test ( )
  timestamp ( )

