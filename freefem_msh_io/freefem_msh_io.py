#! /usr/bin/env python3
#
def freefem_mesh_2d_data_example ( v_num, e_num, t_num ):

#*****************************************************************************80
#
## freefem_mesh_2d_data_example() returns example freefem_mesh data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer V_NUM, the number of vertices.
#
#    integer E_NUM, the number of boundary edges.
#
#    integer T_NUM, the number of triangles.
#
#  Output:
#
#    real V_XY(2,V_NUM), vertex coordinates.
#
#    integer V_L(V_NUM), vertex labels.
#
#    integer E_V(2,E_NUM), edge vertices.
#
#    integer E_L(E_NUM), vertex labels.
#
#    integer T_V(3,T_NUM), triangle vertices.
#
#    integer T_L(T_NUM), triangle labels.
#
  import numpy as np

  v_l = np.array ( [ \
    1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1 ] );

  v_xy = np.array ( [ \
    [ -0.309016994375,  0.951056516295 ], \
    [ -0.809016994375,  0.587785252292 ], \
    [ -0.321175165867,  0.475528256720 ], \
    [  0.309016994375,  0.951056516295 ], \
    [ -1.000000000000,  0.000000000000 ], \
    [  0.809016994375,  0.587785252292 ], \
    [ -0.333333334358,  0.000000000000 ], \
    [  0.237841829972,  0.293892623813 ], \
    [ -0.809016994375, -0.587785252292 ], \
    [ -0.321175165867, -0.475528259963 ], \
    [  1.000000000000,  0.000000000000 ], \
    [  0.206011327827, -0.391856835534 ], \
    [ -0.309016994375, -0.951056516295 ], \
    [  0.809016994375, -0.587785252292 ], \
    [  0.309016994375, -0.951056516295 ] \
  ] )

  v_xy = v_xy.T

  e_l = np.array ( [ \
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] )

  e_v = np.array ( [ \
    [ 11,  6 ], \
    [  6,  4 ], \
    [  4,  1 ], \
    [  1,  2 ], \
    [  2,  5 ], \
    [  5,  9 ], \
    [  9, 13 ], \
    [ 13, 15 ], \
    [ 15, 14 ], \
    [ 14, 11 ] \
  ] )

  e_v = e_v.T

  t_l = np.array ( [ \
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] )

  t_v = np.array ( [ \
    [   1,  3,  4 ], \
    [   7,  2,  5 ], \
    [   9,  7,  5 ], \
    [   8,  6,  4 ], \
    [  12,  8,  7 ], \
    [  12, 11,  8 ], \
    [   3,  1,  2 ], \
    [   7,  3,  2 ], \
    [   7,  8,  3 ], \
    [   4,  3,  8 ], \
    [   6,  8, 11 ], \
    [  12,  7, 10 ], \
    [  11, 12, 14 ], \
    [  10,  9, 13 ], \
    [  12, 10, 13 ], \
    [   7,  9, 10 ], \
    [  12, 13, 15 ], \
    [  14, 12, 15 ] \
  ] )

  t_v = t_v.T

  return v_xy, v_l, e_v, e_l, t_v, t_l

def freefem_mesh_2d_data_print ( title, v_num, e_num, t_num, v_xy, v_l, e_v, \
  e_l, t_v, t_l ):

#*****************************************************************************80
#
## freefem_mesh_2d_data_print() prints freefem_mesh data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string TITLE, a title.
#
#    integer V_NUM, the number of vertices.
#
#    integer E_NUM, the number of boundary edges.
#
#    integer T_NUM, the number of triangles.
#
#    real V_XY(2,V_NUM), vertex coordinates.
#
#    integer V_L(V_NUM), vertex labels.
#
#    integer E_V(2,E_NUM), edge vertices.
#
#    integer E_L(E_NUM), vertex labels.
#
#    integer T_V(3,T_NUM), triangle vertices.
#
#    integer T_L(T_NUM), triangle labels.
#
  print ( '' )
  print ( title )
  
  i4vec_print (              v_num, v_l,  '  Vertex labels:' )
  r8mat_transpose_print ( 2, v_num, v_xy, '  Vertex coordinates:' )
  i4vec_print (              e_num, e_l,  '  Edge labels:' )
  i4mat_transpose_print ( 2, e_num, e_v,  '  Edge vertices:' )
  i4vec_print (              t_num, t_l,  '  Triangle labels:' )
  i4mat_transpose_print ( 3, t_num, t_v,  '  Triangle vertices:' )

  return

