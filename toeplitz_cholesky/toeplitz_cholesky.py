#! /usr/bin/env python3
#
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
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

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

def t_cholesky_lower ( n, t ):

#*****************************************************************************80
#
## T_CHOLESKY_LOWER: lower Cholesky factor of a compressed Toeplitz matrix.
#
#  Discussion:
#
#    The first row of the Toeplitz matrix A is supplied in T.
#
#    The Toeplitz matrix must be positive semi-definite.
#
#    After factorization, A = L * L'.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2017
#
#  Author:
#
#    Python version by John Burkardt
#
#  Reference:
#
#    Michael Stewart,
#    Cholesky factorization of semi-definite Toeplitz matrices.
#    Linear Algebra and its Applications,
#    Volume 254, pages 497-525, 1997.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real T(N), the first row of the Toeplitz matrix.
#
#    Output, real L(N,N), the lower Cholesky factor.
#
  import numpy as np

  g = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
    g[0,j] = t[j]
  for j in range ( 1, n ):
    g[1,j] = t[j]

  l = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    l[j,0] = g[0,j]

  for j in range ( n - 1, 0, -1 ):
    g[0,j] = g[0,j-1]
  g[0,0] = 0.0

  for i in range ( 1, n ):
    rho = - g[1,i] / g[0,i]
    gam = np.sqrt ( ( 1.0 - rho ) * ( 1.0 + rho ) )
    for j in range ( i, n ):
      alf = g[0,j]
      bet = g[1,j]
      g[0,j] = (       alf + rho * bet ) / gam
      g[1,j] = ( rho * alf +       bet ) / gam
    for j in range ( i, n ):
      l[j,i] = g[0,j]
    for j in range ( n - 1, i, -1 ):
      g[0,j] = g[0,j-1]
    g[0,i] = 0.0

  return l

def t_cholesky_lower_test ( ):

#*****************************************************************************80
#
## T_CHOLESKY_LOWER_TEST tests T_CHOLESKY_LOWER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'T_CHOLESKY_LOWER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_CHOLESKY_LOWER computes the lower Cholesky' )
  print ( '  factor of a positive semi-definite Toeplitz matrix.' )
  print ( '  The Toeplitz matrix is defined by its first row.' )

  n = 3
  t = np.array ( [ 1.0,   0.5, -0.375 ] )

  r8vec_print ( n, t, '  First row of Toeplitz matrix T:' )

  l = t_cholesky_lower ( n, t )
  r8mat_print ( n, n, l, '  Computed lower Cholesky factor L:' )

  b = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, b, '  Product L*L\':' )

  return

def t_cholesky_upper ( n, t ):

#*****************************************************************************80
#
## T_CHOLESKY_UPPER: upper Cholesky factor of a compressed Toeplitz matrix.
#
#  Discussion:
#
#    The Toeplitz matrix A is supplied by its first row.
#
#    The Toeplitz matrix must be positive semi-definite.
#
#    After factorization, A = R' * R.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2017
#
#  Author:
#
#    Python version by John Burkardt
#
#  Reference:
#
#    Michael Stewart,
#    Cholesky factorization of semi-definite Toeplitz matrices.
#    Linear Algebra and its Applications,
#    Volume 254, pages 497-525, 1997.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real T(N), the compressed Toeplitz matrix.
#
#    Output, real R(N,N), the upper Cholesky factor.
#
  import numpy as np

  g = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
    g[0,j] = t[j]
  for j in range ( 1, n ):
    g[1,j] = t[j]

  r = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    r[0,j] = g[0,j]

  for j in range ( n - 1, 0, -1 ):
    g[0,j] = g[0,j-1]
  g[0,0] = 0.0

  for i in range ( 1, n ):
    rho = - g[1,i] / g[0,i]
    gam = np.sqrt ( ( 1.0 - rho ) * ( 1.0 + rho ) )
    for j in range ( i, n ):
      alf = g[0,j]
      bet = g[1,j]
      g[0,j] = (       alf + rho * bet ) / gam
      g[1,j] = ( rho * alf +       bet ) / gam
    for j in range ( i, n ):
      r[i,j] = g[0,j]
    for j in range ( n - 1, i, -1 ):
      g[0,j] = g[0,j-1]
    g[0,i] = 0.0

  return r

