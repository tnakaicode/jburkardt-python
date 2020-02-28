#! /usr/bin/env python
#
def bal_seq_to_tableau ( n, t ):

#*****************************************************************************80
#
## BAL_SEQ_TO_TABLEAU converts a balanced sequence to a 2 by N tableau.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2015
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
#    Input, integer N, the number of 0's (and 1's) in the sequence.
#    N must be positive.
#
#    Input, integer T(2*N), a balanced sequence.
#
#    Output, integer TAB(2,N), a 2 by N tableau.
#
  import numpy as np
  from bal_seq_check import bal_seq_check
  from sys import exit
#
#  Check.
#
  check = bal_seq_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'BAL_SEQ_TO_TABLEAU - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'BAL_SEQ_TO_TABLEAU - Fatal error!' )

  c = np.zeros ( 2, dtype = np.int32 )
  tab = np.zeros ( [ 2, n ], dtype = np.int32 )

  for i in range ( 0, 2 * n ):
    r = t[i] + 1
    c[r-1] = c[r-1] + 1
    tab[r-1,c[r-1]-1] = i + 1

  return tab

def bal_seq_to_tableau_test ( ):

#*****************************************************************************80
#
## BAL_SEQ_TO_TABLEAU_TEST tests BAL_SEQ_TO_TABLEAU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from bal_seq_unrank import bal_seq_unrank
  from i4mat_print import i4mat_print
  from i4vec_transpose_print import i4vec_transpose_print

  n = 4

  print ( '' )
  print ( 'BAL_SEQ_TO_TABLEAU_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BAL_SEQ_TO_TABLEAU converts a balanced' )
  print ( '  sequence to a tableau' )
#
#  Pick a "random" balanced sequence.
#
  rank = 7

  t = bal_seq_unrank ( rank, n )

  i4vec_transpose_print ( 2 * n, t, '  Balanced sequence:' )
#
#  Convert to a tableau.
#
  tab = bal_seq_to_tableau ( n, t )

  i4mat_print ( 2, n, tab, '  Tableau:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'BAL_SEQ_TO_TABLEAU_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bal_seq_to_tableau_test ( )
  timestamp ( )
 
