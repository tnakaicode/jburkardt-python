#! /usr/bin/env python3
#
def line_cvt_lloyd_test ( ):

#*****************************************************************************80
#
## line_cvt_lloyd_test() tests line_cvt_lloyd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'line_cvt_lloyd_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test line_cvt_lloyd().' )

  line_cvt_lloyd_test01 ( )
  line_cvt_lloyd_test02 ( )
#
#  Repeat, using sorted initial points.
#
  line_cvt_lloyd_test03 ( )
  line_cvt_lloyd_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'line_cvt_lloyd_test():' )
  print ( '  Normal end of execution.' )

  return

def line_ccvt_lloyd ( n, a, b, it_num, header, x ):

#*****************************************************************************80
#
## line_ccvt_lloyd() carries out the constrained Lloyd algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of generators.
#
#    real A, B, the left and right endpoints.
#
#    integer IT_NUM, the number of iterations to take.
#
#    string HEADER, an identifying string.
#
#    real X(N), the initial point locations.
#
#  Output:
#
#    real X(N), the final point locations.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import pprint

  eps = np.finfo(float).eps
#
#  Print the initial generators.
#
  print ( '' )
  print ( '  Initial generators:' )
  print ( '' )
  pprint.pprint ( x )
#
#  Initialize the plotting arrays.
#
  step = np.arange ( 1, it_num + 1 )
  e = np.nan * np.ones ( it_num )
  xm = np.nan * np.ones ( it_num )
  x_plot = np.zeros ( [ it_num + 1, n ] )

  for it in range ( 0, it_num ):

    x_plot[it,:] = x.copy ( )

    x_new = line_ccvt_lloyd_step ( n, a, b, x )

    e[it] = line_cvt_energy ( n, a, b, x )
    e[it] = max ( e[it], eps )
#
#  Display the energy.
#
    plt.figure ( 1 )
    plt.plot ( step, np.log ( e ), 'm-*' )
    plt.title ( 'Log (Energy)' )
    plt.xlabel ( 'Step' )
    plt.ylabel ( 'Energy' )
    plt.grid ( True )
#
#  Compute the generator motion.
#
    xm[it] = np.sum ( ( x_new - x )**2 ) / n
#
#  Display the generator motion.
#
    plt.figure ( 2 )
    plt.plot ( step, np.log ( xm ), 'm-*' )
    plt.title ( 'Log (Average generator motion)' )
    plt.xlabel ( 'Step' )
    plt.ylabel ( 'Motion' )
    plt.grid ( True )
#
#  Update the generators.
#
    x = x_new.copy ( )

  x_plot[it_num,:] = x.copy()
#
#  Print the current generators.
#
  print ( '' )
  print ( '  Current generators:' )
  print ( '' )
  pprint.pprint ( x )
#
#  Plot the evolution of the locations of the generators.
#
  plt.figure ( 3 )
  y = np.arange ( 0, it_num + 1 )
  for k in range ( 0, n ):
    plt.plot ( x_plot[:,k], y, linewidth = 1 )
  plt.grid ( True )
  plt.title ( 'Generator evolution.' )
  plt.xlabel ( 'Generator positions' )
  plt.ylabel ( 'Iterations' ) 
#
#  Save the plots.
#
  plt.figure ( 1 )
  filename = header + '_energy.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"', filename )
  plt.close ( 1 )

  plt.figure ( 2 )
  filename = header + '_motion.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"', filename )
  plt.close ( 2 )

  plt.figure ( 3 )
  filename = header + '_evolution.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"', filename )
  plt.close ( 3 )

  return x

def line_ccvt_lloyd_step ( n, a, b, x1 ):

#*****************************************************************************80
#
## line_ccvt_lloyd_step() takes one step of Lloyd's constrained CVT algorithm.
#
#  Discussion:
#
#    Each step of Lloyd's algorithm replaces a point by the center of mass
#    of the associated region.  For points on a line, with a uniform
#    density, the associated region is demarcated by the midways between 
#    successive points.
#
#    Here, we include the additional constraint that we want the first and last
#    points to be fixed at the endpoints of the line, that is, X(1) = A
#    and X(2) = B.  In that case, the calculation of the updates for the
#    first two and last two points must be handled differently.
#
#    For points away from the boundary, a step of Lloyd's method can be 
#    regarded as replacing each point by the average of the left and right
#    midways.  The midways, of course, are the average of two points.
#    So for point J, we have:
#
#      M(J-1,J) = ( X(J-1) + X(J) ) / 2
#      M(J,J+1) = ( X(J) + X(J+1) ) / 2
#      X*(J) = ( M(J-1,J) + M(J,J+1) ) / 2 = ( X(J-1) + 2 X(J) + X(J+1) ) / 4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    1 <= N.
#
#    real A, B, the left and right endpoints.
#
#    real X1(N), the current point locations.
#
#  Output:
#
#    real X2(N), the updated point locations.
#
  import numpy as np

  x2 = np.zeros ( n )

  if ( n == 1 ):

    x2[0] = ( a + b ) / 2.0;

  elif ( n == 2 ):

    x2 = np.array ( [ a, b ] )

  else:

    x2[0] = a
    for j in range ( 1, n - 1 ):
      x2[j] = ( 0.5 * ( x1[j-1] + x1[j] ) + 0.5 * ( x1[j] + x1[j+1] ) ) / 2.0
    x2[n-1] = b

  return x2

