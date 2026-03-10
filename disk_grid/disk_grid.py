#! /usr/bin/env python3
#
def disk_grid_display ( n, r, c, ng, cg, filename ):

#*****************************************************************************80
#
## disk_grid_display() displays grid points inside a disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 September 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of subintervals.
#
#    real R, the radius of the disk.
#
#    real C(2), the coordinates of the center of the disk.
#
#    integer NG, the number of grid points inside the disk.
#
#    real CG(2,NG), the grid points.
#
#    string FILENAME, the name of the plotfile to be created.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Make points on the circumference and plot them.
#
  cx = np.zeros ( 51 )
  cy = np.zeros ( 51 )
  for i in range ( 0, 51 ):
    t = 2.0 * np.pi * float ( i ) / 50.0
    cx[i] = c[0] + r * np.cos ( t )
    cy[i] = c[1] + r * np.sin ( t )

  plt.plot ( cx, cy, linewidth = 2.0, color = 'r' )
#
#  Plot the gridpoints.
#
  plt.plot ( cg[0,0:ng], cg[1,0:ng], 'bs' )
#
#  Cleanup and annotate.
#
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---Y--->' )
  plt.title ( 'Grid points in circle' )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '' )
  print ( '  Graphics data saved in file "%s"' % (filename ) )

  return

def disk_grid_display_test ( ):

#*****************************************************************************80
#
## disk_grid_display_test() tests disk_grid_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk_grid_display_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  disk_grid_display() displays a grid of points in a disk.' )

  n = 1
  r = 2.0
  c = np.array ( [ 0.0, 0.0 ] )
  ng = 9
  cg = np.array ( [ \
    [ -1.0,  1.0 ], \
    [  0.0,  1.0 ], \
    [  1.0,  1.0 ], \
    [ -1.0,  0.0 ], \
    [  0.0,  0.0 ], \
    [  1.0,  0.0 ], \
    [ -1.0, -1.0 ], \
    [  0.0, -1.0 ], \
    [  1.0, -1.0 ] ] )

  cg = np.transpose ( cg )
  filename = 'disk_grid_display.png'

  disk_grid_display ( n, r, c, ng, cg, filename )

  return
  
def disk_grid_fibonacci ( n, r, c ):

#*****************************************************************************80
#
## disk_grid_fibonacci() computes Fibonacci grid points inside a disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Swinbank, James Purser,
#    Fibonacci grids: A novel approach to global modelling,
#    Quarterly Journal of the Royal Meteorological Society,
#    Volume 132, Number 619, July 2006 Part B, pages 1769-1793.
#
#  Input:
#
#    integer N, the number of points desired.
#
#    real R, the radius of the disk.
#
#    real C(2), the coordinates of the center of the disk.
#
#  Output:
#
#    real CG(2,N), the grid points.
#
  import numpy as np

  r0 = r / np.sqrt ( float ( n ) - 0.5 )
  phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0

  gr = np.zeros ( n )
  gt = np.zeros ( n )
  for i in range ( 0, n ):
    gr[i] = r0 * np.sqrt ( i + 0.5 );
    gt[i] = 2.0 * np.pi * float ( i + 1 ) / phi

  cg = np.zeros ( ( 2, n ) )

  for i in range ( 0, n ):
    cg[0,i] = c[0] + gr[i] * np.cos ( gt[i] )
    cg[1,i] = c[1] + gr[i] * np.sin ( gt[i] )

  return cg

def disk_grid_fibonacci_test ( ):

#*****************************************************************************80
#
## disk_grid_fibonacci_test() tests disk_grid_fibonacci().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk_grid_fibonacci_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  disk_grid_fibonacci can define a grid of N points' )

  n = 1000
  r = 2.0
  c = np.array ( [ 1.0, 5.0 ] )

  print ( '' )
  print ( '  We use N = %d' % ( n ) )
  print ( '  Radius R = %g' % ( r ) )
  print ( '  Center C = (%g,%g)' % ( c[0], c[1] ) )

  ng = n
  cg = disk_grid_fibonacci ( n, r, c );

  r82vec_print_part ( n, cg, 20, '  Part of the grid point array:' );
