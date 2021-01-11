#! /usr/bin/env python
#
def i4vec_part2 ( n, npart ):

#*****************************************************************************80
#
## I4VEC_PART2 partitions an integer N into NPART nearly equal parts.
#
#  Example:
#
#    Input:
#
#      N = 17, NPART = 5
#
#    Output:
#
#      X = ( 4, 4, 3, 3, 3 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the integer to be partitioned.  N
#    may be positive, zero, or negative.
#
#    Input, integer NPART, the number of entries in the array.
#    1 <= NPART
#
#    Output, integer X(NPART), the partition of N.  The entries of
#    X add up to N.  The entries of X are either all equal, or
#    differ by at most 1.  The entries of X all have the same sign
#    as N, and the "largest" entries occur first.
#
  import numpy as np
  from sys import exit

  if ( npart < 1 ):
    print ( '' )
    print ( 'I4VEC_PART2 - Fatal error!' )
    print ( '  The input value of NPART is illegal.' )
    error ( 'I4VEC_PART2 - Fatal error!' )

  x = np.zeros ( npart )

  if ( 0 < n ):

    j = 0
    for i in range ( 0, n ):
      x[j] = x[j] + 1
      j = j + 1
      if ( npart <= j ):
        j = 0

  elif ( n < 0 ):

    j = 0
    for i in range ( n - 1, -1, -1 ):
      x[j] = x[j] - 1
      j = j + 1
      if ( npart <= j ):
        j = 0

  return x

def i4vec_part2_test ( ):

#*****************************************************************************80
#
## I4VEC_PART2_TEST tests I4VEC_PART2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4VEC_PART2_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_PART2 partitions an integer N into NPART parts.' )

  n = 17
  npart = 5

  print ( '' )
  print ( '  Partition N = %d into NPART = %d parts:' % ( n, npart ) )
  print ( '' )

  x = i4vec_part2 ( n, npart )

  for i in range ( 0, npart ):
    print ( '  %2d  %2d' % ( i, x[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_PART2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_part2_test ( )
  timestamp ( )
