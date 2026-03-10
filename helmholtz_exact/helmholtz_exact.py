#! /usr/bin/env python3
#
def helmholtz_exact_test ( ):

#*****************************************************************************80
#
## helmholtz_exact_test() tests helmholtz_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'helmholtz_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test helmholtz_exact().' )

  m = 0
  n = 1
  helmholtz_exact_plot ( m, n )

  m = 1
  n = 2
  helmholtz_exact_plot ( m, n )

  m = 2
  n = 3
  helmholtz_exact_plot ( m, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'helmholtz_exact_test():' )
  print ( '  Normal end of execution.' )

  return

def helmholtz_exact ( a, m, n, alpha, beta, gamma, nxy, x, y ):

#*****************************************************************************80
#
## helmholtz_exact() evaluates an exact solution of the Helmholtz equation.
#
#  Discussion:
#
#    We consider the Helmholtz equation for Z(x,y):
#      Del^2 Z = - k^2 Z
#    where k is a parameter.  We suppose we are interested in the
#    problem when describing the vertical deflection of a vibrating circular
#    membrane, centered at the origin, of radius a.
#
#    In radial coordinates, the equation in Z(r,theta) becomes
#      Zrr + 1/r Zr + 1/r^2 Ztt + k^2 Z = 0
#    We impose the condition that Z vanishes on the circumference:
#      Z(a,theta) = 0 for all theta.
#    We try separation of variables:
#      Z(r,theta) = R(r) T(theta)
#    for which we can suppose that T is periodic
#      T'' + n^2 T = 0 for some n
#    whence
#      T(theta) = alpha * cos ( n * theta ) + beta * sin ( n * theta )
#    and
#      r^2 R'' + r R' + r^2 k^2 R - n^2 R = 0
#    for which the solution is
#      R(r) = gamma * Jn(k*r), gamma arbitrary
#    For each value of n, the Bessel function has infinitely many roots,
#    denoted by rho(m,n). 
#    To enforce the zero boundary condition at r=a, we must have that
#    the parameter k is related to some m-th zero of some n-th Bessel
#    function Jn() by:
#      k(m,n) = rho(m,n)/a
#    An exact solution of the Helmholtz equation, as a function of
#    r and theta, can then be written as a sum of terms of the form
#      gamma * Jn ( rho(m,n) * r / a ) 
#      * alpha * cos ( n * theta ) + beta * sin ( n * theta )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    This discussion relies on the Wikipedia article "Helmholtz Equation".
#
#  Input:
#
#    real a: the radius of the disk.
#
#    integer m: the index of a zero of the Jn(x) Bessel function.
#    Except when n=0, the index m=0 chooses the root zt 0.
#    When n=0, there is not a root at 0, and so m=0 is illegal.
#    In any case, m=1 is the first root of Jn(x) greater than 0, 
#    2 indexes the second smallest root and so on.
#
#    integer n: the index of the J Bessel function.
#
#    real alpha, beta: the coefficients of cosine(theta) and sine(theta)
#    in the angular factor.
#
#    real gamma: the multiplier for the radial factor.
#
#    integer nxy: the number of Cartesian coordinates at which Z should
#    be sampled.
#
#    real x(nxy), y(nxy): the Cartestian coordinates at which Z should
#    be sampled.
#
#  Output:
#
#    real Z(nxy): the solution value at (x,y).
#
  from scipy.special import jn
  from scipy.special import jn_zeros
  import numpy as np
#
#  Convert Cartesian data to polar form.
#
  theta = np.arctan2 ( y, x )
  r = np.hypot ( x, y )
#
#  Evaluate angular component T(theta).
#
  T = alpha * np.cos ( n * theta ) + beta * np.sin ( n * theta )
#
#  Evaluate the m-th zero of the n-th J bessel function.
#  To complicate things, Jn(x) has its first zero at zero,
#  except for n = 0.  So...an input of m=0 requests the 
#  special zero zero, which is illegal if n = 0.
#
  if ( m == 0 ):

    if ( n == 0 ):
      print ( '' )
      print ( 'helmholtz_exact(): Fatal error!' )
      print ( '  m = 0 requests special first zero at 0.' )
      print ( '  This is illegal, because you specified n = 0 as well.' )
      raise Exception ( 'helmholtz_exact(): Fatal error!' )

    rho = 0.0

  else:

    rho_vec = jn_zeros ( n, m )
    rho = rho_vec[m-1] * r / a
#
#  Evaluate the radial component R(r).
#
  R = gamma * jn ( n, rho )
#
#  Z is the elementwise product.
#
  Z = R * T

  return Z

def helmholtz_exact_plot ( m, n ):

#*****************************************************************************80
#
## helmholtz_exact_plot() plots an exact solution of the Helmholtz equation.
#
#  Discussion:
#
#    The solution is assumed to have a simple form depending on the n-th
#    J Bessel function and its m-th root.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 July 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer m: the index of the root of the Bessel function J(n,x).
#
#    integer n: the index of the Bessel function.
#
  import matplotlib.pyplot as plt
  import matplotlib.tri as mtri
  import numpy as np

  a = 1.5

  alpha = 4.0
  beta = 3.0
  gamma = 2.0

  nt = 48
  nr = 20
  t = np.linspace ( 0.0, 2.0 * np.pi, nt + 1 )
  t = t[0:nt]
  r = np.linspace ( 0.0, 1.0, nr )
  r = np.sqrt ( r )
  r = r * a

  nxy = ( nr - 1 ) * nt + 1
  X = np.zeros ( nxy )
  Y = np.zeros ( nxy )
  nxy = 0
  for i in range ( 0, nt ):
    for j in range ( 0, nr ):
      if ( j == 0 and 0 < i ):
        pass
      else:
        X[nxy] = r[j] * np.cos ( t[i] )
        Y[nxy] = r[j] * np.sin ( t[i] )
        nxy = nxy + 1
#
#  Evaluate the exact solution Z at the points (X,Y).
#
  Z = helmholtz_exact ( a, m, n, alpha, beta, gamma, nxy, X, Y )
#
#  Triangulate the (X,Y) points.
#
  tri = mtri.Triangulation ( X, Y )
#
#  Make a surface plot of Z(X,Y).
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 1, 1, 1, projection = '3d' )
  ax.plot_trisurf ( X, Y, Z, triangles = tri.triangles, cmap = plt.cm.Spectral )

  filename = 'helmholtz_exact_m' + str ( m ) + '_n' + str ( n ) + '.png'
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
  helmholtz_exact_test ( )
  timestamp ( )

