#! /usr/bin/env python
#
def rgf_unrank ( rank, m ):

#*****************************************************************************80
#
## RGF_UNRANK returns the restricted growth function of a given rank.
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
#    Input, integer RANK, the rank of the restricted growth
#    function.
#
#    Input, integer M, the domain of the RGF is the integers
#    from 1 to M.  M must be positive.
#
#    Output, integer F(M), the restricted growth function.
#
  import numpy as np
  from rgf_enum import rgf_enum
  from rgf_g_table import rgf_g_table
  from sys import exit
#
#  Check.
#
  if ( m < 1 ):
    print ( '' )
    print ( 'RGF_UNRANK - Fatal error!' )
    print ( '  Input M is illegal.' )
    exit ( 'RGF_UNRANK - Fatal error!' )

  nrgf = rgf_enum ( m )

  if ( rank < 0 or nrgf < rank ):
    print ( '' )
    print ( 'RGF_UNRANK - Fatal error!' )
    print ( '  The input rank is illegal.' )
    exit ( 'RGF_UNRANK - Fatal error!' )
#
#  Get the generalized restricted growth function table.
#
  d = rgf_g_table ( m )

  f = np.zeros ( m )
  j = 1
  f[0] = 1

  for i in range ( 2, m + 1 ):

    if ( j * d[m-i,j] <= rank ):
      f[i-1] = j + 1
      rank = rank - j * d[m-i,j]
      j = j + 1
    else:
      f[i-1] = 1 + ( rank // d[m-i,j] )
      rank = ( rank % d[m-i,j] )

  return f

def rgf_unrank_test ( ):

#*****************************************************************************80
#
## RGF_UNRANK_TEST tests RGF_UNRANK.
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
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  m = 4

  print ( '' )
  print ( 'RGF_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RGF_UNRANK unranks restricted growth functions.' )

  rank = 7

  f = rgf_unrank ( rank, m )

  i4vec_transpose_print ( m, f, '  The element of rank 7' )
#
#  Terminate.
#
  print ( '' )
  print ( 'RGF_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rgf_unrank_test ( )
  timestamp ( )
 
