#! /usr/bin/env python3
#
def r8_factorial ( n ):

#*****************************************************************************80
#
## R8_FACTORIAL returns N factorial.
#
#  Discussion:
#
#    factorial ( N ) = Product ( 1 <= I <= N ) I
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the function.
#    0 <= N.
#
#    Output, real VALUE, the factorial of N.
#
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'R8_FACTORIAL - Fatal error!' )
    print ( '  N < 0.' )
    exit ( 'R8_FACTORIAL - Fatal error!' )

  value = 1.0

  for i in range ( 2, n + 1 ):
    value = value * i

  return value

def r8_factorial_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL_TEST tests R8_FACTORIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'R8_FACTORIAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FACTORIAL evaluates the factorial function.' )
  print ( '' )
  print ( '      N                     Exact' ),
  print ( '                  Computed' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial ( n )

    print ( '  %4d  %24.16g  %24.16g' % ( n, f1, f2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FACTORIAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_factorial_values ( n_data ):

#*****************************************************************************80
#
## R8_FACTORIAL_VALUES returns values of the real factorial function.
#
#  Discussion:
#
#    0! = 1
#    I! = Product ( 1 <= J <= I ) J
#
#    Although the factorial is an integer valued function, it quickly
#    becomes too large for an integer to hold.  This routine still accepts
#    an integer as the input argument, but returns the function value
#    as a real number.
#
#    In Mathematica, the function can be evaluated by:
#
#      n!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the argument of the function.
#
#    Output, real FN, the value of the function.
#
  import numpy as np

  n_max = 25

  fn_vec = np.array ( [ \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.6000000000000000E+01, \
     0.2400000000000000E+02, \
     0.1200000000000000E+03, \
     0.7200000000000000E+03, \
     0.5040000000000000E+04, \
     0.4032000000000000E+05, \
     0.3628800000000000E+06, \
     0.3628800000000000E+07, \
     0.3991680000000000E+08, \
     0.4790016000000000E+09, \
     0.6227020800000000E+10, \
     0.8717829120000000E+11, \
     0.1307674368000000E+13, \
     0.2092278988800000E+14, \
     0.3556874280960000E+15, \
     0.6402373705728000E+16, \
     0.1216451004088320E+18, \
     0.2432902008176640E+19, \
     0.1551121004333099E+26, \
     0.3041409320171338E+65, \
     0.9332621544394415E+158, \
     0.5713383956445855E+263 ] )

  n_vec = np.array ( [ \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9, \
      10, \
      11, \
      12, \
      13, \
      14, \
      15, \
      16, \
      17, \
      18, \
      19, \
      20, \
      25, \
      50, \
     100, \
     150 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    fn = 0
  else:
    n = n_vec[n_data]
    fn = fn_vec[n_data]
    n_data = n_data + 1

  return n_data, n, fn

def r8_factorial_values_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL_VALUES_TEST tests R8_FACTORIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8_FACTORIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FACTORIAL_VALUES returns values of the real factorial function.' )
  print ( '' )
  print ( '          N          R8_FACTORIAL(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %14.6g' % ( n, fn ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FACTORIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT prints an R8MAT, transposed.
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
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_TEST tests R8MAT_TRANSPOSE_PRINT.
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
  print ( 'R8MAT_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_TRANSPOSE_PRINT prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
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
## R8MAT_TRANSPOSE_PRINT_SOME_TEST tests R8MAT_TRANSPOSE_PRINT_SOME.
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
  print ( 'R8MAT_TRANSPOSE_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_TRANSPOSE_PRINT_SOME prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def simplex01_volume ( m ):

#*****************************************************************************80
#
## SIMPLEX01_VOLUME returns the volume of the unit simplex in M dimensions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real VALUE, the volume.
#
  value = 1.0
  for i in range ( 1, m + 1 ):
    value = value / float ( i )

  return value

def simplex01_volume_test ( ) :

#*****************************************************************************80
#
## SIMPLEX01_VOLUME_TEST tests SIMPLEX01_VOLUME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'SIMPLEX01_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIMPLEX01_VOLUME returns the volume of the unit simplex' )
  print ( '  in M dimensions.' )
  print ( '' )
  print ( '   M   Volume' )
  print ( '' )

  for m in range ( 1, 10 ):
    value = simplex01_volume ( m )
    print ( '  %2d  %g' % ( m, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX01_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

def simplex_coordinates1 ( m ):

#*****************************************************************************80
#
## SIMPLEX_COORDINATES1 computes the Cartesian coordinates of simplex vertices.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real X(M,M+1), the coordinates of the vertices
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
## SIMPLEX_COORDINATES1_TEST tests SIMPLEX_COORDINATES1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'SIMPLEX_COORDINATES1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test SIMPLEX_COORDINATES1' )

  x = simplex_coordinates1 ( m )

  r8mat_transpose_print ( m, m + 1, x, '  Simplex vertex coordinates:' )

  s = 0.0
  for i in range ( 0, m ):
    s = s + ( x[i,0] - x[i,1] ) ** 2

  side = np.sqrt ( s )

  volume = simplex_volume ( m, x )

  volume2 = np.sqrt ( m + 1 ) / r8_factorial ( m ) \
    / np.sqrt ( 2.0 ** m ) * side ** m

  print ( '' )
  print ( '  Side length =     %g' % ( side ) )
  print ( '  Volume =          %g' % ( volume ) )
  print ( '  Expected volume = %g' % ( volume2 ) )

  xtx = np.dot ( np.transpose ( x ), x )

  r8mat_transpose_print ( m + 1, m + 1, xtx, '  Dot product matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX_COORDINATES1_TEST' )
  print ( '  Normal end of execution.' )
  return

def simplex_coordinates2 ( m ):

#*****************************************************************************80
#
## SIMPLEX_COORDINATES2 computes the Cartesian coordinates of simplex vertices.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real X(M,M+1), the coordinates of the vertices
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
## SIMPLEX_COORDINATES2_TEST tests SIMPLEX_COORDINATES2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'SIMPLEX_COORDINATES2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test SIMPLEX_COORDINATES2' )

  x = simplex_coordinates2 ( m )

  r8mat_transpose_print ( m, m + 1, x, '  Simplex vertex coordinates:' )

  s = 0.0
  for i in range ( 0, m ):
    s = s + ( x[i,0] - x[i,1] ) ** 2

  side = np.sqrt ( s )

  volume = simplex_volume ( m, x )

  volume2 = np.sqrt ( m + 1 ) / r8_factorial ( m ) \
    / np.sqrt ( 2.0 ** m ) * side ** m

  print ( '' )
  print ( '  Side length =     %g' % ( side ) )
  print ( '  Volume =          %g' % ( volume ) )
  print ( '  Expected volume = %g' % ( volume2 ) )

  xtx = np.dot ( np.transpose ( x ), x )

  r8mat_transpose_print ( m + 1, m + 1, xtx, '  Dot product matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX_COORDINATES2_TEST' )
  print ( '  Normal end of execution.' )
  return

def simplex_coordinates_test ( ):

#*****************************************************************************80
#
## SIMPLEX_COORDINATES_TEST tests the SIMPLEX_COORDINATES library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'SIMPLEX_COORDINATES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the SIMPLEX_COORDINATES library.' )
#
#  Utility routines:
#
  r8_factorial_test ( )
  r8_factorial_values_test ( )
  r8mat_transpose_print_test ( )
  r8mat_transpose_print_some_test ( )
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
  print ( 'SIMPLEX_COORDINATES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def simplex_volume ( m, x ):

#*****************************************************************************80
#
## SIMPLEX_VOLUME computes the volume of a simplex.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Input, real X(M,M+1), the coordinates of the vertices
#    of a simplex in M dimensions.
#
#    Output, real VOLUME, the volume of the simplex.
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
## SIMPLEX_VOLUME_TEST tests SIMPLEX_VOLUME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'SIMPLEX_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIMPLEX_VOLUME returns the volume of a simplex' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX_VOLUME_TEST' )
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
  simplex_coordinates_test ( )
  timestamp ( )

