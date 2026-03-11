#! /usr/bin/env python3
#
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
  import platform

  print ( '' )
  print ( 'r8mat_transpose_print_test' )
  print ( '  r8mat_transpose_print prints an R8MAT.' )

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
  import platform

  print ( '' )
  print ( 'r8mat_transpose_print_some_test' )
  print ( '  r8mat_transpose_print_some prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )

  return

def simplex01_volume ( m ):

#*****************************************************************************80
#
## simplex01_volume() returns the volume of the unit simplex in M dimensions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real VALUE, the volume.
#
  value = 1.0
  for i in range ( 1, m + 1 ):
    value = value / float ( i )

  return value

def simplex01_volume_test ( ) :

#*****************************************************************************80
#
## simplex01_volume_test() tests simplex01_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'simplex01_volume_test' )
  print ( '  simplex01_volume returns the volume of the unit simplex' )
  print ( '  in M dimensions.' )
  print ( '' )
  print ( '   M   Volume' )
  print ( '' )

  for m in range ( 1, 10 ):
    value = simplex01_volume ( m )
    print ( '  %2d  %g' % ( m, value ) )

  return

def simplex_coordinates1 ( m ):

#*****************************************************************************80
#
## simplex_coordinates1() computes the Cartesian coordinates of simplex vertices.
#
#  Discussion:
#
#    The simplex will have its centroid at 0
#
#    The sum of the vertices will be zero.
#
#    The distance of each vertex from the origin will be 1.
#
#    The length of each edge will be constant.
#
#    The dot product of the vectors defining any two vertices will be - 1 / M.
#    This also means the angle subtended by the vectors from the origin
#    to any two distinct vertices will be arccos ( - 1 / M ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real X(M,M+1), the coordinates of the vertices
#    of a simplex in M dimensions.
#
  import numpy as np

  x = np.zeros ( [ m, m + 1 ] )

  for k in range ( 0, m ):
#
#  Set X(K,K) so that sum ( X(1:K,K)^2 ) = 1.
#
    s = 0.0
    for i in range ( 0, k ):
      s = s + x[i,k] ** 2

    x[k,k] = np.sqrt ( 1.0 - s )
#
#  Set X(K,J) for J = K+1 to M+1 by using the fact that XK dot XJ = - 1 / M.
#
    for j in range ( k + 1, m + 1 ):
      s = 0.0
      for i in range ( 0, k ):
        s = s + x[i,k] * x[i,j]

      x[k,j] = ( - 1.0 / float ( m ) - s ) / x[k,k]

  return x

def simplex_coordinates1_test ( m ):

#*****************************************************************************80
#
## simplex_coordinates1_test() tests simplex_coordinates1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
  from scipy.special import factorial
  import numpy as np
  import platform

  print ( '' )
  print ( 'simplex_coordinates1_test' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test simplex_coordinates1' )

  x = simplex_coordinates1 ( m )

  r8mat_transpose_print ( m, m + 1, x, '  Simplex vertex coordinates:' )

  s = 0.0
  for i in range ( 0, m ):
    s = s + ( x[i,0] - x[i,1] ) ** 2

  side = np.sqrt ( s )

  volume = simplex_volume ( m, x )

  volume2 = np.sqrt ( m + 1 ) / factorial ( m ) \
    / np.sqrt ( 2.0 ** m ) * side ** m

  print ( '' )
  print ( '  Side length =     %g' % ( side ) )
  print ( '  Volume =          %g' % ( volume ) )
  print ( '  Expected volume = %g' % ( volume2 ) )

  xtx = np.dot ( np.transpose ( x ), x )

  r8mat_transpose_print ( m + 1, m + 1, xtx, '  Dot product matrix:' )

  return

def simplex_coordinates2 ( m ):

#*****************************************************************************80
#
## simplex_coordinates2() computes the Cartesian coordinates of simplex vertices.
#
#  Discussion:
#
#    This routine uses a simple approach to determining the coordinates of
#    the vertices of a regular simplex in n dimensions.
#
#    We want the vertices of the simplex to satisfy the following conditions:
#
#    1) The centroid, or average of the vertices, is 0.
#    2) The distance of each vertex from the centroid is 1.
#       By 1), this is equivalent to requiring that the sum of the squares
#       of the coordinates of any vertex be 1.
#    3) The distance between any pair of vertices is equal (and is not zero.)
#    4) The dot product of any two coordinate vectors for distinct vertices
#       is -1/M; equivalently, the angle subtended by two distinct vertices
#       from the centroid is arccos ( -1/M).
#
#    Note that if we choose the first M vertices to be the columns of the
#    MxM identity matrix, we are almost there.  By symmetry, the last column
#    must have all entries equal to some value A.  Because the square of the
#    distance between the last column and any other column must be 2 (because
#    that's the distance between any pair of columns), we deduce that
#    (A-1)^2 + (M-1)*A^2 = 2, hence A = (1-sqrt(1+M))/M.  Now compute the
#    centroid C of the vertices, and subtract that, to center the simplex
#    around the origin.  Finally, compute the norm of one column, and rescale
#    the matrix of coordinates so each vertex has unit distance from the origin.
#
#    This approach devised by John Burkardt, 19 September 2010.  What,
#    I'm not the first?
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real X(M,M+1), the coordinates of the vertices
#    of a simplex in M dimensions.
#
  import numpy as np

  x = np.zeros ( [ m, m + 1 ] )

  for j in range ( 0, m ):
    x[j,j] = 1.0

  a = ( 1.0 - np.sqrt ( float ( 1 + m ) ) ) / float ( m )

  for i in range ( 0, m ):
    x[i,m] = a
#
#  Adjust coordinates so the centroid is at zero.
#
  c = np.zeros ( m )
  for i in range ( 0, m ):
    s = 0.0
    for j in range ( 0, m + 1 ):
      s = s + x[i,j]
    c[i] = s / float ( m + 1 )

  for j in range ( 0, m + 1 ):
    for i in range ( 0, m ):
      x[i,j] = x[i,j] - c[i]
#
#  Scale so each column has norm 1.
#
  s = 0.0
  for i in range ( 0, m ):
    s = s + x[i,0] ** 2
  s = np.sqrt ( s )

  for j in range ( 0, m + 1 ):
    for i in range ( 0, m ):
      x[i,j] = x[i,j] / s

  return x

def simplex_coordinates2_test ( m ):

#*****************************************************************************80
#
## simplex_coordinates2_test() tests simplex_coordinates2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
  from scipy.special import factorial
  import numpy as np
  import platform

  print ( '' )
  print ( 'simplex_coordinates2_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test simplex_coordinates2' )

  x = simplex_coordinates2 ( m )

  r8mat_transpose_print ( m, m + 1, x, '  Simplex vertex coordinates:' )

  s = 0.0
  for i in range ( 0, m ):
    s = s + ( x[i,0] - x[i,1] ) ** 2

  side = np.sqrt ( s )

  volume = simplex_volume ( m, x )

  volume2 = np.sqrt ( m + 1 ) / factorial ( m ) \
    / np.sqrt ( 2.0 ** m ) * side ** m

  print ( '' )
  print ( '  Side length =     %g' % ( side ) )
  print ( '  Volume =          %g' % ( volume ) )
  print ( '  Expected volume = %g' % ( volume2 ) )

  xtx = np.dot ( np.transpose ( x ), x )

  r8mat_transpose_print ( m + 1, m + 1, xtx, '  Dot product matrix:' )

  return

def simplex_coordinates_test ( ):

#*****************************************************************************80
#
## simplex_coordinates_test() tests the simplex_coordinates library().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'simplex_coordinates_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the simplex_coordinates library.' )
#
#  Library routines:
#
  simplex_coordinates1_test ( 3 )
  simplex_coordinates1_test ( 4 )
  simplex_coordinates2_test ( 3 )
  simplex_coordinates2_test ( 4 )
  simplex_volume_test ( )
  simplex01_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'simplex_coordinates_test():' )
  print ( '  Normal end of execution.' )
  return

def simplex_volume ( m, x ):

#*****************************************************************************80
#
## simplex_volume() computes the volume of a simplex.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    real X(M,M+1), the coordinates of the vertices
#    of a simplex in M dimensions.
#
#  Output:
#
#    real VOLUME, the volume of the simplex.
#
  import numpy as np

  a = np.zeros ( [ m, m ] )
  for j in range ( 0, m ):
    for i in range ( 0, m ):
      a[i,j] = x[i,j] - x[i,m]

  volume = abs ( np.linalg.det ( a ) )

  volume01 = simplex01_volume ( m )

  volume = volume * volume01

  return volume

def simplex_volume_test ( ) :

#*****************************************************************************80
#
## simplex_volume_test() tests simplex_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'simplex_volume_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  simplex_volume returns the volume of a simplex' )
  print ( '  in M dimensions.' )

  m = 2
  x2 = np.array ( [ \
    [ 0.0, 7.0, 4.0 ], \
    [ 0.0, 2.0, 4.0 ] ] )
  r8mat_transpose_print ( m, m + 1, x2, '  Triangle:' )
  value = simplex_volume ( m, x2 )

  print ( '' )
  print ( '  Volume = %g' % ( value ) )

  m = 3
  x3 = np.array ( [ \
    [ 0.0, 7.0, 4.0, 0.0 ], \
    [ 0.0, 2.0, 4.0, 0.0 ], \
    [ 0.0, 0.0, 0.0, 6.0 ] ] )
  r8mat_transpose_print ( m, m + 1, x3, '  Tetrahedron:' )
  value = simplex_volume ( m, x3 )

  print ( '' )
  print ( '  Volume = %g' % ( value ) )

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
  simplex_coordinates_test ( )
  timestamp ( )

