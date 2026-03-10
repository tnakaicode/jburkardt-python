#! /usr/bin/env python3
#
def house_test ( ):

#*****************************************************************************80
#
## house_test() tests house().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'house_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test house().' )

  house_identity_test ( )
#
#  Isometries.
#
  house_translation_test ( )
  house_rotation_test ( )
  house_reflection_ud_test ( )
  house_reflection_rl_test ( )
  house_reflection_udrl_test ()
#
#  Scaling along axes.
#
  house_scale_uniform_test ( )
  house_scale_nonuniform_test ( )
#
#  Shears.
#
  house_shear_vertical_test ( )
  house_shear_horizontal_test ( )
  house_shear_general_test ( )
#
#  Singularities.
#
  house_zero_test ( )
  house_projection_test ( )
#
#  General transformation.
#
  house_linear_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'house_test():' )
  print ( '  Normal end of execution.' )

  return

def house ( ):

#*****************************************************************************80
#
## house() returns line segments that outline a house.
#
#  Discussion:
#
#    The first node is repeated at the end to close the final line segment.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    Original version by Cleve Moler.
#    This version by John Burkardt.
#
#  Output:
#
#    real H(12,2), line segments that outline a house.
#
  import numpy as np

  H = np.array ( [ \
    [ -6, -7 ], \
    [ -6,  2 ], \
    [ -7,  1 ], \
    [  0,  8 ], \
    [  7,  1 ], \
    [  6,  2 ], \
    [  6, -7 ], \
    [ -3, -7 ], \
    [ -3, -2 ], \
    [  0, -2 ], \
    [  0, -7 ], \
    [ -6, -7 ] ] )

  return H

def house_identity_test ( ):

#*****************************************************************************80
#
## house_identity_test() applies the identity map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_identity_test():' )
  print ( '  Apply the identity map to the house.' )

  H0 = house ( )
  m, n = H0.shape

  A = np.identity ( n )
  H1 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'k.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'Identity * House' )

  filename = 'house_identity.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_linear_test ( ):

#*****************************************************************************80
#
## house_projection_test() applies a linear map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_linear_test():' )
  print ( '  Apply a linear map to the house.' )

  H0 = house ( )

  A = np.array ( [ [ 0.25, 0.5 ], [ 0.75, 1.0 ] ] )
  H1 = np.matmul ( H0, A.T )

  A = np.array ( [ [ 1.0, 0.5 ], [ 0.25, 0.75 ] ] )
  H2 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.plot ( H2[:,0], H2[:,1], 'g.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + linear map' )

  filename = 'house_linear.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_projection_test ( ):

#*****************************************************************************80
#
## house_projection_test() applies projection to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_projection_test():' )
  print ( '  Apply projection to the house.' )

  H0 = house ( )

  A = np.array ( [ [ 1, 0 ], [ 0, 0 ] ] )
  H1 = np.matmul ( H0, A.T )

  A = np.array ( [ [ 2, 1 ], [ 2, 1 ] ] )
  H2 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.plot ( H2[:,0], H2[:,1], 'g.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + projection' )

  filename = 'house_projection.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_reflection_rl_test ( ):

#*****************************************************************************80
#
## house_reflection_rl_test() applies the reflection Right/Left map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_reflection_rl_test():' )
  print ( '  Apply the reflection Right/Left map to the house.' )

  H0 = house ( )

  A = np.array ( [ [ -1, 0 ], [ 0, 1 ] ] )
  H1 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + reflection Right/Left' )

  filename = 'house_reflection_rl.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_reflection_udrl_test ( ):

#*****************************************************************************80
#
## house_reflection_udrl_test(): reflection Up/Down Right/Left to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_reflection_udrl_test():' )
  print ( '  Apply the reflection Up/Down Right/Left map to the house.' )

  H0 = house ( )

  A = np.array ( [ [ -1, 0 ], [ 0, -1 ] ] )
  H1 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + reflection Up/Down Right/Left' )

  filename = 'house_reflection_udrl.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_reflection_ud_test ( ):

#*****************************************************************************80
#
## house_reflection_ud_test() applies the reflection Up/Down map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_reflection_ud_test():' )
  print ( '  Apply the reflection Up/Down map to the house.' )

  H0 = house ( )

  A = np.array ( [ [ 1, 0 ], [ 0, -1 ] ] )
  H1 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + reflection Up/Down' )

  filename = 'house_reflection_ud.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_rotation_test ( ):

#*****************************************************************************80
#
## house_rotation_test() applies the rotation map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_rotation_test():' )
  print ( '  Apply the rotation map to the house.' )

  H0 = house ( )

  t1 = 15.0 * np.pi / 180.0
  A = np.array ( [ [ np.cos(t1), -np.sin(t1) ], [ np.sin(t1),  np.cos(t1) ] ] )
  H1 = np.matmul ( H0, A.T )

  t2 = 30.0 * np.pi / 180.0
  A = np.array ( [ [ np.cos(t2), -np.sin(t2) ], [ np.sin(t2),  np.cos(t2) ] ] )
  H2 = np.matmul ( H0, A.T )

  t3 = 75.0 * np.pi / 180.0
  A = np.array ( [ [ np.cos(t3), -np.sin(t3) ], [ np.sin(t3),  np.cos(t3) ] ] )
  H3 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.plot ( H2[:,0], H2[:,1], 'g.-', markersize = 18, linewidth = 2 )
  plt.plot ( H3[:,0], H3[:,1], 'b.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + rotation of 15, 30 and 75 degrees' )

  filename = 'house_rotation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_scale_nonuniform_test ( ):

