#! /usr/bin/env python
#
def ksubset_colex_check ( k, n, t ):

#*****************************************************************************80
#
## KSUBSET_COLEX_CHECK checks a K subset in colex form.
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
#    Input, integer K, the number of elements each K subset must
#    have. 0 <= K <= N.
#
#    Input, integer N, the number of elements in the master set.
#    0 <= N.
#
#    Input, integer T(K), describes a K subset.  T(I) is the I-th
#    element of the K subset.  The elements must be listed in
#    DESCENDING order.
#
#    Output, integer CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True

  if ( n < 0 ):
    check = False
    return check

  if ( k < 0 or n < k ):
    check = False
    return check
#
#  Check that entries are in descending order, and between 1 and N.
#
  tmax = n + 1

  for i in range ( 0, k ):

    if ( t[i] <= 0 or tmax <= t[i] ):
      check = False
      return check

    tmax = t[i]

  return check

def ksubset_colex_check_test ( ):

#*****************************************************************************80
#
## KSUBSET_COLEX_CHECK_TEST tests KSUBSET_COLEX_CHECK.
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
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'KSUBSET_COLEX_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUBSET_COLEX_CHECK checks a K subset of an N set.' )
  
  for test in range ( 1, 8 ):

    if ( test == 1 ):
      k = -1
      n = 5
      s = np.array ( [ ] )
    elif ( test == 2 ):
      k = 3
      n = 0
      s = np.array ( [ 5, 3, 2 ] )
    elif ( test == 3 ):
      k = 3
      n = 5
      s = np.array ( [ 5, 2, 3 ] )
    elif ( test == 4 ):
      k = 3
      n = 5
      s = np.array ( [ 7, 3, 2 ] )
    elif ( test == 5 ):
      k = 3
      n = 5
      s = np.array ( [ 5, 3, 2 ] )
    elif ( test == 6 ):
      k = 0
      n = 5
      s = np.array ( [ ] )
    elif ( test == 7 ):
      k = 0
      n = 0
      s = np.array ( [ ] )

    check = ksubset_colex_check ( k, n, s )
    i4vec_transpose_print ( k, s, '  Subset:' )
    print ( '  N = %d, K = %d' % ( n, k ) )
    print ( '  Check = %s' %  ( check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUBSET_COLEX_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksubset_colex_check_test ( )
  timestamp ( )
 
