#! /usr/bin/env python3
#
def c8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## c8mat_print() prints a C8MAT.
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
#    complex A(M,N), the matrix.
#
#    string TITLE, a title.
#
  c8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def c8mat_print_test ( ):

#*****************************************************************************80
#
## c8mat_print_test() tests c8mat_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'c8mat_print_test' )
  print ( '  c8mat_print prints an C8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ complex(10.0, 1.0), complex(10.0, 2.0), complex(10.0, 3.0) ], \
    [ complex(20.0, 1.0), complex(20.0, 2.0), complex(20.0, 3.0) ], \
    [ complex(30.0, 1.0), complex(30.0, 2.0), complex(30.0, 3.0) ], \
    [ complex(40.0, 1.0), complex(40.0, 2.0), complex(40.0, 3.0) ] ], \
    dtype = np.complex128 )

  c8mat_print ( m, n, v, '  Here is a C8MAT:' )

  return

def c8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## c8mat_print_some() prints out a portion of an C8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    complex A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 4

  print ( '' )
  print  ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '       %7d              ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  %12gi ' % ( a.real[i,j], a.imag[i,j] ), end = '' )

      print ( '' )

  return

def c8mat_print_some_test ( ):

#*****************************************************************************80
#
## c8mat_print_some_test() tests c8mat_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'c8mat_print_some_test' )
  print ( '  c8mat_print_some prints some of an C8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ complex(10.0, 1.0), complex(10.0, 2.0), complex(10.0, 3.0), \
      complex(10.0, 4.0), complex(10.0, 5.0), complex(10.0, 6.0) ], \
    [ complex(20.0, 1.0), complex(20.0, 2.0), complex(20.0, 3.0), \
      complex(20.0, 4.0), complex(20.0, 5.0), complex(20.0, 6.0) ], \
    [ complex(30.0, 1.0), complex(30.0, 2.0), complex(30.0, 3.0), \
      complex(30.0, 4.0), complex(30.0, 5.0), complex(30.0, 6.0) ], \
    [ complex(40.0, 1.0), complex(40.0, 2.0), complex(40.0, 3.0), \
      complex(40.0, 4.0), complex(40.0, 5.0), complex(40.0, 6.0) ] ], \
    dtype = np.complex128 )

  c8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is a C8MAT:' )

  return

def c8mat_sftb ( n1, n2, y ):

#*****************************************************************************80
#
## c8mat_sftb() computes a "slow" backward Fourier transform of a C8MAT.
#
#  Discussion:
#
#    SFTF and SFTB are inverses of each other.  If we begin with data
#    X and apply SFTF to get Y, and then apply SFTB to Y,
#    we should get back the original X.
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 0 <= I1 <= N1 - 1,
#        0 <= I2 <= N2 - 1,
#
#      X(I1,I2) = Sum ( 0 <= K2 <= N2 - 1 ) Sum ( 0 <= K1 <= N1 - 1 )
#        Y(K1,K2) * exp ( 2 pi i I1 K1 / N1 ) * exp ( 2 pi i I2 K2 / N2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the number of rows and columns of data.
#
#    complex Y(0:N1-1,0:N2-1), the Fourier coefficients.
#
#  Output:
#
#    complex X(0:N1-1,0:N2-1), the data.
#
  import numpy as np

  x = np.zeros ( [ n1, n2 ], dtype = np.complex128 )

  for i2 in range ( 0, n2 ):
    for j2 in range ( 0, n2 ):
      theta2 = 2.0 * np.pi * float ( i2 ) * float ( j2 ) / float ( n2 )
      cs2 = np.cos ( theta2 ) - 1j * np.sin ( theta2 )
      for i1 in range ( 0, n1 ):
        for j1 in range ( 0, n1 ):
          theta1 = 2.0 * np.pi * float ( i1 ) * float ( j1 ) / float ( n1 )
          cs1 = np.cos ( theta1 ) - 1j * np.sin ( theta1 )
          x[i1,i2] = x[i1,i2] + y[j1,j2] * cs1 * cs2

  for i2 in range ( 0, n2 ):
    for i1 in range ( 0, n1 ):
      x[i1,i2] = x[i1,i2] / float ( n1 * n2 )

  return x

def c8mat_sftf ( n1, n2, x ):

#*****************************************************************************80
#
## c8mat_sftf() computes a "slow" forward Fourier transform of a C8MAT.
#
#  Discussion:
#
#    SFTF and SFTB are inverses of each other.  If we begin with data
#    X and apply SFTF to get Y, and then apply SFTB to Y,
#    we should get back the original X.
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 0 <= I1 <= N1 - 1,
#        0 <= I2 <= N2 - 1,
#
#      Y(I1,I2) = Sum ( 0 <= K2 <= N2 - 1 ) Sum ( 0 <= K1 <= N1 - 1 )
#        X(K1,K2) * exp ( - 2 pi i I1 K1 / N1 ) * exp ( - 2 pi i I2 K2 / N2 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N1, N2, the number of rows and columns of data.
#
#    complex X(0:N1-1,0:N2-1), the data to be transformed.
#
#  Output:
#
#    complex Y(0:N1-1,0:N2-1), the Fourier coefficients.
#
  import numpy as  np

  y = np.zeros ( [ n1, n2 ], dtype = np.complex128 )

  for i2 in range ( 0, n2 ):
    for j2 in range ( 0, n2 ):
      theta2 = - 2.0 * np.pi * float ( i2 ) * float ( j2 ) / float ( n2 )
      cs2 = np.cos ( theta2 ) - 1j * np.sin ( theta2 )
      for i1 in range ( 0, n1 ):
        for j1 in range ( 0, n1 ):
          theta1 = - 2.0 * np.pi * float ( i1 ) * float ( j1 ) / float ( n1 )
          cs1 = np.cos ( theta1 ) - 1j * np.sin ( theta1 )
          y[i1,i2] = y[i1,i2] + x[j1,j2] * cs1 * cs2

  return y

def c8mat_sft_test ( rng ):

#*****************************************************************************80
#
## c8mat_sft_test() tests c8mat_sftb() and c8mat_sftf().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  n1 = 10
  n2 = 4

  print ( '' )
  print ( 'c8mat_sft_test():' )
  print ( '  c8mat_sftf() computes the forward slow Fourier transform.' )
  print ( '  c8mat_sftb() computes the backward slow Fourier transform.' )
  print ( '' )
  print ( '  The data has dimension N1 = %d by N2 = %d' % ( n1, n2 ) )

  x = c8mat_uniform_01 ( n1, n2, rng )

  c8mat_print_some ( n1, n2, x, 1, 1, 10, 10, '  The data X:' )
#
#  Compute the slow Fourier transform of the data.
#
  y = c8mat_sftf ( n1, n2, x )

  c8mat_print_some ( n1, n2, y, 1, 1, 10, 10, '  The Fourier coefficients Y:' )

  x2 = c8mat_sftb ( n1, n2, y )

  c8mat_print_some ( n1, n2, x2, 1, 1, 10, 10, '  The recovered data:' )

  return

def c8mat_uniform_01 ( m, n, rng ):

#*****************************************************************************80
#
## c8mat_uniform_01() returns a unit pseudorandom C8MAT.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the matrix.
#
#    rng: the current random number generator.
#
#  Output:
#
#    complex C(M,N), the pseudorandom complex matrix.
#
  import numpy as np

  c = np.zeros ( ( m, n ), 'complex' )

  for i2 in range ( 0, n ): 
    for i1 in range ( 0, m ):

      r = np.sqrt ( rng.random ( ) )

      theta = 2.0 * np.pi * rng.random ( )

      c[i1,i2] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c

def c8mat_uniform_01_test ( rng ):

#*****************************************************************************80
#
## c8mat_uniform_01_test() tests c8mat_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 December 2014
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

  m = 5
  n = 3

  print ( '' )
  print ( 'c8mat_uniform_01_test():' )
  print ( '  c8mat_uniform_01() computes a random C8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )

  v = c8mat_uniform_01 ( m, n, rng )

  c8mat_print ( m, n, v, '  Random C8MAT:' )

  return

def c8vec_indicator ( n ):

#*****************************************************************************80
#
## c8vec_indicator() sets a C8VEC to the indicator vector.
#
#  Discussion:
#
#    X(1:N) = ( 1-1i, 2-2i, 3-3i, 4-4i, ... )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#  Output:
#
#    complex A(N), the array.
#
  import numpy as np

  a = np.zeros ( n, 'complex' )

  for i in range ( 0, n ):
    a[i] = float ( i + 1 ) - float ( i + 1 ) * 1j

  return a

def c8vec_indicator_test ( ):

#*****************************************************************************80
#
## c8vec_indicator_test() tests c8vec_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'c8vec_indicator_test' )
  print ( '  c8vec_indicator returns the indicator vector.' )

  n = 10

  x = c8vec_indicator ( n )

  c8vec_print ( n, x, '  The indicator vector:' )

  return

def c8vec_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## c8vec_print_part() prints "part" of an C8VEC.
#
#  Discussion:
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    complex A(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )
    print ( '  ......  ..............  ..............' )
    i = n - 1
    print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '  %6d  %14g  %14g' % ( i, a.real[i], a.imag[i] ) )
    i = max_print - 1
    print ( '  %6d  %14g  %14g  ...more entries...' % ( i, a.real[i], a.imag[i] ) )

  return

def c8vec_print_part_test ( ):

#*****************************************************************************80
#
## c8vec_print_part_test() tests c8vec_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'c8vec_print_part_test' )
  print ( '  c8vec_print_part prints part of a C8VEC.' )

  n = 100
  a = c8vec_indicator ( n )

  max_print = 10

  c8vec_print_part ( n, a, max_print, '  Part of the C8VEC:' )

  return

def c8vec_print ( n, a, title ):

#*****************************************************************************80
#
## c8vec_print() prints a C8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    complex A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %12g  %12g' % ( i, a.real[i], a.imag[i] ) )

def c8vec_print_test ( ):

#*****************************************************************************80
#
## c8vec_print_test() tests c8vec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'c8vec_print_test' )
  print ( '  c8vec_print prints an C8VEC.' )

  n = 4
  v = np.array ( [ complex ( 1.0, 2.0 ), \
                   complex ( 3.0, 4.0 ), \
                   complex ( 5.0, 6.0 ), \
                   complex ( 7.0, 8.0 ) ], dtype = np.complex128 )
  c8vec_print ( n, v, '  Here is a C8VEC:' )

  return

def c8vec_sftb ( n, y ):

#*****************************************************************************80
#
## c8vec_sftb() computes a "slow" backward Fourier transform of a C8VEC.
#
#  Discussion:
#
#    SFTF and SFTB are inverses of each other.  If we begin with data
#    X and apply SFTF to get Y, and then apply SFTB to Y,
#    we should get back the original X.
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 0 <= I <= N - 1
#
#      X(I) = 1/N * Sum ( 0 <= J <= N - 1 ) Y(J) * exp ( 2 pi i I J / N )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data values.
#
#    complex Y(0:N-1), the Fourier coefficients.
#
#  Output:
#
#    complex X(0:N-1), the data.
#
  import numpy as np

  x = np.zeros ( n, dtype = np.complex128 )

  for k in range ( 0, n ):
    for j in range ( 0, n ):
      theta = - 2.0 * np.pi * float ( k ) * float ( j ) / float ( n )
      x[k] = x[k] + y[j] * ( np.cos ( theta ) + 1j * np.sin ( theta ) )

  for i in range ( 0, n ):
    x[i] = x[i] / float ( n )

  return x

def c8vec_sftf ( n, x ):

#*****************************************************************************80
#
## c8vec_sftf() computes a "slow" forward Fourier transform of a C8VEC.
#
#  Discussion:
#
#    SFTF and SFTB are inverses of each other.  If we begin with data
#    X and apply SFTF to get Y, and then apply SFTB to Y,
#    we should get back the original X.
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 0 <= I <= N - 1
#
#      Y(I) = Sum ( 0 <= J <= N - 1 ) X(J) * exp ( - 2 pi i I J / N )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data values.
#
#    complex X(0:N-1), the data to be transformed.
#
#  Output:
#
#    complex Y(0:N-1), the Fourier coefficients.
#
  import numpy as np

  y = np.zeros ( n, dtype = np.complex128 )

  for k in range ( 0, n ):
    for j in range ( 0, n ):
      theta = - 2.0 * np.pi * float ( k ) * float ( j ) / float ( n )
      y[k] = y[k] + x[j] * ( np.cos ( theta ) - 1j * np.sin ( theta ) )

  return y

def c8vec_sft_test ( rng ):

#*****************************************************************************80
#
## c8vec_sft_test() tests c8vec_sftb() and c8vec_sftf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  n = 36

  print ( '' )
  print ( 'c8vec_sft_test():' )
  print ( '  c8vec_sftf() computes the forward slow Fourier transform.' )
  print ( '  c8vec_sftb() computes the backward slow Fourier transform.' )
  print ( '' )
  print ( '  The number of data values, N = %d' % ( n ) )

  x = c8vec_uniform_01 ( n, rng )

  c8vec_print_part ( n, x, 10, '  The original data:' )
#
#  Compute the slow Fourier transform of the data.
#
  y = c8vec_sftf ( n, x )

  c8vec_print_part ( n, y, 10, '  The Fourier coefficients:' )
#
#  Now try to retrieve the data from the coefficients.
#
  x2 = c8vec_sftb ( n, y )

  c8vec_print_part ( n, x2, 10, '  The retrieved data:' )

  return

def c8vec_uniform_01 ( n, rng ):

#*****************************************************************************80
#
## c8vec_uniform_01() returns a unit pseudorandom C8VEC.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Input:
#
#    integer N, the number of values to compute.
#
#    rng: the current random number generator.
#
#  Output:
#
#    complex C(N), the pseudorandom complex vector.
#
  import numpy as np

  c = np.zeros ( n, 'complex' )

  for j in range ( 0, n ):

    r = np.sqrt ( rng.random ( ) )

    theta = 2.0 * np.pi * rng.random ( )

    c[j] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c

def c8vec_uniform_01_test ( rng ):

#*****************************************************************************80
#
## c8vec_uniform_01_test() tests c8vec_uniform_01().
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
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'c8vec_uniform_01_test():' )
  print ( '  c8vec_uniform_01() computes pseudorandom complex values' )
  print ( '  in the unit circle.' )
  print ( '' )
 
  n = 10

  x = c8vec_uniform_01 ( n, rng )

  for i in range ( 0, n ):
    print ( '  %6d  ( %f, %f )' % ( i, x[i].real, x[i].imag ) )

  return