#*****************************************************************************80
#
## house_scale_nonuniform_test() applies nonuniform scale map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_scale_nonuniform_test()' )
  print ( '  Apply the nonuniform scale map to the house.' )

  H0 = house ( )

  A = np.array ( [ [ 1.25, 0 ], [ 0, 0.75 ] ] )
  H1 = np.matmul ( H0, A.T )

  A = np.array ( [ [ 1.50, 0 ], [ 0, 0.50 ] ] )
  H2 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.plot ( H2[:,0], H2[:,1], 'g.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + nonuniform scaling' )

  filename = 'house_scale_nonuniform.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_scale_uniform_test ( ):

#*****************************************************************************80
#
## house_scale_uniform_test() applies uniform scale map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_scale_uniform_test():' )
  print ( '  Apply the uniform scale map to the house.' )

  H0 = house ( )

  A = np.array ( [ [ 1.25, 0 ], [ 0, 1.25 ] ] )
  H1 = np.matmul ( H0, A.T )

  A = np.array ( [ [ 1.50, 0 ], [ 0, 1.50 ] ] )
  H2 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.plot ( H2[:,0], H2[:,1], 'g.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + uniform scaling' )

  filename = 'house_scale_uniform.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_shear_general_test ( ):

#*****************************************************************************80
#
## house_shear_general_test() applies general shear map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_shear_general_test():' )
  print ( '  Apply the general shear map to the house.' )

  H0 = house ( )

  A = np.array ( [ [ 1, 0.25 ], [ np.sqrt(3)/4, 1 ] ] )
  H1 = np.matmul ( H0, A.T )

  A = np.array ( [ [ 1, 0.5 ], [ np.sqrt(3)/2, 1 ] ] )
  H2 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.plot ( H2[:,0], H2[:,1], 'g.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + general shear' )

  filename = 'house_shear_general.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_shear_horizontal_test ( ):

#*****************************************************************************80
#
## house_shear_horizontal_test() applies horizontal shear map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_shear_horizontal_test():' )
  print ( '  Apply the horizontal shear map to the house.' )

  H0 = house ( )

  A = np.array ( [ [ 1, 0.25 ], [ 0, 1 ] ] )
  H1 = np.matmul ( H0, A.T )

  A = np.array ( [ [ 1, 0.5 ], [ 0, 1 ] ] )
  H2 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.plot ( H2[:,0], H2[:,1], 'g.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + horizontal shear' )

  filename = 'house_shear_horizontal.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_shear_vertical_test ( ):

#*****************************************************************************80
#
## house_shear_vertical_test() applies vertical shear map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_shear_vertical_test():' )
  print ( '  Apply the vertical shear map to the house.' )

  H0 = house ( )

  A = np.array ( [ [ 1, 0 ], [ 0.25, 1 ] ] )
  H1 = np.matmul ( H0, A.T )

  A = np.array ( [ [ 1, 0.0 ], [ 0.5, 1 ] ] )
  H2 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.plot ( H2[:,0], H2[:,1], 'g.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + vertical shear' )

  filename = 'house_shear_vertical.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_translation_test ( ):

#*****************************************************************************80
#
## house_translation_test() applies the translation map to the house.
#
#  Discussion:
#
#    Translation is NOT a linear mapping.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_translation_test():' )
  print ( '  Apply the translation map to the house.' )

  H0 = house ( )

  t1 = np.array ( [ - 3.0, 0.0 ] )
  H1 = H0 + t1

  t2 = np.array ( [ 0.0, 2.0 ] )
  H2 = H0 + t2

  t3 = np.array ( [ 4.0, 4.0 ] )
  H3 = H0 + t3

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'r.-', markersize = 18, linewidth = 2 )
  plt.plot ( H2[:,0], H2[:,1], 'g.-', markersize = 18, linewidth = 2 )
  plt.plot ( H3[:,0], H3[:,1], 'b.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'House + t' )

  filename = 'house_translation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def house_zero_test ( ):

#*****************************************************************************80
#
## house_zero_test() applies the zero map to the house.
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2026
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_zero_test():' )
  print ( '  Apply the zero map to the house.' )

  H0 = house ( )
  m, n = H0.shape

  A = np.zeros ( [ n, n ] )
  H1 = np.matmul ( H0, A.T )

  plt.clf ( )
  plt.plot ( H0[:,0], H0[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( H1[:,0], H1[:,1], 'k.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -12, 12, -12, 12 ] )
  plt.axis ( 'equal' )
  plt.title ( 'zero * House' )

  filename = 'house_zero.png'
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
  house_test ( )
  timestamp ( )

