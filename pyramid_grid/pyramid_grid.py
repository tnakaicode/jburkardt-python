#! /usr/bin/env python3
#
def pyramid_grid_count ( n ):

#*****************************************************************************80
#
## PYRAMID_GRID_COUNT counts the points in a pyramid grid.
#
#  Discussion:
#
#    0:  x
#
#    1:  x  x
#        x  x
#
#    2:  x  x  x
#        x  x  x
#        x  x  x
#
#    3:  x  x  x  x
#        x  x  x  x
#        x  x  x  x
#        x  x  x  x
#
#    N  Size
#
#    0     1
#    1     5 = 1 + 4
#    2    14 = 1 + 4 + 9
#    3    30 = 1 + 4 + 9 + 16
#    4    55 = 1 + 4 + 9 + 16 + 25
#    5    91 = 1 + 4 + 9 + 16 + 25 + 36
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Output, integer VALUE, the number of
#    nodes in the grid of size N.
#
  np1 = n + 1

  value = ( np1 * ( np1 + 1 ) * ( 2 * np1 + 1 ) ) // 6

  return value

def pyramid_grid_count_test ( ):

#*****************************************************************************80
#
## PYRAMID_GRID_COUNT_TEST tests PYRAMID_GRID_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PYRAMID_GRID_COUNT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PYRAMID_GRID_COUNT can count the grid points in a pyramid' )
  print ( '  with N+1 points on a side.' )

  print ( '' )
  print ( '     N        NG' )
  print ( '' )

  for n in [ 1, 2, 3, 4, 5, 10, 15, 20, 25, 50, 100 ]:
    ng = pyramid_grid_count ( n )
    print ( '  %4d  %8d' % ( n, ng ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PYRAMID_GRID_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def pyramid_grid_display ( ng, xg, filename ):

#*****************************************************************************80
#
## PYRAMID_GRID_DISPLAY displays grid points inside the unit pyramid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NG, the number of grid points.
#
#    Input, real XG[NG,3], the grid points.
#
#    Input, string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
  from mpl_toolkits.mplot3d import Axes3D

  xv = np.array ( [
    [  0.0,  0.0, +1.0 ], \
    [ -1.0, -1.0,  0.0 ], \
    [ +1.0, -1.0,  0.0 ], \
    [ +1.0, +1.0,  0.0 ], \
    [ -1.0, +1.0,  0.0 ] ] )

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
  ax.plot ( [ xv[0,0], xv[2,0] ], [ xv[0,1], xv[2,1] ], [ xv[0,2], xv[2,2] ], 'r' )
  ax.plot ( [ xv[0,0], xv[3,0] ], [ xv[0,1], xv[3,1] ], [ xv[0,2], xv[3,2] ], 'r' )
  ax.plot ( [ xv[0,0], xv[4,0] ], [ xv[0,1], xv[4,1] ], [ xv[0,2], xv[4,2] ], 'r' )

  ax.plot ( [ xv[4,0], xv[1,0] ], [ xv[4,1], xv[1,1] ], [ xv[4,2], xv[1,2] ], 'r' )
  ax.plot ( [ xv[1,0], xv[2,0] ], [ xv[1,1], xv[2,1] ], [ xv[1,2], xv[2,2] ], 'r' )
  ax.plot ( [ xv[2,0], xv[3,0] ], [ xv[2,1], xv[3,1] ], [ xv[2,2], xv[3,2] ], 'r' )
  ax.plot ( [ xv[3,0], xv[4,0] ], [ xv[3,1], xv[4,1] ], [ xv[3,2], xv[4,2] ], 'r' )

  ax.set_xlabel ( '<---X--->' )
  ax.set_ylabel ( '<---Y--->' )
  ax.set_zlabel ( '<---Z--->' )
  ax.set_title ( 'Grid points in unit pyramid' )
  ax.grid ( True )
# ax.axis ( 'equal' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.clf ( )

  return

def pyramid_grid_display_test ( ):

#*****************************************************************************80
#
## PYRAMID_GRID_DISPLAY displays grid points inside a unit pyramid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'PYRAMID_GRID_DISPLAY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PYRAMID_GRID_DISPLAY can display a grid of points in the unit pyramid.' )

  n = 3

  ng = pyramid_grid_count ( n )
  xg = pyramid_grid_points ( n, ng )

  filename = 'pyramid_grid_display.png'

  pyramid_grid_display ( ng, xg, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'PYRAMID_GRID_DISPLAY_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def pyramid_grid_points ( n, ng ):

#*****************************************************************************80
#
## PYRAMID_GRID_POINTS computes grid points in the unit pyramid.
#
#  Discussion:
#
#    The unit pyramid has base (-1,-1,0), (+1,1,0), (+1,+1,0), (-1,+1,0)
#    and vertex (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, real NG, the number of nodes to generate,
#    as determined by pyramid_grid_size().
#
#    Output, real XG[Ng,3], the grid point coordinates.
#
  import numpy as np

  xg = np.zeros ( ( ng, 3 ) );

  g = 0

  for k in range ( n, -1, -1 ):
    hi = n - k
    lo = - hi
    for j in range ( lo, hi + 1, 2 ):
      for i in range ( lo, hi + 1, 2 ):
        xg[g,0] = float ( i ) / float ( n )
        xg[g,1] = float ( j ) / float ( n )
        xg[g,2] = float ( k ) / float ( n )
        g = g + 1

  return xg

def pyramid_grid_points_test ( ):

#*****************************************************************************80
#
#% PYRAMID_GRID_POINTS_TEST tests PYRAMID_GRID_POINTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PYRAMID_GRID_POINTS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PYRAMID_GRID_POINTS determines a unit pyramid' )
  print ( '  grid with N+1 points along each edge.' )

  n = 4

  print ( '' )
  print ( '  Grid parameter N = %d' % ( n ) )

  ng = pyramid_grid_count ( n )

  print ( '' )
  print ( '  Grid size NG = %d' % ( ng ) )

  xg = pyramid_grid_points ( n, ng )

  r83col_print_part ( ng, xg, 20, '  Pyramid grid points:' )
#
#  Write the data to a file.
#
  filename = 'pyramid_grid_points.xyz'
  r8mat_write ( filename, ng, 3, xg )

  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )
#
#  Plot the data.
#
  filename = 'pyramid_grid_points.png'
  pyramid_grid_display ( ng, xg, filename )

  print ( '' )
  print ( '  Plot written to the file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PYRAMID_GRID_POINTS_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def pyramid_grid_test ( ):

#*****************************************************************************80
#
## PYRAMID_GRID_TEST tests the PYRAMIDE_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PYRAMID_GRID_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the PYRAMID_GRID library.' )
#
#  Utilities:
#
  r83col_print_part_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  pyramid_grid_count_test ( )
  pyramid_grid_display_test ( )
  pyramid_grid_points_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'PYRAMID_GRID_TEST:' )
  print ( '  Normal end of execution.' )
  return

def pyramid_unit_vertices ( ):

#*****************************************************************************80
#
## PYRAMID_UNIT_VERTICES returns the vertices of the unit pyramid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real V1(3), V2(3), V3(3), V4(3), V5(3), the vertices.
#
  import numpy as  np

  v1 = np.array ( [  0.0,  0.0, +1.0 ] )
  v2 = np.array ( [ -1.0, -1.0,  0.0 ] )
  v3 = np.array ( [ +1.0, -1.0,  0.0 ] )
  v4 = np.array ( [ +1.0, +1.0,  0.0 ] )
  v5 = np.array ( [ -1.0, +1.0,  0.0 ] )

  return v1, v2, v3, v4, v5

def r83col_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## R83COL_PRINT_PART prints "part" of an R83COL.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vector.
#
#    Input, real A(N,3), the vector to be printed.
#
#    Input, integer MAX_PRINT, the maximum number of lines
#    to print.
#
#    Input, string TITLE, a title.
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
## R83COL_PRINT_PART_TEST tests R83COL_PRINT_PART.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R83COL_PRINT_PART_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R83COL_PRINT_PART prints part of an R83COL.' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'R83COL_PRINT_PART_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## R8MAT_WRITE writes an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
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
## R8MAT_WRITE_TEST tests R8MAT_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R8MAT_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test R8MAT_WRITE, which writes an R8MAT to a file.' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  pyramid_grid_test ( )
  timestamp ( )

