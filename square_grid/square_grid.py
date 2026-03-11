#! /usr/bin/env python3
#
def r82col_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## r82col_print_part() prints "part" of an R82COL.
#
#  Discussion:
#
#    An R82COL is an (N,2) array of R8's.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 December 2001
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(N,2), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
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

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
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
  
def square_grid_count ( ns ):

#*****************************************************************************80
#
## square_grid_count() counts grid points in a quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NS(2), the number of intervals along each dimension.
#
#  Output:
#
#    integer NG, the number of grid points.
#
  ng = ( ns[0] + 1 ) * ( ns[1] + 1 )

  return ng

def square_grid_display ( xv, ng, xg, filename ):

#*****************************************************************************80
#
## square_grid_display() displays grid points inside a quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#   10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real XV(4,2), the coordinates of the vertices.
#
#    integer NG, the number of grid points.
#
#    real XG(NG,2), the grid points.
#
#    string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Plot the outline.
#
  qx = np.zeros ( 5 )
  qy = np.zeros ( 5 )

  qx[0] = xv[0,0]
  qx[1] = xv[1,0]
  qx[2] = xv[2,0]
  qx[3] = xv[3,0]
  qx[4] = xv[0,0]

  qy[0] = xv[0,1]
  qy[1] = xv[1,1]
  qy[2] = xv[2,1]
  qy[3] = xv[3,1]
  qy[4] = xv[0,1]

  plt.plot ( qx, qy, linewidth = 2.0, color = 'r' )
#
#  Plot the gridpoints.
#
  plt.plot ( xg[0:ng,0], xg[0:ng,1], 'bs' )
#
#  Cleanup and annotate.
#
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Grid points in quadrilateral' )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def square_grid_display_test ( ):

#*****************************************************************************80
#
## square_grid_display() displays grid points inside a quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'square_grid_display_test():' )
  print ( '  square_grid_display() displays a grid of points in a quadrilateral.' )

  xv = np.array ( [ \
    [ 2.0, 1.0 ], \
    [ 5.0, 4.0 ], \
    [ 3.0, 6.0 ], \
    [ 0.0, 3.0 ] ] )

  ng = 18
  xg = np.array ( [ \
    [ 2.0, 1.0 ], \
    [ 1.0, 2.0 ], \
    [ 2.0, 2.0 ], \
    [ 3.0, 2.0 ], \
    [ 0.0, 3.0 ], \
    [ 1.0, 3.0 ], \
    [ 2.0, 3.0 ], \
    [ 3.0, 3.0 ], \
    [ 4.0, 3.0 ], \
    [ 1.0, 4.0 ], \
    [ 2.0, 4.0 ], \
    [ 3.0, 4.0 ], \
    [ 4.0, 4.0 ], \
    [ 5.0, 4.0 ], \
    [ 2.0, 5.0 ], \
    [ 3.0, 5.0 ], \
    [ 4.0, 5.0 ], \
    [ 3.0, 6.0 ] ] )

  filename = 'square_grid_display.png'

  square_grid_display ( xv, ng, xg, filename )

  return
  
def square_grid_points ( ns, xv, ng ):

#*****************************************************************************80
#
## square_grid_points(): grid points over a quadrilateral.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NS[2], the number of points along each dimension.
#
#    real XV[4,2], the vertices, in counter clockwise order.
#
#    integer NG, the number of points.
#    NG = NS[0] * NS[1].
#
#  Output:
#
#    real XG[NG,2], the grid points.
#
  import numpy as np
#
#  Create the 1D grids in each dimension.
#
  xg = np.zeros ( ( ng, 2 ) )

  m = ns[0]
  n = ns[1]

  ig = 0
  for j in range ( 0, n + 1 ):
    for i in range ( 0, m + 1 ):
      a0 = float ( ( m - i ) * ( n - j ) ) / float ( m * n )
      a1 = float ( (     i ) * ( n - j ) ) / float ( m * n )
      a2 = float ( (     i ) * (     j ) ) / float ( m * n )
      a3 = float ( ( m - i ) * (     j ) ) / float ( m * n )
      xg[ig,0] = a0 * xv[0,0] + a1 * xv[1,0] + a2 * xv[2,0] + a3 * xv[3,0]
      xg[ig,1] = a0 * xv[0,1] + a1 * xv[1,1] + a2 * xv[2,1] + a3 * xv[3,1]
      ig = ig + 1

  return xg

def square_grid_points_test ( m, n ):

#*****************************************************************************80
#
## square_grid_points_test() tests square_grid_points().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'square_grid_points_test():' )
  print ( '  square_grid_points() defines a grid' )
  print ( '  with M*N points on a side, based on a quadrilateral.' )

  print ( '' )
  print ( '  Input value of M is %d' % ( m ) )
  print ( '  Input value of N is %d' % ( n ) )

  ns = np.zeros ( 2, dtype = np.int32 );
  ns[0] = m
  ns[1] = n

  ng = square_grid_count ( ns )

  print ( '' )
  print ( '  Number of grid points will be %d' % ( ng ) )

  xv = np.array ( [ \
    [ 0.0, 1.0 ], \
    [ 3.0, 2.0 ], \
    [ 4.0, 5.0 ], \
    [ 1.0, 3.0 ] ] )

  r8mat_print ( 4, 2, xv, '  Quadrilateral vertices:' )

  xg = square_grid_points ( ns, xv, ng )

  r82col_print_part ( ng, xg, 20, '  Part of the grid point array:' );
#
#  Write the data to a file.
#
  filename = 'square_grid_points.xy'
  r8mat_write ( filename, ng, 2, xg )

  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )
#
#  Plot the data.
#
  filename = 'square_grid_points.png'
  square_grid_display ( xv, ng, xg, filename )

  return

def square_grid_test ( ):

#*****************************************************************************80
#
## square_grid_test() tests square_grid().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'square_grid_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test square_grid().' )

  square_grid_display_test ( )
  square_grid_points_test ( 10, 8 )
#
#  Terminate.
#
  print ( '' )
  print ( 'square_grid_test():' )
  print ( '  Normal end of execution.' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  square_grid_test ( )
  timestamp ( )

