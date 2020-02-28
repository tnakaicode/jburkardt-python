#! /usr/bin/env python
#
def subset_colex_unrank ( rank, n ):

#*****************************************************************************80
#
## SUBSET_COLEX_UNRANK computes the subset of given colexicographic rank.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
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
#    Input, integer RANK, the rank of the subset.
#
#    Input, integer N, the number of items in the master set.
#    N must be positive.
#
#    Output, integer T(N), the subsetof the given rank.
#    If T(I) = 0, item I is not in the subset; if T(I) = 1, item I is
#    in the subset.
#
  import numpy as np
  from subset_enum import subset_enum
  from sys import exit
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'SUBSET_COLEX_UNRANK - Fatal error!' )
    print ( '  Input N is illegal.' )
    exit ( 'SUBSET_COLEX_UNRANK - Fatal error!' )

  nsub = subset_enum ( n )

  if ( rank < 0 or nsub < rank ):
    print ( '' )
    print ( 'SUBSET_COLEX_UNRANK - Fatal error!' )
    print ( '  The input rank is illegal.' )
    exit ( 'SUBSET_COLEX_UNRANK - Fatal error!' )

  t = np.zeros ( n )

  for i in range ( 0, n ):
    t[i] = ( rank % 2 )
    rank = ( rank // 2 )

  return t

def subset_colex_unrank_test ( ):

#*****************************************************************************80
#
## SUBSET_COLEX_UNRANK_TEST tests SUBSET_COLEX_UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 5

  print ( '' )
  print ( 'SUBSET_COLEX_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_COLEX_UNRANK unranks subsets of a set,' )
  print ( '  using the colexicographic ordering.' )

  rank = 10

  t = subset_colex_unrank ( rank, n )

  i4vec_transpose_print ( n, t, '  The subset of rank 10:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_COLEX_UNRANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_colex_unrank_test ( )
  timestamp ( )
 
