#! /usr/bin/env python
#
def perm_ascend ( n, p ):

#*****************************************************************************80
#
## PERM_ASCEND computes the longest ascending subsequence of permutation.
#
#  Discussion:
#
#    Although this routine is intended to be applied to a permutation,
#    it will work just as well for an arbitrary vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 June 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the permutation.
#
#    Input, integer P(N), the permutation to be examined.
#
#    Output, integer LENGTH, the length of the longest increasing subsequence.
#
#    Output, integer SUB(LENGTH), a longest increasing subsequence of A.
#
  import numpy as np

  top = np.zeros ( n + 1, dtype = np.int32 )
  top_prev = np.zeros ( n + 1, dtype = np.int32 )

  length = 0

  if ( n <= 0 ):
    sub = np.zeros ( length )
    return length, sub

  for i in range ( 0, n ):

    k = 0

    for j in range ( 1, length + 1 ):
      if ( p[i] <= p[top[j]] ):
        k = j
        break

    if ( k == 0 ):
      length = length + 1
      k = length

    top[k] = i
    top_prev[i] = top[k-1]
#
#  Construct the subsequence.
#
  sub = np.zeros ( length, dtype = np.int32 )

  j = top[length]
  sub[length-1] = p[j]

  for i in range ( length - 2, -1, -1 ):
    j = top_prev[j]
    sub[i] = p[j]

  return length, sub

def perm_ascend_test ( ):

#*****************************************************************************80
#
## PERM_ASCEND_TEST tests PERM_ASCEND.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_print import i4vec_print
  from perm0_print import perm0_print

  n = 9
  p = np.array ( [ 1,2,8,5,6,7,4,3,0 ], dtype = np.int32 )

  print ( '' )
  print ( 'PERM_ASCEND_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_ASCEND determines the length of the longest' )
  print ( '  increasing subsequence in a permutation.' )

  perm0_print ( n, p, '  The permutation:' )

  length, subseq = perm_ascend ( n, p )

  print ( '' )
  print ( '  The longest increasing subsequence has length %d' % ( length ) )

  i4vec_print ( length, subseq, '  A longest increasing subsequence:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_ASCEND_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_ascend_test ( )
  timestamp ( )

