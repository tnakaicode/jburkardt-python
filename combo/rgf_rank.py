#! /usr/bin/env python
#
def rgf_rank ( m, f ):

#*****************************************************************************80
#
## RGF_RANK ranks a restricted growth function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
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
#    Input, integer M, the domain of the RGF is the integers
#    from 1 to M.  M must be positive.
#
#    Input, integer F(M), the restricted growth function.
#
#    Output, integer RANK, the rank of the restricted growth
#    function.
#
  from rgf_check import rgf_check
  from rgf_g_table import rgf_g_table
  from sys import exit
#
#  Check.
#
  check = rgf_check ( m, f )

  if ( not check ):
    print ( '' )
    print ( 'RGF_RANK - Fatal error!' )
    print ( '  The input array is illegal!' )
    exit ( 'RGF_RANK - Fatal error!' )
#
#  Get the generalized restricted growth function table.
#
  d = rgf_g_table ( m )

  rank = 0
  j = 1
  for i in range ( 2, m + 1 ):
    rank = rank + ( f[i-1] - 1 ) * d[m-i,j]
    j = max ( j, f[i-1] )

  return rank

def rgf_rank_test ( ):

#*****************************************************************************80
#
## RGF_RANK_TEST tests RGF_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  m = 4

  print ( '' )
  print ( 'RGF_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RGF_RANK ranks restricted growth functions.' )

  f = np.array ( [ 1, 2, 1, 3 ] )
  i4vec_transpose_print ( m, f, '  Element to be ranked:' )

  rank = rgf_rank ( m, f )

  print ( '' )
  print ( '  The rank of the element is computed as %d:' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RGF_RANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rgf_rank_test ( )
  timestamp ( )
 