def t_cholesky_upper_test ( ):

#*****************************************************************************80
#
## T_CHOLESKY_UPPER_TEST tests T_CHOLESKY_UPPER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'T_CHOLESKY_UPPER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_CHOLESKY_UPPER computes the upper Cholesky' )
  print ( '  factor of a positive semi-definite Toeplitz matrix.' )
  print ( '  The Toeplitz matrix is defined by its first row.' )

  n = 3
  t = np.array ( [ 1.0,   0.5, -0.375 ] )

  r8vec_print ( n, t, '  First row of Toeplitz matrix T:' )

  r = t_cholesky_upper ( n, t )
  r8mat_print ( n, n, r, '  Computed upper Cholesky factor R:' )

  b = np.dot ( r.transpose ( ), r )
  r8mat_print ( n, n, b, '  Product R\'R:' )

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

def toep_cholesky_lower ( n, g ):

#*****************************************************************************80
#
## TOEP_CHOLESKY_LOWER: lower Cholesky factor of a compressed Toeplitz matrix.
#
#  Discussion:
#
#    The Toeplitz matrix A is supplied in a compressed form G.
#
#    The Toeplitz matrix must be positive semi-definite.
#
#    After factorization, A = L * L'.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2017
#
#  Author:
#
#    Python version by John Burkardt
#
#  Reference:
#
#    Michael Stewart,
#    Cholesky factorization of semi-definite Toeplitz matrices.
#    Linear Algebra and its Applications,
#    Volume 254, pages 497-525, 1997.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real G(2,N), the compressed Toeplitz matrix.
#    G(1,1:N) contains the first row.
#    G(2,2:N) contains the first column.
#
#    Output, real L(N,N), the lower Cholesky factor.
#
  import numpy as np

  l = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    l[j,0] = g[0,j]

  for j in range ( n - 1, 0, -1 ):
    g[0,j] = g[0,j-1]
  g[0,0] = 0.0

  for i in range ( 1, n ):
    rho = - g[1,i] / g[0,i]
    gam = np.sqrt ( ( 1.0 - rho ) * ( 1.0 + rho ) )
    for j in range ( i, n ):
      alf = g[0,j]
      bet = g[1,j]
      g[0,j] = (       alf + rho * bet ) / gam
      g[1,j] = ( rho * alf +       bet ) / gam
    for j in range ( i, n ):
      l[j,i] = g[0,j]
    for j in range ( n - 1, i, -1 ):
      g[0,j] = g[0,j-1]
    g[0,i] = 0.0

  return l

def toep_cholesky_lower_test ( ):

#*****************************************************************************80
#
## TOEP_CHOLESKY_LOWER_TEST tests TOEP_CHOLESKY_LOWER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TOEP_CHOLESKY_LOWER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TOEP_CHOLESKY_LOWER computes the lower Cholesky' )
  print ( '  factor of a positive semi-definite Toeplitz matrix.' )
  print ( '  The Toeplitz matrix is supplied as a (2,N) array.' )

  n = 3
  g = np.array ( [ \
    [ 1.0,   0.5, -0.375 ], \
    [ 0.0,   0.5, -0.375 ] ] )

  r8mat_print ( 2, n, g, '  Compressed Toeplitz matrix G:' )

  l = toep_cholesky_lower ( n, g )
  r8mat_print ( n, n, l, '  Computed lower Cholesky factor L:' )

  b = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, b, '  Product L*L\':' )

  return

def toep_cholesky_upper ( n, g ):

