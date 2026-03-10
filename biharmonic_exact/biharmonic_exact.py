#! /usr/bin/env python3
#
def biharmonic_exact_test ( ):

#*****************************************************************************80
#
## biharmonic_exact_test() tests biharmonic_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib
  import numpy as np
  import platform
  import scipy

  print ( '' )
  print ( 'biharmonic_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  scipy version:  ' + scipy.__version__ )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test biharmonic_exact().' )

  rng = default_rng ( )

  n = 5
  X = rng.random ( size = n )
  Y = rng.random ( size = n )
  a = 1.0
  b = 2.0
  c = 3.0
  d = 4.0
  e = 5.0
  f = 6.0
  g = 7.0
#
#  Exact function 1.
#
  print ( '' )
  print ( '  Exact solution 1 residual at random points:' )

  R = biharmonic_exact_r1 ( X, Y, a, b, c, d, e, f, g )

  print ( R )
#
#  Exact function 2.
#
  print ( '' )
  print ( '  Exact solution 2 residual at random points:' )

  R = biharmonic_exact_r2 ( X, Y, a, b, c, d, e, f, g )

  print ( R )
#
#  Exact function 3.
#
  print ( '' )
  print ( '  Exact solution 3 residual at random points:' )

  R = biharmonic_exact_r3 ( X, Y, a, b, c, d, e, f )

  print ( R )
#
#  Flow for exact function 1.
#
  print ( '' )
  print ( '  Exact solution 1 flow on grid:' )

  x = np.linspace ( 0.5, +1.25, 21 )
  y = np.linspace ( 0.5, +1.25, 21 )
  X, Y = np.meshgrid ( x, y )
  U, V = biharmonic_exact_uv1 ( X, Y, a, b, c, d, e, f, g )
  filename = 'biharmonic_exact_uv1.png'
  flow_display ( X, Y, U, V, filename )
#
#  Flow for exact function 2.
#
  print ( '' )
  print ( '  Exact solution 2 flow on grid:' )

  x = np.linspace ( 0.5, +1.25, 21 )
  y = np.linspace ( 0.5, +1.25, 21 )
  X, Y = np.meshgrid ( x, y )
  U, V = biharmonic_exact_uv2 ( X, Y, a, b, c, d, e, f, g )
  filename = 'biharmonic_exact_uv2.png'
  flow_display ( X, Y, U, V, filename )
#
#  Flow for exact function 3.
#
  print ( '' )
  print ( '  Exact solution 3 flow on grid:' )

  x = np.linspace ( 4.5, +5.5, 21 )
  y = np.linspace ( 5.5, +6.5, 21 )
  X, Y = np.meshgrid ( x, y )
  U, V = biharmonic_exact_uv3 ( X, Y, a, b, c, d, e, f )
  filename = 'biharmonic_exact_uv3.png'
  flow_display ( X, Y, U, V, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'biharmonic_exact_test()' )
  print ( '  Normal end of execution.' )

  return

def biharmonic_exact_r1 ( X, Y, a, b, c, d, e, f, g ):

#*****************************************************************************80
#
## biharmonic_exact_r1() evaluates exact biharmonic residual for W(X,Y) #1.
#
#  Discussion:
#
#   Note the formula for W:
#
#   W = ( a     * np.cosh ( g * X ) \
#       + b     * np.sinh ( g * X ) \
#       + c * X * np.cosh ( g * X ) \
#       + d * X * np.sinh ( g * X ) ) \ 
#       * \
#       ( e * np.cos ( g * Y ) \
#       + f * np.sin ( g * Y ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c, d, e, f, g: parameters.
#
#  Output:
#
#    real R: the residual evaluated at the points (X,Y).
#
  import numpy as np

  Wxxxx =  \
    g**3 * ( e * np.cos ( g * Y ) + f * np.sin ( g * Y ) ) \
    * \
    (     a * g     * np.cosh ( g * X ) \
    +     b * g     * np.sinh ( g * X ) \
    +     c * g * X * np.cosh ( g * X ) \
    + 4 * c         * np.sinh ( g * X ) \
    +     d * g * X * np.sinh ( g * X ) \
    + 4 * d         * np.cosh ( g * X ) )

  Wxxyy = \
    -g**3 * ( e * np.cos ( g * Y ) + f * np.sin ( g * Y ) ) \
    * \
    (     a * g     * np.cosh ( g * X ) \
    +     b * g     * np.sinh ( g * X ) \
    +     c * g * X * np.cosh ( g * X ) \
    + 2 * c         * np.sinh ( g * X ) \
    +     d * g * X * np.sinh ( g * X ) \
    + 2 * d         * np.cosh ( g * X ) )

  Wyyyy = \
    g**4 * ( e * np.cos ( g * Y ) + f * np.sin ( g * Y ) ) \
    * \
    ( a     * np.cosh ( g * X ) \
    + b     * np.sinh ( g * X ) \
    + c * X * np.cosh ( g * X ) \
    + d * X * np.sinh ( g * X ) )

  R = Wxxxx + 2.0 * Wxxyy + Wyyyy

  return R