def freefem_mesh_2d_data_read ( freefem_mesh_filename, v_num, e_num, t_num ):

#*****************************************************************************80
#
## freefem_mesh_2d_data_read() reads data from an freefem_mesh file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string freefem_mesh_FILENAME, the freefem_mesh filename.
#
#    integer V_NUM, the number of vertices.
#
#    integer E_NUM, the number of boundary edges.
#
#    integer T_NUM, the number of triangles.
#
#  Output:
#
#    real V_XY(2,V_NUM), vertex coordinates.
#
#    integer V_L(V_NUM), vertex labels.
#
#    integer E_V(2,E_NUM), edge vertices.
#
#    integer E_L(E_NUM), vertex labels.
#
#    integer T_V(3,T_NUM), triangle vertices.
#
#    integer T_L(T_NUM), triangle labels.
#
  import numpy as np

  freefem_mesh_unit = open ( freefem_mesh_filename, 'r' )

  line = freefem_mesh_unit.readline ( )
  words = line.strip().split()
  v_num2 = int ( words[0] )
  t_num2 = int ( words[1] )
  e_num2 = int ( words[2] )
#
#  Read Vertex X, Y, Label
#
  v_xy = np.zeros ( [ 2, v_num ] )
  v_l = np.zeros ( v_num )

  for j in range ( 0, v_num ):
    line = freefem_mesh_unit.readline ( )
    words = line.strip().split()
    v_xy[0,j] = float ( words[0] )
    v_xy[1,j] = float ( words[1] )
    v_l[j] = int ( words[2] )
#
#  Read Triangle V1, V2, V3, Label
#
  t_v = np.zeros ( [3, t_num ] )
  t_l = np.zeros ( t_num )

  for j in range ( 0, t_num ):
    line = freefem_mesh_unit.readline ( )
    words = line.strip().split()
    t_v[0,j] = int ( words[0] )
    t_v[1,j] = int ( words[1] )
    t_v[2,j] = int ( words[2] )
    t_l[j] = int ( words[3] )
#
#  Read Edge V1, V2, Label
#
  e_v = np.zeros ( [ 2, e_num ] )
  e_l = np.zeros ( e_num )

  for j in range ( 0, e_num ):
    line = freefem_mesh_unit.readline ( )
    words = line.strip().split()
    e_v[0,j] = int ( words[0] )
    e_v[1,j] = int ( words[1] )
    e_l[j] = int ( words[2] )

  freefem_mesh_unit.close ( )

  return v_xy, v_l, e_v, e_l, t_v, t_l

def freefem_mesh_2d_size_example ( ):

#*****************************************************************************80
#
## freefem_mesh_2d_size_example() returns sizes for the 2D example.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer V_NUM, the number of vertices.
#
#    integer E_NUM, the number of boundary edges.
#
#    integer T_NUM, the number of triangles.
#
  e_num = 10
  t_num = 18
  v_num = 15

  return v_num, e_num, t_num

def freefem_mesh_2d_size_print ( title, v_num, e_num, t_num ):

#*****************************************************************************80
#
## freefem_mesh_2d_size_print() prints the sizes of an freefem_mesh.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string TITLE, a title.
#
#    integer V_NUM, the number of vertices.
#
#    integer E_NUM, the number of boundary edges.
#
#    integer T_NUM, the number of triangles.
#
  print ( '' )
  print ( title )
  print ( '' )
  print ( '  Number of vertices = %d' % ( v_num ) )
  print ( '  Number of boundary edges = %d' % ( e_num ) )
  print ( '  Number of triangles = %d' % ( t_num ) )

  return

def freefem_mesh_2d_size_read ( freefem_mesh_filename ):

