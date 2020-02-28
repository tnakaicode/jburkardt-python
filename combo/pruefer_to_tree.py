#! /usr/bin/env python
#
def pruefer_to_tree ( n, p ):

#*****************************************************************************80
#
## PRUEFER_TO_TREE converts a Pruefer code to a tree.
#
#  Discussion:
#
#    The original code attempts to tack on an extra entry to P.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the number of nodes in the tree.
#    N must be at least 3.
#
#    Input, integer P(N-2), the Pruefer code for the tree.
#
#    Output, integer T(2,N-1), describes the edges of the tree
#    as pairs of nodes.
#
  import numpy as np
  from pruefer_check import pruefer_check
#
#  Check.
#
  check = pruefer_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PRUEFER_TO_TREE - Fatal error!' )
    print ( '  Input array is illegal.' )
    exit ( 'PRUEFER_TO_TREE - Fatal error!' )
#
#  Initialize the tree to 0.
#
  t = np.zeros ( [ 2, n - 1 ], dtype = np.int32 )

  d = np.ones ( n, dtype = np.int32 )

  for i in range ( 0, n - 2 ):
    d[p[i]-1] = d[p[i]-1] + 1

  for i in range ( 0, n - 1 ):

    x = n
    while ( d[x-1] != 1 ):
      x = x - 1

    if ( i == n - 2 ):
      y = 1
    else:
      y = p[i]

    d[x-1] = d[x-1] - 1
    d[y-1] = d[y-1] - 1

    t[0,i] = x
    t[1,i] = y

  return t

def pruefer_to_tree_test ( ):

#*****************************************************************************80
#
## PRUEFER_TO_TREE_TEST tests PRUEFER_TO_TREE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_uniform_ab import i4_uniform_ab
  from i4mat_print import i4mat_print
  from i4vec_print import i4vec_print
  from pruefer_enum import pruefer_enum
  from pruefer_unrank import pruefer_unrank

  n = 5
  seed = 123456789

  print ( '' )
  print ( 'PRUEFER_TO_TREE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PRUEFER_TO_TREE converts a Pruefer code to a tree;' )

  pruefer_num = pruefer_enum ( n )

  i4_lo = 0
  i4_hi = pruefer_num - 1

  for test in range ( 0, 5 ):
#
#  Pick a "random" Pruefer code.
#
    rank, seed = i4_uniform_ab ( i4_lo, i4_hi, seed )

    p = pruefer_unrank ( rank, n )

    i4vec_print ( n - 2, p, '  Pruefer code' )
#
#  Convert the Pruefer code to a tree.
#
    t = pruefer_to_tree ( n, p )

    i4mat_print ( 2, n - 1, t, '  Edge list of tree:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PRUEFER_TO_TREE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pruefer_to_tree_test ( )
  timestamp ( )
 
