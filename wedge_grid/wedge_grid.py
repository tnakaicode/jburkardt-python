#! /usr/bin/env python3
#
def r83col_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## r83col_print_part() prints "part" of an R83COL.
#
#  Discussion:
#
#    An R83COL is a (3,N) array of R8's.
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_PRINT, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(N,3), the vector to be printed.
#
#    integer MAX_PRINT, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( 0 < max_print ):

    if ( 0 < n ):

      if ( 0 < len ( title ) ):
        print ( '' )
        print ( title )

      print ( '' )

      if ( n <= max_print ):

        for i in range ( 0, n ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
        print ( '  ....  ..............  ..............  ..............' )
        i = n - 1
        print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )

      else:

        for i in range ( 0, max_print - 1 ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
        i = max_print - 1
        print ( '  %4d  %14g  %14g  %14g  ...more entries...' \
          % ( i, a[i,0], a[i,1], a[i,2] ) )

  return

def r83col_print_part_test ( ):

#*****************************************************************************80
#
## r83col_print_part_test() tests r83col_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  print ( '' )
  print ( 'r83col_print_part_test():' )
  print ( '  r83col_print_part() prints part of an R83COL.' )

  n = 10

  v = np.array ( [ \
    [  11,  12,  13 ], \
    [  21,  22,  23 ], \
    [  31,  32,  33 ], \
    [  41,  42,  43 ], \
    [  51,  52,  53 ], \
    [  61,  62,  63 ], \
    [  71,  72,  73 ], \
    [  81,  82,  83 ], \
    [  91,  92,  93 ], \
    [ 101, 102, 103 ] ] )

  max_print = 2
  r83col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 2' )

  max_print = 5
  r83col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 5' )

  max_print = 25
  r83col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 25' )

  return

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## r8mat_write() writes an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8mat_write_test ( ):

#*****************************************************************************80
#
## r8mat_write_test() tests r8mat_write().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_write_test():' )
  print ( '  r8mat_write() writes an R8MAT to a file.' )

  filename = 'r8mat_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 1.1, 1.2, 1.3 ), \
    ( 2.1, 2.2, 2.3 ), \
    ( 3.1, 3.2, 3.3 ), \
    ( 4.1, 4.2, 4.3 ), \
    ( 5.1, 5.2, 5.3 ) ) )
  r8mat_write ( filename, m, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )

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

  return None

def wedge_grid_count ( n ):

#*****************************************************************************80
#
## wedge_grid_count() counts the points in a grid of the unit wedge in 3D.
#
#  Discussion:
#
#    The interior of the unit wedge in 3D is defined by the constraints:
#      0 <= X
#      0 <= Y
#           X + Y <= 1
#     -1 <= Z <= +1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of subintervals.
#    0 <= N.
#
#  Output:
#
#    integer NG, the number of grid points.
#
  ng = ( n + 1 ) * ( ( n + 1 ) * ( n + 2 ) ) // 2

  return ng

def wedge_grid_count_test ( ):

#*****************************************************************************80
#
## wedge_grid_count_test() tests wedge_grid_count().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'wedge_grid_count_test():' )
  print ( '  wedge_grid_count() defines a grid of points' )
  print ( '  with N+1 points on a side' )
  print ( '  over the interior of the unit wedge in 3D.' )
  print ( '' )
  print ( '   N    NG' )
  print ( '' )
  for n in range ( 1, 11 ):
    ng = wedge_grid_count ( n )
    print ( '  %2d  %4d' % ( n, ng ) )

  return

def wedge_grid_display ( ng, xg, filename ):

#*****************************************************************************80
#
## wedge_grid_display() displays grid points inside the unit wedge.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NG, the number of grid points.
#
#    real XG[NG,3], the grid points.
#
#    string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
  from mpl_toolkits.mplot3d import Axes3D

  xv = np.array ( [ \
    [  0.0,  0.0, -1.0 ], \
    [  1.0,  0.0, -1.0 ], \
    [  0.0,  1.0, -1.0 ], \
    [  0.0,  0.0, +1.0 ], \
    [  1.0,  0.0, +1.0 ], \
    [  0.0,  1.0, +1.0 ] \
  ] )

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
#
#  Draw the grid points.
#
  ax.scatter ( xg[:,0], xg[:,1], xg[:,2], 'b' )
#
#  Outline the hexahedron by its edges.
#
  ax.plot ( [ xv[0,0], xv[1,0] ], [ xv[0,1], xv[1,1] ], [ xv[0,2], xv[1,2] ], 'r' )
  ax.plot ( [ xv[1,0], xv[2,0] ], [ xv[1,1], xv[2,1] ], [ xv[1,2], xv[2,2] ], 'r' )
  ax.plot ( [ xv[2,0], xv[0,0] ], [ xv[2,1], xv[0,1] ], [ xv[2,2], xv[0,2] ], 'r' )

  ax.plot ( [ xv[3,0], xv[4,0] ], [ xv[3,1], xv[4,1] ], [ xv[3,2], xv[4,2] ], 'r' )
  ax.plot ( [ xv[4,0], xv[5,0] ], [ xv[4,1], xv[5,1] ], [ xv[4,2], xv[5,2] ], 'r' )
  ax.plot ( [ xv[5,0], xv[3,0] ], [ xv[5,1], xv[3,1] ], [ xv[5,2], xv[3,2] ], 'r' )

  ax.plot ( [ xv[0,0], xv[3,0] ], [ xv[0,1], xv[3,1] ], [ xv[0,2], xv[3,2] ], 'r' )
  ax.plot ( [ xv[1,0], xv[4,0] ], [ xv[1,1], xv[4,1] ], [ xv[1,2], xv[4,2] ], 'r' )
  ax.plot ( [ xv[2,0], xv[5,0] ], [ xv[2,1], xv[5,1] ], [ xv[2,2], xv[5,2] ], 'r' )

  ax.set_xlabel ( '<---X--->' )
  ax.set_ylabel ( '<---Y--->' )
  ax.set_zlabel ( '<---Z--->' )
  ax.set_title ( 'Grid points in unit wedge' )
  ax.grid ( True )
# ax.axis ( 'equal' )
  plt.savefig ( filename )
  plt.show ( block = False )

  plt.close ( )

  return

def wedge_grid_display_test ( ):

#*****************************************************************************80
#
## wedge_grid_display_test() tests wedge_grid_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'wedge_grid_display_test():' )
  print ( '  wedge_grid_display() can display a grid of points in the unit wedge.' )

  n = 3

  ng = wedge_grid_count ( n )
  xg = wedge_grid_points ( n, ng )

  filename = 'wedge_grid_display.png'

  wedge_grid_display ( ng, xg, filename )

  return
  
def wedge_grid_points ( n, ng ):

#*****************************************************************************80
#
## wedge_grid_points() computes grid points in the unit wedge in 3D.
#
#  Discussion:
#
#    The interior of the unit wedge in 3D is defined by the constraints:
#      0 <= X
#      0 <= Y
#           X + Y <= 1
#     -1 <= Z <= +1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of subintervals.
#    0 <= N.
#
#    integer NG, the number of grid points.
#    This can be computed by WEDGE_GRID_SIZE, or else determined by
#    NG =(N+1)*((N+1)*(N+2))/2.
#
#  Output:
#
#    real XG[NG,3], the coordinates
#    of the grid points.
#
  import numpy as np

  xg = np.zeros ( ( ng, 3 ) )

  if ( n == 0 ):

    xg[0,0] = 0.5
    xg[0,1] = 0.5
    xg[0,2] = 0.0

  else:

    p = 0

    for k in range ( 0, n + 1 ):
      kr = float ( 2 * k - n ) / float ( n )
      for j in range ( 0, n + 1 ):
        jr = float ( j ) / float ( n )
        for i in range ( 0, n + 1 - j ):
          ir = float ( i ) / float ( n )
          xg[p,0] = ir
          xg[p,1] = jr
          xg[p,2] = kr
          p = p + 1

  return xg

def wedge_grid_points_test ( ):

#*****************************************************************************80
#
## wedge_grid_points_test() tests wedge_grid_points().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'wedge_grid_points_test():' )
  print ( '  wedge_grid_points() determines a unit wedge' )
  print ( '  grid with N+1 points along each edge.' )

  n = 6
  print ( '' )
  print ( '  Grid parameter N = %d' % ( n ) )

  ng = wedge_grid_count ( n )
  print ( '' )
  print ( '  Grid size NG = %d' % ( ng ) )

  xg = wedge_grid_points ( n, ng )

  r83col_print_part ( ng, xg, 20, '  Wedge grid points:' )
#
#  Write the data to a file.
#
  filename = 'wedge_grid_points.xyz'
  r8mat_write ( filename, ng, 3, xg )
  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )
#
#  Plot the data.
#
  filename = 'wedge_grid_points.png'
  wedge_grid_display ( ng, xg, filename )
  print ( '' )
  print ( '  Plot written to the file "%s".' % ( filename ) )

  return
  
def wedge_grid_test ( ):

#*****************************************************************************80
#
## wedge_grid_test() tests wedge_grid().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'wedge_grid_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test wedge_grid().' )
#
#  Utilities:
#
  r83col_print_part_test ( )
  r8mat_write_test ( )
#
#  Library.
#
  wedge_grid_count_test ( )
  wedge_grid_display_test ( )
  wedge_grid_points_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'wedge_grid_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  wedge_grid_test ( )
  timestamp ( )

