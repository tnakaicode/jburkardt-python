#! /usr/bin/env python3
#
def bvp_shooting_test ( ):

#*****************************************************************************80
#
## bvp_shooting_test() shows the shooting method for boundary value problems.
#
#  Discussion:
#
#    Demonstrate how the solution of a boundary value problem (BVP) can be
#    approximated using an initial value problem (IVP) solver, using the
#    shooting method.
#
#    The idea is to guess the missing initial condition ALPHA, use the IVP
#    solver to get the corresponding solution, call F(ALPHA) the difference
#    between the computed solution and the desired end condition, and then
#    employ a nonlinear equation solver to seek ALPHA such that F(ALPHA)=0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Josef Stoer, Roland Bulirsch,
#    Introduction to Numerical Mathematics,
#    Springer, 2002,
#    ISBN: 038795452X,
#    LC: QA297.S8213.
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'bvp_shooting_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test bvp_shooting()' )

  print ( '' )
  print ( '  A simple example of the shooting method,' )
  print ( '  in which a boundary value problem (BVP) is solved' )
  print ( '  using an initial value problem (IVP) solver,' )
  print ( '  a guess for the missing initial condition ALPHA' )
  print ( '  and a nonlinear equation solver.' )

  bvp_shooting_test01 ( )
  bvp_shooting_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'bvp_shooting_test():' )
  print ( '  Normal end of execution.' )

  return

def bvp_shooting_test01 ( ):

#*****************************************************************************80
#
## bvp_shooting_test01() solves a boundary value problem with shooting.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'bvp_shooting_test01():' )
  print ( '  Seek the initial condition for y''(a) to determine' )
  print ( '  the solution of a two point boundary value problem:' )
  print ( '    y"=3/2 y^2, y(0)=4, y(1)=1.' )
#
#  The BVP is specified over [a,b]:
#
  a = 0.0
  b = 1.0
#
#  The side conditions are y(a) = ya, y(b) = yb.
#
  ya = 4.0
  yb = 1.0
#
#  Get the solution by shooting.
#
  x, y = bvp_shooting ( a, b, ya, yb, ode1 )
