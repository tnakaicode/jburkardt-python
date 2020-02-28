#! /usr/bin/env python3
#
def r4_exp ( x ):

#*****************************************************************************80
#
## R4_EXP computes the exponential function, avoiding overflow and underflow.
#
#  Discussion:
#
#    For arguments of very large magnitude, the evaluation of the
#    exponential function can cause computational problems.  Some languages
#    and compilers may return an infinite value or a "Not-a-Number".  
#    An alternative, when dealing with a wide range of inputs, is simply
#    to truncate the calculation for arguments whose magnitude is too large.
#    Whether this is the right or convenient approach depends on the problem
#    you are dealing with, and whether or not you really need accurate
#    results for large magnitude inputs, or you just want your code to
#    stop crashing.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the exponential function.
#
#    Output, real VALUE, the value of exp ( X ).
#
  import numpy as np

  r4_huge = 1.0E+30
  r4_log_max = +69.0776
  r4_log_min = -69.0776

  if ( x <= r4_log_min ):
    value = 0.0
  elif ( x < r4_log_max ):
    value = np.exp ( x )
  else:
    value = r4_huge

  return value

def r4_exp_test ( ):

#*****************************************************************************80
#
## R4_EXP_TEST tests R4_EXP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R4_EXP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4_EXP returns the exponential of a real number.' )
  print ( '' )
  print ( '        X           R4_EXP(X)' )
  print ( '' )

  for i in range ( -80, +90, 10 ):
    x = float ( i )
    print ( '  %12g  %12g' % ( x, r4_exp ( x ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4_EXP_TEST' )
  print ( '  Normal end of execution.' )
  return

def r4lib_test ( ):

#*****************************************************************************80
#
## R4LIB_TEST tests the R4LIB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R4LIB_TEST' )
  print ( '  Python version:' )
  print ( '  Test the R4LIB library.' )

  r4_exp_test ( )
  r4_uniform_01_test ( )
  r4_uniform_ab_test ( )

  r4mat_print_test ( )
  r4mat_print_some_test ( )
  r4mat_uniform_01_test ( )
  r4mat_uniform_ab_test ( )

  r4vec_covariance_test ( )
  r4vec_print_test ( )
  r4vec_uniform_01_test ( )
  r4vec_uniform_ab_test ( )

  timestamp_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4LIB_TEST:' )
  print ( '  Normal end of execution.' )

def r4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R4MAT_PRINT prints an R4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
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
  r4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r4mat_print_test ( ):

#*****************************************************************************80
#
## R4MAT_PRINT_TEST tests R4MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R4MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4MAT_PRINT prints an R4MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float32 )
  r4mat_print ( m, n, v, '  Here is an R4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R4MAT_PRINT_SOME prints out a portion of an R4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 September 2018
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

  for j2lo in range ( max ( jlo, 0 ), min ( jhi, n - 1 ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r4mat_print_some_test ( ):

#*****************************************************************************80
#
## R4MAT_PRINT_SOME_TEST tests R4MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R4MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4MAT_PRINT_SOME prints some of an R4MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float32 )
  r4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## R4MAT_UNIFORM_01 returns a unit pseudorandom R4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
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
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.
#
#    Output, real R(M,N), an array of random values between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R4MAT_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R4MAT_UNIFORM_01 - Fatal error!' )

  r = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = seed * 4.656612875E-10

  return r, seed

def r4mat_uniform_01_test ( ):

#*****************************************************************************80
#
## R4MAT_UNIFORM_01_TEST tests R4MAT_UNIFORM_01.
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

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'R4MAT_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4MAT_UNIFORM_01 computes a random R4MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r4mat_uniform_01 ( m, n, seed )

  r4mat_print ( m, n, v, '  Random R4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4MAT_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## R4MAT_UNIFORM_AB returns a scaled pseudorandom R4MAT.
#
#  Discussion:
#
#    An R4MAT is an array of R4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
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
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.
#
#    Output, real R(M,N), an array of random values between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R4MAT_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R4MAT_UNIFORM_AB - Fatal error!' )

  r = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r4mat_uniform_ab_test ( ):

#*****************************************************************************80
#
## R4MAT_UNIFORM_AB_TEST tests R4MAT_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R4MAT_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4MAT_UNIFORM_AB computes a random R4MAT.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r4mat_uniform_ab ( m, n, a, b, seed )

  r4mat_print ( m, n, v, '  Uniform R4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4MAT_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4_uniform_01 ( seed ):

#*****************************************************************************80
#
## R4_UNIFORM_01 returns a unit pseudorandom R4.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      R4_UNIFORM_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
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
#  Parameters:
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#    Output, real R, a random value between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  from sys import exit

  i4_huge = 2147483647

  if ( seed == 0 ):
    print ( '' )
    print ( 'R4_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R4_UNIFORM_01 - Fatal error!' )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r4_uniform_01_test ( ):

#*****************************************************************************80
#
## R4_UNIFORM_01_TEST tests R4_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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

  print ( '' )
  print ( 'R4_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4_UNIFORM_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  R4_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r4_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789

  print ( '' )
  print ( '  SEED  R4_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r4_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4_UNIFORM_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def r4_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## R4_UNIFORM_AB returns a scaled pseudorandom R4.
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
#  Parameters:
#
#    Input, real A, B, the minimum and maximum values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real R, the randomly chosen value.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from sys import exit

  i4_huge = 2147483647

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R4_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R4_UNIFORM_AB - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r4_uniform_ab_test ( ):

#*****************************************************************************80
#
## R4_UNIFORM_AB_TEST tests R4_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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

  a = 10.0
  b = 20.0

  print ( '' )
  print ( 'R4_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4_UNIFORM_AB returns random values in a given range:' )
  print ( '  [ A, B ]' )
  print ( '' )
  print ( '  For this problem:' )
  print ( '  A = %f' % ( a ) )
  print ( '  B = %f' % ( b ) )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):
    r, seed = r4_uniform_ab ( a, b, seed )
    print ( '  %f' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4_UNIFORM_AB_TEST' )
  print ( '  Normal end of execution' )
  return

def r4vec_covariance ( n, x, y ):

#*****************************************************************************80
#
## R4VEC_COVARIANCE computes the covariance of two vectors.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer N, the dimension of the two vectors.
#
#    Input, real X(N), Y(N), the two vectors.
#
#    Output, real VALUE, the covariance of the two vectors.
#
  import numpy as np

  x_average = np.mean ( x[0:n] )
  y_average = np.mean ( y[0:n] )
  
  value = 0.0
  for i in range ( 0, n ):
    value = value + ( x[i] - x_average ) * ( y[i] - y_average )

  value = value / float ( n - 1 )

  return value

def r4vec_covariance_test ( ):

#*****************************************************************************80
#
## R4VEC_COVARIANCE_TEST tests R4VEC_COVARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R4VEC_COVARIANCE_TEST:' )
  print ( '  R4VEC_COVARIANCE computes the covariance of two R4VECs.' )

  seed = 123456789

  n = 2

  v1 = np.array ( [ 1.0, 0.0 ] )
  print ( '' )
  print ( '  Vector V1:' ),
  for i in range ( 0, n ):
    print ( '%g' % ( v1[i] ) ),
  print ( '' )

  seed = 123456789
  for i in range ( 0, 12 ):
    angle = float ( 2 * i ) * np.pi / 12.0
    r, seed = r4_uniform_01 ( seed )
    v2 = r * np.array ( [ np.cos(angle), np.sin(angle) ] )
    print ( '' )
    print ( '  Vector V2:' ),
    for i in range ( 0, n ):
      print ( '%g' % ( v2[i] ) ),
    print ( '' )
    value = r4vec_covariance ( n, v1, v2 )
    print ( '  Covariance(V1,V2) = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4VEC_COVARIANCE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r4vec_print ( n, a, title ):

#*****************************************************************************80
#
## R4VEC_PRINT prints an R4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
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
    print ( '%6d  %12g' % ( i, a[i] ) )

def r4vec_print_test ( ):

#*****************************************************************************80
#
## R4VEC_PRINT_TEST tests R4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R4VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4VEC_PRINT prints an R4VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float32 )
  r4vec_print ( n, v, '  Here is an R4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R4VEC_UNIFORM_01 returns a unit pseudorandom R4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
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
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R4VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R4VEC_UNIFORM_01 - Fatal error!' )

  x = np.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r4vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R4VEC_UNIFORM_01_TEST tests R4VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R4VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4VEC_UNIFORM_01 computes a random R4VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r4vec_uniform_01 ( n, seed )

  r4vec_print ( n, v, '  Uniform R4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4VEC_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## R4VEC_UNIFORM_AB returns a scaled pseudorandom R4VEC.
#
#  Discussion:
#
#    Each dimension ranges from A to B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Springer Verlag, pages 201-202, 1983.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, pages 362-376, 1986.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, pages 136-143, 1969.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R4VEC_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R4VEC_UNIFORM_AB - Fatal error!' )

  x = np.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = a + ( b - a ) * seed * 4.656612875E-10

  return x, seed

def r4vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## R4VEC_UNIFORM_AB_TEST tests R4VEC_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R4VEC_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4VEC_UNIFORM_AB computes a random R4VEC.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r4vec_uniform_ab ( n, a, b, seed )

  r4vec_print ( n, v, '  Uniform R4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4VEC_UNIFORM_AB_TEST:' )
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
  r4lib_test ( )
  timestamp ( )

