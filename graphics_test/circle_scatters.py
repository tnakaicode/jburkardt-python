#! /usr/bin/env python3
#
def circle_scatters ( ):

#*****************************************************************************80
#
## circle_scatters plots data in and out of a circle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 May 2016
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'circle_scatters:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a scatterplot of two sets of data representing' )
  print ( '  points in the unit square that are also in or not in' )
  print ( '  the unit circle.' )
#
#  Read the pairs "in circle" data from the file.
#
  xi = []
  yi = []
  ni = 0

  file = open ( 'circle1_data.txt', 'r' )

  for line in file:
    line = line.strip ( )
    columns = line.split ( )
    xi.append ( float ( columns[0] ) )
    yi.append ( float ( columns[1] ) )
    ni = ni + 1

  file.close ( )
#
#  Read the pairs "iout circle" data from the file.
#
  xo = []
  yo = []
  no = 0

  file = open ( 'circle2_data.txt', 'r' )

  for line in file:
    line = line.strip ( )
    columns = line.split ( )
    xo.append ( float ( columns[0] ) )
    yo.append ( float ( columns[1] ) )
    no = no + 1

  file.close ( )
#
#  Report on the estimate for pi:
#
  print ( '' )
  print ( '  Number of points inside the circle = %d' % ( ni ) )
  print ( '  Number outside                     = %d' % ( no ) )
  print ( '  Total                              = %d' % ( ni + no ) )
  print ( '  Estimate for PI                    = %d' % ( 4.0 * float ( ni ) / float ( ni + no ) ) )
#
#  Set up points on a circle
#
  nc = 50
  t = np.linspace ( 0.0, 0.5 * np.pi, nc )
  xc = np.cos ( t )
  yc = np.sin ( t )
#
#  Plot the data.
#
  plt.plot ( xc, yc, linewidth = 2, color = 'r' )
  plt.plot ( xi, yi, 'bo' )
  plt.plot ( xo, yo, 'ro' )
  plt.axis ( [ 0.0, 1.0, 0.0, 1.0] )
  plt.gca().set_aspect ( 'equal', adjustable = 'box' )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  plt.title ( 'Random points inside/outside the unit circle', fontsize = 16 )
  filename = 'circle_scatters.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
#
#  Terminate.
#
  print ( '' )
  print ( 'circle_scatters' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  circle_scatters ( )
  timestamp ( )
 
