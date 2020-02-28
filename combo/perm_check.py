#! /usr/bin/env python
#
def perm_check ( n, p ):

#*****************************************************************************80
#
## PERM_CHECK checks that a vector represents a permutation.
#
#  Discussion:
#
#    The routine verifies that each of the integers from 1
#    to N occurs among the N entries of the permutation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries.
#
#    Input, integer P(N), the array to check.
#
#    Output, integer CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  for seek in range ( 1, n + 1 ):

    check = False

    for find in range ( 0, n ):
      if ( p[find] == seek ):
        check = True
        break

    if ( not check ):
      return check

  return check

def perm_check_test ( ):

#*****************************************************************************80
#
## PERM_CHECK_TEST tests PERM_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'PERM_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_CHECK checks a permutation.' )
  
  for test in range ( 1, 4 ):

    if ( test == 1 ):
      n = 5
      s = np.array ( [ 5, 1, 8, 3, 4 ] )
    elif ( test == 2 ):
      n = 5
      s = np.array ( [ 5, 1, 4, 3, 4 ] )
    elif ( test == 3 ):
      n = 5
      s = np.array ( [ 5, 1, 2, 3, 4 ] )

    check = perm_check ( n, s )
    i4vec_transpose_print ( n, s, '  Permutation:' )
    print ( '  Check = %s' % ( check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_check_test ( )
  timestamp ( )
 
