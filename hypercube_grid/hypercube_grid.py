#! /usr/bin/env python3
#
def hypercube_grid_points ( m, n, ns, a, b, c ):

#*****************************************************************************80
#
## hypercube_grid_points(): grid points in a hypercube in M dimensions.
#
#  Discussion:
#
#    In M dimensional space, a logically rectangular grid is to be created.
#    In the I-th dimension, the grid will use S(I) points.
#    The total number of grid points is 
#      N = product ( 1 <= I <= M ) S(I)
#
#    Over the interval [A(i),B(i)], we have 5 choices for grid centering:
#      1: 0,   1/3, 2/3, 1
#      2: 1/5, 2/5, 3/5, 4/5
#      3: 0,   1/4, 2/4, 3/4
#      4: 1/4, 2/4, 3/4, 1
#      5: 1/8, 3/8, 5/8, 7/8
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of points.
#    N = product ( 1 <= I <= M ) NS(I).
#
#    integer NS(M), the number of points along 
#    each dimension.
#
#    real A(M), B(M), the endpoints for each dimension.
#
#    integer C(M), the grid centering for each dimension.
#    1 <= C(*) <= 5.
#
#  Output:
#
#    real X(M,N) = X(M*S(1),S(2),...,S(M)), the points.
#
  import numpy as np
#
#  Create the 1D grids in each dimension.
#
  x = np.zeros ( ( m, n ) )

  contig = 0
  rep = 0
  skip = 0

  for i in range ( 0, m ): 

    s = ns[i]

    xs = np.zeros ( s )

    for j in range ( 0, s ):

      if ( c[i] == 1 ):

        if ( s == 1 ):
          xs[j] = 0.5 * ( a[i] + b[i] )
        else:
          xs[j] = (   ( s - j     ) * a[i]   \
                    + (     j - 1 ) * b[i] ) \
                    / ( s     - 1 )
      elif ( c[i] == 2 ):
        xs[j] = (   ( s - j + 1 ) * a[i]   \
                  + (     j     ) * b[i] ) \
                  / ( s     + 1 )
      elif ( c[i] == 3 ):
        xs[j] = (   ( s - j + 1 ) * a[i]   \
                  + (     j - 1 ) * b[i] ) \
                  / ( s         )
      elif ( c[i] == 4 ):
        xs[j] = (   ( s - j ) * a[i]   \
                  + (     j ) * b[i] ) \
                  / ( s     )
      elif ( c[i] == 5 ):
        xs[j] = (   ( 2 * s - 2 * j + 1 ) * a[i]   \
                  + (         2 * j - 1 ) * b[i] ) \
                  / ( 2 * s             )

    x, contig, rep, skip = \
      r8vec_direct_product ( i, s, xs, m, n, x, contig, rep, skip )

  return x

def hypercube_grid_points_test01 ( ):

#*****************************************************************************80
#
## hypercube_grid_test01() tests hypercube_grid on a two dimensional example.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 2

  a = np.array ( [ 0.0, 0.0 ] )
  b = np.array ( [ 1.0, 10.0 ] )
  c = np.array ( [ 2, 4 ] )
  ns = np.array ( [ 4, 5 ] )

  n = np.prod ( ns )

  print ( '' )
  print ( 'hypercube_grid_points_test01' )
  print ( '  hypercube_grid_points creates a grid of points in a hypercube.' )
  print ( '  Spatial dimension M = %d' % (m ) )
  print ( '  Number of grid points N = %d' % ( n ) )
  print ( '' )
  print ( '     I    NS     C      A         B' )
  print ( '' )
  for i in range ( 0, m ):
    print ( '  %4d  %4d  %4d  %8.4f  %8.4f' % ( i, ns[i], c[i], a[i], b[i] ) )

  x = hypercube_grid_points ( m, n, ns, a, b, c )
#
#  Transpose the data.
#
  x = np.transpose ( x )
#
#  Print the points.
#
  r8mat_print ( n, m, x, '  Grid points:' )
#
#  Write the data to a file.
#
  filename = 'hypercube_grid_points_test01.xyz'
  r8mat_write ( filename, n, m, x )
  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )

  return

def hypercube_grid_points_test02 ( ):

