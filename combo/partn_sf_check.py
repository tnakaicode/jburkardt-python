#! /usr/bin/env python
#
def partn_sf_check ( n, nmax, npart, a ):

#*****************************************************************************80
#
## PARTN_SF_CHECK checks an SF partition of an integer with largest entry NMAX.
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
#    Input, integer NMAX, the value of the largest entry.
#    1 <= NMAX <= N.
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

  if ( nmax < 1 or n < nmax ):
    check = False
    return check

  if ( npart < 1 or n < npart ):
    check = False
    return check
#
#  Entry 1 must be NMAX.
#
  if ( a[0] != nmax ):
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
    if ( a[i-1] < a[i] ):
      check = False
      return check
#
#  The entries must add up to N.
#
  asum = 0
  for i in range ( 0, npart ):
    asum = asum + a[i]
  if ( asum != n ):
    check = False
    return check

  return check

def partn_sf_check_test ( ):

#*****************************************************************************80
#
## PARTN_SF_CHECK_TEST tests PARTN_SF_CHECK.
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
  from i4vec_transpose_print import i4vec_transpose_print

  print ( '' )
  print ( 'PARTN_SF_CHECK TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PARTN_SF_CHECK checks a standard form partition' )
  print ( '  of N with largest entry NMAX.' )

  for test in range ( 1, 8 ):

    if ( test == 1 ):
      n = 0
      nmax = 6
      npart = 4
      a = np.array ( [ 6, 4, 4, 1 ] )
    elif ( test == 2 ):
      n = 15
      nmax = 6
      npart = 0
      a = np.array ( [ 6, 4, 4, 1 ] )
    elif ( test == 3 ):
      n = 15
      nmax = 6
      npart = 4
      a = np.array ( [ 6, 6, 6, -3 ] )
    elif ( test == 4 ):
      n = 15
      nmax = 6
      npart = 4
      a = np.array ( [ 8, 4, 2, 1 ] )
    elif ( test == 5 ):
      n = 15
      nmax = 6
      npart = 4
      a = np.array ( [ 1, 4, 4, 6 ] )
    elif ( test == 6 ):
      n = 15
      nmax = 6
      npart = 4
      a = np.array ( [ 6, 5, 4, 1 ] )
    elif ( test == 7 ):
      n = 15
      nmax = 6
      npart = 4
      a = np.array ( [ 6, 4, 4, 1 ] )

    print ( '' )
    print ( '  Partition in SF form.' )
    print ( '  Partition of N = %d' % ( n ) )
    print ( '  Maximum entry NMAX = %d' % ( nmax ) )
    print ( '  Number of parts NPART = %d' % ( npart ) )
    i4vec_transpose_print ( npart, a, '' )
    check = partn_sf_check ( n, nmax, npart, a )
    print ( '  Check = %s' % ( check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PARTN_SF_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  partn_sf_check_test ( )
  timestamp ( )
 