#*****************************************************************************80
#
## freefem_mesh_2d_size_read() reads sizes from a freefem_mesh file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string freefem_mesh_FILENAME, the freefem_mesh filename.
#
#  Output:
#
#    integer V_NUM, the number of vertices.
#
#    integer E_NUM, the number of boundary edges.
#
#    integer T_NUM, the number of triangles.
#
  freefem_mesh_unit = open ( freefem_mesh_filename, 'r' )

  line = freefem_mesh_unit.readline ( )

  words = line.strip().split()

  v_num = int ( words[0] )
  t_num = int ( words[1] )
  e_num = int ( words[2] )

  freefem_mesh_unit.close ( )

  return v_num, e_num, t_num

def freefem_mesh_2d_write ( freefem_mesh_filename, v_num, e_num, t_num, v_xy, v_l, \
  e_v, e_l, t_v, t_l ):

#*****************************************************************************80
#
## freefem_mesh_2d_write() writes freefem_mesh data to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string freefem_mesh_FILENAME, the name of the file.
#
#    integer V_NUM, the number of vertices.
#
#    integer E_NUM, the number of boundary edges.
#
#    integer T_NUM, the number of triangles.
#
#    real V_XY(2,V_NUM), vertex coordinates.
#
#    integer V_L(V_NUM), vertex labels.
#
#    integer E_V(2,E_NUM), edge vertices.
#
#    integer E_L(E_NUM), vertex labels.
#
#    integer T_V(3,T_NUM), triangle vertices.
#
#    integer T_L(T_NUM), triangle labels.
#

#
#  Open the file.
#
  freefem_mesh_unit = open ( freefem_mesh_filename, 'wt' )
#
#  Write the data.
#
  freefem_mesh_unit.write ( \
    repr ( v_num ) + '  ' \
  + repr ( t_num ) + '  ' \
  + repr ( e_num ) + '\n' )

  for j in range ( 0, v_num ):
    freefem_mesh_unit.write ( \
      repr ( v_xy[0,j] ) + '  ' \
    + repr ( v_xy[1,j] ) + '  ' \
    + repr ( v_l[j] ) + '\n' )

  for j in range ( 0, t_num ):
    freefem_mesh_unit.write ( \
      repr ( t_v[0,j] ) + '  ' \
    + repr ( t_v[1,j] ) + '  ' \
    + repr ( t_v[2,j] ) + '  ' 
    + repr ( t_l[j] )   + '\n' )

  for j in range ( 0, e_num ):
    freefem_mesh_unit.write ( \
      repr ( e_v[0,j] ) + '  ' \
    + repr ( e_v[1,j] ) + '  ' \
    + repr ( e_l[j] )   + '\n' )

  freefem_mesh_unit.close ( )

  return

def i4mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## i4mat_transpose_print() prints an I4MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2014
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
#    integer A(M,N), the matrix.
#
#    string TITLE, a title.
#
  i4mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_transpose_print_test ( ):

#*****************************************************************************80
#
## i4mat_transpose_print_test() tests i4mat_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import plaform

  print ( '' )
  print ( 'i4mat_transpose_print_test():' )
  print ( '  i4mat_transpose_print() prints an I4MAT, tranposed.' )

  m = 5
  n = 3
  a = np.array ( ( \
    ( 11, 12, 13 ), \
    ( 21, 22, 23 ), \
    ( 31, 32, 33 ), \
    ( 41, 42, 43 ), \
    ( 51, 52, 53 ) ) )
  title = '  A 5 x 3 integer matrix:'
  i4mat_transpose_print ( m, n, a, title )

  return

def i4mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## i4mat_transpose_print_some() prints a portion of an I4MAT, transposed.
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
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer A(M,N), an M by N matrix to be printed.
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

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ' ),

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d  ' % ( i ) ),

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( ' %4d: ' % ( j ) ),
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%7d  ' % ( a[i,j] ) ),

      print ( '' )

  return

