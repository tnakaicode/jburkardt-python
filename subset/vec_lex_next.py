#! /usr/bin/env python
#
def vec_lex_next ( dim_num, base, a, more ):

#*****************************************************************************80
#
## VEC_LEX_NEXT generates vectors in lex order.
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
#    19 May 2015
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
  if ( not more ):

    for i in range ( 0, dim_num ):
      a[i] = 0
    more = True

  else:
      
    more = False
    for i in range ( dim_num - 1, -1, -1 ):

      a[i] = a[i] + 1

      if ( a[i] < base ):
        more = True
        break

      a[i] = 0

  return a, more

def vec_lex_next_test ( ):

#*****************************************************************************80
#
## VEC_LEX_NEXT_TEST tests VEC_LEX_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'VEC_LEX_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VEC_LEX_NEXT generates all DIM_NUM-vectors' )
  print ( '  in lex order in a given base BASE.' )
  
  dim_num = 3
  base = 3
  a = np.zeros ( dim_num )
  more = False

  print ( '' )
  print ( '  The spatial dimension DIM_NUM = %d' % ( dim_num ) )
  print ( '  The base BASE =                 %d' % ( base ) )
  print ( '' )

  while ( True ):

    a, more = vec_lex_next ( dim_num, base, a, more )

    if ( not more ):
      break

    i4vec_transpose_print ( dim_num, a, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'VEC_LEX_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  vec_lex_next_test ( )
  timestamp ( )
