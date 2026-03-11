#! /usr/bin/env python3
#
def mhd_exact_test ( ):

#*****************************************************************************80
#
## mhd_exact_test() tests mhd_exact().
#
#  Discussion:
#
#    mhd_exact() describes the Hartmann exact solution of a 2D MHD system.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Frederic Gerbeau, Claude Le Bris, Tony Lelievre,
#    Mathematical methods for the magnetohydrodynamics
#    of liquid metals,
#    Oxford University Press, 2006,
#    ISBN 978-0-19-856665-6
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'mhd_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Define the Hartmann exact solution of the 2D MHD equation.' )

  mhd_resid_test ( )
  vector_plot ( )
  contour_plot ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'mhd_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def contour_plot ( ):

#*****************************************************************************80
#
## contour_plot() makes a contour plot of pressure.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 August 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'contour_plot():' )
  print ( '  Make a filled color contour plot of pressure.' )
#
#  Get the spatial data.
#
  G, Ha, L, p0, Re, Rm, S = mhd_parameters ( )

  xvec = np.linspace ( 0.0, L, 21 )
  yvec = np.linspace ( -1.0, 1.0, 11 )
  
  X, Y = np.meshgrid ( xvec, yvec )
#
#  Evaluate the solution.
#
  U, V, P, B1, B2 = mhd_solution ( X, Y )
#
#  Plot the pressure.
#
  plt.contourf ( X, Y, P )

  plt.title ( 'pressure contours' )

  filename = 'pressure_contour.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def mhd_parameters ( g_user = None, ha_user = None, l_user = None, \
  p0_user = None, re_user = None, rm_user = None ):

#*****************************************************************************80
#
## mhd_nonlinear_parameters(): parameters for the MHD problem.
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
#    26 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Frederic Gerbeau, Claude Le Bris, Tony Lelievre,
#    Mathematical methods for the magnetohydrodynamics
#    of liquid metals,
#    Oxford University Press, 2006,
#    ISBN 978-0-19-856665-6
#
#  Input:
#
#    real g_user: a linear factor multiplying the solution
#
#    real ha_user: the Hartmann number, B*L*sqrt(sigma/nu).
#
#    real l_user: the length of the channel.
#
#    real p0_user: the base pressure.
#
#    real re_user: the fluid Reynolds number.
#
#    real rm_user: the magnetic Reynolds number.
#
#  Output:
#
#    real g: a linear factor multiplying the solution
#
#    real ha: the Hartmann number.
#
#    real l: the length of the channel.
#
#    real p0: the base pressure
#
#    real re: the fluid Reynolds number
#
#    real rm: the magnetic Reynolds number.
#
#    real s: a linear scale factor for the relative sizes of u and b.
#

#
#  Initialize defaults.
#
  if not hasattr ( mhd_parameters, "g_default" ):
    mhd_parameters.g_default = 1.0

  if not hasattr ( mhd_parameters, "ha_default" ):
    mhd_parameters.ha_default = 1.0

  if not hasattr ( mhd_parameters, "l_default" ):
    mhd_parameters.l_default = 10.0

  if not hasattr ( mhd_parameters, "p0_default" ):
    mhd_parameters.p0_default = 4.0

  if not hasattr ( mhd_parameters, "re_default" ):
    mhd_parameters.re_default = 10.0

  if not hasattr ( mhd_parameters, "rm_default" ):
    mhd_parameters.rm_default = 6.0
#
#  Update defaults if input was supplied.
#
  if ( g_user is not None ):
    mhd_parameters.g_default = g_user

  if ( ha_user is not None ):
    mhd_parameters.ha_default = ha_user

  if ( l_user is not None ):
    mhd_parameters.l_default = l_user

  if ( p0_user is not None ):
    mhd_parameters.p0_default = p0_user

  if ( re_user is not None ):
    mhd_parameters.re_default = re_user

  if ( rm_user is not None ):
    mhd_parameters.rm_default = rm_user
