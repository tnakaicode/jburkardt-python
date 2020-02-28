#! /usr/bin/env python
#
def tableau_check ( n, tab ):

#*****************************************************************************80
#
## TABLEAU_CHECK checks a 2 by N tableau.
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
#    Input, integer N, the number of columns in the tableau.
#    N must be positive.
#
#    Input, integer TAB(2,N), a 2 by N tableau.
#
#    Output, integer CHECK.
#    1, the data is legal.
#    0, the data is not legal.
#
  check = True

  if ( n < 1 ):
    check = False
    return check
#
#  The entries must be between 1 and 2*N.
#
  for i in range ( 0, 2 ):
    for j in range ( 0, n ):
      if ( tab[i,j] < 1 or 2 * n < tab[i,j] ):
        check = False
        return check
#
#  The entries must be increasing to the right.
#
  for i in range ( 0, 2 ):
    for j in range ( 1, n ):
      if ( tab[i,j] <= tab[i,j-1] ):
        check = False
        return check
#
#  The entries must be increasing down.
#
  for j in range ( 0, n ):
    if ( tab[1,j] <= tab[0,j] ):
      check = False
      return check

  return check

def tableau_check_test ( ):

#*****************************************************************************80
#
## TABLEAU_CHECK_TEST tests TABLEAU_CHECK.
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

  print ( '' )
  print ( 'TABLEAU_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TABLEAU_CHECK checks a 2xN tableau.' )
  print ( '' )
  print ( '  Check?' )
  print ( '' )
  
  for test in range ( 1, 6 ):

    if ( test == 1 ):
      n = 0
      t = np.array ( [ \
        [ ],
        [ ] ] )
    elif ( test == 2 ):
      n = 4
      t = np.array ( [ \
        [ 1, 2, 3, 4 ], \
        [ 2, 4, 7, 9 ] ] )
    elif ( test == 3 ):
      n = 4
      t = np.array ( [ \
        [ 1, 3, 5, 3 ], \
        [ 2, 4, 5, 3 ] ] )
    elif ( test == 4 ):
      n = 4
      t = np.array ( [ \
        [ 1, 3, 4, 5 ], \
        [ 2, 4, 5, 3 ] ] )
    elif ( test == 5 ):
      n = 4
      t = np.array ( [ \
        [ 1, 3, 6, 7 ], \
        [ 3, 4, 7, 8 ] ] )

    print ( '' )
    check = tableau_check ( n, t )
    print ( '      Check = %2d' % ( check ) )
    i4mat_print ( 2, n, t, '  Tableau:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TABLEAU_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tableau_check_test ( )
  timestamp ( )
 
