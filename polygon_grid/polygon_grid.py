#! /usr/bin/env python3
#
def polygon_grid_count ( n, nv ):

#*****************************************************************************80
#
## POLYGON_GRID_COUNT counts the grid points inside a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals on a side.
#
#    Input, integer NV, the number of vertices.
#    3 <= NV.
#
#    Output, integer NG, the number of grid points.
#
  ng = 1 + nv * ( n * ( n + 1 ) ) // 2

  return ng

def polygon_grid_count_test ( ):

#*****************************************************************************80
#
## POLYGON_GRID_COUNT_TEST tests POLYGON_GRID_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'POLYGON_GRID_COUNT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_GRID_COUNT counts NG, the number of points in' )
  print ( '  a grid defined with N+1 points on each side of a' )
  print ( '  polygon of NV vertices.' )

  for nv in range ( 3, 6 ):
    print ( '' )
    print ( '  Polygonal vertex count NV = %d' % ( nv ) )
    print ( '' )
    print ( '   N     NG' )
    print ( '' )
    for n in range ( 0, 6 ):
      ng = polygon_grid_count ( n, nv )
      print ( '  %2d  %5d' % ( n, ng ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_GRID_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def polygon_grid_display ( n, nv, v, ng, xg, filename ):

#*****************************************************************************80
#
## POLYGON_GRID_DISPLAY displays grid points inside a polygon.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, integer NV, the number of vertices in the polygon.
#
#    Input, real V[NV,2], the coordinates of the vertices.
#
#    Input, integer NG, the number of grid points.
#
#    Input, real XG[NG,2], the grid points.
#
#    Input, string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Determine the centroid.
#
  vcx = 0.0
  vcy = 0.0
  for i in range ( 0, nv ):
    vcx = vcx + v[i,0]
    vcy = vcy + v[i,1]
  vcx = vcx / float ( nv )
  vcy = vcy / float ( nv )
#
#  Plot the outline of the polygon.
#
  plt.plot ( v[0:nv,0], v[0:nv,1], linewidth = 2.0, color = 'r' )
  plt.plot ( [ v[nv-1,0], v[0,0] ], [ v[nv-1,1], v[0,1] ], linewidth = 2.0, color = 'r' )
#
#  Plot the internal "ribs"
#
  for i in range ( 0, nv ):
    plt.plot ( [ v[i,0], vcx ], [ v[i,1], vcy ], linewidth = 2.0, color = 'k' )
#
#  Plot the gridpoints.
#
  plt.plot ( xg[0:ng,0], xg[0:ng,1], 'bs' )
#
#  Cleanup and annotate.
#
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Grid points in polygon' )
  plt.grid ( True )
  plt.axis ( 'equal' )
# plt.show ( block = False )
#
#  Save plot to file.
#
  plt.savefig ( filename )

  plt.clf ( )

  print ( '' )
  print ( '  Graphics data saved in file "%s"' % ( filename ) )

  return

def polygon_grid_display_test ( ):

#*****************************************************************************80
#
## POLYGON_GRID_DISPLAY_TEST tests POLYGON_GRID_DISPLAY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'POLYGON_GRID_DISPLAY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_GRID_DISPLAY displays a grid of points in a polygon.' )

  n = 2

  nv = 4
  v = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 2.0, 1.0 ], \
    [ 1.0, 1.0 ] ] )

  ng = 13
  xg = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 0.5, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.5, 0.25 ], \
    [ 1.0, 0.25 ], \
    [ 0.5, 0.5 ], \
    [ 1.0, 0.5 ], \
    [ 1.5, 0.5 ], \
    [ 1.0, 0.75 ], \
    [ 1.5, 0.75 ], \
    [ 1.0, 1.0 ], \
    [ 1.5, 1.0 ], \
    [ 2.0, 1.0 ] ] )

  filename = 'polygon_grid_display_test.png'

  polygon_grid_display ( n, nv, v, ng, xg, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_GRID_DISPLAY_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def polygon_grid_points ( n, nv, v, ng ):

#*****************************************************************************80
#
## POLYGON_GRID_POINTS computes points on a polygonal grid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, integer NV, the number of vertices in the polygon.
#
#    Input, real V[NV,2], the coordinates of the vertices.
#
#    Input, integer NG, the number of grid points.
#
#    Output, real XG[NG,2], the coordinates of the grid points.
#
  import numpy as np

  xg = np.zeros ( [ ng, 2 ] )
  p = 0
#
#  Determine the centroid.
#
  vc = np.zeros ( 2 )
  for i in range ( 0, nv ):
    vc[0] = vc[0] + v[i,0]
    vc[1] = vc[1] + v[i,1]
  vc[0] = vc[0] / float ( nv )
  vc[1] = vc[1] / float ( nv )
#
#  Use the centroid as the first grid point.
#
  xg[p,0] = vc[0]
  xg[p,1] = vc[1]
  p = p + 1
#
#  Consider each triangle formed by two consecutive vertices and the centroid,
#  but skip the first line of points.
#
  for l in range ( 0, nv ):
    lp1 = ( l % nv )
    for i in range ( 1, n + 1 ):
      for j in range ( 0, n - i + 1 ):
        k = n - i - j
        xg[p,0] = ( float ( i ) * v[l,0] \
                  + float ( j ) * v[lp1,0] \
                  + float ( k ) * vc[0] ) \
                  / float ( n )
        xg[p,1] = ( float ( i ) * v[l,1] \
                  + float ( j ) * v[lp1,1] \
                  + float ( k ) * vc[1] ) \
                  / float ( n )
        p = p + 1

  return xg

def polygon_grid_points_test01 ( ):

#*****************************************************************************80
#
## POLYGON_GRID_POINTS_TEST01 tests POLYGON_GRID_POINTS
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'POLYGON_GRID_POINTS_TEST01:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_GRID_POINTS returns grid points for a polygon' )
  print ( '  of NV vertices, with N+1 points on a side' )
  print ( '' )
  print ( '  For this test, the polygon is a triangle.' )
