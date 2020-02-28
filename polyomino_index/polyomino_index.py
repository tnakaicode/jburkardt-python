#! /usr/bin/env python3
#
def polyomino_index ( m, n, p ):

#*****************************************************************************80
#
## POLYOMINO_INDEX assigns an index to each nonzero entry of a polyomino.
#
#  Example:
#
#    P = 
#      1 0 1 1
#      1 1 1 0
#      0 1 1 0
#
#    PIN =
#      1 0 2 3
#      4 5 6 0
#      0 7 8 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 May 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the representation
#    of the polyomino P.
#
#    Input, integer P(M,N), the polyomino.  It is assumed that every entry
#    is a 0 or a 1.
#
#    Output, integer PIN(M,N), the index of each nonzero entry.
#
  import numpy as np

  pin = np.zeros ( [ m, n ] )

  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( p[i,j] != 0 ):
        k = k + 1
        pin[i,j] = k

  return pin

def polyomino_index_test ( ):

#*****************************************************************************80
#
## POLYOMINO_INDEX_TEST tests POLYOMINO_INDEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'POLYOMINO_INDEX_TEST' )
  print ( '  POLYOMINO_INDEX assigns an index to each nonzero entry' )
  print ( '  of a polyomino.' )

  m = 3
  n = 4

  p = np.array ( [ \
    [ 1, 0, 1, 1 ], \
    [ 1, 1, 1, 0 ], \
    [ 0, 1, 1, 0 ] ] )

  polyomino_print ( m, n, p, '  The polyomino P:' )

  pin = polyomino_index ( m, n, p )

  print ( '' )
  print ( '  PIN: Index vector for P:' )
  print ( '' )
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      print ( ' %d' % ( pin[i,j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYOMINO_INDEX_TEST' )
  print ( '  Normal end of execution.' )
  return

def polyomino_print ( m, n, p, label ):

#*****************************************************************************80
#
## POLYOMINO_PRINT prints a polyomino.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the representation
#    of the polyomino P.
#
#    Input, integer P(M,N), a matrix of 0's and 1's representing the 
#    polyomino.  The matrix should be "tight", that is, there should be a
#    1 in row 1, and in column 1, and in row M, and in column N.
#
#    Input, string LABEL, a title for the polyomino.
#
  print ( '' )
  print ( label )
  print ( '' )
  if ( m <= 0 or n <= 0 ):
    print ( '  [ Null matrix ]' )
  else:
    for i in range ( 0, m ):
      for j in range ( 0, n ):
        print ( ' %d' % ( p[i,j] ) ),
      print ( '' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None


if ( __name__ == '__main__' ):
  timestamp ( )
  polyomino_index_test ( )
  timestamp ( )