def i4_modp ( i, j ):

#*****************************************************************************80
#
## i4_modp() returns the nonnegative remainder of I4 division.
#
#  Discussion:
#
#    If
#      NREM = i4_modp ( I, J )
#      NMULT = ( I - NREM ) / J
#    then
#      I = J * NMULT + NREM
#    where NREM is always nonnegative.
#
#    The MOD function computes a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, i4_modp(A,360) is between 0 and 360, always.
#
#  Example:
#
#        I     J     MOD  i4_modp    Factorization
#
#      107    50       7       7    107 =  2 *  50 + 7
#      107   -50       7       7    107 = -2 * -50 + 7
#     -107    50      -7      43   -107 = -3 *  50 + 43
#     -107   -50      -7      43   -107 =  3 * -50 + 43
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number to be divided.
#
#    integer J, the number that divides I.
#
#  Output:
#
#    integer VALUE, the nonnegative remainder when I is divided by J.
#
  import numpy as np

  if ( j == 0 ):
    print ( '' )
    print ( 'i4_modp - Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    raise Exception ( 'i4_modp - Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + np.abs ( j )

  return value

def i4_modp_test ( ):

#*****************************************************************************80
#
## i4_modp_test() tests i4_modp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 4

  n_vec = np.array ( ( 107, 107, -107, -107 ) )
  d_vec = np.array ( ( 50, -50, 50, -50 ) )

  print ( '' )
  print ( 'i4_modp_test' )
  print ( '  i4_modp factors a number' )
  print ( '  into a multiple M and a positive remainder R.' )
  print ( '' )
  print ( '    Number   Divisor  Multiple Remainder' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    r = i4_modp ( n, d )
    m = ( n - r ) // d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  print ( '' )
  print ( '  Repeat using Python % Operator:' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  return

def i4_wrap ( value, lo, hi ):

#*****************************************************************************80
#
## i4_wrap() forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    LO = 4, HI = 8
#
#    In   Out
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer VALUE, an integer value.
#
#    integer LO, HI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of VALUE.
#
  value = lo + ( ( value - lo ) % ( hi - lo + 1 ) )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## i4_wrap_test() tests i4_wrap().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'i4_wrap_test' )
  print ( '  i4_wrap forces an integer to lie within given limits.' )
  print ( '' )
  print ( '  ILO = %d' % ( ilo ) )
  print ( '  IHI = %d' % ( ihi ) )
  print ( '' )
  print ( '     I  i4_wrap(I)' )
  print ( '' )

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print ( '  %6d  %6d' % ( i, j ) )

  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## r8vec_indicator1_test() tests r8vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_indicator1_test' )
  print ( '  r8vec_indicator1 returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

  return

def r8vec_permute_cyclic ( n, k, a ):

#*****************************************************************************80
#
## r8vec_permute_cyclic() performs a cyclic permutation of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    For 0 <= K < N, this function cyclically permutes the input vector
#    to have the form
#
#     ( A(K+1), A(K+2), ..., A(N), A(1), ..., A(K) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of objects.
#
#    integer K, the increment used.
#
#    real A(N), the array to be permuted.
#
#  Output:
#
#    real B(N), the permuted array.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    ipk = i4_wrap ( i + k, 0, n - 1 )
    b[i] = a[ipk];

  return b

def r8vec_permute_cyclic_test ( ):

#*****************************************************************************80
#
## r8vec_permute_cyclic_test() tests r8vec_permute_cyclic().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_permute_cyclic_test' )
  print ( '  r8vec_permute_cyclic performa a cyclic permutation' )
  print ( '  of K positions on an R8VEC.' )

  k = 4
  print ( '' )
  print ( '  K = %d' % ( k ) )

  n = 10
  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  Original array X:' )

  x = r8vec_permute_cyclic ( n, k, x )

  r8vec_print ( n, x, '  Array after permutation:' )

  return

def r8vec_print_part ( n, a, i_lo, i_hi, title ):

#*****************************************************************************80
#
## r8vec_print_part() prints "part" of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8 values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2016
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
#    integer MAX_print, the maximum number of lines to print.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )

  for i in range ( max ( 0, i_lo ), min ( n, i_hi + 1 ) ):
    print ( '  %8d: %12g' % ( i, a[i] ) )

  return

def r8vec_print_part_test ( ):

#*****************************************************************************80
#
## r8vec_print_part_test() tests r8vec_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8vec_print_part_test' )
  print ( '  r8vec_print_part prints part of an R8VEC.' )

  n = 100
  a = r8vec_indicator1 ( n )

  r8vec_print_part ( n, a, 10, 20, '  Lines 10:20 of the vector:' )

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

def r8vec_print_some ( n, a, max_print, title ):

#*****************************************************************************80
#
## r8vec_print_some() prints "some" of an R8VEC.
#
#  Discussion:
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '  %6d  %14g' % ( i, a[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    print ( '  ......  ..............' )
    i = n - 1
    print ( '  %6d  %14g' % ( i, a[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    i = max_print - 1
    print ( '  %6d  %14g  ...more entries...' % ( i, a[i] ) )

  return

def r8vec_print_some_test ( ):

#*****************************************************************************80
#
## r8vec_print_some_test() tests r8vec_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8vec_print_some_test' )
  print ( '  r8vec_print_some prints some of an R8VEC.' )

  n = 100
  a = r8vec_indicator1 ( n )

  max_print = 10

  r8vec_print_some ( n, a, max_print, '  No more than 10 lines of this vector:' )

  return

def r8vec_sct ( n, x ):

#*****************************************************************************80
#
## r8vec_sct() computes a forward or backward "slow" cosine transform of an R8VEC.
#
#  Discussion:
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#      Y(1) = Sum ( 1 <= J <= N ) X(J)
#
#      For 2 <= I <= N-1:
#
#        Y(I) = 2 * Sum ( 1 <= J <= N ) X(J)
#          * cos ( PI * ( I - 1 ) * ( J - 1 ) / ( N - 1 ) )
#
#      Y(N) = Sum ( X(1:N:2) ) - Sum ( X(2:N:2) )
#
#    Applying the routine twice in succession should yield the original data,
#    multiplied by 2 * ( N + 1 ).  This is a good check for correctness
#    and accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data values.
#
#    real X(N), the data sequence.
#
#  Output:
#
#    real Y(N), the transformed data.
#
  import numpy as np

  y = np.zeros ( n )

  for i in range ( 0, n ):

    y[i] = x[0] / 2.0

    for j in range ( 1, n - 1 ):
      angle = np.pi * float ( ( i * j ) % ( 2 * ( n - 1 ) ) ) / float ( n - 1 )
      y[i] = y[i] + x[j] * np.cos ( angle )

    j = n - 1

    angle = np.pi * float ( ( i * j ) % ( 2 * ( n - 1 ) ) ) / float ( n - 1 )

    y[i] = y[i] + x[n-1] * np.cos ( angle ) / 2.0

  for i in range ( 0, n ):
    y[i] = 2.0 * y[i] * np.sqrt ( float ( n ) / float ( n - 1 ) )

  return y

def r8vec_sct_test ( rng ):

#*****************************************************************************80
#
## r8vec_sct_test() tests r8vec_sct().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 256
  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'r8vec_sct_test():' )
  print ( '  r8vec_sct() does a forward or backward slow cosine transform.' )
  print ( '' )
  print ( '  The number of data items is N = %d' % ( n ) )
#
#  Set the data values.
#
  c = alo + ( ahi - alo ) * rng.random ( size = n )

  r8vec_print_part ( n, c, 1, 10, '  The original data:' )
#
#  Compute the coefficients.
#
  d = r8vec_sct ( n, c )

  r8vec_print_part ( n, d, 1, 10, '  The cosine coefficients:' )
#
#  Now compute inverse transform of coefficients.  Should get back the
#  original data.

  e = r8vec_sct ( n, d )

  for i in range ( 0, n ):
    e[i] = e[i] / float ( 2 * n )

  r8vec_print_part ( n, e, 1, 10, '  The retrieved data:' )

  return

def r8vec_sftb ( n, azero, a, b ):

#*****************************************************************************80
#
## r8vec_sftb() computes a "slow" backward Fourier transform of an R8VEC.
#
#  Discussion:
#
#    SFTB and SFTF are inverses of each other.  If we begin with data
#    AZERO, A, and B, and apply SFTB to it, and then apply SFTF to the
#    resulting R vector, we should get back the original AZERO, A and B.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data values.
#
#    real AZERO, the constant Fourier coefficient.
#
#    real A(N/2), B(N/2), the Fourier coefficients.
#
#  Output:
#
#    real R(N), the reconstructed data sequence.
#
  import numpy as np

  r = np.zeros ( n )
  for i in range ( 0, n ):
    r[i] = azero

  for i in range ( 0, n ):
    for k in range ( 0, ( n // 2 ) ):
      theta = float ( ( k + 1 ) * i * 2 ) * np.pi / float ( n )
      r[i] = r[i] + a[k] * np.cos ( theta ) + b[k] * np.sin ( theta )

  return r

def r8vec_sftf ( n, r ):

#*****************************************************************************80
#
## r8vec_sftf() computes a "slow" forward Fourier transform of an R8VEC.
#
#  Discussion:
#
#    SFTF and SFTB are inverses of each other.  If we begin with data
#    R and apply SFTB to it, and then apply SFTB to the resulting AZERO, 
#    A, and B, we should get back the original R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data values.
#
#    real R(N), the data to be transformed.
#
#    real AZERO, = sum ( 1 <= I <= N ) R(I) / N.
#
#  Output:
#
#    real A(N/2), B(N/2), the Fourier coefficients.
#
  import numpy as np

  a = np.zeros ( ( n // 2 ) )
  b = np.zeros ( ( n // 2 ) )

  azero = np.sum ( r ) / float ( n )

  for i in range ( 0, (  n // 2 ) ):

    a[i] = 0.0
    b[i] = 0.0

    for j in range ( 0, n ):
      theta = float ( 2 * ( i + 1 ) * j ) * np.pi / float ( n )
      a[i] = a[i] + r[j] * np.cos ( theta )
      b[i] = b[i] + r[j] * np.sin ( theta )

    a[i] = a[i] / float ( n )
    b[i] = b[i] / float ( n )

    if ( ( n % 2 ) == 1 or i + 1 != ( n // 2 ) ):
      a[i] = 2.0 * a[i]
      b[i] = 2.0 * b[i]
 
  return azero, a, b

def r8vec_sft_n_test ( n, rng ):

#*****************************************************************************80
#
## r8vec_sft_n_test() tests r8vec_sftb() and r8vec_sftf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'r8vec_sft_n_test():' )
  print ( '  r8vec_sftf() computes the forward slow Fourier transform.' )
  print ( '  r8vec_sftb() computes the backward slow Fourier transform.' )
  print ( '' )
  print ( '  The number of data values, N = %d' % ( n ) )

  x = alo + ( ahi - alo ) * rng.random ( size = n )

  r8vec_print_some ( n, x, 10, '  The original data:' )
#
#  Compute the slow Fourier transform of the data.
#
  azero, a, b = r8vec_sftf ( n, x )

  print ( '' )
  print ( '  A (cosine) coefficients:' )
  print ( '' )

  print ( '  %4d  %g' % ( 0, azero ) )

  for i in range ( 0, ( n // 2 ) ):
    print ( '  %4d  %g' % ( i, a[i] ) )

  print ( '' )
  print ( '  B (sine) coefficients:' )
  print ( '' )

  for i in range ( 0, ( n // 2 ) ):
    print ( '  %4d  %g' % ( i, b[i] ) )
#
#  Now try to retrieve the data from the coefficients.
#
  x = r8vec_sftb ( n, azero, a, b )

  r8vec_print_some ( n, x, 10, '  The retrieved data:' )

  return

def r8vec_sft_test ( rng ):

#*****************************************************************************80
#
## r8vec_sft_test() tests r8vec_sftb() and r8vec_sftf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2017
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
  print ( 'r8vec_sft_test():' )

  r8vec_sft_n_test ( 35, rng )
  r8vec_sft_n_test ( 36, rng )

  return

def r8vec_sht ( n, a ):

#*****************************************************************************80
#
## r8vec_sht() computes a "slow" Hartley transform of an R8VEC.
#
#  Discussion:
#
#    The discrete Hartley transform B of a set of data A is
#
#      B(I) = 1/sqrt(N) * Sum ( 0 <= J <= N-1 ) A(J) * CAS(2*PI*I*J/N)
#
#    Here, the data and coefficients are indexed from 0 to N-1.
#
#    With the above normalization factor of 1/sqrt(N), the Hartley
#    transform is its own inverse.
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Ralph Hartley,
#    A More Symmetrical Fourier Analysis Applied to Transmission Problems,
#    Proceedings of the Institute of Radio Engineers,
#    Volume 30, pages 144-150, 1942.
#
#  Input:
#
#    integer N, the number of data values.
#
#    real A(N), the data to be transformed.
#
#  Output:
#
#    real B(N), the transformed data.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      theta = 2.0 * np.pi * float ( ( i * j ) % n ) / float ( n )
      b[i] = b[i] + a[j] * ( np.cos ( theta ) + np.sin ( theta ) )

  for i in range ( 0, n ):
    b[i] = b[i] / np.sqrt ( n )

  return b

def r8vec_sht_test ( rng ):

#*****************************************************************************80
#
## r8vec_sht_test() tests r8vec_sht().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 17
  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'r8vec_sht_test():' )
  print ( '  r8vec_sht() does a forward or backward slow Hartley transform.' )
  print ( '' )
  print ( '  The number of data items is N = %d' % ( n ) )
#
#  Set the data values.
#
  c = alo + ( ahi - alo ) * rng.random ( size = n )

  r8vec_print_part ( n, c, 1, 10, '  The original data:' )
#
#  Compute the coefficients.
#
  d = r8vec_sht ( n, c )

  r8vec_print_part ( n, d, 1, 10, '  The Hartley coefficients:' )
#
#  Now compute inverse transform of coefficients.  Should get back the
#  original data.

  e = r8vec_sht ( n, d )

  r8vec_print_part ( n, e, 1, 10, '  The retrieved data:' )

  return

def r8vec_sqctb ( n, x ):

#*****************************************************************************80
#
## r8vec_sqctb() computes a "slow" quarter cosine transform backward of an R8VEC.
#
#  Discussion:
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 0 <= I <= N-1,
#
#      Y(I) = X(0) + 2 Sum ( 1 <= J <= N-1 ) X(J) * cos ( PI * J * (I+1/2) / N )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Briggs, Van Emden Henson,
#    The Discrete Fourier Transform,
#    SIAM, 1995,
#    LC: QA403.5 B75
#
#  Input:
#
#    integer N, the number of data values.
#
#    real X(N), the data sequence.
#
#  Output:
#
#    real Y(N), the transformed data.
#
  import numpy as np

  y = np.zeros ( n )
  for i in range ( 0, n ):
    y[i] = x[0]

  for i in range ( 0, n ):
    for j in range ( 1, n ):
      theta = 0.5 * np.pi * float ( j * ( 2 * i + 1 ) ) / float ( n )
      y[i] = y[i] + 2.0 * x[j] * np.cos ( theta )

  return y

def r8vec_sqctf ( n, x ):

#*****************************************************************************80
#
## r8vec_sqctf() computes a "slow" quarter cosine transform forward of an R8VEC.
#
#  Discussion:
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 0 <= I <= N-1,
#
#      Y(I) = (1/N) Sum ( 0 <= J <= N-1 ) X(J) * cos ( PI * I * (J+1/2) / N )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Briggs, Van Emden Henson,
#    The Discrete Fourier Transform,
#    SIAM, 1995,
#    QA403.5 B75
#
#  Input:
#
#    integer N, the number of data values.
#
#    real X(N), the data sequence.
#
#  Output:
#
#    real Y(N), the transformed data.
#
  import numpy as np

  y = np.zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      theta = 0.5 * np.pi * float ( i * ( 2 * j + 1 ) ) / float ( n )
      y[i] = y[i] + x[j] * np.cos ( theta  )

  for i in range ( 0, n ):
    y[i] = y[i] / float ( n )

  return y

def r8vec_sqct_test ( rng ):

#*****************************************************************************80
#
## r8vec_sqct_test() tests r8vec_sqctb() and r8vec_sqctf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 256

  ahi = 5.0
  alo = 0.0

  print ( '' )
  print ( 'r8vec_sqct_test():' )
  print ( '  r8vec_sqctf() does a forward slow quarter wave cosine transform' )
  print ( '  r8vec_sqctb() does a backward slow quarter wave cosine transform.' )
  print ( '' )
  print ( '  The number of data items is N = %d' % ( n ) )
#
#  Set the data values.
#
  x = alo + ( ahi - alo ) * rng.random ( size = n )

  r8vec_print_part ( n, x, 1, 10, '  The original data:' )
#
#  Compute the coefficients.
#
  y = r8vec_sqctf ( n, x )

  r8vec_print_part ( n, y, 1, 10, '  The cosine coefficients:' )
#
#  Now compute inverse transform of coefficients.  Should get back the
#  original data.

  x = r8vec_sqctb ( n, y )

  r8vec_print_part ( n, x, 1, 10, '  The retrieved data:' )

  return

def r8vec_sqstb ( n, x ):

#*****************************************************************************80
#
## r8vec_sqstb() computes a "slow" quarter sine transform backward of an R8VEC.
#
#  Discussion:
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 0 <= I <= N-1,
#
#      Y(I) = -2 Sum ( 1 <= J <= N-1 ) X(J) * sin ( PI * J * (I+1/2) / N )
#             - X(N) * cos ( pi * I )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Briggs, Van Emden Henson,
#    The Discrete Fourier Transform,
#    SIAM, 1995,
#    QA403.5 B75
#
#  Input:
#
#    integer N, the number of data values.
#
#    real X(N), the data sequence.
#
#  Output:
#
#    real Y(N), the transformed data.
#
  import numpy as np

  y = np.zeros ( n )

  for i in range ( 0, n ):

    for j in range ( 0, n - 1 ):
      theta = 0.5 * np.pi * float ( j + 1 ) * float ( 2 * i + 1 ) / float ( n )
      y[i] = y[i] - 2.0 * x[j] * np.sin ( theta  )

    theta = np.pi * float ( i )
    y[i] = y[i] - x[n-1] * np.cos ( theta )

  return y

def r8vec_sqstf ( n, x ):

#*****************************************************************************80
#
## r8vec_sqstf() computes a "slow" quarter sine transform forward of an R8VEC.
#
#  Discussion:
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 1 <= I <= N,
#
#      Y(I) = -(1/N) Sum ( 0 <= J <= N-1 ) X(J) * sin ( PI * I * (J+1/2) / N )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Briggs, Van Emden Henson,
#    The Discrete Fourier Transform,
#    SIAM, 1995,
#    QA403.5 B75
#
#  Input:
#
#    integer N, the number of data values.
#
#    real X(N), the data sequence.
#
#  Output:
#
#    real Y(N), the transformed data.
#
  import numpy as np

  y = np.zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      theta = 0.5 * np.pi * float ( i + 1 ) * float ( 2 * j + 1 ) / float ( n )
      y[i] = y[i] + x[j] * np.sin ( theta  )

  for i in range ( 0, n ):
    y[i] = - y[i] / float ( n )

  return y

def r8vec_sqst_test ( rng ):

#*****************************************************************************80
#
## r8vec_sqst_test() tests r8vec_sqstb() and r8vec_sqstf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 256
  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'r8vec_sqst_test():' )
  print ( '  r8vec_sqstf() does a forward slow quarter wave sine transform' )
  print ( '  r8vec_sqstb() does a backward slow quarter wave sine transform.' )
  print ( '' )
  print ( '  The number of data items is N = %d' % ( n ) )
#
#  Set the data values.
#
  x = alo + ( ahi - alo ) * rng.random ( size = n )

  r8vec_print_part ( n, x, 1, 10, '  The original data:' )
#
#  Compute the coefficients.
#
  y = r8vec_sqstf ( n, x )

  r8vec_print_part ( n, y, 1, 10, '  The sine coefficients:' )
#
#  Now compute inverse transform of coefficients.  Should get back the
#  original data.

  x = r8vec_sqstb ( n, y )

  r8vec_print_part ( n, x, 1, 10, '  The retrieved data:' )

  return

def r8vec_sst ( n, x ):

#*****************************************************************************80
#
## r8vec_sst() computes a "slow" sine transform of an R8VEC.
#
#  Discussion:
#
#    This routine is provided for illustration and testing.  It is inefficient
#    relative to optimized routines that use fast Fourier techniques.
#
#    For 1 <= I <= N,
#
#      Y(I) = Sum ( 1 <= J <= N ) X(J) * sin ( PI * I * J / ( N + 1 ) )
#
#    Applying the routine twice in succession should yield the original data,
#    multiplied by N / 2.  This is a good check for correctness and accuracy.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data values.
#
#    real X(N), the data sequence.
#
#  Output:
#
#    real Y(N), the transformed data.
#
  import numpy as np

  y = np.zeros ( n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      y[j] = y[j] + 2.0 * x[i] \
        * np.sin ( float ( i + 1 ) * float ( j + 1 ) * np.pi / float ( n + 1 ) )

  return y

def r8vec_sst_test ( rng ):

#*****************************************************************************80
#
## r8vec_sst_test() tests r8vec_sst().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 256
  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'r8vec_sst_test():' )
  print ( '  r8vec_sst() does a forward or backward slow sine transform.' )
  print ( '' )
  print ( '  The number of data items is N = %d' % ( n ) )
#
#  Set the data values.
#
  c = alo + ( ahi - alo ) * rng.random ( size = n )

  r8vec_print_part ( n, c, 1, 10, '  The original data:' )
#
#  Compute the coefficients.
#
  d = r8vec_sst ( n, c )

  r8vec_print_part ( n, d, 1, 10, '  The sine coefficients:' )
#
#  Now compute inverse transform of coefficients.  Should get back the
#  original data.

  e = r8vec_sst ( n, d )

  for i in range ( 0, n ):
    e[i] = e[i] / 2.0 / float ( n + 1 )

  r8vec_print_part ( n, e, 1, 10, '  The retrieved data:' )

  return

def r8vec_swtb ( n, s, d ):

#*****************************************************************************80
#
## r8vec_swtb() computes a "slow" backward wavelet transform of an R8VEC.
#
#  Discussion:
#
#    This function inverts the D4 Daubechies wavelet.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data values.
#
#    real S((N+1)/2), D((N+1)/2), the transformed data.
#
#  Output:
#
#    real X(N), the original data sequence.
#
  import numpy as np
 
  if ( ( n % 2 ) == 1 ):
    n2 = n + 1
  else:
    n2 = n

  np1h = ( ( n + 1 ) // 2 )
  nh = ( n // 2 )

  for i in range ( 0, np1h ):
    d[i] = d[i] / ( ( np.sqrt ( 3.0 ) + 1.0 ) / np.sqrt ( 2.0 ) )
    s[i] = s[i] / ( ( np.sqrt ( 3.0 ) - 1.0 ) / np.sqrt ( 2.0 ) )

  for i in range ( 0, np1h ):
    ip1 = i4_wrap ( i + 1, 0, np1h - 1 )
    s[i] = s[i] + d[ip1]

  y = np.zeros ( n2 )

  for i in range ( 0, np1h ):
    im1 = i4_wrap ( i - 1, 0, np1h - 1 )
    y[2*i+1] = d[i] + np.sqrt ( 3.0 ) / 4.0 * s[i] \
      + ( np.sqrt ( 3.0 ) - 2.0 ) / 4.0 * s[im1]

  for i in range ( 0, np1h ):
    y[2*i] = s[i] - np.sqrt ( 3.0 ) * y[2*i+1]

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = y[i]

  return x

def r8vec_swtf ( n, x ):

#*****************************************************************************80
#
## r8vec_swtf() computes a "slow" forward wavelet transform of an R8VEC.
#
#  Discussion:
#
#    This function applies the D4 Daubechies wavelet.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of data values.
#
#    real X(N), the data sequence.
#
#  Output:
#
#    real S((N+1)/2), D((N+1)/2), the transformed data.
#
  import numpy as np

  if ( ( n % 2 ) == 1 ):
    n2 = n + 1
  else:
    n2 = n

  y = np.zeros ( n2 )

  for i in range ( 0, n ):
    y[i] = x[i]

  if ( n < n2 ):
    y[n] = 0.0

  np1h = ( ( n + 1 ) // 2 )

  d = np.zeros ( np1h )
  s = np.zeros ( np1h )

  for i in range ( 0, np1h ):
    s[i] = y[2*i] + np.sqrt ( 3.0 ) * y[2*i+1]

  for i in range ( 0, np1h ):
    im1 = i4_wrap ( i - 1, 0, np1h - 1 )
    d[i] = y[2*i+1] - np.sqrt ( 3.0 ) / 4.0 * s[i] \
      - ( np.sqrt ( 3.0 ) - 2.0 ) / 4.0 * s[im1]

  for i in range ( 0, np1h ):
    ip1 = i4_wrap ( i + 1, 0, np1h - 1 )
    s[i] = s[i] - d[ip1]

  for i in range ( 0, np1h ):
    s[i] = ( np.sqrt ( 3.0 ) - 1.0 ) / np.sqrt ( 2.0 ) * s[i]
    d[i] = ( np.sqrt ( 3.0 ) + 1.0 ) / np.sqrt ( 2.0 ) * d[i]

  return s, d

def r8vec_swt_test ( rng ):

#*****************************************************************************80
#
## r8vec_swt_test() tests r8vec_swtb() and r8vec_swtf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  n = 36
  alo = 0.0
  ahi = 5.0

  print ( '' )
  print ( 'r8vec_swt_test():' )
  print ( '  r8vec_swtf() computes the forward slow wavelet transform.' )
  print ( '  r8vec_swtb() computes the backward slow wavelet transform.' )
  print ( '' )
  print ( '  The number of data values, N = %d' % ( n ) )

  x = alo + ( ahi - alo ) * rng.random ( size = n )

  r8vec_print_part ( n, x, 1, 10, '  The original data:' )
#
#  Compute the slow wavelet transform of the data.
#
  s, d = r8vec_swtf ( n, x )

  print ( '' )
  print ( '     I          S(I)            D(I)' )
  print ( '' )
  for i in range ( 0, ( ( n + 1 ) // 2 ) ):
    print ( '  %4d  %14f  %14f' % ( i, s[i], d[i] ) )
#
#  Now try to retrieve the data from the coefficients.
#
  x = r8vec_swtb ( n, s, d )

  r8vec_print_part ( n, x, 1, 10, '  The retrieved data:' )

  return

def sftpack_test ( ):

#*****************************************************************************80
#
## sftpack_test() tests sftpack().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'sftpack_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test sftpack().' )

  rng = default_rng ( )
#
#  Utility functions.
#
  c8mat_print_test ( )
  c8mat_print_some_test ( )
  c8mat_uniform_01_test ( rng )
  c8vec_indicator_test ( )
  c8vec_print_test ( )
  c8vec_print_part_test ( )
  c8vec_uniform_01_test ( rng )
  i4_modp_test ( )
  i4_wrap_test ( )
  r8vec_indicator1_test ( )
  r8vec_print_part_test ( )
#
#  Library functions.
#
  c8mat_sft_test ( rng )
  c8vec_sft_test ( rng )

  r8vec_sct_test ( rng )
  r8vec_sft_test ( rng )
  r8vec_sht_test ( rng )
  r8vec_sqct_test ( rng )
  r8vec_sqst_test ( rng )
  r8vec_sst_test ( rng )
  r8vec_swt_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'sftpack_test():' )
  print ( '  Normal end of execution.' )
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
  sftpack_test ( )
  timestamp ( )