#
#  Write grid points to a file.
#
  filename = 'disk_grid_fibonacci.xy'

  r8mat_transpose_write ( filename, 2, ng, cg )

  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )
#
#  Plot the grid, and save the plot in a file.
#
  filename = 'disk_grid_fibonacci.png'
  disk_grid_display ( n, r, c, ng, cg, filename )

  return

def disk_grid_test ( ):

#*****************************************************************************80
#
## disk_grid_test() tests disk_grid().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'disk_grid_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test disk_grid().' )
#
#  Utilities:
#
  r82vec_print_part_test ( )
  r8mat_transpose_write_test ( )
#
#  Library.
#
  disk_grid_display_test ( )
  disk_grid_regular_count_test ( )
  disk_grid_regular_test ( )
  disk_grid_fibonacci_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk_grid_test():' )
  print ( '  Normal end of execution.' )
  return

def disk_grid_regular_count ( n, r, c ):

#*****************************************************************************80
#
## disk_grid_regular_count() counts the grid points inside a disk.
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the disk,
#    and the number of subintervals N into which the horizontal radius
#    should be divided.  Thus, a value of N = 2 will result in 5 points
#    along that horizontal line.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of subintervals.
#
#    real R, the radius of the disk.
#
#    real C(2), the coordinates of the center of the disk.
#
#  Output:
#
#    integer NG, the number of grid points inside the disk.
#
  ng = 0

  for j in range ( 0, n + 1 ):

    i = 0
    x = c[0]
    y = c[1] + r * float ( 2 * j ) / float ( 2 * n + 1 )
    ng = ng + 1
    if ( 0 < j ):
      ng = ng + 1

    while ( True ):

      i = i + 1
      x = c[0] + r * float ( 2 * i ) / float ( 2 * n + 1 )

      if ( r * r < ( x - c[0] ) ** 2 + ( y - c[1] ) ** 2 ):
        break

      ng = ng + 1
      ng = ng + 1

      if ( 0 < j ):
        ng = ng + 1
        ng = ng + 1

  return ng

def disk_grid_regular_count_test ( ):

#*****************************************************************************80
#
## disk_grid_regular_count_test() tests disk_grid_regular_count().
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the disk,
#    and the number of subintervals N into which the horizontal radius
#    should be divided.  Thus, a value of N = 2 will result in 5 points
#    along that horizontal line.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk_grid_regular_count_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  disk_grid_regular_count counts the number of grid points needed' )
  print ( '  for a regular grid of points in a disk.' )

  print ( '' )
  print ( '  N = number of subintervals of the horizontal radius.' )
  print ( '  NG = resulting number of grid points.' )
  print ( '' )
  print ( '     N        NG' )
  print ( '' )

  for n in [ 1, 2, 4, 8, 16  ]:
    r = 1.0
    c = np.array ( [ 0.0, 0.0 ] )
    ng = disk_grid_regular_count ( n, r, c )
    print ( '  %4d  %8d' % ( n, ng ) )

  return
 
def disk_grid_regular ( n, r, c, ng ):

#*****************************************************************************80
#
## disk_grid_regular() computes grid points inside a disk.
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the disk,
#    and the number of subintervals N into which the horizontal radius
#    should be divided.  Thus, a value of N = 2 will result in 5 points
#    along that horizontal line.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of subintervals.
#
#    real R, the radius of the disk.
#
#    real C(2), the coordinates of the center of the disk.
#
#    integer NG, the number of grid points, as determined by
#    disk_grid_count.
#
#  Output:
#
#    real CG(2,NG), the grid points inside the disk.
#
  import numpy as np

  cg = np.zeros ( [ 2, ng ] )

  p = 0

  for j in range ( 0, n + 1 ):

    i = 0
    x = c[0]
    y = c[1] + r * float ( 2 * j ) / float ( 2 * n + 1 )
    cg[0,p] = x
    cg[1,p] = y
    p = p + 1

    if ( 0 < j ):

      cg[0,p] = x
      cg[1,p] = 2.0 * c[1] - y
      p = p + 1

    while ( True ):

      i = i + 1
      x = c[0] + r * float ( 2 * i ) / float ( 2 * n + 1 )
      if ( r * r < ( x - c[0] ) ** 2 + ( y - c[1] ) ** 2 ):
        break

      cg[0,p] = x
      cg[1,p] = y
      p = p + 1
      cg[0,p] = 2.0 * c[0] - x
      cg[1,p] = y
      p = p + 1

      if ( 0 < j ):
        cg[0,p] = x
        cg[1,p] = 2.0 * c[1] - y
        p = p + 1;
        cg[0,p] = 2.0 * c[0] - x
        cg[1,p] = 2.0 * c[1] - y
        p = p + 1

  return cg

