#! /usr/bin/env python3
#
def combination_lock_test ( ):

#*****************************************************************************80
#
## COMBINATION_LOCK_TEST test COMBINATION_LOCK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'COMBINATION_LOCK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  A combination lock consists of M dials,' )
  print ( '  each having N symbols.' )
  print ( '  We seek to determine the combination C.' )

  m = 4
  n = 5
  c = np.array ( [ 1, 2, 3, 4 ] )
#
#  Report on the problem data.
#
  print ( '' )
  print ( '  The number of dials is M = %d' % ( m ) )
  print ( '  The number of symbols is N = %d' % ( n ) )
  print ( '  The number of possible combinations is M^N = %d' % ( n ** m ) )
  i4vec_print ( m, c, '  The combination:' )

  step = combination_lock ( m, n, c )

  if ( step == -1 ):
    print ( '' )
    print ( '  The combination was not found.' )
  else:
    print ( '' )
    print ( '  The combination was found in %d steps' % ( step ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COMBINATION_LOCK_TEST' )
  print ( '  Normal end of execution.' )
  return

def combination_lock ( m, n, c ):

#*****************************************************************************80
#
## COMBINATION_LOCK determines the combination of a lock.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of dials.
#
#    Input, integer N, the number of symbols on each dial.
#    We assume the symbols are the integers 0 to N-1.
#
#    Input, integer C(M), the combination.
#
#    Output, integer STEP, the step on which the combination 
#    was found.  A value of -1 means the combination was not found.
#
  import numpy as np
#
#  Starting with the guess [ 0, 0, ... 0],
#  generate every possible combination, in order, and try it.
#
  more = False
  a = np.zeros ( m )
  step = 0

  while ( True ):
  
    a, more = combination_next ( m, n, a, more )

    if ( not more ):
      print ( '' )
      print ( '  The program did NOT find the combination!' )
      step = -1
      return step

    step = step + 1

    if ( i4vec_eq ( m, a, c ) ):
      label = '  The combination was found on step %d' % ( step )
      i4vec_print ( m, c, label )
      return step

def combination_next ( dim_num, base, a, more ):

#*****************************************************************************80
#
## COMBINATION_NEXT generates lock combinations in lex order.
#
#  Discussion:
#
#    The vectors are produced in lexical order, starting with
#    (0,0,...,0),
#    (0,0,...,1),
#    ...
#    (BASE-1,BASE-1,...,BASE-1).
#
#  Example:
#
#    DIM_NUM = 2,
#    BASE = 3
#
#    0   0
#    0   1
#    0   2
#    1   0
#    1   1
#    1   2
#    2   0
#    2   1
#    2   2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Parameters:
#
#    Input, integer DIM_NUM, the size of the vectors to be used.
#
#    Input, integer BASE, the base to be used.  BASE = 2 will
#    give vectors of 0's and 1's, for instance.
#
#    Input, integer A(DIM_NUM), except on the first call, this should
#    be the output value of A on the last call.
#
#    Input, logical MORE, should be FALSE on the first call, and
#    thereafter should be the output value of MORE from the previous call.  
#
#    Output, integer A(DIM_NUM), the next vector.
#
#    Output, logical MORE, is TRUE if another vector was computed.
#    If MORE is FALSE on return, then ignore the output value A, and
#    stop calling the routine.
#
  import numpy as np

  if (  not more ):

    a[0:dim_num] = 0
    more = True

  else:
      
    for i in range ( dim_num - 1, -1, -1 ):

      a[i] = a[i] + 1

      if ( a[i] < base ):
        return a, more

      a[i] = 0

    more = False

  return a, more

def i4vec_eq ( n, a, b ):

#*****************************************************************************80
#
## I4VEC_EQ is TRUE if two I4VEC's are equal.
#
#  Example:
#
#    A = ( 9, 7, 7, 3, 2, 1, -8 )
#    B = ( 9, 7, 6, 3, 2, 1, -8 )
#    I4VEC_EQ = FALSE
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the arrays.
#
#    Input, integer A(N), B(N), the arrays to be compared.
#
#    Output, logical VALUE, is TRUE if the arrays are equal.
#
  value = True

  for i in range ( 0, n - 1 ):
    if ( a[i] != b[i] ):
      value = False
      break

  return value

def i4vec_eq_test ( ):

#*****************************************************************************80
#
## I4VEC_EQ_TEST tests I4VEC_EQ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec2_print import i4vec2_print

  n = 4
  test_num = 4

  a_test = np.array ( [ \
    [ 1, 3, 2, 4 ], \
    [ 2, 2, 2, 2 ], \
    [ 1, 2, 2, 4 ], \
    [ 1, 2, 3, 4 ] ] )

  b_test = np.array ( [ \
    [ 1, 3, 2, 4 ], \
    [ 2, 2, 1, 2 ], \
    [ 4, 1, 1, 3 ], \
    [ 1, 2, 3, 4 ] ] )

  print ( '' )
  print ( 'I4VEC_EQ_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_EQ is TRUE if two I4VECs are equal.' )

  for i in range ( 0, test_num ):

    a = a_test[i,0:n].copy ( )
    b = b_test[i,0:n].copy ( )

    i4vec2_print ( n, a, b, '  Vectors A and B:' )

    value = i4vec_eq ( n, a, b )

    print ( '  I4VEC_EQ(A,B) = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_EQ_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## I4VEC_PRINT prints an I4VEC.
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
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_test ( ):

#*****************************************************************************80
#
## I4VEC_PRINT_TEST tests I4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_PRINT prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_PRINT_TEST:' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  combination_lock_test ( )
  timestamp ( )
