#! /usr/bin/env python3
#
def bird_egg_test ( ):

#*****************************************************************************80
#
## bird_egg_test() tests bird_egg().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'bird_egg_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test bird_egg(), code to evaluate the shape of bird eggs.' )

  chicken_egg_test ( )
  pyriform_egg_test ( )
  universal_egg_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'bird_egg_test():' )
  print ( '  Normal end of execution.' )
  return

def cheby1space ( a, b, n ):

#*****************************************************************************80
#
## cheby1space() creates a vector of Type 1 Chebyshev values in [A,B].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the first and last entries.
#
#    integer N, the number of entries in the vector.
#
#  Output:
#
#    real X(N), a vector of Type 1 Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( n - i - 1 ) * np.pi / float ( n - 1 )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

def chicken_egg ( B, L, w, x ):

#*****************************************************************************80
#
## chicken_egg() returns the outline of a chicken egg.
#
#  Discussion:
#
#    When L=B, the shape is a circle.
#
#    When w=0, the shape is an ellipse.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Valeriy Narushin, Michael Romanov, Darren Griffin,
#    "Egg and math: introducing a universal formula for egg shape",
#    Annals of the New York Academy of Sciences,
#    Number 1505, pages 169-177, 23 August 2021.
#
#  Input:
#
#    real B, the maximum breadth of the egg (y direction);
#
#    real L, the maximum length of the egg (x direction).
#
#    real w: the x-distance between the location of the maximum
#    breadth and the midpoint of the egg's length (x=0).
#
#    real x(*): sample points between -L/2 and +L/2.
#
#  Output:
#
#    real y(*): the height of the egg at each x value.
#    The egg is assumed to be vertically symmetric, and 
#    rotationally symmetric about the x axis.
#
  import numpy as np

  top = L**2 - 4.0 * x**2
  bot =  L**2 + 8.0 * w * x + 4.0 * w**2
  y = 0.5 * B * np.sqrt ( top / bot )

  return y

def chicken_egg_test ( ):

#*****************************************************************************80
#
## chicken_egg_test() tests chicken_egg().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chicken_egg_test():' )
  print ( '  chicken_egg() evaluates a formula' )
  print ( '  for chicken egg shapes.' )

  n = 21
  B = 1.0
  L = 1.5
  w = 0.25
  x = cheby1space ( -L/2.0, +L/2.0, n )
  y = chicken_egg ( B, L, w, x )

  egg_plot ( x, y, 'Chicken egg', 'chicken.png' )

  return

def egg_plot ( x, y, title, filename ):

