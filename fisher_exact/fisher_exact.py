#! /usr/bin/env python3
#
def fisher_exact_test ( ):

#*****************************************************************************80
#
## fisher_exact_test() tests fisher_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fisher_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test fisher_exact(), for exact solutions of Fisher PDE.' )
#
#  Report the current parameter values.
#
  a, c, k = fisher_parameters ( )
  print ( '' )
  print ( '  parameters:' )
  print ( '    a = ', a )
  print ( '    c = ', c )
  print ( '    k = ', k )

  f_residual_test ( )

  fisher_residual_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'fisher_exact_test():' )
  print ( '  Normal end of execution.' )

  timestamp ( )

  return

def f_exact ( z ):

#*****************************************************************************80
#
## f_exact() computes a function related to an exact solution of the KPP Fisher PDE.
#
#  Discussion:
#
#    ut = uxx + u * ( 1 - u )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Mark Ablowitz, Anthony Zeppetella,
#    Explicit solutions of Fisher's equation for a special wave speed,
#    Bulletin of Mathematical Biology,
#    Volume 41, pages 835-840, 1979.
#
#    Daniel Arrigo,
#    Analytical Techniques for Solving Nonlinear Partial Differential Equations,
#    Morgan and Clayfoot, 2019,
#    ISBN: 978 168 173 5351.
#
#  Input:
#
#    real Z: the evaluation point.
#
#  Output:
#
#    real F, FZ, FZZ: the function and derivatives at Z.
#
  import numpy as np

  a, c, k = fisher_parameters ( )

  f =     1.0 / ( 1.0 + a * np.exp ( k * z ) )**2
  fz =  - 2.0 / ( 1.0 + a * np.exp ( k * z ) )**3 * a    * k    * np.exp (       k * z )
  fzz = + 6.0 / ( 1.0 + a * np.exp ( k * z ) )**4 * a**2 * k**2 * np.exp ( 2.0 * k * z ) \
        - 2.0 / ( 1.0 + a * np.exp ( k * z ) )**3 * a    * k**2 * np.exp (       k * z ) 

  return f, fz, fzz

def fisher_exact ( t, x ):

#*****************************************************************************80
#
## fisher_exact() computes an exact solution of the KPP Fisher equation.
#
#  Discussion:
#
#    ut = uxx + u * ( 1 - u )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Mark Ablowitz, Anthony Zeppetella,
#    Explicit solutions of Fisher's equation for a special wave speed,
#    Bulletin of Mathematical Biology,
#    Volume 41, pages 835-840, 1979.
#
#    Daniel Arrigo,
#    Analytical Techniques for Solving Nonlinear Partial Differential Equations,
#    Morgan and Clayfoot, 2019,
#    ISBN: 978 168 173 5351.
#
#  Input:
#
#    real T, X: the time and position at which the solution is evaluated.
#
#  Output:
#
#    real U, UT, UX, UXX: the exact solution and derivatives at (T,X).
#
  import numpy as np

  a, c, k = fisher_parameters ( )

  z = x - c * t

  u =     1.0     / ( 1.0 + a * np.exp ( k * z ) )**2
  ut =    2.0 * c / ( 1.0 + a * np.exp ( k * z ) )**3 * a    * k    * np.exp (       k * z )
  ux =  - 2.0     / ( 1.0 + a * np.exp ( k * z ) )**3 * a    * k    * np.exp (       k * z )
  uxx = + 6.0     / ( 1.0 + a * np.exp ( k * z ) )**4 * a**2 * k**2 * np.exp ( 2.0 * k * z ) \
        - 2.0     / ( 1.0 + a * np.exp ( k * z ) )**3 * a    * k**2 * np.exp (       k * z ) 

  return u, ut, ux, uxx

def f_residual_test ( ):

#*****************************************************************************80
#
## f_residual_test() tests f_residual().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'f_residual_test():' )
  print ( '  Evaluate F(Z) and residual at selected points Z=X-cT' )

  x = np.linspace ( 0.0, 1.0, 6 )
  t = np.linspace ( 0.0, 10.0, 6 )

  a, c, k = fisher_parameters ( )

  print ( '' )
  print ( '      Z       F(Z)      Resid(Z)' )
  print ( '' )

  for j in range ( 0, 6 ):
    for i in range ( 0, 6 ):
      z = x[i] - c * t[j]
      f, fz, fzz = f_exact ( z )
      r = f_residual ( f, fz, fzz )
      print ( '  %f  %f  %g' % ( z, f, r ) )
    print ( '' )

  return

