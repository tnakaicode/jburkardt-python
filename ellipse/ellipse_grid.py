#! /usr/bin/env python3
#
def ellipse_grid_count ( n, r, c ):

#*****************************************************************************80
#
## ELLIPSE_GRID_COUNT counts the grid points inside an ellipse.
#
#  Discussion:
#
#    The ellipse is specified as
#
#      ( ( X - C1 ) / R1 )^2 + ( ( Y - C2 ) / R2 )^2 = 1
#
#    The user supplies a number N.  There will be N+1 grid points along
#    the shorter axis.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, real R(2), the half axis lengths.
#
#    Input, real C(2), the center of the ellipse.
#
#    Output, integer NG, the number of grid points inside the ellipse.
#
  import numpy as np

  if ( r[0] < r[1] ):
    h = 2.0 * r[0] / float ( 2 * n + 1 )
    ni = n
    nj = np.ceil ( r[1] / r[0] ) * n
  else:
    h = 2.0 * r[1] / float ( 2 * n + 1 )
    nj = n
    ni = np.ceil ( r[0] / r[1] ) * n

  ng = 0

  for j in range ( 0, nj + 1 ):
    i = 0
    x = c[0]
    y = c[1] + float ( j ) * h
    ng = ng + 1
    if ( 0 < j ):
      ng = ng + 1

    while ( True ):
      i = i + 1
      x = c[0] + float ( i ) * h
      if ( 1 < ( ( x - c[0] ) / r[0] ) ** 2 + ( ( y - c[1] ) / r[1] ) ** 2 ):
        break
      ng = ng + 1
      ng = ng + 1
      if ( 0 < j ):
        ng = ng + 1
        ng = ng + 1

  return ng

def ellipse_grid_count_test ( ):