def line_cvt_energy ( n, a, b, x ):

#*****************************************************************************80
#
## line_cvt_energy() computes the CVT energy for a given set of generators.
#
#  Discussion:
#
#    Given a set of generators G over the line [A,B], then the energy
#    is defined as
#      E = integral ( a <= x <= b ) ( x - g(x) )^2 dx
#    where g(x) is the nearest generator to the point x.
#
#    For the 1D case, this integral can be evaluated exactly as the
#    sum of integrals over each subinterval:
#
#      E(i) = integral ( xl <= x <= xr ) ( x - x(i) )^2 dx
#           = ( ( x(i) - xl )^3 + ( xr - x(i) )^3 ) / 3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of generators.
#
#    real A, B, the left and right endpoints.
#
#    real X(N), the generator locations.
#
#  Output:
#
#    real E, the energy of the generator distribution.
#
  e = 0.0

  for j in range ( 0, n ):

    if ( j == 0 ):
      xl = a
    else:
      xl = ( x[j-1] + x[j] ) / 2.0

    if ( j == n - 1 ):
      xr = b
    else:
      xr = ( x[j] + x[j+1] ) / 2.0

    e = e + ( ( x[j] - xl )**3 + ( xr - x[j] )**3  ) / 3.0

  return e

def line_cvt_lloyd ( n, a, b, it_num, header, x ):

#*****************************************************************************80
#
## line_cvt_lloyd() carries out the Lloyd algorithm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of generators.
#
#    real A, B, the left and right endpoints.
#
#    integer IT_NUM, the number of iterations to take.
#
#    string HEADER, an identifying string.
#
#    real X(N), the initial point locations.
#
#  Output:
#
#    real X(N), the final point locations.
#
  import matplotlib.pyplot as plt
  import numpy as np
  import pprint

  eps = np.finfo(float).eps
#
#  Print the initial generators.
#
  print ( '' )
  print ( '  Initial generators:' )
  print ( '' )
  pprint.pprint ( x )
#
#  Initialize the plotting arrays.
#
  step = np.arange ( 0, it_num )
  e = np.nan * np.ones ( it_num )
  xm = np.nan * np.ones ( it_num )
  x_plot = np.zeros ( [ it_num + 1, n ] )

  for it in range ( 0, it_num ):

    x_plot[it,:] = x.copy()

    x_new = line_cvt_lloyd_step ( n, a, b, x )

    e[it] = line_cvt_energy ( n, a, b, x )
    e[it] = max ( e[it], eps )
#
#  Display the energy.
#
    plt.figure ( 1 )
    plt.plot ( step, np.log ( e ), 'm-*' )
    plt.title ( 'Log (Energy)' )
    plt.xlabel ( 'Step' )
    plt.ylabel ( 'Energy' )
    plt.grid ( True )
#
#  Compute the generator motion.
#
    xm[it] = np.sum ( ( x_new - x )**2 ) / n
#
#  Display the generator motion.
#
    plt.figure ( 2 )
    plt.plot ( step, np.log ( xm ), 'm-*' )
    plt.title ( 'Log (Average generator motion)' )
    plt.xlabel ( 'Step' )
    plt.ylabel ( 'Motion' )
    plt.grid ( True )
#
#  Update the generators.
#
    x = x_new.copy ( )
 
  x_plot[it_num,:] = x.copy ( )
#
#  Print the current generators.
#
  print ( '' )
  print ( '  Current generators:' )
  print ( '' )
  pprint.pprint ( x )
#
#  Plot the evolution of the locations of the generators.
#
  plt.figure ( 3 )
  y = np.arange ( 0, it_num + 1 )
  for k in range ( 0, n ):
    plt.plot ( x_plot[:,k], y )
  plt.grid ( True )
  plt.title ( 'Generator evolution.' )
  plt.xlabel ( 'Generator positions' )
  plt.ylabel ( 'Iterations' ) 
#
#  Save the plots.
#
  plt.figure ( 1 )
  filename = header + '_energy.png'
  print ( '-dpng', filename )
  print ( '  Graphics saved as "' + filename + '"', filename )
  plt.close ( 1 )

  plt.figure ( 2 )
  filename = header + '_motion.png'
  print ( '-dpng', filename )
  print ( '  Graphics saved as "' + filename + '"', filename )
  plt.close ( 2 )

  plt.figure ( 3 )
  filename = header + '_evolution.png'
  print ( '-dpng', filename )
  print ( '  Graphics saved as "' + filename + '"', filename )
  plt.close ( 3 )

  return x

def line_cvt_lloyd_step ( n, a, b, x1 ):

