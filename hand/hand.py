#! /usr/bin/env python3
#
def hand_test ( ):

#*****************************************************************************80
#
## hand_test() tests hand().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hand_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hand().' )

  hand_dilation ( )
  hand_hull ( )
  hand_linear ( )
  hand_negation ( )
  hand_plot ( )
  hand_reflection ( )
  hand_rotation ( )
  hand_spline ( )
  hand_star ( )
  hand_translation ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hand_test():' )
  print ( '  Normal end of execution.' )

  return

def hand_dilation ( ):

#*****************************************************************************80
#
## hand_dilation() dilates the hand data and shows a plot.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'hand_dilation():' )
  print ( '  Dilate the hand data.' )
#
#  Read the data.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  Repeat the first row at the end so the polygon closes.
#
  xy = np.vstack ( ( xy, xy[0,:] ) )
#
#  Define the transformation as a diagonal dilation matrix A:
#
  A = np.array ( [ \
    [ 2.0, 0.0 ], \
    [ 0.0, 0.8 ] ] )
#
#  Tranform the data.
#
  xy2 = np.dot ( xy, A )
#
#  Clear the graphics frame.
#
  plt.clf ( )
#
#  Plot the original data.
#
  plt.plot ( xy[:,0], xy[:,1], 'r-', linewidth = 2 )
#
#  Plot the transformed data.
#
  plt.plot ( xy2[:,0], xy2[:,1], 'b-', linewidth = 2 )
#
#  Annotate.
#
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Hand data after dilation' )
  plt.legend ( [ 'Data', '2*x,0.8*y' ] )

  filename = 'hand_dilation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hand_hull ( ):

#*****************************************************************************80
#
## hand_hull() plots the hull of the hand data.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  from scipy.spatial import ConvexHull

  print ( '' )
  print ( 'hand_hull():' )
  print ( '  Compute and plot the convex hull of the hand data.' )
#
#  Read the data.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  Compute the convex hull.
#
  hull = ConvexHull ( xy )
#
#  Plot the data and the convex hull.
#
  plt.clf ( )
  plt.plot ( xy[:,0], xy[:,1], 'b.', markersize = 20 )
  plt.plot( xy[hull.vertices,0], xy[hull.vertices,1], 'r-', linewidth = 2 )
#
#  Don't forget the line segment from last point to first point!
#
  plt.plot ( 
    [ xy[hull.vertices[-1],0], xy[hull.vertices[0],0] ],
    [ xy[hull.vertices[-1],1], xy[hull.vertices[0],1] ], 'r--', lw = 2 )

  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- Y --->' )
  plt.title ( 'Convex hull of hand data' )

  filename = 'hand_hull.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hand_linear ( ):

#*****************************************************************************80
#
## hand_linear() applies a linear transformation xy2 = A * xy + b to hand data.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'hand_linear()' )
  print ( '  Apply a linear transformation to the hand data.' )
#
#  Read the data.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  Repeat the first row at the end so the polygon closes.
#
  xy = np.vstack ( ( xy, xy[0,:] ) )
#
#  Define the transformation as xy2 = A * x + b.
#
  A = np.array ( [ \
    [ -2.2, +1.0 ], \
    [  0.5,  0.4 ] ] )
#
#  Apply the transformation.
#
  xy2 = np.dot ( xy, A ) + np.array ( [ 1.5, -0.5 ] )
#
#  Clear the graphics frame.
#
  plt.clf ( )
#
#  Plot the original data.
#
  plt.plot ( xy[:,0], xy[:,1], 'r', linewidth = 2 )
#
#  Plot the transformed data.
#
  plt.plot ( xy2[:,0], xy2[:,1], 'b', linewidth = 2 )
#
#  Annotate.
#
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Hand data under linear transformation' )
  plt.legend ( [ 'Data (x)', 'Ax+b' ] )

  filename = 'hand_linear.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hand_negation ( ):

#*****************************************************************************80
#
## hand_negation() negates the hand data and shows the result.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'hand_negation():' )
  print ( '  Negate and plot the hand data.' )
#
#  Read the data.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  Repeat the first row at the end so the polygon closes.
#
  xy = np.vstack ( ( xy, xy[0,:] ) )