#
#  Plot the solution.
#
  plt.clf ( )
  plt.plot ( x, y, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y(X) --->' )
  plt.title ( 'Solution of y"=3/2 y^2, y(0)=4, y(1)=1.' )
  filename = 'bvp1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def bvp_shooting_test02 ( ):

#*****************************************************************************80
#
## bvp_shooting_test02() solves a boundary value problem with shooting.
#
#  Discussion:
#
#    The underlying solution function y(x) is known as the humps function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt

  print ( '' )
  print ( 'bvp_shooting_test02():' )
  print ( '  Seek the initial condition for y''(a) to determine' )
  print ( '  the solution of a two point boundary value problem:' )
  print ( '    y"=3/2 y^2, y(0)=4, y(1)=1.' )
#
#  The BVP is specified over [a,b]:
#
  a = 0.0
  b = 2.0
#
#  The side conditions are y(a) = ya, y(b) = yb.
#
  ya = humps_fun ( a )
  yb = humps_fun ( b )
#
#  Get the solution by shooting.
#
  x, y = bvp_shooting ( a, b, ya, yb, ode2 )
#
#  Plot the solution.
#
  plt.clf ( )
  plt.plot ( x, y, linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y(X) --->' )
  plt.title ( 'BVP for the humps() function.' )
  filename = 'bvp2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def bvp_shooting ( a, b, ya, yb, myode ):

#*****************************************************************************80
#
## bvp_shooting_test() shows the shooting method for boundary value problems.
#
#  Discussion:
#
#    Demonstrate how the solution of a boundary value problem (BVP) can be
#    approximated using an initial value problem (IVP) solver, using the
#    shooting method.
#
#    The idea is to guess the missing initial condition ALPHA, use the IVP
#    solver to get the corresponding solution, call F(ALPHA) the difference
#    between the computed solution and the desired end condition, and then
#    employ a nonlinear equation solver to seek ALPHA such that F(ALPHA)=0.
#
#    The secant iteration is repeated up to ITER_MAX times, a value which
#    can be adjusted by the user.
#
#    The secant iteration is terminated early if the desired boundary
#    condition is approximated to a tolerance of TOL, a value which can
#    be adjusted by the user.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Josef Stoer, Roland Bulirsch,
#    Introduction to Numerical Mathematics,
#    Springer, 2002,
#    ISBN: 038795452X,
#    LC: QA297.S8213.
#
#  Input:
#
#    real a, b: the left and right endpoints of the interval.
#
#    real ya, yb: the left and right boundary conditions:
#    y(a) = ya, y(b) = yb.
#
#    function myode: evaluates the right hand side of the BVP.
#
#  Output:
#
#    real x(*), y(*): the vectors of data defining the computed solution.
#
  from scipy.integrate import solve_ivp
  import numpy as np

  iter_max = 10
  tol = 1.0E-06

  tspan = np.array ( [ a, b ] )
  x_grid = np.linspace ( a, b, 501 )
#
#  Define F(alpha) as the computed value of y(b) - yb.
#  Evaluate F at two starting points, then take secant steps.
#  We hope that we can compute a value of alpha such that the
#  initial value problem with y'(a)=alpha will solve the boundary
#  value problem with y(b) = yb.
#
  print ( '' )
  print ( '  Iteration  Alpha  YB(Alpha)  F(ALPHA)' )
  print ( '' )

  for it in range ( - 1, iter_max + 1 ):

    if ( it == -1 ):
      alpha = 0.0
    elif ( it == 0 ):
      beta = alpha
      f_beta = f_alpha
      alpha = -1.0
    else:
      gamma = alpha - f_alpha * ( beta - alpha ) / ( f_beta - f_alpha )
      beta = alpha
      f_beta = f_alpha
      alpha = gamma

    y0 = np.array ( [ ya, alpha ] )

    sol = solve_ivp ( myode, tspan, y0, t_eval = x_grid )
    x = sol.t[:]
    y = sol.y[0,:]
    yb_alpha = y[-1]
    f_alpha = yb_alpha - yb
    print ( '  %d  %g  %g  %g' % ( it, alpha, yb_alpha, f_alpha ) )

    if ( np.abs ( f_alpha ) < tol ):
      break

  return x, y

def humps_deriv2 ( x ):

#*****************************************************************************80
#
## humps_deriv2() evaluates the second derivative of the humps function.
#
#  Discussion:
#
#    y = 1.0 / ( ( x - 0.3 )**2 + 0.01 ) \
#      + 1.0 / ( ( x - 0.9 )**2 + 0.04 ) \
#      - 6.0
#
#    ypp = - 2.0 * ( x - 0.3 ) / ( ( x - 0.3 )**2 + 0.01 )**2 \
#          - 2.0 * ( x - 0.9 ) / ( ( x - 0.9 )**2 + 0.04 )**2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(): the arguments.
#
#  Output:
#
#    real ypp(): the value of the second derivative at x.
#
  u1 = - 2.0 * ( x - 0.3 )
  v1 = ( ( x - 0.3 )**2 + 0.01 )**2
  u2 = - 2.0 * ( x - 0.9 )
  v2 = ( ( x - 0.9 )**2 + 0.04 )**2

  u1p = - 2.0
  v1p = 2.0 * ( ( x - 0.3 )**2 + 0.01 ) * 2.0 * ( x - 0.3 ) 
  u2p = - 2.0
  v2p = 2.0 * ( ( x - 0.9 )**2 + 0.04 ) * 2.0 * ( x - 0.9 )

  ypp = ( u1p * v1 - u1 * v1p ) / v1**2 \
      + ( u2p * v2 - u2 * v2p ) / v2**2

  return ypp

def humps_fun ( x ):

#*****************************************************************************80
#
## humps_fun() evaluates the humps function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(): the evaluation points.
#
#  Output:
#
#    real y(): the function values.
#
  y = 1.0 / ( ( x - 0.3 )**2 + 0.01 ) \
    + 1.0 / ( ( x - 0.9 )**2 + 0.04 ) \
    - 6.0

  return y

def ode1 ( x, y ):

#*****************************************************************************80
#
## ode1() evaluates the right hand side of the differential equation.
#
#  Discussion:
#
#    y" = 3/2 y^2 is rewritten as a pair of first order equations:
#
#    y'(1) = y(2)
#    y'(2) = 3/2 y(1)^2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(*): values of the independent variable.
#
#    real y(2,*): values of the dependent variable.
#
#    real dydx(2,*): values of the derivative.
#
  import numpy as np

  dydx = np.array ( [ y[1], 1.5 * y[0]**2 ] )

  return dydx

def ode2 ( x, y ):

#*****************************************************************************80
#
## ode2() evaluates the right hand side of the differential equation.
#
#  Discussion:
#
#    y" = humps_deriv2 is rewritten as a pair of first order equations:
#
#    y'(1) = y(2)
#    y'(2) = humps_deriv2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(*): values of the independent variable.
#
#    real y(2,*): values of the dependent variable.
#
#    real dydx(2,*): values of the derivative.
#
  import numpy as np

  dydx = np.array ( [ y[1],  humps_deriv2 ( x ) ] )

  return dydx

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
  bvp_shooting_test ( )
  timestamp ( )