#*****************************************************************************80
#
## TOEP_CHOLESKY_UPPER: upper Cholesky factor of a compressed Toeplitz matrix.
#
#  Discussion:
#
#    The Toeplitz matrix A is supplied in a compressed form G.
#
#    The Toeplitz matrix must be positive semi-definite.
#
#    After factorization, A = R' * R.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2017
#
#  Author:
#
#    Python version by John Burkardt
#
#  Reference:
#
#    Michael Stewart,
#    Cholesky factorization of semi-definite Toeplitz matrices.
#    Linear Algebra and its Applications,
#    Volume 254, pages 497-525, 1997.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real G(2,N), the compressed Toeplitz matrix.
#    G(1,1:N) contains the first row.
#    G(2,2:N) contains the first column.
#
#    Output, real R(N,N), the upper Cholesky factor.
#
  import numpy as np

  r = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    r[0,j] = g[0,j]

  for j in range ( n - 1, 0, -1 ):
    g[0,j] = g[0,j-1]
  g[0,0] = 0.0

  for i in range ( 1, n ):
    rho = - g[1,i] / g[0,i]
    gam = np.sqrt ( ( 1.0 - rho ) * ( 1.0 + rho ) )
    for j in range ( i, n ):
      alf = g[0,j]
      bet = g[1,j]
      g[0,j] = (       alf + rho * bet ) / gam
      g[1,j] = ( rho * alf +       bet ) / gam
    for j in range ( i, n ):
      r[i,j] = g[0,j]
    for j in range ( n - 1, i, -1 ):
      g[0,j] = g[0,j-1]
    g[0,i] = 0.0

  return r

def toep_cholesky_upper_test ( ):

#*****************************************************************************80
#
## TOEP_CHOLESKY_UPPER_TEST tests TOEP_CHOLESKY_UPPER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TOEP_CHOLESKY_UPPER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TOEP_CHOLESKY_UPPER computes the upper Cholesky' )
  print ( '  factor of a positive semi-definite Toeplitz matrix.' )
  print ( '  The Toeplitz matrix is supplied as a (2,N) array.' )

  n = 3
  g = np.array ( [ \
    [ 1.0,   0.5, -0.375 ], \
    [ 0.0,   0.5, -0.375 ] ] )

  r8mat_print ( 2, n, g, '  Compressed Toeplitz matrix G:' )

  r = toep_cholesky_upper ( n, g )
  r8mat_print ( n, n, r, '  Computed upper Cholesky factor R:' )

  b = np.dot ( r.transpose ( ), r )
  r8mat_print ( n, n, b, '  Product R\'R:' )

  return

def toeplitz_cholesky_lower ( n, a ):

#*****************************************************************************80
#
## TOEPLITZ_CHOLESKY_LOWER computes the lower Cholesky factor of a Toeplitz matrix.
#
#  Discussion:
#
#    The Toeplitz matrix must be positive semi-definite.
#
#    After factorization, A = L * L'.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2017
#
#  Author:
#
#    Python version by John Burkardt
#
#  Reference:
#
#    Michael Stewart,
#    Cholesky factorization of semi-definite Toeplitz matrices.
#    Linear Algebra and its Applications,
#    Volume 254, pages 497-525, 1997.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real A(N,N), the Toeplitz matrix.
#
#    Output, real L(N,N), the lower Cholesky factor.
#
  import numpy as np

  g = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
    g[0,j] = a[j,0]
  for j in range ( 1, n ):
    g[1,j] = a[j,0]

  l = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    l[j,0] = g[0,j]

  for j in range ( n - 1, 0, -1 ):
    g[0,j] = g[0,j-1]
  g[0,0] = 0.0

  for i in range ( 1, n ):
    rho = - g[1,i] / g[0,i]
    gam = np.sqrt ( ( 1.0 - rho ) * ( 1.0 + rho ) )
    for j in range ( i, n ):
      alf = g[0,j]
      bet = g[1,j]
      g[0,j] = (       alf + rho * bet ) / gam
      g[1,j] = ( rho * alf +       bet ) / gam
    for j in range ( i, n ):
      l[j,i] = g[0,j]
    for j in range ( n - 1, i, -1 ):
      g[0,j] = g[0,j-1]
    g[0,i] = 0.0

  return l

def toeplitz_cholesky_lower_test ( ):

