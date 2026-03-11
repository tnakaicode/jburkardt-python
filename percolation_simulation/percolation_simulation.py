#! /usr/bin/env python3
#
def percolation_simulation_test ( ):

#*****************************************************************************80
#
## percolation_simulation_test() tests percolation_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'percolation_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  percolation_simulation() simulates percolation.' )
  print ( '  A rectangular region is formed by a grid of M x N squares.' )
  print ( '  Each square may be porous or solid.' )
  print ( '  We are interested in paths of porous squares connecting' )
  print ( '  the top and bottom, or the left and right boundaries.' )

  m = 32
  n = 32
  p = 0.60

  print ( '' )
  print ( '  Grid uses', m, 'rows x', n, 'columns.' )
  print ( '  Prescribed probability of occupation =', p )

  percolation_simulation ( m, n, p )
#
#  Terminate.
#
  print ( '' )
  print ( 'percolation_simulation_test()' )
  print ( '  Normal end of execution.' )

  return

def percolation_simulation ( m, n, p ):

#*****************************************************************************80
#
## percolation_simulation() simulates and analyzes a percolation system.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2025
#
#  Author:
#
#    Original MATLAB version by Ian Cooper
#    This version by John Burkardt
#
#  Input:
#
#    integer m, n: the number of rows and columns in the grid.
#
#    real p: the probability that a given site should be occupied.
#
  from scipy.ndimage import label
  import matplotlib.pyplot as plt
  import numpy as np
#
#  The grid variable U is 0 or 1.
#
  U = np.random.choice ( [ 0, 1 ], [ m, n ], replace = True, p = [ 1-p, p ] )
#
#  Count the number of occupied sites.
#
  nosites = np.sum ( U )
#
#  Observed probability of a site being occupied.
#
  posites = nosites / m / n
#
#  cls = copy of u with nonzeros replaced by component labels.
#
  CLS, component_num = label ( U )
#
#  Number of components is maximum label in CLS.
#
  component_num = np.max ( CLS )
#
#  Number of occupied sites in each component.
#
  component_size = np.zeros ( component_num + 1, dtype = int )
  for c in range ( 0, component_num + 1 ):
    component_size[c] = np.sum ( U [ CLS == c ] )
#
#  Counter from 1 to max number of occupied sites in a component.
#
  component_size_max = np.max ( component_size )
#
#  ns = component size distribution.
#
  ns = np.zeros ( component_size_max + 1, dtype = int )
  for c in range ( 0, component_size_max + 1 ):
    ns[c] = len ( component_size [ component_size == c ] )
#
#  Probability that a site chosen at random is part of
#  an s-site component.
#
  probros = ns / np.sum ( ns )
#
#  Check for spanning components.
#  Does a "c" occur in column 1 and column n?
#  Does a "c" occur in row 1 and row m?
#
  spanx = np.zeros ( component_num, dtype = int )
  spany = np.zeros ( component_num, dtype = int )

  for c in range ( 1, component_num ):

    left = False
    for i in range ( 0, m ):
      if ( CLS[i,0] == c ):
        left = True
        break

    right = False
    for i in range ( 0, m ):
      if ( CLS[i,-1] == c ):
        right = True
        break

    if ( left and right ):
      spanx[c] = 1

    top = False
    for j in range ( 0, n ):
      if ( CLS[0,j] == c ):
        top = True
        break

    bottom = False
    for j in range ( 0, n ):
      if ( CLS[-1,j] == c ):
        bottom = True
        break

    if ( top and bottom ):
      spany[c] = 1
#
#  Output
#
  print ( '' )
  print ( '  Total number of sites = ', m * n )
  print ( '  Number of occupied sites = ', nosites )
  print ( '  Observed probability of occupation = ', posites )
  print ( '  Number of components = ', component_num )
  print ( '  Mean component size = ', np.mean ( component_size ) )
  print ( '' )
  print ( '  component size distribution' )
  print ( '    Size  Number  Probability' )
  print ( '' )
  for c in range ( 0, component_size_max + 1 ):
    if ( 0 < ns[c] ):
      print ( '       %2d  %2d  %g' % ( c, ns[c], probros[c] ) )

  spanx_num = np.sum ( spanx )
  spany_num = np.sum ( spany )

  print ( '' )
  print ( '  Number of horizontal spanning components = ', spanx_num )
  print ( '  Number of vertical spanning components   = ', spany_num )
#
#  Plot occupied cells.
#
  plot_U ( U )
#
#  Plot components.
#
  plot_C ( CLS )

  return

def plot_U ( U ):

#*****************************************************************************80
#
## plot_U() plots the occupied cells.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer U[m,n]: an array of 0's (blocked) and 1's (open).
#
  import matplotlib.pyplot as plt

  m, n = U.shape

  plt.clf ( )
  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  outline = True
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( U[i,j] == 0 ):
        rgb = 'white'
      else:
        rgb = 'blue'
      cell_ij_fill ( m, i, j, rgb, outline )

  plt.title ( 'percolation occupation' )
  filename = 'occupation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def plot_C ( C ):

#*****************************************************************************80
#
## plot_C() plots the percolation components.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer C[m,n]: an array of 0's (blocked) and positive values
#    (labels for component).
#
  import matplotlib.pyplot as plt
  import numpy as np

  m, n = C.shape 

  component_num = np.max ( C )
#
#  Choose a random RGB color for every component, plus 1 for the blocks.
#
  color = np.random.random ( [ component_num + 1, 3 ] )
  color[0,:] = [ 1.0, 1.0, 1.0 ]
  for i in range ( 1, component_num + 1 ):
    color[i,:] = color[i,:] / np.linalg.norm ( color[i,:] )

  plt.clf ( )
  plt.axis ( 'equal' )
  plt.axis ( 'off' )

  outline = True
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      c = C[i,j]
      rgb = color[c,:]
      cell_ij_fill ( m, i, j, rgb, outline )

  plt.title ( 'percolation components' )
  filename = 'components.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def cell_ij_fill ( m, i, j, rgb, outline ):

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
#    17 July 2022
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
#    color RGB, can be any of the 8 abbreviated color terms
#    'r', 'g', 'b', 'c', 'm', 'y', 'w', 'k', or an RGB triple such as 
#    [1.0,0.4,0.0].  The square is filled with this color.
#
#    bool outline: is True if the cell should be outlined in black.
#
  import matplotlib.pyplot as plt

  a = j - 1
  b = j
  c = m - ( i - 1 )
  d = m - i

  plt.fill ( [ a, b, b, a ], [ c, c, d, d ], color = rgb )

  if ( outline ):
    plt.plot ( [ a, b, b, a, a ], [ c, c, d, d, c ], 'k-' )

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
  percolation_simulation_test ( )
  timestamp ( )

