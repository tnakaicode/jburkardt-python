#! /usr/bin/env python3
#
def annulus_grid_count ( n, r1, r2, c ):

#*****************************************************************************80
#
## annulus_grid_count() counts the grid points inside an annulus.
#
#  Discussion:
#
#    The grid is defined by specifying the center of the annulus,
#    the inner and outer radius, and the number of subintervals N 
#    into which the horizontal radius should be divided.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of subintervals.
#
#    real R1, R2, the inner and outer radius of the annulus.
#
#    real C(2), the coordinates of the center of the annulus.
#
#  Output:
#
#    integer NG, the number of grid points inside the annulus.
#
  ng = 0

  for j in range ( 0, n + 1 ):

    i = 0
    x = c[0]
    y = c[1] + r2 * 2 * j / ( 2 * n + 1 )

    if ( r1 * r1 <= ( x - c[0] )**2 + ( y - c[1] )**2 ):
      if ( r1 == 0.0 and j == 0 ):
        ng = ng + 1
      else:
        ng = ng + 2

    while ( True ):

      i = i + 1
      x = c[0] + r2 * 2 * i / ( 2 * n + 1 )
      if ( r1 * r1 <= ( x - c[0] )**2 + ( y - c[1] )**2 ):
        if ( r2 * r2 < ( x - c[0] )**2 + ( y - c[1] )**2 ):
          break
        ng = ng + 1
        ng = ng + 1
        if ( 0 < j ):
          ng = ng + 1
          ng = ng + 1

  return ng

def annulus_grid_display ( ng, xy ):

#*****************************************************************************80
#
## annulus_grid_display() displays grid points inside a annulus.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NG, the number of grid points inside the annulus.
#
#    real XY(NG,2), the grid points.
#
  import matplotlib.pyplot as plt

  plt.plot ( xy[:,0], xy[:,1], 'b.', markersize = 5 )
  plt.axis ( 'equal' )
  label = str ( ng ) + ' grid points inside a annulus'
  plt.title ( label )
  plt.grid ( True )

  return

def annulus_grid_fibonacci ( n, r1, r2, c ):

#*****************************************************************************80
#
## annulus_grid_fibonacci() computes Fibonacci grid points inside a annulus.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Swinbank, James Purser,
#    Fibonacci grids: A novel approach to global modelling,
#    Quarterly Journal of the Royal Meteorological Society,
#    Volume 132, Number 619, July 2006 Part B, pages 1769-1793.
#
#  Input:
#
#    integer N, the number of points desired.
#
#    real R1, R2, the inner and outer radius of the annulus.
#
#    real C(2), the coordinates of the center of the annulus.
#
#  Output:
#
#    real G(N,2), the grid points.
#
  import numpy as np

  phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0

  m = 0.5 + ( n - 0.5 ) * r1**2 / ( r2**2 - r1**2 )
  i = np.linspace ( m + 1, m + n, n )

  gr = r2 * np.sqrt ( i - 0.5 ) / np.sqrt ( m + n - 0.5 )
  gt = 2.0 * np.pi * i / phi

  g = np.zeros ( [ n, 2 ] )

  g[:,0] = c[0] + gr * np.cos ( gt )
  g[:,1] = c[1] + gr * np.sin ( gt )

  return g

def annulus_grid ( n, r1, r2, c, ng ):

#*****************************************************************************80
#
## annulus_grid() computes grid points inside an annulus.
#
#  Discussion:
#
#    The grid is defined by specifying the center of the annulus,
#    the inner and outer radius, and the number of subintervals N 
#    into which the horizontal radial segment should be divided.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of subintervals.
#
#    real R1, R2, the inner and outer radius of the annulus.
#
#    real C(2), the coordinates of the center of the annulus.
#
#    integer NG, the number of grid points, as determined by annulus_grid_count.
#
#  Output:
#
#    real CG(NG,2), the grid points inside the disk.
#
  import numpy as np

  cg = np.zeros ( [ ng, 2 ] )

  p = 0

  for j in range ( 0, n + 1 ):
    i = 0
    x = c[0]
    y = c[1] + r2 * 2 * j / ( 2 * n + 1 )
    if ( r1 * r1 <= ( x - c[0] )**2 + ( y - c[1] )**2 ):

      cg[p,0] = x
      cg[p,1] = y
      p = p + 1
      if ( 0.0 < r1 or 0 < j ):
        cg[p,0] = x
        cg[p,1] = 2 * c[1] - y
        p = p + 1

    while ( True ):

      i = i + 1
      x = c[0] + r2 * 2 * i / ( 2 * n + 1 )

      if ( r1 * r1 <= ( x - c[0] )**2 + ( y - c[1] )**2 ):
        if ( r2 * r2 < ( x - c[0] )**2 + ( y - c[1] )**2 ):
          break
        cg[p,0] = x
        cg[p,1] = y
        p = p + 1
        cg[p,0] = 2 * c[0] - x
        cg[p,1] = y
        p = p + 1
        if ( 0 < j ):
          cg[p,0] = x
          cg[p,1] = 2 * c[1] - y
          p = p + 1
          cg[p,0] = 2 * c[0] - x
          cg[p,1] = 2 * c[1] - y
          p = p + 1

  return cg

