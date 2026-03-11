#! /usr/bin/env python3
#
def mandelbrot_area_test ( ):

#*****************************************************************************80
#
## mandelbrot_area_test() tests mandelbrot_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 December 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'mandelbrot_area_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test mandelbrot_area().' )

  n = 200
  it_max = 100
  mandelbrot_area ( n, it_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'mandelbrot_area_test()' )
  print ( '  Normal end of execution.' )

  return

def mandelbrot_area ( n, it_max ):

#*****************************************************************************80
#
## mandelbrot_area() estimates the area of the Mandelbrot set.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    11 December 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Mandelbrot area and escape times.
#    https://www.johndcook.com/blog/2025/09/08/mandelbrot-area-and-escape-times/
#    Posted: 08 September 2025
#
#  Input:
#
#    integer N: the program will check N^2 points.
#
#    integer IT_MAX: the maximum number of iterations.
#
  import matplotlib
  import matplotlib.cm as cm
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Define the range.
#
  x_min = -2.00
  x_max =  2.00
  y_min = -2.00
  y_max =  2.00

  print ( '' )
  print ( 'mandelbrot_area():' )
  print ( '  Estimate the area of the Mandelbrot set.' )
  print ( '' )
  print ( '  For ', n, '^2 random values C = X + i*Y' )
  print ( '  in the complex circle of radius 2,')
  print ( '  carry out up to ', it_max, ' iterations of the map' )
  print ( '  Z(n+1) = Z(n)^2 + C.' )
  print ( '  If the iterates stay in the circle of radius 2,' )
  print ( '  then C is a member of the Mandelbrot set.' )
  print ( '' )
#
#  Create an array of complex sample points in [x_min,x_max] + [y_min,y_max]*i.
#
  xmin = -2.0
  xmax = 1.0
  ymin = -1.5
  ymax = 1.5
  x = np.linspace ( -2.0, +1.0, n )
  y = np.linspace ( -1.5, +1.5, n )
  X, Y = np.meshgrid ( x, y )
  C = X + Y * 1j
#
#  Carry out the iteration.
#  d(i,j) is the last iteration in which the image of the (i,j) point 
#  did not exceed 2 in norm.
#
  D = - np.ones ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      value = 0.0
      for k in range ( 0, it_max + 1 ):
        if ( 2.0 <= np.linalg.norm ( value ) ):
          D[i,j] = k
          break
        value = value * value + X[i,j] + Y[i,j] * 1j

  print ( '' )
  for k in range ( 0, it_max + 1 ):
    print ( '  Iteration ', k, '  Points escaping =',  sum ( sum ( D == k ) ) )
  
  Dinside = sum ( sum ( D == -1 ) )
  print ( '  Points still inside = ', Dinside, ' out of ', n**2 )

  print ( '')
  print ( '  Estimated area = ', \
    ( xmax - xmin ) * ( ymax - ymin ) * Dinside / n / n )
  print ( '  Cook estimate was 1.5129' )
#
#  Display the data.
#
  plt.clf ( )
  plt.contourf ( X, Y, D, cmap = cm.prism )
  plt.colorbar ( )

  filename = 'mandelbrot_area.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

# t = delaunay ( Zr, Zi )
#
#  Set a nonsmooth color map.
#  colorcube, flag, lines, prism.
#
# colormap ( 'prism')
#
#  Make a color contour plot.
#
# h = trisurf ( t, Zr, Zi, d, 'FaceColor', 'interp', 'EdgeColor', 'interp' )

# view ( 2 )
# axis ( 'equal' )
# axis ( 'tight' )
# xtitle = sprintf ( '#g <---X---> #g', x_min, x_max )
# xlabel ( xtitle )
# ytitle = sprintf ( '#g <---Y---> #g', y_min, y_max )
# ylabel ( ytitle )
# title_string = sprintf ( 'Mandelbrot set, #d x #d pixels, #d iterations', ...
#   n, n, it_max )
# title ( title_string )
# set ( gca, 'xticklabel', [] )
# set ( gca, 'yticklabel', [] )
# filename = 'mandelbrot_area.png'
# print ( '-dpng', filename )
# print ( '  Graphics saved as "#s"', filename )

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
  mandelbrot_area_test ( )
  timestamp ( )

