#! /usr/bin/env python
#
def subset_check ( n, t ):

#*****************************************************************************80
#
## SUBSET_CHECK checks a subset.
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
#    Input, integer N, the number of elements in the master set.
#    N must be positive.
#
#    Input, integer T(N), the subset.  If T(I) = 0, item I is
#    not in the subset; if T(I) = 1, item I is in the subset.
#
#    Output, integer CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  if ( n < 1 ):
    check = False
    return check

  for i in range ( 0, n ):

    if ( t[i] != 0 and t[i] != 1 ):
      check = False
      return check

  return check

def subset_check_test ( ):

#*****************************************************************************80
#
## SUBSET_CHECK_TEST tests SUBSET_CHECK.
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
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'SUBSET_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_CHECK checks a subset.' )
  
  for test in range ( 1, 4 ):

    if ( test == 1 ):
      n = 0
      s = np.array ( [] )
    elif ( test == 2 ):
      n = 3
      s = np.array ( [ 1, 2, 0 ] )
    elif ( test == 3 ):
      n = 5
      s = np.array ( [ 1, 0, 0, 1, 0 ] )

    check = subset_check ( n, s )
    i4vec_transpose_print ( n, s, '  Subset:' )
    print ( '  Check = %s' % ( check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_check_test ( )
  timestamp ( )
 
