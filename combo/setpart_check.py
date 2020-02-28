#! /usr/bin/env python
#
def setpart_check ( m, nsub, s, index ):

#*****************************************************************************80
#
## SETPART_CHECK checks a set partition.
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
#    Input, integer M, the number of elements of the set.
#    M must be positive.
#
#    Input, integer NSUB, the number of nonempty subsets into
#    which the set is partitioned.  1 <= NSUB <= M.
#
#    Input, integer S(M), contains the integers from 1 to M,
#    grouped into subsets as described by INDEX.
#
#    Input, integer INDEX(NSUB), lists the location in S of the
#    last element of each subset.  Thus, the elements of subset 1
#    are S(1) through S(INDEX(1)), the elements of subset 2
#    are S(INDEX(1)+1) through S(INDEX(2)) and so on.
#
#    Output, bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  check = True
#
#  Check M.
#
  if ( m < 1 ):
    check = False
    return check
#
#  Check NSUB.
#
  if ( nsub < 1 or m < nsub ):
    check = False
    return check
#
#  Check INDEX.
#
  imin = 0
  for i in range ( 0, nsub ):
    if ( index[i] <= imin or m < index[i] ):
      check = False
      return check
    imin = index[i]
#
#  Check the elements of S.
#
  for i in range ( 0, m ):

    if ( s[i] <= 0 or m < s[i] ):
      check = False
      return check

    for j in range ( 0, i ):
      if ( s[j] == s[i] ):
        check = False
        return check

  return check

def setpart_check_test ( ):

#*****************************************************************************80
#
## SETPART_CHECK_TEST tests SETPART_CHECK.
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
  print ( 'SETPART_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SETPART_CHECK checks a set partition.' )
  
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      m = 0
      nsub = 3
      s = np.array ( [ 3, 6, 1, 4, 7, 2, 5, 8 ] )
      index = np.array ( [ 2, 5, 8 ] )
    elif ( test == 2 ):
      m = 8
      nsub = 0
      s = np.array ( [ 3, 6, 1, 4, 7, 2, 5, 8 ] )
      index = np.array ( [ 2, 5, 8 ] )
    elif ( test == 3 ):
      m = 8
      nsub = 3
      s = np.array ( [ 3, 6, 1, 4, 7, 2, 5, 8 ] )
      index = np.array ( [ 2, 8, 5 ] )
    elif ( test == 4 ):
      m = 8
      nsub = 3
      s = np.array ( [ 3, 6, 1, 4, 9, 2, 5, 8 ] )
      index = np.array ( [ 2, 5, 8 ] )
    elif ( test == 5 ):
      m = 8
      nsub = 3
      s = np.array ( [ 3, 6, 1, 4, 6, 2, 5, 8 ] )
      index = np.array ( [ 2, 5, 8 ] )
    elif ( test == 6 ):
      m = 8
      nsub = 3
      s = np.array ( [ 3, 6, 1, 4, 7, 2, 5, 8 ] )
      index = np.array ( [ 2, 5, 8 ] )

    print ( '' )
    print ( '  The set partition' )
    print ( '  M = %d' % ( m ) )
    print ( '  NSUB = %d' % ( nsub ) )
    print ( '' )
    jlo = 0
    for i in range ( 0, nsub ):
      for j in range ( jlo, index[i] ):
        print ( '%4d' % ( s[j] ), end = '' )
      print ( '' )
      jlo = index[i]

    check = setpart_check ( m, nsub, s, index )
    print ( '  Check = %s' % ( check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SETPART_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  setpart_check_test ( )
  timestamp ( )
 