def i4mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## i4mat_transpose_print_some_test() tests i4mat_transpose_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'i4mat_transpose_print_some_test():' )
  print ( '  i4mat_transpose_print_some() prints some of an I4MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, \
    '  Here is I4MAT, rows 0:2, cols 3:5:' )

  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print() prints an I4VEC.
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
#    integer N, the dimension of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_test ( ):

#*****************************************************************************80
#
## i4vec_print_test() tests i4vec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_print_test():' )
  print ( '  i4vec_print() prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )

  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_transpose_print() prints an R8MAT, transposed.
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
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_test() tests r8mat_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8mat_transpose_print_test():' )
  print ( '  r8mat_transpose_print() prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )

  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_transpose_print_some() prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2014
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

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ' ),

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ) ),

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ) ),
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

      print ( '' )

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_some_test() tests r8mat_transpose_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8mat_transpose_print_some_test():' )
  print ( '  r8mat_transpose_print_some() prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )

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

def freefem_mesh_io_test ( ):

#*****************************************************************************80
#
## freefem_mesh_io_test() tests freefem_mesh_io().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'freefem_mesh_io_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test freefem_mesh_io().' )
  print ( '' )

  freefem_mesh_io_test01 ( )
  freefem_mesh_io_test02 ( )
  freefem_mesh_io_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'freefem_mesh_io_test():' )
  print ( '  Normal end of execution.' )
  return

def freefem_mesh_io_test01 ( ):

#*****************************************************************************80
#
## freefem_mesh_io_test01() gets the example 2D data and prints it.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'freefem_mesh_io_test01:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Get example 2D data and print it.' )
#
#  Get the sizes.
#
  v_num, e_num, t_num = freefem_mesh_2d_size_example ( )
#
#  Print the sizes.
#
  freefem_mesh_2d_size_print ( '  Example Sizes:', v_num, e_num, t_num )
#
#  Get the data.
#
  [ v_xy, v_l, e_v, e_l, t_v, t_l ] \
    = freefem_mesh_2d_data_example ( v_num, e_num, t_num )
#
#  Print the data.
#
  freefem_mesh_2d_data_print ( '  Example data:', v_num, e_num, t_num, v_xy, \
    v_l, e_v, e_l, t_v, t_l )

  return

def freefem_mesh_io_test02 ( ):

#*****************************************************************************80
#
## freefem_mesh_io_test02() gets the example 2D data and writes it to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'freefem_mesh_io_test02:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Get example 2D data and write it to a file.' )
#
#  Get the sizes.
#
  v_num, e_num, t_num = freefem_mesh_2d_size_example ( );
#
#  Print the sizes.
#
  freefem_mesh_2d_size_print ( '  Example Sizes:', v_num, e_num, t_num )
#
#  Get the data.
#
  v_xy, v_l, e_v, e_l, t_v, t_l \
    = freefem_mesh_2d_data_example ( v_num, e_num, t_num )
#
#  Write the sizes and data.
#
  filename = 'output.msh'

  freefem_mesh_2d_write ( filename, v_num, e_num, t_num, v_xy, \
    v_l, e_v, e_l, t_v, t_l )

  print ( '' )
  print ( '  The data was written to "%s"' % ( filename ) )

  return

def freefem_mesh_io_test03 ( ):

#*****************************************************************************80
#
## freefem_mesh_io_test03() gets the example 2D data and prints it.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  filename = 'input.msh'

  print ( '' )
  print ( 'freefem_mesh_io_test03:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Read 2D data from a file and print it.' )
#
#  Read the sizes.
#
  v_num, e_num, t_num = freefem_mesh_2d_size_read ( filename )
#
#  Print the sizes.
#
  freefem_mesh_2d_size_print ( filename, v_num, e_num, t_num )
#
#  Read the data.
#
  v_xy, v_l, e_v, e_l, t_v, t_l \
    = freefem_mesh_2d_data_read ( filename, v_num, e_num, t_num )
#
#  Print the data.
#
  freefem_mesh_2d_data_print ( filename, v_num, e_num, t_num, v_xy, \
    v_l, e_v, e_l, t_v, t_l )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  freefem_mesh_io_test ( )
  timestamp ( )

