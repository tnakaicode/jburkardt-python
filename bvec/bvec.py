#! /usr/bin/env python3
#
def bvec_add ( n, bvec1, bvec2 ):

#*****************************************************************************80
#
## bvec_add() adds two binary vectors.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer BVEC1(N), BVEC2(N), the vectors to be added.
#
#  Output:
#
#    integer BVEC3(N), the sum of the two input vectors.
#
#    logical OVERFLOW, is true if the sum overflows.
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
## bvec_add_test() tests bvec_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  n = 10
  test_num = 10

  print ( '' )
  print ( 'bvec_add_test():' )
  print ( '  bvec_add() adds binary vectors representing integers;' )
  print ( '' )
  print ( '        I        J        K = I + J   Kb = Ib + Jb' )
  print ( '' )

  for test in range ( 0, test_num ):
    
    i = rng.integers ( low = -100, high = 100, endpoint = True )
    j = rng.integers ( low = -100, high = 100, endpoint = True )

    print ( '  %8d  %8d' % ( i, j ), end = '' )

    k = i + j

    print ( '  %8d' % ( k ), end = '' )

    bvec1 = i4_to_bvec ( i, n )

    bvec2 = i4_to_bvec ( j, n )

    bvec3, overflow = bvec_add ( n, bvec1, bvec2 )

    k = bvec_to_i4 ( n, bvec3 )

    print ( '  %8d' % ( k ) )

  return

def bvec_complement2 ( n, bvec1 ) :

#*****************************************************************************80
#
## bvec_complement2() computes the two's complement of a binary vector.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 November 2006
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer BVEC1(N), the vector to be complemented.
#
#  Output:
#
#    integer BVEC2(N), the two's complemented vector.
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
## bvec_complement2_test() tests bvec_complement2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  n = 10
  test_num = 5

  print ( '' )
  print ( 'bvec_complement2_test():' )
  print ( '  bvec_complement2() returns the twos complement' )
  print ( '  of a (signed) binary vector;' )

  for test in range ( 0, test_num ):

    print ( '' )

    i = rng.integers ( low = -100, high = 100, endpoint = True )
    bvec1 = i4_to_bvec ( i, n )
    bvec_print ( n, bvec1, '' )

    bvec2 = bvec_complement2 ( n, bvec1 )
    bvec_print ( n, bvec2, '' )

    j = bvec_to_i4 ( n, bvec2 )

  return

def bvec_mul ( n, bvec1, bvec2 ):

#*****************************************************************************80
#
## bvec_mul() computes the product of two binary vectors.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer BVEC1(N), BVEC2(N), the vectors to be multiplied.
#
#  Output:
#
#    integer BVEC3(N), the product of the two input vectors.
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
#  Unlike the case of bvec_add, we do NOT allow carries into
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
## bvec_mul_test() tests bvec_mul().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  n = 15
  test_num = 10

  print ( '' )
  print ( 'bvec_mul_test():' )
  print ( '  bvec_mul() multiplies binary vectors representing integers;' )
  print ( '' )
  print ( '        I        J        I * J   bvec_mul' )
  print ( '' )

  for test in range ( 0, test_num ):
    
    i = rng.integers ( low = -100, high = 100, endpoint = True )
    j = rng.integers ( low = -100, high = 100, endpoint = True )

    print ( '  %8d  %8d' % ( i, j ), end = '' )

    k = i * j

    print ( '  %8d' % ( k ), end = '' )

    bvec1 = i4_to_bvec ( i, n )
    bvec2 = i4_to_bvec ( j, n )
    bvec3 = bvec_mul ( n, bvec1, bvec2 )
    l = bvec_to_i4 ( n, bvec3 )

    print ( '  %8d' % ( l ) )

  return

def bvec_next_grlex ( n, bvec ):