#*****************************************************************************80
#
## egg_plot() draws the outline of an egg.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x(), y(): points along the upper side of the egg.
#
#    string title: a title for the plot.
#
#    string filename: the name of the file to be created.
#
  import matplotlib.pyplot as plt

  plt.clf ( )
  plt.plot ( x, y, 'r-', linewidth = 3 )
  plt.plot ( x, -y, 'g-', linewidth = 3 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( title )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def pyriform_egg ( B, L, w, x ):

#*****************************************************************************80
#
## pyriform_egg() returns the outline of a pyriform egg.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Valeriy Narushin, Michael Romanov, Darren Griffin,
#    "Egg and math: introducing a universal formula for egg shape",
#    Annals of the New York Academy of Sciences,
#    Number 1505, pages 169-177, 23 August 2021.
#
#  Input:
#
#    real B, the maximum breadth of the egg (y direction);
#
#    real L, the maximum length of the egg (x direction).
#
#    real w: the x-distance between the location of the maximum
#    breadth and the midpoint of the egg's length (x=0).
#
#    real x(*): sample points between -L/2 and +L/2.
#
#  Output:
#
#    real y(*): the height of the egg at each x value.
#    The egg is assumed to be vertically symmetric, and 
#    rotationally symmetric about the x axis.
#
  import numpy as np

  t1 = ( L**2 - 4.0 * x**2 ) * L
  t2 = 2.0 * ( L - 2.0 * w ) * x**2 \
    + ( L**2 + 8.0 * L * w - 4.0 * w**2 ) * x \
    + 2.0 * L * w**2 + L**2 * w + L**3
  y = 0.5 * B * np.sqrt ( t1 / t2 )

  return y

def pyriform_egg_test ( ):

#*****************************************************************************80
#
## pyriform_egg_test() tests pyriform_egg().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'pyriform_egg_test():' )
  print ( '  pyriform_egg() evaluates a formula' )
  print ( '  for pyriform egg shapes.' )

  n = 21
  B = 1.0
  L = 1.5
  w = 0.25
  x = cheby1space ( - L/2.0, +L/2.0, n )
  y = pyriform_egg ( B, L, w, x )

  egg_plot ( x, y, 'Pyriform egg', 'pyriform.png' )

  return

def universal_egg ( B, L, w, D, x ):

#*****************************************************************************80
#
## universal_egg() evaluates a universal formula for bird egg shapes.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 July 2022
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Valeriy Narushin, Michael Romanov, Darren Griffin,
#    "Egg and math: introducing a universal formula for egg shape",
#    Annals of the New York Academy of Sciences,
#    Number 1505, pages 169-177, 23 August 2021.
#
#  Input:
#
#    real B, the maximum breadth of the egg (y direction);
#
#    real L, the maximum length of the egg (x direction).
#
#    real w: the x-distance between the location of the maximum
#    breadth and the midpoint of the egg's length (x=0).
#
#    real D: the diameter of the egg at a quarter of the length
#    from the pointed end (x=0.25*L?).
#
#    real x(*): sample points between -L/2 and +L/2.
#
#  Output:
#
#    real y(*): the height of the egg at each x value.
#    The egg is assumed to be vertically symmetric, and 
#    rotationally symmetric about the x axis.
#
  import numpy as np

  y_chicken = chicken_egg ( B, L, w, x )

  s1 = np.sqrt ( 5.5 * L**2 + 11.0 * L * w + 4.0 * w**2 )
  s2 = np.sqrt ( 3.0 ) * B * L \
    - 2.0 * D * np.sqrt ( L**2 + 2.0 * w * L + 4.0 * w**2 )
  s3 = np.sqrt ( 5.5 * L**2 + 11.0 * L * w + 4.0 * w**2 )
  s4 = 2.0 * np.sqrt ( L**2 + 2.0 * w * L + 4.0 * w**2 )
  t2 = ( s1 * s2 ) / ( np.sqrt ( 3.0 ) * ( s3 - s4 ) )

  s5 = L * ( L**2 + 8.0 * w * x + 4.0 * w**2 )
  s6 = 2.0 * ( L - 2.0 * w ) * x**2 \
   + ( L**2 + 8.0 * L * w - 4.0 * w**2 ) * x \
    + 2.0 * L * w**2 + L**2 * w + L**3
  t3 = 1.0 - np.sqrt ( s5 / s6 )

  y = y_chicken * ( 1.0 - t2 * t3 )

  return y

def universal_egg_test ( ):

#*****************************************************************************80
#
## universal_egg_test() tests universal_egg().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 July 2022
#
#  Author:
#
#    Original Python version by Christian Hill.
#    Modifications by John Burkardt.
#
  import numpy as np
  import matplotlib.pyplot as plt
  import mpl_toolkits.mplot3d.axes3d as axes3d

  print ( '' )
  print ( 'universal_egg_test():' )
  print ( '  universal_egg() evaluates a universal formula for egg shape.' )
#
#  Ural owl
#
  B = 1.0
  L = 1.0
  w = 0.0
  D = L * np.sqrt ( 3.0 ) / 2.0
  x = cheby1space ( -L/2, L/2, 21 )
  y = universal_egg ( B, L, w, D, x )
  egg_plot ( x, y, 'Ural Owl egg', 'ural_owl.png' )
#
#  Hen
#
  B = 0.8
  L = 1.0
  w = 0.1
  D = 0.6
  x = cheby1space ( -L/2, L/2, 21 )
  y = universal_egg ( B, L, w, D, x )
  egg_plot ( x, y, 'Hen egg', 'hen.png' )
#
#  Guillemot (pyriform)
#
  B = 0.5
  L = 1.0
  w = 0.1
  D = 0.3
  x = cheby1space ( -L/2, L/2, 21 )
  y = universal_egg ( B, L, w, D, x )
  egg_plot ( x, y, 'Guillemot egg', 'guillemot.png' )
#
#  Ostrich
#
  B = 0.7
  L = 1.0
  w = 0.0
  D = 0.6
  x = cheby1space ( -L/2, L/2, 21 )
  y = universal_egg ( B, L, w, D, x )
  egg_plot ( x, y, 'Ostrich egg', 'ostrich.png' )
#
#  Render a 3D image of a guillemot egg.
#
  B = 0.5
  L = 1.0
  w = 0.1
  D = 0.3
  x = cheby1space ( -L/2, L/2, 201 )
  phi = np.linspace ( 0, 2*np.pi, 100 )
  X, Phi = np.meshgrid ( x, phi )
  Y = universal_egg ( B, L, w, D, X ) * np.cos ( Phi )
  Z = universal_egg ( B, L, w, D, X ) * np.sin ( Phi )

  fig = plt.figure()
  ax = fig.add_subplot ( projection = '3d' )
  ax.plot_surface ( X, Y, Z, alpha=0.3, color='r', rstride=10, cstride=10 )
  ax.plot_wireframe ( X, Y, Z, color='k', rstride=10, cstride=10, lw=1 )
  ax.set_xlim ( -L/2, L/2 )
  ax.set_ylim ( -L/2, L/2 )
  ax.set_zlim ( -L/2, L/2 )

  ax.axis ( 'off' )
  filename = 'guillemot_3d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' ) 
  plt.show ( block = False )
  plt.close ( )

  print ( '' )
  print ( 'universal_egg_test():' )
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
  bird_egg_test ( )
  timestamp ( )

