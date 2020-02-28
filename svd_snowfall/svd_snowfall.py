#! /usr/bin/env python3
#
def r8col_flip ( m, n, a ):

#*****************************************************************************80
#
## R8COL_FLIP flips the entries in each column of an R8COL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the array to be examined.
#
#    Output, real B(M,N), the flipped array.
#
  import numpy as np

  b = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[i,j] = a[m-1-i,j]

  return b

def r8col_flip_test ( ):

#*****************************************************************************80
#
## R8COL_FLIP_TEST tests R8COL_FLIP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R8COL_FLIP_TEST:' )
  print ( '  R8COL_FLIP flips the columns of an R8COL.' )

  m = 5
  n = 4
  a = np.random.random ( [ m, n ] )

  r8mat_print ( m, n, a, '  Matrix A:' )

  b = r8col_flip ( m, n, a )

  r8mat_print ( m, n, b, '  Matrix after column flipping:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8COL_FLIP_TEST:' )
  print ( '  Normale end of execution.' )
  return

def r8col_normalize_li ( m, n, a ):

#*****************************************************************************80
#
## R8COL_NORMALIZE_LI normalizes an R8COL with the column infinity norm.
#
#  Discussion:
#
#    Each column is scaled so that the entry of maximum norm has the value 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the array to be examined.
#
#    Output, real B(M,N), the normalized array.
#
  import numpy as np

  b = a.copy ( )

  for j in range ( 0, n ):

    c = a[0,j]
    for i in range ( 1, m ):
      if ( abs ( c ) < abs ( a[i,j] ) ):
        c = a[i,j]

    if ( c != 0.0 ):
      b[0:m,j] = b[0:m,j] / c

  return b

def r8col_normalize_li_test ( ):

#*****************************************************************************80
#
## R8COL_NORMALIZE_LI_TEST tests R8COL_NORMALIZE_LI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R8COL_NORMALIZE_LI_TEST:' )
  print ( '  R8COL_NORMALIZE_LI normalizes an array A, dividing each' )
  print ( '  column by its maximum element.' )

  m = 5
  n = 4
  a = np.random.random ( [ m, n ] )

  r8mat_print ( m, n, a, '  Matrix A:' )

  b = r8col_normalize_li ( m, n, a )

  r8mat_print ( m, n, b, '  Matrix after column LI normalization:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8COL_NORMALIZE_LI_TEST:' )
  print ( '  Normale end of execution.' )
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

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
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
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def snowfall_data_print ( x ):

#*****************************************************************************80
#
## SNOWFALL_DATA_PRINT prints the snowfall data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'SNOWFALL_DATA_PRINT:' )
  print ( '' )

  for j in range ( 0, 127 ):
    print ( '  %3d:  ' % ( j ), end = '' )
    for i in range ( 0, 8 ):
      print ( '%8.2f' % ( x[i,j] ), end = '' )
    print ( '' )

  return x

def snowfall_low_rank ( x ):

#*****************************************************************************80
#
## SNOWFALL_LOW_RANK computes low rank approximations to the matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X(8,*), the snowfall data.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'SNOWFALL_LOW_RANK' )
  print ( '  Compute the rank 1 through rank 5 approximations to the data.' )
  print ( '  Compare each of these to the 2016 snowfall data.' )
#
#  Compute the SVD.
#  Note that for Numpy SVD, X = U * S * V (V is NOT transposed!)
#
  u, s, v = np.linalg.svd ( x, full_matrices = False, compute_uv = True )
#
#  Form the rank 1, 2, 3, 4, 5 approximants to A.
#
  a1 =      s[0] * np.outer ( u[:,0], v[0,:] )
  a2 = a1 + s[1] * np.outer ( u[:,1], v[1,:] )
  a3 = a2 + s[2] * np.outer ( u[:,2], v[2,:] )
  a4 = a3 + s[3] * np.outer ( u[:,3], v[3,:] )
  a5 = a4 + s[4] * np.outer ( u[:,4], v[4,:] )
