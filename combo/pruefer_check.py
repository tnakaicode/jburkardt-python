#! /usr/bin/env python
#
def pruefer_check ( n, p ):

#*****************************************************************************80
#
## PRUEFER_CHECK checks a Pruefer code.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
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
#    Output, logical CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  if ( n < 3 ):
    check = False
    return check

  for i in range ( 0, n - 2 ):
    if ( p[i] < 1 or n < p[i] ):
      check = False
      return check

  return check

def pruefer_check_test ( ):

#*****************************************************************************80
#
## PRUEFER_CHECK_TEST tests PRUEFER_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'PRUEFER_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PRUEFER_CHECK checks a Pruefer code.' )
  print ( '' )
  print ( '     Check?   N      P(1:N-2)' )
  print ( '' )
  
  for test in range ( 1, 5 ):

    if ( test == 1 ):
      n = 2
      p = np.array ( [ ] )
    elif ( test == 2 ):
      n = 3
      p = np.array ( [ 1 ] )
    elif ( test == 3 ):
      n = 4
      p = np.array ( [ 5, 2 ] )
    elif ( test == 4 ):
      n = 5
      p = np.array ( [ 5, 1, 3 ] )

    check = pruefer_check ( n, p )
    print ( '      %5s  %2d:  ' % ( check, n ), end = '' )
    for i in range ( 0, n - 2 ):
      print ( '  %2d' % ( p[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PRUEFER_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pruefer_check_test ( )
  timestamp ( )