#
#  Define the transformation as a negation matrix.
#
  A = np.array ( [  \
    [ -1.0,  0.0 ], \
    [  0.0, -1.0 ] ] )
#
#  Transform the data.
#
  xy2 = np.dot ( xy, A )
#
#  Clear the graphics frame.
#
  plt.clf ( )
#
#  Plot the original data.
#
  plt.plot ( xy[:,0], xy[:,1], 'r', linewidth = 2 )
#
#  Plot the transformed data.
#
  plt.plot ( xy2[:,0], xy2[:,1], 'b', linewidth = 2 )
#
#  Annotate.
#
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Hand data after x and y coordinates negated.' )

  plt.legend ( [ 'Data x', '[-1,0;0,-1]*x' ] )

  filename = 'hand_negation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hand_plot ( ):

#*****************************************************************************80
#
## hand_plot() plots the hand data.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'hand_plot():' )
  print ( '  Read the hand data and plot it.' )
#
#  Read the data.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  Repeat the first row at the end so the polygon closes.
#
  xy = np.vstack ( ( xy, xy[0,:] ) )
#
#  Clear the graphics frame.
#
  plt.clf ( )
  plt.plot ( xy[:,0], xy[:,1], 'r', linewidth = 2 )
  plt.plot ( xy[:,0], xy[:,1], 'b.', markersize = 15 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Hand data and straight line interpolant' )

  filename = 'hand_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hand_reflection ( ):

#*****************************************************************************80
#
## hand_reflection() reflects the data and plots the result.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'hand_reflection():' )
  print ( '  Reflect the hand data.' )
#
#  Read the data.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  Repeat the first row at the end so the polygon closes.
#
  xy = np.vstack ( ( xy, xy[0,:] ) )
#
#  Define the transformations as xy2 = A2 * xy, xy3 = A3 * xy
#  where A2 reflects the x value, and A3 reflects the y value.
#
  A2 = np.array ( [ \
    [ -1.0, 0.0 ], \
    [  0.0, 1.0 ] ] )

  A3 = np.array ( [ \
    [  1.0,  0.0 ], \
    [  0.0, -1.0 ] ] )
#
#  Apply the transformations.
#  
  xy2 = np.dot ( xy, A2 )
  xy3 = np.dot ( xy, A3 )
#
#  Clear the graphics frame.
#
  plt.clf ( )
#
#  Plot the original data.
#
  plt.plot ( xy[:,0], xy[:,1], 'r', linewidth = 2 )
#
#  Plot the transformed data.
#
  plt.plot ( xy2[:,0], xy2[:,1], 'b', linewidth = 2 )
  plt.plot ( xy3[:,0], xy3[:,1], 'g', linewidth = 2 )
#
#  Annotate.
#
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Hand data with x or y reflected' )

  plt.legend ( [ 'Data', 'Reflect x', 'Reflect y' ] )

  filename = 'hand_reflection.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hand_rotation ( ):

#*****************************************************************************80
#
## hand_rotation() rotates the hand data and plots the result.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'hand_rotation():' )
  print ( '  Rotate the hand data.' )
#
#  Read the data.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  Repeat the first row at the end so the polygon closes.
#
  xy = np.vstack ( ( xy, xy[0,:] ) )
#
#  Define the transformation as a rotation, 
#    A = [ cos(a), - sin(a) 
#          sin(a),   cos(a) ]
#
  alpha = 30.0 * np.pi / 180
  sa = np.sin ( alpha )
  ca = np.cos ( alpha )

  A = np.array ( [
    [ ca, -sa ], \
    [ sa,  ca ] ] )
#
#  Apply the transformation.
#
  xy2 = np.dot ( xy, A )
  xy3 = np.dot ( xy2, A )
#
#  Clear the graphics frame.
#
  plt.clf ( )

  plt.plot ( xy[:,0], xy[:,1], 'r', linewidth = 2 )
#
#  Plot Axy and A^2xy.
#
  plt.plot ( xy2[:,0], xy2[:,1], 'b', linewidth = 2 )
  plt.plot ( xy3[:,0], xy3[:,1], 'g', linewidth = 2 )
#
#  Annotate.
#
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Hand data under rotation' )
  plt.legend ( [ 'Data', 'One rotation', 'Double rotation' ] )
  filename = 'hand_rotation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hand_spline ( ):

#*****************************************************************************80
#
## hand_spline() plots the hand data using splines.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
  from scipy.interpolate import CubicSpline
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'hand_spline()' )
  print ( '  Interpolate hand data with a spline.' )
