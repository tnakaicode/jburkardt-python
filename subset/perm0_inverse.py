#! /usr/bin/env python
#
def perm0_inverse ( n, p1 ):

#*****************************************************************************80
#
## PERM0_INVERSE inverts a permutation of (0,...,N-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects being permuted.
#
#    Input, integer P1(N), the permutation.
#
#    Output, integer P2(N), the inverse permutation
#
  import numpy as np
  from sys import exit
  from i4_sign import i4_sign
  from perm0_check import perm0_check

  if ( n <= 0 ):
    print ( '' )
    print ( 'PERM0_INVERSE - Fatal error!' )
    print ( '  Input value of N = %d' % ( n ) )
    exit ( 'PERM0_INVERSE - Fatal error!' )

  check = perm0_check ( n, p1 )

  if ( not check ):
    print ( '' )
    print ( 'PERM0_INVERSE - Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    exit ( 'PERM0_INVERSE - Fatal error!' )

  p2 = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    p2[i] = p1[i] + 1

  s = 1

  for i in range ( 1, n + 1 ):

    i1 = p2[i-1]

    while ( i < i1 ):
      i2 = p2[i1-1]
      p2[i1-1] = - i2
      i1 = i2

    s = - i4_sign ( p2[i-1] )
    p2[i-1] = i4_sign ( s ) * abs ( p2[i-1] )

  for i in range ( 1, n + 1 ):

    i1 = - p2[i-1]

    if ( 0 <= i1 ):

      i0 = i

      while ( True ):

        i2 = p2[i1-1]
        p2[i1-1] = i0

        if ( i2 < 0 ):
          break

        i0 = i1
        i1 = i2

  for i in range ( 0, n ):
    p2[i] = p2[i] - 1

  return p2

def perm0_inverse_test ( ):

#*****************************************************************************80
#
## PERM0_INVERSE_TEST tests PERM0_INVERSE
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from perm0_print import perm0_print

  n = 7
  p1 = np.array ( [ 3, 2, 4, 0, 6, 5, 1 ], dtype = np.int32 )

  print ( '' )
  print ( 'PERM0_INVERSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_INVERSE inverts a permutation of (0,...,N-1)' )

  perm0_print ( n, p1, '  The original permutation:' )
 
  p2 = perm0_inverse ( n, p1 )
 
  perm0_print ( n, p2, '  The inverted permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_INVERSE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_inverse_test ( )
  timestamp ( )

