#! /usr/bin/env python3
#
def c8_normal_01 ( ):

#*****************************************************************************80
#
## c8_normal_01() returns a unit normally distributed complex number.
#
#  Discussion:
#
#    The value has mean 0 and standard deviation 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    complex C, a sample of the PDF.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  v1 = rng.random ( )
  v2 = rng.random ( )

  x = np.sqrt ( - 2.0 * np.log ( v1 ) ) * np.cos ( 2.0 * np.pi * v2 )
  y = np.sqrt ( - 2.0 * np.log ( v1 ) ) * np.sin ( 2.0 * np.pi * v2 )

  c = x + y * 1j

  return c

def c8_normal_01_test ( ):

#*****************************************************************************80
#
## c8_normal_01_test() tests c8_normal_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'c8_normal_01_test' )
  print ( '  c8_normal_01 computes pseudonormal complex values.' )
  print ( '' )

  for i in range ( 1, 11 ):
    c = c8_normal_01 ( )
    print ( '  %6d  ( %f, %f )' % ( i, c.real, c.imag ) )

  return

def i4_normal_ab ( mu, sigma ):

#*****************************************************************************80
#
## i4_normal_ab() returns a scaled pseudonormal I4.
#
#  Discussion:
#
#    The normal probability distribution function (PDF) is sampled,
#    with mean MU and standard deviation SIGMA.
#
#    The result is rounded to the nearest integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real MU, the mean of the PDF.
#
#    real SIGMA, the standard deviation of the PDF.
#
#  Output:
#
#    integer VALUE, a normally distributed random value.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  r1 = rng.random ( )
  r2 = rng.random ( )
  value = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )
  value = int ( mu + sigma * value )

  return value

def i4_normal_ab_test ( ):

#*****************************************************************************80
#
## i4_normal_ab_test() tests i4_normal_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'i4_normal_ab_test' )
  print ( '  i4_normal_ab() computes integer pseudonormal values with' )
  print ( '  mean MU and standard deviation SIGMA.' )

  mu = 10.0
  sigma = 2.0

  print ( '' )
  print ( '  MU = %g' % ( mu ) )
  print ( '  SIGMA = %g' % ( sigma ) )
  print ( '' )
  for i in range ( 0, 10 ):
    i4 = i4_normal_ab ( mu, sigma )
    print ( '  %2d  %12d' % ( i, i4 ) )

  return

def normal_test ( ):

#*****************************************************************************80
#
## normal_test() tests normal().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'normal_test:' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test normal().' )

  c8_normal_01_test ( )
  i4_normal_ab_test ( )
  r8_normal_01_test ( )
  r8_normal_ab_test ( )
  r8mat_normal_01_test ( )
  r8mat_normal_ab_test ( )
  r8vec_normal_01_test ( )
  r8vec_normal_ab_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'normal_test():' )
  print ( '  Normal end of execution.' )
  return

def r8mat_normal_01 ( m, n ):

#*****************************************************************************80
#
## r8mat_normal_01() returns a unit pseudonormal R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#  Output:
#
#    real X(M,N), the pseudorandom values.
#
  import numpy as np

  x = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      x[i,j] = r8_normal_01 ( )

  return x

def r8mat_normal_01_test ( ):

#*****************************************************************************80
#
## r8mat_normal_01_test() tests r8mat_normal_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'r8mat_normal_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_normal_01 returns a matrix of Normal 01 values' )
  print ( '' )

  r = r8mat_normal_01 ( m, n )

  r8mat_print ( m, n, r, '  Matrix:' )

  return

def r8mat_normal_ab ( m, n, mu, sigma ):

#*****************************************************************************80
#
## r8mat_normal_ab() returns a scaled pseudonormal R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns.
#
#    real MU, SIGMA, the mean and standard deviation.
#
#  Output:
#
#    real X(M,N), the pseudorandom values.
#
  import numpy as np

  x = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      x[i,j] = mu + sigma * r8_normal_01 ( )

  return x

