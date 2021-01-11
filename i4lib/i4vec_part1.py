#! /usr/bin/env python
#
def i4vec_part1 ( n, npart ):

#*****************************************************************************80
#
## I4VEC_PART1 partitions an integer N into NPART parts.
#
#  Example:
#
#    Input:
#
#      N = 17, NPART = 5
#
#    Output:
#
#      X = ( 13, 1, 1, 1, 1 ).
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
#    1 <= NPART <= N.
#
#    Output, integer X(NPART), the partition of N.  The entries of
#    X add up to N.  X(1) = N + 1 - NPART, and all other entries
#    are equal to 1.
#
  import numpy as np
  from sys import exit

  if ( npart < 1 or n < npart ):
    print ( '' )
    print ( 'I4VEC_PART1 - Fatal error!' )
    print ( '  The input value of NPART is illegal.' )
    exit ( 'I4VEC_PART1 - Fatal error!' )

  x = np.ones ( npart )

  x[0] = n + 1 - npart

  return x

def i4vec_part1_test ( ):

#*****************************************************************************80
#
## I4VEC_PART1_TEST tests I4VEC_PART1.
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
  print ( 'I4VEC_PART1_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_PART1 partitions an integer N into NPART parts.' )

  n = 17
  npart = 5

  print ( '' )
  print ( '  Partition N = %d into NPART = %d parts:' % ( n, npart ) )
  print ( '' )

  x = i4vec_part1 ( n, npart )

  for i in range ( 0, npart ):
    print ( '  %2d  %2d' % ( i, x[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_PART1_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_part1_test ( )
  timestamp ( )