#*****************************************************************************80
#
## bvec_next_grlex() generates the next binary vector in GRLEX order.
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
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    int N, the dimension of the vectors.
#
#    int BVEC[N], the vector.  
#
#  Output:
#
#    int BVEC[N], the successor vector.

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
## bvec_next_grlex_test() tests bvec_next_grlex().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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

  n = 4

  print ( '' )
  print ( 'bvec_next_grlex_test():' )
  print ( '  bvec_next_grlex() computes binary vectors in GRLEX order.' )
  print ( '' )

  b = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, 17 ):
    print ( '  %2d:  ' % ( i ), end = '' )
    for j in range ( 0, n ):
      print ( '%1d' % ( b[j] ), end = '' )
    print ( '' )
    b = bvec_next_grlex ( n, b )

  return

def bvec_next ( n, bvec ):

#*****************************************************************************80
#
## bvec_next() generates the next binary vector.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    integer BVEC(N), the vector whose successor is desired.
#
#  Output:
#
#    integer BVEC(N), the successor to the input vector.
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
## bvec_next_test() tests bvec_next().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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

  n = 4

  print ( '' )
  print ( 'bvec_next_test():' )
  print ( '  bvec_next() computes the "next" BVEC.' )
  print ( '' )

  b = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, 17 ):
    bvec_print ( n, b, '' )
    b = bvec_next ( n, b )

  return

def bvec_print ( n, bvec, title ) :

#*****************************************************************************80
#
## bvec_print() prints a binary integer vector, with an optional title.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    integer BVEC(N), the vector to be printed.
#
#    character TITLE, a title to be printed first.
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
## bvec_print_test() tests bvec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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

  n = 10
  bvec = np.array ( [ 1, 0, 0, 1, 0, 1, 1, 1, 0, 0 ] )

  print ( '' )
  print ( 'bvec_print_test():' )
  print ( '  bvec_print() prints a binary vector.' )

  bvec_print ( n, bvec, '  BVEC:' )

  return

def bvec_sub ( n, bvec1, bvec2 ):

#*****************************************************************************80
#
## bvec_sub() subtracts two binary vectors.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the length of the vectors.
#
#    integer BVEC1(N), BVEC2(N), the vectors to be subtracted.
#
#  Output:
#
#    integer BVEC4(N), the value of BVEC1 - BVEC2.
#
  bvec3 = bvec_complement2 ( n, bvec2 )

  bvec4, overflow = bvec_add ( n, bvec1, bvec3 )

  return bvec4

def bvec_sub_test ( ):

#*****************************************************************************80
#
## bvec_sub_test() tests bvec_sub().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 December 2014
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  n = 10
  test_num = 10

  print ( '' )
  print ( 'bvec_sub_test():' )
  print ( '  bvec_sub() subtracts binary vectors representing integers;' )
  print ( '' )
  print ( '        I        J        K = I - J   Kb = Ib - Jb' )
  print ( '' )

  for test in range ( 0, test_num ):
    
    i = rng.integers ( low = -100, high = 100, endpoint = True )
    j = rng.integers ( low = -100, high = 100, endpoint = True )

    print ( '  %8d  %8d' % ( i, j ), end = '' )

    k = i - j

    print ( '  %8d' % ( k ), end = '' )

    bvec1 = i4_to_bvec ( i, n )

    bvec2 = i4_to_bvec ( j, n )

    bvec3 = bvec_sub ( n, bvec1, bvec2 )

    k = bvec_to_i4 ( n, bvec3 )

    print ( '  %8d' % ( k ) )

  return

def bvec_test ( ):

#*****************************************************************************80
#
## bvec_test() tests bvec().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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

  print ( '' )
  print ( 'bvec_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test bvec().' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'bvec_test():' )
  print ( '  Normal end of execution.' )
  return

def bvec_to_i4 ( n, bvec ) :

#*****************************************************************************80
#
## bvec_to_i4() makes an integer from a (signed) binary vector.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer BVEC(N), the binary representation.
#
#  Output:
#
#    integer VALUE, the integer.
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
## bvec_to_i4_test() tests bvec_to_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 September 2018
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'bvec_to_i4_test():' )
  print ( '  bvec_to_i4() converts a signed binary vector' )
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

  return

def bvec_uniform ( n, rng ):

#*****************************************************************************80
#
## bvec_uniform() returns a pseudorandom BVEC.
#
#  Discussion:
#
#    A BVEC is a vector of binary (0/1) values, representing an integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the vector.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer BVEC(N), a pseudorandom binary vector.
#
  import numpy as np

  bvec = rng.integers ( low = 0, high = 1, size = n, endpoint = True )

  return bvec

