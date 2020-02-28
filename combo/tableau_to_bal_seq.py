#! /usr/bin/env python
#
def tableau_to_bal_seq ( n, tab ):

#*****************************************************************************80
#
#% TABLEAU_TO_BAL_SEQ converts a 2 by N tableau to a balanced sequence.
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
#    Input, integer N, the number of 0's (and 1's) in the sequence.
#    N must be positive.
#
#    Input, integer TAB(2,N), a 2 by N tableau.
#
#    Output, integer T(2*N), a balanced sequence.
#
  import numpy as np
  from sys import exit
  from tableau_check import tableau_check
#
#  Check.
#
  check = tableau_check ( n, tab )

  if ( not check ):
    print ( '' )
    print ( 'TABLEAU_TO_BAL_SEQ - Fatal error!' )
    print ( '  The input array is illegal.' )
    error ( 'TABLEAU_TO_BAL_SEQ - Fatal error!' )

  t = np.zeros ( 2 * n )

  for i in range ( 0, 2 ):
    for j in range ( 0, n ):
      t[tab[i,j]-1] = i

  return t

def tableau_to_bal_seq_test ( ):

#*****************************************************************************80
#
## TABLEAU_TO_BAL_SEQ_TEST tests TABLEAU_TO_BAL_SEQ.
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
  import numpy as np
  import platform
  from i4mat_print import i4mat_print
  from i4vec_transpose_print import i4vec_transpose_print

  n = 4

  print ( '' )
  print ( 'TABLEAU_TO_BAL_SEQ_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TABLEAU_TO_BAL_SEQ converts a tableau' )
  print ( '  to a balanced sequence.' )

  tab = np.array ( [ \
    [ 1, 2, 5, 6 ], \
    [ 3, 4, 7, 8 ] ] )

  i4mat_print ( 2, n, tab, '  Tableau:' )

  t = tableau_to_bal_seq ( n, tab )

  i4vec_transpose_print ( 2 * n, t, '  Balanced sequence:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TABLEAU_TO_BAL_SEQ_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tableau_to_bal_seq_test ( )
  timestamp ( )
 
