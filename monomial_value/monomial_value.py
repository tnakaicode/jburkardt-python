#! /usr/bin/env python3
#
def i4vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_transpose_print() prints an I4VEC "transposed".
#
#  Example:
#
#    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
#    TITLE = 'My vector:  '
#
#    My vector:
#
#       1    2    3    4    5
#       6    7    8    9   10
#      11
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( title, end = '' )

  if ( 0 < n ):
    for i in range ( 0, n ):
      print ( ' %d' % ( a[i] ), end = '' )
      if ( ( i + 1 ) % 20 == 0 or i == n - 1 ):
        print ( '' )
  else:
    print ( '(empty vector)' )

  return

def monomial_value_1d ( n, e, x ):

#*****************************************************************************80
#
## monomial_value_1d() evaluates a monomial in 1D.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      x^e
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    integer E, the exponent.
#
#    real X(N), the point coordinates.
#
#  Output:
#
#    real VALUE(N), the value of the monomial.
#
  import numpy as np

  value = np.zeros ( n )

  for i in range ( 0, n ):
    value[i] = x[i] ** e

  return value

def monomial_value_1d_test ( rng ):

#*****************************************************************************80
#
## monomial_value_1d_test() tests monomial_value_1d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'monomial_value_1d_test():' )
  print ( '  monomial_value_1d() evaluates a monomial of a 1D argument.' )
  print ( '' )
  print ( '      X^(-1)       X^(0)       X^(1)       X^(2)       X^(5)' )
  print ( '' )

  n = 5
  x_min = -2.0
  x_max = +10.0

  x = x_min + ( x_max - x_min ) * rng.random ( size = n )

  e = -1
  vm1 = monomial_value_1d ( n, e, x )
  e = 0
  v0 = monomial_value_1d ( n, e, x )
  e = 1
  v1 = monomial_value_1d ( n, e, x )
  e = 2
  v2 = monomial_value_1d ( n, e, x )
  e = 5
  v5 = monomial_value_1d ( n, e, x )

  for j in range ( 0, n ):
    print ( '  %10g  %10g  %10g  %10g  %10g' \
      % ( vm1[j], v0[j], v1[j], v2[j], v5[j] ) )

  return

def monomial_value ( m, n, e, x ):

#*****************************************************************************80
#
## monomial_value() evaluates a monomial.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      product ( 1 <= i <= m ) x(i)^e(i)
#
#    The combination 0.0^0, if encountered, is treated as 1.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of evaluation points.
#
#    integer E(M), the exponents.
#
#    real X(M,N), the point coordinates.
#
#  Output:
#
#    real V(N), the monomial values.
#
  import numpy as np

  v = np.ones ( n )

  for i in range ( 0, m ):
    if ( 0 != e[i] ):
      for j in range ( 0, n ):
        if ( x[i,j] == 0.0 ):
          v[j] = 0.0
        elif ( e[i] != 0 ):
          v[j] = v[j] * x[i,j] ** e[i]

  return v

def monomial_value_test ( rng ):

#*****************************************************************************80
#
## monomial_value_test() tests monomial_value().
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
#    rng(): the current random number generator.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'monomial_value_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  monomial_value() evaluates monomials' )
  print ( '  in dimensions 1 through 3.' )

  e_min = 0
  e_max = 6
  n = 5
  x_min = -2.0
  x_max = +10.0

  for m in range ( 1, 4 ):

    print ( '' )
    print ( '  Spatial dimension M =  %d' % ( m ) )

    e = rng.integers ( low = e_min, high = e_max, size = m, endpoint = True )
    i4vec_transpose_print ( m, e, '  Exponents:' )
    x = x_min + ( x_max - x_min ) * rng.random ( size = [ m, n ] )
    v = monomial_value ( m, n, e, x )

    print ( '' )
    print ( '   V(X)         ', end = '' )
    for i in range ( 0, m ):
      print ( '      X(%d)' % ( i ), end = '' )
    print ( '' )
    print ( '' )
    for j in range ( 0, n ):
      print ( '%14.6g  ' % ( v[j] ), end = '' )
      for i in range ( 0, m ):
        print ( '%10.4f' % ( x[i,j] ), end = '' )
      print ( '' )

  return

def monomial_value_tests ( ):

#*****************************************************************************80
#
## monomial_value_tests() tests monomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import platform

  print ( '' )
  print ( 'monomial_value_tests():' )
  print ( '  Python version: ' + platform.python_version ( ) )
  print ( '  Test monomial_value().' )

  rng = default_rng ( )

  monomial_value_test ( rng )
  monomial_value_1d_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'monomial_value_tests():' )
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
#    08 May 2020
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
#    08 May 2020
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

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
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
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

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
  monomial_value_tests ( )
  timestamp ( )
 