def biharmonic_exact_r2 ( X, Y, a, b, c, d, e, f, g ):

#*****************************************************************************80
#
## biharmonic_exact_r2() evaluates exact biharmonic residual for W(X,Y) #2.
#
#  Discussion:
#
#   Note the formula for W:
#
#  W = ( a     * np.cos ( g * X ) \
#      + b     * np.sin ( g * X ) \
#      + c * X * np.cos ( g * X ) \
#      + d * X * np.sin ( g * X ) ) \ 
#      *
#      ( e * np.cosh ( g * Y ) \
#      + f * np.sinh ( g * Y ) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c, d, e, f, g: parameters.
#
#  Output:
#
#    real R: the residual evaluated at the points (X,Y).
#
  import numpy as np

  Wxxxx =  g**3 * ( e * np.cosh ( g * Y ) + f * np.sinh ( g * Y ) ) \
    * \
    (     a * g     * np.cos ( g * X ) \
    +     b * g     * np.sin ( g * X ) \
    +     c * g * X * np.cos ( g * X ) \
    + 4 * c         * np.sin ( g * X ) \
    +     d * g * X * np.sin ( g * X ) \
    - 4 * d         * np.cos ( g * X ) )

  Wxxyy =  - g**3 * ( e * np.cosh ( g * Y ) + f * np.sinh ( g * Y ) ) \
    * \
    (     a * g     * np.cos ( g * X ) \
    +     b * g     * np.sin ( g * X ) \
    +     c * g * X * np.cos ( g * X ) \
    + 2 * c         * np.sin ( g * X ) \
    +     d * g * X * np.sin ( g * X ) \
    - 2 * d         * np.cos ( g * X ) )

  Wyyyy =  g**4 * ( e * np.cosh ( g * Y ) + f * np.sinh ( g * Y ) ) \
    * \
    ( a     * np.cos ( g * X ) \
    + b     * np.sin ( g * X ) \
    + c * X * np.cos ( g * X ) \
    + d * X * np.sin ( g * X ) )

  R = Wxxxx + 2.0 * Wxxyy + Wyyyy

  return R

def biharmonic_exact_r3 ( X, Y, a, b, c, d, e, f ):