def r8mat_normal_ab_test ( ):

#*****************************************************************************80
#
## r8mat_normal_ab_test() tests r8mat_normal_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_normal_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_normal_ab returns a matrix of Normal AB values' )

  m = 5
  n = 4
  mu = 100.0
  sigma = 5.0

  print ( '' )
  print ( '  Mean = %g' % ( mu ) )
  print ( '  Standard deviation = %g' % ( sigma ) )

  r = r8mat_normal_ab ( m, n, mu, sigma )

  r8mat_print ( m, n, r, '  Matrix:' )

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

def r8_normal_01 ( ):

#*****************************************************************************80
#
## r8_normal_01() samples the standard normal probability distribution.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#    The Box-Muller method is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real X, a sample of the standard normal PDF.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  r1 = rng.random ( )
  r2 = rng.random ( )

  x = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  return x

def r8_normal_01_test ( ):

#*****************************************************************************80
#
## r8_normal_01_test() tests r8_normal_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  test_num = 20

  print ( '' )
  print ( 'r8_normal_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_normal_01 generates normally distributed' )
  print ( '  random values.' )
  print ( '' )

  for test in range ( 0, test_num ):

    x = r8_normal_01 ( )
    print ( '  %f' % ( x ) )

  return

def r8_normal_ab ( a, b ):

#*****************************************************************************80
#
## r8_normal_ab() returns a scaled pseudonormal R8.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, the mean of the normal PDF.
#
#    real B, the standard deviation of the normal PDF.
#
#  Output:
#
#    real X, a sample of the standard normal PDF.
#
  x = a + b * r8_normal_01 ( )
 
  return x

def r8_normal_ab_test ( ):

#*****************************************************************************80
#
## r8_normal_ab_test() tests r8_normal_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  x_mean = 100.0
  x_std = 10.0
  test_num = 20

  print ( '' )
  print ( 'r8_normal_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_normal_ab generates normally distributed values' )
  print ( '  with given mean and standard deviation.' )
  print ( '' )
  print ( '  MEAN = %g' % ( x_mean ) )
  print ( '  STD = %g' % ( x_std ) )
  print ( '' )

  for test in range ( 0, test_num ):

    x = r8_normal_ab ( x_mean, x_std )
    print ( '  %g' % ( x ) )

  return

def r8vec_normal_01 ( n ):

#*****************************************************************************80
#
## r8vec_normal_01() returns a unit pseudonormal R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = r8_normal_01 ( )

  return x

def r8vec_normal_01_test ( ):

#*****************************************************************************80
#
## r8vec_normal_01_test() tests r8vec_normal_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10

  print ( '' )
  print ( 'r8vec_normal_01_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_normal_01 returns a vector of Normal 01 values' )
  print ( '' )

  r = r8vec_normal_01 ( n )

  r8vec_print ( n, r, '  Vector:' )

  return

def r8vec_normal_ab ( n, mu, sigma ):

#*****************************************************************************80
#
## r8vec_normal_ab() returns a scaled pseudonormal R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real MU, the average value of the PDF.
#
#    real SIGMA, the standard deviation of the PDF.
#
#  Output:
#
#    real X(N), the vector of pseudorandom values.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = mu + sigma * r8_normal_01 ( )

  return x

def r8vec_normal_ab_test ( ):

#*****************************************************************************80
#
## r8vec_normal_ab_test() tests r8vec_normal_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_normal_ab_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_normal_ab returns a vector of Normal AB values' )

  n = 10
  mu = 15.0
  sigma = 0.25

  print ( '' )
  print ( '  Mean = %g' % ( mu ) )
  print ( '  Standard deviation = %g' % ( sigma ) )

  r = r8vec_normal_ab ( n, mu, sigma )

  r8vec_print ( n, r, '  Vector:' )

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
  normal_test ( )
  timestamp ( )