def bvec_uniform_test ( ):

#*****************************************************************************80
#
## bvec_uniform_test() tests bvec_uniform().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )
  n = 10

  print ( '' )
  print ( 'bvec_uniform_test():' )
  print ( '  bvec_uniform() computes a random BVEC.' )
  print ( '' )

  for i in range ( 0, 10 ):
    v = bvec_uniform ( n, rng )
    bvec_print ( n, v, '' )

  return

def i4_bclr ( i4, pos ):

#*****************************************************************************80
#
## i4_bclr() returns a copy of an I4 in which the POS-th bit is set to 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer I4, the integer to be tested.
#
#    integer POS, the bit position, between 0 and 31.
#
#  Output:
#
#    integer VALUE, a copy of I4, but with the POS-th bit
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
## i4_bclr_test() tests i4_bclr().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  test_num = 2

  i4_test = np.array ( [ 101, -31 ], dtype = np.int32 )

  print ( '' )
  print ( 'i4_bclr_test():' )
  print ( '  i4_bclr() sets a given bit to 0.' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Working on I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     i4_bclr(I4,Pos)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_bclr ( i4, pos )

      print ( '  %8d  %12d' % ( pos, j ) )

  return

def i4_bset ( i4, pos ):

#*****************************************************************************80
#
## i4_bset() returns a copy of an I4 in which the POS-th bit is set to 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer I4, the integer to be tested.
#
#    integer POS, the bit position, between 0 and 31.
#
#  Output:
#
#    integer VALUE, a copy of I4, but with the POS-th bit
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
## i4_bset_test() tests i4_bset().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  test_num = 2

  i4_test = np.array ( [ 101, -31 ] )

  print ( '' )
  print ( 'i4_bset_test():' )
  print ( '  i4_bset() sets a given bit to 1.' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Working on I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     i4_bset(I4,Pos)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_bset ( i4, pos )

      print ( '  %8d  %12d' % ( pos, j ) )

  return

def i4_btest ( i4, pos ):

#*****************************************************************************80
#
## i4_btest() returns TRUE if the POS-th bit of an I4 is 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer I4, the integer to be tested.
#
#    integer POS, the bit position, between 0 and 31.
#
#  Output:
#
#    logical VALUE, is TRUE if the POS-th bit of I4 is 1.
#
  i4_huge = 2147483647

  if ( pos < 0 ):

    print ( '' )
    print ( 'i4_btest(): Fatal error!' )
    print ( '  POS < 0.' )
    raise Exception ( 'i4_btest(): Fatal error!' )

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
    print ( 'i4_btest - Fatal error!' )
    print ( '  31 < POS.' )
    raise Exception ( 'i4_btest - Fatal error!' )

  return value

def i4_btest_test ( ):

#*****************************************************************************80
#
## i4_btest_test() tests i4_btest().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  i4_test = np.array ( [ 101, -31 ] )

  print ( '' )
  print ( 'i4_btest_test():' )
  print ( '  i4_btest() reports whether a given bit is 0 or 1.' )

  for test in range ( 0, 2 ):

    i4 = i4_test[test]

    print ( '' )
    print ( '  Analyze the integer I4 = %d' % ( i4 ) )
    print ( '' )
    print ( '       Pos     i4_btest(I4,POS)' )
    print ( '' )

    for pos in range ( 0, 32 ):
  
      j = i4_btest ( i4, pos )

      print ( '  %12d             %s' % ( pos, j ) )

  return

def i4_to_bvec ( i, n ) :

#*****************************************************************************80
#
## i4_to_bvec() makes a signed binary vector from an integer.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, an integer to be represented.
#
#    integer N, the dimension of the vector.
#
#  Output:
#
#    integer BVEC(N), the signed binary representation.
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
## i4_to_bvec_test() tests i4_to_bvec().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 September 2018
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'i4_to_bvec_test():' )
  print ( '  i4_to_bvec() converts an integer to a signed binary vector.' )
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

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  bvec_test ( )
  timestamp ( )

