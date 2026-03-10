#! /usr/bin/env python3
#
def mario_fill ( ):

#*****************************************************************************80
#
## mario_fill() creates an image of Mario using colored squares.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2018
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'mario_fill():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Draw a picture of Mario, using colored squares.' )
#
#  Color indices:
#
#  0: white
#  1: black
#  2: red
#  3: blue
#  4: yellow
#  5: beige
#  6: brown
#
  color_index = np.array ( [ \
    [ 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0 ], \
    [ 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0 ], \
    [ 0, 0, 6, 6, 6, 5, 5, 5, 1, 5, 0, 0, 0 ], \
    [ 0, 6, 5, 6, 5, 5, 5, 5, 1, 5, 5, 5, 0 ], \
    [ 0, 6, 5, 6, 6, 5, 5, 5, 5, 1, 5, 5, 5 ], \
    [ 0, 6, 6, 5, 5, 5, 5, 5, 1, 1, 1, 1, 0 ], \
    [ 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0 ], \
    [ 0, 0, 2, 2, 3, 2, 2, 2, 2, 0, 0, 0, 0 ], \
    [ 0, 2, 2, 2, 3, 2, 2, 3, 2, 2, 2, 0, 0 ], \
    [ 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0 ], \
    [ 5, 5, 2, 3, 4, 3, 3, 4, 3, 2, 5, 5, 0 ], \
    [ 5, 5, 5, 3, 3, 3, 3, 3, 3, 5, 5, 5, 0 ], \
    [ 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 0 ], \
    [ 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 0, 0, 0 ], \
    [ 0, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 0, 0 ], \
    [ 6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 0 ] ] )

  dims = color_index.shape
  color_index_m = dims[0]
  color_index_n = dims[1]

  grid_m = color_index_m
  grid_n = color_index_n
  grid = np.zeros ( [ grid_m, grid_n ] )
#
#  Fill the I,J box with color K.
#  Actually, "I" becomes M-I+1, because matrix row 1 is at the top,
#  but cell row 1 is at the bottom.
#
#  (m-i,j-1) <------ (m-i,j)
#      |                 ^
#      |                 |
#      |    Color K      |
#      V                 |
#                        |
#  (m-i+1,j-1) ----> (m-i+1,j)
#
  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  for i in range ( 0, grid_m ):
    for j in range ( 0, grid_n ):

      k = color_index[i,j]

#     if ( k == 0 ):
#       rgb = 'white'
#     elif ( k == 1 ):
#       rgb = 'black'
#     elif ( k == 2 ):
#       rgb = 'red'
#     elif ( k == 3 ):
#       rgb = 'blue'
#     elif ( k == 4 ):
#       rgb = 'yellow'
#     elif ( k == 5 ):
#       rgb = 'bisque'
#     elif ( k == 6 ):
#       rgb = 'brown'

      if ( k == 0 ):
        rgb = [ 1.0, 1.0, 1.0 ];
      elif ( k == 1 ):
        rgb = [ 0.0, 0.0, 0.0 ];
      elif ( k == 2 ):
        rgb = [ 1.0, 0.0, 0.0 ];
      elif ( k == 3 ):
        rgb = [ 0.0, 0.0, 1.0 ];
      elif ( k == 4 ):
        rgb = [ 1.0, 1.0, 0.0 ];
      elif ( k == 5 ):
        rgb = [ 1.0, 0.8, 0.6 ];
      elif ( k == 6 ):
        rgb = [ 0.8, 0.4, 0.0 ];

      cell_ij_fill ( grid_m, i, j, color = rgb )

  filename = 'mario_fill.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'mario_fill():' )
  print ( '  Normal end of execution.' )

  return

def cell_ij_fill ( m, i, j, color ):

#*****************************************************************************80
#
## cell_ij_fill() plots a filled (I,J) cell.
#
#  Discussion:
#
#    We assume the data is represented in a matrix.
#
#    In order to convert between the matrix coordinates and picture
#    coordinates, the (I,J) cell will be drawn with the following corners:
#
#    (j-1,m-i+1), (j,m-i+1), (j,m-i), (j-1,m-1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the maximum row index.
#
#    integer I, J, the index of the cell.
#
#    color COLOR, can be any of the 8 abbreviated color terms
#    'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k', or an RGB triple such as 
#    [1.0,0.4,0.0].  The square is filled with this color.
#
  import matplotlib.pyplot as plt

  a = j - 1
  b = j
  c = m - ( i - 1 )
  d = m - i

  plt.fill ( [ a, b, b, a ], [ c, c, d, d ], color )

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
#    06 April 2013
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
  mario_fill ( )
  timestamp ( )