#*****************************************************************************80
#
## TOEPLITZ_CHOLESKY_LOWER_TEST tests TOEPLITZ_CHOLESKY_LOWER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TOEPLITZ_CHOLESKY_LOWER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TOEPLITZ_CHOLESKY_LOWER computes the lower Cholesky' )
  print ( '  factorization of a positive semi-definite Toeplitz matrix.' )
  print ( '  The matrix is supplied as an NxN array.' )

  n = 3
  a = np.array ( [ \
    [  1.0,   0.5, -0.375 ], \
    [  0.5,   1.0,  0.5   ], \
    [ -0.375, 0.5,  1.0   ] ] )

  r8mat_print ( n, n, a, '  Toeplitz matrix A:' )

  l = toeplitz_cholesky_lower ( n, a )
  r8mat_print ( n, n, l, '  Computed lower Cholesky factor L:' )

  b = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, b, '  Product LL\':' )

  return

def toeplitz_cholesky_upper ( n, a ):

#*****************************************************************************80
#
## TOEPLITZ_CHOLESKY_UPPER computes the upper Cholesky factor of a Toeplitz matrix.
#
#  Discussion:
#
#    The Toeplitz matrix must be positive semi-definite.
#
#    After factorization, A = R' * R.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2017
#
#  Author:
#
#    Python version by John Burkardt
#
#  Reference:
#
#    Michael Stewart,
#    Cholesky factorization of semi-definite Toeplitz matrices.
#    Linear Algebra and its Applications,
#    Volume 254, pages 497-525, 1997.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real A(N,N), the Toeplitz matrix.
#
#    Output, real R(N,N), the upper Cholesky factor.
#
  import numpy as np

  g = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
    g[0,j] = a[0,j]
  for j in range ( 1, n ):
    g[1,j] = a[j,0]

  r = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    r[0,j] = g[0,j]

  for j in range ( n - 1, 0, -1 ):
    g[0,j] = g[0,j-1]
  g[0,0] = 0.0

  for i in range ( 1, n ):
    rho = - g[1,i] / g[0,i]
    gam = np.sqrt ( ( 1.0 - rho ) * ( 1.0 + rho ) )
    for j in range ( i, n ):
      alf = g[0,j]
      bet = g[1,j]
      g[0,j] = (       alf + rho * bet ) / gam
      g[1,j] = ( rho * alf +       bet ) / gam
    for j in range ( i, n ):
      r[i,j] = g[0,j]
    for j in range ( n - 1, i, -1 ):
      g[0,j] = g[0,j-1]
    g[0,i] = 0.0

  return r

def toeplitz_cholesky_upper_test ( ):

#*****************************************************************************80
#
## TOEPLITZ_CHOLESKY_UPPER_TEST tests TOEPLITZ_CHOLESKY_UPPER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TOEPLITZ_CHOLESKY_UPPER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TOEPLITZ_CHOLESKY_UPPER computes the upper Cholesky' )
  print ( '  factorization of a positive semi-definite Toeplitz matrix.' )
  print ( '  The matrix is supplied as an NxN array.' )

  n = 3
  a = np.array ( [ \
    [  1.0,   0.5, -0.375 ], \
    [  0.5,   1.0,  0.5   ], \
    [ -0.375, 0.5,  1.0   ] ] )

  r8mat_print ( n, n, a, '  Toeplitz matrix A:' )

  r = toeplitz_cholesky_upper ( n, a )
  r8mat_print ( n, n, r, '  Computed upper Cholesky factor R:' )

  b = np.dot ( r.transpose ( ), r )
  r8mat_print ( n, n, b, '  Product R\'R:' )

  return

def toeplitz_cholesky_test ( ):

#*****************************************************************************80
#
## TOEPLITZ_CHOLESKY_TEST tests the TOEPLITZ_CHOLESKY library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 January 2017
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TOEPLITZ_CHOLESKY_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TOEPLITZ_CHOLESKY library.' )

  t_cholesky_lower_test ( )
  toep_cholesky_lower_test ( )
  toeplitz_cholesky_lower_test ( )

  t_cholesky_upper_test ( )
  toep_cholesky_upper_test ( )
  toeplitz_cholesky_upper_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TOEPLITZ_CHOLESKY_TEST:' )
  print ( '  Normal end of execution.' )
  print ( '' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  toeplitz_cholesky_test ( )
  timestamp ( )

