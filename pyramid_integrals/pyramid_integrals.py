#! /usr/bin/env python3
#
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
#    07 April 2015
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
        v[j] = v[j] * x[i,j] ** e[i]

  return v

def pyramid01_monomial_integral ( expon ):

#*****************************************************************************80
#
## pyramid01_monomial_integral(): monomial integral in a unit pyramid.
#
#  Discussion:
#
#    This routine returns the integral of
#
#      product ( 1 <= I <= 3 ) X(I)^EXPON(I)
#
#    over the unit pyramid.
#
#    The unit pyramid is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
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
#  Reference:
#
#    Arthur Stroud,
#    Approximate Calculation of Multiple Integrals,
#    Prentice Hall, 1971,
#    ISBN: 0130438936,
#    LC: QA311.S85.
#
#  Input:
#
#    integer EXPON(3), the exponents.
#
#  Output:
#
#    real VALUE, the integral of the monomial.
#
  from scipy.special import comb

  if ( ( ( expon[0] % 2 ) == 0 ) and ( ( expon[1] % 2 ) == 0 ) ):

    i_hi = 2 + expon[0] + expon[1]

    value = 0.0
    for i in range ( 0, i_hi + 1 ):
      value = value + r8_mop ( i ) * comb ( i_hi, i ) / float ( i + expon[2] + 1 )

    value = value * 2.0 / float ( expon[0] + 1 ) * 2.0 / float ( expon[1] + 1 )

  else:

    value = 0.0

  return value

def pyramid01_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## pyramid01_monomial_integral_test() tests pyramid01_monomial_integral().
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

  m = 3
  n = 500000
  e_max = 6

  print ( '' )
  print ( 'pyramid01_monomial_integral_test' )
  print ( '  pyramid01_monomial_integral returns the integral of a monomial' )
  print ( '  over the unit pyramid in 3D.' )
  print ( '  Compare to a Monte Carlo estimate.' )
#
#  Get sample points.
#
  x = pyramid01_sample ( n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
  print ( '' )
  print ( '   E1  E2  E3     MC-Estimate      Exact           Error' )
  print ( '' )
#
#  Check all monomials, with only even dependence on X or Y, 
#  up to total degree E_MAX.
#
  e = np.zeros ( 3, dtype = np.int32 )

  for e3 in range ( 0, e_max + 1 ):
    e[2] = e3
    for e2 in range ( 0, e_max - e3 + 1, 2 ):
      e[1] = e2
      for e1 in range ( 0 , e_max - e3 - e2 + 1, 2 ):
        e[0] = e1

        value = monomial_value ( m, n, e, x )

        q = pyramid01_volume ( ) * np.sum ( value ) / float ( n )
        exact = pyramid01_monomial_integral ( e )
        error = abs ( q - exact )

        print ( '  %2d  %2d  %2d  %14.6g  %14.6g  %10.2g' \
          % ( e[0], e[1], e[2], q, exact, error ) )

  return

def pyramid01_sample ( n, rng ):

#*****************************************************************************80
#
## pyramid01_sample(): sample the unit pyramid.
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
#    integer N, the number of samples desired.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(3,N), the sample values.
#
  import numpy as np

  one_third = 1.0 / 3.0

  x = rng.random ( size = [ 3, n ] )

  for j in range ( 0, n ):
    x[2,j] = 1.0 - x[2,j] ** one_third
    x[1,j] = ( 1.0 - x[2,j] ) * ( 2.0 * x[1,j] - 1.0 )
    x[0,j] = ( 1.0 - x[2,j] ) * ( 2.0 * x[0,j] - 1.0 )

  return x

def pyramid01_sample_test ( rng ):

#*****************************************************************************80
#
## pyramid01_sample_test() tests pyramid01_sample().
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
  print ( '' )
  print ( 'pyramid01_sample_test()' )
  print ( '  pyramid01_sample samples points from the unit pyramid.' )

  n = 20
  x = pyramid01_sample ( n, rng )

  m = 3
  r8mat_transpose_print ( m, n, x, '  Unit pyramid points' )

  return

def pyramid01_volume ( ):

#*****************************************************************************80
#
## pyramid01_volume() returns the volume of a unit pyramid.
#
#  Discussion:
#
#    A pyramid with square base can be regarded as the upper half of a
#    3D octahedron.
#
#    The integration region:
#
#      - ( 1 - Z ) <= X <= 1 - Z
#      - ( 1 - Z ) <= Y <= 1 - Z
#                0 <= Z <= 1.
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
#  Output:
#
#    real VALUE, the volume of the pyramid.
#
  value = 4.0 / 3.0;

  return value

def pyramid01_volume_test ( ) :

#*****************************************************************************80
#
## pyramid01_volume_test() tests pyramid01_volume().
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
  print ( '' )
  print ( 'pyramid01_volume_test()' )
  print ( '  pyramid01_volume() returns the volume of the unit pyramid.' )

  value = pyramid01_volume ( )

  print ( '' )
  print ( '  pyramid01_volume() = %g' % ( value ) )

  return

def pyramid_integrals_test ( ):

#*****************************************************************************80
#
## pyramid_integrals_test() tests pyramid_integrals().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'pyramid_integrals_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pyramid_integrals().' )

  rng = default_rng ( )

  r8_mop_test ( rng )
  pyramid01_monomial_integral_test ( rng )
  pyramid01_sample_test ( rng )
  pyramid01_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'pyramid_integrals_test():' )
  print ( '  Normal end of execution.' )
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

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop() returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real VALUE, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( rng ):

#*****************************************************************************80
#
## r8_mop_test() tests r8_mop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
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
  print ( 'r8_mop_test():' )
  print ( '  r8_mop() evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_mop(I4)' )
  print ( '' )

  for test in range ( 0, 10 ):
    i4 = rng.integers ( low = -100, high = +100, endpoint = True )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )

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
  pyramid_integrals_test ( )
  timestamp ( )

