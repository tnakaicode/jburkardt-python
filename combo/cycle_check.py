#! /usr/bin/env python
#
def cycle_check ( n, ncycle, t, index ):

#*****************************************************************************80
#
## CYCLE_CHECK checks a permutation in cycle form.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
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
#    Input, integer N, the number of items permuted.
#    N must be positive.
#
#    Input, integer NCYCLE, the number of cycles.
#    1 <= NCYCLE <= N.
#
#    Input, integer T(N), INDEX(NCYCLE), describes the permutation
#    as a collection of NCYCLE cycles.
#
#    Output, integer CHECK, error flag.
#    1, the data is legal.
#    0, the data is not legal.
#
  import numpy as np

  check = True
#
#  N must be at least 1.
#
  if ( n < 1 ):
    check = False
    return check
#
#  1 <= NCYCLE <= N.
#
  if ( ncycle < 1 or n < ncycle ):
    check = False
    return check
#
#  1 <= INDEX(I) <= N.
#
  for i in range ( 0, ncycle ):
    if ( index[i] < 1 or n < index[i] ):
      check = False
      return check
#
#  The INDEX values sum to N.
#
  if ( np.sum ( index ) != n ):
    check = False
    return check
#
#  1 <= T(I) <= N.
#
  for i in range ( 0, n ):
    if ( t[i] < 1 or n < t[i] ):
      check = 0
      return check
#
#  Verify that every value from 1 to N occurs in T.
#
  for iseek in range ( 1, n + 1 ):

    ifind = False

    for i in range ( 0, n ):
      if ( t[i] == iseek ):
        ifind = True
        break

    if ( not ifind ):
      check = False
      return check

  return check

def cycle_check_test ( ):

#*****************************************************************************80
#
## CYCLE_CHECK_TEST tests CYCLE_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'CYCLE_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CYCLE_CHECK checks a permutation in cycle form.' )
  
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      n = 0
      ncycle = 3
      t = np.array ( [ 5, 1, 3, 8, 6, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 3 ] )
    elif ( test == 2 ):
      n = 8
      ncycle = 0
      t = np.array ( [ 5, 1, 3, 8, 6, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 3 ] )
    elif ( test == 3 ):
      n = 8
      ncycle = 3
      t = np.array ( [ 5, 1, 3, 8, 6, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 2 ] )
    elif ( test == 4 ):
      n = 8
      ncycle = 3
      t = np.array ( [ 5, 1, 3, 12, 6, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 3 ] )
    elif ( test == 5 ):
      n = 8
      ncycle = 3
      t = np.array ( [ 5, 1, 3, 8, 5, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 3 ] )
    elif ( test == 6 ):
      n = 8
      ncycle = 3
      t = np.array ( [ 5, 1, 3, 8, 6, 2, 4, 7 ] )
      index = np.array ( [ 1, 4, 3 ] )

    print ( '' )
    print ( '  Permutation in cycle form:' )
    print ( '  Number of cycles is %d' % ( ncycle ) )
    print ( '' )
    jlo = 0
    for i in range ( 0, ncycle ):
      print ( '    ', end = '' )
      for j in range ( jlo, jlo + index[i] ):
        print ( '%4d'% ( t[j] ), end = '' )
      print ( '' )
      jlo = jlo + index[i]

    check = cycle_check ( n, ncycle, t, index )
    print ( '  Check = %2d' % ( check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CYCLE_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cycle_check_test ( )
  timestamp ( )
 
