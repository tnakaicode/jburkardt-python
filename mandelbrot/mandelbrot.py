#! /usr/bin/env python3
#
def mandelbrot_image ( xmin, xmax, ymin, ymax, xnum, ynum, countmax ):

#*****************************************************************************80
#
## MANDELBROT_IMAGE creates an image of the Mandelbrot set.
#
#  Discussion:
#
#    Over the rectangle [XMIN,XMAX] x [YMIN,YMAX], determine the Mandelbrot
#    count for a grid of XNUMxYNUM points, using a particular value of
#    COUNTMAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real XMIN, XMAX, YMIN, YMAX, the physical limits of the rectangle.
#
#    Input, integer XNUM, YNUM, the number of points in X and Y directions.
#
#    Input, integer COUNTMAX, the maximum number of iterations.
#
  import matplotlib.cm as cm
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
  import time

  print ( '' )
  print ( 'MANDELBROT_IMAGE:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Compute the Mandelbrot set and display it.' )

  print ( '' )
  print ( '  X range: [ %g, %g ]' % ( xmin, xmax ) )
  print ( '  Y range: [ %g, %g ]' % ( ymin, ymax ) )
  print ( '  Xnum = %d x Ynum = %d = %d Pixels' % ( xnum, ynum, xnum * ynum ) )
  print ( '  Maximum number of iterations = %d' % ( countmax ) )

  time1 = time.time ( )
  clock1 = time.clock ( )

  dpi = 72
  width_inches = int ( xnum / dpi )
  height_inches = int ( ynum / dpi )

  x, y, count = mandelbrot_set ( xmin, xmax, ymin, ymax, xnum, ynum, countmax )

  clock2 = time.clock ( )
  time2 = time.time ( )

  print ( '' )
  print ( '  Compute time:' )
  print ( '  Wallclock: %.02f sec.' % ( time2 - time1 ) )
  print ( '        CPU: %.02f sec.' % ( clock2 - clock1 ) )

  X, Y = np.meshgrid ( x, y, indexing = 'ij' )
  fig, ax = plt.subplots ( figsize = ( width_inches, height_inches ), dpi = 72 )
  cs = ax.contourf ( X, Y, count, cmap = cm.prism )

  filename = 'mandelbrot.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Plot saved in file "%s"' % ( filename ) )

  plt.show ( block = False )
#
#  Terminate.
#
  print ( '' )
  print ( 'MANDELBROT_IMAGE:' )
  print ( '  Normal end of execution.' )

  return

def mandelbrot_set ( xmin, xmax, ymin, ymax, xnum, ynum, countmax ):

#*****************************************************************************80
#
## MANDELBROT_SET computes the Mandelbrot count for a grid of points.
#
#  Discussion:
#
#    Over the rectangle [XMIN,XMAX] x [YMIN,YMAX], determine the Mandelbrot
#    count for a grid of XNUMxYNUM points, using a particular value of
#    COUNTMAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real XMIN, XMAX, YMIN, YMAX, the physical limits of the rectangle.
#
#    Input, integer XNUM, YNUM, the number of points in X and Y directions.
#
#    Input, integer COUNTMAX, the maximum number of iterations.
#
#    Output, real X(XNUM), Y(YNUM), COUNT(XNUM,YNUM), the X and Y
#    grid locations, and the count for each point in the grid.
#
  import numpy as np

  x = np.linspace ( xmin, xmax, xnum )
  y = np.linspace ( ymin, ymax, ynum )

  count = np.empty ( ( xnum, ynum ) )
  for i in range ( xnum ):
    for j in range ( ynum ):
      count[i,j] = mandelbrot_count ( x[i] + 1j * y[j], countmax )

  return ( x, y, count )

def mandelbrot_count ( c, countmax ):

#*****************************************************************************80
#
## MANDELBROT_COUNT returns the Mandelbrot count for a single point.
#
#  Discussion:
#
#    Starting with the value 0, repeatedly square and add complex value C.
#
#    Return number of applications of this process at which the
#    value exceeds 2 in norm.
#
#    Repeat no more than COUNTMAX times.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    10 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, complex C, the value added at each step.
#
#    Input, integer COUNTMAX, the maximum number of iterations.
#
#    Output, integer MANDEL_COUNT, the number of operations at which
#    the iterate first exceeded 2 in norm.  If this never happens,
#    return COUNTMAX.
#
  z = 0.0 + 0.0 * 1j
  for i in range ( countmax ):
    if ( 2.0 <= abs ( z ) ):
      return i
    z = z * z + c

  return countmax

if ( __name__ == '__main__' ):

  mandelbrot_image ( -2.0, 0.5, -1.25, 1.25, 720, 720, 200 )