#
#  Read the data.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  Repeat the first row at the end so the polygon closes.
#
  xy = np.vstack ( ( xy, xy[0,:] ) )

  m = xy.shape[0]
#
#  Consider the point index 0:M-1 as the independent variable for X and Y.
#
  s = np.arange ( m, dtype = float )
#
#  Compute splines U and V that treat X and Y as functions of the index.
#
  xspline = CubicSpline ( s, xy[:,0], bc_type = 'not-a-knot' )
  yspline = CubicSpline ( s, xy[:,1], bc_type = 'not-a-knot' )
#
#  Prepare to evaluate the spline function at a grid 20 times finer.
#
  t = np.linspace ( 0, m - 1, 20 * m )
#
#  Evaluate splines.
#
  xint = xspline ( t )
  yint = yspline ( t )
#
#  Display the parameterized spline U(T), V(T):
#
  plt.clf ( )

  plt.plot ( xint, yint, 'r', linewidth = 2 )
#
#  Include the data points.
#
  plt.plot ( xy[:,0], xy[:,1], 'b.', markersize = 15 )
#
#  Annotate.
#
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Spline interpolant to hand data' )
  plt.legend ( [ 'Spline interpolant', 'Data' ] )
  filename = 'hand_spline.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hand_star ( ):

#*****************************************************************************80
#
## hand_star() plots the hand data and shows it has a star structure.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'hand_star()' )
  print ( '  Show hand data is star-shaped.' )

  star = np.array ( [ 0.45, 0.23 ] )
#
#  Read the data.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  Reduce the amount of data to simplify the plot.
#  The correct syntax to get every other row of this array
#  is mind-numbingly idiotic.
#
  xy = xy[0::2,:]
  m = xy.shape[0]
#
#  Repeat the first row at the end so the polygon closes.
#
  xy = np.vstack ( ( xy, xy[0,:] ) )
#
#  Clear the graphics frame.
#
  plt.clf ( )
  plt.plot ( xy[:,0], xy[:,1], 'b.', markersize = 15 )
  plt.plot ( xy[:,0], xy[:,1], 'r', linewidth = 2 )
  plt.axis ( 'equal' )
  plt.grid ( 'True' )
  for i in range ( 0, m ):
    plt.plot ( [ star[0], xy[i,0] ], [ star[1], xy[i,1] ] )
    dx = xy[i,0] - star[0]
    dy = xy[i,1] - star[1]
    a = np.arctan2 ( dy, dx ) * 180 / np.pi
  plt.title ( 'hand data polygon is star shaped!' )
  filename = 'hand_star.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hand_translation ( ):

#*****************************************************************************80
#
## hand_translation() applies a translation xy2 = xy + b to hand data.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'hand_translation():' )
  print ( '  Translate the hand data.' )
#
#  Read the data.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  Repeat the first row at the end so the polygon closes.
#
  xy = np.vstack ( ( xy, xy[0,:] ) )
#
#  Define the transformation as xy2 = xy + b.
#
  b = np.array ( [ 1.0, -0.5 ] )
#
#  Transform the data.
#
  xy2 = xy + b
#
#  Clear the graphics frame.
#
  plt.clf ( )
#
#  Plot the original data.
#
  plt.plot ( xy[:,0], xy[:,1], 'r', linewidth = 2 )
#
#  Plot the transformed data.
#
  plt.plot ( xy2[:,0], xy2[:,1], 'b', linewidth = 2 )
#
#  Annotate.
#
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Hand data under translation' )

  plt.legend ( [ 'Hand data', 'Translated data' ] )

  filename = 'hand_translation.png'
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
  hand_test ( )
  timestamp ( )

