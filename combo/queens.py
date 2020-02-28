#! /usr/bin/env python
#
def queens ( n, iarray, k, nstack, istack, maxstack ):

#*****************************************************************************80
#
## QUEENS finds possible positions for the K-th nonattacking queen.
#
#  Discussion:
#
#    The chessboard is N by N, and is being filled one column at a time,
#    with a tentative solution to the nonattacking queen problem.  So
#    far, K-1 rows have been chosen, and we now need to provide a list
#    of all possible rows that might be used in column K.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the total number of queens to place, and
#    the length of a side of the chessboard.
#
#    Input, integer IARRAY(N).  The first K-1 entries of IARRAY
#    record the rows into which queens have already been placed.
#
#    Input, integer K, the column for which we need possible
#    row positions for the next queen.
#
#    Input/output, integer NSTACK, the current length of stack.
#    On output, this has been updated.
#
#    Input/output, integer ISTACK(MAXSTACK).  On output, we have added
#    the candidates, and the number of candidates, to the end of the
#    stack.
#
#    Input, integer MAXSTACK, maximum dimension of ISTACK.
#
  ncan = 0

  for irow in range ( 1, n + 1 ):
#
#  If row IROW has already been used, that is it.
#
    row = False

    for jcol in range ( 1, k ):
      if ( iarray[jcol-1] == irow ):
        row = True

    if ( not row ):

      diag = False

      for jcol in range ( 1, k ):
 
        if ( irow == ( iarray[jcol-1] + k - jcol ) or \
             irow == ( iarray[jcol-1] - ( k - jcol ) ) ):

          diag = True

      if ( not diag ):
        ncan = ncan + 1
        nstack = nstack + 1
        istack[nstack-1] = irow

  nstack = nstack + 1
  istack[nstack-1] = ncan

  return nstack, istack

def queens_test ( ):

#*****************************************************************************80
#
## QUEENS_TEST tests QUEENS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from backtrack import backtrack
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'QUEENS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  QUEENS produces nonattacking queens' )
  print ( '  on a chessboard using a backtrack search.' )
  print ( '' )

  n = 8
  iarray = np.zeros ( n )
  indx = 0
  k = -1
  nstack = -1
  maxstack = n * n
  stack = np.zeros ( maxstack )

  while ( True ):

    n, iarray, indx, k, nstack, stack = backtrack ( n, iarray, \
      indx, k, nstack, stack, maxstack )

    if ( indx == 1 ):

      i4vec_transpose_print ( n, iarray, '' )

    elif ( indx == 2 ):

      nstack, stack = queens ( n, iarray, k, nstack, stack, maxstack )

    else:

      break
#
#  Terminate.
#
  print ( '' )
  print ( 'QUEENS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  queens_test ( )
  timestamp ( )
 