def fisher_residual_test ( ):

#*****************************************************************************80
#
## fisher_residual_test() tests fisher_residual().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'fisher_residual_test():' )
  print ( '  Evaluate solution and residual at selected points (X,T)' )
  
  x = np.linspace ( 0.0, 1.0, 6 )
  t = np.linspace ( 0.0, 10.0, 6 )

  print ( '' )
  print ( '      X       T       U(X,T)      Resid(X,T)' )
  print ( '' )

  for j in range ( 0, 6 ):
    for i in range ( 0, 6 ):
      u, ut, ux, uxx = fisher_exact ( x[i], t[j] )
      r = fisher_residual ( x[i], t[j] )
      print ( '  %f  %f  %f  %g' % ( x[i], t[j], u, r ) )
    print ( '' )

  return

def fisher_parameters ( a_user = None, c_user = None, k_user = None ):

#*****************************************************************************80
#
## fisher_parameters() returns parameters for the Fisher ODE.
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
#    06 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A_USER: a new value for A.
#
#    real C_USER: a new value for C.
#
#    real K_USER: a new value for K.
#
#  Output:
#
#    real A: the default or new value for A.
#
#    real C: the default or new value for C.
#
#    real K: the default or new value for K.
#
  import numpy as np
#
#  Initialize defaults.
#
  if not hasattr ( fisher_parameters, "a_default" ):
    fisher_parameters.a_default = 2.0

  if not hasattr ( fisher_parameters, "c_default" ):
    fisher_parameters.c_default = 5.0 / np.sqrt ( 6.0 )

  if not hasattr ( fisher_parameters, "k_default" ):
    fisher_parameters.k_default = 1.0 / np.sqrt ( 6.0 )
#
#  Update defaults if input was supplied.
#
  if ( a_user is not None ):
    fisher_parameters.a_default = a_user

  if ( c_user is not None ):
    fisher_parameters.c_default = c_user

  if ( k_user is not None ):
    fisher_parameters.k_default = k_user
#
#  Return values.
#
  a = fisher_parameters.a_default
  c = fisher_parameters.c_default
  k = fisher_parameters.k_default

  return a, c, k

def fisher_residual ( t, x ):

#*****************************************************************************80
#
## fisher_residual() computes the residual of the KPP Fisher equation.
#
#  Discussion:
#
#    ut = uxx + u * ( 1 - u )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Mark Ablowitz, Anthony Zeppetella,
#    Explicit solutions of Fisher's equation for a special wave speed,
#    Bulletin of Mathematical Biology,
#    Volume 41, pages 835-840, 1979.
#
#    Daniel Arrigo,
#    Analytical Techniques for Solving Nonlinear Partial Differential Equations,
#    Morgan and Clayfoot, 2019,
#    ISBN: 978 168 173 5351.
#
#  Input:
#
#    real T, X: the time and position where the solution is evaluated.
#
#  Output:
#
#    real R: the residual at that time and position.
#
  u, ut, ux, uxx = fisher_exact ( t, x )
  r = ut - uxx - u * ( 1.0 - u )

  return r

def f_residual ( f, fz, fzz ):

#*****************************************************************************80
#
## f_residual() computes a residual related to the KPP Fisher equation.
#
#  Discussion:
#
#    The KPP Fisher equation is
#
#      ut = uxx + u * ( 1 - u )
#
#    For a particular value of c, and function f(z), the KPP Fisher 
#    equation admits a traveling wave solution of the form
#
#      u(x,t) = f(x-ct) = f(z)
#
#    where the function f(z) satisfies the ODE
#
#      f'' + cf' + f - f^2 = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 May 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Mark Ablowitz, Anthony Zeppetella,
#    Explicit solutions of Fisher's equation for a special wave speed,
#    Bulletin of Mathematical Biology,
#    Volume 41, pages 835-840, 1979.
#
#    Daniel Arrigo,
#    Analytical Techniques for Solving Nonlinear Partial Differential Equations,
#    Morgan and Clayfoot, 2019,
#    ISBN: 978 168 173 5351.
#
#  Input:
#
#    real F, FZ, FZZ: the associated function and derivatives.
#
#  Output:
#
#    real R: the residual of the f(z) solution at that time and position.
#
  a, c, k = fisher_parameters ( )

  r = fzz + c * fz + f - f**2

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
  fisher_exact_test ( )
  timestamp ( )

