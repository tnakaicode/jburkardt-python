#! /usr/bin/env python3
#
def gray_scott_movie_test ( ):

#*****************************************************************************80
#
## gray_scott_movie_test() tests gray_scott_movie().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'gray_scott_movie_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  gray_scott_movie() solves the 2D Gray-Scott ' )
  print ( '  reaction-diffusion equation, and makes a movie.' )
#
#  Set the grid size.
#
  n = 200
#
#  Use the same grid size for x and y.
#
  nx = n
  ny = n
#
#  Assume the grid spacing is 1.
#
  dx = 1.0
  dy = 1.0
#
#  Set the diffusion coefficients for U and V.
#
  du = 0.3
  dv = 0.15
#
#  There are several interesting choices for the feed and kill rates.
#
#  Rings.
#
  if ( False ):
    f = 0.01
    k = 0.1
#
#  Splits.
#
  elif ( False ):
    f = 0.0367
    k = 0.0649
#
#  Coral.
#
  elif ( True ):
    f = 0.0545
    k = 0.0620
#
#  Bubbles.
#
  elif ( False ):
    f = 0.012
    k = 0.05
#
#  Waves.
#
  elif ( False ):
    f = 0.025
    k = 0.05
#
#  Set the time step.
#
  dt = 1.0
#
#  Choose the initial condition.
#
  if ( True ):
    initial_condition = 'wavefront'
  elif ( False ):
    initial_condition = 'bar'
  else:
    initial_condition = 'square'

  gray_scott_movie ( nx, ny, f, k, dx, dy, dt, du, dv, initial_condition )
#
#  Terminate.
#
  print ( '' )
  print ( 'gray_scott_movie_test():' )
  print ( '  Normal end of execution.' )

  return

def gray_scott_movie ( nx, ny, f, k, dx, dy, dt, du, dv, initial_condition ):

#*****************************************************************************80
#
## gray_scott_movie() generates Gray-Scott solutions and creates a movie.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer nx, ny: the number of columns and rows of data.
#
#    real f, k: the flow rate and the kill rate.
#
#    real dx, dy: the x and y spacing.
#
#    real dt: the time step.
#
#    real du, dv: the diffusion rates for u and v.
#
#    character initial_condition: a choice of one of three patterns:
#    'wavefront'
#    'bar'
#    'square'
#
  import matplotlib.pyplot as plt
  import numpy as np

  filename = 'gray_scott_movie_00000.png'
#
#  Compute the sequence of solutions.
#
  nt = 15001

  for it in range ( 0, nt ):
#
#  On first step, initialize the data.
#
    if ( it == 0 ):

      u = np.ones ( [ nx, ny ] )
      v = np.zeros ( [ nx, ny ] )

      xm = nx // 2 - 1
      ym = ny // 2 - 1

      if ( initial_condition == 'wavefront' ):
        u[xm-30:xm+31,ym-6:ym-3] = 0.75
        u[xm-30:xm+31,ym-3:ym  ] = 0.50
        u[xm-30:xm+31,ym  :ym+3] = 0.25
        u[xm-30:xm+31,ym+3:ym+6] = 0.00
        v[xm-30:xm+31,ym+3:ym+6] = 1.00
      elif ( initial_condition == 'bar' ): 
        u[xm-10:xm+11,ym-2:ym+3] = 0.0
        v[xm-10:xm+11,ym-2:ym+3] = 1.0
      else:
        u[xm-5:xm+6,ym-5:ym+6] = 0.0
        v[xm-5:xm+6,ym-5:ym+6] = 1.0
#
#  On subsequent steps, use the Euler method to update the data.
#
    else:

      uLaplace = laplacian9_torus ( u, dx, dy )
      vLaplace = laplacian9_torus ( v, dx, dy )

      dudt = du * uLaplace - u * v**2 + f * ( 1.0 - u )
      dvdt = dv * vLaplace + u * v**2 - ( f + k ) * v

      u = u + dt * dudt
      v = v + dt * dvdt