#*****************************************************************************80
#
## biharmonic_exact_r3() evaluates exact biharmonic residual for W(X,Y) #3.
#
#  Discussion:
#
#   Note the formula for W:
#
#   R = sqrt ( ( X - e )**2 + ( Y - f )**2 )
#
#   W =   a     * R**2 * log ( R ) \
#       + b     * R**2 \
#       + c * log ( R ) \
#       + d
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c, d, e, f: parameters.
#
#  Output:
#
#    real R: the residual evaluated at the points (X,Y).
#
  import numpy as np

  Wxxxx =  2 * ( 8 * a * ( e - X )**4 \
    / ( ( e - X )**2 + ( f - Y )**2 )**2 - 12 * a * ( e - X )**2 \
    / ( ( e - X )**2 + ( f - Y )**2 ) + 3 * a - 24 * c * ( e - X )**4 \
    / ( ( e - X )**2 + ( f - Y )**2 )**3 + 24 * c * ( e - X )**2 \
    / ( ( e - X )**2 + ( f - Y )**2 )**2 - 3 * c \
    / ( ( e - X )**2 + ( f - Y )**2 ) ) \
    / ( ( e - X )**2 + ( f - Y )**2 )

  Wxxyy =  2 * ( 8 * a * ( e - X )**2 * ( f - Y )**2 \
    / ( ( e - X )**2 + ( f - Y )**2 )**2 - 2 * a * ( e - X )**2 \
    / ( ( e - X )**2 + ( f - Y )**2 ) - 2 * a * ( f - Y )**2 \
    / ( ( e - X )**2 + ( f - Y )**2 ) + a - 24 * c * ( e - X )**2 * ( f - Y )**2 \
    / ( ( e - X )**2 + ( f - Y )**2 )**3 + 4 * c * ( e - X )**2 \
    / ( ( e - X )**2 + ( f - Y )**2 )**2 + 4 * c * ( f - Y )**2 \
    / ( ( e - X )**2 + ( f - Y )**2 )**2 - c \
    / ( ( e - X )**2 + ( f - Y )**2 ) ) \
    / ( ( e - X )**2 + ( f - Y )**2 )

  Wyyyy =  2 * ( 8 * a * ( f - Y )**4 \
    / ( ( e - X )**2 + ( f - Y )**2 )**2 - 12 * a * ( f - Y )**2 \
    / ( ( e - X )**2 + ( f - Y )**2 ) + 3 * a - 24 * c * ( f - Y )**4 \
    / ( ( e - X )**2 + ( f - Y )**2 )**3 + 24 * c * ( f - Y )**2 \
    / ( ( e - X )**2 + ( f - Y )**2 )**2 - 3 * c \
    / ( ( e - X )**2 + ( f - Y )**2 ) ) \
    / ( ( e - X )**2 + ( f - Y )**2 )

  R = Wxxxx + 2.0 * Wxxyy + Wyyyy

  return R

def biharmonic_exact_w1 ( X, Y, a, b, c, d, e, f, g ):

#*****************************************************************************80
#
## biharmonic_exact_w1() evaluates exact biharmonic solution W(X,Y) #1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c, d, e, f, g: parameters.
#
#  Output:
#
#    real W: the solution evaluated at the points (X,Y).
#
  import numpy as np

  W = ( a     * np.cosh ( g * X ) \
      + b     * np.sinh ( g * X ) \
      + c * X * np.cosh ( g * X ) \
      + d * X * np.sinh ( g * X ) ) \
      * \
      ( e * np.cos ( g * Y ) \
      + f * np.sin ( g * Y ) )

  return W

def biharmonic_exact_w2 ( X, Y, a, b, c, d, e, f, g ):

#*****************************************************************************80
#
## biharmonic_exact_w2() evaluates exact biharmonic solution W(X,Y) #2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c, d, e, f, g: parameters.
#
#  Output:
#
#    real W: the solution evaluated at the points (X,Y).
#
  import numpy as np

  W = ( a     * np.cos ( g * X ) \
      + b     * np.sin ( g * X ) \
      + c * X * np.cos ( g * X ) \
      + d * X * np.sin ( g * X ) ) \
      * \
      ( e * np.cosh ( g * Y ) \
      + f * np.sinh ( g * Y ) )

  return W

def biharmonic_exact_w3 ( X, Y, a, b, c, d, e, f ):

#*****************************************************************************80
#
## biharmonic_exact_w3() evaluates exact biharmonic solution W(X,Y) #3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c, d, e, f: parameters.
#
#  Output:
#
#    real W: the solution evaluated at the points (X,Y).
#
  import numpy as np

  R = np.sqrt ( ( X - e )**2 + ( Y - f )**2 )

  W =   a     * R**2 * np.log ( R ) \
      + b     * R**2 \
      + c            * np.log ( R ) \
      + d

  return W

def biharmonic_exact_uv1 ( X, Y, a, b, c, d, e, f, g ):

#*****************************************************************************80
#
## biharmonic_exact_uv1() evaluates the flow field for biharmonic solution W(X,Y) #1.
#
#  Discussion:
#
#   W = ( a     * np.cosh ( g * X ) \
#       + b     * np.sinh ( g * X ) \
#       + c * X * np.cosh ( g * X ) \
#       + d * X * np.sinh ( g * X ) ) \ 
#       * \
#       ( e * np.cos ( g * Y ) \
#       + f * np.sin ( g * Y ) )
#
#    U =  dWdy
#    V = -dWdx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c, d, e, f, g: parameters.
#
#  Output:
#
#    real U, V: the flow vector evaluated at the points (X,Y).
#
  import numpy as np

  Wx = \
    ( e         * np.cos ( g * Y ) \
    + f         * np.sin ( g * Y ) ) * \
    ( a * g     * np.sinh ( g * X ) \
    + b * g     * np.cosh ( g * X ) \
    + c * g * X * np.sinh ( g * X ) \
    + c         * np.cosh ( g * X ) \
    + d * g * X * np.cosh ( g * X ) \
    + d         * np.sinh ( g * X ) )

  Wy = \
    ( - e * g * np.sin ( g * Y ) \
    +   f * g * np.cos ( g * Y ) ) * \
    ( a     * np.cosh ( g * X ) \
    + b     * np.sinh ( g * X ) \
    + c * X * np.cosh ( g * X ) \
    + d * X * np.sinh ( g * X ) )

  U =   Wy
  V = - Wx

  return U, V

