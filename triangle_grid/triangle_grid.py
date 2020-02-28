#! /usr/bin/env python3
#
def r82col_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## R82COL_PRINT_PART prints "part" of an R82COL.
#
#  Discussion:
#
#    An R82COL is an (N,2) array of R8's.
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
#    19 December 2001
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vector.
#
#    Input, real A(N,2), the vector to be printed.
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
          print ( '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] ) )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print ( '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] ) )
        print ( '  ....  ..............  ..............' )
        i = n - 1
        print ( '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] ) )

      else:

        for i in range ( 0, max_print - 1 ):
          print ( '  %4d  %14g  %14g' % ( i, a[i,0], a[i,1] ) )
        i = max_print - 1
        print ( '  %4d  %14g  %14g  ...more entries...' % ( i, a[i,0], a[i,1] ) )

  return

def r82col_print_part_test ( ):

#*****************************************************************************80
#
## R82COL_PRINT_PART_TEST tests R82COL_PRINT_PART.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R82COL_PRINT_PART_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R82COL_PRINT_PART prints an R82COL.' )

  n = 10

  v = np.array ( [ \
    [  11,  12 ], \
    [  21,  22 ], \
    [  31,  32 ], \
    [  41,  42 ], \
    [  51,  52 ], \
    [  61,  62 ], \
    [  71,  72 ], \
    [  81,  82 ], \
    [  91,  92 ], \
    [ 101, 102 ] ] )

  max_print = 2
  r82col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 2' )

  max_print = 5
  r82col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 5' )

  max_print = 25
  r82col_print_part ( n, v, max_print, '  Output with MAX_PRINT = 25' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R82COL_PRINT_PART_TEST:' )
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

def triangle_grid_count ( n ):

#*****************************************************************************80
#
## TRIANGLE_GRID_COUNT counts the grid points inside a triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Output, integer NG, the number of grid points inside the triangle.
#
  ng = ( ( n + 1 ) * ( n + 2 ) ) // 2

  return ng

def triangle_grid_count_test ( ):

#*****************************************************************************80
#
## TRIANGLE_GRID_COUNT_TEST tests TRIANGLE_GRID_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRIANGLE_GRID_COUNT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_GRID_COUNT can count the points in a triangular grid' )
  print ( '  with N+1 points on a side, based on any triangle.' )

  print ( '' )
  print ( '     N        NG' )
  print ( '' )

  for n in [ 1, 2, 3, 4, 5, 10, 15, 20, 25, 50, 100 ]:
    ng = triangle_grid_count ( n )
    print ( '  %4d  %8d' % ( n, ng ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_GRID_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def triangle_grid_display ( t, ng, tg, filename ):

#*****************************************************************************80
#
## TRIANGLE_GRID_DISPLAY displays grid points inside a triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   09 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T(3,2), the coordinates of the vertices of the triangle.
#
#    Input, integer NG, the number of grid points inside the triangle.
#
#    Input, real TG(NG,2), the grid points.
#
#    Input, string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Plot the outline of the triangle.
#
  tx = np.zeros ( 4 )
  ty = np.zeros ( 4 )

  tx[0] = t[0,0];
  tx[1] = t[1,0];
  tx[2] = t[2,0];
  tx[3] = t[0,0];
  ty[0] = t[0,1];
  ty[1] = t[1,1];
  ty[2] = t[2,1];
  ty[3] = t[0,1];

  plt.plot ( tx, ty, linewidth = 2.0, color = 'r' )
#
#  Plot the gridpoints.
#
  plt.plot ( tg[0:ng,0], tg[0:ng,1], 'bs' )
#
#  Cleanup and annotate.
#
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Grid points in triangle' )
  plt.grid ( True )
  plt.axis ( 'equal' )

  plt.savefig ( filename )

  plt.show ( block = False )
  plt.clf ( )

  print ( '' )
  print ( '  Graphics data saved in file "%s"' % (filename ) )

  return

def triangle_grid_display_test ( ):

#*****************************************************************************80
#
## TRIANGLE_GRID_DISPLAY displays grid points inside a triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TRIANGLE_GRID_DISPLAY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_GRID_DISPLAY displays a grid of points in a triangle.' )

  t = np.array ( [ \
    [ 1.0, 3.0 ], \
    [ 6.0, 4.0 ], \
    [ 3.0, 8.0 ] ] )

  ng = 11
  tg = np.array ( [ \
    [ 2.0, 4.0 ], \
    [ 3.0, 4.0 ], \
    [ 4.0, 4.0 ], \
    [ 5.0, 4.0 ], \
    [ 2.0, 5.0 ], \
    [ 3.0, 5.0 ], \
    [ 4.0, 5.0 ], \
    [ 5.0, 5.0 ], \
    [ 3.0, 6.0 ], \
    [ 4.0, 6.0 ], \
    [ 3.0, 7.0 ] ] )

  filename = 'triangle_grid_display.png'

  triangle_grid_display ( t, ng, tg, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_GRID_DISPLAY_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def triangle_grid_points ( n, t ):

#*****************************************************************************80
#
## TRIANGLE_GRID_POINTS computes points on a triangular grid.
#
#  Discussion:
#
#    The grid is defined by specifying the coordinates of an enclosing
#    triangle T, and the number of subintervals each side of the triangle
#    should be divided into.
#
#    Choosing N = 10, for instance, breaks each side into 10 subintervals,
#    and produces a grid of ((10+1)*(10+2))/2 = 66 points.
#
#              X
#             9 X
#            8 9 X
#           7 8 9 X
#          6 7 8 9 X
#         5 6 7 8 9 X
#        4 5 6 7 8 9 X
#       3 4 5 6 7 8 9 X
#      2 3 4 5 6 7 8 9 X
#     1 2 3 4 5 6 7 8 9 X
#    0 1 2 3 4 5 6 7 8 9 X
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, real T[3,2], the coordinates of the points
#    defining the triangle.
#
#    Output, real TG[NG,2], the coordinates
#    of the points in the triangle.
#
  import numpy as np

  ng = ( ( n + 1 ) * ( n + 2 ) ) // 2
  tg = np.zeros ( ( ng, 2 ) )

  p = 0

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 - i ):

      tg[p,0] = ( float (     i     ) * t[0,0]   \
                + float (         j ) * t[1,0]   \
                + float ( n - i - j ) * t[2,0] ) \
                / float ( n )

      tg[p,1] = ( float (     i     ) * t[0,1]   \
                + float (         j ) * t[1,1]   \
                + float ( n - i - j ) * t[2,1] ) \
                / float ( n )
      p = p + 1

  return tg

def triangle_grid_points_test ( n ):

#*****************************************************************************80
#
## TRIANGLE_GRID_POINTS_TEST tests TRIANGLE_GRID_POINTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TRIANGLE_GRID_POINTS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_GRID_POINTS defines a triangular grid' )
  print ( '  with N+1 points on a side, based on any triangle.' )

  print ( '' )
  print ( '  Input value of N is %d' % ( n ) )

  ng = triangle_grid_count ( n )
  print ( '  Number of grid points will be %d' % ( ng ) )

  t = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.5, 0.86602540378443860 ] ] )

  r8mat_print ( 3, 2, t, '  Triangle vertices:' )

  tg = triangle_grid_points ( n, t )

  r82col_print_part ( ng, tg, 20, '  Part of the grid point array:' );
#
#  Write the data to a file.
#
  filename = 'triangle_grid_points.xy'

  r8mat_write ( filename, ng, 2, tg )
#
#  Plot the data.
#
  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )

  filename = 'triangle_grid_points.png'
  triangle_grid_display ( t, ng, tg, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_GRID_POINTS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def triangle_grid_test ( ):

#*****************************************************************************80
#
## TRIANGLE_GRID_TEST tests the TRIANGLE_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRIANGLE_GRID_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TRIANGLE_GRID library.' )
#
#  Utilities:
#
  r82col_print_part_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  triangle_grid_display_test ( )
  triangle_grid_count_test ( )
  triangle_grid_points_test ( 15 )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_GRID_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  triangle_grid_test ( )
  timestamp ( )

