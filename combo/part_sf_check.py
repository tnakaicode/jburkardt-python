#! /usr/bin/env python
#
def part_sf_check ( n, npart, a ):

#*****************************************************************************80
#
## PART_SF_CHECK checks a standard form partition of an integer.
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
#    Input, integer N, the integer to be partitioned.
#    N must be positive.
#
#    Input, integer NPART, the number of parts of the partition.
#    1 <= NPART <= N.
#
#    Input, integer A(NPART), contains the partition.
#    A(1) through A(NPART) contain the nonzero integers which
#    sum to N.  The entries must be in DESCENDING order.
#
#    Output, bool CHECK.
#    True, the data is legal.
#    False, the data is not legal.
#
  import numpy as np

  check = True

  if ( n < 1 ):
    check = False
    return check

  if ( npart < 1 or n < npart ):
    check = False
    return check
#
#  Every entry must lie between 1 and N.
#
  for i in range ( 0, npart ):
    if ( a[i] < 1 or n < a[i] ):
      check = False
      return check
#
#  The entries must be in descending order.
#
  for i in range ( 1, npart ):
    if ( a[i] > a[i-1] ):
      check = False
      return check
#
#  The entries must add up to N.
#
  if ( np.sum ( a ) != n ):
    check = False
    return check

  return check

def part_sf_check_test ( ):

#*****************************************************************************80
#
## PART_SF_CHECK_TEST tests PART_SF_CHECK.
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
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'PART_SF_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PART_SF_CHECK checks a standard form partition.' )
  
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      n = 0
      npart = 4
      a = np.array ( [ 6, 4, 4, 1 ] )
    elif ( test == 2 ):
      n = 15
      npart = 0
      a = np.array ( [ 6, 4, 4, 1 ] )
    elif ( test == 3 ):
      n = 15
      npart = 4
      a = np.array ( [ 16, 4, 4, -9 ] )
    elif ( test == 4 ):
      n = 15
      npart = 4
      a = np.array ( [ 1, 4, 4, 6 ] )
    elif ( test == 5 ):
      n = 15
      npart = 4
      a = np.array ( [ 6, 5, 4, 1 ] )
    elif ( test == 6 ):
      n = 15
      npart = 4
      a = np.array ( [ 6, 4, 4, 1 ] )

    print ( '' )
    print ( '  Partition in SF form.' )
    print ( '  Partition of N = %d' % ( n ) )
    print ( '  Number of parts NPART = %d' % ( npart ) )
    i4vec_transpose_print ( npart, a, '' )
    check = part_sf_check ( n, npart, a )
    print ( '  Check = %s' % ( check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PART_SF_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  part_sf_check_test ( )
  timestamp ( )
 