def annulus_grid_test01 ( ):

#*****************************************************************************80
#
## annulus_grid_test01() tests annulus_grid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'annulus_grid_test01():' )
  print ( '  annulus_grid() defines a grid of points' )
  print ( '  with N+1 points on a horizontal or vertical radius,' )
  print ( '  based on any annulus.' )

  n = 20
  r1 = 1.0
  r2 = 2.0
  c = np.array ( [ 1.0, 5.0 ] )

  print ( '' )
  print ( '  We use N =', n )
  print ( '  Inner radius R1 =', r1 )
  print ( '  Outer radius R2 =', r2 )
  print ( '  Center C = (', c[0], ', ',  c[1] )

  ng = annulus_grid_count ( n, r1, r2, c )

  print ( '' )
  print ( '  Number of grid points will be', ng )

  cg = annulus_grid ( n, r1, r2, c, ng )

  print ( '' )
  print ( '  First 20 points:' )
  print ( cg[0:20,:] )

  filename = 'annulus_grid_test01.xy'
  np.savetxt ( filename, cg )

  print ( '' )
  print ( '  Data written to the file "' + filename + '".' )
#
# Plot the points.
#
  t = 2.0 * np.pi * np.linspace ( 0.0, 1.0, 51 )

  cx1 = c[0] + r1 * np.cos ( t )
  cy1 = c[1] + r1 * np.sin ( t )

  cx2 = c[0] + r2 * np.cos ( t )
  cy2 = c[1] + r2 * np.sin ( t )

  plt.clf ( )
  plt.plot ( cx1, cy1, 'r-', linewidth = 3 )
  plt.plot ( cx2, cy2, 'r-', linewidth = 3 )
  plt.plot ( cg[:,0], cg[:,1], 'b.' )
  plt.axis ( 'equal' )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Circle grid with ' + str ( ng ) + ' points' )
  filename = 'annulus_grid_test01.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def annulus_grid_test02 ( ):

#*****************************************************************************80
#
## annulus_grid_test02() tests annulus_grid_fibonacci().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 November 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'annulus_grid_test02():' )
  print ( '  annulus_grid_fibonacci() defines a grid of N points' )
  print ( '  ' )

  n = 1000
  r1 = 1.0
  r2 = 2.0
  c = np.array ( [ 1.0, 5.0 ] )

  print ( '' )
  print ( '  We use N =', n )
  print ( '  Inner radius R1 =', r1 )
  print ( '  Outer radius R2 =', r2 )
  print ( '  Center C = (', c[0],' ,', c[1], ')' )

  g = annulus_grid_fibonacci ( n, r1, r2, c )

  print ( '' )
  print ( '  First 20 points in grid:' )
  print ( g[0:20,:] )

  filename = 'annulus_grid_test02.xy'

  np.savetxt ( filename, g )
  print ( '  Gridpoint coordinates saved as "' + filename + '".' )
#
#  Plot the points.
#
  t = 2.0 * np.pi * np.linspace ( 0.0, 1.0, 51 )
 
  cx1 = c[0] + r1 * np.cos ( t )
  cy1 = c[1] + r1 * np.sin ( t )

  cx2 = c[0] + r2 * np.cos ( t )
  cy2 = c[1] + r2 * np.sin ( t )

  plt.clf ( )
  plt.plot ( cx1, cy1, 'r-', linewidth = 3 )
  plt.plot ( cx2, cy2, 'r-', linewidth = 3 )
  plt.plot ( g[:,0], g[:,1], 'b.' )
  plt.axis ( 'equal' )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  s = 'Fibonacci grid with ' + str ( n ) + ' points'
  plt.title ( s )
  filename = 'annulus_grid_test02.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def annulus_grid_test ( ):

#*****************************************************************************80
#
## annulus_grid_test() tests annulus_grid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'annulus_grid_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test annulus_grid().' )

  annulus_grid_test01 ( )
  annulus_grid_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'annulus_grid_test():' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  annulus_grid_test ( )
  timestamp ( )