#*****************************************************************************80
#
## hypercube_grid_test02() tests hypercube_grid on a five dimensional example.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5

  a = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  b = np.array ( [ 1.0, 1.0, 1.0, 1.0, 1.0 ] )
  c = np.array ( [ 1, 2, 3, 4, 5 ] )
  ns = np.array ( [ 2, 2, 2, 2, 2 ] )

  n = np.prod ( ns )

  print ( '' )
  print ( 'hypercube_grid_points_test02():' )
  print ( '  hypercube_grid_points() creates a grid of points in a hypercube.' )
  print ( '  Spatial dimension M = %d' % (m ) )
  print ( '  Number of grid points N = %d' % ( n ) )
  print ( '' )
  print ( '     I    NS     C      A         B' )
  print ( '' )
  for i in range ( 0, m ):
    print ( '  %4d  %4d  %4d  %8.4f  %8.4f' % ( i, ns[i], c[i], a[i], b[i] ) )

  x = hypercube_grid_points ( m, n, ns, a, b, c )
#
#  Transpose the data.
#
  x = np.transpose ( x )
#
#  Print the points.
#
  r8mat_print ( n, m, x, '  Grid points:' )
#
#  Write the data to a file.
#
  filename = 'hypercube_grid_points_test02.xyz'
  r8mat_write ( filename, n, m, x )
  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )

  return

def hypercube_grid_points_test03 ( ):

#*****************************************************************************80
#
## hypercube_grid_test03() tests hypercube_grid on a three dimensional example.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 3

  a = np.array ( [ -1.0, -1.0, -1.0 ] )
  b = np.array ( [ +1.0, +1.0, +1.0 ] )
  c = np.array ( [ 1, 1, 1 ] )
  ns = np.array ( [ 3, 3, 3 ] )

  n = np.prod ( ns )

  print ( '' )
  print ( 'hypercube_grid_points_test03():' )
  print ( '  hypercube_grid_points creates a grid of points in a hypercube.' )
  print ( '  Spatial dimension M = %d' % (m ) )
  print ( '  Number of grid points N = %d' % ( n ) )
  print ( '' )
  print ( '     I    NS     C      A         B' )
  print ( '' )
  for i in range ( 0, m ):
    print ( '  %4d  %4d  %4d  %8.4f  %8.4f' % ( i, ns[i], c[i], a[i], b[i] ) )

  x = hypercube_grid_points ( m, n, ns, a, b, c )
#
#  Transpose the data.
#
  x = np.transpose ( x )
#
#  Print the points.
#
  r8mat_print ( n, m, x, '  Grid points:' )
#
#  Write the data to a file.
#
  filename = 'hypercube_grid_points_test03.xyz'
  r8mat_write ( filename, n, m, x )
  print ( '' )
  print ( '  Data written to the file "%s".' % ( filename ) )

  return

def hypercube_grid_test ( ):

#*****************************************************************************80
#
## hypercube_grid_test() tests hypercube_grid().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hypercube_grid_test' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hypercube_grid().' )
#
#  Library.
#
  hypercube_grid_points_test01 ( )
  hypercube_grid_points_test02 ( )
  hypercube_grid_points_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hypercube_grid_test():' )
  print ( '  Normal end of execution.' )

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
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
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
  
def r8vec_direct_product ( factor_index, factor_order, \
  factor_value, factor_num, point_num, x, contig, rep, skip ):