#
#  Define the polygon.
#
  nv = 3
  v = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.5, 0.86602540378443860 ] ] )

  r8mat_print ( nv, 2, v, '  Polygon vertices:' )
#
#  Count the grid points.
#
  n = 5
  ng = polygon_grid_count ( n, nv )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '  Number of grid points will be NG = %d' % ( ng ) )
#
#  Compute the grid points.
#
  xg = polygon_grid_points ( n, nv, v, ng )

  r8mat_print ( ng, 2, xg, '  The grid point array:' )
#
#  Display the points.
#
  filename = 'triangle.png'

  polygon_grid_display ( n, nv, v, ng, xg, filename )
#
#  Write the points to a file.
#
  filename = 'triangle.xy'

  r8mat_write ( filename, ng, 2, xg )

  print ( '' )
  print ( '  Data written to the file "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_GRID_POINTS_TEST01:' )
  print ( '  Normal end of execution.' )
  return

def polygon_grid_points_test02 ( ):

#*****************************************************************************80
#
## POLYGON_GRID_POINTS_TEST02 tests POLYGON_GRID_POINTS
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'POLYGON_GRID_POINTS_TEST02:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_GRID_POINTS returns grid points for a polygon' )
  print ( '  of NV vertices, with N+1 points on a side' )
  print ( '' )
  print ( '  For this test, the polygon is a convex quadrilateral' )
  print ( '  with sides of varying length.' )
#
#  Define the polygon.
#
  nv = 4
  v = np.array ( [ \
    [ 1.0, 1.0 ], \
    [ 2.0, 0.0 ], \
    [ 4.0, 3.0 ], \
    [ 0.0, 5.0 ] ] )

  r8mat_print ( nv, 2, v, '  Polygon vertices:' )
#
#  Count the grid points.
#
  n = 7
  ng = polygon_grid_count ( n, nv )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '  Number of grid points will be NG = %d' % ( ng ) )
#
#  Compute the grid points.
#
  xg = polygon_grid_points ( n, nv, v, ng )

  r8mat_print ( ng, 2, xg, '  The grid point array:' )
#
#  Display the points.
#
  filename = 'quad.png'

  polygon_grid_display ( n, nv, v, ng, xg, filename )
#
#  Write the points to a file.
#
  filename = 'quad.xy'

  r8mat_write ( filename, ng, 2, xg )

  print ( '' )
  print ( '  Data written to the file "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_GRID_POINTS_TEST02:' )
  print ( '  Normal end of execution.' )
  return

def polygon_grid_points_test03 ( ):

#*****************************************************************************80
#
## POLYGON_GRID_POINTS_TEST03 tests POLYGON_GRID_POINTS
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'POLYGON_GRID_POINTS_TEST03:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_GRID_POINTS returns grid points for a polygon' )
  print ( '  of NV vertices, with N+1 points on a side' )
  print ( '' )
  print ( '  For this test, the polygon is nonconvex and six sided.' )
  print ( '  Two degenerate triangles are created, and some grid points' )
  print ( '  are generated several times.' )
#
#  Define the polygon.
#
  nv = 6
  v = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 2.0, 0.0 ], \
    [ 2.0, 1.0 ], \
    [ 1.0, 1.0 ], \
    [ 1.0, 2.0 ], \
    [ 0.0, 2.0 ] ] )

  r8mat_print ( nv, 2, v, '  Polygon vertices:' )
#
#  Count the grid points.
#
  n = 5
  ng = polygon_grid_count ( n, nv )

  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '  Number of grid points will be NG = %d' % ( ng ) )
#
#  Compute the grid points.
#
  xg = polygon_grid_points ( n, nv, v, ng )

  r8mat_print ( ng, 2, xg, '  The grid point array:' )
#
#  Display the points.
#
  filename = 'ell.png'

  polygon_grid_display ( n, nv, v, ng, xg, filename )
#
#  Write the points to a file.
#
  filename = 'ell.xy'

  r8mat_write ( filename, ng, 2, xg )

  print ( '' )
  print ( '  Data written to the file "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_GRID_POINTS_TEST03:' )
  print ( '  Normal end of execution.' )
  return

def polygon_grid_test ( ):

#*****************************************************************************80
#
## POLYGON_GRID_TEST tests the POLYGON_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'POLYGON_GRID_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the POLYGON_GRID library.' )
#
#  Utilities.
#
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_write_test ( )
#
#  Library.
#
  polygon_grid_count_test ( )

  polygon_grid_display_test ( )

  polygon_grid_points_test01 ( )
  polygon_grid_points_test02 ( )
  polygon_grid_points_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_GRID_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
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
  polygon_grid_test ( )
  timestamp ( )