#
#  Return values.
#
  g = mhd_parameters.g_default
  ha = mhd_parameters.ha_default
  l = mhd_parameters.l_default
  p0 = mhd_parameters.p0_default
  re = mhd_parameters.re_default
  rm = mhd_parameters.rm_default
  s = ha**2 / re / rm
  
  return g, ha, l, p0, re, rm, s

def mhd_resid ( x, y ):

#*****************************************************************************80
#
## mhd_resid(): residuals for underlying exact solution definitions.
#
#  Discussion:
#
#    Formulas for u(y) and b(y) are used to define an exact solution
#    of an MHD system.  This function tests whether these formulas
#    satisfy the underlying equations involving u''(y) and b''(y).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Frederic Gerbeau, Claude Le Bris, Tony Lelievre,
#    Mathematical methods for the magnetohydrodynamics
#    of liquid metals,
#    Oxford University Press, 2006,
#    ISBN 978-0-19-856665-6
#
#  Input:
#
#    real X(:), Y(:): the spatial locations.
#
#  Output:
#
#    real ur(:):
#
#    real br(:):
#
  import numpy as np

  G, Ha, L, p0, Re, Rm, S = mhd_parameters ( )
#
#  The velocity function u(y):
#
  u =     G * Re / np.tanh ( Ha ) / Ha * ( 1.0 - np.cosh ( y * Ha ) / np.cosh ( Ha ) )
  uy =  - G * Re / np.sinh ( Ha )              * np.sinh ( y * Ha )
  uyy = - G * Re / np.sinh ( Ha ) * Ha         * np.cosh ( y * Ha )
#
#  The magnetic field function b(y):
#
  b =   G / S * (           np.sinh ( y * Ha ) / np.sinh ( Ha ) - y )
  by =  G / S * ( Ha      * np.cosh ( y * Ha ) / np.sinh ( Ha ) - 1.0 )
  byy = G / S *   Ha**2 * ( np.sinh ( y * Ha ) / np.sinh ( Ha ) )
#
#  Residuals associated with velocity and magnetic field.
#
  ur = uyy + Re * S * by + G * Re
  br = byy + Rm * uy

  return ur, br

def mhd_resid_test ( ):

#*****************************************************************************80
#
## mhd_resid_test() tests mhd_resid().
#
#  Discussion:
#
#    Formulas for u(y) and b(y) are used to define an exact solution
#    of an MHD system.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Frederic Gerbeau, Claude Le Bris, Tony Lelievre,
#    Mathematical methods for the magnetohydrodynamics
#    of liquid metals,
#    Oxford University Press, 2006,
#    ISBN 978-0-19-856665-6
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'mhd_resid_test():' )
  print ( '  Compute maximum residual over sample points for' )
  print ( '  functions u(y) and b(y) that define an exact solution' )
  print ( '  of the Hartmann MHD solution.' )

  G, Ha, L, p0, Re, Rm, S = mhd_parameters ( )
#
#  Select random points in the region.
#
  x = 0.0 + L * rng.random ( 10 )
  y = -1.0 + 2.0 * rng.random ( 10 )
#
#  Evaluate the residuals.
#
  ur, br = mhd_resid ( x, y )

  print ( '' )
  print ( '  Maximum residual in u(y) equation = ', np.max ( np.abs ( ur ) ) )
  print ( '  Maximum residual in b(y) equation = ', np.max ( np.abs ( br ) ) )

  return

def mhd_solution ( x, y ):