#*****************************************************************************80
#
## r8vec_direct_product() creates a direct product of R8VEC's.
#
#  Discussion:
#
#    To explain what is going on here, suppose we had to construct
#    a multidimensional quadrature rule as the product of K rules
#    for 1D quadrature.
#
#    The product rule will be represented as a list of points and weights.
#
#    The J-th item in the product rule will be associated with
#      item J1 of 1D rule 1,
#      item J2 of 1D rule 2, 
#      ..., 
#      item JK of 1D rule K.
#
#    In particular, 
#      X(J) = ( X(1,J1), X(2,J2), ..., X(K,JK))
#    and
#      W(J) = W(1,J1) * W(2,J2) * ... * W(K,JK)
#
#    So we can construct the quadrature rule if we can properly
#    distribute the information in the 1D quadrature rules.
#
#    This routine carries out that task.
#
#    Another way to do this would be to compute, one by one, the
#    set of all possible indices (J1,J2,...,JK), and then index
#    the appropriate information.  An advantage of the method shown
#    here is that you can process the K-th set of information and
#    then discard it.
#
#  Example:
#
#    Rule 1: 
#      Order = 4
#      X(1:4) = ( 1, 2, 3, 4 )
#
#    Rule 2:
#      Order = 3
#      X(1:3) = ( 10, 20, 30 )
#
#    Rule 3:
#      Order = 2
#      X(1:2) = ( 100, 200 )
#
#    Product Rule:
#      Order = 24
#      X(1:24) = 
#        ( 1, 10, 100 )
#        ( 2, 10, 100 )
#        ( 3, 10, 100 )
#        ( 4, 10, 100 )
#        ( 1, 20, 100 )
#        ( 2, 20, 100 )
#        ( 3, 20, 100 )
#        ( 4, 20, 100 )
#        ( 1, 30, 100 )
#        ( 2, 30, 100 )
#        ( 3, 30, 100 )
#        ( 4, 30, 100 )
#        ( 1, 10, 200 )
#        ( 2, 10, 200 )
#        ( 3, 10, 200 )
#        ( 4, 10, 200 )
#        ( 1, 20, 200 )
#        ( 2, 20, 200 )
#        ( 3, 20, 200 )
#        ( 4, 20, 200 )
#        ( 1, 30, 200 )
#        ( 2, 30, 200 )
#        ( 3, 30, 200 )
#        ( 4, 30, 200 )
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
#    integer FACTOR_INDEX, the index of the factor being processed.
#    The first factor processed must be factor 1#
#
#    integer FACTOR_ORDER, the order of the factor.
#
#    real FACTOR_VALUE(FACTOR_ORDER), the factor values
#    for factor FACTOR_INDEX.
#
#    integer FACTOR_NUM, the number of factors.
#
#    integer POINT_NUM, the number of elements in the direct product.
#
#    real X(FACTOR_NUM,POINT_NUM), the elements of the
#    direct product.  The user should not set or alter this value.
#
#    integer CONTIG, the number of consecutive values to set.
#    The user should not set or alter this value.
#
#    integer SKIP, the distance from the current value of START
#    to the next location of a block of values to set.
#    The user should not set or alter this value.
#
#    integer REP, the number of blocks of values to set.
#    The user should not set or alter this value.
#
#  Output:
#
#    real X(FACTOR_NUM,POINT_NUM), the updated elements of the
#    direct product.
#
#    integer CONTIG, the number of consecutive values to set.
#
#    integer SKIP, the distance from the current value of START
#    to the next location of a block of values to set.
#
#    integer REP, the number of blocks of values to set.
#
#  Local:
#
#    integer START, the first location of a block of values to set.
#
  import numpy as np

  if ( factor_index == 0 ):
    contig = 1
    skip = 1
    rep = point_num

  rep = ( rep // factor_order )
  skip = skip * factor_order

  for j in range ( 0, factor_order ):

    start = j * contig

    for k in range ( 0, rep ):
      for l in range ( start, start + contig ):
        x[factor_index,l] = factor_value[j]
      start = start + skip

  contig = contig * factor_order

  return x, contig, rep, skip

def r8vec_direct_product_test ( ):

#*****************************************************************************80
#
## r8vec_direct_product_test() tests r8vec_direct_product().
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

  factor_num = 3
  point_num = 24

  print ( '' )
  print ( 'r8vec_direct_product_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_direct_product forms the entries of a' )
  print ( '  direct product of a given number of R8VEC factors.' )

  x = np.zeros ( ( factor_num, point_num ) )
  contig = 0
  skip = 0
  rep = 0

  for factor_index in range ( 0, factor_num ):

    if ( factor_index == 0 ):
      factor_order = 4
      factor_value = np.array ( [ 1.0, 2.0, 3.0, 4.0 ] )
    elif ( factor_index == 1 ):
      factor_order = 3
      factor_value = np.array ( [ 50.0, 60.0, 70.0 ] )
    elif ( factor_index == 2 ):
      factor_order = 2
      factor_value = np.array ( [ 800.0, 900.0 ] )
  
    x, contig, rep, skip = r8vec_direct_product ( factor_index, factor_order, \
      factor_value, factor_num, point_num, x, contig, rep, skip );

  r8mat_transpose_print ( factor_num, point_num, x, '  Matrix (transposed)' )

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
  hypercube_grid_test ( )
  timestamp ( )