#
#  Display the data, and create a graphics frame, and add it to the movie.
#
    if ( ( it % 100 ) == 0 ):
      plt.imshow ( u )
      label = 'Gray-Scott U, step =' + str ( it )
      plt.title ( label )
      plt.axis ( 'equal' )
      plt.axis ( 'off' )
      plt.savefig ( filename )
      print ( '  Graphics saved as "' + filename + '"' )
      filename = filename_inc ( filename )

  return

def laplacian9_torus ( A, dx, dy ):

#*****************************************************************************80
#
## laplacian9_torus() uses a 9 point Laplacian stencil on a 2D torus.
#
#  Discussion:
#
#    1) Assumes the region is a rectangular torus
#    2) Assumes the mesh is uniform in both X and Y directions.
#    3) Assumes the spacing is dx in both directions.
#
#    Because of the periodic boundary conditions, the first and last rows
#    and columns are identified, that is, equivalent.  Therefore, when
#    computing indices im1, ip1, jm1, jp1, we have to skip over the last
#    row or column.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(NXP,NYP): function values, sampled on a regular 2D grid.
#
#    real DX, DY: the grid spacing in the X and Y directions.
#
#  Output:
#
#    real L(NXP,NYP): the values of the Laplacian, as estimated by the
#    9 point periodic stencil.
#
  import numpy as np

  nxp, nyp = A.shape
  L = np.zeros ( [ nxp, nyp ] )

  for j in range ( 0, nyp ):

    if ( j == nyp - 2 ):
      jp1 = 0
    elif ( j == nyp - 1 ):
      jp1 = 1
    else:
      jp1 = j + 1

    if ( j == 0 ):
      jm1 = nyp - 2
    else:
      jm1 = j - 1

    for i in range ( 0, nxp ):

      if ( i == nxp - 2 ):
        ip1 = 0
      elif ( i == nxp - 1 ):
        ip1 = 1
      else:
        ip1 = i + 1

      if ( i == 0 ):
        im1 = nxp - 2
      else:
        im1 = i - 1

      L[i,j] = \
        ( 1.0 * A[im1,jm1] +  4.0 * A[im1,j] + 1.0 * A[im1,jp1] \
        + 4.0 * A[i,  jm1] - 20.0 * A[i,j]   + 4.0 * A[i,  jp1] \
        + 1.0 * A[ip1,jm1] +  4.0 * A[ip1,j] + 1.0 * A[ip1,jp1] ) \
        / 6.0 / dx**2

  return L

def filename_inc ( filename ):

#*****************************************************************************80
#
## filename_inc() generates the next filename in a series.
#
#  Discussion:
#
#    It is assumed that the digits in the name, whether scattered or
#    connected, represent a number that is to be increased by 1 on
#    each call.  If this number is all 9's on input, the output number
#    is all 0's.  Non-numeric letters of the name are unaffected..
#
#    If the name is empty, then the routine stops.
#
#    If the name contains no digits, the empty string is returned.
#
#  Example:
#
#      Input            Output
#      -----            ------
#      'a7to11.txt'     'a7to12.txt'  (typical case.  Last digit incremented)
#      'a7to99.txt'     'a8to00.txt'  (last digit incremented, with carry.)
#      'a9to99.txt'     'a0to00.txt'  (wrap around)
#      'cat.txt'        ' '           (no digits in input name.)
#      ' '              STOP!         (error.)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the string to be incremented.
#
#  Output:
#
#    string FILENAME, the incremented string.
#
  i0 = ord ( '0' )
  i8 = ord ( '8' )
  i9 = ord ( '9' )

  lens = len ( filename )

  if ( lens <= 0 ):
    return None

  change = 0
  filename2 = ''

  for i in range ( lens - 1, -1, -1 ):

    c = filename[i]

    ic = ord ( c )

    if ( change < 2 and i0 <= ic and ic <= i8 ):
      ic = ic + 1
      filename2 = chr ( ic ) + filename2
      change = 2
    elif ( change == 0 and ic == i9 ):
      change = 1
      c = '0'
      filename2 = c + filename2
    else:
      filename2 = c + filename2

  if ( change == 0 ):
    filename2 = None

  return filename2

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
  gray_scott_movie_test ( )
  timestamp ( )


