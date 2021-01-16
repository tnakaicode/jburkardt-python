#! /usr/bin/env python3
#
def bvec_add ( n, bvec1, bvec2 ):

#*****************************************************************************80
#
## BVEC_ADD adds two binary vectors.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Example:
#
#    N = 4
#
#    BVEC1    dec  BVEC2    dec  BVEC3    dec
#    -------  ---  -------  ---  -------  ---
#    1 0 0 0   1   1 1 0 0   3   0 0 1 0   4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the vectors.
#
#    Input, integer BVEC1(N), BVEC2(N), the vectors to be added.
#
#    Output, integer BVEC3(N), the sum of the two input vectors.
#
#    Output, logical OVERFLOW, is true if the sum overflows.
#
  import numpy as np

  base = 2
  overflow = False

  bvec3 = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    bvec3[i] = bvec1[i] + bvec2[i]

  for i in range ( 0, n ):
    
    while ( base <= bvec3[i] ):
      bvec3[i] = bvec3[i] - base
      if ( i < n - 1 ):
        bvec3[i+1] = bvec3[i+1] + 1
      else:
        overflow = True

  return bvec3, overflow

def bvec_add_test ( ):

#*****************************************************************************80
#
## BVEC_ADD_TEST tests BVEC_ADD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10
  seed = 123456789
  test_num = 10

  print ( '' )
  print ( 'BVEC_ADD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BVEC_ADD adds binary vectors representing integers;' )
  print ( '' )
  print ( '        I        J        K = I + J   Kb = Ib + Jb' )
  print ( '' )

  for test in range ( 0, test_num ):
    
    i, seed = i4_uniform_ab ( -100, 100, seed )
    j, seed = i4_uniform_ab ( -100, 100, seed )

    print ( '  %8d  %8d' % ( i, j ), end = '' )

    k = i + j

    print ( '  %8d' % ( k ), end = '' )

    bvec1 = i4_to_bvec ( i, n )

    bvec2 = i4_to_bvec ( j, n )

    bvec3, overflow = bvec_add ( n, bvec1, bvec2 )

    k = bvec_to_i4 ( n, bvec3 )

    print ( '  %8d' % ( k ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BVEC_ADD_TEST:' )
  print ( '  Normal end of execution.' )
  return

def bvec_complement2 ( n, bvec1 ) :

#*****************************************************************************80
#
## BVEC_COMPLEMENT2 computes the two's complement of a binary vector.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 November 2006
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the vectors.
#
#    Input, integer BVEC1(N), the vector to be complemented.
#
#    Output, integer BVEC2(N), the two's complemented vector.
#
  import numpy as np

  base = 2

  bvec3 = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    bvec3[i] = ( base - 1 ) - bvec1[i]

  bvec4 = np.zeros ( n, dtype = np.int32 )
  bvec4[0] = 1

  bvec2, overflow = bvec_add ( n, bvec3, bvec4 )

  return bvec2

def bvec_complement2_test ( ):

#*****************************************************************************80
#
## BVEC_COMPLEMENT2_TEST tests BVEC_COMPLEMENT2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  seed = 123456789
  test_num = 5

  print ( '' )
  print ( 'BVEC_COMPLEMENT2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BVEC_COMPLEMENT2 returns the twos complement' )
  print ( '  of a (signed) binary vector;' )

  for test in range ( 0, test_num ):

    print ( '' )

    i, seed = i4_uniform_ab ( -100, 100, seed );
    bvec1 = i4_to_bvec ( i, n )
    bvec_print ( n, bvec1, '' )

    bvec2 = bvec_complement2 ( n, bvec1 )
    bvec_print ( n, bvec2, '' )

    j = bvec_to_i4 ( n, bvec2 )
#
#  Terminate.
#
  print ( '' )
  print ( 'BVEC_COMPLEMENT2_TEST' )
  print ( '  Normal end of execution.' )
  return

def bvec_mul ( n, bvec1, bvec2 ):

#*****************************************************************************80
#
## BVEC_MUL computes the product of two binary vectors.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the vectors.
#
#    Input, integer BVEC1(N), BVEC2(N), the vectors to be multiplied.
#
#    Output, integer BVEC3(N), the product of the two input vectors.
#
  import numpy as np

  base = 2
#
#  Copy the input.
#
  bveca = np.zeros ( n, dtype = np.int32 )
  bvecb = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    bveca[i] = bvec1[i]
    bvecb[i] = bvec2[i]
#
#  Record the sign of the product.
#  Make the factors positive.
#
  product_sign = 1

  if ( bveca[n-1] != 0 ):
    product_sign = - product_sign
    bveca = bvec_complement2 ( n, bveca )

  if ( bvecb[n-1] != 0 ):
    product_sign = - product_sign
    bvecb = bvec_complement2 ( n, bvecb )

  bvecc = np.zeros ( n, dtype = np.int32 )
#
#  Multiply.
#
  for i in range ( 0, n - 1 ):
    for j in range ( i, n - 1 ):
      bvecc[j] = bvecc[j] + bveca[i] * bvecb[j-i]
#
#  Take care of carries.
#
  for i in range ( 0, n - 1 ):

    carry = ( bvecc[i] // base )
    bvecc[i] = bvecc[i] - carry * base
#
#  Unlike the case of BVEC_ADD, we do NOT allow carries into
#  the N-th position when multiplying.
#
    if ( i < n - 2 ):
      bvecc[i+1] = bvecc[i+1] + carry
#
#  Take care of the sign of the product.
#
  if ( product_sign < 0 ):
    bvecc = bvec_complement2 ( n, bvecc )

  return bvecc

def bvec_mul_test ( ):

#*****************************************************************************80
#
## BVEC_MUL_TEST tests BVEC_MUL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 15
  seed = 123456789
  test_num = 10

  print ( '' )
  print ( 'BVEC_MUL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BVEC_MUL multiplies binary vectors representing integers;' )
  print ( '' )
  print ( '        I        J        I * J   BVEC_MUL' )
  print ( '' )

  for test in range ( 0, test_num ):
    
    i, seed = i4_uniform_ab ( -100, 100, seed )
    j, seed = i4_uniform_ab ( -100, 100, seed )

    print ( '  %8d  %8d' % ( i, j ), end = '' )

    k = i * j

    print ( '  %8d' % ( k ), end = '' )

    bvec1 = i4_to_bvec ( i, n )
    bvec2 = i4_to_bvec ( j, n )
    bvec3 = bvec_mul ( n, bvec1, bvec2 )
    l = bvec_to_i4 ( n, bvec3 )

    print ( '  %8d' % ( l ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BVEC_MUL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def bvec_next_grlex ( n, bvec ):

#*****************************************************************************80
#
## BVEC_NEXT generates the next binary vector in GRLEX order.
#
#  Discussion:
#
#    N = 3
#
#    Input      Output
#    -----      ------
#    0 0 0  =>  0 0 1
#    0 0 1  =>  0 1 0
#    0 1 0  =>  1 0 0
#    1 0 0  =>  0 1 1
#    0 1 1  =>  1 0 1
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
#    13 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, int N, the dimension of the vectors.
#
#    Input/output, int BVEC[N], on output, the successor to the
#    input vector.  
#

#
#  Initialize locations of 0 and 1.
#
  if ( bvec[0] == 0 ):
    z = 0
    o = -1
  else:
    z = -1
    o = 0
#
#  Moving from right to left, search for a "1", preceded by a "0".
#
  for i in range ( n - 1, 0, -1 ):
    if ( bvec[i] == 1 ):
      o = i
      if ( bvec[i-1] == 0 ):
        z = i - 1
        break
#
#  BVEC = 0
#
  if ( o == -1 ):
    bvec[n-1] = 1
#
#  01 never occurs.  So for sure, B(1) = 1.
#
  elif ( z == -1 ):

    s = 0
    for i in range ( 0, n ):
      s = s + bvec[i]

    if ( s == n ):

      for i in range ( 0, n ):
        bvec[i] = 0

    else:

      for i in range ( 0, n - s - 1 ):
        bvec[i] = 0

      for i in range ( n - s - 1, n ):
        bvec[i] = 1
      type ( n - s - 1 )
#
#  Found the rightmost "01" string.
#  Replace it by "10".
#  Shift following 1's to the right.
#
  else:

    bvec[z] = 1
    bvec[o] = 0

    s = 0
    for i in range ( o + 1, n ):
      s = s + bvec[i]

    for i in range ( o + 1, n - s ):
      bvec[i] = 0
    
    for i in range ( n - s, n ):
      bvec[i] = 1

  return bvec

def bvec_next_grlex_test ( ):

#*****************************************************************************80
#
## BVEC_NEXT_GRLEX_TEST tests BVEC_NEXT_GRLEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'BVEC_NEXT_GRLEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BVEC_NEXT_GRLEX computes binary vectors in GRLEX order.' )
  print ( '' )

  b = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, 17 ):
    print ( '  %2d:  ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( '%1d' % ( b[j] ), end = '' )
    print ( '' )
    b = bvec_next_grlex ( n, b )
#
#  Terminate.
#
  print ( '' )
  print ( 'BVEC_NEXT_GRLEX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def bvec_next ( n, bvec ):

#*****************************************************************************80
#
## BVEC_NEXT generates the next binary vector.
#
#  Discussion:
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
#    03 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, integer BVEC(N), the vector whose successor is desired.
#
#    Output, integer BVEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( bvec[i] == 0 ):
      bvec[i] = 1
      return bvec

    bvec[i] = 0

  return bvec

def bvec_next_test ( ):

#*****************************************************************************80
#
## BVEC_NEXT_TEST tests BVEC_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'BVEC_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BVEC_NEXT computes the "next" BVEC.' )
  print ( '' )

  b = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, 17 ):
    bvec_print ( n, b, '' )
    b = bvec_next ( n, b )
#
#  Terminate.
#
  print ( '' )
  print ( 'BVEC_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def bvec_print ( n, bvec, title ) :

#*****************************************************************************80
#
## BVEC_PRINT prints a binary integer vector, with an optional title.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#    The vector is printed "backwards", that is, the first entry
#    printed is BVEC(N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, integer BVEC(N), the vector to be printed.
#
#    Input, character ( len = * ) TITLE, a title to be printed first.
#    TITLE may be blank.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  for ihi in range ( n - 1, -1, -70 ):
    ilo = max ( ihi - 70, -1 )
    print ( '  ', end = '' )
    for i in range ( ihi, -1, ilo ):
      print ( '%1d' % ( bvec[i] ), end = '' )
    print ( '' )

  return

def bvec_print_test ( ):

#*****************************************************************************80
#
## BVEC_PRINT_TEST tests BVEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  bvec = np.array ( [ 1, 0, 0, 1, 0, 1, 1, 1, 0, 0 ] )

  print ( '' )
  print ( 'BVEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BVEC_PRINT prints a binary vector.' )

  bvec_print ( n, bvec, '  BVEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BVEC_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

def bvec_sub ( n, bvec1, bvec2 ):

#*****************************************************************************80
#
## BVEC_SUB subtracts two binary vectors.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Example:
#
#    N = 4
#
#    BVEC1    dec  BVEC2    dec  BVEC3    dec
#    -------  ---  -------  ---  -------  ---
#    0 0 1 0   4   1 0 0 0   1   1 1 0 0   3
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
#    Input, integer N, the length of the vectors.
#
#    Input, integer BVEC1(N), BVEC2(N), the vectors to be subtracted.
#
#    Output, integer BVEC4(N), the value of BVEC1 - BVEC2.
#
  bvec3 = bvec_complement2 ( n, bvec2 )

  bvec4, overflow = bvec_add ( n, bvec1, bvec3 )

  return bvec4

def bvec_sub_test ( ):

#*****************************************************************************80
#
## BVEC_SUB_TEST tests BVEC_SUB.
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
  import platform

  n = 10
  seed = 123456789
  test_num = 10

  print ( '' )
  print ( 'BVEC_SUB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BVEC_SUB subtracts binary vectors representing integers;' )
  print ( '' )
  print ( '        I        J        K = I - J   Kb = Ib - Jb' )
  print ( '' )

  for test in range ( 0, test_num ):
    
    i, seed = i4_uniform_ab ( -100, 100, seed )
    j, seed = i4_uniform_ab ( -100, 100, seed )

    print ( '  %8d  %8d' % ( i, j ), end = '' )

    k = i - j

    print ( '  %8d' % ( k ), end = '' )

    bvec1 = i4_to_bvec ( i, n )

    bvec2 = i4_to_bvec ( j, n )

    bvec3 = bvec_sub ( n, bvec1, bvec2 )

    k = bvec_to_i4 ( n, bvec3 )

    print ( '  %8d' % ( k ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BVEC_SUB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def bvec_test ( ):

#*****************************************************************************80
#
## BVEC_TEST tests the BVEC library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BVEC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the BVEC library.' )

  bvec_add_test ( )
  bvec_complement2_test ( )
  bvec_mul_test ( )
  bvec_next_test ( )
  bvec_next_grlex_test ( )
  bvec_print_test ( )
  bvec_sub_test ( )
  bvec_to_i4_test ( )
  bvec_uniform_test ( )
  i4_bclr_test ( )
  i4_bset_test ( )
  i4_btest_test ( )
  i4_to_bvec_test ( )
  i4_uniform_ab_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'BVEC_TEST:' )
  print ( '  Normal end of execution.' )
  return

def bvec_to_i4 ( n, bvec ) :

#*****************************************************************************80
#
## BVEC_TO_I4 makes an integer from a (signed) binary vector.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2**(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#  Example:
#
#         BVEC   binary  I
#    ----------  -----  --
#    1  2  3  4
#    ----------
#    1, 0, 0, 0       1  1
#    0, 1, 0, 0      10  2
#    0, 0, 1, 1    -100 -4
#    0, 0, 1, 0     100  4
#    1, 0, 0, 1    -111 -9
#    1, 1, 1, 1      -0  0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer BVEC(N), the binary representation.
#
#    Output, integer VALUE, the integer.
#
  import numpy as np

  base = 2

  bvec2 = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    bvec2[i] = bvec[i]

  i_sign = 1

  if ( bvec2[n-1] == base - 1 ):
    i_sign = -1
    bvec3 = bvec_complement2 ( n - 1, bvec2 )
    for i in range ( 0, n - 1 ):
      bvec2[i] = bvec3[i]

  value = 0
  for j in range ( n - 2, -1, -1 ):
    value = base * value + bvec2[j]

  value = i_sign * value

  return value

def bvec_to_i4_test ( ):

#*****************************************************************************80
#
## BVEC_TO_I4_TEST tests BVEC_TO_I4;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'BVEC_TO_I4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BVEC_TO_I4 converts a signed binary vector' )
  print ( '  to an integer;' )
  print ( '' )
  print ( '  I --> BVEC  -->  I' )
  print ( '' )

  for i in range ( -3, 11 ):
    bvec = i4_to_bvec ( i, n )
    i2 = bvec_to_i4 ( n, bvec )
    print ( '  %2d  ' % ( i ), end = '' )
    for j in range ( n - 1, -1, -1 ):
      print ( '%1d' % ( bvec[j] ), end = '' )
    print ( '  %2d' % ( i2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BVEC_TO_I4_TEST' )
  print ( '  Normal end of execution.' )
  return

def bvec_uniform ( n, seed ):

#*****************************************************************************80
#
## BVEC_UNIFORM returns a pseudorandom BVEC.
#
#  Discussion:
#
#    A BVEC is a vector of binary (0/1) values, representing an integer.
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
#    Output, integer BVEC(N), a pseudorandom binary vector.
#
#    Output, integer SEED, the updated seed.
#
  import numpy as np
  from sys import exit

  i4_huge      = 2147483647
  i4_huge_half = 1073741823

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'BVEC_UNIFORM - Fatal error!' )
    print ( '  Input value of SEED = 0.' )
    exit ( 'BVEC_UNIFORM - Fatal error!' )

  bvec = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    if ( i4_huge_half < seed ):
      bvec[i] = 0
    else:
      bvec[i] = 1

  return bvec, seed

def bvec_uniform_test ( ):

#*****************************************************************************80
#
## BVEC_UNIFORM_TEST tests BVEC_UNIFORM.
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
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'BVEC_UNIFORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BVEC_UNIFORM computes a random BVEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  print ( '' )
  for i in range ( 0, 10 ):
    v, seed = bvec_uniform ( n, seed )
    bvec_print ( n, v, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BVEC_UNIFORM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4_bclr ( i4, pos ):

#*****************************************************************************80
#
## I4_BCLR returns a copy of an I4 in which the POS-th bit is set to 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 June 20145
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Military Standard 1753,
#    FORTRAN, DoD Supplement To American National Standard X3.9-1978,
#    9 November 1978.
#
#  Parameters:
#
#    Input, integer I4, the integer to be tested.
#
#    Input, integer POS, the bit position, between 0 and 31.
#
#    Output, integer VALUE, a copy of I4, but with the POS-th bit
#    set to 0.
#
  i4_huge = 2147483647

  value = i4

  if ( pos < 0 ):
    pass
  elif ( pos < 31 ):

    sub = 1

    if ( 0 <= i4 ):
      j = i4
    else:
      j = ( i4_huge + i4 ) + 1

    for k in range ( 0, pos ):
      j = ( j // 2 )
      sub = sub * 2

    if ( ( j % 2 ) == 1 ):
      value = i4 - sub

  elif ( pos == 31 ):

    if ( i4 < 0 ):
      value = ( i4_huge + i4 ) + 1

  elif ( 31 < pos ):

    value = i4

  return value

def i4_bclr_test ( ):

#*****************************************************************************80
#
## I4_BCLR_TEST tests I4_BCLR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 2

  i4_test = np.array ( [ 101, -31 ], dtype = np.int32 )

  print ( '' )
  print ( 'I4_BCLR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_BCLR sets a given bit to 0.' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Working on I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     I4_BCLR(I4,Pos)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_bclr ( i4, pos )

      print ( '  %8d  %12d' % ( pos, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_BCLR_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_bset ( i4, pos ):

#*****************************************************************************80
#
## I4_BSET returns a copy of an I4 in which the POS-th bit is set to 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Military Standard 1753,
#    FORTRAN, DoD Supplement To American National Standard X3.9-1978,
#    9 November 1978.
#
#  Parameters:
#
#    Input, integer I4, the integer to be tested.
#
#    Input, integer POS, the bit position, between 0 and 31.
#
#    Output, integer VALUE, a copy of I4, but with the POS-th bit
#    set to 1.
#
  i4_huge = 2147483647

  value = i4

  if ( pos < 0 ):

    pass

  elif ( pos < 31 ):

    add = 1

    if ( 0 <= i4 ):
      j = i4
    else:
      j = ( i4_huge + i4 ) + 1

    for k in range ( 0, pos ):
      j = ( j // 2 )
      add = add * 2

    if ( ( j % 2 ) == 0 ):
      value = i4 + add

  elif ( pos == 31 ):

    if ( 0 < i4 ):
      value = - ( i4_huge - i4 ) - 1

  elif ( 31 < pos ):

    value = i4

  return value

def i4_bset_test ( ):

#*****************************************************************************80
#
## I4_BSET_TEST tests I4_BSET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 2

  i4_test = np.array ( [ 101, -31 ] )

  print ( '' )
  print ( 'I4_BSET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_BSET sets a given bit to 1.' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Working on I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     I4_BSET(I4,Pos)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_bset ( i4, pos )

      print ( '  %8d  %12d' % ( pos, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_BSET_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_btest ( i4, pos ):

#*****************************************************************************80
#
## I4_BTEST returns TRUE if the POS-th bit of an I4 is 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Military Standard 1753,
#    FORTRAN, DoD Supplement To American National Standard X3.9-1978,
#    9 November 1978.
#
#  Parameters:
#
#    Input, integer I4, the integer to be tested.
#
#    Input, integer POS, the bit position, between 0 and 31.
#
#    Output, logical VALUE, is TRUE if the POS-th bit of I4 is 1.
#
  from sys import exit

  i4_huge = 2147483647

  if ( pos < 0 ):

    print ( '' )
    print ( 'I4_BTEST - Fatal error!' )
    print ( '  POS < 0.' )
    exit ( 'I4_BTEST - Fatal error!' )

  elif ( pos < 31 ):

    if ( 0 <= i4 ):
      j = i4
    else:
      j = ( i4_huge + i4 ) + 1

    for k in range ( 0, pos ):
      j = ( j // 2 )

    if ( ( j % 2 ) == 0 ):
      value = False
    else:
      value = True

  elif ( pos == 31 ):

    if ( i4 < 0 ):
      value = True
    else:
      value = False

  elif ( 31 < pos ):

    print ( '' )
    print ( 'I4_BTEST - Fatal error!' )
    print ( '  31 < POS.' )
    exit ( 'I4_BTEST - Fatal error!' )

  return value

def i4_btest_test ( ):

#*****************************************************************************80
#
## I4_BTEST_TEST tests I4_BTEST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  i4_test = np.array ( [ 101, -31 ] )

  print ( '' )
  print ( 'I4_BTEST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_BTEST reports whether a given bit is 0 or 1.' )

  for test in range ( 0, 2 ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Analyze the integer I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     I4_BTEST(I4,POS)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_btest ( i4, pos )

      print ( '  %12d             %s' % ( pos, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_BTEST_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_to_bvec ( i, n ) :

#*****************************************************************************80
#
## I4_TO_BVEC makes a signed binary vector from an integer.
#
#  Discussion:
#
#    A BVEC is an integer vector of binary digits, intended to
#    represent an integer.  BVEC(1) is the units digit, BVEC(N-1)
#    is the coefficient of 2^(N-2), and BVEC(N) contains sign
#    information.  It is 0 if the number is positive, and 1 if
#    the number is negative.
#
#    To guarantee that there will be enough space for any
#    value of I, it would be necessary to set N = 32.
#
#  Example:
#
#     I       BVEC         binary
#    --  ----------------  ------
#     1  1, 0, 0, 0, 0, 0      1
#     2  0, 1, 0, 0, 0, 0     10
#     3  1, 1, 0, 0, 0, 0     11
#     4  0, 0, 1, 0, 0, 0    100
#     9  1, 0, 0, 1, 0, 0   1001
#    -9  1, 1, 1, 0, 1, 1  -1001 = 110111 (2's complement)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, an integer to be represented.
#
#    Input, integer N, the dimension of the vector.
#
#    Output, integer BVEC(N), the signed binary representation.
#
  import numpy as np

  base = 2
  i2 = abs ( i )

  bvec = np.zeros ( n, dtype = np.int32 )

  for j in range ( 0, n - 1 ):
    bvec[j] = ( i2 % base )
    i2 = ( i2 // base )

  bvec[n-1] = 0

  if ( i < 0 ):
    bvec2 = bvec_complement2 ( n, bvec )
    for j in range ( 0, n - 1 ):
      bvec[j] = bvec2[j]
    bvec[n-1] = 1

  return bvec

def i4_to_bvec_test ( ):

#*****************************************************************************80
#
## I4_TO_BVEC_TEST tests I4_TO_BVEC;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'I4_TO_BVEC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_TO_BVEC converts an integer to a ' )
  print ( '  signed binary vector.' )
  print ( '' )
  print ( '  I --> BVEC  -->  I' )
  print ( '' )

  for i in range ( -3, 11 ):
    bvec = i4_to_bvec ( i, n )
    i2 = bvec_to_i4 ( n, bvec )
    print ( '  %2d  ' % ( i ), end = '' )
    for j in range ( n - 1, -1, -1 ):
      print ( '%1d' % ( bvec[j] ), end = '' )
    print ( '  %2d' % ( i2 ) )
#
#  Terminate
#
  print ( '' )
  print ( 'I4_TO_BVEC_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## I4_UNIFORM_AB returns a scaled pseudorandom I4.
#
#  Discussion:
#
#    The pseudorandom number will be scaled to be uniformly distributed
#    between A and B.
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
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C, the randomly chosen integer.
#
#    Output, integer SEED, the updated seed.
#
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge; 

  if ( seed == 0 ):
    print ( '' )
    print ( 'I4_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'I4_UNIFORM_AB - Fatal error!' )

  k = floor ( seed / 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
  a = round ( a )
  b = round ( b )

  r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
    +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
  value = round ( r )

  value = max ( value, min ( a, b ) )
  value = min ( value, max ( a, b ) )
  value = int ( value )

  return value, seed

def i4_uniform_ab_test ( ):

#*****************************************************************************80
#
## I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
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
  import platform

  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_UNIFORM_AB computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 21 ):
    [ j, seed ] = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST:' )
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
  bvec_test ( )
  timestamp ( )