#
#  Column 1 of X is the 2016 snowfall.
#  Column 1 of A1 is the rank 1 approximant to 2016 snowfall.
#
  t = np.linspace ( 0, 7, 8 )

  plt.subplot ( 2, 3, 1 )
  plt.plot ( t, x[:,0], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.title ( '2016 Snowfall' )

  plt.subplot ( 2, 3, 2 )
  plt.plot ( t, x[:,0], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.plot ( t, a1[:,0], 'k-', linewidth = 3 )
  plt.title ( 'Rank 1 Approx (black)' )

  plt.subplot ( 2, 3, 3 )
  plt.plot ( t, x[:,0], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.plot ( t, a2[:,0], 'k-', linewidth = 3 )
  plt.title ( 'Rank 2 Approx (black)' )

  plt.subplot ( 2, 3, 4 )
  plt.plot ( t, x[:,0], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.plot ( t, a3[:,0], 'k-', linewidth = 3 )
  plt.title ( 'Rank 3 Approx (black)' )

  plt.subplot ( 2, 3, 5 )
  plt.plot ( t, x[:,0], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.plot ( t, a4[:,0], 'k-', linewidth = 3 )
  plt.title ( 'Rank 4 Approx (black)' )

  plt.subplot ( 2, 3, 6 )
  plt.plot ( t, x[:,0], 'r-', linewidth = 3 )
  plt.grid ( True )
  plt.plot ( t, a5[:,0], 'k-', linewidth = 3 )
  plt.title ( 'Rank 5 Approx (black)' )

  file_name = 'rank_one_approximants.png'

  plt.savefig ( file_name )
  plt.show ( block = False )

  print ( '' )
  print ( '  Plotted rank 1 to 5 approximants in "%s"' % ( file_name ) )

  return

def snowfall_singular_value_display ( x ):

#*****************************************************************************80
#
## SNOWFALL_SINGULAR_VALUE_DISPLAY looks at the singular values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X(8,*), the snowfall data.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'SVD_SINGULAR_VALUE_DISPLAY' )
  print ( '  Look at the singular values.' )
  print ( '  If the singular values are close, then the data is' )
  print ( '  well spread out.  If the singular values decay rapidly,' )
  print ( '  then the data exhibits patterns, or is constrained to' )
  print ( '  a lower-dimensional subspace.' )
#
#  Compute the SVD.
#
  s = np.linalg.svd ( x, compute_uv = False )
#
#  Print the singular values.
#
  r8vec_print ( 8, s, '  The singular values:' )
#
#  Plot the singular values.
#
  t = np.linspace ( 0, 7, 8 )
  plt.plot ( t, s, 'b.-', linewidth = 3, markersize = 25 )
  plt.title ( 'Singular values of the SNOWFALL matrix' )
  plt.grid ( True )
  plt.savefig ( 'singular_values.png' )
  plt.show ( block = False )

  print ( '' )
  print ( '  Plotted the singular values in "singular_values.png".' )
#
#  Print the cumulative "energy" of the singular values.
#
  s_squared = s ** 2
  energy = np.cumsum ( s_squared ) / np.sum ( s_squared )

  r8vec_print ( 8, energy, '  The cumulative energy:' )

  return

def snowfall_trim ( file_name ):

#*****************************************************************************80
#
## SNOWFALL_TRIM reads the snowfall file and trims the data.
#
#  Discussion:
#
#    The data file contains monthly snowfall records from 1890 to 2016.
#    Column 1 is the year, columns 2 through 9 are the snowfall for
#    October, November, December, January, February, March, April, May,
#    and column 10 is the total snowfall for that season.
#
#    After the LOAD command is executed, the data is stored as
#    8 rows and 126 columns, with the first column of X the
#    1890 data, and the last column is 2016!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILE_NAME, the name of the file.
#
#    Output, real X(8,127), the snowfall data.
#
  import numpy as np

  print ( '' )
  print ( 'SNOWFALL_TRIM' )
  print ( '  Read snowfall file "%s".' % ( file_name ) )
  print ( '  Trim off first (YEAR) and last (TOTAL) items.' )
  print ( '  Output as 8xYEARS array.' )

  file_unit = open ( file_name, 'r' )

  x = np.zeros ( [ 8, 129 ] )

  m = 8
  n = 0
  for line in file_unit:
    line = line.strip ( )
    print ( line )
    values = line.split ( )
    for i in range ( 0, m ):
      x[i,n] = float ( values[i+1] )
    n = n + 1

  print ( '' )
  print ( '  Trimmed snowfall data array:' )
  print ( '  Number of data rows    M = %d' % ( m ) )
  print ( '  Number of data columns N = %d' % ( n ) )

  return x

def snowfall_u_basis_vectors ( x ):

#*****************************************************************************80
#
## SNOWFALL_U_BASIS_VECTORS looks at the first 6 modes in the U matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X(8,*), the snowfall data.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'SNOWFALL_U_BASIS_VECTORS' )
  print ( '  Look at the first 6 modes in the SVD factor U.' )
  print ( '  Each of these represents a pattern for snowfall over a year.' )
  print ( '  The first mode is the pattern that is strongest in the data.' )
#
#  Compute the SVD.
#
  u, s, v = np.linalg.svd ( x, full_matrices = False, compute_uv = True )
#
#  Normalize the patterns so that each column has maximum entry 1.
#
  us = r8col_normalize_li ( 8, 8, u )
#
#  Plot the modes.
#
  t = np.linspace ( 0, 7, 8 )

  plt.subplot ( 2, 3, 1 )
  plt.plot ( [0,7], [0,0], 'r-' )
  plt.plot ( t, us[:,0], 'b-', linewidth = 3 )
  plt.axis ( [0,7,-1.0,+1.0] )
  plt.grid ( True )
  plt.title ( 'U Mode #1' )

  plt.subplot ( 2, 3, 2 )
  plt.plot ( [0,7], [0,0], 'r-' )
  plt.plot ( t, us[:,1], 'b-', linewidth = 3 )
  plt.axis ( [0,7,-1.0,+1.0] )
  plt.grid ( True )
  plt.title ( 'U Mode #2' )

  plt.subplot ( 2, 3, 3 )
  plt.plot ( [0,7], [0,0], 'r-' )
  plt.plot ( t, us[:,2], 'b-', linewidth = 3 )
  plt.axis ( [0,7,-1.0,+1.0] )
  plt.grid ( True )
  plt.title ( 'U Mode #3' )

  plt.subplot ( 2, 3, 4 )
  plt.plot ( [0,7], [0,0], 'r-' )
  plt.plot ( t, us[:,3], 'b-', linewidth = 3 )
  plt.axis ( [0,7,-1.0,+1.0] )
  plt.grid ( True )
  plt.title ( 'U Mode #4' )

  plt.subplot ( 2, 3, 5 )
  plt.plot ( [0,7], [0,0], 'r-' )
  plt.plot ( t, us[:,4], 'b-', linewidth = 3 )
  plt.axis ( [0,7,-1.0,+1.0] )
  plt.grid ( True )
  plt.title ( 'U Mode #5' )

  plt.subplot ( 2, 3, 6 )
  plt.plot ( [0,7], [0,0], 'r-' )
  plt.plot ( t, us[:,5], 'b-', linewidth = 3 )
  plt.axis ( [0,7,-1.0,+1.0] )
  plt.grid ( True )
  plt.title ( 'U Mode #6' )

  file_name = 'u_modes.png'
  plt.savefig ( file_name )
  plt.show ( block = False )

  print ( '' )
  print ( '  Plotted U modes 1 to 6 in "%s".' % ( file_name ) )

  return

def snowfall_v_basis_vectors ( x ):

#*****************************************************************************80
#
## SNOWFALL_V_BASIS_VECTORS looks at the first 6 modes in the V matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X(8,*), the snowfall data.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'SNOWFALL_V_BASIS_VECTORS' )
  print ( '  Look at the first 6 modes in the SVD factor V.' )
  print ( '  Each of these represents a pattern shared by all the months,' )
  print ( '  and extending across all the sampling years' )
#
#  Compute the SVD.
#  Note that Numpy's SVD has A=U*S*V, NOT A=U*S*V'.
#
  u, s, v = np.linalg.svd ( x, full_matrices = True, compute_uv = True )

  m, n = v.shape
#
#  Normalize the patterns so that each column has maximum entry 1.
#
  v = v.transpose ( )

  v = r8col_flip ( m, n, v )

  vs = r8col_normalize_li ( m, n, v )
#
#  Plot the modes.
#
  y = np.linspace ( 1890, 2018, 129 )

  plt.subplot ( 2, 3, 1 )
  plt.scatter ( y, vs[:,0], s = 5 )
  plt.grid ( True )
  plt.axis ( [1890, 2018, -1, +1 ] )
  plt.xlabel ( '<--Year-->' )
  plt.title ( 'V Mode #1' )

  plt.subplot ( 2, 3, 2 )
  plt.scatter ( y, vs[:,1], s = 5 )
  plt.grid ( True )
  plt.axis ( [1890, 2018, -1, +1 ] )
  plt.xlabel ( '<--Year-->' )
  plt.title ( 'V Mode #2' )

  plt.subplot ( 2, 3, 3 )
  plt.scatter ( y, vs[:,2], s = 5 )
  plt.grid ( True )
  plt.axis ( [1890, 2018, -1, +1 ] )
  plt.xlabel ( '<--Year-->' )
  plt.title ( 'V Mode #3' )

  plt.subplot ( 2, 3, 4 )
  plt.scatter ( y, vs[:,3], s = 5 )
  plt.grid ( True )
  plt.axis ( [1890, 2018, -1, +1 ] )
  plt.xlabel ( '<--Year-->' )
  plt.title ( 'V Mode #4' )

  plt.subplot ( 2, 3, 5 )
  plt.scatter ( y, vs[:,4], s = 5 )
  plt.grid ( True )
  plt.axis ( [1890, 2018, -1, +1 ] )
  plt.xlabel ( '<--Year-->' )
  plt.title ( 'V Mode #5' )

  plt.subplot ( 2, 3, 6 )
  plt.scatter ( y, vs[:,5], s = 5 )
  plt.grid ( True )
  plt.axis ( [1890, 2018, -1, +1 ] )
  plt.xlabel ( '<--Year-->' )
  plt.title ( 'V Mode #6' )

  file_name = 'v_modes.png'
  plt.savefig ( file_name )
  plt.show ( block = False )

  print ( '' )
  print ( '  Plotted V modes 1 to 6 in "%s".' % ( file_name ) )

  return

def svd_snowfall_test ( ):

#*****************************************************************************80
#
## SVD_SNOWFALL_TEST tests SVD_SNOWFALL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SVD_SNOWFALL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the SVD_SNOWFALL library.' )

  file_name = 'snowfall.txt'

  x = snowfall_trim ( file_name )

  snowfall_data_print ( x )

  snowfall_singular_value_display ( x )

  snowfall_low_rank ( x )

  snowfall_u_basis_vectors ( x )

  snowfall_v_basis_vectors ( x )
#
#  Terminate.
#
  print ( '' )
  print ( 'SVD_SNOWFALL_TEST:' )
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
  svd_snowfall_test ( )
  timestamp ( )

