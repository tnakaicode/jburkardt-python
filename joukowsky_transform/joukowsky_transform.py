#! /usr/bin/env python3
#
def joukowsky_transform ( z ):

#*****************************************************************************80
#
## joukowsky_transform() applies the Joukowsky transform to data.
#
#  Discussion:
#
#    The transform is its own inverse.
#
#    Typically, the input is a set of complex points on the circumference
#    of a circle with center c and radius r which contains the point z=-1.
#
#    For a certain range of c and r, the transformed data can take a
#    shape suggestive of various airfoils.  
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    Airfoils,
#    https://www.johndcook.com/blog/2023/01/21/airfoils/
#    Posted 21 January 2021
#
#  Input:
#
#    complex z(*): data to be transformed.
#
#  Output:
#
#    complex fz(*): the transformed data.
#
  fz = 0.5 * ( z + 1.0 / z )
  
  return fz

def joukowsky_transform_test ( ):

#*****************************************************************************80
#
## joukowsky_transform_test() tests joukowsky_transform().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 January 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'joukowsky_transform_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test joukowsky_transform().' )

  joukowsky_transform_test01 ( )
  joukowsky_transform_test02 ( )
  joukowsky_transform_test03 ( )
  joukowsky_transform_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'joukowsky_transform_test():' )
  print ( '  Normal end of execution.' )

  return

def joukowsky_transform_test01 ( ):

#*****************************************************************************80
#
## joukowsky_transform_test01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 January 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'joukowsky_transform_test01():' )

  n = 101

  c1 = -0.156
  r1 = 1.2
  z1 = circle_points ( c1, r1, n )
  fz1 = joukowsky_transform ( z1 )

  c2 = -0.100
  r2 = 1.1
  z2 = circle_points ( c2, r2, n )
  fz2 = joukowsky_transform ( z2 )

  plt.clf ( )
  plt.plot ( np.real ( fz1 ), np.imag ( fz1 ), 'b.' )
  plt.plot ( np.real ( fz2 ), np.imag ( fz2 ), 'r.' )
  plt.axis ( 'equal' )
  plt.grid ( True )
  filename = 'airfoil1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  
  return

def joukowsky_transform_test02 ( ):

#*****************************************************************************80
#
## joukowsky_transform_test02().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 January 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'joukowsky_transform_test02():' )

  n = 101

  c1 = -0.133 + 0.238j
  r1 = 1.2
  z1 = circle_points ( c1, r1, n )
  fz1 = joukowsky_transform ( z1 )

  c2 =  0.022 + 0.219j
  r2 = 1.1
  z2 = circle_points ( c2, r2, n )
  fz2 = joukowsky_transform ( z2 )

  plt.clf ( )
  plt.plot ( np.real ( fz1 ), np.imag ( fz1 ), 'b.' )
  plt.plot ( np.real ( fz2 ), np.imag ( fz2 ), 'r.' )
  plt.axis ( 'equal' )
  plt.grid ( True )
  filename = 'airfoil2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  
  return

def joukowsky_transform_test03 ( ):

#*****************************************************************************80
#
## joukowsky_transform_test03().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 January 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'joukowsky_transform_test03():' )

  n = 101
  c = -0.5 + 0.05j
  r = 1.2
  z = circle_points ( c, r, n )
  fz = joukowsky_transform ( z )

  plt.clf ( )
  plt.plot ( np.real ( fz ), np.imag ( fz ), 'b.' )
  plt.axis ( 'equal' )
  plt.grid ( True )
  filename = 'airfoil3.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  
  return

def joukowsky_transform_test04 ( ):

#*****************************************************************************80
#
## joukowsky_transform_test04().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 January 2023
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'joukowsky_transform_test04():' )

  n = 101
  c = -0.02 + 0.3j
  r = 1.2
  z = circle_points ( c, r, n )
  fz = joukowsky_transform ( z )

  plt.clf ( )
  plt.plot ( np.real ( fz ), np.imag ( fz ), 'b.' )
  plt.axis ( 'equal' )
  plt.grid ( True )
  filename = 'airfoil4.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  
  return
  
def circle_points ( c, r, n ):

#*****************************************************************************80
#
## circle_points() returns n points on circle of center c and radius r.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 January 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    complex c: the center of the circle.
#
#    real r: the radius of the circle.
#
#    integer n: the number of points to compute.
#
#  Output:
#
#    complex z(n): points along the circumference of the circle.
#
  import numpy as np
  
  theta = np.linspace ( 0.0, 2.0 * np.pi, n )
  z = r * ( np.cos ( theta ) + np.sin ( theta ) * 1j + c )
  
  return z

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
  joukowsky_transform_test ( )
  timestamp ( )