def disk_grid_regular_test ( ):

#*****************************************************************************80
#
## disk_grid_regular_test() tests disk_grid_regular().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk_grid_regular_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  disk_grid_regular can define a grid of points' )
  print ( '  with N+1 points on a horizontal or vertical radius,' )
  print ( '  based on any disk.' )

  n = 20
  r = 2.0
  c = np.array ( [ 1.0, 5.0 ] )

  print ( '' )
  print ( '  We use N = %d' % ( n ) )
  print ( '  Radius R = %g' % ( r ) )
  print ( '  Center C = (%g,%g)' % ( c[0], c[1] ) )

  ng = disk_grid_regular_count ( n, r, c )

  print ( '' )
  print ( '  Number of grid points will be %d' % ( ng ) )

  cg = disk_grid_regular ( n, r, c, ng )

  r82vec_print_part ( ng, cg, 20, '  Part of the grid point array:' )
#
#  Write grid points to a file.
#
  filename = 'disk_grid_regular.xy'

  r8mat_transpose_write ( filename, 2, ng, cg )

  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )
#
#  Plot the grid, and save the plot in a file.
#
  filename = 'disk_grid_regular.png'
  disk_grid_display ( n, r, c, ng, cg, filename )

  return
  
def r82vec_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## r82vec_print_part() prints "part" of an R82VEC.
#
#  Discussion:
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
#    real A(2,N), the vector to be printed.
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
          print ( '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] ) )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print ( '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] ) )
        print ( '  ....  ..............  ..............' )
        i = n - 1
        print ( '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] ) )

      else:

        for i in range ( 0, max_print - 1 ):
          print ( '  %4d  %14f  %14f' % ( i, a[0,i], a[1,i] ) )
        i = max_print - 1
        print ( '  %4d  %14f  %14f  ...more entries...' % ( i, a[0,i], a[1,i] ) )

  return

def r82vec_print_part_test ( ):

#*****************************************************************************80
#
## r82vec_print_part_test() tests r82vec_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R82VEC_PRINT_part_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R82VEC_PRINT_part prints an R8VEC.' )

  n = 10

  v = np.array ( [ \
    [  11,  12, 13, 14, 15, 16, 17, 18, 19, 20 ], \
    [  21,  22, 23, 24, 25, 26, 27, 28, 29, 30 ] ] )

  max_print = 2
  r82vec_print_part ( n, v, max_print, '  Output with MAX_PRINT = 2' )

  max_print = 5
  r82vec_print_part ( n, v, max_print, '  Output with MAX_PRINT = 5' )

  max_print = 25
  r82vec_print_part ( n, v, max_print, '  Output with MAX_PRINT = 25' )

  return

def r8mat_transpose_write ( filename, m, n, a ):

#*****************************************************************************80
#
## r8mat_transpose_write() writes the transpose of an R8MAT to a file.
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

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8mat_transpose_write_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_write_test() tests r8mat_transpose_write().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_transpose_write_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test r8mat_transpose_write, which writes the transpose of an R8MAT to a file.' )

  filename = 'r8mat_transpose_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 1.1, 1.2, 1.3 ), \
    ( 2.1, 2.2, 2.3 ), \
    ( 3.1, 3.2, 3.3 ), \
    ( 4.1, 4.2, 4.3 ), \
    ( 5.1, 5.2, 5.3 ) ) )
  r8mat_transpose_write ( filename, m, n, a )

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

if ( __name__ == '__main__' ):
  timestamp ( )
  disk_grid_test ( )
  timestamp ( )
