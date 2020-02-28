#! /usr/bin/env python3
#
def i4_to_l4 ( i4 ):

#*****************************************************************************80
#
## I4_TO_L4 converts an I4 to an L4.
#
#  Discussion:
#
#    An I4 is an integer value.
#    An L4 is a boolean value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I4, an integer.
#
#    Output, boolean I4_TO_L4, the logical value of I4.
#
  value = ( i4 != 0 )

  return value

def i4_to_l4_test ( ):

#*****************************************************************************80
#
## I4_TO_L4_TEST tests I4_TO_L4. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'I4_TO_L4_TEST' )
  print ( '  I4_TO_L4 converts an I4 to an L4.' )
  print ( '' )
  print ( '  I4   L4' )
  print ( '' )

  for i4 in range ( -5, +6 ):

    l4 = i4_to_l4 ( i4 )
    print ( '  %2d  %s' % ( i4, l4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_TO_L4_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_to_l4vec ( i4, n ):

#*****************************************************************************80
#
## I4_TO_L4VEC converts an I4 into an L4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I4, the integer.
#
#    Input, integer N, the dimension of the vector.
#
#    Output, bool L4VEC(N), the vector of logical values.
#
  import numpy as np

  l4vec = np.zeros ( n, dtype = np.bool )

  for i in range ( n - 1, -1, -1 ):
    l4vec[i] = ( ( i4 % 2 ) == 1 )
    i4 = ( i4 // 2 )

  return l4vec

def i4_to_l4vec_test ( ):

#*****************************************************************************80
#
## I4_TO_L4VEC_TEST tests I4_TO_L4VEC. 
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
  print ( '' )
  print ( 'I4_TO_L4VEC_TEST' )
  print ( '  I4_TO_L4VEC converts an I4 to an L4VEC.' )
  print ( '' )
  print ( '  I4   L4VEC' )
  print ( '' )

  n = 8

  for i4 in range ( 0, 11 ):

    l4vec = i4_to_l4vec ( i4, n )
    print ( '  %2d: ' % ( i4 ), end = '' )
    for j in range ( 0, n ):
      print ( ' %1d' % ( l4vec[j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' ) 
  print ( 'I4_TO_L4VEC_TEST' )
  print ( '  Normal end of execution.' )
  return

def l4lib_test ( ):

#*****************************************************************************80
#
## L4LIB_TEST tests the L4LIB library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'L4LIB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the L4LIB library.' )

  i4_to_l4_test ( )
  i4_to_l4vec_test ( )

  l4_to_i4_test ( )
  l4_to_s_test ( )
  l4_uniform_test ( )
  l4_xor_test ( )

  l4mat_print_test ( )
  l4mat_print_some_test ( )
  l4mat_transpose_print_test ( )
  l4mat_transpose_print_some_test ( )
  l4mat_uniform_test ( )

  l4vec_next_test ( )
  l4vec_print_test ( )
  l4vec_uniform_test ( )

  s_to_l4_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4LIB_TEST:' )
  print ( '  Normal end of execution.' )
  print ( '' )
  return

def l4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## L4MAT_PRINT prints an L4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
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
#    Input, integer A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  l4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def l4mat_print_test ( ):

#*****************************************************************************80
#
## L4MAT_PRINT_TEST tests L4MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'L4MAT_PRINT_TEST:' )
  print ( '  L4MAT_PRINT prints an L4MAT.' )

  m = 5
  n = 12
  seed = 123456789
  a, seed = l4mat_uniform ( m, n, seed )
  title = '  A 5 x 3 integer matrix:'
  l4mat_print ( m, n, a, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def l4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## L4MAT_PRINT_SOME prints out a portion of an L4MAT.
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
#    Input, integer A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 35

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
      print ( '%2d' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( a[i,j] == 0 ):
          print ( ' F', end = '' )
        else:
          print ( ' T', end = '' )
      print ( '' )

  return

def l4mat_print_some_test ( ):

#*****************************************************************************80
#
## L4MAT_PRINT_SOME_TEST tests L4MAT_PRINT_SOME.
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
  import numpy as np

  print ( '' )
  print ( 'L4MAT_PRINT_SOME_TEST' )
  print ( '  L4MAT_PRINT_SOME prints some of an L4MAT.' )

  m = 4
  n = 6
  seed = 123456789
  v, seed = l4mat_uniform ( m, n, seed )
  l4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is L4MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def l4mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## L4MAT_TRANSPOSE_PRINT prints an L4MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
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
#    Input, integer A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  l4mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def l4mat_transpose_print_test ( ):

#*****************************************************************************80
#
## L4MAT_TRNSPOSE_PRINT_TEST tests L4MAT_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'L4MAT_TRANSPOSE_PRINT_TEST:' )
  print ( '  L4MAT_TRANSPOSE_PRINT prints an L4MAT transposed.' )

  m = 5
  n = 12
  seed = 123456789
  a, seed = l4mat_uniform ( m, n, seed )
  title = '  A 5 x 12 integer matrix:'
  l4mat_transpose_print ( m, n, a, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4MAT_TRANSPOSE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def l4mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## L4MAT_TRANSPOSE_PRINT_SOME prints some of an L4MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, integer A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 35

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
      print ( '%2d' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( ' %4d: ' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        if ( a[i,j] == 0 ):
          print ( ' F', end = '' )
        else:
          print ( ' T', end = '' )
      print ( '' )

  return

def l4mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## L4MAT_TRANSPOSE_PRINT_SOME_TEST tests L4MAT_TRANSPOSE_PRINT_SOME.
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
  import numpy as np

  print ( '' )
  print ( 'L4MAT_TRANSPOSE_PRINT_SOME_TEST' )
  print ( '  L4MAT_TRANSPOSE_PRINT_SOME prints some of an L4MAT, transposed.' )

  m = 4
  n = 6
  seed = 123456789
  v, seed = l4mat_uniform ( m, n, seed )
  l4mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  Here is L4MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4MAT_TRANSPOSE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def l4mat_uniform ( m, n, seed ):

#*****************************************************************************80
#
## L4MAT_UNIFORM returns a pseudorandom L4MAT.
#
#  Discussion:
#
#    An L4MAT is a two dimensional array of LOGICAL values.
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
#    Input, integer M, N, the order of the matrix.
#
#    Input/output, integer SEED, the "seed" value, which should
#    NOT be 0.  On output, SEED has been updated.
#
#    Output, logical L4MAT(M,N), a pseudorandom logical matrix.
#
  import numpy
  from sys import exit

  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'L4MAT_UNIFORM - Fatal error!' )
    print ( '  Input value of SEED = 0.' )
    exit ( 'L4MAT_UNIFORM - Fatal error!' )

  l4mat = numpy.zeros ( ( m, n ) )

  for j in range ( 0, n ):

    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      if ( seed < 0 ):
        seed = seed + i4_huge

      l4mat[i][j] = ( i4_huge_half < seed )

  return l4mat, seed

def l4mat_uniform_test ( ):

#*****************************************************************************80
#
## L4MAT_UNIFORM_TEST tests L4MAT_UNIFORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'L4MAT_UNIFORM_TEST' )
  print ( '  L4MAT_UNIFORM computes a random L4MAT.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = l4mat_uniform ( m, n, seed )

  l4mat_print ( m, n, v, '  Random L4MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4MAT_UNIFORM_TEST:' )
  print ( '  Normal end of execution.' )

  return

def l4_to_i4 ( l ):

#*****************************************************************************80
#
## L4_TO_I4 converts an L4 to an I4.
#
#  Discussion:
#
#    0 is FALSE, and anything else if TRUE.
#
#    An I4 is an integer value.
#    An L4 is a logical value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, bool L, a logical value.
#
#    Output, integer VALUE, the integer value of L.
#
  if ( l ):
    value = 1
  else:
    value = 0

  return value

def l4_to_i4_test ( ):

#*****************************************************************************80
#
## L4_TO_I4_TEST tests L4_TO_I4. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'L4_TO_I4_TEST' )
  print ( '  L4_TO_I4 converts an L4 to an I4.' )
  print ( '' )
  print ( '      L4   I4' )
  print ( '' )

  l4 = False
  i4 = l4_to_i4 ( l4 )
  print ( '   %5s    %1d' % ( l4, i4 ) )

  l4 = True
  i4 = l4_to_i4 ( l4 )
  print ( '   %5s    %1d' % ( l4, i4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4_TO_I4_TEST' )
  print ( '  Normal end of execution.' )

def l4_to_s ( l4 ):

#*****************************************************************************80
#
## L4_TO_S converts an L4 to a string.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, bool L4, a logical value.
#
#    Output, string VALUE, the string.
#
  if ( l4 ):
    value = 'True'
  else:
    value = 'False'

  return value

def l4_to_s_test ( ):

#*****************************************************************************80
#
## L4_TO_S_TEST tests L4_TO_S. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'L4_TO_S_TEST' )
  print ( '  L4_TO_S converts an L4 to a string.' )
  print ( '' )
  print ( '      L4   S' )
  print ( '' )

  l4 = False
  s= l4_to_s ( l4 )
  print ( '   %5s    %s' % ( l4, s ) )

  l4 = True
  s = l4_to_s ( l4 )
  print ( '   %5s    %s' % ( l4, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4_TO_S_TEST' )
  print ( '  Normal end of execution.' )

def l4_uniform ( seed ):

#*****************************************************************************80
#
## L4_UNIFORM returns a pseudorandom L4.
#
#  Discussion:
#
#    An L4 is a LOGICAL value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2013
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
#    Input, integer SEED, the "seed" value, which should NOT be 0. 
#
#    Output, logical VALUE, a pseudorandom logical value.
#
#    Output, integer SEED, the updated seed value.
#
  from sys import exit

  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  seed = ( seed % i4_huge )

  if ( seed == 0 ):
    print ( '' )
    print ('L4_UNIFORM - Fatal error!' )
    print ( '  Input value of SEED = 0.' )
    exit ( 'L4_UNIFORM - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  value = ( i4_huge_half < seed )

  return value, seed

def l4_uniform_test ( ):

#*****************************************************************************80
#
## L4_UNIFORM_TEST tests L4_UNIFORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'L4_UNIFORM_TEST' )
  print ( '  L4_UNIFORM returns random logical values' )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):
    l4, seed = l4_uniform ( seed )
    print ( '  %d' % ( l4 ) )

  print ( '' )
  print ( 'L4_UNIFORM_TEST' )
  print ( '  Normal end of execution' )

  return

def l4vec_next ( n, l4vec ):

#*****************************************************************************80
#
## L4VEC_NEXT generates the next logical vector.
#
#  Discussion:
#
#    In the following discussion, we will let '0' stand for FALSE and
#    '1' for TRUE.
#
#    The vectors have the order
#
#      (0,0,...,0),
#      (0,0,...,1),
#      ...
#      (1,1,...,1)
#
#    and the "next" vector after (1,1,...,1) is (0,0,...,0).  That is,
#    we allow wrap around.
#
#  Example:
#
#    N = 3
#
#    Input      Output
#    -----      ------
#    0 0 0  =>  0 0 1
#    0 0 1  =>  0 1 0
#    0 1 0  =>  0 1 1
#    0 1 1  =>  1 0 0
#    1 0 0  =>  1 0 1
#    1 0 1  =>  1 1 0
#    1 1 0  =>  1 1 1
#    1 1 1  =>  0 0 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, logical L4VEC(N), the vector whose successor is desired.
#
#    Output, logical L4VEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( not l4vec[i] ):
      l4vec[i] = True
      break

    l4vec[i] = False

  return l4vec

def l4vec_next_test ( ):

#*****************************************************************************80
#
## L4VEC_NEXT_TEST tests L4VEC_NEXT.
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
  import numpy as np

  print ( '' )
  print ( 'L4VEC_NEXT_TEST' )
  print ( '  L4VEC_NEXT generates logical vectors of dimension N one at a time.' )

  for n in range ( 2, 4 ):

    print ( '' )
    print ( '  Vector size N = %d' % ( n ) )
    print ( '' )

    k = 0

    l4vec = np.zeros ( n, dtype = np.bool )

    for i in range ( 0, n ):
      l4vec[i] = False

    while ( True ):

      print ( '  %2d:  ' % ( k ), end = '' )
      for i in range ( 0, n ):
        print ( '  %s' % ( l4vec[i] ), end = '' )
      print ( '' )

      l4vec = l4vec_next ( n, l4vec )

      if ( not any ( l4vec ) ):
        break

      k = k + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'L4VEC_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def l4vec_print ( n, a, title ):

#*****************************************************************************80
#
## L4VEC_PRINT prints an L4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    if ( a[i] == 0 ):
      print ( '%6d  F' % ( i ) )
    else:
      print ( '%6d  T' % ( i ) )

  return

def l4vec_print_test ( ):

#*****************************************************************************80
#
## L4VEC_PRINT_TEST tests L4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'L4VEC_PRINT_TEST' )
  print ( '  L4VEC_PRINT prints an L4VEC.' )

  n = 10
  seed = 123456789
  v, seed = l4vec_uniform ( n, seed )
  l4vec_print ( n, v, '  Here is an L4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def l4vec_uniform ( n, seed ):

#*****************************************************************************80
#
## L4VEC_UNIFORM returns a pseudorandom L4VEC.
#
#  Discussion:
#
#    An L4VEC is a vector of LOGICAL values.
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
#    Input, integer N, the order of the vector.
#
#    Input, integer SEED, the "seed" value, which should NOT be 0.
#
#    Output, logical L4VEC(N), a pseudorandom logical vector.
#
#    Output, integer SEED, the updated seed.
#
  import numpy
  from sys import exit

  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'L4VEC_UNIFORM - Fatal error!' )
    print ( '  Input value of SEED = 0.' )
    exit ( 'L4VEC_UNIFORM - Fatal error!' )

  l4vec = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    l4vec[i] = ( i4_huge_half < seed )

  return l4vec, seed

def l4vec_uniform_test ( ):

#*****************************************************************************80
#
## L4VEC_UNIFORM_TEST tests L4VEC_UNIFORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'L4VEC_UNIFORM_TEST' )
  print ( '  L4VEC_UNIFORM computes a random L4VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = l4vec_uniform ( n, seed )

  l4vec_print ( n, v, '  Random L4VEC:' )

  print ( '' )
  print ( 'L4VEC_UNIFORM_TEST:' )
  print ( '  Normal end of execution.' )

  return

def l4_xnor ( l1, l2 ):

#*****************************************************************************80
#
## L4_XBOR returns the complement exclusive OR of two L4's.
#
#  Discussion:
#
#    An L4 is a logical value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2017
#
#  Author:
#
#   John Burkardt
#
#  Parameters:
#
#    Input, bool L1, L2, two values.
#
#    Output, bool VALUE, the complement exclusive OR of L1 and L2.
#
  value =  ( (       l1   and       l2   ) or \
             ( ( not l1 ) and ( not l2 ) ) )

  return value

def l4_xnor_test ( ):

#*****************************************************************************80
#
## L4_XNOR_TEST tests L4_XNOR. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'L4_XNOR_TEST' )
  print ( '  L4_XNOR computes the complement exclusive OR of two L4\'s' )
  print ( '' )
  print ( '      L1      L2  L4_XOR(L1,L2)' )
  print ( '' )

  for l1 in ( False, True ):
    for l2 in ( False, True ):
      l4 = l4_xnor ( l1, l2 )
      print ( '   %5s   %5s    %5s' % ( l1, l2, l4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4_XNOR_TEST' )
  print ( '  Normal end of execution.' )
  return

def l4_xor ( l1, l2 ):

#*****************************************************************************80
#
## L4_XOR returns the exclusive OR of two L4's.
#
#  Discussion:
#
#    An L4 is a logical value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#   John Burkardt
#
#  Parameters:
#
#    Input, bool L1, L2, two values whose exclusive OR is needed.
#
#    Output, bool VALUE, the exclusive OR of L1 and L2.
#
  value =  ( (       l1   and ( not l2 ) ) or \
             ( ( not l1 ) and       l2   ) )

  return value

def l4_xor_test ( ):

#*****************************************************************************80
#
## L4_XOR_TEST tests L4_XOR. 
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'L4_XOR_TEST' )
  print ( '  L4_XOR computes the exclusive OR of two L4\'s' )
  print ( '' )
  print ( '      L1      L2  L4_XOR(L1,L2)' )
  print ( '' )

  for l1 in ( False, True ):
    for l2 in ( False, True ):
      l4 = l4_xor ( l1, l2 )
      print ( '   %5s   %5s    %5s' % ( l1, l2, l4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'L4_XOR_TEST' )
  print ( '  Normal end of execution.' )
  return

def s_to_l4 ( s ):

#*****************************************************************************80
#
## S_TO_L4 reads a logical value from a string.
#
#  Discussion:
#
#    There are several ways of representing logical data that this routine
#    recognizes:
#
#      False   True
#      -----   ----
#
#      0       1
#      F       T
#      f       t
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S, the string to be read.
#
#    Output, bool L, the logical value read from the string.
#
  from sys import exit

  s_length = len ( s )

  for i in range ( 0, s_length ):

    if ( s[i] == '0' or s[i] == 'F' or s[i] == 'f' ):
      l = False
      return l
    elif ( s[i] == '1' or s[i] == 'T' or s[i] == 't' ):
      l = True
      return l

  print ( '' )
  print ( 'S_TO_L4 - Fatal error!' )
  print ( '  The input string did not contain logical data.' )
  exit ( 'S_TO_L4 - Fatal error!' )

def s_to_l4_test ( ):

#*****************************************************************************80
#
## S_TO_L4_TEST tests S_TO_L4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 November 2015
#
#  Author:
#
#    John Burkardt
#
  test_num = 10

  import numpy as np

  s_test = [ \
    '0      ', \
    'F      ', \
    'f      ', \
    '1      ', \
    'T      ', \
    't      ', \
    '  0    ', \
    '  1  0 ', \
    '  01   ', \
    '  Talse' ]

  print ( '' )
  print ( 'S_TO_L4_TEST' )
  print ( '  S_TO_L4 reads logical data from a string.' )
  print ( '' )
  print ( '        S   L4' )
  print ( '' )

  for test in range ( 0, test_num ):
    s = s_test[test]
    l4 = s_to_l4 ( s )
    print ( '  "%7s"  %s' % ( s, l4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'S_TO_L4_TEST' )
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
  l4lib_test ( )
  timestamp ( )