#*****************************************************************************80
#
## mhd_solution(): Hartmann exact solution of a steady 2D MHD equation.
#
#  Discussion:
#
#    We consider the domain XxY = [0,L]x[-1,+1].
#    The horizontal velocity u(x,y) is constant along any fixed y value.
#    The vertical velocity v(x,y) is zero everywhere.
#    The magnetic field B satisfies B(x,y) = (b(y),1).
#    The boundary walls y=-1 and y=+1 have no slip boundary conditions:
#      u(x,-1) = u(x,+1) = 0
#    The inlet x=0 and outlet x=L have Neumann boundary conditions:
#      -p n + 1/Re (Del u,n) = - pd n
#    where n is the unit normal vector and the pressure pd is given.
#    The walls are perfectly insulating.
#    On the boundary, we impose the tangential part of the magnetic field:
#      B x n = Bd x n
#    where the external transverse magnetic field Bd is given
#    as Bd(x,y)=(0,1).
#
#      pd(x,y) = - G x - 1/2 S b(y)^2 + p0
#      u''(x,y) + Re S b'(y) = - G Re
#      v(x,y) = 0
#      b''(x,y) + R m u'(x,y) = 0
#
#    The system to be solved is
#
#      -1/Re del^2 u + del p + u dot del u + s B cross curl B = f
#      div u = 0
#      1/Rm curl ( curl ( B ) ) - curl ( u cross B ) = h
#      div B = 0
#
#    with homogeneous boundary conditions
#
#      1/Rm curl B cross n = 0
#      B dot n = 0
#      u = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jean-Frederic Gerbeau, Claude Le Bris, Tony Lelievre,
#    Mathematical methods for the magnetohydrodynamics
#    of liquid metals,
#    Oxford University Press, 2006,
#    ISBN 978-0-19-856665-6
#
#  Input:
#
#    real X(:), Y(:): the spatial locations.
#
#  Output:
#
#    real U(:), V(:), P(:), B1(:), B2(:): the solution components
#    (velocity, pressure, magnetic field).
#
  import numpy as np

  G, Ha, L, p0, Re, Rm, S = mhd_parameters ( )

  u = G * Re / Ha / np.tanh ( Ha ) * ( 1.0 - np.cosh ( y * Ha ) / np.cosh ( Ha ) )
  v = np.zeros_like ( x )
  b = G / S * ( np.sinh ( y * Ha ) / np.sinh ( Ha ) - y )
  b1 = b
  b2 = np.ones_like ( x )
  p = - G * x - 0.5 * S * b**2

  return u, v, p, b1, b2

def vector_plot ( ):

#*****************************************************************************80
#
## vector_plot() plots the flow velocity and magnetic field.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'vector_plot():' )
  print ( '  Plot velocity and magnetic fields using vectors.' )
#
#  Get the spatial data.
#
  G, Ha, L, p0, Re, Rm, S = mhd_parameters ( )

  xvec = np.linspace ( 0.0, L, 21 )
  yvec = np.linspace ( -1.0, 1.0, 11 )
  
  X, Y = np.meshgrid ( xvec, yvec )
#
#  Evaluate the solution.
#
  U, V, P, B1, B2 = mhd_solution ( X, Y )
#
#  Make the vector field (U,V).
#
  plt.clf ( )
#
#  Plot the vectors.
#  For some idiotic reason, scale doesn't do ANYTHING.
#  Worse, documentation claims "scale" is an inverse scale!
#
  scale = 0.50
  plt.quiver ( X, Y, U, V, scale )
#
#  Finish the plot.
#
  plt.axis ( 'equal' )
  plt.axis ( 'tight' )
  plt.xlabel ( '<--X-->' )
  plt.ylabel ( '<--Y-->' )
  plt.title ( 'Velocity vector field' )
  filename = 'velocity_vector.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Plot (B1,B2).
#
  plt.clf ( )
#
#  Plot the vectors.
#
  scale = 0.75
  plt.quiver ( X, Y, B1, B2, scale )
#
#  Finish the plot.
#
  plt.axis ( 'equal' )
  plt.axis ( 'tight' )
  plt.xlabel ( '<--X-->' )
  plt.ylabel ( '<--Y-->' )
  plt.title ( 'Magnetic vector field' )
  filename = 'magnetic_vector.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

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
  mhd_exact_test ( )
  timestamp ( )