#*****************************************************************************80
#
## ELLIPSE_GRID_COUNT_TEST tests ELLIPSE_GRID_COUNT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ELLIPSE_GRID_COUNT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPSE_GRID_COUNT can count the points in a grid,' )
  print ( '  with N+1 points on the minor half axis,' )
  print ( '  based on any ellipse.' )

  n = 8
  r = np.array ( [ 2.0, 1.0 ] )
  c = np.array ( [ 1.0, 2.0 ] )

  print ( '' )
  print ( '  We use N = %d' % ( n ) )
  print ( '  Radius R = (%g,%g)' % ( r[0], r[1] ) )
  print ( '  Center C = (%g,%g)' % ( c[0], c[1] ) )

  ng = ellipse_grid_count ( n, r, c )

  print ( '' )
  print ( '  Number of grid points will be %d' % ( ng ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPSE_GRID_COUNT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def ellipse_grid_display ( n, r, c, ng, cg, filename ):

#*****************************************************************************80
#
## ELLIPSE_GRID_DISPLAY displays grid points inside an ellipse.
#
#  Discussion:
#
#    The ellipse is specified as
#
#      ( ( X - C1 ) / R1 )^2 + ( ( Y - C2 ) / R2 )^2 = 1
#
#    The user supplies a number N.  There will be N+1 grid points along
#    the shorter axis.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, real R(2), the half axis lengths.
#
#    Input, real C(2), the center of the ellipse.
#
#    Input, integer NG, the number of grid points inside the ellipse.
#
#    Input, real XY(2,NG), the grid points.
#
#    Input, string FILENAME, the name of the plotfile to be created.
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
    cx[i] = c[0] + r[0] * np.cos ( t )
    cy[i] = c[1] + r[1] * np.sin ( t )

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
  plt.title ( 'Grid points in ellipse' )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.clf ( )

  print ( '' )
  print ( '  Graphics data saved in file "%s"' % (filename ) )

  return

def ellipse_grid_display_test ( ):

#*****************************************************************************80
#
## ELLIPSE_GRID_DISPLAY_TEST tests ELLIPSE_GRID_DISPLAY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ELLIPSE_GRID_DISPLAY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPSE_GRID_DISPLAY can display a grid of points in an ellipse.' )

  n = 3
  r = np.array ( [ 3.0, 2.0 ] )
  c = np.array ( [ 3.0, 0.0 ] )
  ng = 19
  cg = np.array ( [ \
    [  3.0,  2.0 ], \
    [  1.0,  1.0 ], \
    [  2.0,  1.0 ], \
    [  3.0,  1.0 ], \
    [  4.0,  1.0 ], \
    [  5.0,  1.0 ], \
    [  0.0,  0.0 ], \
    [  1.0,  0.0 ], \
    [  2.0,  0.0 ], \
    [  3.0,  0.0 ], \
    [  4.0,  0.0 ], \
    [  5.0,  0.0 ], \
    [  6.0,  0.0 ], \
    [  1.0, -1.0 ], \
    [  2.0, -1.0 ], \
    [  3.0, -1.0 ], \
    [  4.0, -1.0 ], \
    [  5.0, -1.0 ], \
    [  3.0, -2.0 ]  ] )

  cg = np.transpose ( cg )
  filename = 'ellipse_grid_display.png'

  ellipse_grid_display ( n, r, c, ng, cg, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPSE_GRID_DISPLAY_TEST:' )
  print ( '  Normal end of execution.' )
  return

def ellipse_grid_points ( n, r, c, ng ):

#*****************************************************************************80
#
## ELLIPSE_GRID_POINTS generates grid points inside an ellipse.
#
#  Discussion:
#
#    The ellipse is specified as
#
#      ( ( X - C1 ) / R1 )^2 + ( ( Y - C2 ) / R2 )^2 = 1
#
#    The user supplies a number N.  There will be N+1 grid points along
#    the shorter axis.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of subintervals.
#
#    Input, real R(2), the half axis lengths.
#
#    Input, real C(2), the center of the ellipse.
#
#    Input, integer NG, the number of grid points inside the ellipse.
#
#    Output, real XY(2,NG), the grid points.
#
  import numpy as np

  if ( r[0] < r[1] ):
    h = 2.0 * r[0] / float ( 2 * n + 1 )
    ni = n
    nj = np.ceil ( r[1] / r[0] ) * n
  else:
    h = 2.0 * r[1] / float ( 2 * n + 1 )
    nj = n
    ni = np.ceil ( r[0] / r[1] ) * n

  p = 0
  xy = np.zeros ( [ 2, ng ] )

  for j in range ( 0, nj + 1 ):
    i = 0
    x = c[0]
    y = c[1] + float ( j ) * h

    xy[0,p] = x
    xy[1,p] = y
    p = p + 1
    if ( 0 < j ):
      xy[0,p] = x
      xy[1,p] = 2.0 * c[1] - y
      p = p + 1

    while ( True ):
      i = i + 1
      x = c[0] + float ( i ) * h
      if ( 1.0 < ( ( x - c[0] ) / r[0] ) ** 2 + ( ( y - c[1] ) / r[1] ) ** 2 ):
        break

      xy[0,p] = x
      xy[1,p] = y
      p = p + 1
      xy[0,p] = 2.0 * c[0] - x
      xy[1,p] = y
      p = p + 1
      if ( 0 < j ):
        xy[0,p] = x
        xy[1,p] = 2.0 * c[1] - y
        p = p + 1
        xy[0,p] = 2.0 * c[0] - x
        xy[1,p] = 2.0 * c[1] - y
        p = p + 1

  return xy

def ellipse_grid_points_test ( ):

#*****************************************************************************80
#
#% ELLIPSE_GRID_POINTS_TEST tests ELLIPSE_GRID_POINTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ELLIPSE_GRID_POINTS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ELLIPSE_GRID_POINTS can define a grid of points' )
  print ( '  with N+1 points on the minor half axis,' )
  print ( '  based on any ellipse.' )

  n = 8
  r = np.array ( [ 2.0, 1.0 ] )
  c = np.array ( [ 1.0, 2.0 ] )

  print ( '' )
  print ( '  We use N = %d' % ( n ) )
  print ( '  Radius R = (%g,%g)' % ( r[0], r[1] ) )
  print ( '  Center C = (%g,%g)' % ( c[0], c[1] ) )

  ng = ellipse_grid_count ( n, r, c )

  print ( '' )
  print ( '  Number of grid points will be %d' % ( ng ) )

  cg = ellipse_grid_points ( n, r, c, ng )

  r82vec_print_part ( ng, cg, 20, '  Part of the grid point array:' )
#
#  Write grid points to a file.
#
  filename = 'ellipse_grid.xy'

  r8mat_transpose_write ( filename, 2, ng, cg );

  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )
#
#  Plot the grid, and save the plot in a file.
#
  filename = 'ellipse_grid.png'
  ellipse_grid_display ( n, r, c, ng, cg, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPSE_GRID_POINTS_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def ellipse_grid_test ( ):

#*****************************************************************************80
#
## ELLIPSE_GRID_TEST tests the ELLIPSE_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ELLIPSE_GRID_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the ELLIPSE_GRID library.' )
#
#  Utilities:
#
  r82vec_print_part_test ( )
  r8mat_transpose_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  ellipse_grid_display_test ( )
  ellipse_grid_count_test ( )
  ellipse_grid_points_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ELLIPSE_GRID_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r82vec_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## R82VEC_PRINT_PART prints "part" of an R82VEC.
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
#    Input, real A(2,N), the vector to be printed.
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
## R82VEC_PRINT_PART_TEST tests R82VEC_PRINT_PART.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R82VEC_PRINT_PART_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R82VEC_PRINT_PART prints an R8VEC.' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'R82VEC_PRINT_PART_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_write ( filename, m, n, a ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_WRITE writes the transpose of an R8MAT to a file.
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
## R8MAT_TRANSPOSE_WRITE_TEST tests R8MAT_TRANSPOSE_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8MAT_TRANSPOSE_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test R8MAT_TRANSPOSE_WRITE, which writes the transpose of an R8MAT to a file.' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_WRITE_TEST:' )
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
  ellipse_grid_test ( )
  timestamp ( )