#*****************************************************************************80
#
## line_cvt_lloyd_step() takes one step of Lloyd's unconstrained CVT algorithm.
#
#  Discussion:
#
#    Each step of Lloyd's algorithm replaces a point by the center of mass
#    of the associated region.  For points on a line, with a uniform
#    density, the associated region is demarcated by the midways between 
#    successive points.
#
#    For points away from the boundary, a step of Lloyd's method can be 
#    regarded as replacing each point by the average of the left and right
#    midways.  The midways, of course, are the average of two points.
#    So for point J, we have:
#
#      M(J-1,J) = ( X(J-1) + X(J) ) / 2
#      M(J,J+1) = ( X(J) + X(J+1) ) / 2
#      X*(J) = ( M(J-1,J) + M(J,J+1) ) / 2 = ( X(J-1) + 2 X(J) + X(J+1) ) / 4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#    1 <= N.
#
#    real A, B, the left and right endpoints.
#
#    real X1(N), the current point locations.
#
#  Output:
#
#    real X2(N), the updated point locations.
#
  import numpy as np

  x2 = np.zeros ( n )

  if ( n == 1 ):

    x2[0] = ( a + b ) / 2.0

  else:

    j = 0
    x2[j] = (           a                 + 0.5 * ( x1[j] + x1[j+1] ) ) / 2.0

    for j in range ( 1, n - 1 ):
      x2[j] = ( 0.5 * ( x1[j-1] + x1[j] ) + 0.5 * ( x1[j] + x1[j+1] ) ) / 2.0
 
    j = n - 1
    x2[j] =   ( 0.5 * ( x1[j-1] + x1[j] ) +                       b   ) / 2.0

  return x2

def line_cvt_lloyd_test01 ( ):

#*****************************************************************************80
#
## line_cvt_lloyd_test01() tests the unconstrained computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  rng = default_rng ( )

  print ( '' )
  print ( 'line_cvt_lloyd_test01():' )
  print ( '  Test the unconstrained computation.' )

  n = 25
  a = 0.0
  b = 1.0
  it_num = 200
  x = a + ( b - a ) * rng.random ( n )
  header = 'test01'

  print ( '' )
  print ( '  Use', n, 'points in the interval [', a, ',', b, ']' )
  print ( '  Take', it_num, 'iterations.' )
  print ( '  Call this calculation "' + header + '"' )
  print ( '  Expect a uniform spacing of', ( b - a ) / ( n - 1 ) )

  x = line_cvt_lloyd ( n, a, b, it_num, header, x )

  return

def line_cvt_lloyd_test02 ( ):

#*****************************************************************************80
#
## line_cvt_lloyd_test02() tests the constrained computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  rng = default_rng ( )

  print ( '' )
  print ( 'line_cvt_lloyd_test02():' )
  print ( '  Test the constrained computation.' )

  n = 25
  a = 0.0
  b = 1.0
  it_num = 200
  x = a + ( b - a ) * rng.random ( n )
  header = 'test02'

  print ( '' )
  print ( '  Use', n, 'points in the interval [', a, ',', b, ']' )
  print ( '  Take', it_num, 'iterations.' )
  print ( '  Call this calculation "' + header + '"' )
  print ( '  Expect a uniform spacing of', ( b - a ) / n )

  x = line_ccvt_lloyd ( n, a, b, it_num, header, x )

  return

def line_cvt_lloyd_test03 ( ):

#*****************************************************************************80
#
## line_cvt_lloyd_test03() tests the unconstrained computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'line_cvt_lloyd_test03():' )
  print ( '  Test the unconstrained computation.' )
  print ( '  Sort the random initial values before use.' )

  n = 25
  a = 0.0
  b = 1.0
  it_num = 200
  x = a + ( b - a ) * rng.random ( n )
  x = np.sort ( x )
  header = 'test03'

  print ( '' )
  print ( '  Use', n, 'points in the interval [', a, ',', b, ']' )
  print ( '  Take', it_num, 'iterations.' )
  print ( '  Call this calculation "' + header + '"' )
  print ( '  Expect a uniform spacing of', ( b - a ) / ( n - 1 ) )

  x = line_cvt_lloyd ( n, a, b, it_num, header, x )

  return

def line_cvt_lloyd_test04 ( ):

#*****************************************************************************80
#
## line_cvt_lloyd_test04() tests the constrained computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 March 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'line_cvt_lloyd_test04():' )
  print ( '  Test the constrained computation.' )
  print ( '  Sort the initial points before use.' )

  n = 25
  a = 0.0
  b = 1.0
  it_num = 200
  x = a + ( b - a ) * rng.random ( n )
  x = np.sort ( x )
  header = 'test04'

  print ( '' )
  print ( '  Use', n, 'points in the interval [', a, ',', b, ']' )
  print ( '  Take', it_num, 'iterations.' )
  print ( '  Call this calculation "' + header + '"' )
  print ( '  Expect a uniform spacing of', ( b - a ) / n )

  x = line_ccvt_lloyd ( n, a, b, it_num, header, x )

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
  line_cvt_lloyd_test ( )
  timestamp ( )