def biharmonic_exact_uv2 ( X, Y, a, b, c, d, e, f, g ):

#*****************************************************************************80
#
## biharmonic_exact_uv2() evaluates the flow field for biharmonic solution W(X,Y) #2.
#
#  Discussion:
#
#  W = ( a     * np.cos ( g * X ) \
#      + b     * np.sin ( g * X ) \
#      + c * X * np.cos ( g * X ) \
#      + d * X * np.sin ( g * X ) ) \ 
#      *
#      ( e * np.cosh ( g * Y ) \
#      + f * np.sinh ( g * Y ) )
#
#    U =  dWdy
#    V = -dWdx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c, d, e, f, g: parameters.
#
#  Output:
#
#    real U, V: the flow vector evaluated at the points (X,Y).
#
  import numpy as np

  Wx = \
    ( e * np.cosh ( g * Y ) \
    + f * np.sinh ( g * Y ) ) \
    * ( \
    - a * g     * np.sin ( g * X ) \
    + b * g     * np.cos ( g * X ) \
    - c * g * X * np.sin ( g * X ) \
    + c         * np.cos ( g * X ) \
    + d * g * X * np.cos ( g * X ) \
    + d         * np.sin ( g * X ) )

  Wy = \
    ( e * g * np.sinh ( g * Y ) \
    + f * g * np.cosh ( g * Y ) ) * ( \
      a     * np.cos ( g * X ) \
    + b     * np.sin ( g * X ) \
    + c * X * np.cos ( g * X ) \
    + d * X * np.sin ( g * X ) )

  U =   Wy
  V = - Wx

  return U, V

def biharmonic_exact_uv3 ( X, Y, a, b, c, d, e, f ):

#*****************************************************************************80
#
## biharmonic_exact_uv3() evaluates the flow field for biharmonic solution W(X,Y) #3.
#
#  Discussion:
#
#    R = sqrt ( ( X - e )**2 + ( Y - f )**2 )
#
#    W =   a * R**2 * log ( R ) \
#        + b * R**2 \
#        + c * log ( R ) \
#        + d
#
#    U =  dWdy
#    V = -dWdx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, Y: the coordinates of the points.
#
#    real a, b, c, d, e, f, g: parameters.
#
#  Output:
#
#    real U, V: the flow vector evaluated at the points (X,Y).
#
  import numpy as np

  Wx = \
      a * ( - 2 * e + 2 * X ) * np.log ( np.sqrt ( ( - e + X )**2 + ( - f + Y )**2 ) ) \
    + a * ( - e + X ) \
    + b * ( - 2 * e + 2 * X ) \
    + c * ( - e + X ) / ( ( - e + X )**2 + ( - f + Y )**2 )

  Wy = \
      a * ( - 2 * f + 2 * Y ) * np.log ( np.sqrt ( ( - e + X )**2 + ( - f + Y )**2 ) ) \
    + a * ( - f + Y ) \
    + b * ( - 2 * f + 2 * Y ) \
    + c * ( - f + Y ) / ( ( - e + X )**2 + ( - f + Y )**2 )

  U =   Wy
  V = - Wx

  return U, V

def flow_display ( X, Y, U, V, filename ):

#*****************************************************************************80
#
## flow_vector() makes a vector plot of the gradient of a function f(x,y).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 August 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Plot 
#
  plt.clf ( )

  plt.quiver ( X, Y, U, V, color = 'c' )
  plt.axis ( 'Equal' )
  plt.title ( 'Velocity flow field', fontsize = 16 )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
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
  biharmonic_exact_test ( )
  timestamp ( )

